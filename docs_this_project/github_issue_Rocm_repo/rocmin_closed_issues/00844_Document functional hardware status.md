# Document functional hardware status

- **Issue #:** 844
- **State:** closed
- **Created:** 2019-07-13T13:26:58Z
- **Updated:** 2024-01-11T04:42:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/844

The section "Hardware Support" of ROCm's README lists the status of various GPUs:

https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#hardware-support
https://rocm.github.io/hardware.html

* The documentation lists some GFX7 GPUs as working, while not being supported.
* The documentation states that GFX8 GPUs are supported, while they do not actually work.[1]
* The documentation lists GFX9 GPUs that are supported, but does not make a statement about whether or not they actually work.

1: ROCm 2.0 broke TF-ROCm: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479

There should be a clear statement on whether or not which GPUs work with ROCm. This statement should be reevaluated and updated with at least each minor (1.9, 2.0, 2.1 ...) release.

A more thorough solution would be to add the actual build status to the documentation as badges, like TensorFlow does:

https://github.com/tensorflow/tensorflow#continuous-build-status

However, there are not even resources to add GFX8 gpus to CI in the first place:

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479#issuecomment-500099977