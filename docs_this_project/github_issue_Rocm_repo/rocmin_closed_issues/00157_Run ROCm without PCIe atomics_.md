# Run ROCm without PCIe atomics?

- **Issue #:** 157
- **State:** closed
- **Created:** 2017-07-08T12:03:20Z
- **Updated:** 2023-06-25T00:10:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/157

Hi I am having trouble using ROCm 1.6
My system is
E5-2670v1 + two RX480
CPU itself is using PCIe 3.0, but no PCIe atomics support

I can see two RX480, If I use "rocm-smi -a"
But If I run vector_copy I got "Getting a gpu agent failed."
This is output of "dmesg | grep kfd"
kfd kfd: skipped device 1002:67df, PCI rejects atomics

Is there any solution to run ROCm without PCIe atomics?

Thank you