# [Issue]: Ubuntu 24.04 install of Rocm 6.2.xxx fails

- **Issue #:** 3762
- **State:** closed
- **Created:** 2024-09-19T23:13:39Z
- **Updated:** 2024-09-20T17:39:39Z
- **Labels:** AMD Radeon Pro W7900, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3762

### Problem Description

I followed the quick-install steps on a fresh install of Ubuntu 24.04 desktop. I have a Ryzen 3700x CPU and a Radeon Pro W7900. I followed these instructions: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html

It seems that the installation is failing when trying to compile the kernel module(s):

ProblemType: Package
DKMSBuildLog:
 DKMS make.log for amdgpu-6.8.5-2009582.24.04 for kernel 6.8.0-45-generic (x86_64)
 Thu Sep 19 05:54:57 PM CDT 2024
 make: Entering directory '/usr/src/linux-headers-6.8.0-45-generic'
 warning: the compiler differs from the one used to build the kernel
   The kernel was built by: x86_64-linux-gnu-gcc-13 (Ubuntu 13.2.0-23ubuntu4) 13.2.0
   You are using:           gcc-13 (Ubuntu 13.2.0-23ubuntu4) 13.2.0
   CC [M]  /tmp/amd.chrxdkMD/scheduler/sched_main.o
   CC [M]  /tmp/amd.chrxdkMD/scheduler/sched_fence.o
   CC [M]  /tmp/amd.chrxdkMD/scheduler/sched_entity.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdxcp/amdgpu_xcp_drv.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdxcp/./backport/kcl_drm_drv.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_tt.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_bo.o
   CC [M]  /tmp/amd.chrxdkMD/drm_gem_ttm_helper.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_bo_util.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_bo_vm.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_module.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/main.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_execbuf_util.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_range_manager.o
   CC [M]  /tmp/amd.chrxdkMD/drm_buddy.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdgpu/amdgpu_drv.o
 /tmp/amd.chrxdkMD/amd/amdkcl/main.c:17:12: warning: no previous prototype for ‘amdkcl_init’ [-Wmissing-prototypes]
    17 | int __init amdkcl_init(void)
       |            ^~~~~~~~~~~
 /tmp/amd.chrxdkMD/amd/amdkcl/main.c:35:13: warning: no previous prototype for ‘amdkcl_exit’ [-Wmissing-prototypes]
    35 | void __exit amdkcl_exit(void)
       |             ^~~~~~~~~~~
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_common.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_kernel_params.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_resource.o
   LD [M]  /tmp/amd.chrxdkMD/amd/amdxcp/amdxcp.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/dma-buf/dma-resv.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdgpu/amdgpu_device.o
 /tmp/amd.chrxdkMD/amd/amdkcl/kcl_common.c:30:6: warning: no previous prototype for ‘amdkcl_symbol_init’ [-Wmissing-prototypes]
    30 | void amdkcl_symbol_init(void)
       |      ^~~~~~~~~~~~~~~~~~
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_pool.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_backlight.o
   LD [M]  /tmp/amd.chrxdkMD/amddrm_buddy.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_ioctl.o
   LD [M]  /tmp/amd.chrxdkMD/amddrm_ttm_helper.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdgpu/amdgpu_doorbell_mgr.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_device.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_kthread.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_sys_manager.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdgpu/amdgpu_kms.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_io.o
   CC [M]  /tmp/amd.chrxdkMD/ttm/ttm_agp_backend.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_seq_file.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdgpu/amdgpu_atombios.o
   CC [M]  /tmp/amd.chrxdkMD/amd/amdkcl/kcl_suspend.o
 /tmp/amd.chrxdkMD/amd/amdkcl/kcl_suspend.c:32:6: warning: no previous prototype for ‘amdkcl_suspend_init’ [-Wmissing-prototypes]
    32 | void amdkcl_suspend_init(void)
       |      ^~~~~~~~~~~~~~~~~~~
 /tmp/amd.chrxdkMD/amd/amdkcl/kcl_io.c:69:6: warning: no previous prototype for ‘amdkcl_io_init’ [-Wmissing-prototypes]


### Operating System

Ubuntu 24.04.1 LTS (Noble Numbat)

### CPU

AMD Ryzen 7 3700x 8-Core Processor

### GPU

AMD Radeon Pro W7900

### ROCm Version

ROCm 6.2.0

### ROCm Component

ROCm

### Steps to Reproduce

1. Install Ubuntu 24.04 desktop onto a computer as the only operating system.
2. Follow the steps detailed on https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html
3. Observe error installing amdgpu-dkms.
4. Look at the file /var/crash/amdgpu-dkms.0.crash for details

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

This program cannot be run because the install failed:

### Additional Information

$uname -a
Linux radeonpro 6.8.0-45-generic #45-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug 30 12:02:04 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

$cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04.1 LTS"

$ cat /proc/cpuinfo

vendor_id	: AuthenticAMD
cpu family	: 23
model		: 113
model name	: AMD Ryzen 7 3700X 8-Core Processor
stepping	: 0
microcode	: 0x8701021
cpu MHz		: 2124.398
cache size	: 512 KB
physical id	: 0
siblings	: 16
core id		: 7
cpu cores	: 8
apicid		: 15
initial apicid	: 15
fpu		: yes
fpu_exception	: yes
cpuid level	: 16
wp		: yes