# On the issue of RCOM not being properly recognized under WSL2

- **Issue #:** 5007
- **State:** open
- **Created:** 2025-07-08T12:35:02Z
- **Updated:** 2025-08-08T14:50:55Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5007

### System Environment Description

1. Windows 10 latest version with WSL2 Ubuntu 22.04  
2. GPU: RX 9070 XT; CPU: Ryzen 7 9700X  
3. ROCm 6.4.1; PyTorch 2.6.0; vLLM 0.8.2 (using 0.8.2 because vLLM 0.9.1 requires PyTorch 2.7.0)  
4. ROCm [installation reference](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html);  
   PyTorch [installation reference](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-pytorch.html)  

### Self-check status

`
rocminfo
Agent 2
  Name:                    gfx1201
  Marketing Name:          AMD Radeon RX 9070 XT
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU`

`root@DESKTOP-3IMOAOF:~# python3 -c 'import torch' 2> /dev/null && echo 'Success' || echo 'Failure'
Success`
`root@DESKTOP-3IMOAOF:~# python3 -c 'import torch; print(torch.cuda.is_available())'
True`

`root@DESKTOP-3IMOAOF:~# python3 -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"
/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py:736: UserWarning: Can't initialize amdsmi - Error code: 34
  warnings.warn(f"Can't initialize amdsmi - Error code: {e.err_code}")
device name [0]: AMD Radeon RX 9070 XT`

`
# modprobe amdgpu command fails after WSL reboot
root@DESKTOP-3IMOAOF:~# lsmod | grep amdgpu
root@DESKTOP-3IMOAOF:~# rocm-smi
ERROR:root:Driver not initialized (amdgpu not found in modules)
root@DESKTOP-3IMOAOF:~# modprobe amdgpu
root@DESKTOP-3IMOAOF:~# lsmod | grep amdgpu
amdgpu               8892416  0
drm_exec               12288  1 amdgpu
amdxcp                 12288  1 amdgpu
drm_buddy              16384  1 amdgpu
gpu_sched              49152  1 amdgpu
video                  65536  1 amdgpu
drm_suballoc_helper    12288  1 amdgpu
drm_display_helper    155648  1 amdgpu
i2c_algo_bit           12288  1 amdgpu
root@DESKTOP-3IMOAOF:~# rocm-smi
ERROR:root:ROCm SMI returned 8 (the expected value is 0)`

### Problem Description
The /dev/kfd and /dev/dri directories do not exist, and the rocm-smi command reports errors. I suspect the GPU passthrough feature is not working. The GPU driver on Windows is the latest version (25.6.1). How can I resolve this?
When running large models with vLLM, errors occur, but running them directly with PyTorch works fine. However, this remains an issue, and a fix is expected to be provided.
