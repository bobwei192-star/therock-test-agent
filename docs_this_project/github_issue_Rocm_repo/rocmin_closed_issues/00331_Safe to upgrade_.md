# Safe to upgrade?

- **Issue #:** 331
- **State:** closed
- **Created:** 2018-02-11T06:15:07Z
- **Updated:** 2018-02-16T22:41:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/331

Hi,

I am on Ubuntu 16.04 and rocking ROCm with Ryzen and Vega.
I added the Padoka PPA Mesa, but haven't actually upgraded to Mesa git yet (I am still on 17.2.4).

Additionally, when I do:
```bash
$ sudo apt-get install libclblas-dev
[sudo] password for chris: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libclblas2 libdrm-dev libgl1-mesa-dev libpthread-stubs0-dev libx11-dev libx11-doc libx11-xcb-dev libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-shape0-dev libxcb-sync-dev
  libxcb-xfixes0-dev libxcb1-dev libxdamage-dev libxdmcp-dev libxext-dev libxfixes-dev libxshmfence-dev libxxf86vm-dev mesa-common-dev ocl-icd-libopencl1 ocl-icd-opencl-dev opencl-headers x11proto-core-dev x11proto-damage-dev x11proto-dri2-dev x11proto-fixes-dev
  x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-xext-dev x11proto-xf86vidmode-dev xorg-sgml-doctools xtrans-dev
```

```bash
$ sudo apt-get install libclfft-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libclfft2 libdrm-dev libgl1-mesa-dev libpthread-stubs0-dev libx11-dev libx11-doc libx11-xcb-dev libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-shape0-dev libxcb-sync-dev
  libxcb-xfixes0-dev libxcb1-dev libxdamage-dev libxdmcp-dev libxext-dev libxfixes-dev libxshmfence-dev libxxf86vm-dev mesa-common-dev ocl-icd-libopencl1 ocl-icd-opencl-dev opencl-headers x11proto-core-dev x11proto-damage-dev x11proto-dri2-dev x11proto-fixes-dev
  x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-xext-dev x11proto-xf86vidmode-dev xorg-sgml-doctools xtrans-dev
```

```bash
$ sudo apt-get install libglfw3-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libdrm-dev libgl1-mesa-dev libglfw3 libglu1-mesa-dev libpthread-stubs0-dev libx11-dev libx11-doc libx11-xcb-dev libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxcb-randr0-dev libxcb-render0-dev libxcb-shape0-dev
  libxcb-sync-dev libxcb-xfixes0-dev libxcb1-dev libxcursor-dev libxdamage-dev libxdmcp-dev libxext-dev libxfixes-dev libxi-dev libxinerama-dev libxrandr-dev libxrender-dev libxshmfence-dev libxxf86vm-dev mesa-common-dev x11proto-core-dev x11proto-damage-dev
  x11proto-dri2-dev x11proto-fixes-dev x11proto-gl-dev x11proto-input-dev x11proto-kb-dev x11proto-randr-dev x11proto-render-dev x11proto-xext-dev x11proto-xf86vidmode-dev x11proto-xinerama-dev xorg-sgml-doctools xtrans-dev
```

The number of packages that would be installed is rather...large, and I am concerned that some of them will conflict with ROCm.
Is it safe to install these? If not, are there any good workarounds? Trying to build these from source?

I ask, because I had installed these, and I do not remember what else over the past month. I did not reboot my computer over that time, but when I finally did just now, it would not -- after grub, everything was blank. Googling, it sounded like GPU driver problems.
So I wiped everything, reinstalled, and started over.
Hence my concern over how sensitive ROCm is.

I primarily use ROCm through Julia. Julia's CLArray's library requires CLBLAS and CLFFT as dependencies. It's a little limiting to only have access to GPGPU through compiling HIP into shared libraries, although that has been working well.

On that note, compiling `hipcc -shared -fPIC name.cpp -o name.so` gives me a warning that `shared` was an unused argument, but everything works as intended.

Thanks for the great work, and looking forward to Linux Kernel 17.

PS. 
I do not have a background in C++ or GPGPU/Cuda, so I found basic things like this
https://github.com/ROCm-Developer-Tools/HIP/tree/master/samples/2_Cookbook
very helpful as an introduction.

EDIT:
This isn't so much an issue as a question.
Is there a better place to ask?

EDIT:
Are there some settings I can change in VSCode so that its linter works correctly?
For `hipLaunchKernel`, `__global__`, etc:
`grep -r hipLaunchKernel .` from within `/opt/rocm`, and all I find is the obvious `hip/include`. Adding this does not stop VSCode from registering these as errors. But the code compiles fine.
Is there some way I can make it aware of `hipcc`?
Or some other better supported editor?