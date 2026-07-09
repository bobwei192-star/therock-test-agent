# Segmentation fault in Ubuntu 16.04.3

- **Issue #:** 280
- **State:** closed
- **Created:** 2017-12-21T18:49:02Z
- **Updated:** 2018-06-03T15:26:18Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/280

**DISCLAIMER**: Yes, I have tried the installation method at https://rocm.github.io/ROCmInstall.html. With multiple kernel versions (4.4, 4.10, 4.11, 4.14.8, 4.15-rc4). Some of them just wouldn't build. Some I'd get the same behavior I'm describing here.

The system is a Ubuntu 16.04.3 with kernel 4.4.0-104-generic. I decided just to go with the default kernel and the normal installation of amdgpu-pro 17.40 after failing miserably to install with rocm-dkms (as stated above). My system has 4 VGAs: 2 Tonga, 1 Hawaii and 1 RX Vega 56.

After installing the 17.40 driver, clinfo works OK but it can only see the first 3 cards, i.e. it doesn't see Vega. Then I add ROCm with "apt install -y rocm-amdgpu-pro" as per http://support.amd.com/en-us/kb-articles/Pages/AMDGPU-PRO-Install.aspx and run clinfo again:

```
root@aaaa:~# clinfo
Segmentation fault (core dumped)

```

On dmesg, what I see is:

```
[ 2086.221499] amdgpu: [powerplay] 
                failed to send pre message 145 ret is 0 
[ 2086.637046] amdgpu: [powerplay] 
                failed to send message 145 ret is 0 
[ 2087.468138] amdgpu: [powerplay] 
      *          failed to send pre message 146 ret is 0 
[ 2087.883676] amdgpu: [powerplay] 
                failed to send message 146 ret is 0 
[ 2087.926991] clinfo[2447]: segfault at 1 ip 00007f3aaecc862d sp 00007fff1fe12d90 error 4 in libhsakmt.so.1.0.0[7f3aaecbb000+15000]
[ 2088.882545] amdgpu: [powerplay] 
                failed to send pre message 145 ret is 0 
[ 2089.298094] amdgpu: [powerplay] 
                failed to send message 145 ret is 0 
[ 2090.129184] amdgpu: [powerplay] 
                failed to send pre message 146 ret is 0 
[ 2090.544809] amdgpu: [powerplay] 
                failed to send message 146 ret is 0 
```

For reference, the relevant bit of my lspci is:

```
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Amethyst XT [Radeon R9 M295X Mac Edition / R9 380X] (rev f1)
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tonga HDMI Audio [Radeon R9 285/380]
02:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Amethyst XT [Radeon R9 M295X Mac Edition / R9 380X] (rev f1)
02:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Tonga HDMI Audio [Radeon R9 285/380]
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii XT [Radeon R9 290X]
04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Hawaii HDMI Audio
05:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1470 (rev c3)
06:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD] Device 1471
07:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c3)
07:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf8
```
**EDIT**: I should also note that when ROCm is installed (regardless of installation method) it's making the fan on the GPU at my 1st PCI slot go crazy (like it was under heavy load all the time).
**EDIT 2**: It seems that I only get the crash when the Hawaii card is plugged in. When it is removed, clinfo executes fine, but it only finds 1 Tonga (the one whose fan is going nuts) and none of the other Tongas or Vegas.
**EDIT 3**: I see the 'failed to send message' errors in dmesg anyway, even when clinfo does work without the segfault, and I see them early in dmesg too, when the system is still initializing.