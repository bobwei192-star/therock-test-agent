# qcm fence wait loop timeout expired after kernel execution; PCIe atomics issue?

- **Issue #:** 407
- **State:** closed
- **Created:** 2018-05-08T20:25:26Z
- **Updated:** 2018-05-12T13:01:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/407

I'm currently using a system with
i7 4790K
MSI Z97 Krait
Vega FE in PCI_E_2 (x16 slot--manual lists PCI_E_2 and PCI_E_5 as x16, PCI-E Gen 3 selected in UEFI/BIOS)

On rocm 1.7, Ubuntu 16.04.4, 4.4.0-119, I notice that certain kernels   repeatably produce
```
qcm fence wait loop timeout expired
Unmapping queues failed.
The cp might be in an unrecoverable state due to an unsuccessful queues preemption
qcm fence wait loop timeout expired
Unmapping queues failed.
```
at which point other, previously working kernels will also fail. Only after a reboot do other kernels starting working again.

This message is also preceded with
```
amdgpu 0000:03:00.0: VM_L2_PROTECTION_FAULT_STATUS
```
although there other kernels that produce this message do not leave the system in an unrecoverable state.

Is this a PCIe atomics issue? (e.g., in #46) It appears that out of thousands of different kernels only a few will trigger this behavior; the majority do not leave the system in an unrecoverable state.
