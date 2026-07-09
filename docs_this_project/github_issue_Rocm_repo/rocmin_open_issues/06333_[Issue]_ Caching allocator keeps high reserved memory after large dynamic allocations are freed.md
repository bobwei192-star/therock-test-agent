# [Issue]: Caching allocator keeps high reserved memory after large dynamic allocations are freed

- **Issue #:** 6333
- **State:** open
- **Created:** 2026-06-04T07:48:29Z
- **Updated:** 2026-06-04T07:48:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/6333

### Problem Description

# [ROCm][PyTorch] Caching allocator keeps high reserved memory after large dynamic allocations are freed

## Summary

On ROCm/PyTorch, large dynamic BF16 allocations can leave `torch.cuda.memory_reserved()` much higher than current `torch.cuda.memory_allocated()` after tensors are deleted. The extra reserved memory is mostly held as large-pool cached memory, not as live tensors.

We first observed this in a VERL RL training workload that OOMed very quickly. During step-by-step memory instrumentation, `torch.cuda.memory_allocated()` dropped after some training phases, but `torch.cuda.memory_reserved()` stayed high and kept increasing in a stair-step pattern. To isolate the behavior from VERL, Ray, vLLM, model weights, and distributed training, the repro below uses only standalone PyTorch tensor allocations and frees.

The repro shows:

- current `allocated` can drop to zero after tensors are deleted;
- `reserved` remains high;
- most extra reserved memory is `cached_large_pool_gb`;
- `inactive_split_large_pool_gb` is much smaller than `cached_large_pool_gb`, so split fragmentation does not appear to be the primary cause;
- `torch.cuda.empty_cache()` releases the extra reserved memory without changing peak allocated memory.

## Environment

Docker image used for the reference run:

```text
rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.9.1
```

PyTorch version printed by the reference run:

```text
torch 2.9.1+rocm7.2.4.git39497456
```

The repro requires an AMD GPU with ROCm driver support and Docker access to `/dev/kfd` and `/dev/dri`.

## Minimal Reproduction Script

Save the following as `repro_rocm_allocator_reserved.py`. This is a single-file, framework-free repro. It does not require VERL, Ray, vLLM, distributed training, or model weights.

```python
#!/usr/bin/env python3
import argparse
import gc
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import torch

LAST_INFO: dict[str, Any] | None = None
SEQ = 0


def to_gib(value: int | float) -> float:
    return float(value) / 1024**3


def parse_csv_ints(value: str) -> list[int]:
    return [int(v.strip()) for v in value.split(",") if v.strip()]


def gib_tensor(size_gib: float, dtype: torch.dtype, device: torch.device) -> torch.Tensor:
    element_size = torch.empty((), dtype=dtype).element_size()
    numel = int(size_gib * 1024**3 / element_size)
    return torch.empty((numel,), dtype=dtype, device=device)


def memory_info() -> dict[str, Any]:
    device_id = torch.cuda.current_device()
    info: dict[str, Any] = {
        "allocated_gb": to_gib(torch.cuda.memory_allocated(device_id)),
        "reserved_gb": to_gib(torch.cuda.memory_reserved(device_id)),
        "max_allocated_gb": to_gib(torch.cuda.max_memory_allocated(device_id)),
        "max_reserved_gb": to_gib(torch.cuda.max_memory_reserved(device_id)),
    }
    info["cached_gb"] = info["reserved_gb"] - info["allocated_gb"]

    stats = torch.cuda.memory_stats(device_id)
    byte_keys = {
        "allocated_bytes.large_pool.current": "allocated_large_pool_gb",
        "reserved_bytes.large_pool.current": "reserved_large_pool_gb",
        "inactive_split_bytes.large_pool.current": "inactive_split_large_pool_gb",
    }
    count_keys = {
        "segment.large_pool.current": "segments_large_pool",
        "num_alloc_retries": "num_alloc_retries",
        "num_sync_all_streams": "num_sync_all_streams",
        "num_ooms": "num_ooms",
    }
    for source, target in byte_keys.items():
        if source in stats:
            info[target] = to_gib(stats[source])
    for source, target in count_keys.items():
        if source in stats:
            info[target] = int(stats[source])

    info["cached_large_pool_gb"] = info.get("reserved_large_pool_gb", 0.0) - info.get(
        "allocated_large_pool_gb", 0.0
    )
    return info


def delta(info: dict[str, Any], previous: dict[str, Any] | None, key: str) -> float:
    if previous is None:
        return 0.0
    return float(info.get(key, 0.0)) - float(previous.get(key, 0.0))


def log_memory(stage: str, detail: str = "", events: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    global LAST_INFO, SEQ
    info = memory_info()
    SEQ += 1
    event: dict[str, Any] = {
        "seq": SEQ,
        "ts": datetime.now().isoformat(timespec="milliseconds"),
        "monotonic_s": time.monotonic(),
        "stage": stage,
        "detail": detail,
        **info,
        "delta_reserved_gb": delta(info, LAST_INFO, "reserved_gb"),
        "delta_allocated_gb": delta(info, LAST_INFO, "allocated_gb"),
    }
    LAST_INFO = dict(info)
    if events is not None:
        events.append(event)

    print(
        "MEM "
        f"seq={event['seq']} stage={stage} {detail} "
        f"reserved={event.get('reserved_gb', 0.0):.3f}GB "
        f"allocated={event.get('allocated_gb', 0.0):.3f}GB "
        f"cached_large={event.get('cached_large_pool_gb', 0.0):.3f}GB "
        f"inactive_split_large={event.get('inactive_split_large_pool_gb', 0.0):.3f}GB "
        f"d_reserved={event.get('delta_reserved_gb', 0.0):.3f}GB "
        f"segments_large={event.get('segments_large_pool', 0)} "
        f"retries={event.get('num_alloc_retries', 0)} "
        f"sync_all_streams={event.get('num_sync_all_streams', 0)}",
        flush=True,
    )
    return event


def print_max(events: list[dict[str, Any]], field: str) -> None:
    row = max(events, key=lambda r: r.get(field, 0.0))
    print(
        f"max {field}={row.get(field, 0.0):.3f} "
        f"seq={row.get('seq')} stage={row.get('stage')} {row.get('detail', '')}"
    )


def run(args: argparse.Namespace) -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("ROCm/CUDA device is required")

    print("torch", torch.__version__)
    print("cuda_available", torch.cuda.is_available())
    print("device_count", torch.cuda.device_count())
    print("device0", torch.cuda.get_device_name(0))

    dtype = {"bf16": torch.bfloat16, "fp16": torch.float16, "fp32": torch.float32}[args.dtype]
    device = torch.device("cuda")
    tokens_list = parse_csv_ints(args.tokens)
    comm_stream = torch.cuda.Stream()
    aux_stream = torch.cuda.Stream()
    events: list[dict[str, Any]] = []

    torch.cuda.reset_peak_memory_stats()
    log_memory("start", events=events)

    for round_idx in range(args.rounds):
        for micro_idx, tokens in enumerate(tokens_list):
            detail = f"round={round_idx} micro={micro_idx} tokens={tokens}"
            log_memory("micro:entry", detail, events)

            logits = torch.empty((tokens, args.vocab_size), dtype=dtype, device=device)
            log_memory("micro:after_logits_alloc", detail, events)

            with torch.cuda.stream(aux_stream):
                flat_buffer = gib_tensor(args.flat_buffer_gb, dtype, device)
            log_memory("micro:after_flat_buffer_alloc", detail, events)

            with torch.cuda.stream(comm_stream):
                reduce_buffer = gib_tensor(args.reduce_buffer_gb, dtype, device)
                small_reduce = gib_tensor(args.small_reduce_gb, dtype, device)
            log_memory("micro:after_reduce_buffers_alloc", detail, events)

            del reduce_buffer, small_reduce, flat_buffer, logits
            gc.collect()
            log_memory("micro:after_delete_refs", detail, events)

            if args.empty_cache_after_step:
                torch.cuda.synchronize()
                torch.cuda.empty_cache()
                log_memory("micro:after_empty_cache", detail, events)

    torch.cuda.synchronize()
    log_memory("end:after_synchronize", events=events)
    torch.cuda.empty_cache()
    log_memory("end:after_empty_cache", events=events)

    if args.output_jsonl:
        path = Path(args.output_jsonl)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            for row in events:
                f.write(json.dumps(row, sort_keys=True) + "\n")

    print(f"events={len(events)}")
    for field in [
        "reserved_gb",
        "allocated_gb",
        "max_reserved_gb",
        "max_allocated_gb",
        "cached_gb",
        "cached_large_pool_gb",
        "inactive_split_large_pool_gb",
        "segments_large_pool",
        "num_alloc_retries",
        "num_sync_all_streams",
    ]:
        print_max(events, field)

    print("\nreserved jumps >= 1.000 GB:")
    for row in events:
        if row.get("delta_reserved_gb", 0.0) >= 1.0:
            print(
                f"seq={row.get('seq'):04d} "
                f"d_res={row.get('delta_reserved_gb', 0.0):8.3f} "
                f"d_alloc={row.get('delta_allocated_gb', 0.0):8.3f} "
                f"res={row.get('reserved_gb', 0.0):8.3f} "
                f"alloc={row.get('allocated_gb', 0.0):8.3f} "
                f"large_cache={row.get('cached_large_pool_gb', 0.0):8.3f} "
                f"large_inact={row.get('inactive_split_large_pool_gb', 0.0):8.3f} "
                f"segL={row.get('segments_large_pool', 0):4} "
                f"{row.get('stage')} {row.get('detail', '')}"
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tokens", default="14000,17000,19000,20480,16800,14500")
    parser.add_argument("--vocab-size", type=int, default=151936)
    parser.add_argument("--dtype", choices=["bf16", "fp16", "fp32"], default="bf16")
    parser.add_argument("--rounds", type=int, default=2)
    parser.add_argument("--flat-buffer-gb", type=float, default=2.318)
    parser.add_argument("--reduce-buffer-gb", type=float, default=4.637)
    parser.add_argument("--small-reduce-gb", type=float, default=0.580)
    parser.add_argument("--empty-cache-after-step", action="store_true")
    parser.add_argument("--output-jsonl", default="")
    run(parser.parse_args())


if __name__ == "__main__":
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    main()
```

## Steps to Reproduce

1. Save the script above as `repro_rocm_allocator_reserved.py`.
2. Run the main repro in the ROCm PyTorch Docker image:

```bash
docker run --rm \
  --device=/dev/kfd \
  --device=/dev/dri \
  --group-add video \
  --ipc=host \
  --shm-size=16G \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  -e HIP_VISIBLE_DEVICES=0 \
  -e ROCR_VISIBLE_DEVICES=0 \
  -v "$PWD:/workspace" \
  -w /workspace \
  rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.9.1 \
  python3 repro_rocm_allocator_reserved.py
```

If the host requires the `render` group for GPU access and the group exists, add:

```bash
--group-add render \
```

If Docker requires sudo, run the same command with `sudo docker run ...`.

3. Run the `empty_cache` control:

```bash
docker run --rm \
  --device=/dev/kfd \
  --device=/dev/dri \
  --group-add video \
  --ipc=host \
  --shm-size=16G \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  -e HIP_VISIBLE_DEVICES=0 \
  -e ROCR_VISIBLE_DEVICES=0 \
  -v "$PWD:/workspace" \
  -w /workspace \
  rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.9.1 \
  python3 repro_rocm_allocator_reserved.py --empty-cache-after-step
```

## Observed Result

Reference output from the main repro:

```text
events=63
max reserved_gb=27.488 seq=18 stage=micro:after_logits_alloc round=0 micro=3 tokens=20480
max allocated_gb=13.332 seq=20 stage=micro:after_reduce_buffers_alloc round=0 micro=3 tokens=20480
max cached_large_pool_gb=27.488 seq=21 stage=micro:after_delete_refs round=0 micro=3 tokens=20480
max inactive_split_large_pool_gb=0.711 seq=30 stage=micro:after_reduce_buffers_alloc round=0 micro=5 tokens=14500
```

The important signal is that reserved memory grows to `27.488 GB`, while current allocated memory peaks at only `13.332 GB`. After tensor references are deleted, allocated memory can drop to zero while reserved memory remains high and is almost entirely large-pool cache:

```text
MEM seq=21 stage=micro:after_delete_refs round=0 micro=3 tokens=20480 reserved=27.488GB allocated=0.000GB cached_large=27.488GB inactive_split_large=0.000GB ...
MEM seq=63 stage=end:after_empty_cache reserved=0.000GB allocated=0.000GB cached_large=0.000GB ...
```

The reserved-memory increases are stair-step shaped as the dynamic large allocations change size:

```text
seq=0008 d_res=4.812 res=16.312 alloc=4.811 large_cache=11.501 micro:after_logits_alloc round=0 micro=1 tokens=17000
seq=0013 d_res=5.379 res=21.691 alloc=5.377 large_cache=16.314 micro:after_logits_alloc round=0 micro=2 tokens=19000
seq=0018 d_res=5.797 res=27.488 alloc=5.797 large_cache=21.691 micro:after_logits_alloc round=0 micro=3 tokens=20480
```

Reference output from the `--empty-cache-after-step` control:

```text
events=75
max reserved_gb=13.334 seq=23 stage=micro:after_reduce_buffers_alloc round=0 micro=3 tokens=20480
max allocated_gb=13.332 seq=23 stage=micro:after_reduce_buffers_alloc round=0 micro=3 tokens=20480
max cached_large_pool_gb=13.334 seq=24 stage=micro:after_delete_refs round=0 micro=3 tokens=20480
max inactive_split_large_pool_gb=0.004 seq=35 stage=micro:after_reduce_buffers_alloc round=0 micro=5 tokens=14500
```

With `--empty-cache-after-step`, `max_allocated_gb` stays essentially the same, but `max_reserved_gb` drops from `27.488` to `13.334`. This strongly suggests that the extra reserved memory in the main run is allocator cache high-water, not live tensor memory.

## Expected Behavior

After large temporary tensors are freed and current allocated memory drops, the allocator should either:

- reuse the existing large cached blocks more effectively for subsequent dynamic large allocations; or
- avoid retaining a reserved high-water level that is much larger than the current and peak live allocation requirement.

At minimum, this behavior should not make a workload appear close to OOM solely because whole large-pool cached segments remain reserved and are not reused well.

## Why This Matters

In real RL training workloads with dynamic sequence lengths and large logits / temporary buffers, this allocator behavior can make `reserved` memory grow far beyond current live memory. That can cause training jobs to OOM even when `allocated` memory indicates that live tensors are much smaller than the reserved footprint.

The standalone repro is intentionally framework-free so the behavior can be investigated at the ROCm/PyTorch caching allocator level.


### Operating System

Ubuntu 22.04.5 LTS

### CPU

AMD EPYC 9575F

### GPU

AMD Instinct MI325X

### ROCm Version

ROCm 7.2.4

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_