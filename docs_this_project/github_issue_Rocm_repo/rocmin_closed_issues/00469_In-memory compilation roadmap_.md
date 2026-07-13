# In-memory compilation roadmap?

- **Issue #:** 469
- **State:** closed
- **Created:** 2018-07-26T08:11:04Z
- **Updated:** 2023-12-08T18:17:30Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/469

I'm currently using the old catalyst and waiting for a few OpenCL things to land in the new drivers.

One of those is in-memory compilation. My programs simply have to generate and compile kernels during the runtime so I don't have a way around it.

Is there any rough estimate on when I could expect any of the new OpenCL implementations (I admit that I am confused by different amd libraries by now: ROCm, AMDGPU(PRO) etc. when it comes to OpenCL) to have support for in-memory compilation on newer hardware (VEGA 64 in my case)?

For the time being, I do net even insist on open-source. Any way to use this functionality would be acceptable.