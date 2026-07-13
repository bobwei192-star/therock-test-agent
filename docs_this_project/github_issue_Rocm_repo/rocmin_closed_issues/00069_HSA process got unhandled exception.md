# HSA process got unhandled exception

- **Issue #:** 69
- **State:** closed
- **Created:** 2017-01-04T02:31:59Z
- **Updated:** 2017-07-02T17:17:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/69

I have here a supermicro workstation with 2x R9 Nano and 2x S9150 installed running Ubuntu 16.04. This setup worked well with amdgpu-pro 16.40 previously.

I removed amdgpu-pro and installed ROCm 1.4 following instructions. However, the basic HSA sample (vector_copy) segfaults in libhsa-runtime64. dmesg shows a GPU fault detected, VM_CONTEXT1_PROTECTION_FAULT and VM fault.

Running any (previously working) OpenCL code or even just running clinfo causes "kfd: HSA Process (PID $$$$) got unhandled exception". After this, the executable hangs and after killing it dmesg contains kfd: cp queue preemption time out and amdkfd: Resetting wave fronts on dev.

What do I need to do to get this setup to work?