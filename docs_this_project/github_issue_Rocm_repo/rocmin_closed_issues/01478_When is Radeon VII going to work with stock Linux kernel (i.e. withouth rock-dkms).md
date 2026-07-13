# When is Radeon VII going to work with stock Linux kernel (i.e. withouth rock-dkms)

- **Issue #:** 1478
- **State:** closed
- **Created:** 2021-05-20T19:12:52Z
- **Updated:** 2021-05-31T05:31:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1478

On ROCm 3.x, Radeon VII is working fine with a variety of stock Linux kernels, such as: 5.10, 5.11, 5.12. That means that Radeon VII can be used without installing rock-dkms.

Starting with ROCm 4.1, Radeon VII does not work anymore with *any* stock Linux kernel, and requires the installation of rocm-dkms. This fact is noted in the release notes: https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html#driver-compability-issue-in-rocm-v4-1

I would like to know when Radeon VII can be used again without rock-dkms (as was possible with ROCm 3.x). And which stock Linux kernel version will be required for that (maybe the upcoming 5.13?)
