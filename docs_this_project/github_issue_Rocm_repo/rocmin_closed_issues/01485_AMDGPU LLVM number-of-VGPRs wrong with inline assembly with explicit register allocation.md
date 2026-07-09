# AMDGPU LLVM number-of-VGPRs wrong with inline assembly with explicit register allocation

- **Issue #:** 1485
- **State:** closed
- **Created:** 2021-05-30T18:18:00Z
- **Updated:** 2021-12-16T03:39:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1485

Using ROCm 3.3.0, Ubuntu 20.04, Linux kernel 5.12.7, GPU Radeon VII, OpenCL.

This seems to be an LLVM/AMDGPU bug, that I'm reporting here because I don't know a better location (please let me know if there's a better place to report such issues).

It seems the counting of #VGPRs used is wrong when using inline assembly with explicit VGPR allocation, as in the example below:
```
uint foo(uint x) {
  unsigned long long out;
  __asm("v_mad_u64_u32 v[6:7], vcc, %1, %1, 0" : "={v[6:9]}"(out) : "v"(x));
  return out;
}

kernel void testKernel(global uint* io) {
  uint me = get_local_id(0);

  io[me] = foo(io[me]) + ((ulong) (io[me])) * io[me + 1];
}
```
Generates the ISA below. As you can see in the ISA, the .amdhsa_next_free_vgpr is 11, in agreement with NumVGPRsForWavesPerEU: 11, yet this value is wrong as the actual number of VGPRs used is 10. The error seems to be an off-by-one (extra by one). (the actual number of VGPRs is 10 according to the __asm explicit allocation "={v[6:9]}" which pushes the upper VGPR bound).

```
	.text
	.protected	testKernel      ; -- Begin function testKernel
	.globl	testKernel
	.p2align	8
	.type	testKernel,@function
testKernel:                             ; @testKernel
testKernel$local:
; %bb.0:
	s_load_dwordx2 s[0:1], s[4:5], 0x0
	v_lshlrev_b32_e32 v0, 2, v0
	s_waitcnt lgkmcnt(0)
	v_mov_b32_e32 v1, s1
	v_add_co_u32_e32 v0, vcc, s0, v0
	v_addc_co_u32_e32 v1, vcc, 0, v1, vcc
	global_load_dwordx2 v[2:3], v[0:1], off
	s_waitcnt vmcnt(0)
	;;#ASMSTART
	v_mad_u64_u32 v[6:7], vcc, v2, v2, 0
	;;#ASMEND
	v_mul_lo_u32 v3, v3, v2
	v_add_u32_e32 v2, v3, v6
	global_store_dword v[0:1], v2, off
	s_endpgm
	.section	.rodata,#alloc
	.p2align	6
	.amdhsa_kernel testKernel
		.amdhsa_group_segment_fixed_size 0
		.amdhsa_private_segment_fixed_size 0
		.amdhsa_user_sgpr_private_segment_buffer 1
		.amdhsa_user_sgpr_dispatch_ptr 0
		.amdhsa_user_sgpr_queue_ptr 0
		.amdhsa_user_sgpr_kernarg_segment_ptr 1
		.amdhsa_user_sgpr_dispatch_id 0
		.amdhsa_user_sgpr_flat_scratch_init 0
		.amdhsa_user_sgpr_private_segment_size 0
		.amdhsa_system_sgpr_private_segment_wavefront_offset 0
		.amdhsa_system_sgpr_workgroup_id_x 1
		.amdhsa_system_sgpr_workgroup_id_y 0
		.amdhsa_system_sgpr_workgroup_id_z 0
		.amdhsa_system_sgpr_workgroup_info 0
		.amdhsa_system_vgpr_workitem_id 0
		.amdhsa_next_free_vgpr 11
		.amdhsa_next_free_sgpr 6
		.amdhsa_reserve_flat_scratch 0
		.amdhsa_float_round_mode_32 0
		.amdhsa_float_round_mode_16_64 0
		.amdhsa_float_denorm_mode_32 3
		.amdhsa_float_denorm_mode_16_64 3
		.amdhsa_dx10_clamp 1
		.amdhsa_ieee_mode 1
		.amdhsa_fp16_overflow 0
		.amdhsa_exception_fp_ieee_invalid_op 0
		.amdhsa_exception_fp_denorm_src 0
		.amdhsa_exception_fp_ieee_div_zero 0
		.amdhsa_exception_fp_ieee_overflow 0
		.amdhsa_exception_fp_ieee_underflow 0
		.amdhsa_exception_fp_ieee_inexact 0
		.amdhsa_exception_int_div_zero 0
	.end_amdhsa_kernel
	.text
.Lfunc_end8:
	.size	testKernel, .Lfunc_end8-testKernel
                                        ; -- End function
	.section	.AMDGPU.csdata
; Kernel info:
; codeLenInByte = 72
; NumSgprs: 8
; NumVgprs: 11
; ScratchSize: 0
; MemoryBound: 0
; FloatMode: 240
; IeeeMode: 1
; LDSByteSize: 0 bytes/workgroup (compile time only)
; SGPRBlocks: 0
; VGPRBlocks: 2
; NumSGPRsForWavesPerEU: 8
; NumVGPRsForWavesPerEU: 11
; Occupancy: 10
; WaveLimiterHint : 1
; COMPUTE_PGM_RSRC2:USER_SGPR: 6
; COMPUTE_PGM_RSRC2:TRAP_HANDLER: 0
; COMPUTE_PGM_RSRC2:TGID_X_EN: 1
; COMPUTE_PGM_RSRC2:TGID_Y_EN: 0
; COMPUTE_PGM_RSRC2:TGID_Z_EN: 0
; COMPUTE_PGM_RSRC2:TIDIG_COMP_CNT: 0
	.ident	"clang version 11.0.0 (/data/jenkins-workspace/compute-rocm-rel-3.3/external/llvm-project/clang 54cdcbb04e8b53c512e7868d4bb7b8347c6136b5)"
	.section	".note.GNU-stack"
	.addrsig
	.amdgpu_metadata
```