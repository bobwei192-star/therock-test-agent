# Will my setup rx 580 (Polaris/gfx803) setup function in AMD's ROCm and HIP applications (eg. blender when it adds legacy cards support) ?

- **Issue #:** 1745
- **State:** closed
- **Created:** 2022-05-29T13:23:16Z
- **Updated:** 2024-01-26T08:45:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/1745

OS : Arch linux Rolling x64
System : 

{CPU : i5-4570s
               RAM : 16GB 1666mhz ddr3
               GPU : RX 580 8GB}


Driver : mesa-tkg-git + amdgpu-pro (userspace only) + ROCm

Mesa ver :  22.2.0-devel

AMDGPU-PRO ver : 22.10

AMDGPU-PRO pkgs : 


{local/amdgpu-pro-libgl 22.10_1395274-1
                                    local/amf-amdgpu-pro 22.10_1395274-1
                                    local/lib32-amdgpu-pro-libgl 22.10_1395274-1
                                    local/lib32-opencl-legacy-amdgpu-pro 22.10.1_1401426-1
                                    local/lib32-vulkan-amdgpu-pro 22.10_1395274-1
                                     local/opencl-legacy-amdgpu-pro 22.10.1_1401426-1
                                     local/vulkan-amdgpu-pro 22.10_1395274-1}



ROCm ver : 5.1.1

ROCm pkgs : 


{local/rocblas 5.1.1-1 (patched for polaris)
                       local/rocm-cmake 5.1.3-1
                       local/rocm-core 5.1.3-1
                       local/rocm-device-libs 5.1.1-1
                       local/rocm-hip-runtime 5.1.3-1
                       local/rocm-language-runtime 5.1.3-1
                       local/rocm-llvm 5.1.1-1
                       local/rocm-opencl-runtime 5.1.1-1 (patched for polaris)
                       local/rocminfo 5.1.1-2}


my end goal is to know if i have a system that : 

- [x] Supports AMD's ROCm OpenCL runtime
- [x] Supports AMD's ROCm HIP runtime
- [ ] Supports Blender's Implementation of ROCm HIP 


And i have included as much debugging outputs as i can. 
                      
[clinfo output](https://github.com/RadeonOpenCompute/ROCm/files/8793412/cl-output.txt)
[hipInfo output](https://github.com/RadeonOpenCompute/ROCm/files/8793413/hip-output.txt)
[rocminfo output](https://github.com/RadeonOpenCompute/ROCm/files/8793414/rocm-output.txt)
["vulkaninfo --summary" output](https://github.com/RadeonOpenCompute/ROCm/files/8793415/vulkan-output.txt)

