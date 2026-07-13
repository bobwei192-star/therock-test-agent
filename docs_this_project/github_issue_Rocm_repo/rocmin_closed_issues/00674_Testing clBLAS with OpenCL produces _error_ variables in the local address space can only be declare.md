# Testing clBLAS with OpenCL produces "error: variables in the local address space can only be declared in the outermost scope of a kernel function"

- **Issue #:** 674
- **State:** closed
- **Created:** 2019-01-16T19:27:14Z
- **Updated:** 2019-01-17T08:57:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/674

1. I've install ROCm on Centos 7.6 where the rocminfo and clinfo execute normally.
2. I've build clBLAS with OpenCL 2.0 and then started test_short which fails with
error: variables in the local address space can only be declared in the outermost scope of a kernel function
        __local float4 ascratch[4*16*4];

And if you check the kernel you will see that ascratch is defined almost at the end of the function.,

Now I have no knowledge on who generates the kernel and how, but I assume that you know and can fix this.

Best regards
Waldemar

[test_short.txt](https://github.com/RadeonOpenCompute/ROCm/files/2765736/test_short.txt)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2765737/clinfo.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2765738/rocminfo.txt)


