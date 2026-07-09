# [Issue]: amdgpu compute wave store and resume causing MES firmware 0x80 hang

- **Issue #:** 5590
- **State:** closed
- **Created:** 2025-10-28T17:17:08Z
- **Updated:** 2026-03-04T11:33:50Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5590

### Problem Description

Updated 11/14 w/ new image references, use cases against ROCm 7.1
Updated 11/16 jump to the bottom for the workaround `amdgpu.cwsr_enable=0`

Strix Halo, even with the MES kernel patches, and the latest MES firmware (0x80) is still experiencing problems.   The goal here is to create a simple scenario, without building anything against a constantly changing upstream git repository or a dynamic set of pytorch wheels, in order to allow AMD developers to focus on consistently reproducing this issue in a static environment, so they can get it fixed.  

Ubuntu 24.04 includes a patched kernel with the MES fixes, and depends on the Instinct amdgpu-dkms packages so it is a good candidate distro.   

The steps to reproduce are:
1) Prepare the system following the docs, [using the linux-oem-24.04c kernel](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/native_linux/install-ryzen.html#prepare-the-system) 
2) ROCm 7.1 amdgpu-dkms installs the new MES firmware, so we can now skip [pinning upstream cleanly against Ubuntu 24.04](https://github.com/ROCm/ROCm/issues/5151#issuecomment-3453898122) using the resolute linux-firmware package
3) Pull AMD's most recent pre-built vLLM dev image from docker based on ROCm 7.1 (`docker pull rocm/vllm-dev:preview7.1_1117_rc1_20251112`) 
4) Serve up the new [IBM Granite 4 H Small ](https://huggingface.co/ibm-granite/granite-4.0-h-small); A new flagship model we were happy to see [AMD support day 0](https://www.amd.com/en/developer/resources/technical-articles/2025/run-granite-4-0-models-with-amd-instinct-gpus.html). 

On the vLLM cli, we get the cleanly emitted `HW Exception by GPU node-1 (Agent handle: 0x2f0fbb70) reason :GPU Hang`  and on the kernel console we see `amdgpu: MES failed to respond to msg=REMOVE_QUEUE`

After posting an example in [a related ticket](https://github.com/ROCm/ROCm/issues/5443#issuecomment-3454127614), it seemed like a good use case to focus resolution around. 

Our setup uses a [large 125 GiB unified memory configuration](https://github.com/ROCm/ROCm/issues/5562#issuecomment-3457153637)

```
# /etc/default/grub.d/amd_ttm.cfg
GRUB_CMDLINE_LINUX="${GRUB_CMDLINE_LINUX:+$GRUB_CMDLINE_LINUX }ttm.pages_limit=32768000 ttm.page_pool_size=32768000 amdttm.pages_limit=32768000 amdttm.page_pool_size=32768000"
```

You can actually now serve up the new Nano Series (newly released 10/28) of the IBM Mamba hybrids `ibm-granite/granite-4.0-h-350m`  as the CUDA graph is captured quickly enough to avoid the GPU hang.   If you go larger, you are hung. 

You can pick your preffered attention backend. 

ROCm Attention (default):
```
vllm serve ibm-granite/granite-4.0-h-350m --compilation-config '{"cudagraph_mode":"PIECEWISE"}'  #works
vllm serve ibm-granite/granite-4.0-h-small --compilation-config '{"cudagraph_mode":"PIECEWISE"}'   #hangs
```

Triton Attention:
```
export VLLM_ROCM_USE_AITER=0
export VLLM_V1_USE_PREFILL_DECODE_ATTENTION=0
vllm serve ibm-granite/granite-4.0-h-350m   #works
vllm serve ibm-granite/granite-4.0-h-small    #hangs    
```

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
    rocm/vllm-dev:preview7.1_1117_rc1_20251112
```
And here is what you will see on the console
```
root@ai2:/app# vllm serve ibm-granite/granite-4.0-h-small --compilation-config '{"cudagraph_mode":"PIECEWISE"}'
(APIServer pid=733) INFO 11-14 21:01:38 [api_server.py:1961] vLLM API server version 0.11.1rc6.dev115+gbc926c122
(APIServer pid=733) INFO 11-14 21:01:38 [utils.py:253] non-default args: {'model_tag': 'ibm-granite/granite-4.0-h-small', 'model': 'ibm-granite/granite-4.0-h-small', 'compilation_config': {'level': None, 'mode': None, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['+rms_norm', '+silu_and_mul', '+quant_fp8'], 'splitting_ops': None, 'use_inductor': None, 'compile_sizes': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.PIECEWISE: 1>, 'use_cudagraph': True, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'full_cuda_graph': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'local_cache_dir': None}}
(APIServer pid=733) INFO 11-14 21:01:39 [model.py:630] Resolved architecture: GraniteMoeHybridForCausalLM
(APIServer pid=733) INFO 11-14 21:01:39 [model.py:1728] Using max model len 131072
(APIServer pid=733) INFO 11-14 21:01:39 [scheduler.py:226] Chunked prefill is enabled with max_num_batched_tokens=8192.
(APIServer pid=733) INFO 11-14 21:01:39 [config.py:309] Disabling cascade attention since it is not supported for hybrid models.
(APIServer pid=733) INFO 11-14 21:01:39 [config.py:422] Setting attention block size to 528 tokens to ensure that attention page size is >= mamba page size.
(APIServer pid=733) INFO 11-14 21:01:39 [config.py:446] Padding mamba page size by 0.69% to ensure that mamba page size and attention page size are exactly equal.
(EngineCore_DP0 pid=809) INFO 11-14 21:01:43 [core.py:93] Initializing a V1 LLM engine (v0.11.1rc6.dev115+gbc926c122) with config: model='ibm-granite/granite-4.0-h-small', speculative_config=None, tokenizer='ibm-granite/granite-4.0-h-small', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=ibm-granite/granite-4.0-h-small, enable_prefix_caching=False, chunked_prefill_enabled=True, pooler_config=None, compilation_config={'level': None, 'mode': 3, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['+rms_norm', '+silu_and_mul', '+quant_fp8', 'none'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_mla_attention', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::plamo2_mamba_mixer', 'vllm::gdn_attention', 'vllm::kda_attention', 'vllm::sparse_attn_indexer'], 'use_inductor': None, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.PIECEWISE: 1>, 'use_cudagraph': True, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 272, 288, 304, 320, 336, 352, 368, 384, 400, 416, 432, 448, 464, 480, 496, 512], 'cudagraph_copy_inputs': False, 'full_cuda_graph': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': 512, 'local_cache_dir': None}
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=809) INFO 11-14 21:01:43 [parallel_state.py:1325] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=809) INFO 11-14 21:01:44 [gpu_model_runner.py:2932] Starting to load model ibm-granite/granite-4.0-h-small...
(EngineCore_DP0 pid=809) INFO 11-14 21:01:44 [rocm.py:292] Using Rocm Attention backend.
(EngineCore_DP0 pid=809) WARNING 11-14 21:01:47 [compilation.py:908] Op 'quant_fp8' not present in model, enabling with '+quant_fp8' has no effect
Loading safetensors checkpoint shards:   0% Completed | 0/14 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   7% Completed | 1/14 [00:02<00:31,  2.44s/it]
Loading safetensors checkpoint shards:  14% Completed | 2/14 [00:07<00:48,  4.01s/it]
Loading safetensors checkpoint shards:  21% Completed | 3/14 [00:12<00:50,  4.55s/it]
Loading safetensors checkpoint shards:  29% Completed | 4/14 [00:17<00:47,  4.79s/it]
Loading safetensors checkpoint shards:  36% Completed | 5/14 [00:22<00:43,  4.89s/it]
Loading safetensors checkpoint shards:  43% Completed | 6/14 [00:28<00:39,  4.96s/it]
Loading safetensors checkpoint shards:  50% Completed | 7/14 [00:33<00:35,  5.05s/it]
Loading safetensors checkpoint shards:  57% Completed | 8/14 [00:38<00:30,  5.09s/it]
Loading safetensors checkpoint shards:  64% Completed | 9/14 [00:43<00:25,  5.13s/it]
Loading safetensors checkpoint shards:  71% Completed | 10/14 [00:48<00:20,  5.14s/it]
Loading safetensors checkpoint shards:  79% Completed | 11/14 [00:54<00:15,  5.22s/it]
Loading safetensors checkpoint shards:  86% Completed | 12/14 [00:59<00:10,  5.27s/it]
Loading safetensors checkpoint shards:  93% Completed | 13/14 [01:05<00:05,  5.55s/it]
Loading safetensors checkpoint shards: 100% Completed | 14/14 [01:11<00:00,  5.51s/it]
Loading safetensors checkpoint shards: 100% Completed | 14/14 [01:11<00:00,  5.09s/it]
(EngineCore_DP0 pid=809) 
(EngineCore_DP0 pid=809) INFO 11-14 21:02:59 [default_loader.py:314] Loading weights took 71.42 seconds
(EngineCore_DP0 pid=809) INFO 11-14 21:03:04 [gpu_model_runner.py:2997] Model loading took 78.4272 GiB and 77.370219 seconds
(EngineCore_DP0 pid=809) /usr/local/lib/python3.12/dist-packages/torch/_dynamo/variables/functions.py:1652: UserWarning: Dynamo detected a call to a `functools.lru_cache`-wrapped function. Dynamo ignores the cache wrapper and directly traces the wrapped function. Silent incorrectness is only a *potential* risk, not something we have observed. Enable TORCH_LOGS="+dynamo" for a DEBUG stack trace.
(EngineCore_DP0 pid=809)   torch._dynamo.utils.warn_once(msg)
(EngineCore_DP0 pid=809) INFO 11-14 21:03:08 [backends.py:620] Using cache directory: /root/.cache/vllm/torch_compile_cache/4f6a0d7a6e/rank_0_0/backbone for vLLM's torch.compile
(EngineCore_DP0 pid=809) INFO 11-14 21:03:08 [backends.py:636] Dynamo bytecode transform time: 3.07 s
(EngineCore_DP0 pid=809) INFO 11-14 21:03:09 [backends.py:250] Cache the graph for dynamic shape for later use
(EngineCore_DP0 pid=809) INFO 11-14 21:03:23 [backends.py:281] Compiling a graph for dynamic shape takes 15.78 s
(EngineCore_DP0 pid=809) WARNING 11-14 21:03:24 [fused_moe.py:887] Using default MoE config. Performance might be sub-optimal! Config file not found at ['/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=72,N=768,device_name=0x1586.json']
(EngineCore_DP0 pid=809) INFO 11-14 21:03:26 [monitor.py:34] torch.compile takes 18.85 s in total
HW Exception by GPU node-1 (Agent handle: 0x2f0fbb70) reason :GPU Hang
HW Exception by GPU node-1 (Agent handle: 0x1f62da10) reason :GPU Hang
Aborted (core dumped)
root@ai2:/app# /usr/lib/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```
And the dmesg is going to be similar to the following
```
[  990.479743] amdgpu 0000:c5:00.0: amdgpu: MES failed to respond to msg=REMOVE_QUEUE
[  990.479760] amdgpu 0000:c5:00.0: amdgpu: failed to remove hardware queue from MES, doorbell=0x1002
[  990.479768] amdgpu 0000:c5:00.0: amdgpu: MES might be in unrecoverable state, issue a GPU reset
[  990.479779] amdgpu 0000:c5:00.0: amdgpu: Failed to evict queue 1
[  990.479799] amdgpu 0000:c5:00.0: amdgpu: GPU reset begin!. Source:  3
[  990.479898] amdgpu 0000:c5:00.0: amdgpu: Failed to evict process queues
[  990.479920] amdgpu: Failed to quiesce KFD
[  990.479967] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State
[  990.486732] amdgpu 0000:c5:00.0: amdgpu: Dumping IP State Completed
[  990.520342] amdgpu 0000:c5:00.0: amdgpu: MODE2 reset
[  990.549888] amdgpu 0000:c5:00.0: amdgpu: GPU reset succeeded, trying to resume
[  990.550342] [drm] PCIE GART of 512M enabled (table at 0x000000801FB00000).
[  990.550415] amdgpu 0000:c5:00.0: amdgpu: [drm] AMDGPU device coredump file has been created
[  990.550417] amdgpu 0000:c5:00.0: amdgpu: [drm] Check your /sys/class/drm/card1/device/devcoredump/data
[  990.550419] amdgpu 0000:c5:00.0: amdgpu: SMU is resuming...
[  990.564041] amdgpu 0000:c5:00.0: amdgpu: SMU is resumed successfully!
[  990.580876] amdgpu 0000:c5:00.0: amdgpu: [drm] DMUB hardware initialized: version=0x09002F00
[  990.640096] amdgpu 0000:c5:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[  990.640105] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[  990.640106] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[  990.640107] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 6 on hub 0
[  990.640108] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 7 on hub 0
[  990.640109] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 8 on hub 0
[  990.640110] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 9 on hub 0
[  990.640111] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 10 on hub 0
[  990.640112] amdgpu 0000:c5:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 11 on hub 0
[  990.640113] amdgpu 0000:c5:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
[  990.640114] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 8
[  990.640115] amdgpu 0000:c5:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 8
[  990.640116] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_0 uses VM inv eng 4 on hub 8
[  990.640117] amdgpu 0000:c5:00.0: amdgpu: ring jpeg_dec_1 uses VM inv eng 6 on hub 8
[  990.640118] amdgpu 0000:c5:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[  990.640119] amdgpu 0000:c5:00.0: amdgpu: ring vpe uses VM inv eng 7 on hub 8
[  990.712022] amdgpu 0000:c5:00.0: amdgpu: GPU reset(1) succeeded!
[  990.712038] amdgpu 0000:c5:00.0: [drm] device wedged, but recovered through reset
[ 1019.947543] amdgpu: Freeing queue vital buffer 0x79c031400000, queue evicted
[ 1019.947554] amdgpu: Freeing queue vital buffer 0x79c032a00000, queue evicted
```
```
OS:
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"
CPU: 
model name	: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
GPU:
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Name:                    gfx1151                            
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx1151         
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
  Name:                    aie2                               
  Marketing Name:          AIE-ML     
```
```
root@ai2:~# dpkg -l | grep amdgpu
root@ai2:~# dpkg -l | grep amdgpu
ii  amdgpu-core                          1:7.1.70100-2238427.24.04               all          Core meta package for unified amdgpu driver.
ii  amdgpu-dkms                          1:6.16.6.30200000-2238411.24.04         all          amdgpu driver in DKMS format.
ii  amdgpu-dkms-firmware                 30.20.0.0.30200000-2238411.24.04        all          firmware blobs used by amdgpu driver in DKMS format
ii  amdgpu-install                       30.20.0.0.30200000-2238411.24.04        all          AMDGPU driver repository and installer
ii  libdrm-amdgpu-amdgpu1:amd64          1:2.4.125.70100-2238427.24.04           amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-amdgpu-common                 1.0.0.70100-2238427.24.04               all          List of AMD/ATI cards' device IDs, revision IDs and marketing names
ii  libdrm-amdgpu-dev:amd64              1:2.4.125.70100-2238427.24.04           amd64        Userspace interface to kernel DRM services -- development files
ii  libdrm-amdgpu-radeon1:amd64          1:2.4.125.70100-2238427.24.04           amd64        Userspace interface to radeon-specific kernel DRM services -- runtime
ii  libdrm-amdgpu1:amd64                 2.4.122-1~ubuntu0.24.04.1               amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm2-amdgpu:amd64                 1:2.4.125.70100-2238427.24.04           amd64        Userspace interface to kernel DRM services -- runtime

root@ai2:~# cat /sys/kernel/debug/dri/128/amdgpu_firmware_info | grep MES
MES_KIQ feature version: 6, firmware version: 0x0000006f
MES feature version: 1, firmware version: 0x00000080
```


### Operating System

Ubuntu 24.04.3 LTS

### CPU

Strix Halo

### GPU

Strix Halo

### ROCm Version

ROCm 7.1

### ROCm Component

_No response_

### Steps to Reproduce


Described in the problem description 

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module version 6.16.6 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.14
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5187                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    131009800(0x7cf0d08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    131009800(0x7cf0d08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131009800(0x7cf0d08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131009800(0x7cf0d08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1151                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      2048(0x800) KB                     
    L3:                      32768(0x8000) KB                   
  Chip ID:                 5510(0x1586)                       
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2900                               
  BDFID:                   50432                              
  Internal Node ID:        1                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 32                                 
  SDMA engine uCode::      17                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    125829120(0x7800000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    125829120(0x7800000) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1151         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*******                  
Agent 3                  
*******                  
  Name:                    aie2                               
  Uuid:                    AIE-XX                             
  Marketing Name:          AIE-ML                             
  Vendor Name:             AMD                                
  Feature:                 AGENT_DISPATCH                     
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        1(0x1)                             
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          64(0x40)                           
  Queue Type:              SINGLE                             
  Node:                    0                                  
  Device Type:             DSP                                
  Cache Info:              
    L2:                      2048(0x800) KB                     
    L3:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          0(0x0)                             
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            0                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:0                                  
  Memory Properties:       
  Features:                AGENT_DISPATCH
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, COARSE GRAINED
      Size:                    131009800(0x7cf0d08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65536(0x10000) KB                  
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131009800(0x7cf0d08) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*** Done ***              
```

### Additional Information

_No response_