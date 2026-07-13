# [Issue]: Consistent GPU crashes with pytorch on 7900XTX (gfx1100)

- **Issue #:** 5933
- **State:** open
- **Created:** 2026-02-05T13:51:22Z
- **Updated:** 2026-03-04T20:47:22Z
- **Labels:** status: assessed
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5933

### Problem Description

Consistent GPU crashes when running code inside [rocm/pytorch:latest](https://hub.docker.com/r/rocm/pytorch) container. (was not tested outside of container)

Code to reproduce and please see `dmesg` output below. 

This might very well be because of my limited understanding of proper `pytorch`, `transfomers` etiquette. However it is currently keeping me from learning the proper way. 

The proper implementation and example code follow the [transformers guide on how to use paddle-ocr](https://huggingface.co/docs/transformers/model_doc/paddleocr_vl?usage=AutoModel#batched-inference) exactly, including set parameters.

The goal was to create a pipeline which can take images containing text of arbitrary sizes (height, width), batch them up (goal was: 16-64 images) and have the model perform batched inference on them. The images usually include just a single sentence in binary colors (text:black, background: white). Multiple `CPUWorkers` gather the images and queue them towards a single `GPUWorker` which then performs the inference once the batch is sufficiently large. 

The example code does not reflect that behavior, just represents a presumed minimum viable example to crash the Desktop and GPU.

I assumed it might be my GPU clock speed, which can exceed 3020MHz - so I tried limited it naively with [CoreCtrl](https://gitlab.com/corectrl/corectrl) using the  `Powermode=Advanced` and then `Power Profile=Compute` which held the `GPU Clock` at just 568Mhz (also the same in `nvtop`, `amd-smi` and `rocm-smi`), but could still get it to crash consistently. 

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

AMD Ryzen 9 7900X 12-Core Processor

### GPU

Radeon RX 7900 XTX - gfx1100 

### ROCm Version

ROCm version: 7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

- Install Ubuntu fresh
- Install [Rocm for Radeon products](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/native_linux/install-radeon.html)
- Install docker
- Run [pytorch container](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installrad/native_linux/install-pytorch.html)

Happens much faster with higher `batchsize` (`>=8`). 

The code creates a `PaddlePaddle/PaddleOCR-VL` with `flash_attention_2`, creates a batch of 8 images and tries to analyze text inside. (in this case just random noise for easier reproduction, but does not matter)

```
from transformers import AutoModelForCausalLM, AutoProcessor
from copy import deepcopy
from PIL import Image
import numpy as np
import torch


def main():
    # Model setup
    torch_device        = "cuda"
    model_name          = "PaddlePaddle/PaddleOCR-VL"
    attn_implementation = "flash_attention_2"

    model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            dtype=torch.bfloat16,
            attn_implementation=attn_implementation, 
        ).to(device=torch_device).eval()
    processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True, use_fast=True)


    # Batch setup
    batch = []
    batch_size = 8
    task = "ocr"
    prompts = {
        "ocr": "OCR:",
    }
    message_template = [
                {"role": "user",         
                 "content": [
                        {"type": "image", "image": None},
                        {"type": "text", "text": prompts[task]},
                    ]
                }
            ]

    for _ in range(0, batch_size):
        height  = np.random.randint(24, 180)
        width   = np.random.randint(24, 180)
        a       = np.random.rand(height, width, 3) * 255
        image   = Image.fromarray(a.astype('uint8')).convert('RGB')

        message = deepcopy(message_template)
        message[0]["content"][0]["image"] = image
        batch.append(message)


    # Input setup
    inputs = processor.apply_chat_template(
            batch, 
            add_generation_prompt=True,
	        tokenize=True,
	        return_dict=True,
	        return_tensors="pt",
            padding=True,
            padding_side='left',
        ).to(torch_device)
    
    with torch.inference_mode():
            out = model.generate(
                **inputs,
                max_new_tokens=1024,
                do_sample=False,
                use_cache=True
            )

    generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, out)]
    texts = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)



if __name__ == "__main__":
    main()
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.16.13 is loaded
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
  Name:                    AMD Ryzen 9 7900X 12-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 7900X 12-Core Processor
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
  Max Clock Freq. (MHz):   5911                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            24                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32566780(0x1f0edfc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32566780(0x1f0edfc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32566780(0x1f0edfc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32566780(0x1f0edfc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1100                            
  Uuid:                    GPU-029a3387f47e439f               
  Marketing Name:          Radeon RX 7900 XTX                 
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
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29772(0x744c)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2431                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            96                                 
  SIMDs per CU:            2                                  
  Shader Engines:          6                                  
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
  SDMA engine uCode::      27                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    25149440(0x17fc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25149440(0x17fc000) KB             
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

### Additional Information

`dmesg` output:
[one crash isolated.txt](https://github.com/user-attachments/files/25097627/one.crash.isolated.txt)
[multi-crashes.txt](https://github.com/user-attachments/files/25097628/multi-crashes.txt)
