# modprobe amdgpu crashes on Ubuntu 18.04 / kernel 4.18.x with amdgpu firmware binaries dated 12/08/2018

- **Issue #:** 716
- **State:** closed
- **Created:** 2019-02-20T20:17:05Z
- **Updated:** 2019-03-14T15:18:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/716

Setup:

* ASUS x86_64 Ubuntu 18.04 Bionic with 4.18.0-041800-generic kernel (or can be any point release 4.18.x or any 4.19.x)
* Vega 10 gfx900 WX 9100 GPU
* I have the amdgpu kernel module blacklisted so it doesn't load on boot

Then 
`sudo modprobe amdgpu`  will result in a kernel crash forcing a full power-cycle to recover (I can get the kernel logs as needed) when using `vega10_*.bin` firmware binaries dated 12/08/2018.

Is this a known issue?

Part of the reason I'm motivated to use the latest amdgpu (vega10) firmware is that my OpenCL testcase hangs on the clEnqueueMapBuffer (see Issue [67](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/67))

and some investigation shows my testcase is working in all instances where the latest firmware is successfully loaded by amdgpu (either dkms amdgpu on 4.15 or vanilla amdgpu in 4.20).

I'm wondering if there's an up-to-date kernel 4.18 that works with the latest provided firmware binaries.

Thanks for any insight you can provide!

-Ben