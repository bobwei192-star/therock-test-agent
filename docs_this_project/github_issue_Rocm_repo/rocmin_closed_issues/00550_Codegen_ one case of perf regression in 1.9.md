# Codegen: one case of perf regression in 1.9 

- **Issue #:** 550
- **State:** closed
- **Created:** 2018-09-19T02:36:49Z
- **Updated:** 2020-12-16T12:22:38Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/550

In GpuOwl https://github.com/preda/gpuowl I see a perf regression after moving to 1.9 from 1.8.2. I think the bulk of it comes from the miscompilation of one kernel "mulFused" that I paste below for comparison.
[mulFused-1.8.2.txt](https://github.com/RadeonOpenCompute/ROCm/files/2395206/mulFused-1.8.2.txt)
[mulFused-1.9.txt](https://github.com/RadeonOpenCompute/ROCm/files/2395207/mulFused-1.9.txt)

In 1.8.2:
		workitem_private_segment_byte_size = 0
		workgroup_group_segment_byte_size = 4096
		gds_segment_byte_size = 0
		kernarg_segment_byte_size = 56
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 28
		workitem_vgpr_count = 216

In 1.9:
		workitem_private_segment_byte_size = 380
		workgroup_group_segment_byte_size = 4096
		gds_segment_byte_size = 0
		kernarg_segment_byte_size = 72
		workgroup_fbarrier_count = 0
		wavefront_sgpr_count = 27
		workitem_vgpr_count = 256

As you see, there is an issue with the VGPRs allocation. 1.9 causes spilling, while 1.8.2 did not.

On a related note, how may I install ROCm 1.8.2 or 1.8.3, not that it's not the most recent version anymore?
thanks!

(for repro in GpuOwl, please do: echo "88593847" > worktodo.txt )