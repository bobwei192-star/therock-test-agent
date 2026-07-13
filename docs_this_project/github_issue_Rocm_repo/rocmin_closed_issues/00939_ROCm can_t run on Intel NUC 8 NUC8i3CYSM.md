# ROCm can't run on Intel NUC 8 NUC8i3CYSM

- **Issue #:** 939
- **State:** closed
- **Created:** 2019-11-19T07:52:24Z
- **Updated:** 2023-12-18T16:12:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/939

Hi guys,

I tried to install ROCm on Intel NUC 8 NUC8i3CYSM recently. After the installation, I couldn't run rocminfo or clinfo.

Hardware spec:
https://www.intel.com/content/www/us/en/products/boards-kits/nuc/mini-pcs/nuc8i3cysm.html

Intel Core i3-8121U (Gen 8)
RAM: 8GB
PCIe 3
GPU: Radeon RX540 with 2GB RAM
Disk: 128GB SSD

OS: Ubuntu 18.04.3 x64
ROCm: newest version 2.9

It's weird because lspci says it's RX550.
$ lspci | grep VGA
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon RX 550/550X] (rev c3)

Before I could install ROCm on NUC, I failed once due to Intel Security check. It failed at last step to install. Then I rebooted to BIOS and disable Intel security technology, and booted to Ubuntu and apt autoremove rocm-dkms and apt install rocm-dkms again. I am not sure whether this is clean enough.

Then I followed the guide at https://rocm.github.io/ROCmInstall.html#installing-from-amd-rocm-repositories, till:

$ /opt/rocm/bin/rocminfo 
ROCk module is loaded
username is member of video group
Killed

And at the console I found some error messages

![1623148944](https://user-images.githubusercontent.com/4979674/69127020-6c0f8880-0ae4-11ea-9c4a-0267310a551d.jpg)

$ /opt/rocm/opencl/bin/x86_64/clinfo 

It hangs there always, then I killed it.

![1769260135](https://user-images.githubusercontent.com/4979674/69127026-6e71e280-0ae4-11ea-9c7f-d6c6dab0c9c8.jpg)

At last I could not restart the box normally because clinfo hangs there. 

What would be the problem?

Thanks,

Gavin