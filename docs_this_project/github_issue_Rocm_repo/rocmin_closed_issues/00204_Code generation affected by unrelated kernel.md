# Code generation affected by unrelated kernel

- **Issue #:** 204
- **State:** closed
- **Created:** 2017-09-13T01:33:46Z
- **Updated:** 2019-03-12T19:09:11Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/204

The exact source that displays the problem can be found here:
https://github.com/preda/gpuowl/blob/master/gpuowl.cl#L338

On AMDGPU-pro 17.30, RX Vega 64, on Linux:

I have two OpenCL kernels, that invoke the same function with different arguments:
```
void carryConvolution(....) { /* skipped */ }

kernel void carryConv1K_2K(uint baseBitlen, [etc]) {
  local double lds[4 * 256];
  double2 u[4];
  carryConvolution(4, 2048, lds, u, baseBitlen, etc);
}

#ifdef ENABLE_BUG
kernel void  carryConv2K_2K(uint baseBitlen, [etc]) {
  local double lds[8 * 256];
  double2 u[8];
  carryConvolution(8, 2048, lds, u, baseBitlen, etc);
}
#endif
```
The ISA code generated for the first kernel depends on whether the second kernel (the #ifdef one) exists or not. The difference in code and perf is major, see these stats for the first kernel:

1. When the second kernel is not present:
```
		workitem_private_segment_byte_size = 0
		workgroup_group_segment_byte_size = 8192
		kernarg_segment_byte_size = 88
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 20
		workitem_vgpr_count = 83
```
2. When the second kernel is present (but not used):
```
		workitem_private_segment_byte_size = 80
		workgroup_group_segment_byte_size = 8192
		kernarg_segment_byte_size = 88
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 28
		workitem_vgpr_count = 87
```

Both variants seems to function correctly (aside from performance).