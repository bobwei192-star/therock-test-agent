# What is the functionality of si58_mc.bin

- **Issue #:** 179
- **State:** closed
- **Created:** 2017-08-10T08:50:22Z
- **Updated:** 2018-06-03T14:56:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/179

With Git hub pre-build OCL bins , Luxmark  works with out si58_mc.bin from /lib/amdgpu/firmware.

I tried to build libOenCL.so and libamdocl64.so  from  open source.  But Luxmark failed to run and gave IOMMU fault. When i copy si58_mc.bin to amdgpu firmware and ran initramfs , Luxmark runs without any issue.

Can you explain how this firmware bin fixing the issue?

