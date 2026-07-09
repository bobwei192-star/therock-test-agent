# [Issue]: Unable to Run vLLM Inference on AMD Ryzen AI MAX+ 395

- **Issue #:** 4909
- **State:** closed
- **Created:** 2025-06-10T07:36:05Z
- **Updated:** 2025-11-25T03:20:26Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4909

### Problem Description

I attempted to use vLLM for model inference on an AMD Ryzen AI MAX+ 395 (gfx1151) with ROCm 6.4.1, as it appears that ROCm 6.4.1 has added support for this GPU.

I pulled and ran the docker image rocm/vllm-dev:rocm6.4.1_navi_ubuntu24.04_py3.12_pytorch_2.6_vllm_0.8.5 (and also tried rocm/vllm-dev:rocm6.4.1_navi_ubuntu24.04_py3.12_pytorch_2.7_vllm_0.8.5), but encountered an "invalid device function" error during inference.

### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### ROCm Version

ROCm 6.4.1

### Steps to Reproduce

1. Downloaded the model files from `https://huggingface.co/Qwen/Qwen3-1.7B` to `/home/flintylemming/models/Qwen3-1.7B`.
2. Pulled the ROCm 6.4.1 Navi vLLM Docker image:
   ```bash
   sudo docker pull rocm/vllm-dev:rocm6.41_navi_ubuntu24.04_py3.12_pytorch_2.7_vllm_0.8.5
   ```
3. Followed the documentation at [Radeon ROCm vLLM Docker guide](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/advanced/vllm/build-docker-image.html) to run the container with the necessary path mapping.

   ```bash
   sudo docker run -it   \
      --privileged   \
      --device=/dev/kfd   \
      --device=/dev/dri   \
      --network=host   \
      --group-add sudo   \
      -w /app/vllm/ \
      -v /home/flintylemming/models:/models  \
      --name vllm \
      rocm/vllm-dev:rocm6.4.1_navi_ubuntu24.04_py3.12_pytorch_2.7_vllm_0.8.5   \
      /bin/bash
   ```

4. Ran the following command to perform model inference:

   ```bash
   vllm serve /models/Qwen3-1.7B
   ```
The full error info below

<details>

<summary>vLLM output</summary>
<pre><code>
INFO 06-10 07:31:36 [__init__.py:239] Automatically detected platform rocm.
INFO 06-10 07:31:45 [api_server.py:1042] vLLM API server version 0.7.4.dev1638+ga7ddaa9b9
INFO 06-10 07:31:45 [api_server.py:1043] args: Namespace(subparser='serve', model_tag='/models/Qwen3-1.7B', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/models/Qwen3-1.7B', task='auto', tokenizer=None, tokenizer_mode='auto', trust_remote_code=False, dtype='auto', seed=None, hf_config_path=None, allowed_local_media_path='', revision=None, code_revision=None, rope_scaling={}, rope_theta=None, tokenizer_revision=None, max_model_len=None, quantization=None, enforce_eager=False, max_seq_len_to_capture=8192, max_logprobs=20, disable_sliding_window=False, disable_cascade_attn=False, skip_tokenizer_init=False, enable_prompt_embeds=False, served_model_name=None, disable_async_output_proc=False, config_format='auto', hf_token=None, hf_overrides={}, override_neuron_config={}, override_pooler_config=None, logits_processor_pattern=None, generation_config='auto', override_generation_config={}, enable_sleep_mode=False, model_impl='auto', load_format='auto', download_dir=None, model_loader_extra_config={}, ignore_patterns=None, use_tqdm_on_load=True, qlora_adapter_name_or_path=None, pt_load_map_location='cpu', guided_decoding_backend='auto', guided_decoding_disable_fallback=False, guided_decoding_disable_any_whitespace=False, guided_decoding_disable_additional_properties=False, enable_reasoning=None, reasoning_parser='', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, worker_cls='auto', worker_extension_cls='', block_size=None, gpu_memory_utilization=0.9, swap_space=4, kv_cache_dtype='auto', num_gpu_blocks_override=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', cpu_offload_gb=0, calculate_kv_scales=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config={}, limit_mm_per_prompt={}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=None, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=None, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', speculative_config=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, max_num_batched_tokens=None, max_num_seqs=None, max_num_partial_prefills=1, max_long_partial_prefills=1, cuda_graph_sizes=[512], long_prefill_token_threshold=0, num_lookahead_slots=0, scheduler_delay_factor=0.0, preemption_mode=None, num_scheduler_steps=1, multi_step_stream_outputs=True, scheduling_policy='fcfs', enable_chunked_prefill=None, disable_chunked_mm_input=False, scheduler_cls='vllm.core.scheduler.Scheduler', compilation_config=None, kv_transfer_config=None, kv_events_config=None, additional_config=None, use_v2_block_manager=True, disable_log_stats=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False, dispatch_function=<function ServeSubcommand.cmd at 0x74229577a3e0>)
INFO 06-10 07:31:56 [config.py:753] This model supports multiple tasks: {'classify', 'reward', 'generate', 'score', 'embed'}. Defaulting to 'generate'.
INFO 06-10 07:31:56 [arg_utils.py:1561] rocm is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
WARNING 06-10 07:31:56 [arg_utils.py:1402] The model has a long context length (40960). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value.
INFO 06-10 07:31:56 [config.py:1861] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-10 07:31:56 [config.py:1832] Disabled the custom all-reduce kernel because it is not working correctly when using two AMD Navi GPUs.
INFO 06-10 07:31:56 [api_server.py:246] Started engine process with PID 165
INFO 06-10 07:31:58 [__init__.py:239] Automatically detected platform rocm.
INFO 06-10 07:32:06 [llm_engine.py:240] Initializing a V0 LLM engine (v0.7.4.dev1638+ga7ddaa9b9) with config: model='/models/Qwen3-1.7B', speculative_config=None, tokenizer='/models/Qwen3-1.7B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=None, served_model_name=/models/Qwen3-1.7B, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
INFO 06-10 07:32:06 [rocm.py:211] None is not supported in AMD GPUs.
INFO 06-10 07:32:06 [rocm.py:212] Using ROCmFlashAttention backend.
INFO 06-10 07:32:06 [parallel_state.py:1004] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0
INFO 06-10 07:32:06 [model_runner.py:1161] Starting to load model /models/Qwen3-1.7B...
/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_device.py:104: UserWarning: Ignoring invalid value for boolean flag AMD_SERIALIZE_KERNEL: 3valid values are 0 or 1. (Triggered internally at /app/pytorch/c10/util/env.cpp:86.)
  return func(*args, **kwargs)
ERROR 06-10 07:32:06 [engine.py:448] HIP error: invalid device function
ERROR 06-10 07:32:06 [engine.py:448] HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
ERROR 06-10 07:32:06 [engine.py:448] For debugging consider passing AMD_SERIALIZE_KERNEL=3
ERROR 06-10 07:32:06 [engine.py:448] Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.
ERROR 06-10 07:32:06 [engine.py:448] Traceback (most recent call last):
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 06-10 07:32:06 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 06-10 07:32:06 [engine.py:448]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 06-10 07:32:06 [engine.py:448]     return cls(
ERROR 06-10 07:32:06 [engine.py:448]            ^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 06-10 07:32:06 [engine.py:448]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/llm_engine.py", line 275, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config)
ERROR 06-10 07:32:06 [engine.py:448]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/executor/executor_base.py", line 52, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self._init_executor()
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 06-10 07:32:06 [engine.py:448]     self.collective_rpc("load_model")
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 06-10 07:32:06 [engine.py:448]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-10 07:32:06 [engine.py:448]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/utils.py", line 2645, in run_method
ERROR 06-10 07:32:06 [engine.py:448]     return func(*args, **kwargs)
ERROR 06-10 07:32:06 [engine.py:448]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/worker/worker.py", line 231, in load_model
ERROR 06-10 07:32:06 [engine.py:448]     self.model_runner.load_model()
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/worker/model_runner.py", line 1164, in load_model
ERROR 06-10 07:32:06 [engine.py:448]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 06-10 07:32:06 [engine.py:448]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 06-10 07:32:06 [engine.py:448]     return loader.load_model(vllm_config=vllm_config)
ERROR 06-10 07:32:06 [engine.py:448]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/model_loader/loader.py", line 453, in load_model
ERROR 06-10 07:32:06 [engine.py:448]     model = _initialize_model(vllm_config=vllm_config)
ERROR 06-10 07:32:06 [engine.py:448]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
ERROR 06-10 07:32:06 [engine.py:448]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 06-10 07:32:06 [engine.py:448]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 269, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self.model = Qwen3Model(vllm_config=vllm_config,
ERROR 06-10 07:32:06 [engine.py:448]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/compilation/decorators.py", line 151, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 241, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     super().__init__(vllm_config=vllm_config,
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/compilation/decorators.py", line 151, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen2.py", line 305, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 06-10 07:32:06 [engine.py:448]                                                     ^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 610, in make_layers
ERROR 06-10 07:32:06 [engine.py:448]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 06-10 07:32:06 [engine.py:448]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen2.py", line 307, in <lambda>
ERROR 06-10 07:32:06 [engine.py:448]     lambda prefix: decoder_layer_type(config=config,
ERROR 06-10 07:32:06 [engine.py:448]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 172, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self.self_attn = Qwen3Attention(
ERROR 06-10 07:32:06 [engine.py:448]                      ^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 108, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     self.rotary_emb = get_rope(
ERROR 06-10 07:32:06 [engine.py:448]                       ^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 1502, in get_rope
ERROR 06-10 07:32:06 [engine.py:448]     rotary_emb = RotaryEmbedding(head_size, rotary_dim, max_position, base,
ERROR 06-10 07:32:06 [engine.py:448]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 111, in __init__
ERROR 06-10 07:32:06 [engine.py:448]     cache = self._compute_cos_sin_cache()
ERROR 06-10 07:32:06 [engine.py:448]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 128, in _compute_cos_sin_cache
ERROR 06-10 07:32:06 [engine.py:448]     inv_freq = self._compute_inv_freq(self.base)
ERROR 06-10 07:32:06 [engine.py:448]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 122, in _compute_inv_freq
ERROR 06-10 07:32:06 [engine.py:448]     inv_freq = 1.0 / (base**(torch.arange(
ERROR 06-10 07:32:06 [engine.py:448]                              ^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448]   File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_device.py", line 104, in __torch_function__
ERROR 06-10 07:32:06 [engine.py:448]     return func(*args, **kwargs)
ERROR 06-10 07:32:06 [engine.py:448]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 06-10 07:32:06 [engine.py:448] RuntimeError: HIP error: invalid device function
ERROR 06-10 07:32:06 [engine.py:448] HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
ERROR 06-10 07:32:06 [engine.py:448] For debugging consider passing AMD_SERIALIZE_KERNEL=3
ERROR 06-10 07:32:06 [engine.py:448] Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.
ERROR 06-10 07:32:06 [engine.py:448] 
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/opt/conda/envs/py_3.12/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/opt/conda/envs/py_3.12/lib/python3.12/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 450, in run_mp_engine
    raise e
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
    return cls(
           ^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
    self.engine = LLMEngine(*args, **kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/engine/llm_engine.py", line 275, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
    self.collective_rpc("load_model")
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/utils.py", line 2645, in run_method
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/worker/worker.py", line 231, in load_model
    self.model_runner.load_model()
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/worker/model_runner.py", line 1164, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
    return loader.load_model(vllm_config=vllm_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/model_loader/loader.py", line 453, in load_model
    model = _initialize_model(vllm_config=vllm_config)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
    return model_class(vllm_config=vllm_config, prefix=prefix)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 269, in __init__
    self.model = Qwen3Model(vllm_config=vllm_config,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/compilation/decorators.py", line 151, in __init__
    old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 241, in __init__
    super().__init__(vllm_config=vllm_config,
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/compilation/decorators.py", line 151, in __init__
    old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen2.py", line 305, in __init__
    self.start_layer, self.end_layer, self.layers = make_layers(
                                                    ^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 610, in make_layers
    maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen2.py", line 307, in <lambda>
    lambda prefix: decoder_layer_type(config=config,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 172, in __init__
    self.self_attn = Qwen3Attention(
                     ^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/models/qwen3.py", line 108, in __init__
    self.rotary_emb = get_rope(
                      ^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 1502, in get_rope
    rotary_emb = RotaryEmbedding(head_size, rotary_dim, max_position, base,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 111, in __init__
    cache = self._compute_cos_sin_cache()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 128, in _compute_cos_sin_cache
    inv_freq = self._compute_inv_freq(self.base)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/model_executor/layers/rotary_embedding.py", line 122, in _compute_inv_freq
    inv_freq = 1.0 / (base**(torch.arange(
                             ^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/utils/_device.py", line 104, in __torch_function__
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

[rank0]:[W610 07:32:07.050956870 ProcessGroupNCCL.cpp:1476] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
Traceback (most recent call last):
  File "/opt/conda/envs/py_3.12/bin/vllm", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 53, in main
    args.dispatch_function(args)
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run
    return __asyncio.run(
           ^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
           ^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 1077, in run_server
    async with build_async_engine_client(args) as engine_client:
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 269, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
</code><pre>
</details>


Additionally, I tried adding AMD_SERIALIZE_KERNEL=3 to get more information (by executing `AMD_SERIALIZE_KERNEL=3 vllm serve /models/Qwen3-1.7B` inside the container). However, the error message remains the same as without the parameter. Could you please advise where this parameter should be placed?  

This is my first time using ROCm. If anything is unclear or if you need additional information from me, please let me know—I’m happy to provide it.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>

<summary>rocminfo output</summary>

```
ROCk module version 6.12.12 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
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
  Max Clock Freq. (MHz):   5185                               
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
      Size:                    65464680(0x3e6e968) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65464680(0x3e6e968) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65464680(0x3e6e968) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65464680(0x3e6e968) KB             
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
    L3:                      16384(0x4000) KB                   
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
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 26                                 
  SDMA engine uCode::      14                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    67108864(0x4000000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    67108864(0x4000000) KB             
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***
```

</details>

### Additional Information

_No response_