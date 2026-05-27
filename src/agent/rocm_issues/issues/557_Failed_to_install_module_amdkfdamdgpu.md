# Failed to install module amdkfdamdgpu

> **Issue #557**
> **状态**: closed
> **创建时间**: 2018-09-24T22:05:41Z
> **更新时间**: 2018-09-25T19:32:31Z
> **关闭时间**: 2018-09-25T19:32:31Z
> **作者**: le-mikcho
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/557

## 描述

Is anyone else getting the following error when installing rocm-dkms via yum (Version : 1.9.211)on Centos 7.5 ?
Failed to install module amdkfdamdgpu

---

## 评论 (5 条)

### 评论 #1 — kentrussell (2018-09-25T11:14:56Z)

Is there anything in the dkms log to help indicate why the failure occurred? 

---

### 评论 #2 — le-mikcho (2018-09-25T17:52:56Z)

Im no expert but logs ok to me...

```
DKMS make.log for amdgpu-1.9-211.el7 for kernel 3.10.0-862.11.6.el7.x86_64 (x86_64)
Mon Sep 24 23:52:58 CEST 2018
make: Entering directory /usr/src/kernels/3.10.0-862.11.6.el7.x86_64'
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/built-in.o
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/built-in.o
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/lib/built-in.o
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_drm.o
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/scheduler/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/lib/chash.o
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/scheduler/gpu_scheduler.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_module.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_memory.o
  LD      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/built-in.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_device.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/lib/amdchash.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_chardev.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_topology.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_pasid.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_doorbell.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_drm_global.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_flat_memory.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_process.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_pci.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_queue.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/kcl_prime.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_mqd_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_mqd_manager_cik.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_mqd_manager_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_mqd_manager_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_kernel_queue.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_kernel_queue_cik.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_object.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_lock.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_kernel_queue_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_kernel_queue_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_packet_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_process_queue_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_device_queue_manager.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_device_queue_manager_cik.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_device_queue_manager_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_device_queue_manager_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_test.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_pm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_interrupt.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_events.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/cik_event_interrupt.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_afmt.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_int_process_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_dbgdev.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_dbgmgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_crat.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_prime.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_sa.c: In function ‘amdgpu_sa_bo_du                                                                                              mp_debug_info’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_sa.c:393:6: warning: format ‘%d’ e                                                                                              xpects argument of type ‘int’, but argument 4 has type ‘u64’ [-Wformat=]
      i->fence->seqno, i->fence->context);
      ^
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_rdma.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ib.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_peerdirect.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ucode.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_bo_list.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_ipc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_iommu.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/kfd_debugfs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_vram_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_queue_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_vf_error.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/amdkfd.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_sched.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_debugfs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ids.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_sem.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_amdkfd_fence.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/cik.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/cik_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/kv_smc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/kv_dpm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/ci_smc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/ci_dpm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/dce_v8_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gfx_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/cik_sdma.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/uvd_v4_2.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/cik.o: warning: objtool: cik_set_ip_block                                                                                              s()+0x48: sibling call from callable instruction with changed frame pointer
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vce_v2_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/si.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gfx_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/si_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/si_dma.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/dce_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/si_dpm.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v6_0.c: In function ‘gmc_v6_0_mc_init                                                                                              ’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v6_0.c:281:6: warning: unused variabl                                                                                              e ‘r’ [-Wunused-variable]
  int r;
      ^
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/si_smc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/mxgpu_vi.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/nbio_v6_1.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/soc15.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/emu_soc.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vi.o: warning: objtool: vi_set_ip_blocks(                                                                                              )+0x6f: sibling call from callable instruction with changed frame pointer
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/mxgpu_ai.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/nbio_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vega10_reg_init.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vega20_reg_init.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/df_v1_7.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/df_v3_6.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v8_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gfxhub_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/mmhub_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v9_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_irq.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v7_0.c: In function ‘gmc_v7_0_mc_init                                                                                              ’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v7_0.c:320:6: warning: unused variabl                                                                                              e ‘r’ [-Wunused-variable]
  int r;
      ^
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v8_0.c: In function ‘gmc_v8_0_mc_init                                                                                              ’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v8_0.c:498:6: warning: unused variabl                                                                                              e ‘r’ [-Wunused-variable]
  int r;
      ^
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v9_0.c: In function ‘gmc_v9_0_mc_init                                                                                              ’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gmc_v9_0.c:711:6: warning: unused variabl                                                                                              e ‘r’ [-Wunused-variable]
  int r;
      ^
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/iceland_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/tonga_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/cz_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vega10_ih.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_psp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/psp_v3_1.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/psp_v10_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_dpm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/dce_v10_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/dce_v11_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/dce_virtual.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_gfx.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gfx_v8_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/gfx_v9_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/sdma_v2_4.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/sdma_v3_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/sdma_v4_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_uvd.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/uvd_v5_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/uvd_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/uvd_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_vce.o
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_uvd.c: In function ‘amdgpu_uvd_sw_                                                                                              init’:
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_uvd.c:237:65: warning: ‘version_mi                                                                                              nor’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  adev->uvd.fw_version = ((version_major << 24) | (version_minor << 16) |
                                                                 ^
/var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_uvd.c:237:41: warning: ‘version_ma                                                                                              jor’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  adev->uvd.fw_version = ((version_major << 24) | (version_minor << 16) |
                                         ^
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vce_v3_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vce_v4_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_vcn.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/vcn_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_amdkfd.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_amdkfd_gfx_v7.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_amdkfd_gfx_v8.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_amdkfd_gfx_v9.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_amdkfd_gpuvm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_cgs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_job.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_ioc32.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_atpx_handler.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_acpi.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu_mn.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/smumgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/smu8_smumgr                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/tonga_smumg                                                                                              r.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/fiji_smumgr                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/polaris10_s                                                                                              mumgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/iceland_smu                                                                                              mgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/smu7_smumgr                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/vega10_smum                                                                                              gr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/smu10_smumg                                                                                              r.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/ci_smumgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/vega12_smum                                                                                              gr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/smumgr/vegam_smumg                                                                                              r.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/hwmgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/processpptab                                                                                              les.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/hardwaremana                                                                                              ger.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu8_hwmgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/pppcielanes.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/process_ppta                                                                                              bles_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/ppatomctrl.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/ppatomfwctrl                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu7_hwmgr.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu7_powertu                                                                                              ne.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu7_thermal                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu7_clockpo                                                                                              wergating.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega10_proce                                                                                              sspptables.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega10_hwmgr                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega10_power                                                                                              tune.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega10_therm                                                                                              al.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu10_hwmgr.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/pp_psm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega12_proce                                                                                              sspptables.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega12_hwmgr                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/vega12_therm                                                                                              al.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/pp_overdrive                                                                                              r.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/hwmgr/smu_helper.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../powerplay/amd_powerplay.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm_                                                                                              irq.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm_                                                                                              mst_types.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm_                                                                                              color.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm_                                                                                              services.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm_                                                                                              helpers.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/amdgpu_dm/amdgpu_dm_                                                                                              crc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/basics/conversion                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/basics/fixpt31_32                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/basics/logger.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/basics/log_helper                                                                                              s.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/basics/vector.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/bios_parser.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/bios_parser_                                                                                              interface.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/bios_parser_                                                                                              helper.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/command_tabl                                                                                              e.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/command_tabl                                                                                              e_helper.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/bios_parser_                                                                                              common.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/command_tabl                                                                                              e2.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/command_tabl                                                                                              e_helper2.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/bios_parser2                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/dce80/comman                                                                                              d_table_helper_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/dce110/comma                                                                                              nd_table_helper_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/dce112/comma                                                                                              nd_table_helper_dce112.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/bios/dce112/comma                                                                                              nd_table_helper2_dce112.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/calcs/dce_calcs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/calcs/bw_fixed.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/calcs/custom_floa                                                                                              t.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/calcs/dcn_calcs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/calcs/dcn_calc_ma                                                                                              th.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/calcs/dcn_calc_au                                                                                              to.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_audio.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_stream_en                                                                                              coder.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_link_enco                                                                                              der.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_hwseq.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_mem_input                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_clock_sou                                                                                              rce.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_scl_filte                                                                                              rs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_transform                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_clocks.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_opp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_dmcu.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_abm.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce/dce_ipp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/gpio_base.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/gpio_service                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/hw_factory.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/hw_gpio.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/hw_hpd.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/hw_ddc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/hw_translate                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dce80/hw_tra                                                                                              nslate_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dce80/hw_fac                                                                                              tory_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dce110/hw_tr                                                                                              anslate_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dce110/hw_fa                                                                                              ctory_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dce120/hw_tr                                                                                              anslate_dce120.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dce120/hw_fa                                                                                              ctory_dce120.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dcn10/hw_tra                                                                                              nslate_dcn10.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/dcn10/hw_fac                                                                                              tory_dcn10.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/diagnostics/                                                                                              hw_translate_diag.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/gpio/diagnostics/                                                                                              hw_factory_diag.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/aux_engine                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/engine_bas                                                                                              e.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/i2caux.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/i2c_engine                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/i2c_generi                                                                                              c_hw_engine.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/i2c_hw_eng                                                                                              ine.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/i2c_sw_eng                                                                                              ine.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce80/i2ca                                                                                              ux_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce80/i2c_                                                                                              hw_engine_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce80/i2c_                                                                                              sw_engine_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce100/i2c                                                                                              aux_dce100.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce110/i2c                                                                                              aux_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce110/i2c                                                                                              _sw_engine_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce110/i2c                                                                                              _hw_engine_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce110/aux                                                                                              _engine_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce112/i2c                                                                                              aux_dce112.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dcn10/i2ca                                                                                              ux_dcn10.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/dce120/i2c                                                                                              aux_dce120.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/i2caux/diagnostic                                                                                              s/i2caux_diag.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/irq/irq_service.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/irq/dce80/irq_ser                                                                                              vice_dce80.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/irq/dce110/irq_se                                                                                              rvice_dce110.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/irq/dce120/irq_se                                                                                              rvice_dce120.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/irq/dcn10/irq_ser                                                                                              vice_dcn10.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/virtual/virtual_l                                                                                              ink_encoder.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/virtual/virtual_s                                                                                              tream_encoder.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_resou                                                                                              rce.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_ipp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_hw_se                                                                                              quencer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_dpp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_opp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_optc.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_hubp.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_mpc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_dpp_d                                                                                              scl.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_dpp_c                                                                                              m.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_cm_co                                                                                              mmon.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_hubbu                                                                                              b.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_strea                                                                                              m_encoder.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dcn10/dcn10_link_                                                                                              encoder.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dml/display_mode_                                                                                              lib.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dml/display_rq_dl                                                                                              g_helpers.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dml/dml1_display_                                                                                              rq_dlg_calc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dml/soc_bounding_                                                                                              box.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dml/dml_common_de                                                                                              fs.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce120/dce120_res                                                                                              ource.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce120/dce120_tim                                                                                              ing_generator.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce120/dce120_hw_                                                                                              sequencer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce112/dce112_com                                                                                              pressor.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce112/dce112_hw_                                                                                              sequencer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce112/dce112_res                                                                                              ource.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_tim                                                                                              ing_generator.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_com                                                                                              pressor.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_hw_                                                                                              sequencer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_res                                                                                              ource.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_opp                                                                                              _regamma_v.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_opp                                                                                              _csc_v.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_tim                                                                                              ing_generator_v.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_mem                                                                                              _input_v.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_opp                                                                                              _v.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce110/dce110_tra                                                                                              nsform_v.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce100/dce100_res                                                                                              ource.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce100/dce100_hw_                                                                                              sequencer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce80/dce80_timin                                                                                              g_generator.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce80/dce80_hw_se                                                                                              quencer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dce80/dce80_resou                                                                                              rce.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_link.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_resource.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_hw_sequen                                                                                              cer.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_sink.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_surface.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_link_hwss                                                                                              .o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_link_dp.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_link_ddc.                                                                                              o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_debug.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/core/dc_stream.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/dc/dc_helper.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/modules/freesync/fre                                                                                              esync.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../display/modules/color/color_                                                                                              gamma.o
  CC [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/../backport/kcl_amdgpu.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu.o
  Building modules, stage 2.
  MODPOST 6 modules
  CC      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu.mod.o
  CC      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/amdkcl.mod.o
  CC      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/amdkfd.mod.o
  CC      /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/lib/amdchash.mod.o
  CC      /var/lib/dkms/amdgpu/1.9-211.el7/build/scheduler/amd-sched.mod.o
  CC      /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/amdttm.mod.o
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkfd/amdkfd.ko
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/ttm/amdttm.ko
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/scheduler/amd-sched.ko
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdkcl/amdkcl.ko
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/lib/amdchash.ko
  LD [M]  /var/lib/dkms/amdgpu/1.9-211.el7/build/amd/amdgpu/amdgpu.ko
make: Leaving directory `/usr/src/kernels/3.10.0-862.11.6.el7.x86_64'
```


---

### 评论 #3 — jlgreathouse (2018-09-25T18:46:27Z)

Could you show the outputs of the following commands on your system?
- `uname -r`
- `dkms status`

What commands have you run to see this error? Could you show the whole output of what happens between when you run the command and when the error appears?

---

### 评论 #4 — le-mikcho (2018-09-25T18:59:06Z)

Sure. 
`# uname -r
3.10.0-862.11.6.el7.x86_64
`
`# dkms status
amdgpu, 1.9-211.el7, 3.10.0-862.11.6.el7.x86_64, x86_64: installed (original_module exists)`

to reproduce all I am doing is yum install rocm-dkms and it appears twice during the installation.

the system log looks like this:

`Sep 25 20:46:28 stacker dracut: Skipping udev rule: 40-redhat-cpu-hotplug.rules
Sep 25 20:46:29 stacker dracut: Skipping udev rule: 91-permissions.rules
Sep 25 20:46:29 stacker dracut: *** Including module: biosdevname ***
Sep 25 20:46:29 stacker dracut: *** Including module: systemd ***
Sep 25 20:46:29 stacker dracut: *** Including module: usrmount ***
Sep 25 20:46:29 stacker dracut: *** Including module: base ***
Sep 25 20:46:30 stacker dracut: *** Including module: fs-lib ***
Sep 25 20:46:30 stacker dracut: *** Including module: microcode_ctl-fw_dir_override ***
Sep 25 20:46:30 stacker dracut:  microcode_ctl module: mangling fw_dir
Sep 25 20:46:30 stacker dracut:    microcode_ctl: processing data directory  "/usr/share/microcode_ctl/ucode_with_caveats/intel"...
Sep 25 20:46:30 stacker dracut:    microcode_ctl: kernel version "3.10.0-862.11.6.el7.x86_64" failed early load check for "intel", skipping
Sep 25 20:46:30 stacker dracut:    microcode_ctl: processing data directory  "/usr/share/microcode_ctl/ucode_with_caveats/intel-06-4f-01"...
Sep 25 20:46:30 stacker dracut:    microcode_ctl: kernel version "3.10.0-862.11.6.el7.x86_64" failed early load check for "intel-06-4f-01", skipping
Sep 25 20:46:30 stacker dracut:    microcode_ctl: final fw_dir: "/lib/firmware/3.10.0-693.5.2.el7.x86_64/lib/firmware/3.10.0-862.11.6.el7.x86_64/lib/firmware/3.10.0-514.26.2.el7.x86_64/lib/firmware/3.10.0-693.2.2.el7.x86_64/lib/firmware/3.10.0-693.5.2.el7.x86_64"
Sep 25 20:46:30 stacker dracut: *** Including module: shutdown ***
Sep 25 20:46:30 stacker dracut: *** Including modules done ***
Sep 25 20:46:30 stacker dracut: Possible missing firmware "amdgpu/raven_gpu_info.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "amdgpu/vega12_gpu_info.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "amdgpu/vega10_gpu_info.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/bonaire_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/bonaire_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/mullins_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/mullins_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/mullins_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/mullins_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/mullins_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kabini_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kabini_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kabini_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kabini_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kabini_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kaveri_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kaveri_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kaveri_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kaveri_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kaveri_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/kaveri_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/hawaii_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:30 stacker dracut: Possible missing firmware "radeon/bonaire_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/mullins_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/mullins_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/kabini_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/kabini_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/kaveri_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/kaveri_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hawaii_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hawaii_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/si58_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/tahiti_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hainan_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hainan_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hainan_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hainan_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/tahiti_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/tahiti_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/tahiti_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/tahiti_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/banks_k_2_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hainan_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hainan_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/oland_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/verde_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/pitcairn_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/tahiti_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/topaz_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/hawaii_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "radeon/bonaire_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vega20_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vega20_sos.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vega12_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vega12_sos.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vega10_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vega10_sos.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/raven_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vegam_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vegam_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vegam_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vegam_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vegam_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/vegam_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec2_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_me_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_pfp_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_ce_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris12_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec2_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_me_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_pfp_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_ce_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris11_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec2_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_me_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_pfp_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_ce_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/polaris10_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/fiji_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/fiji_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/fiji_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/fiji_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/fiji_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/fiji_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/topaz_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/topaz_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/topaz_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/topaz_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/topaz_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/tonga_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/stoney_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/stoney_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/stoney_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/stoney_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/stoney_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/carrizo_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/carrizo_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/carrizo_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/carrizo_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/carrizo_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/carrizo_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/raven_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:31 stacker dracut: Possible missing firmware "amdgpu/raven_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/raven_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/raven_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/raven_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/raven_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/topaz_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/topaz_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vegam_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vegam_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris12_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris12_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/stoney_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/fiji_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/fiji_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/carrizo_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/carrizo_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/tonga_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/tonga_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/raven_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vegam_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris12_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/stoney_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/fiji_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/carrizo_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/tonga_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/mullins_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/hawaii_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/kaveri_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/kabini_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/bonaire_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vegam_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris12_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/stoney_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/fiji_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/carrizo_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/tonga_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/mullins_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/hawaii_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/kaveri_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/kabini_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "radeon/bonaire_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/raven_vcn.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega20_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega12_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_acg_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vega10_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/vegam_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris12_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_smc_sk.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris11_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_smc_sk.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/polaris10_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/fiji_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/tonga_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/tonga_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/topaz_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:46:32 stacker dracut: Possible missing firmware "amdgpu/topaz_smc.bin" for kernel module "amdgpu.ko"

Broadcast message from systemd-journald@localhost (Tue 2018-09-25 20:46:32 CEST):

dracut[9113]: Failed to install module amdkfdamdgpu


Message from syslogd@stacker at Sep 25 20:46:32 ...
 dracut:Failed to install module amdkfdamdgpu
Sep 25 20:46:32 stacker dracut: Failed to install module amdkfdamdgpu
Sep 25 20:46:32 stacker dracut: *** Installing kernel module dependencies and firmware ***
Sep 25 20:46:33 stacker dracut: *** Installing kernel module dependencies and firmware done ***
Sep 25 20:46:33 stacker dracut: *** Resolving executable dependencies ***
Sep 25 20:46:35 stacker dracut: *** Resolving executable dependencies done***
Sep 25 20:46:35 stacker dracut: *** Hardlinking files ***
Sep 25 20:46:35 stacker dracut: *** Hardlinking files done ***
Sep 25 20:46:35 stacker dracut: *** Stripping files ***
Sep 25 20:46:36 stacker dracut: *** Stripping files done ***
Sep 25 20:46:36 stacker dracut: *** Generating early-microcode cpio image contents ***
Sep 25 20:46:36 stacker dracut: *** No early-microcode cpio image needed ***
Sep 25 20:46:36 stacker dracut: *** Store current command line parameters ***
Sep 25 20:46:36 stacker dracut: *** Creating image file ***
Sep 25 20:46:45 stacker dracut: *** Creating image file done ***
Sep 25 20:46:54 stacker dracut: *** Creating initramfs image file '/boot/initramfs-3.10.0-862.11.6.el7.x86_64.tmp' done ***
Sep 25 20:47:03 stacker kernel: floppy0: no floppy controllers found
Sep 25 20:47:04 stacker dracut: dracut-033-535.el7_5.1
Sep 25 20:47:04 stacker dracut: Executing: /bin/dracut -f /boot/initramfs-3.10.0-862.11.6.el7.x86_64.img 3.10.0-862.11.6.el7.x86_64
Sep 25 20:47:05 stacker dracut: dracut module 'busybox' will not be installed, because command 'busybox' could not be found!
Sep 25 20:47:05 stacker dracut: dracut module 'multipath' will not be installed, because command 'multipath' could not be found!
Sep 25 20:47:05 stacker dracut: dracut module 'cifs' will not be installed, because command 'mount.cifs' could not be found!
Sep 25 20:47:06 stacker dracut: dracut module 'busybox' will not be installed, because command 'busybox' could not be found!
Sep 25 20:47:06 stacker dracut: dracut module 'multipath' will not be installed, because command 'multipath' could not be found!
Sep 25 20:47:06 stacker dracut: dracut module 'cifs' will not be installed, because command 'mount.cifs' could not be found!
Sep 25 20:47:07 stacker dracut: *** Including module: bash ***
Sep 25 20:47:07 stacker dracut: *** Including module: nss-softokn ***
Sep 25 20:47:07 stacker dracut: *** Including module: i18n ***
Sep 25 20:47:08 stacker dracut: *** Including module: network ***
Sep 25 20:47:09 stacker dracut: *** Including module: ifcfg ***
Sep 25 20:47:09 stacker dracut: *** Including module: drm ***
Sep 25 20:47:10 stacker dracut: *** Including module: plymouth ***
Sep 25 20:47:11 stacker dracut: *** Including module: dm ***
Sep 25 20:47:11 stacker dracut: Skipping udev rule: 64-device-mapper.rules
Sep 25 20:47:11 stacker dracut: Skipping udev rule: 60-persistent-storage-dm.rules
Sep 25 20:47:11 stacker dracut: Skipping udev rule: 55-dm.rules
Sep 25 20:47:12 stacker dracut: *** Including module: kernel-modules ***
Sep 25 20:47:19 stacker dracut: *** Including module: lvm ***
Sep 25 20:47:19 stacker dracut: Skipping udev rule: 64-device-mapper.rules
Sep 25 20:47:19 stacker dracut: Skipping udev rule: 56-lvm.rules
Sep 25 20:47:19 stacker dracut: Skipping udev rule: 60-persistent-storage-lvm.rules
Sep 25 20:47:19 stacker dracut: *** Including module: resume ***
Sep 25 20:47:19 stacker dracut: *** Including module: rootfs-block ***
Sep 25 20:47:19 stacker dracut: *** Including module: terminfo ***
Sep 25 20:47:19 stacker dracut: *** Including module: udev-rules ***
Sep 25 20:47:19 stacker dracut: Skipping udev rule: 40-redhat-cpu-hotplug.rules
Sep 25 20:47:20 stacker dracut: Skipping udev rule: 91-permissions.rules
Sep 25 20:47:20 stacker dracut: *** Including module: biosdevname ***
Sep 25 20:47:20 stacker dracut: *** Including module: systemd ***
Sep 25 20:47:21 stacker dracut: *** Including module: usrmount ***
Sep 25 20:47:21 stacker dracut: *** Including module: base ***
Sep 25 20:47:21 stacker dracut: *** Including module: fs-lib ***
Sep 25 20:47:21 stacker dracut: *** Including module: microcode_ctl-fw_dir_override ***
Sep 25 20:47:21 stacker dracut:  microcode_ctl module: mangling fw_dir
Sep 25 20:47:21 stacker dracut:    microcode_ctl: processing data directory  "/usr/share/microcode_ctl/ucode_with_caveats/intel"...
Sep 25 20:47:21 stacker dracut:    microcode_ctl: kernel version "3.10.0-862.11.6.el7.x86_64" failed early load check for "intel", skipping
Sep 25 20:47:21 stacker dracut:    microcode_ctl: processing data directory  "/usr/share/microcode_ctl/ucode_with_caveats/intel-06-4f-01"...
Sep 25 20:47:21 stacker dracut:    microcode_ctl: kernel version "3.10.0-862.11.6.el7.x86_64" failed early load check for "intel-06-4f-01", skipping
Sep 25 20:47:21 stacker dracut:    microcode_ctl: final fw_dir: "/lib/firmware/3.10.0-693.5.2.el7.x86_64/lib/firmware/3.10.0-862.11.6.el7.x86_64/lib/firmware/3.10.0-514.26.2.el7.x86_64/lib/firmware/3.10.0-693.2.2.el7.x86_64/lib/firmware/3.10.0-693.5.2.el7.x86_64"
Sep 25 20:47:21 stacker dracut: *** Including module: shutdown ***
Sep 25 20:47:21 stacker dracut: *** Including modules done ***
Sep 25 20:47:21 stacker dracut: Possible missing firmware "amdgpu/raven_gpu_info.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "amdgpu/vega12_gpu_info.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "amdgpu/vega10_gpu_info.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/hawaii_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/hawaii_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/bonaire_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/bonaire_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/mullins_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/mullins_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/mullins_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/mullins_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/mullins_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:21 stacker dracut: Possible missing firmware "radeon/kabini_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kabini_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kabini_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kabini_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kabini_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/mullins_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/mullins_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kabini_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kabini_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/kaveri_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/si58_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/tahiti_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hainan_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hainan_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hainan_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hainan_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/tahiti_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/tahiti_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/tahiti_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/tahiti_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/banks_k_2_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hainan_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hainan_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/oland_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/verde_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/pitcairn_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/tahiti_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/topaz_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/hawaii_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "radeon/bonaire_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_mc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vega20_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vega20_sos.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vega12_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vega12_sos.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vega10_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vega10_sos.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/raven_asd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vegam_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vegam_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vegam_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vegam_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vegam_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/vegam_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec2_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_me_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_pfp_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_ce_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris12_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec2_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_me_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_pfp_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_ce_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris11_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec2_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_me_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_pfp_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_ce_2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/polaris10_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/fiji_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/fiji_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/fiji_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/fiji_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/fiji_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/fiji_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/topaz_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/topaz_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/topaz_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/topaz_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/topaz_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/tonga_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/stoney_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/stoney_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/stoney_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/stoney_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:22 stacker dracut: Possible missing firmware "amdgpu/stoney_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_rlc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_mec2.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_mec.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_me.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_pfp.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_ce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/topaz_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/topaz_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vegam_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vegam_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris12_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris12_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/stoney_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/fiji_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/fiji_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/tonga_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/tonga_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_sdma1.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_sdma.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vegam_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris12_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/stoney_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/fiji_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/tonga_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/mullins_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/hawaii_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/kaveri_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/kabini_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/bonaire_uvd.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vegam_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris12_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/stoney_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/fiji_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/carrizo_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/tonga_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/mullins_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/hawaii_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/kaveri_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/kabini_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "radeon/bonaire_vce.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/raven_vcn.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega20_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega12_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_acg_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vega10_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/vegam_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris12_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_smc_sk.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris11_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_smc_sk.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/polaris10_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/fiji_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/tonga_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/tonga_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/topaz_k_smc.bin" for kernel module "amdgpu.ko"
Sep 25 20:47:23 stacker dracut: Possible missing firmware "amdgpu/topaz_smc.bin" for kernel module "amdgpu.ko"

Broadcast message from systemd-journald@localhost (Tue 2018-09-25 20:47:23 CEST):

dracut[21939]: Failed to install module amdkfdamdgpu


Message from syslogd@stacker at Sep 25 20:47:23 ...
 dracut:Failed to install module amdkfdamdgpu
Sep 25 20:47:23 stacker dracut: Failed to install module amdkfdamdgpu
Sep 25 20:47:23 stacker dracut: *** Installing kernel module dependencies and firmware ***
Sep 25 20:47:24 stacker dracut: *** Installing kernel module dependencies and firmware done ***
Sep 25 20:47:24 stacker dracut: *** Resolving executable dependencies ***
Sep 25 20:47:26 stacker dracut: *** Resolving executable dependencies done***
Sep 25 20:47:26 stacker dracut: *** Hardlinking files ***
Sep 25 20:47:27 stacker dracut: *** Hardlinking files done ***
Sep 25 20:47:27 stacker dracut: *** Stripping files ***
Sep 25 20:47:27 stacker dracut: *** Stripping files done ***
Sep 25 20:47:27 stacker dracut: *** Generating early-microcode cpio image contents ***
Sep 25 20:47:27 stacker dracut: *** No early-microcode cpio image needed ***
Sep 25 20:47:27 stacker dracut: *** Store current command line parameters ***
Sep 25 20:47:27 stacker dracut: *** Creating image file ***
Sep 25 20:47:35 stacker dracut: *** Creating image file done ***
Sep 25 20:47:45 stacker dracut: *** Creating initramfs image file '/boot/initramfs-3.10.0-862.11.6.el7.x86_64.img' done ***
Sep 25 20:47:45 stacker yum[2719]: Installed: rock-dkms-1.9-211.el7.noarch
Sep 25 20:47:45 stacker yum[2719]: Installed: rocm-device-libs-0.0.1-1.x86_64
Sep 25 20:47:45 stacker yum[2719]: Installed: rocm-smi-1.0.0_72_gec1da05-1.x86_64
Sep 25 20:47:45 stacker yum[2719]: Installed: rocm-dev-1.9.211-1.x86_64
Sep 25 20:47:45 stacker yum[2719]: Installed: rocm-dkms-1.9.211-1.x86_64
`

---

### 评论 #5 — le-mikcho (2018-09-25T19:32:31Z)

my bad, missing PCIe Atomics

dmesg [    4.421156] kfd kfd: skipped device 1002:67df, PCI rejects atomics



---
