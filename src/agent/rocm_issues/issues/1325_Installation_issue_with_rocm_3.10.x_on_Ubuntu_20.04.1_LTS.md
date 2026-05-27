# Installation issue with rocm 3.10.x on Ubuntu 20.04.1 LTS

> **Issue #1325**
> **状态**: closed
> **创建时间**: 2020-12-09T06:31:38Z
> **更新时间**: 2020-12-11T04:37:43Z
> **关闭时间**: 2020-12-10T09:23:25Z
> **作者**: rajeeb-barman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1325

## 描述

I had a older version of ROCm installed in my system and it it was working. Since new version is available I tried following to install the new version

I have uninstalled using following command:
  sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils && sudo reboot

and followed the remaining installation steps as mentioned in the following link for ubuntu
   https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

Error during installation (make.log):
DKMS make.log for amdgpu-3.10-27 for kernel 5.4.0-56-generic (x86_64)
Wednesday 09 December 2020 10:34:11 AM IST
make: Entering directory '/usr/src/linux-headers-5.4.0-56-generic'
/var/lib/dkms/amdgpu/3.10-27/build/Makefile:20: "Local GCC version 90303 does not match kernel compiler GCC version 90300"
/var/lib/dkms/amdgpu/3.10-27/build/Makefile:21: "This may cause unexpected and hard-to-isolate compiler-related issues"
  AR      /var/lib/dkms/amdgpu/3.10-27/build/built-in.a
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_ioctl.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_cache.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_perf_event.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_suspend.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atom.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.c:103:84: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  103 |  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed", _kcl_pcie_link_speed_stub);
      |                                                                                    ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_pci.c:4:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_common.h:12:63: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
   12 | static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
      |                                                         ~~~~~~^~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_seq_file.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_connector.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_backlight.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_atomic_helper.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_crtc.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_fence.c:30:1: warning: ‘dma_fence_test_signaled_any’ defined but not used [-Wunused-function]
   30 | dma_fence_test_signaled_any(struct dma_fence **fences, uint32_t count,
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_fb.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_modeset_lock.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_drm_modes.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_time.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/dma-buf/dma-resv.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_test.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_afmt.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_encoders.o
  LD [M]  /var/lib/dkms/amdgpu/3.10-27/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_dma_buf.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ib.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ucode.o
  LD [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bo_list.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fb.c: In function ‘amdgpufb_create’:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_fb.c:252:14: warning: assignment discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  252 |  info->fbops = &amdgpufb_ops;
      |              ^
  LD [M]  /var/lib/dkms/amdgpu/3.10-27/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_vram_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_vf_error.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_sched.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_debugfs.o
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.c: In function ‘amdgpu_read_platform_bios’:
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.c:200:9: error: implicit declaration of function ‘pci_platform_rom’ [-Werror=implicit-function-declaration]
  200 |  bios = pci_platform_rom(adev->pdev, &size);
      |         ^~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.c:200:7: warning: assignment to ‘uint8_t *’ {aka ‘unsigned char *’} from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
  200 |  bios = pci_platform_rom(adev->pdev, &size);
      |       ^
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ids.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_gmc.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_mmhub.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_xgmi.o
cc1: some warnings being treated as errors
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_csa.o
  CC [M]  /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_ras.o
make[2]: *** [scripts/Makefile.build:275: /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu/amdgpu_bios.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [scripts/Makefile.build:522: /var/lib/dkms/amdgpu/3.10-27/build/amd/amdgpu] Error 2
make: *** [Makefile:1757: /var/lib/dkms/amdgpu/3.10-27/build] Error 2
make: Leaving directory '/usr/src/linux-headers-5.4.0-56-generic'






---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2020-12-09T08:42:25Z)

Hi @rajeeb-barman 
Thanks for reaching out.
Its already known and worked on the fix already. Its actually duplicate of #1315 
We are ready to push the fix soon, please stay tuned.
Thank you.

---

### 评论 #2 — ROCmSupport (2020-12-11T04:37:43Z)

Hi All,
Fix for 5.4.0-56 is ready and pushed too. Updated Documentation accordingly.
Request to try the new packages.

**_Note: AMD ROCm v3.10 fails to install on Ubuntu kernel v5.4.0-56. To resolve the installation issue, new packages for 'rock-dkms' and 'rock-dkms-firmware' are created and replaced. It is recommended to perform a clean and fresh installation with the new packages._**

Thank you.

---
