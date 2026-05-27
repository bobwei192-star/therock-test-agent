# ROCm support for AWS G4ad instances (gfx1011)

> **Issue #1341**
> **状态**: closed
> **创建时间**: 2020-12-17T23:08:36Z
> **更新时间**: 2021-12-07T18:37:49Z
> **关闭时间**: 2020-12-18T03:54:17Z
> **作者**: amrragab8080
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1341

## 描述

The Amazon G4ad instance have AMD Radeon V520 GPUs with device name ```gfx1011``` unfortunately many of the ROCm utils do not have binaries supporting ```gfx1011``` 
```
2020-12-17 23:03:23.004276: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
/src/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")
Fatal Python error: Aborted
```
docker run -it --device=/dev/kfd --device=/dev/dri --security-opt seccomp=unconfined --group-add video rocm/tensorflow

But I do see the output from ```rocminfo```
```
*******                  
Agent 2                  
*******                  
  Name:                    gfx1011                            
  Uuid:                    GPU-XX                             
  Marketing Name:          Device 7362                        
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 29538(0x7362)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1150                               
  BDFID:                   240                                
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2 
```

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2020-12-18T03:54:17Z)

Hi @amrragab8080 
Thanks for reaching out.
We are not officially supporting Navi series of cards at present.
We have plans to support some series of cards in 2021 and we will update accordingly.
Thank you. 

---

### 评论 #2 — lingfanyu (2021-02-20T02:04:14Z)

I also tried installing ROCm on Amazon G4ad instance following [this guide](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html).

The installation looks successful. However, `/opt/rocm/bin/rocminfo` returns:
> ROCk module is NOT loaded, possibly no GPU devices
Unable to open /dev/kfd read-write: No such file or directory
ubuntu is member of video group
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

and `/opt/rocm/bin/rocm-smi` returns:
> ERROR:root:ROCm SMI returned 8 (the expected value is 0)

I hope to see the official support AMD Radeon V520 GPUs and AWS G4ad instance soon!

---

### 评论 #3 — dsahni (2021-05-13T13:43:48Z)

Hi @ROCmSupport , do you have any estimates on when ROCm support for AWS G4ad will be available?

---

### 评论 #4 — ROCmSupport (2021-05-31T10:01:29Z)

Hi @dsahni 
Internal testing is happening on some series of Navi cards and so can not comment on exact estimates right now.

---

### 评论 #5 — monkeyhippies (2021-12-07T18:37:49Z)

Hello @ROCmSupport do you have nay update on support for AWS G4ad instances?? Thank you

---
