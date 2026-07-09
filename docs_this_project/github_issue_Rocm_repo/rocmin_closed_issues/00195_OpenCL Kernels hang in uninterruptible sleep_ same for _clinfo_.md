# OpenCL Kernels hang in uninterruptible sleep, same for 'clinfo'

- **Issue #:** 195
- **State:** closed
- **Created:** 2017-09-04T13:21:33Z
- **Updated:** 2018-06-03T14:48:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/195

Executing OpenCL kernels (generated with LLVM's AMDGPU backend, exactly according to documentation) leads to the program waiting in uninterruptible sleep forever.
So far I have been able to observe that it usually works 2-3 times, but after that, the hanging starts to appear. `clinfo` always works, but after the hanging appears, `clinfo` starts to hang in uninterruptible sleep too.
With `ps -eo comm,wchan:32` I have been able to identify:
  - `clinfo` hangs at call `amd_sched_entity_fini`
  - the first executable that hangs, stops at call `kfd_process_notifier_release`
  - all programs after that halt at `kfd_create_process`

The GPU used is an R9 Nano (Fiji), running the latest ROCm package (clean install) from the repositories (Ubuntu 16.04).