# [Issue]: HSA_STATUS_ERROR_EXCEPTION (0x1016) during Qwen2.5-32B text generation on RX 7900 XTX

- **Issue #:** 5025
- **State:** closed
- **Created:** 2025-07-10T08:02:18Z
- **Updated:** 2025-11-27T16:49:53Z
- **Labels:** status: triage
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5025

### Problem Description

# ROCm GPU Exception Debug Report - Qwen2.5-32B Model

## 🔧 System Information

**Hardware:**
- **Primary GPU:** AMD Radeon RX 7900 XTX (gfx1100, 25.8 GB VRAM)
- **Secondary GPU:** AMD Radeon 780M (integrated in CPU, gfx1100)
- **CPU:** AMD Ryzen 7 8700G w/ Radeon 780M Graphics (Zen 4 architecture)
- **Memory:** Multi-GPU environment (discrete + integrated)

**Software Stack:**
- **OS:** Ubuntu 24.04.2 LTS (Noble Numbat)
- **Kernel:** Linux 6.11.0-29-generic  
- **ROCm Version:** 6.4
- **Architecture:** gfx1100 (RDNA 3)
- **PyTorch:** 2.9.0.dev20250629+rocm6.4
- **Transformers:** 4.43.1+
- **CUDA available:** True (ROCm compatibility layer)
- **Device count:** 2 (discrete + integrated)
- **Primary device:** 0 (RX 7900 XTX used for inference)

## ⚠️ Issue Description

### Primary Problem
ROCm GPU exceptions during large language model (Qwen2.5-32B, 65GB) text generation, specifically during `model.generate()` calls.

### Error Pattern
```
:0:rocdevice.cpp:2993: [timestamp] us: Callback: Queue [address] aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016
```

**Specific Error Examples:**
```
:0:rocdevice.cpp:2993: 89216349659 us: Callback: Queue 0x76f0b0600000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016

:0:rocdevice.cpp:2993: 89368970309 us: Callback: Queue 0x740ca7200000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016

:0:rocdevice.cpp:2993: 90251751038 us: Callback: Queue 0x78b511400000 aborting with error : HSA_STATUS_ERROR_EXCEPTION: An HSAIL operation resulted in a hardware exception. code: 0x1016
```

## 🎯 Reproducible Test Case

### Working Operations
✅ **Model Loading:** Successfully loads all 17 checkpoint shards (32B parameters)
✅ **Tokenization:** Input tokenization works correctly
✅ **Device Placement:** Model and tensors properly placed on cuda:0
✅ **Small Generation:** Very minimal generation (10 tokens) sometimes succeeds but takes 38+ seconds

### Failing Operations
❌ **Extended Generation:** Generation with 50-150 tokens consistently triggers ROCm exceptions
❌ **Repeated Calls:** Multiple generation calls tend to hang or crash
❌ **Complex Parameters:** Using temperature, top_p, etc. increases failure rate

### Minimal Reproduction Script

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load Qwen2.5-32B model
model_path = "./llama33-masala-chai-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
    low_cpu_mem_usage=True
)

# Simple test that triggers the error
prompt = "Generate a simple circuit description:"
inputs = tokenizer(prompt, return_tensors="pt")
inputs = {k: v.to("cuda") for k, v in inputs.items()}

# This reliably triggers the ROCm exception:
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,  # Reducing to 10 sometimes works
        temperature=0.7,     # Removing sampling params sometimes helps
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )
```

## 📊 Memory Analysis

**VRAM Usage During Operation:**
```bash
$ rocm-smi --showmeminfo vram
ROCm System Management Interface
Memory Usage (Bytes)
GPU[0]: VRAM Total Memory (B): 25753026560  # ~25.8GB
GPU[0]: VRAM Total Used Memory (B): 2144231424  # ~2.1GB during model load
```

**Memory Pattern:**
- Model loading: Uses ~20GB VRAM (estimated for 32B parameters in fp16)
- Generation start: Additional memory allocation
- Exception occurs: During active compute, not memory allocation

## 🔍 Debug Timeline

### Step 1: Basic Model Loading
```
✅ Loading checkpoint shards: 100%|██████████| 17/17 [00:13<00:00, 1.24it/s]
✅ Some parameters are on the meta device because they were offloaded to the cpu.
✅ Model loaded successfully
```

### Step 2: Input Preparation
```
✅ Tokenization successful - Input shape: torch.Size([1, 12])
✅ Input IDs device: cpu → cuda:0 (successful transfer)
✅ Model device: cuda:0
```

### Step 3: Generation Attempt
```
⏳ Starting generation...
❌ :0:rocdevice.cpp:2993: [timestamp]: HSA_STATUS_ERROR_EXCEPTION: code: 0x1016
⚠️ Process hangs or continues with corrupted output
```

## 🧪 Attempted Workarounds

### Successful Workarounds
1. **Reduce max_new_tokens to 10:** Sometimes works but very slow (38s)
2. **Use greedy decoding (do_sample=False):** Slightly more stable
3. **Remove sampling parameters:** Eliminates some variables
4. **torch.cuda.empty_cache():** Clear GPU memory before operations

### Failed Workarounds
1. **Lower batch size:** Already using batch_size=1
2. **Different torch_dtype:** Tried float16, auto
3. **CPU offloading:** Some parameters already offloaded
4. **Different device_map:** "auto" vs explicit mapping
5. **Flash attention:** Not available in this environment

## 💻 Environment Details

### PyTorch Installation
```python
torch.__version__ = "2.9.0.dev20250629+rocm6.4"
torch.cuda.is_available() = True
torch.cuda.device_count() = 1
torch.cuda.current_device() = 0
torch.cuda.get_device_name() = "Radeon RX 7900 XTX"
```

### ROCm Detection
```bash
$ rocm-smi
# Shows GPU properly detected and functional
# Basic operations work (model loading, simple tensor ops)
```

### Model Configuration
```json
{
  "model_type": "qwen2",
  "num_hidden_layers": 64,
  "hidden_size": 5120,
  "num_attention_heads": 40,
  "max_position_embeddings": 32768,
  "torch_dtype": "bfloat16",
  "vocab_size": 152064
}
```

## 🎯 Bug Report Summary

**Issue:** ROCm HSA_STATUS_ERROR_EXCEPTION (code 0x1016) during large language model text generation

**Severity:** High - Prevents reliable use of large models on AMD GPUs

**Reproducibility:** Consistent with Qwen2.5-32B model (65GB, fp16)

**Impact:** 
- Model loading works perfectly
- Small generations occasionally work but are extremely slow
- Extended generations consistently fail
- Affects production deployment of large language models on AMD hardware

**Hardware:** AMD Radeon RX 7900 XTX (25.8GB VRAM)
**Software:** ROCm 6.4, PyTorch 2.9.0.dev+rocm6.4

**Suggested Investigation Areas:**
1. HSAIL operation handling in large matrix operations
2. Memory management during attention computation
3. Queue management for extended operations
4. Interaction between transformers library and ROCm runtime

**Workaround:** Use CPU inference for reliable operation (significantly slower)

**Files Available for Testing:**
- Complete reproduction environment with 65GB model
- Debug scripts with step-by-step ROCm interaction
- Detailed logs with timestamps and memory usage

## 📝 Additional Notes

This issue appears to be specific to:
- Large models (32B+ parameters)
- Extended generation sequences (>50 tokens)
- Complex attention operations during autoregressive generation

The same operations work reliably on CPU, suggesting a ROCm-specific issue rather than a model or software stack problem.

---

**Contact:** Available for additional debugging, logs, or testing with ROCm development team.
**Environment:** Can provide SSH access to reproduction system if needed for ROCm debugging.

### Operating System

- **OS:** Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

- **CPU:** AMD Ryzen 7 8700G w/ Radeon 780M Graphics (Zen 4 architecture)

### GPU

**Primary GPU:** AMD Radeon RX 7900 XTX (gfx1100, 25.8 GB VRAM)

### ROCm Version

**ROCm Version:** 6.4

### ROCm Component

_No response_

### Steps to Reproduce

## 🎯 Reproducible Test Case

### Working Operations
✅ **Model Loading:** Successfully loads all 17 checkpoint shards (32B parameters)
✅ **Tokenization:** Input tokenization works correctly
✅ **Device Placement:** Model and tensors properly placed on cuda:0
✅ **Small Generation:** Very minimal generation (10 tokens) sometimes succeeds but takes 38+ seconds

### Failing Operations
❌ **Extended Generation:** Generation with 50-150 tokens consistently triggers ROCm exceptions
❌ **Repeated Calls:** Multiple generation calls tend to hang or crash
❌ **Complex Parameters:** Using temperature, top_p, etc. increases failure rate

### Minimal Reproduction Script

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load Qwen2.5-32B model
model_path = "./llama33-masala-chai-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
    low_cpu_mem_usage=True
)

# Simple test that triggers the error
prompt = "Generate a simple circuit description:"
inputs = tokenizer(prompt, return_tensors="pt")
inputs = {k: v.to("cuda") for k, v in inputs.items()}

# This reliably triggers the ROCm exception:
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,  # Reducing to 10 sometimes works
        temperature=0.7,     # Removing sampling params sometimes helps
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.12.12 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.15
Runtime Ext Version:     1.7
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
  Name:                    AMD Ryzen 7 8700G w/ Radeon 780M Graphics
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 8700G w/ Radeon 780M Graphics
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
  Max Clock Freq. (MHz):   5176                               
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
      Size:                    197461364(0xbc50574) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    197461364(0xbc50574) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    197461364(0xbc50574) KB            
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    197461364(0xbc50574) KB            
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
  Uuid:                    GPU-defd142329fa1f3a               
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
  Max Clock Freq. (MHz):   2526                               
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
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 542                                
  SDMA engine uCode::      24                                 
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
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
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             


### Additional Information

[rocm_bug_report_package_updated.tar.gz](https://github.com/user-attachments/files/21156782/rocm_bug_report_package_updated.tar.gz)