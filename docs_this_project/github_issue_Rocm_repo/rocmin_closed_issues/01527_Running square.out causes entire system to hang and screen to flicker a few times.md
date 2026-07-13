# Running square.out causes entire system to hang and screen to flicker a few times 

- **Issue #:** 1527
- **State:** closed
- **Created:** 2021-07-17T08:18:04Z
- **Updated:** 2021-07-20T07:10:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/1527

As the title stated, I am trying to get ROCm to work on my Laptop with AMD Ryzen 7 4800U with integrated Radeon graphics.

I am using Ubuntu 20.04, with kernel 5.8.0-59-generic.
I've also tried reinstalling rocm multiple times with:
```
sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils
sudo apt install rocm-dkms
```
Without rebooting my laptop, running square.out works perfectly fine.

However, when I try rebooting ubuntu and running the same program again, I get the following output

```
info: running on device Renoir
info: allocate host mem ( 7.63mb)
info: allocate device mem ( 7.63mb)
info: copy Host2Device
```
and my ubuntu hangs immediately. 
I can still move my cursor around, but nothing responds to any clicks or whatsoever and I have to force shutdown the laptop.

can anyone please suggest how I may be able to figure out the root cause and how i could fix it? Thank you.