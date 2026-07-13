# Which Intel and AMD chipsets support pcie atomics?

- **Issue #:** 237
- **State:** closed
- **Created:** 2017-10-26T21:57:37Z
- **Updated:** 2018-06-03T15:14:33Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/237

Is there any information about pcie atomics support in Intel and AMD chipsets?
I have Intel B250 based motherboard with 2 pcie 3.0 slots.
But only 1 Vega card is usable for rocm.
One pcie slot is OK, but second is routed via chipset and rejects atomics. 

In dmesg:
[    6.087732] kfd kfd: added device 1002:687f
[    8.190144] kfd kfd: skipped device 1002:687f, PCI rejects atomics

I need to search for motherboard with all pcie slots connected to CPU or there are known chipsets with atomics support?
Have you information about atomics support in Intel Z270, H270, X299, AMD X370?