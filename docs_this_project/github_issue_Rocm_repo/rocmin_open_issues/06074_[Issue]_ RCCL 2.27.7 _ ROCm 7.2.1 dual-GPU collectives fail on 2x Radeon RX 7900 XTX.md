# [Issue]: RCCL 2.27.7 / ROCm 7.2.1 dual-GPU collectives fail on 2x Radeon RX 7900 XTX

- **Issue #:** 6074
- **State:** open
- **Created:** 2026-03-28T17:27:22Z
- **Updated:** 2026-06-22T10:33:38Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6074

### Problem Description

## Context

I originally hit this while trying to get **vLLM nightlies** working for tensor-parallel multi-GPU inference. The container I was using was:

- `vllm/vllm-openai-rocm:nightly-148a5c1226f8668cb52c4900b5ff2c80344e78f2`

However, after reducing the problem, this reproduces **outside vLLM** using a minimal `torch.distributed` script on the host. So this does not appear to be a vLLM-specific issue.

## Problem Description

Dual-GPU collectives fail on a host system with **2x Radeon RX 7900 XTX** on **ROCm 7.2.1 / RCCL 2.27.7**.

Each GPU works individually. The failure only occurs when both GPUs participate in the same collective. The public `ROCm/rccl` repository appears deprecated/moved, so I am filing this in `ROCm/ROCm` for triage.

## System Information

### OS

```text
NAME="Ubuntu"
VERSION="24.04.4 LTS (Noble Numbat)"
```

### CPU

```text
AMD Ryzen 7 7800X3D 8-Core Processor
```

### GPU

```text
Name:                    AMD Ryzen 7 7800X3D 8-Core Processor
Marketing Name:          AMD Ryzen 7 7800X3D 8-Core Processor
Name:                    gfx1100
Marketing Name:          Radeon RX 7900 XTX
    Name:                    amdgcn-amd-amdhsa--gfx1100
    Name:                    amdgcn-amd-amdhsa--gfx11-generic
Name:                    gfx1100
Marketing Name:          Radeon RX 7900 XTX
    Name:                    amdgcn-amd-amdhsa--gfx1100
    Name:                    amdgcn-amd-amdhsa--gfx11-generic
Name:                    gfx1100
Marketing Name:          AMD Radeon Graphics
    Name:                    amdgcn-amd-amdhsa--gfx1100
    Name:                    amdgcn-amd-amdhsa--gfx11-generic
```

### Software Versions

- ROCm: `7.2.1`
- RCCL: `2.27.7-HEAD:96a25b5`
- PyTorch: `2.9.1+rocm7.2.0.git7e1940d4`
- Kernel: `6.17.0-19-generic`

## Expected Behavior

A minimal 2-rank `torch.distributed` program should successfully complete:

- `dist.barrier()`
- `dist.all_reduce()`

## Actual Behavior

The process group initializes and RCCL communicator initialization completes on both GPUs, but the first collective fails with:

- `HIP failure: 'the operation cannot be performed in the present state'`
- `torch.distributed.DistBackendError`
- `NCCL version 2.27.7`

This happens in a minimal host-side PyTorch repro, so this does **not** appear to be a vLLM-specific issue.

## Topology Observation

RCCL reports the two discrete GPUs on a `PHB` path with bandwidth `6.0`, and the second GPU is the chipset-side device (`busId d000`). The failure occurs only when a collective spans both GPUs.

## Minimal Reproduction Script

Save as `rccl_smoke.py`:

```python
#!/usr/bin/env python3
import os
import sys
import torch
import torch.distributed as dist


def log(msg: str) -> None:
    rank = int(os.environ.get("RANK", "-1"))
    local_rank = int(os.environ.get("LOCAL_RANK", "-1"))
    print(f"[rank={rank} local_rank={local_rank}] {msg}", flush=True)


def main() -> int:
    print("HIP_VISIBLE_DEVICES =", os.environ.get("HIP_VISIBLE_DEVICES"), flush=True)
    print("ROCR_VISIBLE_DEVICES =", os.environ.get("ROCR_VISIBLE_DEVICES"), flush=True)

    if not torch.cuda.is_available():
        print("torch.cuda.is_available() is False", file=sys.stderr, flush=True)
        return 2

    rank = int(os.environ["RANK"])
    local_rank = int(os.environ["LOCAL_RANK"])
    world_size = int(os.environ["WORLD_SIZE"])

    log(f"torch={torch.__version__}")
    log(f"cuda/HIP available={torch.cuda.is_available()} device_count={torch.cuda.device_count()}")

    torch.cuda.set_device(local_rank)
    dev = torch.device(f"cuda:{local_rank}")
    props = torch.cuda.get_device_properties(dev)
    log(f"using device {local_rank}: {props.name}")

    dist.init_process_group(
        backend="nccl",
        init_method="env://",
        world_size=world_size,
        rank=rank,
        device_id=dev,
    )
    log("process group initialized")

    x = torch.tensor([rank + 1.0], device=dev, dtype=torch.float32)
    log(f"before barrier: {x.item()}")

    # Fails here on the affected setup
    dist.barrier()
    torch.cuda.synchronize()
    log("barrier passed")

    dist.all_reduce(x, op=dist.ReduceOp.SUM)
    torch.cuda.synchronize()
    log(f"after all_reduce: {x.item()}")

    dist.destroy_process_group()
    log("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Reproduction Command

```bash
export HIP_VISIBLE_DEVICES=0,1
unset ROCR_VISIBLE_DEVICES

export NCCL_DEBUG=INFO
export NCCL_DEBUG_SUBSYS=INIT,P2P,GRAPH,ENV
export NCCL_DMABUF_ENABLE=1
export NCCL_P2P_DISABLE=1
export NCCL_MIN_NCHANNELS=1
export NCCL_MAX_NCHANNELS=1
export RCCL_CHANNEL_TUNING_ENABLE=0
export RCCL_P2P_BATCH_ENABLE=0
export HSA_FORCE_FINE_GRAIN_PCIE=1

torchrun --nproc_per_node=2 rccl_smoke.py
```

## Result

The 2-rank run fails on the first collective. A representative error is:

```text
[rank1]: torch.distributed.DistBackendError: NCCL error in:
... ProcessGroupNCCL.cpp ...
unhandled cuda error, NCCL version 2.27.7

[FATAL ERROR]: HIP failure: 'the operation cannot be performed in the present state'
```

Host-side repro logs show:

- both GPUs visible and selected correctly
- process group initialized
- communicator init completed on both ranks
- `NCCL_P2P_DISABLE=1` was honored
- transport was `via SHM/direct/direct`
- failure still occurred on the first collective on rank 1 / `busId d000`

## Additional Validation

### Single GPU: first 7900 XTX works

This passes with only the first discrete GPU exposed:

```bash
unset ROCR_VISIBLE_DEVICES
export HIP_VISIBLE_DEVICES=0
export NCCL_DEBUG=INFO
torchrun --nproc_per_node=1 rccl_smoke.py
```

### Single GPU: second 7900 XTX works

This also passes with only the second discrete GPU exposed:

```bash
unset ROCR_VISIBLE_DEVICES
export HIP_VISIBLE_DEVICES=1
export NCCL_DEBUG=INFO
torchrun --nproc_per_node=1 rccl_smoke.py
```

### Interpretation

This suggests:

- GPU 0 alone is healthy
- GPU 1 alone is healthy
- communicator initialization across both GPUs is healthy
- the failure is specific to the **first dual-GPU collective** on this topology

## Notes

- This issue reproduces both inside and outside containers, but the host-side PyTorch repro is the cleanest evidence that the failure is below vLLM.
- I previously observed this setup working on an earlier RCCL generation around `2.26.x` on the same machine, though I do not currently have a minimized side-by-side repro attached for that older version.
- The machine also has an AMD iGPU present, but the failure reproduces with only the two discrete GPUs exposed to the repro.

## Attachments

I can attach, if helpful:

1. `rccl_smoke.py`
2. full 2-GPU failing host log
3. single-GPU passing log for GPU 0
4. single-GPU passing log for GPU 1
5. equivalent vLLM failure log showing the same first-collective failure pattern

### Operating System

24.04.4 LTS (Noble Numbat)

### CPU

7800X3D

### GPU

2 x AMD Radeon 7900XTX

### ROCm Version

7.2.1

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_