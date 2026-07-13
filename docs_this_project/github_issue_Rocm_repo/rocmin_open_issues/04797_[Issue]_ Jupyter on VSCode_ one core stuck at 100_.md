# [Issue]: Jupyter on VSCode, one core stuck at 100%

- **Issue #:** 4797
- **State:** open
- **Created:** 2025-05-23T23:09:00Z
- **Updated:** 2025-07-17T17:26:33Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4797

### Problem Description

First , i'm using wsl2 on windows 10 so maybe is this.
I used a cell (vscode + jupyter) to load a whisper model and keep it loaded but one CPU core is stuck at 100%, this happens with torch load too.
If i use device = cpu instead of cuda it work fine (model is loaded ram usage go up, the cpu does nothing since the model is not in use).

### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

13th Gen Intel(R) Core(TM) i5-13600K

### GPU

AMD Radeon RX 7800 XT

### ROCm Version

ROCm 6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

whisper_model = whisper.load_model("tiny", device="cuda")

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_