# Downgrade to 3.9 fails

> **Issue #1333**
> **状态**: closed
> **创建时间**: 2020-12-12T10:46:17Z
> **更新时间**: 2020-12-14T08:17:34Z
> **关闭时间**: 2020-12-14T05:40:27Z
> **作者**: Dan-RAI
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1333

## 描述

Have been running 3.9 successfully before. Now I get via apt install:

Loading new amdgpu-3.9-17 DKMS files...
Building for 4.15.0-128-generic
Building for architecture x86_64
Building initial module for 4.15.0-128-generic
Error! Bad return status for module build on kernel: 4.15.0-128-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.9-17/build/make.log for more information.


make.log:

DKMS make.log for amdgpu-3.9-17 for kernel 4.15.0-128-generic (x86_64)
Sa Dez 12 11:38:12 CET 2020
make: Entering directory '/usr/src/linux-headers-4.15.0-128-generic'
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_ioctl.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm_cache.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_perf_event.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_suspend.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_seq_file.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_connector.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_backlight.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm_atomic_helper.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_display.o
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_mm.c:5:44: warning: ‘struct task_struct’ declared inside parameter list will not be visible outside of this definition or declaration
 struct mm_struct* (*_kcl_mm_access)(struct task_struct *task, unsigned int mode);
                                            ^~~~~~~~~~~
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_mm.c:8:55: warning: ‘struct task_struct’ declared inside parameter list will not be visible outside of this definition or declaration
 static struct mm_struct * __kcl_mm_access_stub(struct task_struct *task, unsigned int mode)
                                                       ^~~~~~~~~~~
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_suspend.c: In function ‘amdkcl_suspend_init’:
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_suspend.c:30:21: warning: comparison of distinct pointer types lacks a cast
  if (_kcl_ksys_sync != _kcl_sys_sync_stub) {
                     ^~
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_suspend.c:35:21: warning: comparison of distinct pointer types lacks a cast
  if (_kcl_ksys_sync != _kcl_sys_sync_stub) {
                     ^~
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm_fb.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm_modeset_lock.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_drm_modes.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/dma-buf/dma-resv.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_test.o
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_pci.c:103:84: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed", _kcl_pcie_link_speed_stub);
                                                                                    ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_pci.c:4:0:
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/kcl_common.h:12:21: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
 static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
                     ^~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_afmt.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_dma_buf.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ib.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ucode.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bo_list.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_vram_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_vf_error.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_sched.o
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_fb.c: In function ‘amdgpufb_create’:
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_fb.c:252:14: warning: assignment discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  info->fbops = &amdgpufb_ops;
              ^
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_debugfs.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ids.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_gmc.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_mmhub.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_xgmi.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_csa.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ras.o
  LD [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_vm_cpu.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_vm_sdma.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_discovery.o
  LD [M]  /var/lib/dkms/amdgpu/3.9-17/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_ras_eeprom.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_nbio.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_umc.o
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_cs.c:1225:12: warning: ‘amdgpu_cs_process_syncobj_timeline_out_dep’ defined but not used [-Wunused-function]
 static int amdgpu_cs_process_syncobj_timeline_out_dep(struct amdgpu_cs_parser *p,
            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_cs.c:1165:12: warning: ‘amdgpu_cs_process_syncobj_timeline_in_dep’ defined but not used [-Wunused-function]
 static int amdgpu_cs_process_syncobj_timeline_in_dep(struct amdgpu_cs_parser *p,
            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bios.c: In function ‘amdgpu_read_platform_bios’:
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bios.c:200:9: error: implicit declaration of function ‘pci_platform_rom’; did you mean ‘pci_map_rom’? [-Werror=implicit-function-declaration]
  bios = pci_platform_rom(adev->pdev, &size);
         ^~~~~~~~~~~~~~~~
         pci_map_rom
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bios.c:200:7: warning: assignment makes pointer from integer without a cast [-Wint-conversion]
  bios = pci_platform_rom(adev->pdev, &size);
       ^
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/smu_v11_0_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_sem.o
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_fru_eeprom.o
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_sa.c: In function ‘amdgpu_sa_bo_dump_debug_info’:
/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_sa.c:391:41: warning: format ‘%llx’ expects argument of type ‘long long unsigned int’, but argument 3 has type ‘unsigned int’ [-Wformat=]
    seq_printf(m, " protected by 0x%016llx on context %llu",
                                   ~~~~~~^
                                   %016x
        i->fence->seqno, i->fence->context);
        ~~~~~~~~~~~~~~~                   
  CC [M]  /var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_rap.o
  LD [M]  /var/lib/dkms/amdgpu/3.9-17/build/ttm/amdttm.o
cc1: some warnings being treated as errors
scripts/Makefile.build:330: recipe for target '/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bios.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu/amdgpu_bios.o] Error 1
make[2]: *** Waiting for unfinished jobs....
scripts/Makefile.build:604: recipe for target '/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/3.9-17/build/amd/amdgpu] Error 2
Makefile:1587: recipe for target '_module_/var/lib/dkms/amdgpu/3.9-17/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/3.9-17/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.15.0-128-generic'






---

## 评论 (5 条)

### 评论 #1 — alekseYY (2020-12-12T18:15:20Z)

Almost the same problem for me when trying to upgrade to the kernel 4.15.0-128...
AMD driver is amdgpu-pro-20.40-1147287-ubuntu-18.04


---

### 评论 #2 — iHandle (2020-12-13T06:02:14Z)

Similar to #1323

---

### 评论 #3 — ROCmSupport (2020-12-14T05:40:26Z)

Hi @Dan-RAI , @alekseYY and @iHandle 
Thanks for reaching out.
Fix for  ‘pci_platform_rom’ is available in 3.10, so I recommend to do a fresh install of 3.10 and it works.
(The fix was not there in 3.9 and before and so it fails.)

Please check the below information which is updated in ROCm docs.

_Note: AMD ROCm v3.10 fails to install on Ubuntu kernel v5.4.0-56. To resolve the installation issue, new packages for 'rock-dkms' and 'rock-dkms-firmware' are created and replaced. It is recommended to perform a clean and fresh installation with the new packages._

Thank you.

---

### 评论 #4 — Dan-RAI (2020-12-14T07:01:29Z)

The reason why I want to go back to 3.9 is because 3.10 is NOT working in
my setup !

On Mon, Dec 14, 2020 at 6:40 AM ROCmSupport <notifications@github.com>
wrote:

> Closed #1333 <https://github.com/RadeonOpenCompute/ROCm/issues/1333>.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1333#event-4107245879>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AE575QWATJP5N2YTZ7HMANDSUWQNRANCNFSM4UX7VWAQ>
> .
>


---

### 评论 #5 — ROCmSupport (2020-12-14T07:05:40Z)

Hi @Dan-RAI 
After that fix for kernel packages, 3.10 should work definitely.
3.9 and lower might not work in your machine as the fix is not available for the kernel in those versions.
So recommend to do a clean uninstall of all ROCm components and then only do a fresh and clean install of ROCm 3.10, it works.

---
