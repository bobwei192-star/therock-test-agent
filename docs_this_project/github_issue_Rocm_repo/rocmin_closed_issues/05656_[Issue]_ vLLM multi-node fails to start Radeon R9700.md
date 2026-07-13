# [Issue]: vLLM multi-node fails to start Radeon R9700

- **Issue #:** 5656
- **State:** closed
- **Created:** 2025-11-12T13:30:51Z
- **Updated:** 2026-04-01T15:20:04Z
- **Labels:** AMD Radeon AI PRO R9700, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5656

### Problem Description

Distributed vLLM was working with the flags as discussed in this previous ticket: https://github.com/ROCm/ROCm/issues/5567

The `rocm/vllm:latest` image ID `fdb0ad05db4b` fails with the error described in the steps to reproduce.

Previously, these steps worked with `rocm/vllm:rocm7.0.0_vllm_0.10.2_20251006` Image ID `beeea916d4a4`

The two systems in this test have the same hardware.

### Operating System

24.04.3 LTS (Noble Numbat)

### CPU

AMD EPYC 9115 16-Core Processor

### GPU

AMD Radeon AI PRO R9700 

### ROCm Version

ROCm 7.0

### ROCm Component

_No response_

### Steps to Reproduce

### vLLM Distributed

Reference: https://docs.vllm.ai/en/v0.8.0/serving/distributed_serving.html#running-vllm-on-multiple-nodes 

1. Setup
  a. Download run_cluster.sh
```
wget https://raw.githubusercontent.com/vllm-project/vllm/refs/heads/main/examples/online_serving/run_cluster.sh
chmod +x run_cluster.sh
```
  b. Edit run_cluster.sh
    i. Remove the `--gpus all` where the script runs the container
  c. Create a conda environment and install ray
```
conda create -n vllm python=3.13
conda activate vllm
pip install -U "ray[default]"
```

2. Start the Ray cluster
Start the head node
```
./run_cluster.sh \
                rocm/vllm:latest \
                10.20.1.126 \
                --head \
                /opt/huggingface \
                -e VLLM_HOST_IP=10.20.1.126 \
                -e NCCL_SOCKET_IFNAME=enp165s0f1np1 \
                -e GLOO_SOCKET_IFNAME=enp165s0f1np1 \
                -e NCCL_DEBUG=TRACE \
                --ipc=host \
				--device=/dev/kfd \
				--device=/dev/dri \
				--security-opt seccomp=unconfined \
				--group-add video \
				--shm-size 32G \
				-w /workspace
```
Start the worker node
```
./run_cluster.sh \
                rocm/vllm:latest \
                10.20.1.126 \
                --worker \
                /opt/huggingface \
                -e VLLM_HOST_IP=10.20.1.125 \
                -e NCCL_SOCKET_IFNAME=enp165s0f1np1 \
                -e GLOO_SOCKET_IFNAME=enp165s0f1np1 \
                -e NCCL_DEBUG=TRACE \
                --ipc=host \
				--device=/dev/kfd \
				--device=/dev/dri \
				--security-opt seccomp=unconfined \
				--group-add video \
				--shm-size 32G \
				-w /workspace
```

4. Check the ray status
```
# ray status
======== Autoscaler status: 2025-11-12 13:23:16.804602 ========
Node status
---------------------------------------------------------------
Active:
 1 node_35afdf3ae762c5562e26215333773093338dabcd47b9f5ae4d1081b0
 1 node_104ceb8ab69f5a9e0339138fd49a4152e58b48bbbc7e0998853aebe5
Pending:
 (no pending nodes)
Recent failures:
 (no failures)

Resources
---------------------------------------------------------------
Total Usage:
 0.0/128.0 CPU
 0.0/2.0 GPU
 0B/351.65GiB memory
 0B/150.71GiB object_store_memory

From request_resources:
 (none)
Pending Demands:
 (no resource demands)
```

5. Start vLLM serve from inside a container
```
docker exec -it node-25259 /bin/bash

vllm serve openai/gpt-oss-20b --enforce-eager --tensor-parallel 2 --distributed_executor_backend="ray"
```

Error message
```
INFO 11-12 11:11:28 [__init__.py:225] Automatically detected platform rocm.
(APIServer pid=445) INFO 11-12 11:11:32 [api_server.py:1876] vLLM API server version 0.11.1rc2.dev141+g38f225c2a
(APIServer pid=445) INFO 11-12 11:11:32 [utils.py:243] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'model': 'openai/gpt-oss-20b', 'enforce_eager': True, 'distributed_executor_backend': 'ray', 'tensor_parallel_size': 2}
(APIServer pid=445) INFO 11-12 11:11:39 [model.py:658] Resolved architecture: GptOssForCausalLM
Parse safetensors files: 
[00:02<00:00,  1.06it/s]
(APIServer pid=445) INFO 11-12 11:11:42 [model.py:1745] Using max model len 131072
(APIServer pid=445) INFO 11-12 11:11:43 [scheduler.py:225] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=445) INFO 11-12 11:11:43 [config.py:273] Overriding max cuda graph capture size to 992 for performance.
(APIServer pid=445) INFO 11-12 11:11:43 [vllm.py:375] Cudagraph is disabled under eager mode
INFO 11-12 11:11:45 [__init__.py:225] Automatically detected platform rocm.
(EngineCore_DP0 pid=742) INFO 11-12 11:11:48 [core.py:730] Waiting for init message from front-end.
(EngineCore_DP0 pid=742) INFO 11-12 11:11:48 [core.py:97] Initializing a V1 LLM engine (v0.11.1rc2.dev141+g38f225c2a) with config: model='openai/gpt-oss-20b', speculative_config=None, tokenizer='openai/gpt-oss-20b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=mxfp4, enforce_eager=True, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='openai_gptoss'), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=openai/gpt-oss-20b, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={'level': None, 'mode': 0, 'debug_dump_path': None, 'cache_dir': '', 'backend': 'inductor', 'custom_ops': ['+rms_norm', '+silu_and_mul', '+quant_fp8', 'all', '+rms_norm'], 'splitting_ops': None, 'use_inductor': None, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.NONE: 0>, 'use_cudagraph': False, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': [], 'cudagraph_copy_inputs': False, 'full_cuda_graph': False, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_capture_size': 0, 'local_cache_dir': None}
(EngineCore_DP0 pid=742) 2025-11-12 11:11:48,752	INFO worker.py:1833 -- Connecting to existing Ray cluster at address: 10.20.1.126:6379...
(EngineCore_DP0 pid=742) 2025-11-12 11:11:48,762	INFO worker.py:2013 -- Connected to Ray cluster.
(EngineCore_DP0 pid=742) /usr/local/lib/python3.12/dist-packages/ray/_private/worker.py:2052: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
(EngineCore_DP0 pid=742)   warnings.warn(
(EngineCore_DP0 pid=742) INFO 11-12 11:11:49 [ray_utils.py:378] No current placement group found. Creating a new placement group.
(EngineCore_DP0 pid=742) WARNING 11-12 11:11:49 [ray_utils.py:227] tensor_parallel_size=2 is bigger than a reserved number of GPUs (1 GPUs) in a node 105bc4e57711c6d8124de9ca4ea66c94df13653ce39ff1f0179e31c3. Tensor parallel workers can be spread out to 2+ nodes which can degrade the performance unless you have fast interconnect across nodes, like Infiniband. To resolve this issue, make sure you have more than 2 GPUs available at each node.
(EngineCore_DP0 pid=742) WARNING 11-12 11:11:49 [ray_utils.py:227] tensor_parallel_size=2 is bigger than a reserved number of GPUs (1 GPUs) in a node ead2c3ac59a39ba02e4fcabc212b72c1eab038705586247e7fb5bda7. Tensor parallel workers can be spread out to 2+ nodes which can degrade the performance unless you have fast interconnect across nodes, like Infiniband. To resolve this issue, make sure you have more than 2 GPUs available at each node.
(EngineCore_DP0 pid=742) INFO 11-12 11:11:49 [ray_distributed_executor.py:179] use_ray_spmd_worker: True
(EngineCore_DP0 pid=742) (pid=927) INFO 11-12 11:11:50 [__init__.py:225] Automatically detected platform rocm.
(EngineCore_DP0 pid=742) INFO 11-12 11:11:56 [ray_env.py:66] RAY_NON_CARRY_OVER_ENV_VARS from config: set()
(EngineCore_DP0 pid=742) INFO 11-12 11:11:56 [ray_env.py:69] Copying the following environment variables to workers: ['VLLM_USE_RAY_COMPILED_DAG', 'VLLM_USE_V1', 'LD_LIBRARY_PATH', 'VLLM_WORKER_MULTIPROC_METHOD', 'VLLM_USE_RAY_SPMD_WORKER']
(EngineCore_DP0 pid=742) INFO 11-12 11:11:56 [ray_env.py:74] If certain env vars should NOT be copied, add them to /root/.config/vllm/ray_non_carry_over_env_vars.json file
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) WARNING 11-12 11:11:56 [worker_base.py:309] Missing `shared_worker_lock` argument from executor. This argument is needed for mm_processor_cache_type='shm'.
(EngineCore_DP0 pid=742) (pid=233, ip=10.20.1.125) INFO 11-12 11:11:51 [__init__.py:225] Automatically detected platform rocm.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) [Gloo] Rank 0 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:11:57 [pynccl.py:111] vLLM is using nccl==2.26.6
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) [2025-11-12 11:11:57] corona:927:927 [0] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04/22.04/build/rccl/hipify/src/init.cc:140 NCCL WARN NUMA auto balancing enabled which can lead to variability in the RCCL performance! Disable by "sudo sysctl kernel.numa_balancing=0"
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Kernel version: 6.14.0-35-generic
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to enp165s0f1np1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Bootstrap: Using enp165s0f1np1:10.20.1.126<0>
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO ROCr version 1.18
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) [2025-11-12 11:11:57] corona:927:927 [0] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04/22.04/build/rccl/hipify/src/init.cc:140 NCCL WARN NUMA auto balancing enabled which can lead to variability in the RCCL performance! Disable by "sudo sysctl kernel.numa_balancing=0"
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Kernel version: 6.14.0-35-generic
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO RCCL version : 2.26.6-HEAD:f224e2c
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) HIP version  : 7.0.51831-a3e329ad8
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) ROCm version : 7.0.0.0-38-9428210
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) Hostname     : corona
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) Librccl path : /opt/rocm/lib/librccl.so.1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO NET/Plugin: Could not find: librccl-net.so. Using internal net plugin.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Failed to open libibverbs.so[.1]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to enp165s0f1np1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO NET/Socket : Using [0]enp165s0f1np1:10.20.1.126<0>
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO PROFILER/Plugin: Could not find: librccl-profiler.so. 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Using network Socket
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO [node_id = 2; gpu_id = 28209; unique_id = 938631638730650368; location_id = 1792; bdf = 1792; domain = 0; partition = 0], 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO initialized internal alternative rsmi functionality
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO ncclCommInitRank_impl comm 0x2083dd50 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 7000 commId 0x9110735f21e7cb02 - Init START
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Bootstrap timings total 0.059598 (create 0.000043, send 0.000099, recv 0.039276, ring 0.019702, delay 0.000001)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO initialized internal alternative rsmi functionality
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Setting affinity for GPU 0 to ffff,0000ffff
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO comm 0x2083dd50 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Channel 00/02 : 0 1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Channel 01/02 : 0 1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1 comm 0x2083dd50 nRanks 02 busId 7000
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO P2P Chunksize set to 131072
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Check P2P Type intraNodeP2pSupport 0 directMode 0
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:4796 [0] NCCL INFO [Proxy Service] Device 0 CPU core 42
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:4797 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 2
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:4798 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 42
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [receive] via NET/Socket/0 comm 0x2083dd50 nRanks 02
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [receive] via NET/Socket/0 comm 0x2083dd50 nRanks 02
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/Socket/0 comm 0x2083dd50 nRanks 02
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/Socket/0 comm 0x2083dd50 nRanks 02
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 0
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Connected all trees
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Connected binomial trees
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 256 | 256
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO CC Off, workFifoBytes 4194304
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO RCCL Unroll Factor (pre-set): 4
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL IINFO 11-12 11:12:00 [shm_broadcast.py:313] vLLM message queue communication handle: Handle(local_reader_ranks=[], buffer_handle=None, local_subscribe_addr=None, remote_subscribe_addr='tcp://10.20.1.126:36983', remote_addr_ipv6=False)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) NFO TUNER/Plugin: Could not find: librccl-tuner.so. Using internal tuner plugin.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO ncclCommInitRank_impl comm 0x2083dd50 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 7000 commId 0x9110735f21e7cb02 - Init COMPLETE
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) corona:927:927 [0] NCCL INFO Init timings - ncclCommInitRank_impl: rank 0 nranks 2 total 3.18 (kernels 2.81, alloc 0.26, bootstrap 0.06, allgathers 0.00, topo 0.04, graphs 0.00, connections 0.01, rest 0.00)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:12:00 [pynccl.py:111] vLLM is using nccl==2.26.6
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) Hostname     : bootes
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO TUNER/Plugin: Could not find: librccl-tuner.so. Using internal tuner plugin.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:12:00 [parallel_state.py:1325] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:12:00 [gpu_model_runner.py:2843] Starting to load model openai/gpt-oss-20b...
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:01 [rocm.py:298] Using Rocm Attention backend on V1 engine.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:01 [mxfp4.py:131] Using Triton backend
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) WARNING 11-12 11:12:01 [compilation.py:874] Op 'silu_and_mul' not present in model, enabling with '+silu_and_mul' has no effect
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) WARNING 11-12 11:12:01 [compilation.py:874] Op 'quant_fp8' not present in model, enabling with '+quant_fp8' has no effect
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:01 [weight_utils.py:419] Using model weights format ['*.safetensors']
Loading safetensors checkpoint shards:   0% Completed | 0/3 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  33% Completed | 1/3 [00:03<00:06,  3.06s/it]
Loading safetensors checkpoint shards:  67% Completed | 2/3 [00:06<00:03,  3.19s/it]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:10 [default_loader.py:314] Loading weights took 8.59 seconds
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) WARNING 11-12 11:11:57 [worker_base.py:309] Missing `shared_worker_lock` argument from executor. This argument is needed for mm_processor_cache_type='shm'.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [Gloo] Rank 1 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1 [repeated 11x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:11:57] bootes:233:233 [0] /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/out/ubuntu-22.04/22.04/build/rccl/hipify/src/init.cc:140 NCCL WARN NUMA auto balancing enabled which can lead to variability in the RCCL performance! Disable by "sudo sysctl kernel.numa_balancing=0"
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Kernel version: 6.14.0-35-generic
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to enp165s0f1np1 [repeated 2x across cluster]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Bootstrap: Using enp165s0f1np1:10.20.1.125<0>
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO ROCr version 1.18
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO RCCL version : 2.26.6-HEAD:f224e2c
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) HIP version  : 7.0.51831-a3e329ad8
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) ROCm version : 7.0.0.0-38-9428210
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) Librccl path : /opt/rocm/lib/librccl.so.1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO NET/Plugin: Could not find: librccl-net.so. Using internal net plugin.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Failed to open libibverbs.so[.1]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO NET/Socket : Using [0]enp165s0f1np1:10.20.1.125<0>
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO PROFILER/Plugin: Could not find: librccl-profiler.so. 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Using network Socket
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO [node_id = 2; gpu_id = 28209; unique_id = 5818553147422564044; location_id = 1792; bdf = 1792; domain = 0; partition = 0], 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO initialized internal alternative rsmi functionality [repeated 2x across cluster]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO ncclCommInitRank_impl comm 0x3ef16db0 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 7000 commId 0x9110735f21e7cb02 - Init START
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Bootstrap timings total 0.021221 (create 0.000055, send 0.000246, recv 0.000305, ring 0.000056, delay 0.000001)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Setting affinity for GPU 0 to ffff,0000ffff
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO comm 0x3ef16db0 rank 1 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1 comm 0x3ef16db0 nRanks 02 busId 7000
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO P2P Chunksize set to 131072
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:340 [0] NCCL INFO [Proxy Service] Device 0 CPU core 36
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:341 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 10
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:342 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 38
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [receive] via NET/Socket/0 comm 0x3ef16db0 nRanks 02 [repeated 2x across cluster]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [send] via NET/Socket/0 comm 0x3ef16db0 nRanks 02 [repeated 2x across cluster]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 0
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Connected all trees
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Connected binomial trees
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 256 | 256
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO RCCL Unroll Factor (pre-set): 4
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO ncclCommInitRank_impl comm 0x3ef16db0 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 7000 commId 0x9110735f21e7cb02 - Init COMPLETE
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) bootes:233:233 [0] NCCL INFO Init timings - ncclCommInitRank_impl: rank 1 nranks 2 total 3.18 (kernels 2.85, alloc 0.25, bootstrap 0.02, allgathers 0.00, topo 0.04, graphs 0.00, connections 0.01, rest 0.00)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:00 [parallel_state.py:1325] rank 1 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:00 [gpu_model_runner.py:2843] Starting to load model openai/gpt-oss-20b...
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:12:01 [rocm.py:298] Using Rocm Attention backend on V1 engine.
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:12:01 [mxfp4.py:131] Using Triton backend
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) WARNING 11-12 11:12:01 [compilation.py:874] Op 'silu_and_mul' not present in model, enabling with '+silu_and_mul' has no effect
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) WARNING 11-12 11:12:01 [compilation.py:874] Op 'quant_fp8' not present in model, enabling with '+quant_fp8' has no effect
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) INFO 11-12 11:12:01 [weight_utils.py:419] Using model weights format ['*.safetensors']
Loading safetensors checkpoint shards: 100% Completed | 3/3 [00:08<00:00,  2.89s/it]
Loading safetensors checkpoint shards: 100% Completed | 3/3 [00:08<00:00,  2.96s/it]
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=927) 
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) INFO 11-12 11:12:10 [gpu_model_runner.py:2904] Model loading took 7.2637 GiB and 9.390913 seconds
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [aiter] type hints mismatch, override to --> rmsnorm2d_fwd(input: torch.Tensor, weight: torch.Tensor, epsilon: float, use_model_sensitive_rmsnorm: int = 0) -> torch.Tensor
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17] WARNING core.py:622: type hints mismatch, override to --> rmsnorm2d_fwd(input: torch.Tensor, weight: torch.Tensor, epsilon: float, use_model_sensitive_rmsnorm: int = 0) -> torch.Tensor
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) *** SIGSEGV received at time=1762945937 on cpu 6 ***
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) PC: @     0x71bd29eb3ab5  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71d139f9e520  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd07e0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd07d8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd07d0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd07c8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0710  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0708       1472  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0718  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0700  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd04c0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd04b8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0408  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0400  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd03f8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd03f0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd03e8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd03e0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd03d8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd03d0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0318  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0310       3024  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0308  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0300  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd02f8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd02f0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd02e8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0320  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd02e0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0230       6944  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0228  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0220  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @     0x71bb1bfd0218  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125)     @ ... and at least 1000 more frames
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,145 E 233 233] logging.cc:474: *** SIGSEGV received at time=1762945937 on cpu 6 ***
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,146 E 233 233] logging.cc:474: PC: @     0x71bd29eb3ab5  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,146 E 233 233] logging.cc:474:     @     0x71d139f9e520  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,147 E 233 233] logging.cc:474:     @     0x71bb1bfd07e0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,149 E 233 233] logging.cc:474:     @     0x71bb1bfd07d8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,150 E 233 233] logging.cc:474:     @     0x71bb1bfd07d0  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,152 E 233 233] logging.cc:474:     @     0x71bb1bfd07c8  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,154 E 233 233] logging.cc:474:     @     0x71bb1bfd0710  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,156 E 233 233] logging.cc:474:     @     0x71bb1bfd0708       1472  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,158 E 233 233] logging.cc:474:     @     0x71bb1bfd0718  (unknown)  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,181 E 233 233] logging.cc:474:     @     0x71bb1bfd0310       3024  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,195 E 233 233] logging.cc:474:     @     0x71bb1bfd0230       6944  (unknown)
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) [2025-11-12 11:12:17,200 E 233 233] logging.cc:474:     @ ... and at least 1000 more frames
(EngineCore_DP0 pid=742) (RayWorkerWrapper pid=233, ip=10.20.1.125) Fatal Python error: Segmentation fault
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.11
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
  Name:                    AMD EPYC 9115 16-Core Processor    
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD EPYC 9115 16-Core Processor    
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
  Max Clock Freq. (MHz):   4118                               
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
      Size:                    131577576(0x7d7b6e8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    131577576(0x7d7b6e8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131577576(0x7d7b6e8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    131577576(0x7d7b6e8) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    AMD EPYC 9115 16-Core Processor    
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD EPYC 9115 16-Core Processor    
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4118                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
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
      Size:                    132056036(0x7df03e4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    132056036(0x7df03e4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    132056036(0x7df03e4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    132056036(0x7df03e4) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 3                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-0d06b080997bb300               
  Marketing Name:                                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30033(0x7551)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2350                               
  BDFID:                   1792                               
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
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
  Packet Processor uCode:: 752                                
  SDMA engine uCode::      749                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    33406976(0x1fdc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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
*** Done *** 
```