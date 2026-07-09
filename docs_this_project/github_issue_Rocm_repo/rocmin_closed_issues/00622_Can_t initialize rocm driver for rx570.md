# Can't initialize rocm driver for rx570

- **Issue #:** 622
- **State:** closed
- **Created:** 2018-11-25T11:35:29Z
- **Updated:** 2019-01-02T22:54:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/622

I am currently running such a setup:
MB - Msi z270 A pro
CPU - intel core i3-7100
GPU - AMD Rx 570, installed in second x16 pcie 3.0 slot
RAM - 8gb ddr4
Kernel - 4.10.17
OS - Ubuntu 16.04

Before i had amdgpu-pro drivers installed, but now i want to use tensorflow with my amd gpu. So i uninstalled amdgpu-pro, installed rocm, but when i try running python tensorflow script, i get an error:
`2018-11-25 13:14:06.572026: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
terminate called after throwing an instance of 'ihipException'
  what():  std::exception`

Command `dmesg | grep 'kfd'` gives this output:
`[   17.588141] kfd kfd: Initialized module
[   17.642852] kfd kfd: skipped device 1002:67df, PCI rejects atomics`

Overall, something seems to be wrong with PCIe atomics support in my setup, but all components seem to be compatible. Thanks.