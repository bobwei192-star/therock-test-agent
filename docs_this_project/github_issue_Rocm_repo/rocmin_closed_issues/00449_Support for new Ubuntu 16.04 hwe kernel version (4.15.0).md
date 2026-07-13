# Support for new Ubuntu 16.04 hwe kernel version (4.15.0)

- **Issue #:** 449
- **State:** closed
- **Created:** 2018-07-02T15:29:20Z
- **Updated:** 2018-07-20T16:14:28Z
- **Assignees:** jedwards-AMD
- **URL:** https://github.com/ROCm/ROCm/issues/449

Ubuntu 16.04 was updated today to the 4.15 kernel from 18.04, but there were no updates from rocm-dkms so naturally it failed to build for the new kernel version.

> Processing triggers for linux-image-4.15.0-24-generic (4.15.0-24.26~16.04.1) ...
> /etc/kernel/postinst.d/dkms:
> ERROR (dkms apport): kernel package linux-headers-4.15.0-24-generic is not supported
> Error! Bad return status for module build on kernel: 4.15.0-24-generic (x86_64)
> Consult /var/lib/dkms/amdgpu/1.8-151/build/make.log for more information.

[make.log](https://github.com/RadeonOpenCompute/ROCm/files/2155780/make.log)

I realize that this new kernel release is ahead of the proposed schedule (says Aug. 2018) as can be seen [here](https://wiki.ubuntu.com/Kernel/LTSEnablementStack#Kernel.2FSupport.A16.04.x_Ubuntu_Kernel_Support), but will we seen an update to ROCm soon?