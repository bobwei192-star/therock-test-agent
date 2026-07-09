# Multi GPU scaling

- **Issue #:** 38
- **State:** closed
- **Created:** 2016-10-15T17:03:35Z
- **Updated:** 2016-10-18T03:04:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/38

Hello!
First of all, very cool project!

My question is not specific to ROCm, but it is related, and I thought you folks may have some advice on the following:

I have two RX 470 cards. I am running a series of OpenCL kernels which are fairly memory intensive : this is a video compression application, so a lot of data passes from host to GPU and back. There is also
high CPU usage.

When I run my kernels on a single 470, total frame rate is 40 FPS. When I use two 470s, frame rate equals
60 FPS.  There is no dependency in the code between the two devices.

 So, it looks like scaling is sub-optimal. I was hoping/expecting to get around 80 FPS for two cards. What factors may be affecting compute scaling on multiple cards?  How can I trouble-shoot this issue? 

Any advice would be greatly appreciated.

Thanks!
Aaron
