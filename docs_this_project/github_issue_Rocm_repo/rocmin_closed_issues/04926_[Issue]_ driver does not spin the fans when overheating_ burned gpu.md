# [Issue]: driver does not spin the fans when overheating, burned gpu

- **Issue #:** 4926
- **State:** closed
- **Created:** 2025-06-13T20:47:44Z
- **Updated:** 2025-06-17T12:38:41Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4926

### Problem Description

ERROR:root:Driver not initialized (amdgpu not found in modules)

i have tried everything and have reinstalled the gpu many times. it worked previously but after reboot it suddenly doesn't work
i don't know what has caused it but i know none of known solutions fixed any issues.
last time i ran "amdgpu-install --usecase=graphics,rocm,opencl,hip,dkms"
and once i ran "amdgpu-install --usecase=graphics,rocm,opencl --no-dkms"
none worked. OS uses CPU intergrated graphics and none of the apps (CPU-X, CoreCtrl) detect it
CPU-X says it is there but no drivers or extra info, just device id

the commands above also don't detect GPU:
```
OS:
NAME="Ubuntu"
VERSION="24.04.2 LTS (Noble Numbat)"
CPU: 
model name	: Intel(R) Core(TM) i5-4570 CPU @ 3.20GHz
GPU:
```

by the way i am a little beginner in linux, this is my first time trying linux but i had no issues until recently.
i also had to move root partition and fix grub multiple times because i gave too little storage for ubuntu

### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

Intel(R) Core(TM) i5-4570 CPU @ 3.20GHz

### GPU

AMD Radeon RX 5600 (maybe XT)

### ROCm Version

rocm-core6.4.1/noble 6.4.1.60401-83~24.04 amd64

### ROCm Component

rocminfo

### Steps to Reproduce

i have no idea
here is the history, if it ever helps:

[history.txt](https://github.com/user-attachments/files/20732710/history.txt)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

/opt/rocm/bin/rocminfo --support
ROCk module is NOT loaded, possibly no GPU devices

### Additional Information

[dmesg.txt](https://github.com/user-attachments/files/20732743/dmesg.txt)