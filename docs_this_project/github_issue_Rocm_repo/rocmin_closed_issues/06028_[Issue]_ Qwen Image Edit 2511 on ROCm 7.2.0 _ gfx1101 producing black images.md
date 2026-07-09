# [Issue]: Qwen Image Edit 2511 on ROCm 7.2.0 + gfx1101 producing black images.

- **Issue #:** 6028
- **State:** closed
- **Created:** 2026-03-10T15:57:09Z
- **Updated:** 2026-03-16T14:06:42Z
- **Labels:** status: triage
- **Assignees:** sshi-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6028

### Problem Description

### Custom Node Testing on ComfyUI

- [x] I have tried disabling custom nodes and the issue persists

### Expected Behavior

- Image is produced with and without lightning LoRA.

### Actual Behavior

Multiple Images:
- Black image
- Without LoRA, the image turns out black at 18/19th step out of 20 or around 25th step out of 40. Subsequent runs start black. Have to clean start again from beginning to reproduce behavior (i.e. stop server -> clean cookies and site-related data from browser -> start server).
- With LoRA, at the first fresh run the image turns black or mosaicked at the 3rd or the last step out of 4. If mosaicked the output consequentially appears hillarious (Image 1).

<img width="1024" height="1024" alt="Image" src="https://github.com/user-attachments/assets/a61c972e-0001-4066-bdb8-9289fe8557fc" />

- Subsequent runs with LoRA start with black image. Have to clean start similarly to reproduce.

Single Images:
- Without LoRA, image turns black at around 6/7th step out of 20. Subsequent runs start black.
- With LoRA, image starts black. Subsequent runs are also black.

### Operating System

Fedora Linux 43 KDE

### CPU

AMD Ryzen 7 7700

### GPU

Sapphire PURE Radeon RX 7700XT

### ROCm Version

ROCm 7.2.0

### ROCm Component

_No response_

### Steps to Reproduce


- disable igpu from kernel cmdline with `pci-stub.ids=1002:164e`. Reboot.
- ensure `rocminfo` doesn't show igpu.
- pull rocm/pytorch:latest docker image
- install `amd-container-toolkit`
- issue `# amd-ctk gpu-tracker enable; amd-ctk gpu-tracker reset; amd-ctk cdi generate; systemctl try-restart docker{,.socket}`
- create a container with
```
docker run -it \
        --gpus device=all --runtime=amd \
        -v /mnt/a/projects/comfyui:/src:Z \
        -v /mnt/a/cache/uv:/mnt/a/cache/uv:Z \
        -v /mnt/a/cache/huggingface:/mnt/a/cache/huggingface:Z \
        -p 8188:8188 \
        --name rocm-pytorch \
        rocm/pytorch:latest
```
Note: traditionally passing `/dev/kfd`, `/dev/dri/renderD128` and `shm` devices instead of `amd-container-toolkit` also has similar effect.
- `rocminfo` doesn't show igpu.
- activate venv and run comfyui with:
`# python main.py --listen 0.0.0.0 --preview-method auto --cache-none --disable-all-custom-nodes`
- load [this official Qwen Image Edit 2511 guide](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/templates/image_qwen_image_edit_2511.json)
- replace qwen_image_edit_2511_bf16.safetensors with _fp8mixed.safetensors in `unet_name` field
- go to the subgraph, connect "Switch (Steps)::output" => "KSampler::steps"
- return to parent page, use a sofa image from internet. I used this 600x600 jpg image as leather_sofa.png

![Image](https://github.com/user-attachments/assets/2dd18f3b-7a77-4d60-bf25-faa355b76f26)

- use a fur texture image from internet. I used this 280x280px jpg image as texture_fur.jpg

![Image](https://github.com/user-attachments/assets/292ffa9e-c357-4e76-b43b-8b7999d02c10)

- hit "Run".

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

Within Docker
```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.15
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 7700 8-Core Processor  
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 7700 8-Core Processor  
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
  Max Clock Freq. (MHz):   5583                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    31408680(0x1df4228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    31408680(0x1df4228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    31408680(0x1df4228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31408680(0x1df4228) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1101                            
  Uuid:                    GPU-df042d5d020a464f               
  Marketing Name:          AMD Radeon RX 7700 XT              
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
    L2:                      4096(0x1000) KB                    
    L3:                      49152(0xc000) KB                   
  Chip ID:                 29822(0x747e)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2226                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            54                                 
  SIMDs per CU:            2                                  
  Shader Engines:          3                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
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
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 602                                
  SDMA engine uCode::      29                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1101         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx11-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*** Done ***   
```

### Additional Information

[defaults+lora-singleImage-fresh-4steps.log](https://github.com/user-attachments/files/25826747/defaults%2Blora-singleImage-fresh-4steps.log)
[defaults+lora-singleImage-run2-4steps.log](https://github.com/user-attachments/files/25826750/defaults%2Blora-singleImage-run2-4steps.log)
[defaults+lora-twoImages-fresh-4steps.log](https://github.com/user-attachments/files/25826748/defaults%2Blora-twoImages-fresh-4steps.log)
[defaults+lora-twoImages-run2-4steps.log](https://github.com/user-attachments/files/25826746/defaults%2Blora-twoImages-run2-4steps.log)
[defaults+lora-twoImages-run3-4steps.log](https://github.com/user-attachments/files/25826745/defaults%2Blora-twoImages-run3-4steps.log)
[defaults-singleImage-20steps.log](https://github.com/user-attachments/files/25826752/defaults-singleImage-20steps.log)
[defaults-twoImages-20steps.log](https://github.com/user-attachments/files/25826749/defaults-twoImages-20steps.log)
[defaults-twoImages-fresh-20steps.log](https://github.com/user-attachments/files/25826753/defaults-twoImages-fresh-20steps.log)
[defaults-twoImages-run2-20steps.log](https://github.com/user-attachments/files/25826751/defaults-twoImages-run2-20steps.log)

These are my additional system specs and info:
- 16x2=32GB DDR5 RAM
- comfyui v0.16.4


I'm using the qwen_image_edit_2511_fp8mixed.safetensors as the bf16 version doesn't fit in my machine. Also, installed `torch`, `torchaudio`, `torchvision` and `triton` following [this](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/native_linux/install-pytorch.html#option-a-pytorch-via-pip-installation) guide but for python 3.13.

Also tried downgrading the python version to 3.12.3. This is the behavior now:

Without LoRA:
- Fresh start: image starts black
- Subsequent runs: either succeeds (20 steps), turns black at 15th/16th step out of 20, starts black or outputs black image after VAE decode after 40 steps succeeds and shows in the log:
```
/src/ComfyUI/nodes.py:1664: RuntimeWarning: invalid value encountered in cast
  img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
```
although the latent image is not black.

With LoRA:
- Fresh start: image starts black
- Subsequent run 1: succeeds (4 steps) or starts black.
- Subsequent run 2: image turns black at 3rd step out of 4.

logs in all cases are same as before except python version change, but for "Fresh Start" if I complete the step till end (with black image) this comes up again:
```
/src/ComfyUI/nodes.py:1664: RuntimeWarning: invalid value encountered in cast
  img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
```
which seems obvious since the image started black initially.

EDIT: [Posted issue on comfyui repo](https://github.com/Comfy-Org/ComfyUI/issues/12839)