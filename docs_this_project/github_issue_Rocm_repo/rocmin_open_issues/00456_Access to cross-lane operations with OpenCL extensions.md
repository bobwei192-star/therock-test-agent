# Access to cross-lane operations with OpenCL extensions

- **Issue #:** 456
- **State:** open
- **Created:** 2018-07-12T00:27:25Z
- **Updated:** 2026-02-24T17:07:15Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/456

Hi,

Intel has a very useful extension:
cl_intel_subgroups

Which enables inside a subgroup (a wavefront) to shuffle items, do reduce operations, etc.

According to https://gpuopen.com/amd-gcn-assembly-cross-lane-operations/
Recent AMD hardware can do the same, and even better.

I know this functionnality is available via HSA or inline assembly, but there is no OpenCL extension supported by AMD for that. Assembly is not a good solution for an OpenCL developper, as the assembly might need to be updated for new cards or for bug workarounds. Please make it an extension !

Features I'd like to have: shuffle, fine grained reduction operations. For example reduction among work items 0, 8, 16, etc, and 1, 9, 17, etc you get the idea, or reduction among 0-7, 8-15, etc. This type of fine grained reduction would be very useful. Going through LDS is possible, but for a reduction operation, you need several lds reads, and using the cross lane operations would be much faster.