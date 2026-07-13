# [Issue]: running voxCPM model caused Computer crashes

- **Issue #:** 5716
- **State:** closed
- **Created:** 2025-11-28T06:16:11Z
- **Updated:** 2026-01-29T19:06:49Z
- **Labels:** status: triage
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5716

### Problem Description


Running following code

```
import soundfile as sf
from voxcpm import VoxCPM

model = VoxCPM.from_pretrained("/home/gqy/.cache/modelscope/hub/models/OpenBMB/VoxCPM-0.5B")

wav = model.generate(
    text="哼…哼哈哈…哈哈哈！真是可笑啊！这污浊的世界，竟妄想用平凡的枷锁束缚本王？（缓缓抬头，指缝间露出锐利的目光）吾之右眼封印着混沌的深渊，左眼则倒映着星辰的终焉。当双眸再次同时睁开之时，便是因果逆转、法则重构之刻！凡人，庆幸吧——你此刻见证的，将是新纪元的第一缕曙光！碎裂吧，现实的幻象！降临吧，吾的‘寂灭永恒领域’！",
    prompt_wav_path=None,      # optional: path to a prompt speech for voice cloning
    prompt_text=None,          # optional: reference text
    cfg_value=2.0,             # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
    inference_timesteps=10,   # LocDiT inference timesteps, higher for better result, lower for fast speed
    normalize=True,           # enable external TN tool
    denoise=True,             # enable external Denoise tool
    retry_badcase=True,        # enable retrying mode for some bad cases (unstoppable)
    retry_badcase_max_times=3,  # maximum retrying times
    retry_badcase_ratio_threshold=6.0, # maximum length restriction for bad case detection (simple but effective), it could be adjusted for slow pace speech
)

sf.write("output2.wav", wav, 16000)
print("saved: output.wav")

```
success to output wav file, but   Computer crashes Shader Interpolator 100%。

### Operating System

Ubuntu 24

### CPU

AMD radeon AI max+395

### GPU

product: Strix Halo [Radeon Graphics / Radeon 8050S Graphics / Radeon 8060S Graphics]

### ROCm Version

ROCk module version 6.16.6 is loaded

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_