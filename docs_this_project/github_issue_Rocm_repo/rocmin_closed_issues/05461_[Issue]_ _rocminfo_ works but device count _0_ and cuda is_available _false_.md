# [Issue]: "rocminfo" works but device count "0" and cuda is_available "false"

- **Issue #:** 5461
- **State:** closed
- **Created:** 2025-10-02T08:59:56Z
- **Updated:** 2025-10-06T11:07:01Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5461

### Problem Description

I have a Ubuntu WSL installation and im trying to use TTS-Webui with chatterbox but i can't generate audio at all. With the help of the developer of TTS-Webui i did some checks and rocm is installed properly but when using `python -c "import torch; print(f'CUDA/ROCm available: {torch.cuda.is_available()}, Device count: {torch.cuda.device_count()}')"` the output is `CUDA/ROCm available: False, Device count: 0`. On WSL i installed the driver with `amdgpu-install -y --usecase=wsl,rocm --no-dkmsI`. On Windows i originally was on Adrenalin 25.9.2 and it didn't work. I installed 25.3.1 as in this page (https://rocm.docs.amd.com/projects/radeon-ryzen/en/docs-6.3.4/docs/compatibility/wsl/wsl_compatibility.html) says that this driver officially supports wsl2 with rocm 6.3.4 but it still doesn't work.

The output of `AMD_LOG_LEVEL=3 python -c "import torch; print(torch.cuda.is_available())"` is 

:3:rocdevice.cpp            :469 : 1341533546d us:  Initializing HSA stack.
:3:hip_context.cpp          :49  : 1341534453d us:  Direct Dispatch: 1
:3:hip_device_runtime.cpp   :649 : 1341534484d us:   hipGetDeviceCount ( 0x7ffee00c60dc )
:3:hip_device_runtime.cpp   :651 : 1341534510d us:  hipGetDeviceCount: Returned hipErrorNoDevice :
:3:hip_error.cpp            :36  : 1341534532d us:   hipGetLastError (  )
:3:hip_error.cpp            :36  : 1341534554d us:  hipGetLastError: Returned hipErrorNoDevice :
False
:3:hip_device_runtime.cpp   :618 : 1341630470d us:   hipDeviceSynchronize (  )
:3:hip_device_runtime.cpp   :618 : 1341630503d us:  hipDeviceSynchronize: Returned hipErrorNoDevice :


### Operating System

Windows 11 Pro / WSL 

### CPU

AMD Ryzen 7 5800x3D

### GPU

AMD Radeon RX 7900GRE

### ROCm Version

ROCm 6.3.42131-fa1d09cbd

### ROCm Component

_No response_

### Steps to Reproduce

wget https://repo.radeon.com/amdgpu-install/6.4.2.1/ubuntu/noble/amdgpu-install_6.4.60402-1_all.deb
sudo apt install ./amdgpu-install_6.4.60402-1_all.deb
amdgpu-install -y --usecase=wsl,rocm --no-dkms

git clone https://github.com/rsxdalv/TTS-WebUI.git
cd TTS-WebUI
sh tools/conda_env_bash.sh
cd ..
AMD_LOG_LEVEL=3 python -c "import torch; print(torch.cuda.is_available())"



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_