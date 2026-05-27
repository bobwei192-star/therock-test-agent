# cannot install rocm 2.10 on ubuntu 16.04.7

> **Issue #1509**
> **状态**: closed
> **创建时间**: 2021-06-30T05:56:55Z
> **更新时间**: 2021-06-30T11:37:43Z
> **关闭时间**: 2021-06-30T11:37:43Z
> **作者**: protoss1235
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1509

## 描述

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


---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-06-30T06:11:50Z)

Hi @hongbilu 
Thanks for reaching out.
We are NOT supporting Ubuntu 16.04 officially and also ROCm 2.10 is much old, which is around 2 years old.
I am not sure why are you trying the old code and with old Ubuntu version too.
Recommend to try with the latest ROCm 4.2 + Ubuntu 20.04.2(or Ubuntu 18.04.5).
Thank you.

---

### 评论 #2 — protoss1235 (2021-06-30T06:18:44Z)

by the way, i tried to modify /var/lib/dkms/amdgpu/2.10-14/build/amd/amdgpu/amdgpu_bios.c

#if 0
static bool amdgpu_read_platform_bios(struct amdgpu_device *adev)
{
        uint8_t __iomem *bios;
        size_t size;

        adev->bios = NULL;

        bios = pci_platform_rom(adev->pdev, &size);
        if (!bios) {
                return false;
        }

        adev->bios = kzalloc(size, GFP_KERNEL);
        if (adev->bios == NULL)
                return false;

        memcpy_fromio(adev->bios, bios, size);

        if (!check_atom_bios(adev->bios, size)) {
                kfree(adev->bios);
                return false;
        }

        adev->bios_size = size;

        return true;
}
#endif
static bool amdgpu_read_platform_bios(struct amdgpu_device *adev)
{
        phys_addr_t rom = adev->pdev->rom;
        size_t romlen = adev->pdev->romlen;
        void __iomem *bios;

        adev->bios = NULL;

        if (!rom || romlen == 0)
                return false;

        adev->bios = kzalloc(romlen, GFP_KERNEL);
        if (!adev->bios)
                return false;

        bios = ioremap(rom, romlen);
        if (!bios)
                goto free_bios;

        memcpy_fromio(adev->bios, bios, romlen);
        iounmap(bios);

        if (!check_atom_bios(adev->bios, romlen))
                goto free_bios;

        adev->bios_size = romlen;

        return true;
free_bios:
        kfree(adev->bios);
        return false;
}

so the compiling issue fixed, and it will install succesfully, but after server reboot, there're some resize-bar error in boot phase:

[    2.720473] [drm:amdgpu_get_bios [amdgpu]] *ERROR* ACPI VFCT table present but broken (too short #2)
[    3.765920] amdgpu 0000:1a:00.0: BAR 2: releasing [mem 0x17ff4000000-0x17ff41fffff 64bit pref]
[    3.765921] amdgpu 0000:1a:00.0: BAR 0: releasing [mem 0x17fe0000000-0x17fefffffff 64bit pref]
[    3.766027] [drm:amdgpu_device_resize_fb_bar [amdgpu]] *ERROR* Problem resizing BAR0 (-2) rbar_size(13).
[    3.766088]  amdgpu_device_resize_fb_bar+0x1f4/0x200 [amdgpu]
[    3.766140]  gmc_v8_0_sw_init+0x6ca/0x910 [amdgpu]
[    3.766182]  amdgpu_device_init+0x100a/0x1b20 [amdgpu]
[    3.766228]  amdgpu_driver_load_kms+0x87/0x2d0 [amdgpu]
[    3.766281]  amdgpu_pci_probe+0xdd/0x190 [amdgpu]
[    3.766298] amdgpu 0000:1a:00.0: BAR 0: assigned [mem 0x17fe0000000-0x17fefffffff 64bit pref]
[    3.766306] amdgpu 0000:1a:00.0: BAR 2: assigned [mem 0x17ff4000000-0x17ff41fffff 64bit pref]
[    3.766325] amdgpu 0000:1a:00.0: VRAM: 8190M 0x000000F400000000 - 0x000000F5FFDFFFFF (8190M used)
[    3.766326] amdgpu 0000:1a:00.0: GART: 1024M 0x000000FF00000000 - 0x000000FF3FFFFFFF
[    3.766544] [drm] amdgpu: 8190M of VRAM memory ready
[    3.766546] [drm] amdgpu: 128582M of GTT memory ready.
[    3.768069] amdgpu: [powerplay] hwmgr_sw_init smu backed is tonga_smu
[    4.094992] [drm] Initialized amdgpu 3.34.0 20150101 for 0000:1a:00.0 on minor 1
[    4.095414] [drm:amdgpu_get_bios [amdgpu]] *ERROR* ACPI VFCT table present but broken (too short #2)
[    5.132413] amdgpu 0000:1c:00.0: BAR 2: releasing [mem 0x17ed4000000-0x17ed41fffff 64bit pref]
[    5.132414] amdgpu 0000:1c:00.0: BAR 0: releasing [mem 0x17ec0000000-0x17ecfffffff 64bit pref]
[    5.132494] [drm:amdgpu_device_resize_fb_bar [amdgpu]] *ERROR* Problem resizing BAR0 (-2) rbar_size(13).

does anybody see this error?

---

### 评论 #3 — protoss1235 (2021-06-30T06:21:33Z)

> Hi @hongbilu
> Thanks for reaching out.
> We are NOT supporting Ubuntu 16.04 officially and also ROCm 2.10 is much old, which is around 2 years old.
> I am not sure why are you trying the old code and with old Ubuntu version too.
> Recommend to try with the latest ROCm 4.2 + Ubuntu 20.04.2(or Ubuntu 18.04.5).
> Thank you.

because we  want to use rocSHMEM which only have been verified on rocm 2.10, so we need to install rocm 2.10

---

### 评论 #4 — ROCmSupport (2021-06-30T07:06:06Z)

Hi @hongbilu 
[https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/62](url) might help you on the bar resizing problem.

---

### 评论 #5 — protoss1235 (2021-06-30T11:37:43Z)

> Hi @hongbilu
> Thanks for reaching out.
> We are NOT supporting Ubuntu 16.04 officially and also ROCm 2.10 is much old, which is around 2 years old.
> I am not sure why are you trying the old code and with old Ubuntu version too.
> Recommend to try with the latest ROCm 4.2 + Ubuntu 20.04.2(or Ubuntu 18.04.5).
> Thank you.



---
