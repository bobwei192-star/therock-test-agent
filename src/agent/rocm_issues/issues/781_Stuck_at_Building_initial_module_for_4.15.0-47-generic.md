# Stuck at "Building initial module for 4.15.0-47-generic"

> **Issue #781**
> **状态**: closed
> **创建时间**: 2019-04-24T19:16:56Z
> **更新时间**: 2021-05-19T06:55:41Z
> **关闭时间**: 2021-05-19T06:55:41Z
> **作者**: calvintam236
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/781

## 描述

Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-47-generic x86_64)
ROCm 2.3-14

I have ran `apt upgrade` for updates, and the computer is stuck at `Building initial module`. SSH becomes unresponsive at this stage (computer froze). I have tried `dpkg --configure -a` and get the same behavior. I know the computer was upgraded to 4.15.0-45 kernel and ROCm 2.2-31 in the last `apt upgrade`, and there was no problem.

```console
$ apt upgrade -y
Reading package lists... Done
Unpacking rock-dkms (2.3-14) over (2.2-31) ...
Preparing to unpack .../12-rocm-device-libs_0.0.1_amd64.deb ...
Unpacking rocm-device-libs (0.0.1) over (0.0.1) ...
Preparing to unpack .../13-rocm-smi_1.0.0-129-g71924de_amd64.deb ...
Unpacking rocm-smi (1.0.0-129-g71924de) over (1.0.0-102-gdb444a9) ...
Preparing to unpack .../14-rocr%5fdebug%5fagent_1.0.0_amd64.deb ...
Unpacking rocr_debug_agent (1.0.0) over (1.0.0) ...
Preparing to unpack .../15-rocm-dev_2.3.14_amd64.deb ...
Unpacking rocm-dev (2.3.14) over (2.2.31) ...
Preparing to unpack .../16-rocm-dkms_2.3.14_amd64.deb ...
Unpacking rocm-dkms (2.3.14) over (2.2.31) ...
Preparing to unpack .../17-rocm-opencl_1.2.0-2019040843_amd64.deb ...
Unpacking rocm-opencl (1.2.0-2019040843) over (1.2.0-2019030702) ...
Preparing to unpack .../18-rocm-opencl-dev_1.2.0-2019040843_amd64.deb ...
Unpacking rocm-opencl-dev (1.2.0-2019040843) over (1.2.0-2019030702) ...
Setting up rocm-utils (2.3.14) ...
Setting up comgr (1.2.0) ...
Setting up rocr_debug_agent (1.0.0) ...
Setting up rocm-smi (1.0.0-129-g71924de) ...
Setting up rocm-device-libs (0.0.1) ...
Setting up hip_base (1.5.19123) ...
Setting up rock-dkms (2.3-14) ...
Loading new amdgpu-2.3-14 DKMS files...
Building for 4.15.0-46-generic 4.15.0-48-generic
Building for architecture x86_64
Building initial module for 4.15.0-46-generic
// frozen here

$ /opt/rocm/bin/rocm-smi 
Traceback (most recent call last):
  File "/opt/rocm/bin/rocm-smi", line 1796, in <module>
    deviceList = listDevices(args.alldevices)
  File "/opt/rocm/bin/rocm-smi", line 518, in listDevices
    devicelist = [device for device in os.listdir(drmprefix) if re.match(r'^card\d+$', device) and (isAmdDevice(device) or showall)]
OSError: [Errno 2] No such file or directory: '/sys/class/drm'
```

---

## 评论 (2 条)

### 评论 #1 — calvintam236 (2019-04-25T03:41:30Z)

Looks like 4.15.0-48 doesn't work either.

```console
$ cat /var/lib/dkms/amdgpu/2.3-14/build/make.log 
DKMS make.log for amdgpu-2.3-14 for kernel 4.15.0-48-generic (x86_64)
Thu Apr 25 11:38:05 CST 2019
make: Entering directory '/usr/src/linux-headers-4.15.0-48-generic'
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_atombios.o
/var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_reservation.c:427:1: warning: ‘reservation_object_add_shared_replace’ defined but not used [-Wunused-function]
 reservation_object_add_shared_replace(struct reservation_object *obj,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_reservation.c:375:1: warning: ‘reservation_object_add_shared_inplace’ defined but not used [-Wunused-function]
 reservation_object_add_shared_inplace(struct reservation_object *obj,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_memory.c:29:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.3-14/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.3-14/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:285:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/atom.o
  LD [M]  /var/lib/dkms/amdgpu/2.3-14/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_object.o
  LD [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_agp_backend.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ring.o
/var/lib/dkms/amdgpu/2.3-14/build/ttm/ttm_agp_backend.c:33:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.3-14/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.3-14/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:285:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_test.o
  LD [M]  /var/lib/dkms/amdgpu/2.3-14/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_pm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_afmt.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_prime.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ib.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ucode.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_bo_list.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vram_mgr.o
/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_prime.c:197:1: warning: ‘__reservation_object_make_exclusive’ defined but not used [-Wunused-function]
 __reservation_object_make_exclusive(struct reservation_object *obj)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vf_error.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_debugfs.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ids.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_xgmi.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_gmc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_csa.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_sem.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ras.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vm_cpu.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vm_sdma.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/cik.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/cik_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/kv_smc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/kv_dpm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/dce_v8_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gfx_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/cik_sdma.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v4_2.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vce_v2_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/si.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gmc_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gfx_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/si_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/si_dma.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/dce_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/si_dpm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/si_smc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vi.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/mxgpu_vi.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/nbio_v6_1.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/soc15.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/emu_soc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/mxgpu_ai.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/nbio_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vega10_reg_init.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vega20_reg_init.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/nbio_v7_4.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/df_v1_7.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/df_v3_6.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gmc_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gmc_v8_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gfxhub_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/mmhub_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gmc_v9_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gfxhub_v1_1.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_irq.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/iceland_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/tonga_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/cz_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vega10_ih.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_psp.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/psp_v3_1.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/psp_v10_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/psp_v11_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_dpm.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/dce_v10_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/dce_v11_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/dce_virtual.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_gfx.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_rlc.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gfx_v8_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/gfx_v9_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_sdma.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/sdma_v2_4.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/sdma_v3_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/sdma_v4_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_uvd.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v5_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v6_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v7_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vce.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vce_v3_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vce_v4_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_vcn.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/vcn_v1_0.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/amdgpu_amdkfd.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/../amdkfd/kfd_module.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/../amdkfd/kfd_device.o
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/../amdkfd/kfd_chardev.o
/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v6_0.c: In function ‘uvd_v6_0_ring_emit_pipeline_sync’:
/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v6_0.c:1058:1: internal compiler error: Segmentation fault
 }
 ^
  CC [M]  /var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/../amdkfd/kfd_topology.o
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-7/README.Bugs> for instructions.
scripts/Makefile.build:330: recipe for target '/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v6_0.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu/uvd_v6_0.o] Error 1
make[2]: *** Waiting for unfinished jobs....
scripts/Makefile.build:604: recipe for target '/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/2.3-14/build/amd/amdgpu] Error 2
Makefile:1552: recipe for target '_module_/var/lib/dkms/amdgpu/2.3-14/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/2.3-14/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.15.0-48-generic'
```

---

### 评论 #2 — calvintam236 (2019-05-10T18:00:06Z)

Update for v2.4:
Build success up to 4.15.0-47, not on 4.15.0-48

```log
DKMS make.log for amdgpu-2.4-25 for kernel 4.15.0-48-generic (x86_64)
Sat May 11 01:57:18 CST 2019
make: Entering directory '/usr/src/linux-headers-4.15.0-48-generic'
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_bo_manager.o
/var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_memory.c:29:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.4-25/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.4-25/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:285:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/atombios_crtc.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_connectors.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_agp_backend.o
/var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_reservation.c:427:1: warning: ‘reservation_object_add_shared_replace’ defined but not used [-Wunused-function]
 reservation_object_add_shared_replace(struct reservation_object *obj,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_reservation.c:375:1: warning: ‘reservation_object_add_shared_inplace’ defined but not used [-Wunused-function]
 reservation_object_add_shared_inplace(struct reservation_object *obj,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_ttm.o
  LD [M]  /var/lib/dkms/amdgpu/2.4-25/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_object.o
/var/lib/dkms/amdgpu/2.4-25/build/ttm/ttm_agp_backend.c:33:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.4-25/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.4-25/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:285:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_gart.o
/var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_pci.c:255:83: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed",_kcl_pcie_link_speed_stub);
                                                                                   ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_pci.c:3:0:
/var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_common.h:22:21: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
 static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
                     ^~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_display.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_fb.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_bios.o
  LD [M]  /var/lib/dkms/amdgpu/2.4-25/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_test.o
  LD [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_pm.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_afmt.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_prime.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_ib.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_ucode.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_bo_list.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_vram_mgr.o
/var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_prime.c:197:1: warning: ‘__reservation_object_make_exclusive’ defined but not used [-Wunused-function]
 __reservation_object_make_exclusive(struct reservation_object *obj)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_vf_error.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_debugfs.o
Killed
scripts/Makefile.build:330: recipe for target '/var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_bo_list.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu/amdgpu_bo_list.o] Error 137
make[2]: *** Waiting for unfinished jobs....
make[2]: *** wait: No child processes.  Stop.
scripts/Makefile.build:604: recipe for target '/var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/2.4-25/build/amd/amdgpu] Error 2
Makefile:1552: recipe for target '_module_/var/lib/dkms/amdgpu/2.4-25/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/2.4-25/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.15.0-48-generic'
```

---
