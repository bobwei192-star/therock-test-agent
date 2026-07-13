# ROCm on IBM Power8: PCIe atomics?

- **Issue #:** 800
- **State:** closed
- **Created:** 2019-05-18T16:53:09Z
- **Updated:** 2024-01-19T04:16:06Z
- **URL:** https://github.com/ROCm/ROCm/issues/800

Hi,

I'm aware that Power8 is not officially supported for ROCm 2.4, but it seems to have been supported previously (mentioned in issue #157 and [here](https://www.anandtech.com/show/10831/amd-sc16-rocm-13-released-boltzmann-realized)), so I wanted to give it a try and see if I could get current ROCm working with my system (Tyan TN71-BP012 with Power8 CPU, Radeon Pro WX2100, Ubuntu 19.04).

I got to the point where I managed to get `rock-dkms` compile (with a couple of minor changes), but `amdkfd` prints the infamous error `kfd: skipped device [...], PCI rejects atomics`.  The GPU is in a PCIe slot directly attached to the CPU, without switches in between.

This [stackoverflow](https://stackoverflow.com/a/44509852) post indicates that Power8 doesn't implement atomics.

This make me wonder, if Power8 really doesn't support atomics as a hardware limitation, how come that it supposedly worked previously? Is there some magic kernel/driver parameter that needs to be used? Or was there perhaps a special codepath for Power8, possibly using CAPI instead of regular PCIe atomics? Is there anything I can do to get it working?