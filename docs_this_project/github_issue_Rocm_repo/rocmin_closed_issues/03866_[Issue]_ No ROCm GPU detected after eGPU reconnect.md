# [Issue]: No ROCm GPU detected after eGPU reconnect

- **Issue #:** 3866
- **State:** closed
- **Created:** 2024-10-05T11:51:05Z
- **Updated:** 2025-01-10T16:13:30Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 GRE
- **URL:** https://github.com/ROCm/ROCm/issues/3866

### Problem Description

ROCm sees 0 GPUs available after the eGPU is disconnected and reconnected (concrete use-cases: mobility, sleep mode on laptop). Games work perfectly after reconnecting the enclosure.

### Operating System

Arch Linux

### CPU

12th Gen Intel(R) Core(TM) i7-1260P

### GPU

AMD Radeon RX 7900 GRE

### ROCm Version

ROCm 6.0.0

### ROCm Component

ROCK-Kernel-Driver, ROCm, rocm-core, rocminfo

### Steps to Reproduce

1. Boot linux-lts 
2. Connect the eGPU enclosure (ref: [link](https://www.adt.link/product/UT3G.html)) with a Sapphire Pulse RX 7900 GRE
3. `rocminfo` returns 1 detected GPU, `rocm-smi` returns 1 GPU, PyTorch (just sometimes?) detects 1 CUDA GPU
4. Disconnect enclosure
5. Reconnect enclosure
6. `rocminfo` returns 0 detected GPUs, `rocm-smi` returns 2 GPUs, PyTorch (always) detects 0 CUDA GPUs

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is loaded
Unable to open /dev/kfd read-write: Invalid argument
mihai is member of render group

### Additional Information

- `sudo dmesg` output: [dmesg.log](https://github.com/user-attachments/files/17266021/dmesg.log)
- `sudo lshw` output: [lshw.txt](https://github.com/user-attachments/files/17267498/lshw.txt)
- package versions:
    - linux-lts: 6.6.52-1
    - linux-firmware: 20240909.552ed9b8-1
    - rocm-core: 6.0.2-2
    - rocminfo: 6.0.2-1
    - rocm-smi-lib: 6.0.2-1
- packages were installed using `pacman`, not using the provided driver from AMD
- booting linux instead of linux-lts does not fix the issue
- rebooting always solves the issue
- tried removing the amdgpu module, did not work
- tried forcefully removing the amdgpu module, resulted in (partial?) kernel panic, needed to reboot
- tried to change the firmware of the eGPU enclosure (provided by manufacturer on manufacturer's page), but without luck
