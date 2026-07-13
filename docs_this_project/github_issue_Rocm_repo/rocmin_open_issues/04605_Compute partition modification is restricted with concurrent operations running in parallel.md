# Compute partition modification is restricted with concurrent operations running in parallel

- **Issue #:** 4605
- **State:** open
- **Created:** 2025-04-11T23:11:32Z
- **Updated:** 2025-04-11T23:41:20Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4605

Modification to compute partition in GPU is prohibited by design while concurrent operations run in parallel. You must ensure no concurrent operations on the device are running when attempting to modify the compute partitions. Additional checks and error messaging to inform users of correct operation for partition modification are planned for future ROCm releases.