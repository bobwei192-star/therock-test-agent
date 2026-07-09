# Will ROCm 2.2 support PCI 3 x8 slot ?

- **Issue #:** 742
- **State:** closed
- **Created:** 2019-03-18T19:12:23Z
- **Updated:** 2019-03-18T19:58:16Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/742

I have two cards on my system, one on x16 slot and one on x8 slot.

Only the x16 card has been detected by ROCm for OpenCL, although
`rocm-smi` sees both cards. 

Why can `rocm-smi` see both cards, but `clinfo` only detects one ?

And will both cards be usable for OpenCL in the future ?

