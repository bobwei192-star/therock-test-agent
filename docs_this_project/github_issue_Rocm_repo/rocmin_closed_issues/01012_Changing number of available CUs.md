# Changing number of available CUs

- **Issue #:** 1012
- **State:** closed
- **Created:** 2020-02-13T01:28:23Z
- **Updated:** 2024-08-01T14:31:38Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/1012

I'm studying scaling of a variety of compute workloads, and I was wondering if there is a way to adjust the number of CUs?

I came across a [similar discussion](https://github.com/RadeonOpenCompute/ROC-smi/issues/5) where use of "hsa_amd_queue_cu_set_mask()" was suggested. Since this requires changing the applications source code, are there any other alternative approaches that can achieve the same without modifying the source code?