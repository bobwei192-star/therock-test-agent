# [Issue]: Illegal memory access torch.AcceleratorError: HIP error: an illegal memory access `hipErrorIllegalAddress'

- **Issue #:** 5742
- **State:** closed
- **Created:** 2025-12-04T23:29:41Z
- **Updated:** 2026-02-11T15:28:58Z
- **Labels:** status: triage
- **Assignees:** zichguan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5742

### Problem Description

Hello,

I'm running into this error in regular basis (comfyui ubuntu). 
I believe that it the fact I'm juggling between 2 simple workflow
1 ollama vision model (qwen 3vl and gemma3) 
1 Inference wf, using netayume lumina 2 model


# ComfyUI Error Report
## Error Details
- **Node ID:** 25
- **Node Type:** KSampler
- **Exception Type:** torch.AcceleratorError
- **Exception Message:** HIP error: an illegal memory access was encountered
Search for `hipErrorIllegalAddress' in https://rocm.docs.amd.com/projects/HIP/en/latest/index.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.


## Stack Trace
```
  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 515, in execute
    output_data, output_ui, has_subgraph, has_pending_tasks = await get_output_data(prompt_id, unique_id, obj, input_data_all, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 329, in get_output_data
    return_values = await _async_map_node_over_list(prompt_id, unique_id, obj, input_data_all, obj.FUNCTION, allow_interrupt=True, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 303, in _async_map_node_over_list
    await process_inputs(input_dict, i)

  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 291, in process_inputs
    result = f(**inputs)

  File "/home/zeuss194/COMFY/ComfyUI/nodes.py", line 1538, in sample
    return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)

  File "/home/zeuss194/COMFY/ComfyUI/nodes.py", line 1505, in common_ksampler
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/sample.py", line 60, in sample
    samples = sampler.sample(noise, positive, negative, cfg=cfg, latent_image=latent_image, start_step=start_step, last_step=last_step, force_full_denoise=force_full_denoise, denoise_mask=noise_mask, sigmas=sigmas, callback=callback, disable_pbar=disable_pbar, seed=seed)

  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes/smZNodes.py", line 131, in KSampler_sample
    return orig_fn(*args, **kwargs)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 1163, in sample
    return sample(self.model, noise, positive, negative, cfg, self.device, sampler, sigmas, self.model_options, latent_image=latent_image, denoise_mask=denoise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)

  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes/smZNodes.py", line 149, in sample
    return orig_fn(*args, **kwargs)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 1053, in sample
    return cfg_guider.sample(noise, latent_image, sampler, sigmas, denoise_mask, callback, disable_pbar, seed)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 1035, in sample
    output = executor.execute(noise, latent_image, sampler, sigmas, denoise_mask, callback, disable_pbar, seed, latent_shapes=latent_shapes)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/patcher_extension.py", line 112, in execute
    return self.original(*args, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^

  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 997, in outer_sample
    output = self.inner_sample(noise, latent_image, device, sampler, sigmas, denoise_mask, callback, disable_pbar, seed, latent_shapes=latent_shapes)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 980, in inner_sample
    samples = executor.execute(self, sigmas, extra_args, callback, noise, latent_image, denoise_mask, disable_pbar)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/patcher_extension.py", line 112, in execute
    return self.original(*args, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^

  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes/smZNodes.py", line 114, in KSAMPLER_sample
    return orig_fn(*args, **kwargs)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 752, in sample
    samples = self.sampler_function(model_k, noise, sigmas, extra_args=extra_args, callback=k_callback, disable=disable_pbar, **self.extra_options)

  File "/home/zeuss194/COMFY/ComfyUI/Comfyenv313/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/k_diffusion/sampling.py", line 212, in sample_euler_ancestral
    return sample_euler_ancestral_RF(model, x, sigmas, extra_args, callback, disable, eta, s_noise, noise_sampler)

  File "/home/zeuss194/COMFY/ComfyUI/Comfyenv313/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)

  File "/home/zeuss194/COMFY/ComfyUI/comfy/k_diffusion/sampling.py", line 246, in sample_euler_ancestral_RF
    if sigmas[i + 1] == 0:
       ^^^^^^^^^^^^^^^^^^

```
## System Information
- **ComfyUI Version:** 0.3.76
- **Arguments:** main.py
- **OS:** linux
- **Python Version:** 3.13.10 (main, Dec  3 2025, 08:59:02) [GCC 13.3.0]
- **Embedded Python:** false
- **PyTorch Version:** 2.10.0.dev20251124+rocm7.1
## Devices

- **Name:** cuda:0 AMD Radeon AI PRO R9700 : native
  - **Type:** cuda
  - **VRAM Total:** 34208743424
  - **VRAM Free:** 34131148800
  - **Torch VRAM Total:** 0
  - **Torch VRAM Free:** 0

## Logs
```
2025-12-04T23:43:13.640095 - [92m[rgthree-comfy] Loaded 48 magnificent nodes. 🎉[0m2025-12-04T23:43:13.640111 - 
2025-12-04T23:43:13.640126 - 
2025-12-04T23:43:13.640158 - [33m[rgthree-comfy] ComfyUI's new Node 2.0 rendering may be incompatible with some rgthree-comfy nodes and features, breaking some rendering as well as losing the ability to access a node's properties (a vital part of many nodes). It also appears to run MUCH more slowly spiking CPU usage and causing jankiness and unresponsiveness, especially with large workflows. Personally I am not planning to use the new Nodes 2.0 and, unfortunately, am not able to invest the time to investigate and overhaul rgthree-comfy where needed. If you have issues when Nodes 2.0 is enabled, I'd urge you to switch it off as well and join me in hoping ComfyUI is not planning to deprecate the existing, stable canvas rendering all together.
[0m2025-12-04T23:43:13.640175 - 
2025-12-04T23:43:13.644630 - --------------------- Jake Upgrade Nodes ---------------------2025-12-04T23:43:13.644659 - 
2025-12-04T23:43:13.644822 - 🔶 Version 2.3.142025-12-04T23:43:13.644842 - 
2025-12-04T23:43:13.645267 - 🔶 Config file loaded successfully2025-12-04T23:43:13.645288 - 
2025-12-04T23:43:13.645333 - 🔶 Using standard version of RandomPrompter2025-12-04T23:43:13.645350 - 
2025-12-04T23:43:13.653082 - 🔶 All main modules loaded2025-12-04T23:43:13.653111 - 
2025-12-04T23:43:13.653129 - 🔶 No deprecated nodes loaded2025-12-04T23:43:13.653144 - 
2025-12-04T23:43:13.653606 - 🔶 Total nodes: 1042025-12-04T23:43:13.653628 - 
2025-12-04T23:43:13.653644 - --------------------------------------------------------------2025-12-04T23:43:13.653657 - 
2025-12-04T23:43:13.655457 - AMD GPU Monitor thread started2025-12-04T23:43:13.655490 - 
2025-12-04T23:43:13.655712 - Using AMD SMI tool: /opt/rocm/bin/rocm-smi2025-12-04T23:43:13.655818 - AMD GPU Monitor: Web directory set to /home/zeuss194/COMFY/ComfyUI/custom_nodes/amdgpumonitor/web2025-12-04T23:43:13.655846 - 
2025-12-04T23:43:13.655952 - 
2025-12-04T23:43:13.658290 - [MultiGPU Core Patching] Patching mm.soft_empty_cache for Comprehensive Memory Management (VRAM + CPU + Store Pruning)
2025-12-04T23:43:13.659407 - [MultiGPU Core Patching] Patching mm.get_torch_device, mm.text_encoder_device, mm.unet_offload_device
2025-12-04T23:43:13.659615 - [MultiGPU DEBUG] Initial current_device: cuda:0
2025-12-04T23:43:13.659766 - [MultiGPU DEBUG] Initial current_text_encoder_device: cuda:0
2025-12-04T23:43:13.659905 - [MultiGPU DEBUG] Initial current_unet_offload_device: cpu
2025-12-04T23:43:13.662389 - [MultiGPU] Initiating custom_node Registration. . .
2025-12-04T23:43:13.662549 - -----------------------------------------------
2025-12-04T23:43:13.662705 - custom_node                   Found     Nodes
2025-12-04T23:43:13.662845 - -----------------------------------------------
2025-12-04T23:43:13.663481 - ComfyUI-LTXVideo                  N         0
2025-12-04T23:43:13.663652 - ComfyUI-Florence2                 Y         2
2025-12-04T23:43:13.663801 - ComfyUI_bitsandbytes_NF4          N         0
2025-12-04T23:43:13.663946 - x-flux-comfyui                    N         0
2025-12-04T23:43:13.664094 - ComfyUI-MMAudio                   N         0
2025-12-04T23:43:13.664238 - ComfyUI-GGUF                      Y        18
2025-12-04T23:43:13.664379 - PuLID_ComfyUI                     N         0
2025-12-04T23:43:13.664521 - ComfyUI-WanVideoWrapper           N         0
2025-12-04T23:43:13.664673 - -----------------------------------------------
2025-12-04T23:43:13.664855 - [MultiGPU] Registration complete. Final mappings: CheckpointLoaderAdvancedMultiGPU, CheckpointLoaderAdvancedDisTorch2MultiGPU, UNetLoaderLP, UNETLoaderMultiGPU, VAELoaderMultiGPU, CLIPLoaderMultiGPU, DualCLIPLoaderMultiGPU, TripleCLIPLoaderMultiGPU, QuadrupleCLIPLoaderMultiGPU, CLIPVisionLoaderMultiGPU, CheckpointLoaderSimpleMultiGPU, ControlNetLoaderMultiGPU, DiffusersLoaderMultiGPU, DiffControlNetLoaderMultiGPU, UNETLoaderDisTorch2MultiGPU, VAELoaderDisTorch2MultiGPU, CLIPLoaderDisTorch2MultiGPU, DualCLIPLoaderDisTorch2MultiGPU, TripleCLIPLoaderDisTorch2MultiGPU, QuadrupleCLIPLoaderDisTorch2MultiGPU, CLIPVisionLoaderDisTorch2MultiGPU, CheckpointLoaderSimpleDisTorch2MultiGPU, ControlNetLoaderDisTorch2MultiGPU, DiffusersLoaderDisTorch2MultiGPU, DiffControlNetLoaderDisTorch2MultiGPU, Florence2ModelLoaderMultiGPU, DownloadAndLoadFlorence2ModelMultiGPU, UnetLoaderGGUFDisTorchMultiGPU, UnetLoaderGGUFAdvancedDisTorchMultiGPU, CLIPLoaderGGUFDisTorchMultiGPU, DualCLIPLoaderGGUFDisTorchMultiGPU, TripleCLIPLoaderGGUFDisTorchMultiGPU, QuadrupleCLIPLoaderGGUFDisTorchMultiGPU, UnetLoaderGGUFDisTorch2MultiGPU, UnetLoaderGGUFAdvancedDisTorch2MultiGPU, CLIPLoaderGGUFDisTorch2MultiGPU, DualCLIPLoaderGGUFDisTorch2MultiGPU, TripleCLIPLoaderGGUFDisTorch2MultiGPU, QuadrupleCLIPLoaderGGUFDisTorch2MultiGPU, UnetLoaderGGUFMultiGPU, UnetLoaderGGUFAdvancedMultiGPU, CLIPLoaderGGUFMultiGPU, DualCLIPLoaderGGUFMultiGPU, TripleCLIPLoaderGGUFMultiGPU, QuadrupleCLIPLoaderGGUFMultiGPU
2025-12-04T23:43:13.667088 - [36;20m[/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_controlnet_aux] | INFO -> Using ckpts path: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_controlnet_aux/ckpts[0m
2025-12-04T23:43:13.667284 - [36;20m[/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_controlnet_aux] | INFO -> Using symlinks: False[0m
2025-12-04T23:43:13.667458 - [36;20m[/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_controlnet_aux] | INFO -> Using ort providers: ['CUDAExecutionProvider', 'DirectMLExecutionProvider', 'OpenVINOExecutionProvider', 'ROCMExecutionProvider', 'CPUExecutionProvider', 'CoreMLExecutionProvider'][0m
2025-12-04T23:43:14.156403 - [34mWAS Node Suite: [0mOpenCV Python FFMPEG support is enabled[0m2025-12-04T23:43:14.156492 - 
2025-12-04T23:43:14.156648 - [34mWAS Node Suite [93mWarning: [0m`ffmpeg_bin_path` is not set in `/home/zeuss194/COMFY/ComfyUI/custom_nodes/was-ns/was_suite_config.json` config file. Will attempt to use system ffmpeg binaries if available.[0m2025-12-04T23:43:14.156704 - 
2025-12-04T23:43:14.482627 - [34mWAS Node Suite: [0mFinished.[0m [32mLoaded[0m [0m220[0m [32mnodes successfully.[0m2025-12-04T23:43:14.482711 - 
2025-12-04T23:43:14.482815 - 
	[3m[93m"Art is not a thing; it is a way."[0m[3m - Elbert Hubbard[0m
2025-12-04T23:43:14.482888 - 
2025-12-04T23:43:14.913553 - [34m[ComfyUI-Easy-Use] server: [0mv1.3.4 [92mLoaded[0m2025-12-04T23:43:14.913595 - 
2025-12-04T23:43:14.913612 - [34m[ComfyUI-Easy-Use] web root: [0m/home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-Easy-Use/web_version/v2 [92mLoaded[0m2025-12-04T23:43:14.913625 - 
2025-12-04T23:43:14.916837 - Traceback (most recent call last):
  File "/home/zeuss194/COMFY/ComfyUI/nodes.py", line 2149, in load_custom_node
    module_spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "<frozen importlib._bootstrap_external>", line 1023, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI_MIGraphX/__init__.py", line 1, in <module>
    from .migraphx_compile_sd3 import CompileDiffusersMIGraphX
  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI_MIGraphX/migraphx_compile_sd3.py", line 4, in <module>
    from .migraphx_utils import load_MGX_transformer_model
  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI_MIGraphX/migraphx_utils.py", line 8, in <module>
    import migraphx as mgx
ModuleNotFoundError: No module named 'migraphx'

2025-12-04T23:43:14.917075 - Cannot import /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI_MIGraphX module for custom nodes: No module named 'migraphx'
2025-12-04T23:43:14.917994 - ComfyUI-GGUF: Allowing full torch compile
2025-12-04T23:43:14.921497 - [92mEclipse: [0mVersion: 1.0.61[0m2025-12-04T23:43:14.921524 - 
2025-12-04T23:43:14.922655 - ComfyUI-GGUF: Allowing full torch compile
2025-12-04T23:43:14.923283 - [92mEclipse: [0m[GGUF Wrapper] ✓ GGUF components imported successfully[0m2025-12-04T23:43:14.923307 - 
2025-12-04T23:43:14.923335 - [92mEclipse: [0m[GGUF Wrapper] Module loaded. GGUF available: True[0m2025-12-04T23:43:14.923349 - 
2025-12-04T23:43:14.923934 - [92mEclipse [93mWarning: [0m[Nunchaku Wrapper] Nunchaku package not available: No module named 'nunchaku'[0m2025-12-04T23:43:14.923957 - 
2025-12-04T23:43:15.053435 - /home/zeuss194/COMFY/ComfyUI/Comfyenv313/lib/python3.13/site-packages/timm/models/layers/__init__.py:48: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
2025-12-04T23:43:15.057323 - [92mEclipse: [0m[Florence-2 Wrapper] ✓ Custom Florence-2 classes imported successfully[0m2025-12-04T23:43:15.057352 - 
2025-12-04T23:43:15.059584 - [92mEclipse: [0m[SmartLM] Loaded 9 QwenVL prompts, 15 Florence-2 tasks[0m2025-12-04T23:43:15.059609 - 
2025-12-04T23:43:15.059709 - [92mEclipse: [0m[SmartLM] Loaded LLM few-shot training examples[0m2025-12-04T23:43:15.059725 - 
2025-12-04T23:43:15.061229 - [92mEclipse: [0m[SmartLM] Found 36 model templates[0m2025-12-04T23:43:15.061251 - 
2025-12-04T23:43:15.061283 - [92mEclipse: [0m[SmartLM] Transformers version: 4.57.1[0m2025-12-04T23:43:15.061298 - 
2025-12-04T23:43:15.078281 - [92mEclipse: [0m[SmartLM] llama-cpp-python version: 0.3.16[0m2025-12-04T23:43:15.078314 - 
2025-12-04T23:43:15.103795 - [92mEclipse: [0m[Wildcard] Loading wildcards from: /home/zeuss194/COMFY/ComfyUI/models/wildcards[0m2025-12-04T23:43:15.103827 - 
2025-12-04T23:43:15.109475 - [92mEclipse: [0m[Wildcard] Loaded 107 wildcard groups[0m2025-12-04T23:43:15.109504 - 
2025-12-04T23:43:15.109551 - [92mEclipse: [0m[Wildcard] Registered server endpoints[0m2025-12-04T23:43:15.109575 - 
2025-12-04T23:43:15.109596 - [92mEclipse: [0m[Wildcard] Server endpoints and prompt handler initialized successfully[0m2025-12-04T23:43:15.109609 - 
2025-12-04T23:43:15.213875 - [34m[ComfyUI-RMBG][0m v[93m2.9.4[0m | [93m33 nodes[0m [92mLoaded[0m2025-12-04T23:43:15.213911 - 
2025-12-04T23:43:15.215378 - ### Loading: ComfyUI-Impact-Subpack (V1.3.5)
2025-12-04T23:43:15.216238 - [Impact Pack/Subpack] Using folder_paths to determine whitelist path: /home/zeuss194/COMFY/ComfyUI/user/default/ComfyUI-Impact-Subpack/model-whitelist.txt
2025-12-04T23:43:15.216323 - [Impact Pack/Subpack] Ensured whitelist directory exists: /home/zeuss194/COMFY/ComfyUI/user/default/ComfyUI-Impact-Subpack
2025-12-04T23:43:15.216404 - [Impact Pack/Subpack] Loaded 0 model(s) from whitelist: /home/zeuss194/COMFY/ComfyUI/user/default/ComfyUI-Impact-Subpack/model-whitelist.txt
2025-12-04T23:43:15.255254 - [Impact Subpack] ultralytics_bbox: /home/zeuss194/COMFY/ComfyUI/models/ultralytics/bbox
2025-12-04T23:43:15.255354 - [Impact Subpack] ultralytics_segm: /home/zeuss194/COMFY/ComfyUI/models/ultralytics/segm
2025-12-04T23:43:15.286713 - 
----------------------------------------------------------------------2025-12-04T23:43:15.286745 - 
2025-12-04T23:43:15.286761 - [ComfyUI-Manager] NOTICE: Legacy backup exists2025-12-04T23:43:15.286774 - 
2025-12-04T23:43:15.286788 -   - Your old Manager data was backed up to:2025-12-04T23:43:15.286800 - 
2025-12-04T23:43:15.286813 -       /home/zeuss194/COMFY/ComfyUI/user/__manager/.legacy-manager-backup2025-12-04T23:43:15.286826 - 
2025-12-04T23:43:15.286839 -   - Please verify and remove it when no longer needed.2025-12-04T23:43:15.286851 - 
2025-12-04T23:43:15.286863 - ----------------------------------------------------------------------
2025-12-04T23:43:15.286875 - 
2025-12-04T23:43:15.287080 - ### Loading: ComfyUI-Manager (V3.38.1)
2025-12-04T23:43:15.287512 - [ComfyUI-Manager] network_mode: public
2025-12-04T23:43:15.336147 - ### ComfyUI Version: v0.3.76-24-g3c845622 | Released on '2025-12-04'
2025-12-04T23:43:15.379808 - 
[36mEfficiency Nodes:[0m Attempting to add Control Net options to the 'HiRes-Fix Script' Node (comfyui_controlnet_aux add-on)...[92mSuccess![0m2025-12-04T23:43:15.379844 - 
2025-12-04T23:43:15.385502 - 
Import times for custom nodes:
2025-12-04T23:43:15.385720 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/websocket_image_save.py
2025-12-04T23:43:15.385799 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-Lotus
2025-12-04T23:43:15.385847 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-lora-auto-trigger-words
2025-12-04T23:43:15.385891 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-tcd-sampler
2025-12-04T23:43:15.385936 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-lama-remover
2025-12-04T23:43:15.385981 -    0.0 seconds (IMPORT FAILED): /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI_MIGraphX
2025-12-04T23:43:15.386036 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/cg-use-everywhere
2025-12-04T23:43:15.386086 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/amdgpumonitor
2025-12-04T23:43:15.386134 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-inpaint-cropandstitch
2025-12-04T23:43:15.386182 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-inpaint-nodes
2025-12-04T23:43:15.386229 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-GGUF
2025-12-04T23:43:15.386272 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-custom-scripts
2025-12-04T23:43:15.386314 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/eacloudnodes
2025-12-04T23:43:15.386356 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-MultiGPU
2025-12-04T23:43:15.386396 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/rgthree-comfy
2025-12-04T23:43:15.386439 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-jakeupgrade
2025-12-04T23:43:15.386490 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_controlnet_aux
2025-12-04T23:43:15.386531 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_ipadapter_plus
2025-12-04T23:43:15.386579 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/efficiency-nodes-comfyui
2025-12-04T23:43:15.386624 -    0.0 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-impact-subpack
2025-12-04T23:43:15.386664 -    0.1 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes
2025-12-04T23:43:15.386704 -    0.1 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-manager
2025-12-04T23:43:15.386744 -    0.1 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-rmbg
2025-12-04T23:43:15.386783 -    0.1 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-Crystools
2025-12-04T23:43:15.386828 -    0.1 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-impact-pack
2025-12-04T23:43:15.386868 -    0.1 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-ollama
2025-12-04T23:43:15.386908 -    0.2 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI_Eclipse
2025-12-04T23:43:15.386947 -    0.2 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui-florence2
2025-12-04T23:43:15.386987 -    0.4 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-Easy-Use
2025-12-04T23:43:15.387027 -    0.8 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/was-ns
2025-12-04T23:43:15.387067 -    2.2 seconds: /home/zeuss194/COMFY/ComfyUI/custom_nodes/ComfyUI-MiniMax-Remover
2025-12-04T23:43:15.387107 - 
2025-12-04T23:43:15.526519 - [ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/model-list.json
2025-12-04T23:43:15.528047 - [ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/alter-list.json
2025-12-04T23:43:15.579603 - [ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/github-stats.json
2025-12-04T23:43:15.659011 - [ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json
2025-12-04T23:43:15.741002 - [ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/extension-node-map.json
2025-12-04T23:43:15.755271 - Context impl SQLiteImpl.
2025-12-04T23:43:15.755372 - Will assume non-transactional DDL.
2025-12-04T23:43:15.756128 - No target revision found.
2025-12-04T23:43:15.791237 - Starting server

2025-12-04T23:43:15.791513 - To see the GUI go to: http://127.0.0.1:8188
2025-12-04T23:43:18.774926 - FETCH ComfyRegistry Data: 5/1102025-12-04T23:43:18.774969 - 
2025-12-04T23:43:22.065523 - [DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
2025-12-04T23:43:22.102815 - [DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/clipspace.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
2025-12-04T23:43:22.104725 - [DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui/components/buttonGroup.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
2025-12-04T23:43:22.109466 - [DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/widgetInputs.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
2025-12-04T23:43:22.178765 - [DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/groupNode.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
2025-12-04T23:43:22.296939 - FETCH ComfyRegistry Data: 10/1102025-12-04T23:43:22.309461 - 
2025-12-04T23:43:24.357134 - [DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui/components/button.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
2025-12-04T23:43:25.794628 - FETCH ComfyRegistry Data: 15/1102025-12-04T23:43:25.794665 - 
2025-12-04T23:43:29.268033 - FETCH ComfyRegistry Data: 20/1102025-12-04T23:43:29.268077 - 
2025-12-04T23:43:32.786385 - FETCH ComfyRegistry Data: 25/1102025-12-04T23:43:32.786454 - 
2025-12-04T23:43:36.324238 - FETCH ComfyRegistry Data: 30/1102025-12-04T23:43:36.324284 - 
2025-12-04T23:43:39.811853 - FETCH ComfyRegistry Data: 35/1102025-12-04T23:43:39.811894 - 
2025-12-04T23:43:43.677686 - FETCH ComfyRegistry Data: 40/1102025-12-04T23:43:43.677727 - 
2025-12-04T23:43:47.159253 - FETCH ComfyRegistry Data: 45/1102025-12-04T23:43:47.159288 - 
2025-12-04T23:43:50.658209 - FETCH ComfyRegistry Data: 50/1102025-12-04T23:43:50.658296 - 
2025-12-04T23:43:54.158474 - FETCH ComfyRegistry Data: 55/1102025-12-04T23:43:54.158513 - 
2025-12-04T23:43:57.661130 - FETCH ComfyRegistry Data: 60/1102025-12-04T23:43:57.661178 - 
2025-12-04T23:44:01.145582 - FETCH ComfyRegistry Data: 65/1102025-12-04T23:44:01.145640 - 
2025-12-04T23:44:04.717306 - FETCH ComfyRegistry Data: 70/1102025-12-04T23:44:04.717363 - 
2025-12-04T23:44:08.245924 - FETCH ComfyRegistry Data: 75/1102025-12-04T23:44:08.245974 - 
2025-12-04T23:44:11.785822 - FETCH ComfyRegistry Data: 80/1102025-12-04T23:44:11.785859 - 
2025-12-04T23:44:15.342950 - FETCH ComfyRegistry Data: 85/1102025-12-04T23:44:15.343001 - 
2025-12-04T23:44:18.864385 - FETCH ComfyRegistry Data: 90/1102025-12-04T23:44:18.864423 - 
2025-12-04T23:44:22.386377 - FETCH ComfyRegistry Data: 95/1102025-12-04T23:44:22.386417 - 
2025-12-04T23:44:25.883610 - FETCH ComfyRegistry Data: 100/1102025-12-04T23:44:25.883653 - 
2025-12-04T23:44:29.416927 - FETCH ComfyRegistry Data: 105/1102025-12-04T23:44:29.416978 - 
2025-12-04T23:44:33.258603 - FETCH ComfyRegistry Data: 110/1102025-12-04T23:44:33.258682 - 
2025-12-04T23:44:33.759016 - FETCH ComfyRegistry Data [DONE]2025-12-04T23:44:33.759120 - 
2025-12-04T23:44:33.886504 - [ComfyUI-Manager] default cache updated: https://api.comfy.org/nodes
2025-12-04T23:44:33.912708 - FETCH DATA from: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json2025-12-04T23:44:33.912747 - 2025-12-04T23:44:34.041768 -  [DONE]2025-12-04T23:44:34.041828 - 
2025-12-04T23:44:34.089582 - [ComfyUI-Manager] All startup tasks have been completed.
2025-12-04T23:47:28.129740 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-04T23:50:51.219278 - got prompt
2025-12-04T23:50:51.264318 - model weight dtype torch.bfloat16, manual cast: None
2025-12-04T23:50:51.264869 - model_type FLOW
2025-12-04T23:50:53.855705 - Using split attention in VAE
2025-12-04T23:50:53.856767 - Using split attention in VAE
2025-12-04T23:50:54.120507 - VAE load device: cuda:0, offload device: cpu, dtype: torch.bfloat16
2025-12-04T23:50:54.121952 - [MultiGPU Core Patching] text_encoder_device_patched returning device: cuda:0 (current_text_encoder_device=cuda:0)
2025-12-04T23:50:54.434369 - Requested to load LuminaTEModel_
2025-12-04T23:50:54.847547 - loaded completely; 95367431640625005117571072.00 MB usable, 4986.46 MB loaded, full load: True
2025-12-04T23:50:54.975150 - CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cuda:0, dtype: torch.float16
2025-12-04T23:51:00.429155 - Requested to load Lumina2
2025-12-04T23:51:01.949179 - loaded completely; 25851.34 MB usable, 4977.74 MB loaded, full load: True
2025-12-04T23:51:27.257570 - 
 90%|█████████████████████████████████████▊    | 27/30 [00:25<00:02,  1.11it/s]2025-12-04T23:51:27.564100 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-04T23:51:29.988391 - 
100%|██████████████████████████████████████████| 30/30 [00:27<00:00,  1.10it/s]2025-12-04T23:51:29.988647 - 
100%|██████████████████████████████████████████| 30/30 [00:27<00:00,  1.07it/s]2025-12-04T23:51:29.988672 - 
2025-12-04T23:51:29.989548 - Requested to load AutoencodingEngine
2025-12-04T23:51:30.032870 - loaded completely; 8795.91 MB usable, 159.87 MB loaded, full load: True
2025-12-04T23:51:32.382763 - Prompt executed in 41.16 seconds
2025-12-04T23:52:49.917612 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-04T23:53:23.124755 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-04T23:53:55.494875 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-04T23:54:42.255635 - got prompt
2025-12-04T23:55:11.113465 - 
100%|██████████████████████████████████████████| 30/30 [00:27<00:00,  1.09it/s]2025-12-04T23:55:11.113750 - 
100%|██████████████████████████████████████████| 30/30 [00:27<00:00,  1.10it/s]2025-12-04T23:55:11.113789 - 
2025-12-04T23:55:12.962738 - Prompt executed in 30.70 seconds
2025-12-04T23:57:01.419997 - got prompt
2025-12-04T23:57:30.362470 - 
100%|██████████████████████████████████████████| 30/30 [00:27<00:00,  1.09it/s]2025-12-04T23:57:30.362709 - 
100%|██████████████████████████████████████████| 30/30 [00:27<00:00,  1.10it/s]2025-12-04T23:57:30.362732 - 
2025-12-04T23:57:32.117629 - Prompt executed in 30.69 seconds
2025-12-05T00:02:17.139691 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-05T00:02:30.746038 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-05T00:03:52.870989 - got prompt
2025-12-05T00:04:20.722095 - 
100%|██████████████████████████████████████████| 30/30 [00:26<00:00,  1.10it/s]2025-12-05T00:04:20.722289 - 
100%|██████████████████████████████████████████| 30/30 [00:26<00:00,  1.11it/s]2025-12-05T00:04:20.722318 - 
2025-12-05T00:04:22.429421 - Prompt executed in 29.56 seconds
2025-12-05T00:04:31.042022 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-05T00:04:46.502490 - HTTP Request: GET http://127.0.0.1:11434/api/tags "HTTP/1.1 200 OK"
2025-12-05T00:08:25.603179 - got prompt
2025-12-05T00:08:37.922229 - HTTP Request: POST http://127.0.0.1:11434/api/generate "HTTP/1.1 200 OK"
2025-12-05T00:08:37.923273 - Prompt executed in 12.32 seconds
2025-12-05T00:09:59.520261 - got prompt
2025-12-05T00:10:04.568945 - HTTP Request: POST http://127.0.0.1:11434/api/generate "HTTP/1.1 200 OK"
2025-12-05T00:10:04.570240 - Prompt executed in 5.05 seconds
2025-12-05T00:11:57.175907 - got prompt
2025-12-05T00:12:11.075943 - HTTP Request: POST http://127.0.0.1:11434/api/generate "HTTP/1.1 200 OK"
2025-12-05T00:12:11.076997 - Prompt executed in 13.90 seconds
2025-12-05T00:13:13.638066 - got prompt
2025-12-05T00:13:13.687168 - model weight dtype torch.bfloat16, manual cast: None
2025-12-05T00:13:13.687502 - model_type FLOW
2025-12-05T00:13:16.212092 - Using split attention in VAE
2025-12-05T00:13:16.213302 - Using split attention in VAE
2025-12-05T00:13:16.400293 - VAE load device: cuda:0, offload device: cpu, dtype: torch.bfloat16
2025-12-05T00:13:16.401872 - [MultiGPU Core Patching] text_encoder_device_patched returning device: cuda:0 (current_text_encoder_device=cuda:0)
2025-12-05T00:13:16.689225 - Requested to load LuminaTEModel_
2025-12-05T00:13:16.700958 - loaded completely; 95367431640625005117571072.00 MB usable, 4986.46 MB loaded, full load: True
2025-12-05T00:13:16.703343 - CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cuda:0, dtype: torch.float16
2025-12-05T00:13:20.046260 - Requested to load Lumina2
2025-12-05T00:13:21.433125 - loaded completely; 25679.34 MB usable, 4977.74 MB loaded, full load: True
2025-12-05T00:13:47.814901 - 
100%|██████████████████████████████████████████| 30/30 [00:26<00:00,  1.13it/s]2025-12-05T00:13:47.815125 - 
100%|██████████████████████████████████████████| 30/30 [00:26<00:00,  1.14it/s]2025-12-05T00:13:47.815153 - 
2025-12-05T00:13:47.816123 - Requested to load AutoencodingEngine
2025-12-05T00:13:47.853524 - loaded completely; 8770.71 MB usable, 159.87 MB loaded, full load: True
2025-12-05T00:13:49.593847 - Prompt executed in 35.95 seconds
2025-12-05T00:14:16.940779 - got prompt
2025-12-05T00:14:34.199483 - 
 63%|██████████████████████████▌               | 19/30 [00:16<00:09,  1.11it/s]2025-12-05T00:14:34.567014 - /home/zeuss194/COMFY/ComfyUI/comfy/k_diffusion/sampling.py:246: UserWarning: HIP warning: an illegal memory access was encountered (Triggered internally at /pytorch/aten/src/ATen/hip/impl/HIPGuardImplMasqueradingAsCUDA.h:83.)
  if sigmas[i + 1] == 0:
2025-12-05T00:14:34.567328 - 
 63%|██████████████████████████▌               | 19/30 [00:17<00:10,  1.10it/s]2025-12-05T00:14:34.567365 - 
2025-12-05T00:14:34.574847 - !!! Exception during processing !!! HIP error: an illegal memory access was encountered
Search for `hipErrorIllegalAddress' in https://rocm.docs.amd.com/projects/HIP/en/latest/index.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

2025-12-05T00:14:34.579477 - Traceback (most recent call last):
  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 515, in execute
    output_data, output_ui, has_subgraph, has_pending_tasks = await get_output_data(prompt_id, unique_id, obj, input_data_all, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 329, in get_output_data
    return_values = await _async_map_node_over_list(prompt_id, unique_id, obj, input_data_all, obj.FUNCTION, allow_interrupt=True, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 303, in _async_map_node_over_list
    await process_inputs(input_dict, i)
  File "/home/zeuss194/COMFY/ComfyUI/execution.py", line 291, in process_inputs
    result = f(**inputs)
  File "/home/zeuss194/COMFY/ComfyUI/nodes.py", line 1538, in sample
    return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)
  File "/home/zeuss194/COMFY/ComfyUI/nodes.py", line 1505, in common_ksampler
    samples = comfy.sample.sample(model, noise, steps, cfg, sampler_name, scheduler, positive, negative, latent_image,
                                  denoise=denoise, disable_noise=disable_noise, start_step=start_step, last_step=last_step,
                                  force_full_denoise=force_full_denoise, noise_mask=noise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/sample.py", line 60, in sample
    samples = sampler.sample(noise, positive, negative, cfg=cfg, latent_image=latent_image, start_step=start_step, last_step=last_step, force_full_denoise=force_full_denoise, denoise_mask=noise_mask, sigmas=sigmas, callback=callback, disable_pbar=disable_pbar, seed=seed)
  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes/smZNodes.py", line 131, in KSampler_sample
    return orig_fn(*args, **kwargs)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 1163, in sample
    return sample(self.model, noise, positive, negative, cfg, self.device, sampler, sigmas, self.model_options, latent_image=latent_image, denoise_mask=denoise_mask, callback=callback, disable_pbar=disable_pbar, seed=seed)
  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes/smZNodes.py", line 149, in sample
    return orig_fn(*args, **kwargs)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 1053, in sample
    return cfg_guider.sample(noise, latent_image, sampler, sigmas, denoise_mask, callback, disable_pbar, seed)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 1035, in sample
    output = executor.execute(noise, latent_image, sampler, sigmas, denoise_mask, callback, disable_pbar, seed, latent_shapes=latent_shapes)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/patcher_extension.py", line 112, in execute
    return self.original(*args, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 997, in outer_sample
    output = self.inner_sample(noise, latent_image, device, sampler, sigmas, denoise_mask, callback, disable_pbar, seed, latent_shapes=latent_shapes)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 980, in inner_sample
    samples = executor.execute(self, sigmas, extra_args, callback, noise, latent_image, denoise_mask, disable_pbar)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/patcher_extension.py", line 112, in execute
    return self.original(*args, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/zeuss194/COMFY/ComfyUI/custom_nodes/comfyui_smznodes/smZNodes.py", line 114, in KSAMPLER_sample
    return orig_fn(*args, **kwargs)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/samplers.py", line 752, in sample
    samples = self.sampler_function(model_k, noise, sigmas, extra_args=extra_args, callback=k_callback, disable=disable_pbar, **self.extra_options)
  File "/home/zeuss194/COMFY/ComfyUI/Comfyenv313/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/k_diffusion/sampling.py", line 212, in sample_euler_ancestral
    return sample_euler_ancestral_RF(model, x, sigmas, extra_args, callback, disable, eta, s_noise, noise_sampler)
  File "/home/zeuss194/COMFY/ComfyUI/Comfyenv313/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
  File "/home/zeuss194/COMFY/ComfyUI/comfy/k_diffusion/sampling.py", line 246, in sample_euler_ancestral_RF
    if sigmas[i + 1] == 0:
       ^^^^^^^^^^^^^^^^^^
torch.AcceleratorError: HIP error: an illegal memory access was encountered
Search for `hipErrorIllegalAddress' in https://rocm.docs.amd.com/projects/HIP/en/latest/index.html for more information.
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.


2025-12-05T00:14:34.583952 - Prompt executed in 17.64 seconds
2025-12-05T00:14:35.027900 - Exception in thread 2025-12-05T00:14:35.027961 - Thread-5 (prompt_worker)
```
## Attached Workflow

```

## Additional Context
(Please add any additional context or steps to reproduce the error here)
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"
CPU: 
model name	: Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz
GPU:
  Name:                    Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz
  Marketing Name:          Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz
  Name:                    gfx1201                            
  Marketing Name:          AMD Radeon AI PRO R9700            
      Name:                    amdgcn-amd-amdhsa--gfx1201         
      Name:                    amdgcn-amd-amdhsa--gfx12-generic 

### Operating System

NAME="Ubuntu" VERSION="24.04.3 LTS (Noble Numbat)"

### CPU

CPU:  model name	: Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz

### GPU

GPU:   Name:                    Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz   Marketing Name:          Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz   Name:                    gfx1201                               Marketing Name:          AMD Radeon AI PRO R9700                   Name:                    amdgcn-amd-amdhsa--gfx1201                Name:                    amdgcn-amd-amdhsa--gfx12-generic 

### ROCm Version

7.1.1

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

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
  Name:                    Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz
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
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   4500                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    65419284(0x3e63814) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    65419284(0x3e63814) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65419284(0x3e63814) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65419284(0x3e63814) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-5c5383ed20b3fc7d               
  Marketing Name:          AMD Radeon AI PRO R9700            
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
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30033(0x7551)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2350                               
  BDFID:                   26368                              
  Internal Node ID:        1                                  
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
  Packet Processor uCode:: 108                                
  SDMA engine uCode::      662                                
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

### Additional Information

_No response_