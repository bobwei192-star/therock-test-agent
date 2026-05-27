# Not available as CUDA device

> **Issue #1910**
> **状态**: closed
> **创建时间**: 2023-02-22T18:56:38Z
> **更新时间**: 2023-03-20T15:31:27Z
> **关闭时间**: 2023-03-03T16:51:37Z
> **作者**: arch-user-france1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1910

## 描述

Hello 

My ROCm installation does not seem to work properly. Maybe because the graphics card has not been implemented yet?

There is no CUDA-Compatible device detected, even though I installed ROCm the following:
```
sudo amdgpu-install --usecase=rocm,hip
```
There has been an nvidia gpu on the system before, however I removed it for now. I have installed `nvidia-cuda-toolkit-gcc` after I run the amdgpu install command.
I am running Ubuntu 23.04 which is in development right now, however any errors occurred on 22.04 are not seen on 23.04.

Here's how I checked if there has been found any capable GPU:
```
➜  ~ python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
2023-02-22 19:46:46.250863: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-02-22 19:46:46.808943: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
2023-02-22 19:46:53.521734: E tensorflow/compiler/xla/stream_executor/cuda/cuda_driver.cc:266] failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected
[]
➜  ~ python3 -c "import torch; print(torch.cuda.is_available())"                        
False
```

I did install the rocm version for torch, 5.2.

Here's my GPU listed (without hip it would not be in the list, just the processor then):
```
ROCk module is loaded
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
  Name:                    AMD Ryzen 9 5950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 5950X 16-Core Processor
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
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3400                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32748748(0x1f3b4cc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32748748(0x1f3b4cc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32748748(0x1f3b4cc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-XX                             
  Marketing Name:          Radeon RX 7900 XT                  
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      6144(0x1800) KB                    
    L3:                      81920(0x14000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3125                               
  BDFID:                   2560                               
  Internal Node ID:        1                                  
  Compute Unit:            84                                 
  SIMDs per CU:            2                                  
  Shader Engines:          12                                 
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    20955136(0x13fc000) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx1100         
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


I restarted the system after any installation and would be pleased if someone could help me or fix any bugy.
Thank you.

---

## 评论 (9 条)

### 评论 #1 — arch-user-france1 (2023-02-23T15:05:38Z)

#1911 is what happens on Ubuntu 22.04; and the docker image, too.

---

### 评论 #2 — alexschroeter (2023-02-27T16:37:27Z)

What you have done looks right to me.

Because you previously installed CUDA on the system, I would ensure all remnants of pytorch/tensorflow for CUDA are gone and you don't accidentally use them. How did you install the ROCm version of pytorch/tensorflow?

```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/rocm5.2
pip3 install tensorflow-rocm
```

For the other report where you used docker all the information on how you started the container is missing. I am not sure what the issue is there. Which container did you use, and were you able to see the GPU inside the container?

---

### 评论 #3 — arch-user-france1 (2023-02-27T17:01:09Z)

Do you by chance know if RDNA3 is supported by ROCm?
I could re-install a system on the computer, sure... I have allocated everything already and so I could reinstall a testing system and try without any NVIDIA software installed there.

I installed Tensorflow and PyTorch according to manual (ROCm seems to have been merged into Tensorflow; Pytorch just as you have told me, though there is no tensorflow-rocm package (pip does not find it). I used the first command.

The manual for docker is here: https://github.com/RadeonOpenCompute/ROCm-docker
I used this command:
```
sudo docker run -it --device=/dev/kfd --device=/dev/dri --security-opt seccomp=unconfined --group-add video rocm/rocm-terminal
```
And `rocminfo` shows me right now the processor and the graphics card.

And the same error as in the testing Ubuntu 22.04 installation had occurred - the testing installation is which I am going to reinstall to make sure nothing of nvidia is there.

Maybe you have an idea while I am reinstalling Ubuntu 22.04?
Would be glad to get it working :)
Thanks.

---

### 评论 #4 — alexschroeter (2023-02-27T20:28:27Z)

Sorry, I did not mean for you to reinstall the system but rather uninstall pytorch/tensorflow fully and reinstall it again.

But looking at your point about RDNA3, I see that your GPU is not on the official list of supported GPUs.
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.3/page/Prerequisites.html

I also found this entry here which suggests that the close cousin, the 7900 XTX, is not supported, sadly.
https://github.com/RadeonOpenCompute/ROCm/issues/1880#issuecomment-1367508214

---

### 评论 #5 — arch-user-france1 (2023-03-03T16:51:36Z)

> Sorry, I did not mean for you to reinstall the system but rather uninstall pytorch/tensorflow fully and reinstall it again.
> 
> But looking at your point about RDNA3, I see that your GPU is not on the official list of supported GPUs. https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.3/page/Prerequisites.html
> 
> I also found this entry here which suggests that the close cousin, the 7900 XTX, is not supported, sadly. [#1880 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1880#issuecomment-1367508214)

I guess I'll have to wait until it is fixed. Why did it show the device in `rocminfo`, though?

I also have reinstalled the system, and it didn't work. I even had to install the driver from the AMD repositories because the pre-installed one perhaps was too old.

Thank you for your help, Alex Schröter. Have a great time.

---

### 评论 #6 — alexschroeter (2023-03-11T08:05:48Z)

I just saw this and thought maybe you want to try this. https://github.com/RadeonOpenCompute/ROCm/issues/1916#issuecomment-1461572968
Good Luck.

---

### 评论 #7 — arch-user-france1 (2023-03-15T16:49:39Z)

Thank you for your suggestion. Unfortunately this is not the issue. I am sure the guy that had this issue did not run the command correctly, maybe omited the option not to use the cache or whatever.

The `rocm` version was installed correctly, and it was checked by reading the variable `torch.__version__`.
For installation instructions I have looked at PyTorch's `Get Started`.

---

### 评论 #8 — TheCowboyHermit (2023-03-20T00:58:17Z)

@arch-user-france1 I did wipe the cache and all, it kept going back to 1.13 version when running the instructions. After installing the package manually for ROCm, it works fine. When running various projects like stable diffusion and others, it have some severe limitations that it doesn't support FP16 directly due to missing implementation on kernel norm layer within PyTorch or whatever else. I am currently writing a Vulkan Compute neural net code so that it would be able to run on various platforms including 7900 XTX without issues.

---

### 评论 #9 — arch-user-france1 (2023-03-20T15:27:13Z)

@TechScribe-Deaf 
If you use the command from the [PyTorch Start Locally Site](https://pytorch.org/get-started/locally/), it will install the `rocm` version:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2
```

Of course you must first remove any existing pytorch installations in your environment: `pip uninstall torch`.

I will confirm that it does not work again:
![grafik](https://user-images.githubusercontent.com/72965843/226388906-94954a70-72d9-4d6d-ac23-c1b581b15484.png)


AMD hip is installed, I have rechecked.
It is obvious AMD has problems with their architecture right now, isn't it.

---
