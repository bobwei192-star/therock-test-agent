# How can I allocate different AMD gpu device to different process?

- **Issue #:** 841
- **State:** closed
- **Created:** 2019-07-11T06:34:03Z
- **Updated:** 2022-11-05T13:26:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/841

Suppose, on the machine, there are 2 AMD gpu devices. How can I make process 1 use device0, process2 use device1?  Is there an environment variable like "CUDA_VISIABLE_DEVICES" to set visible AMD GPU devices for processes?

Dy default, are AMD GPU devices shared by all processes?