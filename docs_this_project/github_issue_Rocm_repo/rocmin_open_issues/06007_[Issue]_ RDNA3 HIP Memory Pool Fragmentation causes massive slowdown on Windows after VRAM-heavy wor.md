# [Issue]: RDNA3 HIP Memory Pool Fragmentation causes massive slowdown on Windows after VRAM-heavy workload

- **Issue #:** 6007
- **State:** open
- **Created:** 2026-02-28T10:28:31Z
- **Updated:** 2026-06-17T19:02:11Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6007

### Problem Description

(Get-WmiObject Win32_OperatingSystem).Version

After GPU heavy operation a ComfyUI workflow works significantly slower. 

After running a large VRAM-intensive HIP application (e.g., LM Studio) and closing it, subsequent HIP workloads (e.g., ComfyUI with PyTorch-HIP) experience massive slowdown.  I have now to reboot the system to be able to continue. At one point it even slows down in ComfyUI. But with loading a large LLM in LM Studio it is faster to reproduce:

Fresh boot ComfyUI: Zimage ~1 s, Qwen Image ~3 s per KSampler step
After VRAM-heavy app: Zimage ~25 s, Qwen Image ~45 s per KSampler step
GPU utilization: 100 % during slowdown
Dedicated GPU memory: ~31.4 / 32 GB
Total GPU memory: ~53.5 / 62.8 GB
Shared GPU memory: ~22.2 / 30.8 GB
Power state: normal (full GPU clocks)

This indicates that GPU memory pool is fragmented or memory residency is not properly cleared, causing allocations to spill to system RAM.

### Operating System

Windows 11 Pro 25H2

### CPU

AMD Ryzen 9 9900X

### GPU

AMD Radeon AI Pro 32 Gb

### ROCm Version

7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

Boot Windows
Run ComfyUI → generate image (fast, 1–3 s)
Close ComfyUI
Run a VRAM-heavy HIP application (LM Studio, full model load)
Close HIP application
Run ComfyUI image workflow again → extreme slowdown observed

ComfyUI workflows to reproduce the problem:

[comfyui workflows.zip](https://github.com/user-attachments/files/25620560/comfyui.workflows.zip)

Be aware of this AMD related bug. Create a directory on D:\a\ComfyUI, and copy over the python_embedded folder from the ComfyUI portable. 

https://github.com/Comfy-Org/ComfyUI/issues/11546



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

![Image](https://github.com/user-attachments/assets/95394962-2d06-451f-9571-931f9126335d)

![Image](https://github.com/user-attachments/assets/51680387-f923-4485-8ce8-168466cb64cd)

![Image](https://github.com/user-attachments/assets/fbb75df7-ef4c-4a8c-8ca8-3f5c66ba68cb)

Maybe related issue, has also to do with a massive slowdown at a second run.

https://github.com/Comfy-Org/ComfyUI/issues/12672

Comfy log of a slow generation, which produced the images in three seconds after a fresh boot:
```

G:\comfyamd\ComfyUI_windows_portable>set HIP_PRINT_ENV=1

G:\comfyamd\ComfyUI_windows_portable>set HIP_TRACE_API=1

G:\comfyamd\ComfyUI_windows_portable>set PYTORCH_ALLOC_CONF=garbage_collection_threshold:0.9,max_split_size_mb:512

G:\comfyamd\ComfyUI_windows_portable>.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --disable-pinned-memory --use-split-cross-attention
G:\comfyamd\ComfyUI_windows_portable\python_embeded\Lib\site-packages\requests\__init__.py:113: RequestsDependencyWarning: urllib3 (2.6.3) or chardet (6.0.0.post1)/charset_normalizer (3.4.4) doesn't match a supported version!
  warnings.warn(
[START] Security scan
[DONE] Security scan
## ComfyUI-Manager: installing dependencies done.
** ComfyUI startup time: 2026-02-28 11:04:48.383
** Platform: Windows
** Python version: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
** Python executable: G:\comfyamd\ComfyUI_windows_portable\python_embeded\python.exe
** ComfyUI Path: G:\comfyamd\ComfyUI_windows_portable\ComfyUI
** ComfyUI Base Folder Path: G:\comfyamd\ComfyUI_windows_portable\ComfyUI
** User directory: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\user
** ComfyUI-Manager config path: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\user\default\ComfyUI-Manager\config.ini
** Log path: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\user\comfyui.log

Prestartup times for custom nodes:
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\rgthree-comfy
   6.8 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-Manager

Found comfy_kitchen backend cuda: {'available': True, 'disabled': True, 'unavailable_reason': None, 'capabilities': ['apply_rope', 'apply_rope1', 'dequantize_nvfp4', 'dequantize_per_tensor_fp8', 'quantize_nvfp4', 'quantize_per_tensor_fp8', 'scaled_mm_nvfp4']}
Found comfy_kitchen backend triton: {'available': False, 'disabled': True, 'unavailable_reason': "ImportError: No module named 'triton'", 'capabilities': []}
Found comfy_kitchen backend eager: {'available': True, 'disabled': False, 'unavailable_reason': None, 'capabilities': ['apply_rope', 'apply_rope1', 'dequantize_nvfp4', 'dequantize_per_tensor_fp8', 'quantize_nvfp4', 'quantize_per_tensor_fp8', 'scaled_mm_nvfp4']}
Checkpoint files will always be loaded safely.
Total VRAM 32624 MB, total RAM 63140 MB
pytorch version: 2.9.1+rocmsdk20260116
Set: torch.backends.cudnn.enabled = False for better AMD performance.
AMD arch: gfx1201
ROCm version: (7, 2)
Set vram state to: NORMAL_VRAM
Device: cuda:0 AMD Radeon AI PRO R9700 : native
Using async weight offloading with 2 streams
Using split optimization for attention
Python version: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]
ComfyUI version: 0.15.0
ComfyUI frontend version: 1.39.16
[Prompt Server] web root: G:\comfyamd\ComfyUI_windows_portable\python_embeded\Lib\site-packages\comfyui_frontend_package\static
Traceback (most recent call last):
  File "G:\comfyamd\ComfyUI_windows_portable\ComfyUI\nodes.py", line 2224, in load_custom_node
    module_spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "G:\comfyamd\ComfyUI_windows_portable\ComfyUI\comfy_extras\nodes_glsl.py", line 64, in <module>
    _check_opengl_availability()
  File "G:\comfyamd\ComfyUI_windows_portable\ComfyUI\comfy_extras\nodes_glsl.py", line 35, in _check_opengl_availability
    raise RuntimeError(
RuntimeError: OpenGL dependencies not available.
Please install the updated requirements.txt file by running:
G:\comfyamd\ComfyUI_windows_portable\python_embeded\python.exe -s -m pip install -r G:\comfyamd\ComfyUI_windows_portable\ComfyUI\requirements.txt
If you are on the portable package you can run: update\update_comfyui.bat to solve this problem.


Cannot import G:\comfyamd\ComfyUI_windows_portable\ComfyUI\comfy_extras\nodes_glsl.py module for custom nodes: OpenGL dependencies not available.
Please install the updated requirements.txt file by running:
G:\comfyamd\ComfyUI_windows_portable\python_embeded\python.exe -s -m pip install -r G:\comfyamd\ComfyUI_windows_portable\ComfyUI\requirements.txt
If you are on the portable package you can run: update\update_comfyui.bat to solve this problem.

ComfyUI-FreeMemory nodes loaded: Image, Latent, Model, CLIP, and String versions available.
ComfyUI-GGUF: Allowing full torch compile
### Loading: ComfyUI-Impact-Pack (V8.28.2)
[Impact Pack] Wildcard total size (0.00 MB) is within cache limit (50.00 MB). Using full cache mode.
[Impact Pack] Wildcards loading done.
### Loading: ComfyUI-Manager (V3.37.1)
[ComfyUI-Manager] network_mode: public
### ComfyUI Revision: 150 [b874bd2b] *DETACHED | Released on '2026-02-24'
Error loading module AILab_QwenVL: cannot import name 'AutoModelForVision2Seq' from 'transformers' (G:\comfyamd\ComfyUI_windows_portable\python_embeded\Lib\site-packages\transformers\__init__.py)
Error loading module AILab_QwenVL_GGUF_PromptEnhancer: No module named 'llama_cpp'
Error loading module AILab_QwenVL_PromptEnhancer: cannot import name 'ATTENTION_MODES' from 'AILab_QwenVL' (G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-QwenVL\AILab_QwenVL.py)
[ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/model-list.json
[ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/alter-list.json
Note: NumExpr detected 24 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 16.
NumExpr defaulting to 16 threads.
[ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/github-stats.json
[ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json
[ComfyUI-Manager] default cache updated: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/extension-node-map.json
FizzleDorf Custom Nodes: Loaded

     ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗    ██████╗ ███╗   ██╗
     ██╔══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║   ██╔═══██╗████╗  ██║
     ██████╔╝ ╚████╔╝ ███████║██╔██╗ ██║   ██║   ██║██╔██╗ ██║
     ██╔══██╗  ╚██╔╝  ██╔══██║██║╚██╗██║   ██║   ██║██║╚██╗██║
     ██║  ██║   ██║   ██║  ██║██║ ╚████║   ╚██████╔╝██║ ╚████║
     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═════╝ ╚═╝  ╚═══╝
████████╗██╗  ██╗███████╗   ██╗███╗   ██╗███████╗██╗██████╗ ███████╗
╚══██╔══╝██║  ██║██╔════╝   ██║████╗  ██║██╔════╝██║██╔══██╗██╔════╝
   ██║   ███████║█████╗     ██║██╔██╗ ██║███████╗██║██║  ██║█████╗
   ██║   ██╔══██║██╔══╝     ██║██║╚██╗██║╚════██║██║██║  ██║██╔══╝
   ██║   ██║  ██║███████╗   ██║██║ ╚████║███████║██║██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═════╝ ╚══════╝

             ⚡ R Y A N   O N   T H E   I N S I D E ⚡


[RyanOnTheInside] Copying extension file: widget_hotkey.js
[RyanOnTheInside] Failed to load .nodes.masks.temporal_masks: No module named 'pymunk'
[RyanOnTheInside] Failed to load .nodes.masks.optical_flow_masks: No module named 'pymunk'
[RyanOnTheInside] Failed to load .nodes.masks.particle_system_masks: No module named 'pymunk'
[RyanOnTheInside] Failed to load .nodes.masks.flex_masks: No module named 'pymunk'
Checking for AdvancedLivePortrait at: None
Checking for Advanced-ControlNet at: None
Checking for AnimateDiff-Evolved at: None
ComfyUI-AdvancedLivePortrait not found. FlexExpressionEditor will not be available. Install ComfyUI-AdvancedLivePortrait and restart ComfyUI.
ComfyUI-Advanced-ControlNet not found. Advanced-ControlNet feature nodes will not be available. Install ComfyUI-Advanced-ControlNet and restart ComfyUI.
ComfyUI-AnimateDiff-Evolved not found. AnimateDiff feature nodes will not be available. Install ComfyUI-AnimateDiff-Evolved and restart ComfyUI.
[comfyui_ryanontheinside.acestep] [ACE-Step Patches] Patched resolve_areas_and_cond_masks_multidim for 1D latent support
[comfyui_ryanontheinside.acestep] [ACE-Step Patches] Patched comfy.utils.reshape_mask for 1D latent support
[Crystools ERROR] pynvml is not installed. No module named 'pynvml'
[Crystools WARNING] No GPU monitoring libraries available.

[rgthree-comfy] Loaded 48 fantastic nodes. 🎉

[rgthree-comfy] ComfyUI's new Node 2.0 rendering may be incompatible with some rgthree-comfy nodes and features, breaking some rendering as well as losing the ability to access a node's properties (a vital part of many nodes). It also appears to run MUCH more slowly spiking CPU usage and causing jankiness and unresponsiveness, especially with large workflows. Personally I am not planning to use the new Nodes 2.0 and, unfortunately, am not able to invest the time to investigate and overhaul rgthree-comfy where needed. If you have issues when Nodes 2.0 is enabled, I'd urge you to switch it off as well and join me in hoping ComfyUI is not planning to deprecate the existing, stable canvas rendering all together.

Error: modelscope not installed. Please run: pip install modelscope

Import times for custom nodes:
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\websocket_image_save.py
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\HeartMuLa_ComfyUI
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\comfyui-simple-prompt-batcher
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\z-image-turbo
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\comfyui_auto_prompt_schedule
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-FreeMemory
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-VFI
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\Crystools-MonitorOnly
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyMath
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-Custom-Scripts
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\comfyui-frame-interpolation
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\Derfuu_ComfyUI_ModdedNodes
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-QwenVL
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\rgthree-comfy
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-GGUF
   0.0 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-VideoHelperSuite
   0.1 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-LTXVideo
   0.2 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI_FizzNodes
   0.2 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\comfyui-levelpixel
   0.2 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-Impact-Pack
   0.4 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\comfyui_ryanonyheinside
   0.5 seconds: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-Manager

WARNING: some comfy_extras/ nodes did not import correctly. This may be because they are missing some dependencies.

IMPORT FAILED: nodes_glsl.py

This issue might be caused by new missing dependencies added the last time you updated ComfyUI.
Please run the update script: update/update_comfyui.bat

Context impl SQLiteImpl.
Will assume non-transactional DDL.
Assets scan(roots=['models']) completed in 0.015s (created=0, skipped_existing=65, orphans_pruned=0, total_seen=65)
Starting server

To see the GUI go to: http://127.0.0.1:8188
[DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/clipspace.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/groupNode.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /extensions/core/widgetInputs.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui/components/button.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
[DEPRECATION WARNING] Detected import of deprecated legacy API: /scripts/ui/components/buttonGroup.js. This is likely caused by a custom node extension using outdated APIs. Please update your extensions or contact the extension author for an updated version.
got prompt
Using split attention in VAE
Using split attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.bfloat16
Found quantization metadata version 1
Using MixedPrecisionOps for text encoder
Requested to load QwenImageTEModel_
loaded completely;  7910.28 MB loaded, full load: True
CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cuda:0, dtype: torch.float16
[Prompt Batcher] 📋 Batching 10 prompts:
[Prompt Batcher]   1. modern interior, A singer wearing headphones, singing into a...
[Prompt Batcher]   2. modern interior, A handful of fans in streetwear — some film...
[Prompt Batcher]   3. modern interior, A waitress in simple black attire walks slo...
[Prompt Batcher]   4. modern interior, The singer wearing headphones, singing into...
[Prompt Batcher]   5. modern interior, A fan in streetwear lies flat on the wooden...
[Prompt Batcher]   6. modern interior, A waitress carrying a tray of ceramic mugs ...
[Prompt Batcher]   7. modern interior, The producer behind the laptop, surrounded ...
[Prompt Batcher]   8. modern interior, A fan in streetwear sits cross-legged near ...
[Prompt Batcher]   9. modern interior, The singer wearing headphones, now off-mic ...
[Prompt Batcher]   10. modern interior, The rooftop is silent now — the singer wear...
model weight dtype torch.float8_e4m3fn, manual cast: torch.bfloat16
model_type FLUX
Requested to load QwenImage
Unloaded partially: 3180.03 MB freed, 4730.25 MB remains loaded, 453.25 MB buffer reserved, lowvram patches: 0
loaded completely; 24392.90 MB usable, 19483.95 MB loaded, full load: True
 50%|██████████████████████████████████████████                                          | 2/4 [00:24<00:28, 14.14s/it]FETCH ComfyRegistry Data [DONE]
[ComfyUI-Manager] default cache updated: https://api.comfy.org/nodes
FETCH DATA from: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json [DONE]
[ComfyUI-Manager] All startup tasks have been completed.
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:45<00:00, 11.35s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:41<00:00, 10.33s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:41<00:00, 10.28s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:40<00:00, 10.17s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:42<00:00, 10.56s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:41<00:00, 10.45s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:41<00:00, 10.48s/it]
100%|████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:41<00:00, 10.32s/it]
  0%|                                                                                            | 0/4 [00:00<?, ?it/s]




```
