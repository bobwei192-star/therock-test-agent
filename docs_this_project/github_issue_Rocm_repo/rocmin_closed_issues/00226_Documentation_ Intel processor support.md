# Documentation: Intel processor support

- **Issue #:** 226
- **State:** closed
- **Created:** 2017-10-14T22:42:27Z
- **Updated:** 2020-09-13T16:28:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/226

At the moment the readme states:

> Intel Core i7 v3, Core i5 v3, Core i3 v3 or newer CPUs (i.e. Haswell family or newer).

However, if I'm interpreting "v3" correctly (Intel Core i* 3***), that's Ivy Bridge, not Haswell, which is 4***. So is Ivy Bridge supported? Or is it in theory supportable but not tested? Because Ivy Bridge does have PCIe 3.0 support (see Intel Ark). I'm not sure about the atomics in particular, but I'd assume that it's part of the 3.0 spec.

Is the experimental way of figuring out whether atomics is supported by using `lspci -vvvv` and looking for `AtomicOpsCap` in the root ports and the GPU? In my case the root port does say `AtomicOpsCap: 32bit- 64bit- 128bitCAS-`, which seems to suggest that atomics are not supported (and same on the GPU, but it's not a supported Radeon card, so that's expected).