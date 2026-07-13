# ROCm not uninstalling and messing up pytorch-cpu RX6600XT

- **Issue #:** 1727
- **State:** closed
- **Created:** 2022-04-18T22:01:59Z
- **Updated:** 2024-04-05T23:41:11Z
- **Labels:** application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/1727

So I recently installed ROCm and anaconda and pytorch on new linux dualboot. But after finding out that my gpu is not compatible, I uninstalled ROCm and that version of pytorch and even reinstalled anaconda. But after installing pytorch-cpu and running in python it shows:
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
/opt/amdgpu/share/libdrm/amdgpu.ids: No such file or directory
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"

I dont know what to do, I have gone through the uninstall proceedure 3 times and it still isnt working. 

My gpu: RX6600XT(I understand that it is not supported but I thought I'll try to install since other similar gpus worked.)
ROCm version: 5.0.0
Rocm pytorch version: pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/rocm4.5.2

After running sudo amdgpu-uninstall : 
sudo: amdgpu-uninstall: command not found

After running sudo apt autoremove amdgpu-dkms or sudo apt autoremove rocm-core: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package amdgpu-dkms

At location /etc/apt/sources.list.d is no amd or rocm repository.

At this point I am considering just reinstalling linux.

I am new to linux and this stuff so sorry in advance if I accidantly messed up something simple.
Thanks.
