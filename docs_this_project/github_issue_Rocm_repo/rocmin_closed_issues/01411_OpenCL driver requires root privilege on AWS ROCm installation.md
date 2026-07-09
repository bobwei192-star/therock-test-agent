# OpenCL driver requires root privilege on AWS ROCm installation 

- **Issue #:** 1411
- **State:** closed
- **Created:** 2021-03-19T23:01:26Z
- **Updated:** 2021-05-07T13:01:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1411

I am working to port cuDNN code to MiOpen on AWS AMD GPU clusters.
ROCm is not officially supported on AWS clusters AMD GPUs since they are gfx1011.
However, lots of functionality is working but only with root privileges. For example:
`$> /opt/rocm/opencl/bin/clinfo`

`ERROR: clGetPlatformIDs(-1001)`

But it works with sudo:
`$> sudo /opt/rocm/opencl/bin/clinfo`

When I run my application in GDB it gives more details of the failure:
`No OpenCL platforms found on this system. Ensure you have installed the device driver as well as the OpenCL runtime and ICD from your device vendor. You can use the clinfo utility to debug OpenCL installation issues.`

`/dev/kfd`  is properly owned by user video and my user is in that group.

`dmesg | grep amdgpu`
shows lines like:
`[189766.627920] amdgpu 0000:00:1d.0: amdgpu: Msg issuing pre-check failed and SMU may be not in the right state!`

Followed the [official installation instructions](https://rocmsoftwareplatform.github.io/MIOpen/doc/html/install.html) 
And needed this [excellent support thread](https://github.com/RadeonOpenCompute/ROCm/issues/738) on this site to get it working 

I found a number of threads by people struggling to get ROCm working on AWS and followed a number of them but root privilege is still required. However, some other utils that I need are not compatible with running under sudo.
Some threads claimed that it was due to have AMD-pro driver installed along side ROCm. I have only the ROCm OpenCL driver installed

```
dpkg -l "*opencl*"


||/ Name                                                     Version                           Architecture                      Description
+++-========================================================-=================================-=================================-===============================================================================

un  libopencl-1.1-1                                          <none>                            <none>                            (no description available)
un  libopencl-1.2-1                                          <none>                            <none>                            (no description available)
un  libopencl-2.0-1                                          <none>                            <none>                            (no description available)
un  libopencl-2.1-1                                          <none>                            <none>                            (no description available)
un  libopencl1                                               <none>                            <none>                            (no description available)
ii  miopen-opencl                                            2.9.0.8250-rocm-rel-4.0-23-8a4af4 amd64                             AMD's DNN Library
un  nvidia-libopencl1-dev                                    <none>                            <none>                            (no description available)
ii  ocl-icd-libopencl1:amd64                                 2.2.11-1ubuntu1                   amd64                             Generic OpenCL ICD Loader
ii  opencl-c-headers                                         2.2~2018.02.21-gb5c3680-1         all                               OpenCL (Open Computing Language) C header files
ii  opencl-clhpp-headers                                     2.0.10+git12-g5dd8bb9-1           all                               C++ headers for OpenCL development
un  opencl-clhpp-headers-doc                                 <none>                            <none>                            (no description available)
ii  opencl-headers                                           2.2~2018.02.21-gb5c3680-1         all                               OpenCL (Open Computing Language) header files
un  opencl-icd                                               <none>                            <none>                            (no description available)
ii  rocm-opencl                                              3.6Beta-17-g875c1f8-rocm-rel-4.0- amd64                             OpenCL: Open Computing Language on ROCclr
ii  rocm-opencl-dev                                          3.6Beta-17-g875c1f8-rocm-rel-4.0- amd64                             OpenCL: Open Computing Language on ROCclr
```

I think that it is a user-space issue since the admgpu kernel model seems to have a few issues but it end up working:
```
dmesg | grep amdgpu 

[    4.457490] [drm] amdgpu kernel modesetting enabled.
[    4.461722] [drm] amdgpu version: 5.6.19
[    4.468966] amdgpu: CRAT table not found
[    4.472645] amdgpu: Virtual CRAT table created for CPU
[    4.476983] amdgpu: Topology: Add CPU node
[    4.482437] amdgpu 0000:00:1d.0: remove_conflicting_pci_framebuffers: bar 0: 0x2040000000 -> 0x204fffffff
[    4.490458] amdgpu 0000:00:1d.0: remove_conflicting_pci_framebuffers: bar 2: 0x2060000000 -> 0x20601fffff
[    4.498381] amdgpu 0000:00:1d.0: remove_conflicting_pci_framebuffers: bar 5: 0xfea80000 -> 0xfeafffff
[    4.513824] amdgpu 0000:00:1d.0: amdgpu: Trusted Memory Zone (TMZ) feature disabled as experimental (default)
[    4.521928] amdgpu 0000:00:1d.0: amdgpu: set kernel compute queue number to 8 due to invalid parameter provided by user
[    4.703531] amdgpu 0000:00:1d.0: amdgpu: Fetched VBIOS from VRAM BAR
[    4.708333] amdgpu: ATOM BIOS: 113-D3050100-101
[    4.727924] amdgpu 0000:00:1d.0: amdgpu: VRAM: 8048M 0x0000008000000000 - 0x00000081F6FFFFFF (8048M used)
[    4.735913] amdgpu 0000:00:1d.0: amdgpu: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[    4.769384] [drm] amdgpu: 8048M of VRAM memory ready
[    4.773592] [drm] amdgpu: 127320M of GTT memory ready.
[    4.960293] amdgpu 0000:00:1d.0: amdgpu: smu driver if version = 0x00000036, smu fw if version = 0x00000038, smu fw version = 0x00341e00 (52.30.0)
[    4.970202] amdgpu 0000:00:1d.0: amdgpu: SMU driver if version not matched
[    4.975411] amdgpu 0000:00:1d.0: amdgpu: use vbios provided pptable
[    4.980148] amdgpu 0000:00:1d.0: amdgpu: smc_dpm_info table revision(format.content): 4.7
[    4.988043] amdgpu 0000:00:1d.0: amdgpu: SMU is initialized successfully!
[    5.007643] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    5.013996] amdgpu: Virtual CRAT table created for GPU
[    5.018321] amdgpu: Topology: Add dGPU node [0x7362:0x1002]
[    5.022815] kfd kfd: amdgpu: added device 1002:7362
[    5.031925] amdgpu 0000:00:1d.0: amdgpu: SE 2, SH per SE 2, CU per SH 10, active_cu_number 36
[    5.131265] amdgpu 0000:00:1d.0: fb0: amdgpudrmfb frame buffer device
[    5.152404] amdgpu 0000:00:1d.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
```





