# [Issue]: BF16 VAE poor performance

- **Issue #:** 5191
- **State:** open
- **Created:** 2025-08-13T00:46:00Z
- **Updated:** 2025-12-23T16:41:53Z
- **Labels:** Feature Request, Under Investigation
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5191

### Problem Description

I observed that BF16 VAE is much slower than FP16 and is more prone to OOM.  


### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

7950X

### GPU

AMD Radeon RX7900XTX

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

Execute the following Python file, which can calculate the performance overhead  

```shell
# I found these environment variables from related cases on the Internet, but they didn't seem to bring any improvement.
export PYTORCH_HIP_ALLOC_CONF=expandable_segments:True
export HIPDNN_BENCHMARK=1
export MIOPEN_FIND_MODE=2
python vae_benchmark.py
```

```python
import torch
from diffusers import AutoencoderKL
from PIL import Image
import time
import torchvision.transforms as T
from collections import defaultdict

class ModuleTimer:
    def __init__(self):
        self.module_times = defaultdict(float)
        self.module_counts = defaultdict(int)
        self.module_peak_mems = defaultdict(float) # Store peak memory for each module
        self.handles = []
        self.current_module_name = None
        self.start_time = None

    def _pre_hook(self, module, input):
        torch.cuda.synchronize()
        self.start_time = time.time()
        # Reset peak memory stats before each module call to get accurate peak for that module
        torch.cuda.reset_peak_memory_stats(torch.cuda.current_device())

    def _post_hook(self, module, input, output):
        torch.cuda.synchronize()
        end_time = time.time()
        if self.start_time is not None: # Ensure timing started
            duration = end_time - self.start_time
            peak_mem = torch.cuda.max_memory_allocated(torch.cuda.current_device()) / (1024 ** 2)
            
            self.module_times[self.current_module_name] += duration
            self.module_counts[self.current_module_name] += 1
            # Store the maximum peak memory observed for this module
            self.module_peak_mems[self.current_module_name] = max(self.module_peak_mems[self.current_module_name], peak_mem)
            
        self.start_time = None
        self.current_module_name = None # Reset for next module

    def register_hooks(self, model):
        for name, module in model.named_modules():
            if not list(module.children()): # Only register to leaf modules
                # Bind the module name to the pre-hook and post-hook
                def pre_hook_closure(mod, inp, module_name=name):
                    self.current_module_name = module_name
                    self._pre_hook(mod, inp)
                
                def post_hook_closure(mod, inp, out, module_name=name):
                    self.current_module_name = module_name # Ensure correct name for post_hook
                    self._post_hook(mod, inp, out)

                handle_pre = module.register_forward_pre_hook(pre_hook_closure)
                self.handles.append(handle_pre)
                handle_post = module.register_forward_hook(post_hook_closure)
                self.handles.append(handle_post)

    def remove_hooks(self):
        for handle in self.handles:
            handle.remove()
        self.handles = []

    def get_average_times(self):
        avg_times = {}
        for name, total_time in self.module_times.items():
            if self.module_counts[name] > 0:
                avg_times[name] = total_time / self.module_counts[name]
        return avg_times

def benchmark_vae_performance(model, image_tensor, dtype, device='cuda'):
    """
    Benchmarks the VAE performance for a given data type, including time and memory.
    Reports separate metrics for a warm-up run and subsequent timed runs,
    with fine-grained timing for each module using forward hooks.
    """
    print(f"--- Benchmarking {dtype} ---")
    try:
        model.to(device).to(dtype)
        image_tensor = image_tensor.to(device).to(dtype)

        # --- Warm-up Run (Full Encode/Decode) ---
        torch.cuda.reset_peak_memory_stats(device)
        torch.cuda.synchronize(device)
        start_time = time.time()
        with torch.no_grad():
            latents = model.encode(image_tensor).latent_dist.sample()
            _ = model.decode(latents)
        torch.cuda.synchronize(device)
        warmup_total_time = time.time() - start_time
        warmup_total_mem = torch.cuda.max_memory_allocated(device) / (1024 ** 2)
        print(f"Warm-up (Full) -> Total Time: {warmup_total_time:.4f}s, Peak Memory: {warmup_total_mem:.2f} MB")

        # --- Fine-grained Timed Runs (10 runs) ---
        encoder_timer = ModuleTimer()
        decoder_timer = ModuleTimer()

        encoder_timer.register_hooks(model.encoder)
        decoder_timer.register_hooks(model.decoder)
        
        print("\n--- Fine-grained Timed Runs (Avg of 10) ---")
        for i in range(10):
            # Reset memory stats for the entire run before each full encode/decode cycle
            torch.cuda.reset_peak_memory_stats(device) 
            with torch.no_grad():
                latents = model.encode(image_tensor).latent_dist.sample()
                _ = model.decode(latents)
            # No need to track peak_mem_fine_grained here, as ModuleTimer tracks per-module peak mem

        encoder_avg_times = encoder_timer.get_average_times()
        decoder_avg_times = decoder_timer.get_average_times()
        encoder_peak_mems = encoder_timer.module_peak_mems
        decoder_peak_mems = decoder_timer.module_peak_mems

        encoder_timer.remove_hooks()
        decoder_timer.remove_hooks()

        return {
            'warmup_total_time': warmup_total_time,
            'warmup_total_mem_mb': warmup_total_mem,
            'fine_grained_encoder_times': encoder_avg_times,
            'fine_grained_decoder_times': decoder_avg_times,
            'fine_grained_encoder_mems': encoder_peak_mems,
            'fine_grained_decoder_mems': decoder_peak_mems,
        }

    except Exception as e:
        print(f"Failed to benchmark {dtype}: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    image_path = "image_a.jpg" # Replace with any image path
    model_id = "madebyollin/sdxl-vae-fp16-fix"
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if device == 'cpu':
        print("CUDA not available.")
        return
    
    print(f"Loading VAE model: {model_id}")
    vae = AutoencoderKL.from_pretrained(model_id)
    
    print(f"Loading image: {image_path}")
    image = Image.open(image_path).convert("RGB")
    
    transform = T.Compose([
        T.Resize((1024, 1024)),
        T.ToTensor(),
        T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    image_tensor = transform(image).unsqueeze(0)

    results = {}
    
    results['fp16'] = benchmark_vae_performance(vae, image_tensor, torch.float16, device)

    if torch.cuda.is_available() and torch.cuda.is_bf16_supported():
        results['bf16'] = benchmark_vae_performance(vae, image_tensor, torch.bfloat16, device)
    else:
        print("\n--- Benchmarking bf16 ---")
        print("Skipping bfloat16 benchmark: Not supported on this hardware.")

    print("\n--- Final Benchmark Summary ---")
    for dtype, data in results.items():
        if data:
            print(f"{dtype.upper()}:")
            print(f"  Warm-up (Full) -> Total Time: {data['warmup_total_time']:.4f}s, Peak Memory: {data['warmup_total_mem_mb']:.2f} MB")
            print("  Fine-grained Encoder Times (Avg per call):")
            for k, v in sorted(data['fine_grained_encoder_times'].items(), key=lambda item: item[1], reverse=True):
                print(f"    {k:<40}: {v:.6f}s")
            print("  Fine-grained Encoder Peak Memory (per call):")
            for k, v in sorted(data['fine_grained_encoder_mems'].items(), key=lambda item: item[1], reverse=True):
                print(f"    {k:<40}: {v:.2f} MB")
            print("  Fine-grained Decoder Times (Avg per call):")
            for k, v in sorted(data['fine_grained_decoder_times'].items(), key=lambda item: item[1], reverse=True):
                print(f"    {k:<40}: {v:.6f}s")
            print("  Fine-grained Decoder Peak Memory (per call):")
            for k, v in sorted(data['fine_grained_decoder_mems'].items(), key=lambda item: item[1], reverse=True):
                print(f"    {k:<40}: {v:.2f} MB")
    print("-----------------------------")

    # Calculate and print BF16/FP16 ratios for each module
    if 'fp16' in results and results['fp16'] and 'bf16' in results and results['bf16']:
        print("\n--- BF16 / FP16 Performance Ratios (Time and Memory) ---")
        fp16_enc_times = results['fp16']['fine_grained_encoder_times']
        bf16_enc_times = results['bf16']['fine_grained_encoder_times']
        fp16_dec_times = results['fp16']['fine_grained_decoder_times']
        bf16_dec_times = results['bf16']['fine_grained_decoder_times']

        fp16_enc_mems = results['fp16']['fine_grained_encoder_mems']
        bf16_enc_mems = results['bf16']['fine_grained_encoder_mems']
        fp16_dec_mems = results['fp16']['fine_grained_decoder_mems']
        bf16_dec_mems = results['bf16']['fine_grained_decoder_mems']

        print("\nEncoder Module Ratios (BF16 / FP16):")
        all_encoder_modules = sorted(set(fp16_enc_times.keys()) | set(bf16_enc_times.keys()))
        for module_name in all_encoder_modules:
            fp16_time = fp16_enc_times.get(module_name, 0)
            bf16_time = bf16_enc_times.get(module_name, 0)
            fp16_mem = fp16_enc_mems.get(module_name, 0)
            bf16_mem = bf16_enc_mems.get(module_name, 0)

            time_ratio = bf16_time / fp16_time if fp16_time > 0 else float('nan')
            mem_ratio = bf16_mem / fp16_mem if fp16_mem > 0 else float('nan')
            
            time_ratio_str = f"{time_ratio:.3f}"
            mem_ratio_str = f"{mem_ratio:.3f}"

            # Apply red color if ratio is significantly higher than 1.0 (e.g., > 1.1)
            if time_ratio > 1.1:
                time_ratio_str = f"\033[91m{time_ratio_str}\033[0m" # Red color
            if mem_ratio > 1.1:
                mem_ratio_str = f"\033[91m{mem_ratio_str}\033[0m" # Red color
            
            print(f"  {module_name:<40}: Time Ratio={time_ratio_str}, Memory Ratio={mem_ratio_str}")

        print("\nDecoder Module Ratios (BF16 / FP16):")
        all_decoder_modules = sorted(set(fp16_dec_times.keys()) | set(bf16_dec_times.keys()))
        for module_name in all_decoder_modules:
            fp16_time = fp16_dec_times.get(module_name, 0)
            bf16_time = bf16_dec_times.get(module_name, 0)
            fp16_mem = fp16_dec_mems.get(module_name, 0)
            bf16_mem = bf16_dec_mems.get(module_name, 0)

            time_ratio = bf16_time / fp16_time if fp16_time > 0 else float('nan')
            mem_ratio = bf16_mem / fp16_mem if fp16_mem > 0 else float('nan')
            
            time_ratio_str = f"{time_ratio:.3f}"
            mem_ratio_str = f"{mem_ratio:.3f}"

            # Apply red color if ratio is significantly higher than 1.0 (e.g., > 1.1)
            if time_ratio > 1.1:
                time_ratio_str = f"\033[91m{time_ratio_str}\033[0m" # Red color
            if mem_ratio > 1.1:
                mem_ratio_str = f"\033[91m{mem_ratio_str}\033[0m" # Red color
            
            print(f"  {module_name:<40}: Time Ratio={time_ratio_str}, Memory Ratio={mem_ratio_str}")
    else:
        print("\nCould not calculate BF16 / FP16 ratios: Missing data.")

if __name__ == "__main__":
    main()

```

It's important to note that BF16 requires more time and VRAM than FP16 in some aspects, especially conv_out which can be up to ten times higher.
Be like:
<img width="852" height="601" alt="Image" src="https://github.com/user-attachments/assets/ce5919f2-856a-4808-9e99-5df4aaf77575" />


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
  Name:                    AMD Ryzen 9 7950X 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 7950X 16-Core Processor
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
  Max Clock Freq. (MHz):   5883                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    97950900(0x5d69cb4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    97950900(0x5d69cb4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    97950900(0x5d69cb4) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    97950900(0x5d69cb4) KB             
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
  Uuid:                    GPU-08ca8cb142948e79               
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
*******                  
Agent 3                  
*******                  
  Name:                    gfx1036                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon Graphics                
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      256(0x100) KB                      
  Chip ID:                 5710(0x164e)                       
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   6400                               
  Internal Node ID:        2                                  
  Compute Unit:            2                                  
  SIMDs per CU:            2                                  
  Shader Engines:          1                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       APU
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
  Packet Processor uCode:: 22                                 
  SDMA engine uCode::      9                                  
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    48975448(0x2eb4e58) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    48975448(0x2eb4e58) KB             
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
      Name:                    amdgcn-amd-amdhsa--gfx1036         
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
      Name:                    amdgcn-amd-amdhsa--gfx10-3-generic 
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

_No response_