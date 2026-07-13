# [Issue]: HIP error: an illegal memory access was encountered, hipErrorIllegalAddress (on RX 6700 XT, ROCm 7.2)

- **Issue #:** 6003
- **State:** open
- **Created:** 2026-02-26T09:52:15Z
- **Updated:** 2026-04-01T16:48:17Z
- **Labels:** Under Investigation, status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6003

### Problem Description

I keep getting memory related crashes in ComfyUI (and PyTorch in general). It's been happening since at least ROCm 7.0. It's random and unpredictable, I don't know of any consistent way to reproduce it. Sometimes it will happen after long usage, sometimes right away, sometimes it doesn't happen at all.

I'm currently using ROCm 7.2, I installed the following packages:
```
https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2/torch-2.9.1%2Brocm7.2.0.lw.git7e1940d4-cp313-cp313-linux_x86_64.whl
https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2/torchvision-0.24.0%2Brocm7.2.0.gitb919bd0c-cp313-cp313-linux_x86_64.whl
https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2/triton-3.5.1%2Brocm7.2.0.gita272dfa8-cp313-cp313-linux_x86_64.whl
https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2/torchaudio-2.9.0%2Brocm7.2.0.gite3c6ee2b-cp313-cp313-linux_x86_64.whl
```

Previously I used official builds from PyTorch and the issue happened there too.

Full ComfyUI log (I only removed some logs from custom nodes to make it more readable):
```
$ HSA_OVERRIDE_GFX_VERSION=10.3.0 python main.py

[START] Security scan
[DONE] Security scan
## ComfyUI-Manager: installing dependencies done.
** Platform: Linux
** Python version: 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0]
** Python executable: /mnt/AI/ComfyUI/env/bin/python
** ComfyUI Path: /mnt/AI/ComfyUI
** ComfyUI Base Folder Path: /mnt/AI/ComfyUI
** User directory: /mnt/AI/ComfyUI/user
** ComfyUI-Manager config path: /mnt/AI/ComfyUI/user/__manager/config.ini
** Log path: /mnt/AI/ComfyUI/user/comfyui.log

Checkpoint files will always be loaded safely.
Found comfy_kitchen backend cuda: {'available': True, 'disabled': True, 'unavailable_reason': None, 'capabilities': ['apply_rope', 'apply_rope1', 'dequantize_nvfp4', 'dequantize_per_tensor_fp8', 'quantize_nvfp4', 'quantize_per_tensor_fp8']}
Found comfy_kitchen backend triton: {'available': True, 'disabled': True, 'unavailable_reason': None, 'capabilities': ['apply_rope', 'apply_rope1', 'dequantize_nvfp4', 'dequantize_per_tensor_fp8', 'quantize_nvfp4', 'quantize_per_tensor_fp8']}
Found comfy_kitchen backend eager: {'available': True, 'disabled': False, 'unavailable_reason': None, 'capabilities': ['apply_rope', 'apply_rope1', 'dequantize_nvfp4', 'dequantize_per_tensor_fp8', 'quantize_nvfp4', 'quantize_per_tensor_fp8', 'scaled_mm_nvfp4']}
Total VRAM 12272 MB, total RAM 28026 MB
pytorch version: 2.9.1+rocm7.2.0.git7e1940d4
AMD arch: gfx1030
ROCm version: (7, 2)
Set vram state to: NORMAL_VRAM
Device: cuda:0 AMD Radeon RX 6700 XT : native
Using async weight offloading with 2 streams
Enabled pinned memory 26624.0
Using sub quadratic optimization for attention, if you have memory or speed issues try using: --use-split-cross-attention
Python version: 3.13.5 (main, Jun 25 2025, 18:55:22) [GCC 14.2.0]
ComfyUI version: 0.13.0
ComfyUI frontend version: 1.38.13
[Prompt Server] web root: /mnt/AI/ComfyUI/env/lib/python3.13/site-packages/comfyui_frontend_package/static
Using sub quadratic optimization for attention, if you have memory or speed issues try using: --use-split-cross-attention
ComfyUI-GGUF: Allowing full torch compile
Context impl SQLiteImpl.
Will assume non-transactional DDL.
Assets scan(roots=['models']) completed in 0.502s (created=0, skipped_existing=674, orphans_pruned=0, total_seen=747)
Starting server
To see the GUI go to: http://127.0.0.1:8188
[DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/groupNode.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/widgetInputs.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui/components/button.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui/components/buttonGroup.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
got prompt
Using split attention in VAE
Using split attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.float32
Found quantization metadata version 1
Using MixedPrecisionOps for text encoder
CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cpu, dtype: torch.float16
Requested to load Flux2TEModel_
loaded completely; 10800.80 MB usable, 8263.34 MB loaded, full load: True
gguf qtypes: F32 (80), Q8_0 (112), BF16 (9)
model weight dtype torch.float16, manual cast: None
model_type FLUX
Requested to load Flux2
!!! Exception during processing !!! HIP error: an illegal memory access was encountered
Search for `hipErrorIllegalAddress' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__HIPRT__TYPES.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

Traceback (most recent call last):
  File "/mnt/AI/ComfyUI/execution.py", line 530, in execute
    output_data, output_ui, has_subgraph, has_pending_tasks = await get_output_data(prompt_id, unique_id, obj, input_data_all, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/execution.py", line 334, in get_output_data
    return_values = await _async_map_node_over_list(prompt_id, unique_id, obj, input_data_all, obj.FUNCTION, allow_interrupt=True, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/custom_nodes/ComfyUI-Lora-Manager/py/metadata_collector/metadata_hook.py", line 168, in async_map_node_over_list_with_metadata
    results = await original_map_node_over_list(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
    )
    ^
  File "/mnt/AI/ComfyUI/execution.py", line 308, in _async_map_node_over_list
    await process_inputs(input_dict, i)
  File "/mnt/AI/ComfyUI/execution.py", line 296, in process_inputs
    result = f(**inputs)
  File "/mnt/AI/ComfyUI/comfy_api/internal/__init__.py", line 149, in wrapped_func
    return method(locked_class, **inputs)
  File "/mnt/AI/ComfyUI/comfy_api/latest/_io.py", line 1710, in EXECUTE_NORMALIZED
    to_return = cls.execute(*args, **kwargs)
  File "/mnt/AI/ComfyUI/comfy_extras/nodes_custom_sampler.py", line 963, in execute
    samples = guider.sample(noise.generate_noise(latent), latent_image, sampler, sigmas, denoise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=noise.seed)
  File "/mnt/AI/ComfyUI/comfy/samplers.py", line 1049, in sample
    output = executor.execute(noise, latent_image, sampler, sigmas, denoise_mask, callback, disable_pbar, seed, latent_shapes=latent_shapes)
  File "/mnt/AI/ComfyUI/comfy/patcher_extension.py", line 112, in execute
    return self.original(*args, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/samplers.py", line 983, in outer_sample
    self.inner_model, self.conds, self.loaded_models = comfy.sampler_helpers.prepare_sampling(self.model_patcher, noise.shape, self.conds, self.model_options)
                                                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/sampler_helpers.py", line 130, in prepare_sampling
    return executor.execute(model, noise_shape, conds, model_options=model_options, force_full_load=force_full_load)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/patcher_extension.py", line 112, in execute
    return self.original(*args, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/sampler_helpers.py", line 138, in _prepare_sampling
    comfy.model_management.load_models_gpu([model] + models, memory_required=memory_required + inference_memory, minimum_memory_required=minimum_memory_required + inference_memory, force_full_load=force_full_load)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/model_management.py", line 716, in load_models_gpu
    free_memory(total_memory_required[device] * 1.1 + extra_mem, device, for_dynamic=free_for_dynamic, ram_required=total_ram_required[device])
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/model_management.py", line 635, in free_memory
    if memory_to_free > 0 and current_loaded_models[i].model_unload(memory_to_free):
                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/model_management.py", line 551, in model_unload
    self.model.detach(unpatch_weights)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/model_patcher.py", line 1021, in detach
    self.unpatch_model(self.offload_device, unpatch_weights=unpatch_all)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/comfy/model_patcher.py", line 886, in unpatch_model
    self.model.to(device_to)
    ~~~~~~~~~~~~~^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1371, in to
    return self._apply(convert)
           ~~~~~~~~~~~^^^^^^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
    ~~~~~~~~~~~~~^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
    ~~~~~~~~~~~~~^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
    ~~~~~~~~~~~~~^^^^
  [Previous line repeated 4 more times]
  File "/mnt/AI/ComfyUI/comfy/ops.py", line 914, in _apply
    self.register_parameter(key, torch.nn.Parameter(fn(param), requires_grad=False))
                                                    ~~^^^^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1357, in convert
    return t.to(
           ~~~~^
        device,
        ^^^^^^^
        dtype if t.is_floating_point() or t.is_complex() else None,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        non_blocking,
        ^^^^^^^^^^^^^
    )
    ^
torch.AcceleratorError: HIP error: an illegal memory access was encountered
Search for `hipErrorIllegalAddress' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__HIPRT__TYPES.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.


Prompt executed in 94.48 seconds
Exception in thread Thread-2 (prompt_worker):
Traceback (most recent call last):
  File "/usr/lib/python3.13/threading.py", line 1043, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/usr/lib/python3.13/threading.py", line 994, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/main.py", line 302, in prompt_worker
    comfy.model_management.soft_empty_cache()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/mnt/AI/ComfyUI/comfy/model_management.py", line 1702, in soft_empty_cache
    torch.cuda.synchronize()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/cuda/__init__.py", line 1082, in synchronize
    with torch.cuda.device(device):
         ~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/cuda/__init__.py", line 529, in __init__
    self.idx = _get_device_index(device, optional=True)
               ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/cuda/_utils.py", line 373, in _get_device_index
    return _torch_get_device_index(device, optional, allow_cpu)
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/_utils.py", line 870, in _get_device_index
    device_idx = _get_current_device_index()
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/_utils.py", line 807, in _get_current_device_index
    return _get_device_attr(lambda m: m.current_device())
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/_utils.py", line 792, in _get_device_attr
    return get_member(torch.cuda)
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/_utils.py", line 807, in <lambda>
    return _get_device_attr(lambda m: m.current_device())
                                      ~~~~~~~~~~~~~~~~^^
  File "/mnt/AI/ComfyUI/env/lib/python3.13/site-packages/torch/cuda/__init__.py", line 1070, in current_device
    return torch._C._cuda_getDevice()
           ~~~~~~~~~~~~~~~~~~~~~~~~^^
torch.AcceleratorError: HIP error: an illegal memory access was encountered
Search for `hipErrorIllegalAddress' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__HIPRT__TYPES.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.
```

### Operating System

Debian 13

### CPU

Intel i5-4690K

### GPU

RX 6700 XT

### ROCm Version

ROCm 7.2

### ROCm Component

_No response_

### Steps to Reproduce

It happens with different workflows and different models. There isn't a simple, consistent way to reproduce it.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

I set the `HSA_OVERRIDE_GFX_VERSION=10.3.0` environment variable, since it's the only way for RX 6700 XT to work in ROCm. It works fine, except for the occasional random crashes.

I've heard that setting some kernel parameter might fix those crashes, but I didn't try it, because I don't understand what it does or what the downsides are.

I have ROCm 7.1 from AMD's repo installed on my system, but PyTorch uses its own version (ROCm 7.2 in this case), so it shouldn't matter here.