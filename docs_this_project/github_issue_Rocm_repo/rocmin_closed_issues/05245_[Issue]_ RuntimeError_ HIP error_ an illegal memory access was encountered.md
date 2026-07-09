# [Issue]: RuntimeError: HIP error: an illegal memory access was encountered

- **Issue #:** 5245
- **State:** closed
- **Created:** 2025-09-03T06:30:42Z
- **Updated:** 2026-02-26T10:00:08Z
- **Labels:** Under Investigation
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5245

### Problem Description

hello everyone. I am using a newly purchased PC with AI MAX+395 and Ubuntu 24.04. When I use rocm6.4, the installation is normal, but when I start using any AI app, it reports an error:

**torch.AcceleratorError:** 
**HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.**

I have studied the discussions in the Git community and it seems that 6.4 cannot support gfx1151, so I followed the discussion and used the development version of rocm7, which is currently available. but at
During use, whether it is inference, model training, or daily use, there will be sudden black screens randomly, which will cause my Ubuntu to log out and return to the interface waiting to enter my account and password.
The following text is the error message:

**RuntimeError: HIP error: an illegal memory access was encountered
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.**
**For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.**

I noticed that there are also many similar discussions in the Git discussion forum. The AI MAX+395 has been sold in the market for a long time, and its main sales content is AI. But now it has been unable to be used stably. ROCM7 is not sure when it will be released, I will use the following link:

**pip install   --index-url  https://d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/    rocm[libraries,devel]**

But this development version is very unstable. I am very worried about becoming an abandoned user, and I want to know how to deal with the current problem? Also, what are AMD's plans? When can it be completely resolved? Can someone tell me?

### Operating System

ubuntu 24.04

### CPU

AI MAX+395

### GPU

AI MAX+395

### ROCm Version

ROCM6.4 and ROCM7 dev

### ROCm Component

_No response_

### Steps to Reproduce

ALL AI app

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_