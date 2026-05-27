# cant boot with rocm 2.5 and radeon vii

> **Issue #815**
> **状态**: closed
> **创建时间**: 2019-06-08T20:04:09Z
> **更新时间**: 2019-07-13T17:43:36Z
> **关闭时间**: 2019-07-13T17:43:36Z
> **作者**: witeko
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/815

## 描述

I've tried ubuntu 18.04.02 and 19.04 with various kernel versions.
I have a threadripper 1920x and 2 x radeon vii and an LG 4k60 monitor on DP.
Looks like my monitor is loosing signal while booting.

---

## 评论 (20 条)

### 评论 #1 — kentrussell (2019-06-10T12:37:15Z)

Are you able to ssh into the machine? Is there anything in dmesg to explain the issue? Is the issue present on both cards, or is it limited to the DP output on one card?

---

### 评论 #2 — witeko (2019-06-10T15:47:32Z)

@kentrussell Did You make any changes that could potentially lead to such a problem? :)
Now I reverted back to 2.4.
If its not easy to pin point the problem than I'm willing to help.

---

### 评论 #3 — kentrussell (2019-06-10T16:59:22Z)

I didn't personally, but there could be a bug in some of the patches that we brought in from amdgpu/Display team. There shouldn't be anything that's ROCm-specific that caused the issue, but without investigating it's hard to know for sure. If you're happy with 2.4, that's good, but we'd need to do a lot of debugging to figure out what's up, starting with seeing if the machine is just totally not working, or if it's just the display that's not. But without a second machine or a serial connector, that's tougher to do.

---

### 评论 #4 — witeko (2019-06-11T22:05:55Z)

@kentrussell can You assign someone to this?
There is another similar issue with additional information.

---

### 评论 #5 — witeko (2019-06-14T22:29:11Z)

@kentrussell is there any progress on the issue/s?

---

### 评论 #6 — kentrussell (2019-06-15T00:29:00Z)

We don't have a radeon vii for me to use unfortunately. Can you ssh into it to get a dmesg from it to give us some insight? Or even trying it, rebooting it into another kernel, and extracting the failing log from /var/log/kern.log ?

---

### 评论 #7 — hyc3z (2019-06-15T03:17:42Z)

That's pretty strange. I'm also using radeon vii, and I tried Ubuntu 19.04 , with linux kernel 5.0.0-13, 5.0.0-16, 5.2.0-rc4, and they all worked perfectly well. I'm using rocm 2.5 with KFD that comes with the kernel though, haven't tried to build rocm-dkms module on older kernels.

---

### 评论 #8 — witeko (2019-06-15T08:08:59Z)

@kentrussell can You check the other issue #818 - its seems its the same as i have.

---

### 评论 #9 — witeko (2019-06-15T10:36:00Z)

Looks like the monitor just goes "out of range" during the boot with rocm 2.5 (it didnt with 2.4).
I just need to type in my crypto password for my lvm disk while the sceen is "blank" and eventually it boots and the screen turns on.

---

### 评论 #10 — witeko (2019-06-15T17:23:05Z)

@Hycdog booting with KFD is easy, but if You intend to use it for any compute tasks be prepared to loose a lot of performance. :)

@kentrussell there is nothing in the "failing log", the monitor just goest out of range (no signal) for a while while booting. For most ppl it may not be troublesome, but for me it is (i need to open my luks partition...while the monitor is "blank"). Can You check if the issues is not 100% common to all ppl (but they might not report it).


---

### 评论 #11 — kentrussell (2019-06-17T11:19:08Z)

I just got some feedback from the Display team. Can you try setting amdgpu.ip_block_mask=0x37f as a kernel parameter in GRUB? Let me know if that works, or if it still causes the luks partition to be a problem. We want a proper solution, and this may just be a workaround and we don't want to leave our users who require this in the lurch.
I  would recommend putting this in manually in the GRUB menu by pressing 'e' over the GRUB menu option and manually editing it. That way if something goes sideways, you can just reboot and get your old GRUB config back.

---

### 评论 #12 — witeko (2019-06-17T22:29:19Z)

@kentrussell thx, I will check tomorrow. :)

---

### 评论 #13 — witeko (2019-07-04T21:01:24Z)

@kentrussell i doesnt work for me. I need a different solution.

---

### 评论 #14 — witeko (2019-07-04T21:28:55Z)

@kentrussell I would like to expand my issue.
I order to use rocm 2.5 I need to use kernel 4.18 (it works but has this display issue on boot).
When I want to use 4.15 the dkms driver doesn work at all - when i try to install it i get:
make -j24 KERNELRELEASE=4.15.18-041518-generic -j24 kdir=/lib/modules/4.15.18-041518-generic/build -C /lib/modules/4.15.18-041518-generic/build M=/var/lib/dkms/amdgpu/2.5-27/build....(bad exit status: 2)
ERROR (dkms apport): kernel package linux-headers-4.15.18-041518-generic is not supported
Error! Bad return status for module build on kernel: 4.15.18-041518-generic (x86_64)
Consult /var/lib/dkms/amdgpu/2.5-27/build/make.log for more information.

And the make.log is:
DKMS make.log for amdgpu-2.5-27 for kernel 4.15.18-041518-generic (x86_64)
czw, 4 lip 2019, 23:22:57 CEST
make: Entering directory '/usr/src/linux-headers-4.15.18-041518-generic'
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_drm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/main.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/symbols.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/scheduler/sched_main.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/scheduler/sched_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_fence_array.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_memory.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_tt.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/scheduler/sched_entity.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_kthread.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_bo.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_io.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_bo_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_reservation.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_bo_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_pci.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_module.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_mn.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_bitmap.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_execbuf_util.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_drv.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_device_cgroup.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_page_alloc.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_bo_manager.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_device.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_page_alloc_dma.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_workqueue.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_agp_backend.o
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_reservation.c:427:1: warning: ‘reservation_object_add_shared_replace’ defined but not used [-Wunused-function]
 reservation_object_add_shared_replace(struct reservation_object *obj,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_reservation.c:375:1: warning: ‘reservation_object_add_shared_inplace’ defined but not used [-Wunused-function]
 reservation_object_add_shared_inplace(struct reservation_object *obj,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_mm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_kms.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_atombios.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/atombios_crtc.o
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_pci.c: In function ‘amdkcl_pci_init’:
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_pci.c:257:83: warning: passing argument 2 of ‘amdkcl_fp_setup’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
  _kcl_pcie_link_speed = (const unsigned char *) amdkcl_fp_setup("pcie_link_speed",_kcl_pcie_link_speed_stub);
                                                                                   ^~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_pci.c:3:0:
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/kcl_common.h:22:21: note: expected ‘void *’ but argument is of type ‘const unsigned char *’
 static inline void *amdkcl_fp_setup(const char *symbol, void *fp_stup)
                     ^~~~~~~~~~~~~~~
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_connectors.o
/var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_memory.c:29:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.5-27/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.5-27/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:285:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/atom.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_fence.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_ttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_object.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_gart.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_display.o
  LD [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdkcl/amdkcl.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_fb.o
/var/lib/dkms/amdgpu/2.5-27/build/ttm/ttm_agp_backend.c:33:0: warning: "pr_fmt" redefined
 #define pr_fmt(fmt) "[TTM] " fmt
 
In file included from ./include/linux/kernel.h:14:0,
                 from ./include/linux/list.h:9,
                 from ./include/linux/wait.h:7,
                 from ./include/linux/dma-fence.h:25,
                 from /var/lib/dkms/amdgpu/2.5-27/build/include/kcl/kcl_fence.h:12,
                 from /var/lib/dkms/amdgpu/2.5-27/build/ttm/backport/backport.h:5,
                 from <command-line>:0:
./include/linux/printk.h:285:0: note: this is the location of the previous definition
 #define pr_fmt(fmt) fmt
 
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_gem.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_ring.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_cs.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_bios.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_benchmark.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_test.o
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_device.c: In function ‘amdgpu_device_get_pcie_info’:
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_device.c:3798:2: error: implicit declaration of function ‘pcie_bandwidth_available’; did you mean ‘pci_aer_available’? [-Werror=implicit-function-declaration]
  pcie_bandwidth_available(adev->pdev, NULL,
  ^~~~~~~~~~~~~~~~~~~~~~~~
  pci_aer_available
  LD [M]  /var/lib/dkms/amdgpu/2.5-27/build/scheduler/amd-sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_pm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/atombios_dp.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_afmt.o
  LD [M]  /var/lib/dkms/amdgpu/2.5-27/build/ttm/amdttm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_trace_points.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/atombios_encoders.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_sa.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/atombios_i2c.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_dma_buf.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_vm.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_ib.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_pll.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_ucode.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_bo_list.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_ctx.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_sync.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_gtt_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_vram_mgr.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_virt.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_atomfirmware.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_vf_error.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_sched.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_debugfs.o
  CC [M]  /var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_ids.o
cc1: some warnings being treated as errors
scripts/Makefile.build:324: recipe for target '/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_device.o' failed
make[2]: *** [/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_device.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu/amdgpu_dma_buf.c:144:1: warning: ‘__reservation_object_make_exclusive’ defined but not used [-Wunused-function]
 __reservation_object_make_exclusive(struct reservation_object *obj)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
scripts/Makefile.build:583: recipe for target '/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/2.5-27/build/amd/amdgpu] Error 2
Makefile:1529: recipe for target '_module_/var/lib/dkms/amdgpu/2.5-27/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/2.5-27/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.15.18-041518-generic'

---

### 评论 #15 — kentrussell (2019-07-05T11:01:52Z)

Peculiar, that issue should be fixed in 2.5 (actually, it got fixed in 2.4). Do you have a requirement of using the DKMS package? There is always the option to compile the kernel from the source code as a monolithic kernel and installing it that way, ensuring that you get the ROCm code without DKMS. I've been using it on 18.04 without issue, though it is based on 5.0-rc1, not 4.15/4.18, so I don't know if that's an issue or not. But I don't know why that would be failing there since we have that fix in the 2.4/2.5 branches, it doesn't make sense since the patch to fix the code is in there. I can try to dig around a bit more, but 2.6 is coming soon as well, so we can always try that if the monolithic kernel isn't working, or isn't an option.

---

### 评论 #16 — witeko (2019-07-06T13:51:01Z)

@kentrussell thx for reply, can You give me some guidance on "There is always the option to compile the kernel from the source code as a monolithic kernel and installing it that way, ensuring that you get the ROCm code without DKMS"? :)

---

### 评论 #17 — kentrussell (2019-07-08T16:48:51Z)

Copy arch/x86/configs/rock-rel_defconfig to the top kernel directory and rename it ".config" without the quotes, then do "make bindeb-pkg" to build it. Install the resulting linux-headers and linux-image package and you should be good. You might need to extract the firmware from the dkms package and copy them into /lib/firmware/amdgpu manually, but thats step 2 , after trying the monolithic build. 2.6 should be out this week if you want to wait for that too, as an FYI.

---

### 评论 #18 — witeko (2019-07-08T21:26:18Z)

@kentrussell TY :)
I will try to check the monolithic approach in my free time. :)
And I will also try the 2.6 : )

---

### 评论 #19 — witeko (2019-07-09T19:29:28Z)

@kentrussell looks like the rocm 2.6 solved my problem. I checked only with 4.18 for now.
If You won't close the ticket just yet I can check other kernels, and scenarios. :)
Thank You for your help. :)

---

### 评论 #20 — witeko (2019-07-13T17:43:34Z)

4.18 kernel is still the only one I can use. but its fine for now. :)
TY :)

---
