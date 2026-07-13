# [Issue]: Linux (non-WSL) installation of ROCm 6.2.4 appears to have core dependencies upon libdxcore.so (WSL specific)

- **Issue #:** 4053
- **State:** closed
- **Created:** 2024-11-23T19:00:20Z
- **Updated:** 2026-02-03T17:51:52Z
- **Labels:** Under Investigation, ROCm 6.2.3, Radeon 780M Graphics
- **URL:** https://github.com/ROCm/ROCm/issues/4053

### Problem Description

As the title suggests.   Attempts to build software that uses `amdgpu-arch` and other tooling, fails.

>>> joe@zap:~/build/rocHPL $ /opt/rocm-6.2.4/lib/llvm/bin/amdgpu-arch
Failed to 'dlopen' libhsa-runtime64.so
Failed to load libamdhip64.so: libdxcore.so: cannot open shared object file: No such file or directory

The requested info:joe@zap:~/build/rocHPL $   echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
  echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
  echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
OS:
NAME="Linux Mint"
VERSION="22 (Wilma)"
CPU:
model name      : AMD Ryzen 9 PRO 7940HS w/ Radeon 780M Graphics
GPU:
/opt/rocm/bin/rocminfo: error while loading shared libraries: libdxcore.so: cannot open shared object file: No such file or directory

More specifically
joe@zap:~/build/rocHPL $ dpkg -l | grep wsl
ii  hsa-runtime-rocr4wsl-amdgpu:amd64              1.14.0-2071946.24.04                       amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms in WSL environments.
ii  rocminfo4wsl-amdgpu:amd64                      1.14.0-2071946.24.04                       amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool for WSL environments.

Attempts to remove this are catastrophic for ROCm.

>>> joe@zap:~/build/rocHPL $ sudo apt remove hsa-runtime-rocr4wsl-amdgpu:amd64 rocminfo4wsl-amdgpu:amd64
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  amd-smi-lib comgr composablekernel-dev half hipfft hipfft-dev hipify-clang hiprand hiprand-dev
  hiptensor hiptensor-dev hsa-amd-aqlprofile hsakmt-roct-dev libasan6 libavcodec-dev
  libavformat-dev libavutil-dev libdrm-amdgpu-dev libelf-dev libfile-copy-recursive-perl
  libfile-which-perl libgcc-11-dev libset-scalar-perl libstdc++-11-dev libswresample-dev
  libswscale-dev libsystemd-dev libva-dev libva-glx2 rocfft rocfft-dev rocm-cmake rocm-core
  rocm-dbgapi rocm-debug-agent rocm-device-libs rocm-gdb rocm-llvm rocm-opencl-icd-loader
  rocm-smi-lib rocprofiler-register rocprofiler-sdk rocprofiler-sdk-roctx rocrand rocrand-dev
  roctracer roctracer-dev rocwmma-dev valgrind
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  hip-dev hip-doc hip-runtime-amd hip-samples hipblas hipblas-dev hipblaslt hipblaslt-dev hipcc
  hipcub-dev hipfort-dev hipsolver hipsolver-dev hipsparse hipsparse-dev hipsparselt
  hipsparselt-dev hsa-rocr-dev hsa-runtime-rocr4wsl-amdgpu migraphx migraphx-dev miopen-hip
  miopen-hip-dev mivisionx mivisionx-dev openmp-extras-dev openmp-extras-runtime rccl rccl-dev
  rocalution rocalution-dev rocblas rocblas-dev rocdecode rocdecode-dev rocm rocm-dev
  rocm-developer-tools rocm-hip-libraries rocm-hip-runtime rocm-hip-runtime-dev rocm-hip-sdk
  rocm-language-runtime rocm-ml-libraries rocm-ml-sdk rocm-opencl rocm-opencl-dev
  rocm-opencl-runtime rocm-opencl-sdk rocm-openmp-sdk rocm-utils rocminfo4wsl-amdgpu rocprim-dev
  rocprofiler rocprofiler-dev rocprofiler-plugins rocsolver rocsolver-dev rocsparse rocsparse-dev
  rocthrust-dev rpp rpp-dev
0 upgraded, 0 newly installed, 63 to remove and 0 not upgraded.
After this operation, 25.4 GB disk space will be freed.
Do you want to continue? [Y/n]

Please do not include WSL dependencies in linux.  

It appears that the breakage is in the rocm-llvm package

>>> root@zap:/home/joe/build/rocHPL# dpkg-query -S /opt/rocm-6.2.4/lib/llvm/bin/amdgpu-arch
rocm-llvm: /opt/rocm-6.2.4/lib/llvm/bin/amdgpu-arch


>>> 

### Operating System

Linux Mint 22 (based upon Ubuntu 24.04)

### CPU

AMD Ryzen 9 PRO 7940HS 

### GPU

Radeon 780M Graphics

### ROCm Version

ROCm 6.2.3

### ROCm Component

ROCm

### Steps to Reproduce

Install 6.2.4 on Ubuntu 24.04 or rebuilds running on bare metal.  Try to run rocminfo.  Or /opt/rocm-6.2.4/lib/llvm/bin/amdgpu-arch

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

root@zap:/home/joe/build/rocHPL# /opt/rocm/bin/rocminfo --support
/opt/rocm/bin/rocminfo: error while loading shared libraries: libdxcore.so: cannot open shared object file: No such file or directory

### Additional Information

_No response_