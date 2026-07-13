# cannot install rocm 2.10 on ubuntu 16.04.7

- **Issue #:** 1509
- **State:** closed
- **Created:** 2021-06-30T05:56:55Z
- **Updated:** 2021-06-30T11:37:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1509

hi, 
   we're trying install rocm 2.10.14 on ubuntu 16.04.6, but there 're no 64bit ubuntu version
   does it support ubuntu 16.04.7(kernel 4.15.0-142)?,  we've tried but there is compiling issue,plz see logs below, is that possible to fix it?

 DKMS make.log for amdgpu-2.10-14 for kernel 4.15.0-142-generic (x86_64)
make: Entering directory '/usr/src/linux-headers-4.15.0-142-generic'
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_perf_event.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_benchmark.o
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.c:189:84: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed", _kcl_pcie_link_speed);
                                                                                    ^
In file included from /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_pci.c:3:0:
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/kcl_common.h:22:21: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
 static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
                     ^
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_test.o
/var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_memory.c:29:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 ^
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.10-14/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.10-14/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:289:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 ^
/var/lib/dkms/amdgpu/2.10-14/build/ttm/ttm_agp_backend.c:33:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 ^
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.10-14/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.10-14/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:289:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 ^
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_pm.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_afmt.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_dma_buf.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_ib.o
  LD [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_ucode.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bo_list.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_vram_mgr.o
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.c: In function ‘amdgpu_read_platform_bios’:
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.c:199:9: error: implicit declaration of function ‘pci_platform_rom’ [-Werror=implicit-function-declaration]
  bios = pci_platform_rom(adev->pdev, &size);
         ^
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.c:199:7: warning: assignment makes pointer from integer without a cast [-Wint-conversion]
  bios = pci_platform_rom(adev->pdev, &size);
       ^
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_cs.c:1110:12: warning: ‘amdgpu_cs_process_syncobj_timeline_in_dep’ defined but not used [-Wunused-function]
 static int amdgpu_cs_process_syncobj_timeline_in_dep(struct amdgpu_cs_parser *p,
            ^
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_cs.c:1170:12: warning: ‘amdgpu_cs_process_syncobj_timeline_out_dep’ defined but not used [-Wunused-function]
 static int amdgpu_cs_process_syncobj_timeline_out_dep(struct amdgpu_cs_parser *p,
            ^
  LD [M]  /var/lib/dkms/amdgpu/2.10-14/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_vf_error.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_debugfs.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_ids.o
  CC [M]  /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_gmc.o
cc1: some warnings being treated as errors
scripts/Makefile.build:330: recipe for target '/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_dma_buf.c:144:1: warning: ‘__reservation_object_make_exclusive’ defined but not used [-Wunused-function]
 __reservation_object_make_exclusive(struct reservation_object *obj)
 ^
  LD [M]  /var/lib/dkms/amdgpu/2.10-14/build/ttm/amdttm.o
scripts/Makefile.build:604: recipe for target '/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu] Error 2
Makefile:1584: recipe for target '_module_/var/lib/dkms/amdgpu/2.10-14/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/2.10-14/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.15.0-142-generic'
