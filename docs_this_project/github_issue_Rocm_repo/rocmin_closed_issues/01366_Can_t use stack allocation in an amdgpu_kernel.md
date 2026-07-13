# Can't use stack allocation in an amdgpu_kernel 

- **Issue #:** 1366
- **State:** closed
- **Created:** 2021-01-23T22:13:38Z
- **Updated:** 2021-01-28T06:18:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1366

Whenever an amdgpu_kernel (developed in LLVM IR) makes use of stack allocation, its execution fails with:

:0:rocdevice.cpp            :2303: 6709330589 us: Device::callbackQueue aborting with status: 0x29

A simple kernel that copies an input array of floats to an output array fails whenever it does so storing the float first onto the stack. This stack problem occurs in our application and I was able to boil it down to said simple kernel. I uploaded the minimal exploit onto pastebin (see below).

The workflow is a follows:

1) module.ll gets compiled to module.o using LLVM clang that comes with ROCm 4.0
2) module.o gets relinked to a shared object (module.so) using LLD (that also comes with ROCm)
3) read_launch reads module.so, allocates and initializes arrays of floats.
4) read_launch launches the kernel when the error occurs on the subsequent memory copy DtoH.

I attach a complete exploit via several pastebins. The GCN architecture is set to 'gfx1010' which you might have to adjust to your setup.

To replicate the issue issue:

make read_launch
make module.o
make module.so
./read_launch

On my system this fails with the above error. The system this was tested on is Ubuntu 20.04 with a Navi 10 [Radeon RX 5600 OEM/5600 XT / 5700/5700 XT] on Linux 5.4.0-42-generic

[module.ll](https://pastebin.com/j0ukjYP1)
[Makefile](https://pastebin.com/ms75LveE)
[read_launch.cc](https://pastebin.com/FUksb7pm)

To prove that the whole setup works and the issue is indeed related to the stack allocation in the kernel I attach the simple kernel without any stack usage. Renaming this kernel (module_copy.ll) to module.ll and making the shared object (module.so) lets the program run without errors.

[module_copy.ll](https://pastebin.com/R3sxwHq9)

