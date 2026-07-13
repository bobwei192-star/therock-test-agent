# Clarification regarding PCI-Express requirements

- **Issue #:** 594
- **State:** closed
- **Created:** 2018-10-29T16:21:40Z
- **Updated:** 2018-11-06T17:43:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/594

I have multi-GPU setup, one NVidia GTX 960 and another [AMD RX 560 Baffin 16CU/1024 cores](https://www.msi.com/Graphics-card/Radeon-RX-560-AERO-ITX-4G-OC/Specification).

Due to size restrictions I can plug GTX 960 only to PCIEX16 slot and RX 560 to PCIEX4 slot

MB is GA-B150M-D3H-DDR3  [All of the PCI Express slots conform to PCI Express 3.0 standard](https://www.gigabyte.com/Motherboard/GA-B150M-D3H-DDR3-rev-10#sp) and according to the documentation PCI Express 3.0 should be enough 

In such a configuration ROCM driver complains on atomics on PCIEX4 slot - not allowing to run neither OpenCL nor HIP - dmesg reports `PCI rejects atomics`

Notes:

1. ROCM driver works when the RX 560 installed in PCIEX16 slot but for this purpose I need to remove GTX 960 card.
2. When AMDGPU-PRO drivers where installed AMD RX 560 worked on PCIX4 slot - but it does not support hip (and so hipCaffe/tensorflow-hip)

Questions:

1. why atomics are not supported it should be PCI Express 3 connection?
2. Is it possible to enable RX 960 on second PCIEX4 slot without atomics

Setup:

1. Using ROCM 1.9.2 from official repositories
2. Running Ubuntu 16.04, Kernel 4.15