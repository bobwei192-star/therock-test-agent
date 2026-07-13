# Significant random differences in generated code.

- **Issue #:** 241
- **State:** closed
- **Created:** 2017-10-29T09:44:02Z
- **Updated:** 2018-02-13T19:19:08Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/241

ROCm 1.6-180, Ubuntu 16.04, R9-Nano.

Compiling the exact same OpenCL source in identical conditions, produces two significantly different outputs. The two outputs seem to alternate in a random manner. I attach the two ISA files for comparison. Note, they are output from exactly identical input/args. (!)

The outputs were compiled from GpuOwl  at commit 28c127f.

Note, the two variants have different performance. The differences are not 'neutral'. E.g.
```
3953c3953
<               workitem_private_segment_byte_size = 100
---
>               workitem_private_segment_byte_size = 220
```

[DP_4M_0_fiji-A.txt](https://github.com/RadeonOpenCompute/ROCm/files/1424909/DP_4M_0_fiji-A.txt)
[DP_4M_0_fiji-B.txt](https://github.com/RadeonOpenCompute/ROCm/files/1424910/DP_4M_0_fiji-B.txt)
