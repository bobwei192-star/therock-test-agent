# rocminfo fails with Ubuntu 18.04 and ROCm 2.2

- **Issue #:** 753
- **State:** closed
- **Created:** 2019-03-31T14:23:55Z
- **Updated:** 2019-03-31T20:37:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/753

I have a clean Ubuntu 18.04 installation (kernel 4.18), and I am trying to install ROCm, version 2.2. My GPU is a Radeon VII. I am following the steps [here](https://towardsdatascience.com/train-neural-networks-using-amd-gpus-and-keras-37189c453878).

I can successfully run
`sudo apt install rocm-dkms`
and then add the video group and reboot.

However, when I run
`/opt/rocm/bin/rocminfo`
I get
>hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.2/rocminfo/rocminfo.cc. Call returned 4104

If I run
`/opt/rocm/opencl/bin/x86_64/clinfo`
the output is
>ERROR: clGetPlatformIDs(-1001)

`dmesg | grep kfd` produces no output at all. I also see that there is no kfd folder in /dev.

`lspci | grep VGA` gives

> 0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 20 (rev c1)

Thanks in advance for any help.

