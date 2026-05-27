# RX580 Call returned 4104

> **Issue #783**
> **状态**: closed
> **创建时间**: 2019-04-30T03:14:12Z
> **更新时间**: 2023-12-18T18:55:36Z
> **关闭时间**: 2023-12-18T18:55:35Z
> **作者**: tu6ge
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/783

## 描述

Two months ago, I purchased RX580 GPU, which was planned to be used for machine learning to speed up computing. But when I installed it, I encountered some problems. I just started to ask for help on GitHub and got good support. I said that my PCI model was not supported. Then I added the PCI model according to the tips on github. Later, rocm2.2 version had some problems, saying that it was incompatible with Linux kernel 4.18. But my computer is 4.15 core, or not, until the ROCM 2.3 version, found that the problem is still not solved, the current rocm-smi can display graphics card data, but rocminfo error, I have waited for a long time, tried various methods, also changed the Linux kernel several times during the docker has tried.

There's something wrong with the new version.

```
tu6ge@tu6ge-desktop:~$ rocminfo 
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104
```
my computer`s info :
```
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ uname -a
Linux tu6ge-desktop 4.15.0-041500-generic #201802011154 SMP Thu Feb 1 11:55:45 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
tu6ge@tu6ge-desktop:~$ groups
tu6ge adm cdrom sudo dip video plugdev lpadmin sambashare
tu6ge@tu6ge-desktop:~$ uname -r
4.15.0-041500-generic
tu6ge@tu6ge-desktop:~$ dkms status
amdgpu, 2.3-14, 4.15.0-041500-generic, x86_64: installed
virtualbox, 5.2.18, 4.15.0-041500-generic, x86_64: installed
tu6ge@tu6ge-desktop:~$ modinfo amdgpu | grep filename
filename:       /lib/modules/4.15.0-041500-generic/updates/dkms/amdgpu.ko
tu6ge@tu6ge-desktop:~$ modinfo amdkfd | grep filename
filename:       /lib/modules/4.15.0-041500-generic/kernel/drivers/gpu/drm/amd/amdkfd/amdkfd.ko
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
tu6ge@tu6ge-desktop:~$ dmesg | grep amd
[   11.055816] amdkcl: loading out-of-tree module taints kernel.
[   11.055833] amdkcl: module verification failed: signature and/or required key missing - tainting kernel
[   11.615325] [drm] amdgpu kernel modesetting enabled.
[   11.615326] [drm] amdgpu version: 5.0.19.20.6
[   12.320874] fb: switching to amdgpudrmfb from EFI VGA
[   12.321506] amdgpu 0000:01:00.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0xffff
[   12.772981] amdgpu 0000:01:00.0: VRAM: 8192M 0x000000F400000000 - 0x000000F5FFFFFFFF (8192M used)
[   12.772983] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   12.773139] [drm] amdgpu: 8192M of VRAM memory ready
[   12.773141] [drm] amdgpu: 8192M of GTT memory ready.
[   13.362648] fbcon: amdgpudrmfb (fb0) is primary device
[   13.401764] amdgpu 0000:01:00.0: fb0: amdgpudrmfb frame buffer device
[   13.432512] [drm] Initialized amdgpu 3.31.0 20150101 for 0000:01:00.0 on minor 0
```


---

## 评论 (23 条)

### 评论 #1 — kentrussell (2019-05-09T19:54:32Z)

It could be that rocminfo or the runtime don't support that chipId. Try the 2.4 release and see if it's still happening. If the SMI ran and gave results beyond a bunch of "N/A" responses, then the kernel is supporting the chip, it's just the runtime that isn't supporting it. By virtue of the ROCT not having that Chip ID in its topology, that would also be a bit of a problem.

---

### 评论 #2 — tu6ge (2019-05-10T02:04:39Z)

Where can I see the notification of version upgrade?



---

### 评论 #3 — tu6ge (2019-05-10T02:08:48Z)

I added this PCI into `topology.c` file.the Chip ID is another？

---

### 评论 #4 — kentrussell (2019-05-10T10:23:49Z)

If you still have the apt information saved on your system, "apt update" should retrieve the metadata, and then you can just install it again as you did before.
Chip ID is the PCI. But if rocrinfo doesn't have it in there as well, you'll keep hitting these roadblocks. They also list their supported ASICs in their header. If it still doesn't work, I'd raise an issue in the ROCr section specifically, since they're more likely to see it and reply quicker (the generic ROCm bug report is a catch-all, using the specific repo for what's broken tends to give results quicker).

---

### 评论 #5 — Djip007 (2019-05-11T12:00:49Z)

look like "6fdf" ID is steel missing on 2.4 release
https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.4.x/src/topology.c#L161

for kernel 4.18... it is not 100% clear (for me...) if it work with rocm 2.4... for me it work only without dkms 
I can read : https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels
Using AMD's rock-dkms package  => Not currently supported on kernels newer than 4.18

and main kernel (5.1) missing to:
https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/gpu/drm/amd/amdkfd/kfd_device.c?h=linux-5.1.y#n357
or 4.18
https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/gpu/drm/amd/amdkfd/kfd_device.c?h=linux-4.18.y#n276

no even on 5.2 drm next...
https://cgit.freedesktop.org/~agd5f/linux/tree/drivers/gpu/drm/amd/amdkfd/kfd_device.c?h=drm-next-5.2#n357

---

### 评论 #6 — kentrussell (2019-05-13T12:49:36Z)

It looks like amdgpu has the basic support for it. It looks like amdgpu added the GPU ID later on, but the KFD/Thunk didn't get the updated list, which is the reason why the support isn't there. I'll fix that now to add the missing GPU ID.

But there will still need to be work done in the runtime to support it as well. Once you see it in KFD/Thunk(ROCT), then you can raise a bug issue with the ROCR team specifically (if rocrinfo doesn't work), since they're faster to respond to issues on there rather than the generic ROCm bucket

---

### 评论 #7 — tu6ge (2019-05-13T13:10:23Z)

I added `6fdf` into `topology.c` ,and Perform the following steps
```
mkdir -p build
    cd build
    cmake ..
    make
cp libhsakmt.so.2.3.0 /opt/rocm/lib/libhsakmt.so.2.3.0
cd /opt/rocm/lib
ln -s libhsakmt.so.2.3.0 libhsakmt.so.2
ln -s libhsakmt.so.2 libhsakmt.so
sudo dkms remove amdgpu/2.3-14 --all
sudo dkms add amdgpu/2.3-14
sudo dkms install amdgpu/2.3-14
```
reboot , but the problem remains unsolved.


---

### 评论 #8 — kentrussell (2019-05-13T13:12:00Z)

Try adding the ID to the run_kfdtest.sh script as well (just add "| 6fdf" after 67df), and see if KFDTest works. If it works, that means that the kernel is good, and that runtime will need to add the ID to their list as well. It was a late addition to the Polaris10 list of IDs, so they might not have seen it getting added (hence how KFD missed it too). 

---

### 评论 #9 — tu6ge (2019-05-13T13:14:05Z)

```
tu6ge@tu6ge-desktop:~$ dmesg | grep kfd
[   13.360582] kfd kfd: Allocated 3969056 bytes on gart
[   13.361135] kfd kfd: added device 1002:6fdf
```
KFD is not missed it

---

### 评论 #10 — tu6ge (2019-05-13T13:16:58Z)

where is `run_kfdtest.sh`

---

### 评论 #11 — kentrussell (2019-05-13T13:18:08Z)

It's in the ROCT project under tests/kfdtest . It's our test that tests kernel functionality. In the meantime, I am talking to one of the guys who works on rocminfo to see if we can get that updated as well.

---

### 评论 #12 — Djip007 (2019-05-13T23:58:31Z)

same for me.. but realy strange...
4104 = 0x1008 => HSA_STATUS_ERROR_OUT_OF_RESOURCES
but can't figure how hsa_cache_get_info() can return this error...
need rebuild and use GDB to figure what it is...
to late for today...

---

### 评论 #13 — kentrussell (2019-05-14T10:12:41Z)

@cfreehill , do you have any insight into the OUT_OF_RESOURCES error?


---

### 评论 #14 — cfreehill (2019-05-14T13:29:42Z)

I think line 900 is this hsa_init() line
  err = hsa_init();
  RET_IF_HSA_ERR(err);

(I'm looking at rocminfo.cc in the github distribution).

By inspection, it looks like maybe hsaKmtOpenKFD() which is called when hsa_init() fails to either:
-load topology information (my guess) OR
-initialize process apertures OR
-setup doorbells

---

### 评论 #15 — Djip007 (2019-05-14T17:43:25Z)

I was looking here:
https://github.com/RadeonOpenCompute/rocminfo/blob/master/rocminfo.cc#L900
... look it is wrong place... can explain i can't figure the error...
I'll made more investigation. thanks

I think I can figure the line probleme... I install rocm on Fedora30... and dnf install rocminfo is:
rocminfo.x86_64                                   1.0.0-2.fc30                            @fedora                           

and I look for master... not 1.0.0 tag:
https://github.com/RadeonOpenCompute/rocminfo/blob/1.0.0/rocminfo.cc#L900
it is best ;)


---

### 评论 #16 — Djip007 (2019-05-14T17:55:24Z)

after reboot... it work...  and stop working... :
and same with clinfo 

[edit:]
I think i find my problem I test on fedora and have confict between:
hsakmt-roct from ROCm repo and hsakmt from fedora repo
remove hsakmt and look it work now...
[/edit]

#> rocminfo 
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 3550H with Radeon Vega Mobile Gfx
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32KB                               
  Chip ID:                 5592                               
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):2100                               
  BDFID:                   1280                               
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    33554048KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 5592                               
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1200                               
  BDFID:                   1280                               
  Compute Unit:            11                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  83887104                           
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            160                                
  Max Work-item Per CU:    10240                              
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*** Done ***             


---

### 评论 #17 — kentrussell (2019-05-14T18:07:44Z)

That's awesome! Keep us posted as to how everything else goes!

---

### 评论 #18 — Djip007 (2019-05-14T18:22:39Z)

next news on my post:
https://github.com/RadeonOpenCompute/ROCm/issues/750
to not pollute this issus

---

### 评论 #19 — tu6ge (2019-05-19T14:27:41Z)

I I've upgraded to version 2.4, but the problem remains unresolved.



---

### 评论 #20 — valeriob01 (2019-05-19T14:47:24Z)

> I I've upgraded to version 2.4, but the problem remains unresolved.

It is apparent that they worked on new features but not on bug fixes. Or maybe they do not test the code they write.


---

### 评论 #21 — kentrussell (2019-05-19T18:16:28Z)

Did you follow the steps that @Djip007 did above to manually add the missing ID until 2.5? The RX580 was a newer Polaris10 card that was not added to the kernel until about 1.5 after Polaris10 was added initially., so it was out of the scope of the regular ROCm stuff. The patches for the kernel and thunk will be in 2.5, but I didn't get them into 2.4 before the code freeze.

---

### 评论 #22 — tasso (2023-12-12T20:07:32Z)

Is this still an issue? If not, can we please close it? Thanks!

---

### 评论 #23 — tasso (2023-12-18T18:55:35Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
