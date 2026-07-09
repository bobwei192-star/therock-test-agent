# Installation Problems on openSUSE Tumbleweed.

- **Issue #:** 1534
- **State:** closed
- **Created:** 2021-07-25T17:34:19Z
- **Updated:** 2021-07-27T07:20:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/1534

Hi,

My PC has AMD CPU(Ryzen 5900X) and an AMD graphic card(RX6800XT) (Of course, I'm a super AMD fan), so I want to use my GPU to do some scientific computation. The operating system is openSUSE Tumbleweed(20210726). I want the minimal installation of ROCm on my PC.

I add the repository resource via: `sudo zypper addrepo --no-gpgcheck http://repo.radeon.com/rocm/zyp/zypper/ rocm`
But I don't know which are the necessary packages for the ROCm.
And I find that:

Some packages can be installed directly.
`rock-dkms`
`rocm-gdb`: requires me to install python36 (My OS has python38 installed)
`rocminfo`
`rocm-opencl`
`rocm-opencl-devel`
`rocm-device-libs`
`hsakmt-roct`
`hipify-clang`
...

Some packages cannot be installed with dependencies problems.
`rocm-dkms` 
`rocm-dev`
`rccl`
`rocm-libs`
`hip-samples`
...

I'm new to computational science, could you tell me the minimal installation of ROCm environment requires me to install which packages from the [official repo](http://repo.radeon.com/rocm/zyp/zypper/)?
I just want to use [tensorflow-rocm](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream) and [CuPy-ROCm](https://pypi.org/project/cupy-rocm-4-0/).

I would appreciate it if you can respond to me.



