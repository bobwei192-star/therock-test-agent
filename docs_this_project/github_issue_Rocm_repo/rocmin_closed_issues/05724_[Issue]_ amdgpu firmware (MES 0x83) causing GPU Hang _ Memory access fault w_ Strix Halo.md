# [Issue]: amdgpu firmware (MES 0x83) causing GPU Hang / Memory access fault w/ Strix Halo

- **Issue #:** 5724
- **State:** closed
- **Created:** 2025-11-29T00:14:14Z
- **Updated:** 2026-03-04T14:51:11Z
- **Labels:** status: assessed
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5724

### Problem Description

--> Jump right to the bottom for ROCm 7.2 + 24.04-oem kernels https://github.com/ROCm/ROCm/issues/5724#issuecomment-3821014371

This new firmware causes a GPU fault in known working scenarios.   This was the case for ROCm 7.1.0, and the problem persists after the release of ROCm 7.1.1 just a few days ago. 

TDLR;  Stick to the amdgpu-dkms-firmware package and keep the `cwsr_enable=0` workaround in place.  Older MES 0x80 does not cause this issue.

A new [amdgpu firmware ](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/log/?qt=grep&q=amdgpu) appeared upstream for the Strix Halo (gfx1151).   It can be seen upstream in ubuntu-proposed [linux-firmware](https://code.launchpad.net/ubuntu/+source/linux-firmware/20251125.gitff6418d1-0ubuntu1).  It is just a matter of time before this firmware lands on users with recent linux kernels that may opt not to use the amdgpu-dkms* packages, as the amdgpu stack ships with newer kernels and ABI compatibility with the newest kernels is not baked into the shipped dkms modules.  Additionally the upstream Ubuntu firmware bundle carries new firmware for MT7925 bluetooth and wifi components integrated into most Strix Halo SoCs currently pulling more Strix Halo users in this direction because of other quirks. 

One simple way to reproduce is to use an AMD ROCm vLLM build and serve the smallest of the IBM granite4 hybrid Mamba models.  The result a terminal error similar to the following. 

`Memory access fault by GPU node-1 (Agent handle: 0x43578c10) on address 0x7f58f8001000. Reason: Page not present or supervisor privilege.`

Additionally, the kernel dmesg emits a page fault
```
[  651.971687] amdgpu 0000:c5:00.0: amdgpu: [gfxhub] page fault (src_id:0 ring:153 vmid:8 pasid:32771)
[  651.971715] amdgpu 0000:c5:00.0: amdgpu:  Process VLLM::EngineCor pid 2419 thread VLLM::EngineCor pid 2419
[  651.971725] amdgpu 0000:c5:00.0: amdgpu:   in page starting at address 0x00007f58f8001000 from client 10
[  651.971734] amdgpu 0000:c5:00.0: amdgpu: GCVM_L2_PROTECTION_FAULT_STATUS:0x00800932
[  651.971741] amdgpu 0000:c5:00.0: amdgpu: 	 Faulty UTCL2 client ID: CPF (0x4)
[  651.971748] amdgpu 0000:c5:00.0: amdgpu: 	 MORE_FAULTS: 0x0
[  651.971754] amdgpu 0000:c5:00.0: amdgpu: 	 WALKER_ERROR: 0x1
[  651.971761] amdgpu 0000:c5:00.0: amdgpu: 	 PERMISSION_FAULTS: 0x3
[  651.971769] amdgpu 0000:c5:00.0: amdgpu: 	 MAPPING_ERROR: 0x1
[  651.971774] amdgpu 0000:c5:00.0: amdgpu: 	 RW: 0x0
[  652.292990] amdgpu: Freeing queue vital buffer 0x7f56f8a00000, queue evicted
```

Some additional notes:
- sticking with default kernels, ROCm 7.1.1 and amdgpu 30.20.1 packages will not trip on this as amdgpu-dkms-firmware overrides linux-firmware on Ubuntu by default.  You still need the cwsr workaround in #5590 to avoid that separate GPU hang issue on ROCm 7.1.1. 

- The amdgpu instinct 30.20.1 amdgpu-dkms-firmware was released a few days ago, but ships the older MES 0x80 firmware, possibly indicating a known issue at the time of release.  Also, another RDNA 3 firmware, the gfx1101 updates, were rolled back as seen in the amdgpu linux-firmware commits linked above. 

- As noted earlier, the previous MES hang in #5590 must still be worked around with the `amdgpu.cwsr_enable=0` kernel flag.  Without that flag enabled, ROCm 7.1.1 and amdgpu 30.20.1 on Ubuntu 24.04.3 will still cause a separate known GPU hang, and so the workaround in #5590 must still be enabled.


### Operating System

Ubuntu 24.04.3

### CPU

Strix Halo

### GPU

Strix Halo

### ROCm Version

ROCm 7.1.1

### ROCm Component

_No response_

### Steps to Reproduce


Grab an AMD vllm image;  Either the most recent stable (built against ROCm 7.0) or current nightly (built against ROCm 7.1) will do or [build your own](https://github.com/ROCm/aiter/issues/900#issuecomment-3523554029). 

`docker pull rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103` 
or
`docker pull rocm/vllm-dev:nightly`

Fire up docker 
```
 docker run -it \
    --network host \
    --ipc host \
    --privileged \
    --cap-add=CAP_SYS_ADMIN \
    --cap-add=SYS_PTRACE \
    --device=/dev/kfd \
    --device=/dev/dri \
    --device=/dev/mem \
    --security-opt seccomp=unconfined \
    --shm-size 4G \
    -e TERM=xterm-256color \
    -v /mnt/models/huggingface/:/root/.cache/huggingface/ \
    --name vllm-strixhalohang \
    rocm/vllm:rocm7.0.0_vllm_0.11.1_20251103
```
Serve the model

```
root@ai2:/app# vllm serve ibm-granite/granite-4.0-h-350m
INFO 11-28 23:05:28 [__init__.py:225] Automatically detected platform rocm.
(APIServer pid=13) INFO 11-28 23:05:33 [api_server.py:1876] vLLM API server version 0.11.1rc2.dev141+g38f225c2a
(APIServer pid=13) INFO 11-28 23:05:33 [utils.py:243] non-default args: {'model_tag': 'ibm-granite/granite-4.0-h-350m', 'model': 'ibm-granite/granite-4.0-h-350m'}
(APIServer pid=13) INFO 11-28 23:05:41 [model.py:658] Resolved architecture: GraniteMoeHybridForCausalLM
(APIServer pid=13) INFO 11-28 23:05:41 [model.py:1745] Using max model len 32768
(APIServer pid=13) INFO 11-28 23:05:42 [scheduler.py:225] Chunked prefill is enabled with max_num_batched_tokens=8192.
(APIServer pid=13) INFO 11-28 23:05:42 [config.py:323] Disabling cascade attention since it is not supported for hybrid models.
(APIServer pid=13) INFO 11-28 23:05:42 [config.py:439] Setting attention block size to 400 tokens to ensure that attention page size is >= mamba page size.
(APIServer pid=13) INFO 11-28 23:05:42 [config.py:463] Padding mamba page size by 1.39% to ensure that mamba page size and attention page size are exactly equal.
INFO 11-28 23:05:43 [__init__.py:225] Automatically detected platform rocm.
(EngineCore_DP0 pid=178) INFO 11-28 23:05:46 [core.py:730] Waiting for init message from front-end.
(EngineCore_DP0 pid=178) INFO 11-28 23:05:46 [core.py:97] Initializing a V1 LLM engine (v0.11.1rc2.dev141+g38f225c2a) with config: model='ibm-granite/granite-4.0-h-350m', speculative_config=None, tokenizer='ibm-granite/granite-4.0-h-350m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=ibm-granite/granite-4.0-h-350m, enable_prefix_caching=False, chunked_prefill_enabled=True, pooler_config=None, compilation_config={'level': None, 'mode': 3, 'debug_dump_path': None, 'cache_dir': '', 'backend': 'inductor', 'custom_ops': ['+rms_norm', '+silu_and_mul', '+quant_fp8', 'none', '+rms_norm'], 'splitting_ops': [], 'use_inductor': None, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL: 2>, 'use_cudagraph': True, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [512, 504, 496, 488, 480, 472, 464, 456, 448, 440, 432, 424, 416, 408, 400, 392, 384, 376, 368, 360, 352, 344, 336, 328, 320, 312, 304, 296, 288, 280, 272, 264, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 4, 2, 1], 'cudagraph_copy_inputs': False, 'full_cuda_graph': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_capture_size': 512, 'local_cache_dir': None}
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=178) INFO 11-28 23:05:47 [parallel_state.py:1325] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
Memory access fault by GPU node-1 (Agent handle: 0x43578c10) on address 0x7f58f8001000. Reason: Page not present or supervisor privilege.
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Same observations on Debian 13. 