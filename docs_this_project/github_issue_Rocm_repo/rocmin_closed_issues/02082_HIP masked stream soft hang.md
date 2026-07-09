# HIP masked stream soft hang

- **Issue #:** 2082
- **State:** closed
- **Created:** 2023-04-25T02:49:50Z
- **Updated:** 2023-04-27T08:45:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/2082

In the [change log](https://github.com/RadeonOpenCompute/ROCm/blob/develop/CHANGELOG.md#softhang-with-hipstreamwithcumask-test-on-amd-instinct) I notice that configuring the stream CU mask incorrectly will cause soft hangs in HIP. I'm using 6900xt (`gfx1030`) right now. IIUSC, it composes 4 SEs, then each SE has 2 SAs (shader array) and each SA has 5 CUs, thus totally 40 CUs (returned by the device property `prop.multiProcessorCount`).

The change log says two CUs making up one WGP must be activated at the same time, so I'm wondering now how can I tell whether two CUs belong to one WGP? How this reveals in its 40bit-wide CU masking array?