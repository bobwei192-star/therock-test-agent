# [Issue]: [gfx1201] ROCm kernel cache not persistent across inference runs, causing significant performance regression on subsequent runs

- **Issue #:** 6008
- **State:** open
- **Created:** 2026-03-01T17:08:19Z
- **Updated:** 2026-03-30T21:11:16Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6008

### Problem Description

  (Get-WmiObject win32_Processor).Name

When running WAN VAE (CausalConv3d operations) in ComfyUI on gfx1201 (Radeon AI PRO R9700), subsequent inference runs are significantly slower than the first. The slowdown scales with resolution and frame count – at 1024x576 @ 81 frames it is 4-5x slower, at lower resolutions around 2-3x slower.

The problem appears with ComfyUI and runing a Wan Image to Video workflow, where we get a dramatical speed regression between first run and second run.

It is reproducable on both, Windows 11 and a Docker in Ubuntu 24 with also ROCm 7.2, so no Windows only problem.

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

Download latest WIndows ComfyUI portable here: https://github.com/Comfy-Org/ComfyUI/releases

Load the attached Wan Image to Video workflow on a PC with AMD card and ROCm 7.2. See attached assets.
Download the models that are linked in the workflow.
Let the workflow run through.
Change the image.
Let it run through again.
Watch the generation times.

Minimal reproduction confirms kernel recompilation on new tensor shapes, i ran it from the ComfyUI_windows_portable folder:

```
import torch, time
device = "cuda:0"
x1 = torch.randn(1, 96, 1, 576, 1024, device=device, dtype=torch.float16)
conv = torch.nn.Conv3d(96, 96, 3, padding=1).to(device).half()
start = time.time(); conv(x1); print(f"1 frame: {time.time()-start:.3f}s")
x2 = torch.randn(1, 96, 6, 576, 1024, device=device, dtype=torch.float16)
start = time.time(); conv(x2); print(f"6 frames first call: {time.time()-start:.3f}s")
start = time.time(); conv(x2); print(f"6 frames second call: {time.time()-start:.3f}s")
```

Output:
1 frame: 7.640s
6 frames first call: 83.488s
6 frames second call: 0.001s

The kernel cache works within a session when the same tensor shapes are called back-to-back. However ROCm does not persist this cache across subsequent inference runs, causing full recompilation on every run after the first.

Additional observation: Between Run 1 and Run 2, ComfyUI unloads significantly more VRAM before reloading the diffusion model (Unloaded partially: 8569 MB in Run 2 vs 1232 MB in Run 1). Whether this is related or a separate issue is unclear.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

For the Linux version see this docker here if needed: https://github.com/YanWenKun/ComfyUI-Docker/tree/main/rocm7

**Evidence:

Running ComfyUI with these startup parameters:

--novram (all computation on CPU, no VRAM load/unload) → no performance regression between runs, it is even faster at the second run. This strongly suggests the regression is tied to VRAM load/unload cycles.
--cache-none (disables ComfyUI's internal caching) → regression persists, ruling out ComfyUI cache as cause,  and points directly at ROCm.

--novram result

```
got prompt
Using split attention in VAE
Using split attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.bfloat16
Found quantization metadata version 1
Using MixedPrecisionOps for text encoder
Requested to load WanTEModel
loaded completely;  6419.48 MB loaded, full load: True
CLIP/text encoder model load device: cpu, offload device: cpu, current: cpu, dtype: torch.float16
FETCH ComfyRegistry Data [DONE]
[ComfyUI-Manager] default cache updated: https://api.comfy.org/nodes
FETCH DATA from: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json [DONE]
[ComfyUI-Manager] All startup tasks have been completed.
Requested to load WanVAE
loaded partially; 0.00 MB usable, 0.00 MB loaded, 242.00 MB offloaded, 22.78 MB buffer reserved, lowvram patches: 0
### vae.encode done
loaded partially; 0.00 MB usable, 0.00 MB loaded, 242.00 MB offloaded, 22.78 MB buffer reserved, lowvram patches: 0
gguf qtypes: F16 (694), Q4_K (280), Q6_K (120), F32 (1)
model weight dtype torch.float16, manual cast: None
model_type FLOW
Requested to load WAN21
loaded partially; 0.00 MB usable, 0.00 MB loaded, 9337.19 MB offloaded, 656.56 MB buffer reserved, lowvram patches: 0
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:10<00:00,  5.15s/it]
gguf qtypes: F16 (694), Q4_K (280), Q6_K (120), F32 (1)
model weight dtype torch.float16, manual cast: None
model_type FLOW
Requested to load WAN21
loaded partially; 0.00 MB usable, 0.00 MB loaded, 9337.19 MB offloaded, 656.56 MB buffer reserved, lowvram patches: 0
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:09<00:00,  4.65s/it]
loaded partially; 0.00 MB usable, 0.00 MB loaded, 242.00 MB offloaded, 22.78 MB buffer reserved, lowvram patches: 0
Loading RIFE model from: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-VFI\rife\train_log\flownet.pkl
Prompt executed in 283.42 seconds
got prompt
loaded partially; 0.00 MB usable, 0.00 MB loaded, 242.00 MB offloaded, 22.78 MB buffer reserved, lowvram patches: 0
### vae.encode done
loaded partially; 0.00 MB usable, 0.00 MB loaded, 242.00 MB offloaded, 22.78 MB buffer reserved, lowvram patches: 0
loaded partially; 0.00 MB usable, 0.00 MB loaded, 9337.19 MB offloaded, 656.56 MB buffer reserved, lowvram patches: 0
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:08<00:00,  4.32s/it]
loaded partially; 0.00 MB usable, 0.00 MB loaded, 9337.19 MB offloaded, 656.56 MB buffer reserved, lowvram patches: 0
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:08<00:00,  4.25s/it]
loaded partially; 0.00 MB usable, 0.00 MB loaded, 242.00 MB offloaded, 22.78 MB buffer reserved, lowvram patches: 0
Prompt executed in 177.25 seconds
```

--cache-none result

```

got prompt
Using split attention in VAE
Using split attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.bfloat16
Found quantization metadata version 1
Using MixedPrecisionOps for text encoder
Requested to load WanTEModel
loaded completely;  6419.48 MB loaded, full load: True
CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cuda:0, dtype: torch.float16
Requested to load WanVAE
loaded completely; 30717.34 MB usable, 242.03 MB loaded, full load: True
### vae.encode done
gguf qtypes: F16 (694), Q4_K (280), Q6_K (120), F32 (1)
model weight dtype torch.float16, manual cast: None
model_type FLOW
Requested to load WAN21
loaded completely; 27948.86 MB usable, 9337.19 MB loaded, full load: True
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:07<00:00,  3.64s/it]
gguf qtypes: F16 (694), Q4_K (280), Q6_K (120), F32 (1)
model weight dtype torch.float16, manual cast: None
model_type FLOW
Requested to load WAN21
loaded completely; 27797.48 MB usable, 9337.19 MB loaded, full load: True
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:06<00:00,  3.28s/it]
Loading RIFE model from: G:\comfyamd\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-VFI\rife\train_log\flownet.pkl
Prompt executed in 37.50 seconds
FETCH ComfyRegistry Data [DONE]
[ComfyUI-Manager] default cache updated: https://api.comfy.org/nodes
FETCH DATA from: https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json [DONE]
[ComfyUI-Manager] All startup tasks have been completed.
got prompt
Using split attention in VAE
Using split attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.bfloat16
Found quantization metadata version 1
Using MixedPrecisionOps for text encoder
Requested to load WanTEModel
loaded completely;  6419.48 MB loaded, full load: True
CLIP/text encoder model load device: cuda:0, offload device: cpu, current: cuda:0, dtype: torch.float16
Requested to load WanVAE
loaded completely; 30374.13 MB usable, 242.03 MB loaded, full load: True
### vae.encode done
gguf qtypes: F16 (694), Q4_K (280), Q6_K (120), F32 (1)
model weight dtype torch.float16, manual cast: None
model_type FLOW
Requested to load WAN21
loaded completely; 27698.33 MB usable, 9337.19 MB loaded, full load: True
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:06<00:00,  3.27s/it]
gguf qtypes: F16 (694), Q4_K (280), Q6_K (120), F32 (1)
model weight dtype torch.float16, manual cast: None
model_type FLOW
Requested to load WAN21
loaded completely; 27698.33 MB usable, 9337.19 MB loaded, full load: True
100%|████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:06<00:00,  3.15s/it]
Prompt executed in 78.02 seconds

```

Notice the generation time between first run and second run. Prompt executed in ...

Videos were generated in a size of 320 x 240 px

**Related** 
ComfyUI issue with further informations: https://github.com/Comfy-Org/ComfyUI/issues/12672

Assets contains the test_rocm.py, the wan image to video workflow and two example images in png format.

[assets.zip](https://github.com/user-attachments/files/25663525/assets.zip)

