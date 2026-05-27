# process hang up when move a tensor's memory access from GPU to CPU, by calling the function .cpu() or to('cpu') in pytorch

> **Issue #1275**
> **状态**: closed
> **创建时间**: 2020-11-03T19:45:12Z
> **更新时间**: 2020-11-18T07:44:23Z
> **关闭时间**: 2020-11-18T07:44:23Z
> **作者**: lhf2011
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1275

## 描述

### Environment
CPU: AMD Ryzen 4500U
GPU: AMD Vega 6
OS: Ubuntu18.04
ROCM: rocm-3.8.0
PyTorch in Docker: rocm/pytorch:rocm3.8_ubuntu18.04_py3.6_pytorch


### Code
def validate(val_loader, model):
    frame=0
    lastFrameTime = time.time()
    for _, (input, _) in enumerate(val_loader):
        frame=frame+1
        input = input.cuda()

        # interval cost
        predStartTime= time.time()
        
        # predict cost
        with torch.no_grad():
            pred = model(input)
        predEndTime = time.time()
        
        # sync cost
        torch.cuda.synchronize()
        afterSyncTime = time.time()

        # transfer cost
        predOnCpu = pred.detach().cpu()
        cpuGetTime = time.time()

        print("frame:", frame, " interval cost: {:.2f} ms,".format((cpuGetTime - lastFrameTime) * 1000),
              " predict cost: {:.2f} ms,".format((predEndTime - predStartTime) * 1000),
              " sync cost: {:.2f} ms,".format((afterSyncTime - predEndTime) * 1000),
              " transfer cost: {:.2f} ms".format((cpuGetTime - afterSyncTime) * 1000))

        lastFrameTime = cpuGetTime


### Issue description
The "transfer cost" in this issue is the time cost of code "pred.detach().cpu()", it moves the predict result( a tensor) from gpu to cpu. It is expected to be finished in a short time, but in fact, it is different when there is window event happens or not. 

In this case, the window event includes: the mouse swiping on the window, typing in the terminal, a pop-up system notification, etc. 

When there is an window event occurs, the program runs well,  the "transfer cost" time in the range of 0.1~100 ms, the log as follows:
frame: 506  interpret cost: 29.65 ms,  predict cost: 4.52 ms,  sync cost: 11.75 ms,  transfer cost: 1.31 ms
frame: 507  interpret cost: 25.40 ms,  predict cost: 4.58 ms,  sync cost: 3.33 ms,  transfer cost: 16.77 ms
frame: 508  interpret cost: 26.54 ms,  predict cost: 4.32 ms,  sync cost: 7.92 ms,  transfer cost: 13.64 ms
frame: 509  interpret cost: 10.53 ms,  predict cost: 4.88 ms,  sync cost: 4.80 ms,  transfer cost: 0.13 ms
frame: 510  interpret cost: 23.40 ms,  predict cost: 5.31 ms,  sync cost: 6.36 ms,  transfer cost: 6.01 ms
frame: 511  interpret cost: 10.36 ms,  predict cost: 7.02 ms,  sync cost: 2.55 ms,  transfer cost: 0.12 ms
frame: 512  interpret cost: 94.45 ms,  predict cost: 4.57 ms,  sync cost: 5.39 ms,  transfer cost: 58.97 ms
frame: 513  interpret cost: 11.41 ms,  predict cost: 4.28 ms,  sync cost: 6.46 ms,  transfer cost: 0.17 ms


But when there is no trigger, the process may hang up at "pred.detach().cpu()", therefore the "transfer cost" time varies over a huge range of 0.1 ms ~ 31 s, the log as follows:
frame: 41  interpret cost: 1655.17 ms,  predict cost: 5.72 ms  sync cost: 4.02 ms,  transfer cost: 1618.75 ms
frame: 42  interpret cost: 26.36 ms,  predict cost: 4.37 ms  sync cost: 6.36 ms,  transfer cost: 14.89 ms
frame: 43  interpret cost: 10.73 ms,  predict cost: 6.44 ms  sync cost: 3.52 ms,  transfer cost: 0.13 ms
frame: 44  interpret cost: 32.59 ms,  predict cost: 3.87 ms  sync cost: 7.42 ms,  transfer cost: 0.14 ms
frame: 45  interpret cost: 338.07 ms,  predict cost: 4.59 ms  sync cost: 6.19 ms,  transfer cost: 302.71 ms
frame: 173  interpret cost: 11496.98 ms,  predict cost: 4.65 ms  sync cost: 27.61 ms,  transfer cost: 11461.40 ms
frame: 185  interpret cost: 31853.51 ms,  predict cost: 4.92 ms  sync cost: 6.10 ms,  transfer cost: **31818.34** ms
frame: 209  interpret cost: 5575.45 ms,  predict cost: 5.05 ms  sync cost: 5.45 ms,  transfer cost: 5540.12 ms
frame: 212  interpret cost: 5943.54 ms,  predict cost: 4.74 ms  sync cost: 32.25 ms,  transfer cost: 5905.95 ms
frame: 236  interpret cost: 15143.76 ms,  predict cost: 5.22 ms  sync cost: 4.32 ms,  transfer cost: 15110.32 ms
frame: 264  interpret cost: 5693.94 ms,  predict cost: 5.03 ms  sync cost: 4.90 ms,  transfer cost: 5658.51 ms


Could somebody please help with this issue, as the serious delay reduced the frame rate significantly and cannot be applied in real time tasks.

---

## 评论 (6 条)

### 评论 #1 — ghost (2020-11-05T08:19:37Z)

Hi @lhf2011 ,

     Thank you for reaching out.  

     Request you to kindly paste or attach the logs of  following commands :

     1) /opt/rocm/bin/rocminfo
     2) /opt/rocm/bin/rocm-smi

---

### 评论 #2 — lhf2011 (2020-11-05T15:30:08Z)

> Hi @lhf2011 ,
> 
> ```
>  Thank you for reaching out.  
> 
>  Request you to kindly paste or attach the logs of  following commands :
> 
>  1) /opt/rocm/bin/rocminfo
>  2) /opt/rocm/bin/rocm-smi
> ```
Hi @ashutoshamd ,
Thanks for your reply! And the log as follows.

1) root@6ffacbcb6331:~# /opt/rocm/bin/rocminfo
```shell
sh: 1: lsmod: not found
ROCk module is NOT loaded, possibly no GPU devices
Able to open /dev/kfd read-write
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 4500U with Radeon Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 4500U with Radeon Graphics
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2375                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            6                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    15862504(0xf20ae8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    15862504(0xf20ae8) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-XX                             
  Marketing Name:          Device 1636                        
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
  Chip ID:                 5686(0x1636)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1500                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            26                                 
  SIMDs per CU:            4                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    524288(0x80000) KB                 
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
```

2) root@6ffacbcb6331:~/fast-depth# /opt/rocm/bin/rocm-smi       
 
 the log when no code running:        
```shell                                                                                                                                                                                                                                                        
========================ROCm System Management Interface========================                                                                                                                                                                                               
================================================================================                                                                                                                                                                                               
GPU  Temp   AvgPwr  SCLK    MCLK     Fan    Perf  PwrCap  VRAM%  GPU%                                                                                                                                                                                                          
0    43.0c  10.0W   400Mhz  1200Mhz  None%  auto  N/A      46%   0%                                                                                                                                                                                                            
================================================================================                                                                                                                                                                                               
==============================End of ROCm SMI Log ==============================      
```

The log in program running status:
``` shell
========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr  SCLK    MCLK     Fan    Perf  PwrCap  VRAM%  GPU%  
0    49.0c  29.0W   400Mhz  1200Mhz  None%  auto  N/A      65%   74%   
================================================================================
==============================End of ROCm SMI Log ==============================
```                                                                                                                                                                                         

---

### 评论 #3 — lhf2011 (2020-11-05T15:41:33Z)

Add more information.
This code can be simplified as follows:
```python
import time
import torch

if __name__ == '__main__':
    tartTime = time.time()
    tensorWidth = 224
    with torch.no_grad():
        while (True):
            timeBeforePutIn = time.time()
            pred = torch.ones([1, tensorWidth, tensorWidth, tensorWidth], dtype=torch.float32, device='cuda')
            timeAfterPutIn = time.time()

            torch.cuda.synchronize()
            timeAfterSync = time.time()

            predOnCpu = pred.detach().cpu()
            timeAfterGetOut = time.time()

            print(" put in cost: {:.2f} ms,".format((timeAfterPutIn - timeBeforePutIn) * 1000),
                  " sync cost: {:.2f} ms,".format((timeAfterSync - timeAfterPutIn) * 1000),
                  " get out cost: {:.2f} ms".format((timeAfterGetOut - timeAfterSync) * 1000))
```
The print would be like this, there are serious lag in "get out cost":
```shell
 put in cost: 0.06 ms,  sync cost: 3.13 ms,  get out cost: 47.16 ms
 put in cost: 0.06 ms,  sync cost: 16.77 ms,  get out cost: 48.81 ms
 put in cost: 0.07 ms,  sync cost: 3.23 ms,  get out cost: 44.78 ms
 put in cost: 0.06 ms,  sync cost: 4.64 ms,  get out cost: 33.21 ms
 put in cost: 0.06 ms,  sync cost: 7.93 ms,  get out cost: 2014.91 ms
 put in cost: 0.08 ms,  sync cost: 387.73 ms,  get out cost: 835.83 ms
 put in cost: 0.08 ms,  sync cost: 149.06 ms,  get out cost: 857.78 ms
 put in cost: 0.06 ms,  sync cost: 83.32 ms,  get out cost: 978.19 ms
 put in cost: 0.07 ms,  sync cost: 110.55 ms,  get out cost: 1500.69 ms
 put in cost: 0.07 ms,  sync cost: 115.90 ms,  get out cost: 2206.20 ms
 put in cost: 0.07 ms,  sync cost: 184.32 ms,  get out cost: 991.34 ms
 put in cost: 0.06 ms,  sync cost: 1200.28 ms,  get out cost: 6001.93 ms
 put in cost: 0.08 ms,  sync cost: 128.42 ms,  get out cost: 4672.73 ms
```

But if I run the following scripts in a new terminal, that's creating a window event every 0.01s, the above code will runs smoothly.
The shell script as follows:
```shell
#!/bin/bash
int=1
while(( $int==1 ))
do
    echo
    sleep 0.01
done 
```
And the log as follows:
```shell
 put in cost: 0.06 ms,  sync cost: 17.12 ms,  get out cost: 84.01 ms
 put in cost: 0.06 ms,  sync cost: 19.59 ms,  get out cost: 66.65 ms
 put in cost: 0.05 ms,  sync cost: 17.18 ms,  get out cost: 90.63 ms
 put in cost: 0.05 ms,  sync cost: 16.86 ms,  get out cost: 84.06 ms
 put in cost: 0.06 ms,  sync cost: 16.99 ms,  get out cost: 95.12 ms
 put in cost: 0.07 ms,  sync cost: 18.36 ms,  get out cost: 80.46 ms
 put in cost: 0.05 ms,  sync cost: 17.24 ms,  get out cost: 66.59 ms
 put in cost: 0.05 ms,  sync cost: 18.43 ms,  get out cost: 82.13 ms
 put in cost: 0.06 ms,  sync cost: 17.92 ms,  get out cost: 85.37 ms
 put in cost: 0.05 ms,  sync cost: 17.44 ms,  get out cost: 51.58 ms
 put in cost: 0.06 ms,  sync cost: 18.63 ms,  get out cost: 82.48 ms
```

---

### 评论 #4 — ghost (2020-11-06T12:15:27Z)

@lhf2011 ,
 
    Thanks for the output. This gives the requisite data for checking the problem. Let me have a look.

---

### 评论 #5 — ghost (2020-11-10T06:29:36Z)

@lhf2011 ,
 
   On the official [documentation](https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support)  it mentions the supported hardware
```
 
Supported GPUs

Because the ROCm Platform has a focus on particular computational domains, we offer official support for a selection of AMD GPUs that are designed to offer good performance and price in these domains.


GFX9 GPUs
"Vega 10" chips, such as on the AMD Radeon RX Vega 64 and Radeon Instinct MI25
"Vega 7nm" chips, such as on the Radeon Instinct MI50, Radeon Instinct MI60 or AMD Radeon VII


```
Which means the current hardware ( on which you are trying to run : Vega 6 ; gfx900 ), is not supported officially. 

The result of ROCm execution on this hardware is undefined ( i.e. may work or may not )

---

### 评论 #6 — rkothako (2020-11-18T07:42:41Z)

Hi @lhf2011 
Request to close this ticket as the mentioned hardware is not supported

---
