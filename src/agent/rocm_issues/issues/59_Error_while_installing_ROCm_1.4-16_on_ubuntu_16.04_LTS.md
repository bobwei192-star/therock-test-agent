# Error while installing ROCm 1.4-16 on ubuntu 16.04 LTS:

> **Issue #59**
> **状态**: closed
> **创建时间**: 2016-12-22T18:56:45Z
> **更新时间**: 2017-01-05T00:02:47Z
> **关闭时间**: 2017-01-04T23:01:44Z
> **作者**: utopiabhsg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/59

## 描述

Im trying to install ROCm 1.4-16 on my machine with Ubuntu 16.04. The system is a AMD APU with intergrated GPU. I received the following error message during installation.
ERROR (dkms apport): kernel package linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16 is not supported
Error! Bad return status for module build on kernel: 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64).
I have attached the corresponding log file as .txt file

[makelog.txt](https://github.com/RadeonOpenCompute/ROCm/files/669587/makelog.txt)
Any pointers to what may be wrong and how to fix this issue is much appreciated.

Thanks in advance! 

Log file Details:

DKMS make.log for amdgpu-pro-16.50-362463 for kernel 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64)
Wed Dec 21 12:24:03 PST 2016
make: Entering directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'
  LD      /var/lib/dkms/amdgpu-pro/16.50-362463/build/built-in.o
  LD      /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/built-in.o
  CC [M]  /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_reserve’:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:116:9: error: too many arguments to function ‘ttm_bo_reserve’
  return ttm_bo_reserve(bo, interruptible, no_wait, false, ticket);
         ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:877:19: note: declared here
 static inline int ttm_bo_reserve(struct ttm_buffer_object *bo,
                   ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_move_accel_cleanup’:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:153:11: error: incompatible type for argument 4 of ‘ttm_bo_move_accel_cleanup’
    evict, no_wait_gpu, new_mem);
           ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:1046:12: note: expected ‘struct ttm_mem_reg *’ but argument is of type ‘bool {aka _Bool}’
 extern int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo,
            ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:152:9: error: too many arguments to function ‘ttm_bo_move_accel_cleanup’
  return ttm_bo_move_accel_cleanup(bo, fence,
         ^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:1046:12: note: declared here
 extern int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo,
            ^
scripts/Makefile.build:291: recipe for target '/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o' failed
make[2]: *** [/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o] Error 1
scripts/Makefile.build:440: recipe for target '/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu] Error 2
Makefile:1428: recipe for target '_module_/var/lib/dkms/amdgpu-pro/16.50-362463/build' failed
make: *** [_module_/var/lib/dkms/amdgpu-pro/16.50-362463/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'


---

## 评论 (24 条)

### 评论 #1 — gstoner (2016-12-22T23:02:34Z)

In the System BIOS is IOMMUv2 turned on.    What is make and model of the system your are on.

Greg
On Dec 22, 2016, at 12:56 PM, bhsomegowda <notifications@github.com<mailto:notifications@github.com>> wrote:


Im trying to install ROCm 1.4-16 on my machine with Ubuntu 16.04. The system is a AMD APU with intergrated CARIZZO GPU. I received the following error message during installation.
ERROR (dkms apport): kernel package linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16 is not supported
Error! Bad return status for module build on kernel: 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64).
I have attached the corresponding log file as .txt file

makelog.txt<https://github.com/RadeonOpenCompute/ROCm/files/669587/makelog.txt>
Any pointers to what may be wrong and how to fix this issue is much appreciated.

Thanks in advance!

Log file Details:

DKMS make.log for amdgpu-pro-16.50-362463 for kernel 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64)
Wed Dec 21 12:24:03 PST 2016
make: Entering directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'
LD /var/lib/dkms/amdgpu-pro/16.50-362463/build/built-in.o
LD /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/built-in.o
CC [M] /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
from :0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_reserve’:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:116:9: error: too many arguments to function ‘ttm_bo_reserve’
return ttm_bo_reserve(bo, interruptible, no_wait, false, ticket);
^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
from :0:
include/drm/ttm/ttm_bo_driver.h:877:19: note: declared here
static inline int ttm_bo_reserve(struct ttm_buffer_object *bo,
^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
from :0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_move_accel_cleanup’:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:153:11: error: incompatible type for argument 4 of ‘ttm_bo_move_accel_cleanup’
evict, no_wait_gpu, new_mem);
^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
from :0:
include/drm/ttm/ttm_bo_driver.h:1046:12: note: expected ‘struct ttm_mem_reg *’ but argument is of type ‘bool {aka _Bool}’
extern int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo,
^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5:0,
from :0:
/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:152:9: error: too many arguments to function ‘ttm_bo_move_accel_cleanup’
return ttm_bo_move_accel_cleanup(bo, fence,
^
In file included from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
from /var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/../backport/backport.h:5,
from :0:
include/drm/ttm/ttm_bo_driver.h:1046:12: note: declared here
extern int ttm_bo_move_accel_cleanup(struct ttm_buffer_object *bo,
^
scripts/Makefile.build:291: recipe for target '/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o' failed
make[2]: *** [/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu/amdgpu_drv.o] Error 1
scripts/Makefile.build:440: recipe for target '/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu-pro/16.50-362463/build/amd/amdgpu] Error 2
Makefile:1428: recipe for target 'module/var/lib/dkms/amdgpu-pro/16.50-362463/build' failed
make: *** [module/var/lib/dkms/amdgpu-pro/16.50-362463/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/59>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DucLMaFuyrGhNNh350f_FKmMnyOudks5rKsfugaJpZM4LURxO>.



---

### 评论 #2 — utopiabhsg (2016-12-22T23:27:55Z)

Hi Greg,
The system is AMD Embedded R-Series RX-421BD Radeon R7 (Merlin Falcon) embedded SOC.
In the BIOS i saw only IOMMU (not IOMMUv2). I enabled both IOMMU and SVM options in the BIOS.
I'm attaching output of OpenCL clinfo application here: 
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/670042/clinfo.txt)
Let me know if you need more information.

Thanks,
bhsomegowda 


---

### 评论 #3 — gstoner (2016-12-22T23:46:08Z)

Merlin Falcon has it own Device ID,   we are currently not supporting Merlin Falcon with our public open source versions of ROCm  1.4.   I would get with you AMD Embedded Application Engineer and work with them on this issue.

Greg


On Dec 22, 2016, at 5:27 PM, bhsomegowda <notifications@github.com<mailto:notifications@github.com>> wrote:


Hi Greg,
The system is AMD Embedded R-Series RX-421BD Radeon R7 (Merlin Falcon) embedded SOC.
In the BIOS i saw only IOMMU (not IOMMUv2). I enabled both IOMMU and SVM options in the BIOS.
I'm attaching output of OpenCL clinfo application here:
clinfo.txt<https://github.com/RadeonOpenCompute/ROCm/files/670042/clinfo.txt>
Let me know if you need more information.

Thanks,
bhsomegowda

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/59#issuecomment-268913405>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSBXp2fkqa85yi2urButbRgD9JAWks5rKwd8gaJpZM4LURxO>.



---

### 评论 #4 — utopiabhsg (2016-12-23T00:21:25Z)

How do i get the Device ID of my embedded SOC board? Also, how do i get in touch with an AMD Embedded Application Engineer to solve this problem?

-bhsomegowda

---

### 评论 #5 — gstoner (2016-12-23T00:47:58Z)

Where did you buy the board from.

greg
On Dec 22, 2016, at 6:21 PM, bhsomegowda <notifications@github.com<mailto:notifications@github.com>> wrote:


How do i get the Device ID of my embedded SOC board? Also, how do i get in touch with an AMD Embedded Application Engineer to solve this problem?

-bhsomegowda

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/59#issuecomment-268919656>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZTlKXue9hisFKPH6BznMbWp7f3kks5rKxQFgaJpZM4LURxO>.



---

### 评论 #6 — utopiabhsg (2016-12-23T01:39:27Z)

We purchased the Merlin falcon board from SECO USA Inc.


---

### 评论 #7 — PolarNick239 (2017-01-02T20:05:10Z)

+1

I did as described [here](https://radeonopencompute.github.io/install.html):

1. wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
2. sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
3. sudo apt-get update
4. sudo apt-get install rocm

And got this:
```
...
...
igdrcl: using XCB-DRI2 authentication...
Successfully created the counter files
Setting up hip_hcc (1.0.16503) ...
Setting up hip_samples (1.0.16503) ...
Setting up linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16 (4.6.0-kfd-compute-rocm-rel-1.4-16-1) ...
Setting up linux-image-4.6.0-kfd-compute-rocm-rel-1.4-16 (4.6.0-kfd-compute-rocm-rel-1.4-16-1) ...
ERROR (dkms apport): kernel package linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16 is not supported
Error! Bad return status for module build on kernel: 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64)
Consult /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/make.log for more information.
update-initramfs: Generating /boot/initrd.img-4.6.0-kfd-compute-rocm-rel-1.4-16
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.6.0-kfd-compute-rocm-rel-1.4-16
Found initrd image: /boot/initrd.img-4.6.0-kfd-compute-rocm-rel-1.4-16
Found linux image: /boot/vmlinuz-4.4.0-57-generic
Found initrd image: /boot/initrd.img-4.4.0-57-generic
Found linux image: /boot/vmlinuz-4.4.0-45-generic
Found initrd image: /boot/initrd.img-4.4.0-45-generic
Found Windows Boot Manager on /dev/sda2@/EFI/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for EFI firmware configuration
done
Setting up llvm-amdgpu (3.9.dev) ...
Setting up rocm-smi (1.0.3) ...
Setting up rocm-dev (1.4.0) ...
Setting up rocm-kernel (1.4.0) ...
KERNEL=="kfd", MODE="0666"
Setting up rocm (1.4.0) ...
Processing triggers for libc-bin (2.23-0ubuntu3) ...
```

Log (/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/make.log):
```
DKMS make.log for amdgpu-pro-16.30.3-306809 for kernel 4.6.0-kfd-compute-rocm-rel-1.4-16 (x86_64)
Пн янв  2 22:25:35 MSK 2017
make: Entering directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'
  LD      /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/built-in.o
  LD      /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/built-in.o
  CC [M]  /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/amdgpu_drv.o
In file included from /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/../backport/backport.h:9:0,
                 from <command-line>:0:
/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h: In function ‘kcl_ttm_bo_reserve’:
/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:88:9: error: too many arguments to function ‘ttm_bo_reserve’
  return ttm_bo_reserve(bo, interruptible, no_wait, false, ticket);
         ^
In file included from /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/../backport/include/kcl/kcl_ttm.h:6:0,
                 from /var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/../backport/backport.h:9,
                 from <command-line>:0:
include/drm/ttm/ttm_bo_driver.h:877:19: note: declared here
 static inline int ttm_bo_reserve(struct ttm_buffer_object *bo,
                   ^
scripts/Makefile.build:291: recipe for target '/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/amdgpu_drv.o' failed
make[2]: *** [/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu/amdgpu_drv.o] Error 1
scripts/Makefile.build:440: recipe for target '/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu-pro/16.30.3-306809/build/amd/amdgpu] Error 2
Makefile:1428: recipe for target '_module_/var/lib/dkms/amdgpu-pro/16.30.3-306809/build' failed
make: *** [_module_/var/lib/dkms/amdgpu-pro/16.30.3-306809/build] Error 2
make: Leaving directory '/usr/src/linux-headers-4.6.0-kfd-compute-rocm-rel-1.4-16'
```

P.S. Ubuntu 16.04 LTS, R9 390X

---

### 评论 #8 — gstoner (2017-01-04T03:33:29Z)

@PolarNick239 What CPU are you using with R9 390, if it is Intel CPU Haswell or newer what PCIe slot is it in.   Please check our link for what hardware is supported https://rocm.github.io/hardware.html 

---

### 评论 #9 — PolarNick239 (2017-01-04T09:16:45Z)

i7 6700 (skylake), PCIe is 3.0 (as I read [here](http://ark.intel.com/products/88196/Intel-Core-i7-6700-Processor-8M-Cache-up-to-4_00-GHz)), so as I see - my hardware should be supported

I just want to hipify some CUDA code, am I right that for AMD hardware I really need to install ROCm and run my OS with custom kernel? But this is needed only for compilation, but not for runtime, right?

---

### 评论 #10 — gstoner (2017-01-04T13:47:18Z)

That helps,  one thing we need to make sure all your GPU are in PCIe Gen3 slots directly attach to CPU PCIe Root I/O complex for the Fiji GPU's,   What motherboard are you using.  If you could just use the two fiji first in true x16 lanes.  Then we go from here add back in the Hawaii cards.   Do you have Supermicro system model number as well.  We work with this team closely.


One big difference with ROCm and AMDRadeon Pro  is in ROCm we have native ISA  compiler which generate specific binaries for give GPU Class  here you need to be specific about which GPU you execute a kernel.   We are working on Fat binary system to allow you to pre compile for Hawaii and Fiji and loader pull the correct binary for the card.   With AMDRadeon Pro we had High level IL


This is good are document to understand this
- https://github.com/RadeonOpenCompute/hcc/wiki#how-to-use-hcc
- https://github.com/RadeonOpenCompute/ROCm-ComputeABI-Doc/blob/master/AMDGPU-ABI.md

Greg


On Jan 4, 2017, at 3:16 AM, Nikolay Polyarniy <notifications@github.com<mailto:notifications@github.com>> wrote:


i7 6700 (skylake), PCIe is 3.0 (as I read here<http://ark.intel.com/products/88196/Intel-Core-i7-6700-Processor-8M-Cache-up-to-4_00-GHz>), so as I see - my hardware should be supported

I just want to hipify some CUDA code, am I right that for AMD hardware I really need to install ROCm and run my OS with custom kernel? But this is needed only for compilation, but not for runtime, right?

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/59#issuecomment-270326721>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubD6REJclfHnxWbWLlb_jGwkRDNSks5rO2N9gaJpZM4LURxO>.



---

### 评论 #11 — gstoner (2017-01-04T13:54:15Z)

Nikolay Polyarniy @PolarNick239   I was working on the similar issue with Four GPU in Supermicro system.  Please still check to make sure the GPU's  are in the correct PCIe Lanes.   Also what motherboard are you on. 


---

### 评论 #12 — PolarNick239 (2017-01-04T15:46:37Z)

@gstoner My motherboard is MSI Z170A SLI (I am testing on simple home computer). I am incompetent in hardware, so I can give you wrong information, but I am quite sure, that my R9 390X is in correct slot, because:
- all three slots in my motherboard (MSI Z170A SLI) are PCI-E x16 (I use the top slot)
- I use this single GPU for OpenCL computing and gaming successfully

Is there any way to check PCI-E slot from OS? (maybe some application with hardware information, I have windows on this computer too, so application for Linux/Windows is ok)

Also, I don't understand how can it correlate with compilation failure of rocm package? How can it be dependent on hardware at apt-get stage?

---

### 评论 #13 — gstoner (2017-01-04T16:34:35Z)


This helps.  I looked in the manual can you check to see if your GPU is in PCI_E2 Slot: PCIe 3.0 x16 slot

If you do two gpu’s you need have your GPU in PCI_E2 and  PCI_E4: PCIe 3.0,  but you get PCIe Gen3  x8 performance on both GPU.

Did you have clean Ubuntu install.


greg

On Jan 4, 2017, at 9:46 AM, Nikolay Polyarniy <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> My motherboard is MSI Z170A SLI (I am testing on simple home computer). I am incompetent in hardware, so I can give you wrong information, but I am quite sure, that my R9 390X is in correct slot, because:

  *   all three slots in my motherboard (MSI Z170A SLI) are PCI-E x16 (I use the top slot)
  *   I use this single GPU for OpenCL computing and gaming successfully

Is there any way to check PCI-E slot from OS? (maybe some application with hardware information, I have windows on this computer too, so application for Linux/Windows is ok)

Also, I don't understand how can it correlate with compilation of rocm package failure? How can it be dependent on hardware at apt-get stage?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/59#issuecomment-270403333>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Dueb-rMEx2OvtvTMMsIX3yelCOxBgks5rO77dgaJpZM4LURxO>.



---

### 评论 #14 — utopiabhsg (2017-01-04T19:02:24Z)

Inspite of the error i mentioned in my first post while installing, when i run vector_copy sample, it gives me all success messages.I git cloned hcc examples applications from the git page, installed CLOC 1.3.1. When i execute the binaries in HCC examples applications and CLOC examples/snack or CLOC examples/hsa, the first few binaries(typically first 3 executions of any binaries) of HCC/CLOC examples execute and gives the output. Further when i try to execute the other binaries, it segfaults. Once any of the binaries segfaults, all the binaries which executed and gave the output previously segfaults too including the vector_copy sample.

I have exported /opt/rocm/bin to PATH and /opt/rocm/lib to LD_LIBRARY_PATH in my .bashrc file. And i have provided --amdgpu-target=AMD:AMDGPU:8:0:1 (My APU is Carrizo) in the command when im compiling HCC applications(saxpy.cpp hcc application from git page) like so:

1. hcc `hcc-config --cxxflags --ldflags` --amdgpu-target=AMD:AMDGPU:8:0:1 saxpy.cpp -o saxpy
or
2. hcc `hcc-config --cxxflags` saxpy.cpp -c -o saxpy.cpp.o
    hcc `hcc-config --ldflags` --amdgpu-target=AMD:AMDGPU:8:0:1 saxpy.cpp.o -o saxpy    

i did put hcc-config --cxxflags --ldflags , hcc-config --cxxflags , hcc-config --ldflags in between the two backticks.

My question is why it compiles and executes fine for first 2 or 3 binaries and segfaults later on? Any thoughts on why this is happening? please point out if I'm missing anything.

Thanks  

---

### 评论 #15 — PolarNick239 (2017-01-04T19:13:37Z)

@gstoner yes, it is in PCI_E2.

This Ubuntu I use everyday, so it is not clean, but this is compilation error - so I don't think the problem is in my environment.

I am intrested in how hardware can affect compilation? Or you just want to ensure that my hardware is supported? But anyway - what's wrong with compilation?

---

### 评论 #16 — scchan (2017-01-04T19:18:57Z)

@bhsomegowda  Do you mean if you keep running the hcc saxpy example only, it would fail after 3-4 executions?

---

### 评论 #17 — gstoner (2017-01-04T19:29:24Z)



Nikolay Polyarniy

After you rebooted the systems did you verify the system.

Verify Installation

To verify that the ROCm stack completed successfully you can execute to HSA vectory_copy sample application (we do recommend that you copy it to a separate folder and invoke make therein):

cd /opt/rocm/hsa/sample
make
./vector_copy


On Jan 4, 2017, at 1:18 PM, Siu Chi Chan <notifications@github.com<mailto:notifications@github.com>> wrote:

@bhsomegowda<https://github.com/bhsomegowda>



---

### 评论 #18 — utopiabhsg (2017-01-04T19:29:47Z)

@scchan not just with saxpy, i encounter this problem when i run other HCC /CLOC samples as well. Say I'm running HCC example applications, after building using cmake, i run the binary ./ArrayBandwidth - i get the output, i run ./HCFFT - i get the ouput, when i try to run ./MD - it Segfaults. when i run ./ArrayBandwidth or ./HCFFT or ./Vector_copy (under /opt/rocm/hsa/samples) all segfaults.  

Sometimes rebooting the system helps to get output to the binaries and again after executing of few binaries, the same issue comes up. But rebooting doesn't always help. Most of the times even after reboot when i try to execute the binaries it segfaults.

---

### 评论 #19 — scchan (2017-01-04T19:38:46Z)

@bhsomegowda Once you hit a segfault, it's possible that the driver get into a bad state requiring a reboot.  

I'd like to understand whether the 1st occurrence of a sefault is reproducible with *any* binary or only with MD.  That would help us to narrow down where the problem is.  

So if you keep running only saxpy multiple times, do you observe the segfault?

Then starting your machine from a clean state, would MD segfault right the way the 1st time you run it?



---

### 评论 #20 — scchan (2017-01-04T19:41:49Z)

@bhsomegowda  When you compile hcfft, MD and other CLOC samples, did you also add the amdgpu-target for CZ?

---

### 评论 #21 — utopiabhsg (2017-01-04T19:46:04Z)

Yes i have added the amdgpu-target in the CMakeList.txt file of the HCC-examples-applications. And while running CLOC samples i have added the option -mcpu carrizo option in the snack.sh -c hw.cl/csquares.cl/vector_copy like so:
snack.sh -c -mcpu carrizo hw.cl 

---

### 评论 #22 — utopiabhsg (2017-01-04T20:35:00Z)

I rebooted into the system and did the below steps.

1. I rebooted the system, i cd'ed into /opt/rocm/hsa/samples, typed the command sudo make and executed the binary. I got the output with all success messages. 
2. After ./vector_copy, i ran saxpy.cpp example, it segfaulted in the first run. 
3. I again ran ./vector_copy - it segfaults.
4. I recompiled saxpy.cpp and ran the binary. it segfaults. 

Tried running ./ArrayBandwidth and ./HCFFT on reboot - they segfaulted as well
So i believe, the first Segfault is reproducible by any binary on reboot. Except the vector_copy samples compiles and runs fine if i run it the first thing immediately after rebooting. But again, once any of the HCC/CLOC binary hits segfault, ./vector_copy segfaults too.

Let me know if you need more information about my system or my environment.

PS:I tried attaching the images(.png format), they wont open here. 
 

---

### 评论 #23 — gstoner (2017-01-04T23:01:44Z)

Merlin Falcon as I said currently does not work with ROCm 1.3 and 1.4, this system has been extensively tested internally, the embedded team will need to follow up with you. 

---

### 评论 #24 — utopiabhsg (2017-01-05T00:02:47Z)

Can you please point me to an embedded team member who could help me with this issue? Also, will ROCm be supported on Merlin Falcon any time in the near future? 

---
