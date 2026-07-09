# [Documentation] hipExtMallocWithFlags coherence mixup

- **Issue #:** 2753
- **State:** closed
- **Created:** 2023-12-19T18:14:46Z
- **Updated:** 2024-01-18T16:32:02Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/2753

https://rocm.docs.amd.com/en/latest/conceptual/gpu-memory.html#coherence

There appear to be a number of typos in this section.

The hipHostMallocDefault flag should be hipDeviceMallocDefault and have coarse-grained coherence.
The coherence for hipDeviceMallocFinegrained should be fine-grained.
