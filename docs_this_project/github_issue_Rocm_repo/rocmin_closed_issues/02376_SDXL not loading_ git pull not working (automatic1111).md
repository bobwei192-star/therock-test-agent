# SDXL not loading, git pull not working (automatic1111)

- **Issue #:** 2376
- **State:** closed
- **Created:** 2023-08-11T12:06:47Z
- **Updated:** 2024-02-14T02:38:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/2376

**Hello!When i'm trying to load SDXL model, i get the issue:**

`RuntimeError('Error(s) in loading state_dict for {}:\n\t{}'.format( RuntimeError: Error(s) in loading state_dict for LatentDiffusion: size mismatch for model.diffusion_model.input_blocks.4.1.proj_in.weight: copying a param with shape torch.Size([640, 640]) from checkpoint, the shape in current model is torch `

**Tried to start git pull through cmd in the SD folder, but getting this:**

```
There is no tracking information for the current branch. Please specify which branch you want to merge with. See git-pull(1) for details.

git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

git branch --set-upstream-to=<remote>/<branch> master
```
**I also get "Error loading script: [refiner.py](https://refiner.py/)"**

```
Error loading script: refiner.py

Traceback (most recent call last):

File "E:\automatic1111\stable-diffusion-webui-master\modules\scripts.py", line 263, in load_scripts

script_module = script_loading.load_module(scriptfile.path)

File "E:\automatic1111\stable-diffusion-webui-master\modules\script_loading.py", line 10, in load_module

module_spec.loader.exec_module(module)

File "<frozen importlib._bootstrap_external>", line 883, in exec_module

File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed

File "E:\automatic1111\stable-diffusion-webui-master\extensions\sd-webui-refiner\scripts\refiner.py", line 5, in <module>

import sgm.modules.diffusionmodules.denoiser_scaling

ModuleNotFoundError: No module named 'sgm'
```
**I tried to download everything fresh and it worked well (as git pull), but i have a lot of plugins, scripts i wasted a lot of time to settle so i would REALLY want to solve the issues on a version i have, would appreciate your help so much!
Also i have rtx 3070 8gb (laptop)**

**My WebUI settings:**

```
echo off

for /d %%x in (tmp\tmp*,tmp\pip*,tmp\gradio\*) do rd /s /q "%%x" 2>nul || ("%%x" && exit /b 1) & del /q tmp\tmp* > nul 2>&1 & rd /s /q pip\cache 2>nul

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS= --xformers
set COMMANDLINE_ARGS= --theme dark
set COMMANDLINE_ARGS= --medvram
call webui.bat
```
**List of extensions**:
deforum-for-automatic1111-webui
automatic1111-webui
ebsynth_utility
multidiffusion-upscaler-for-automatic1111
sd-webui-3d-open-pose-editor
sd-webui-aspect-ratio-helper
sd-webui-comfyui
sd-webui-controlnet
sd-webui-inpaint-anything
sd-webui-prompt-all-in-one
sd-webui-refiner
sd-webui-roop-nsfw
sd-webui-stablesr
sd_dreambooth_extension
stable-diffusion-webui-images-browser
LDSR
Lora
ScuNET
SwinIR
prompt-bracket-checker