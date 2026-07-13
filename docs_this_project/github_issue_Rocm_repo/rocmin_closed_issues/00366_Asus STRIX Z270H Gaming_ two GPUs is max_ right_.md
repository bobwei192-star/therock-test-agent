# Asus STRIX Z270H Gaming, two GPUs is max, right?

- **Issue #:** 366
- **State:** closed
- **Created:** 2018-03-18T21:01:06Z
- **Updated:** 2018-05-12T13:12:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/366

Hi, just to confirm I got it right.
My Asus STRIX Z270H Gaming (consumer) motherboard has following PCIe slots:
one PCIe x16
one PCIe x8
one PCIe x2
three  PCIe x1

From this 6 PCIe slots, only the first two can be used by ROCm/atomics because the other four are less than x8, right? 
There is no "amd_iommu=on iommu=pt" GRUB kernel command line options that can enable any of the other PCIe slots so that more than two GPUs can be used, right?