# Running both NVidia & AMD ROCm in a single machine

- **Issue #:** 626
- **State:** closed
- **Created:** 2018-11-27T01:47:58Z
- **Updated:** 2019-01-07T17:41:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/626

I have Ryzen 7 1800X and want to use both VEGA FE & GTX 1080 in that machine. I can use either GPU separately without issues. GTX1080 also works fine by itself in the secondary PCIe slot. However, if I put both graphics cards in, GUI does not come up even though I can log in to console and see that both graphics cards are working by using lspci/nvidia-smi/rocm-smi commands. Also, only the output from Vega seems to work, probably because MB initializes graphics card in the first PCIe slot. Since my motherboard is GA-AB350M-D3H (https://www.gigabyte.com/us/Motherboard/GA-AB350M-D3H-rev-10#kf), I must install VEGA FE in the first PCIe slot.

Is there a way go get both working? Preferably, I'd like to use GTX 1080 to drive the monitor.
Any help and pointers are appreciated. I tried https://askubuntu.com/questions/892532/nvidia-card-for-cuda-and-amd-card-for-display-on-ubuntu-16-04 but that does not seem to quite work for Ubuntu 18.04 which is what I'm running.

Thanks!