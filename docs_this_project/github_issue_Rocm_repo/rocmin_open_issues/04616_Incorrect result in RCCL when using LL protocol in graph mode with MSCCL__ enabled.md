# Incorrect result in RCCL when using LL protocol in graph mode with MSCCL++ enabled

- **Issue #:** 4616
- **State:** open
- **Created:** 2025-04-11T23:21:30Z
- **Updated:** 2025-04-11T23:21:30Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4616

In RCCL library, you might receive incorrect results in All-Reduce collective API, when using Link Layer (LL) protocol in graph mode while MSCCL++ is enabled. This issue occurs when the protocal state information are updated in the host-side code instead of in a kernel, which is not supported in graph mode. As a workaround, you can disable MSCCL++ by setting the environment variable `RCCL_MSCCLPP_ENABLE=0`. However, consider that this might negatively impact the performance. The issue will be fixed in a future ROCm release.