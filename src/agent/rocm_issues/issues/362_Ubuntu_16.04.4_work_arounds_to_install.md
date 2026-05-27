#  Ubuntu 16.04.4 work arounds to install 

> **Issue #362**
> **状态**: closed
> **创建时间**: 2018-03-15T12:49:44Z
> **更新时间**: 2018-09-28T05:14:29Z
> **关闭时间**: 2018-09-28T05:14:29Z
> **作者**: chromakey-io
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/362

## 描述

I tried Cent, then OpenSuSE ... because I'm not a huge fan of Ubuntu for technical reasons.

Anyway I've installed Ubuntu 16.04.4 and followed the instructions to the T on the ROCM installation page.  I can compile the HelloWorld, but it fails to find a working OpenCL runtime.

I've done nothing other than install Ubuntu 16.04.4 and then immediately follow the install instructions (this time).

HelloWorld fails with:
Failed to find any OpenCL platforms.
Failed to create OpenCL context.

... but compiles just fine obv.

clinfo fails with:
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

Previously I've tried a mix of the amdgpu-pro installers, mesa, and pretty much everything under the sun.  I've had no problem getting mesa and the legacy stuff to work.  I've checked the ld.so.conf.d and it all looks okay by my eyes ... I've tried installing by hand from the Beta4.tar.gz ... I've tried installing from the local-repo ... I've tried installing from the network repo.amd site.

I'll write up changes to the documentation and push a merge on git ... if someone can help me get this running.  I feel like it's going to be something obvious I'm missing ... but i've hit a wall.

thx.

-k

---

## 评论 (27 条)

### 评论 #1 — gstoner (2018-03-15T12:51:14Z)

Did you add your user name to the Video group 




---

### 评论 #2 — chromakey-io (2018-03-15T12:51:26Z)

Yup.

---

### 评论 #3 — gstoner (2018-03-15T12:52:29Z)

Can you run HIP sample 



---

### 评论 #4 — gstoner (2018-03-15T12:52:56Z)

CENTOS/OPENSUSE are not supported 

---

### 评论 #5 — chromakey-io (2018-03-15T12:53:44Z)

Oh I know ... I'm on Ubuntu 16.0.4.4 now ... and was trying to use the older releases on those machines.

---

### 评论 #6 — gstoner (2018-03-15T12:57:26Z)

I was out on break last few days it is Spring Break in Austin.  I just saw Ubuntu just release. 16.04.4,  I have SQE running 16.04.4.  If there is an issue we get it cleaned up, I ping you again latter today with update

Have you run rocminfo, what are the results 

---

### 评论 #7 — chromakey-io (2018-03-15T12:58:52Z)

Okay ... so I just tried to build one of the samples in hip.

... and I got this:

Can't exec "/usr/local/cuda/bin/nvcc": No such file or directory at /opt/rocm/hip/bin/hipcc line 501.

I'm running a workstation with multiple cards in it (2 RX570 and 1 NVIDIA 1060) .... I have the monitor running through an nvidia card now, and previously was trying to make all of this work when running things through the onboard intel graphics since I always run headless and figured it would be better to run the monitor not on the cards.

Anyway.  I don't have cuda anything installed right now ... it's *just* ubuntu 16.04.4 and the stuff from the instructions page.

... but is this maybe because I'm running things through the Nvidia card?  Do I need to run my monitor through an AMD card for this to work?

Pulling the nvidia now ...

---

### 评论 #8 — chromakey-io (2018-03-15T13:00:22Z)

rocm info was giving me a nil result ... but I did just install mesa for shits and giggles to give myself a sanity check.

So it's throwing mesa info now:

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
  Name:                    Intel(R) Core(TM) i3-7100 CPU @ 3.90GHz
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
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3900                               
  BDFID:                   0                                  
  Compute Unit:            4                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    4007116KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4007116KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*** Done ***             

---

### 评论 #9 — gstoner (2018-03-15T13:03:31Z)

The KFD driver has not started, the stack is not running based on this input.  Currently, you do have driver properly installed. 

---

### 评论 #10 — chromakey-io (2018-03-15T13:12:02Z)

Okay ... trying to rebuild the DKMS modules by hand to see what's up.  I didn't see any errors on the install though and it seemed like everything built okay.

You think I would have better luck rolling back to 16.04?

I'll post if I can figure out any compile or load errors with the amdkfd module....

---

### 评论 #11 — chromakey-io (2018-03-15T13:25:06Z)

So rebuild the dkms modules amdkfd seems like it's loaded with lsmod:
root@noah-desktop:/opt/rocm/bin# lsmod | grep amd
amdkfd                188416  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               2027520  4
i2c_algo_bit           16384  1 amdgpu
ttm                    94208  1 amdgpu
drm_kms_helper        167936  1 amdgpu
drm                   360448  6 amdgpu,ttm,drm_kms_helper

Also  ... and now I'm getting this result from rocminfo:

hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104

---

### 评论 #12 — gstoner (2018-03-15T13:48:54Z)

Yes we have been running Ubuntu 16.04.3 with generic 4.13 kernel



---

### 评论 #13 — ghost (2018-03-15T15:48:11Z)

 apt-get remove intel-microcode#remove the broken microcode to fix the broken proccessors.#How to you know a update is really broken, when microsoft stops calling it a feature and starts calling it a rollback


#/etc/default/grub
The spectre of Sectre, causes issues and along nmi_watchdog like to byte on quite a few boards.
GRUB_CMDLINE_LINUX_DEFAULT="selinux=0 amdgpu.vm_fragment_size=9 nmi_watchdog=0 pti=off 3 spectre_v2=off nospectre_v2 nopti retp=0 ibrs=0 ibpb=0"

---

### 评论 #14 — wdormann (2018-03-16T17:57:48Z)

FWIW, I ran into a similar problem.  But in my case, it was because I was booting with the "nomodeset" grub option, because without it I'd get a mostly-black, sometimes-flashing actual contents (once every couple seconds) display without it.

However, with "nomodeset", the GPU isn't recognized by the system / OpenCL.  As the result, I've removed the "nomodeset" boot option, and things are suddenly fine (aside from the flashing display).   In my case it's headless, so the flashing screen doesn't really matter to me.  But I suppose I'm curious how one can get both a non-flashing screen and a recognized GPU.

---

### 评论 #15 — chromakey-io (2018-03-16T23:45:44Z)

Thanks guys.  It seems like things are working with 16.04.03 just fine.


---

### 评论 #16 — rhlug (2018-03-28T20:51:43Z)

@tekcomm can you get a working clinfo via amdgpu-pro or rocm with 4.16.0-rc7?  

I cannot.  The only working OCL I get with 4.16.0-rc7+  is Mesa 18. 

After installing amdgpu-pro 17.50, clinfo segfaults with amdgpu dkms loaded.  With amdgpu dkms unloaded,  I get "Number of platforms: 0" unless I enable the mesa.icd.

Also tried same with rocm.  dkms fails to load.  clinfo segfaults.

```
ERROR (dkms apport): kernel package linux-headers-4.16.0-rc7+ is not supported
```

Without dkms loaded, "Number of platforms: 0"

Back to mesa 18.

```
# clinfo
Number of platforms                               1
  Platform Name                                   Clover
  Platform Vendor                                 Mesa
  Platform Version                                OpenCL 1.1 Mesa 18.1.0-devel
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd
  Platform Extensions function suffix             MESA

  Platform Name                                   Clover
Number of devices                                 6
  Device Name                                     Radeon RX Vega (VEGA10 / DRM 3.25.0 / 4.16.0-rc7+, LLVM 6.0.0)
  Device Vendor                                   AMD
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 1.1 Mesa 18.1.0-devel
```





---

### 评论 #17 — rhlug (2018-03-28T20:52:56Z)

amdgpu dkms not supported either i guess.

```
# dkms install amdgpu/17.50-511655 

Creating symlink /var/lib/dkms/amdgpu/17.50-511655/source ->
                 /usr/src/amdgpu-17.50-511655

DKMS: add completed.

Kernel preparation unnecessary for this kernel.  Skipping...

Running the pre_build script:

Building module:
cleaning build area....
make KERNELRELEASE=4.16.0-rc7+ -j4 -C /lib/modules/4.16.0-rc7+/build M=/var/lib/dkms/amdgpu/17.50-511655/build....(bad exit status: 2)
ERROR (dkms apport): kernel package linux-headers-4.16.0-rc7+ is not supported
Error! Bad return status for module build on kernel: 4.16.0-rc7+ (x86_64)
Consult /var/lib/dkms/amdgpu/17.50-511655/build/make.log for more information.
```


---

### 评论 #18 — rhlug (2018-03-28T21:16:41Z)

But vega pp_table wasnt fixed until march 26 nightly.  Didnt work in 994, worked in 996.  So thats a deal breaker.  I shall wait longer...

---

### 评论 #19 — rhlug (2018-03-28T21:25:57Z)

the latest m-bab?  thats what one i installed.  thats what produced the error above

specifically...
```
# dkms install amdgpu/17.50-511655 
ERROR (dkms apport): kernel package linux-headers-4.16.0-rc7+ is not supported
```

---

### 评论 #20 — rhlug (2018-03-30T14:25:38Z)

what does your dkms look like on 4.16.0-041600rc7-generic 

```
# dkms status
```

i built kernels from amd-staging-drm-next and drm-next-4.17-wip repos and i have no working vegas.    Both of them end up with this error, and clinfo hangs indefinitely

```
Mar 30 08:31:43 rig23 kernel: [   38.368042] [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring sdma0 timeout, last signaled seq=3, last emitted seq=5
Mar 30 08:31:43 rig23 kernel: [   38.368365] [drm] No hardware hang detected. Did some blocks stall?
```

If I revert to 4.16.0-996-lowlatency, my vegas all work.   Not sure whats going on there, maybe some regression.




---

### 评论 #21 — rhlug (2018-03-30T17:23:21Z)

I msgd you.   

4.16.0-996-lowlatency - All 6x vega56 OK.
4.16.0-drm-next-4.17-wip-180330 -   4x vega56 OK.  5th vega causes sdma0 ring error.




---

### 评论 #22 — rhlug (2018-03-30T18:08:42Z)

I'll give it a shot.  Its funny that 4 GPU would come up, but my ethminer wasnt crunching any hashes.  It thought it was, but was reporting 0.0 Mh/s.      Back on  4.16.0-996-lowlatency and I'm crunching ~230Mh/s on 6x vega.

drm-next-4.17-wip and Mesa 18.1 must not be a good combo.  


---

### 评论 #23 — rhlug (2018-04-03T14:43:25Z)

I can confirm, the smda0 ring error is gone on amd-staging-drm-next.  All 6 of my vegas come up, and I get a proper environment with mesa/clover. 

However, I'm unable to get a working clinfo on that kernel with amdgpu or amdgpu-pro.   Tried to reinstall amdgpu-pro-17.50, and still get errors on dkms module.

```
Building initial module for 4.16.0-amd-staging-180401
ERROR (dkms apport): kernel package linux-headers-4.16.0-amd-staging-180401 is not supported
Error! Bad return status for module build on kernel: 4.16.0-amd-staging-180401 (x86_64)
Consult /var/lib/dkms/amdgpu/17.50-511655/build/make.log for more information.
```

---

### 评论 #24 — rhlug (2018-04-04T19:20:31Z)

So while amd-staging-drm-next kernel now loads all my vegas, and i get a functional clinfo under mesa, ethminer reports 0.0mh/s.  Even though it thinks its hashing, its not doing shit.

Reverting to 4.16.0-996-lowlatency from drm-next ubuntu mainline, I get 40Mh/s ethash on ethminer.  Same mesa, same ethminer, llvm, etc.   Just a kernel install and reboot.

I'll give drm-tip a shot from ubuntu mainline next out of curiosity.


---

### 评论 #25 — rhlug (2018-04-05T04:15:28Z)

drm-tip 4.16.0-994.201804032201  works.

---

### 评论 #26 — rhlug (2018-06-05T14:10:33Z)

I have been running  fkxamd/drm-next-wip tag (4.17.0-rc2-180424-fkxamd) as recommended by Felix.   It gave me functional power play on all 6 vegas under Mesa opencl.  I havent been running ROCm lately because I couldnt get any dkms loading on any recent kernel that had functional pp_table, and that was a deal break in term of power consumption.

---

### 评论 #27 — rhlug (2018-06-05T16:52:39Z)

Yes, my "new vegas" bought 8 months ago.   We'll have a working linux environment for vega10 just in time for the vega20 drop.  :-) 

---
