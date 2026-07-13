# Is there any chance of supporting Piledriver+Polaris combination on a PCIe 2.0?

- **Issue #:** 1086
- **State:** closed
- **Created:** 2020-04-21T18:49:35Z
- **Updated:** 2020-12-01T17:55:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/1086

Currently Polaris GPUs such as AMD RX 580 and 590 do not work with ROCm when paired with AMD FX processors such as FX 8300, the kfd module shows an error regarding atomics.

> kfd: skipped device 1002:67df, PCI rejects atomics.

I know it is not stated in the documentation that this combo is supported, but will it be supported in the future on a PCIe 2.0?