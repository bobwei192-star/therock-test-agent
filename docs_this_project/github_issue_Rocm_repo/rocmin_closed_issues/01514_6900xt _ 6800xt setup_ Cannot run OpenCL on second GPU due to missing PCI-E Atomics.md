# 6900xt + 6800xt setup: Cannot run OpenCL on second GPU due to missing PCI-E Atomics

- **Issue #:** 1514
- **State:** closed
- **Created:** 2021-07-08T11:11:07Z
- **Updated:** 2021-07-09T12:02:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/1514

I am using ROCm to run OpenCL code on two 6xxx series GPUs. However, it is only running on the first GPU that's connected directly to the CPU PCI-E lanes (B550 motherboard). The second PCI-E slot is using PCI-E lanes from the chipset instead, and PCI atomics are not supported there. Dmesg confirms the issue:

`"skipped device XXX, PCI rejects atomics",`

Interestingly, I installed Windows 10 on a spare SSD and I can run OpenCL code on both devices just fine. I know I can simply dual boot, but I mainly use Linux myself. Having to reboot to Windows every single time I want to crunch OpenCL code is NOT a real solution. However, the fact it works flawlessly under Windows show that it is not a technical limitation. It should therefor be possible to get it in a working state under Linux as well.