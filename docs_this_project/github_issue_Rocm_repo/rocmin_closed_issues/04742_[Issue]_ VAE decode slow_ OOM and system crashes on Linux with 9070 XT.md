# [Issue]: VAE decode slow, OOM and system crashes on Linux with 9070 XT

- **Issue #:** 4742
- **State:** closed
- **Created:** 2025-05-15T08:54:20Z
- **Updated:** 2026-01-05T15:49:03Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4742

### Problem Description

When using  ComfyUI with any parameters with any workflow, you should get OOM or complete system crashes if using the standard VAEDecode node, same with the tiled decoder. Even 64x64 tiled decoder can result in crashes, but less frequently.

I could mitigate this by forcing all models but the VAE to unload, but even in that case, I get a lot of full system crashes and OOM. Sometimes, running the same workflow 2-3 times works...

Using --cpu-vae works but should not have to be used IMO.

I tried using torch 2.7 with ROCm 6.3, but I got the same issues. Before posting, I also read https://github.com/ROCm/ROCm/issues/4729 and https://github.com/ROCm/ROCm/issues/4443, but I believe this should be an issue on its own, as stated in https://github.com/ROCm/ROCm/issues/4729, because this is not limited to WSL.

EDIT: I could reproduce the crash, but I noticed nvtop reporting my GPU using PCIe 5.0x8, I will try to fix that and report back.
EDIT2: Switching to 5.0x16 improved loading times, but did not fix the error.
EDIT3: for t2v, --cpu-vae can be faster than tiled vae on the GPU.

I will update with comfyUI logs.

### Operating System

Arch Linux (6.14.6-arch1-1)

### CPU

AMD Ryzen 9 9950X3D 16-Core Processor

### GPU

AMD Radeon 9070 XT

### ROCm Version

6.4

### ROCm Component

_No response_

### Steps to Reproduce

- Install ROCm 6.4 on a fresh Arch Linux install from [opencl-amd-dev](https://aur.archlinux.org/packages/opencl-amd-dev), 
- Install pytorch for ROCm 6.4 from https://pytorch.org/get-started/locally/,
- Install latest version of ComfyUI and download required models,
- Launch ComfyUI with any parameters (I tried a lot of combination, none solve the problem, maybe ` TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 PYTORCH_HIP_ALLOC_CONF=expandable_segments:True micromamba run -n comfyui python main.py --use-pytorch-cross-attention --lowvram` is a bit better? still OOM and crashes)
- Try any workflow, I could reproduce this for text2video with Hunyuan and all the text2image with Flux.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
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
  Name:                    AMD Ryzen 9 9950X3D 16-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 9 9950X3D 16-Core Processor
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
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5756                               
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
      Size:                    96337528(0x5bdfe78) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    96337528(0x5bdfe78) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    96337528(0x5bdfe78) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    96337528(0x5bdfe78) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-48cef9f706c81cb8               
  Marketing Name:          AMD Radeon Graphics                
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
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30032(0x7550)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2400                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
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
  Packet Processor uCode:: 1012                               
  SDMA engine uCode::      838                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16695296(0xfec000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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
  Chip ID:                 5056(0x13c0)                       
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          128(0x80)                          
  Max Clock Freq. (MHz):   2200                               
  BDFID:                   30208                              
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
      Size:                    48168764(0x2deff3c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    48168764(0x2deff3c) KB             
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
```

### Additional Information

When the system crashes, this is an example of one `journalctl -k -b -1`:
```
amdgpu 0000:03:00.0: amdgpu: 000000009f89a48b pin failed
 [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 amdgpu 0000:03:00.0: amdgpu: 000000000c9ee1f9 pin failed
 [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Not enough memory for command submission!
 [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Not enough memory for command submission!
 amdgpu 0000:03:00.0: amdgpu: 00000000b1a398a4 pin failed
 [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 amdgpu 0000:03:00.0: amdgpu: 000000002d5ba482 pin failed
 [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 amdgpu 0000:03:00.0: amdgpu: 0000000080f7bf1c pin failed
 [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 amdgpu 0000:03:00.0: amdgpu: 000000000c9ee1f9 pin failed
 [drm:amdgpu_dm_plane_helper_prepare_fb [amdgpu]] *ERROR* Failed to pin framebuffer with error -12
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc firefox(2852) task firefox:cs0(2770) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc plasma-systemmo(4082) task plasma-sys:cs0(4078) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc Xorg(1010) task Xorg:cs0(987) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc plasmashell(1362) task plasmashel:cs0(1342) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc (0) task (0) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc Xwayland(1233) task Xwayland:cs0(1218) is non-zero when fini
 amdgpu 0000:03:00.0: amdgpu: VM memory stats for proc kwin_wayland(1163) task kwin_wayla:cs0(1116) is non-zero when fini
```

ComfyUI logs:
```
!!! Exception during processing !!! Allocation on device 
Traceback (most recent call last):
  File "/home/zefresk/Documents/ComfyUI/execution.py", line 349, in execute
    output_data, output_ui, has_subgraph = get_output_data(obj, input_data_all, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb)
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/execution.py", line 224, in get_output_data
    return_values = _map_node_over_list(obj, input_data_all, obj.FUNCTION, allow_interrupt=True, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/execution.py", line 196, in _map_node_over_list
    process_inputs(input_dict, i)
  File "/home/zefresk/Documents/ComfyUI/execution.py", line 185, in process_inputs
    results.append(getattr(obj, func)(**inputs))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/nodes.py", line 1598, in decode
    video = vae.decode(
            ^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/diffusers/utils/accelerate_utils.py", line 46, in wrapper
    return method(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/autoencoder_kl_causal_3d.py", line 345, in decode
    decoded = self._decode(z).sample
              ^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/autoencoder_kl_causal_3d.py", line 309, in _decode
    return self.temporal_tiled_decode(z, return_dict=return_dict)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/autoencoder_kl_causal_3d.py", line 536, in temporal_tiled_decode
    decoded = self.spatial_tiled_decode(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/autoencoder_kl_causal_3d.py", line 462, in spatial_tiled_decode
    decoded = self.decoder(tile)
              ^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1755, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1766, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/vae.py", line 299, in forward
    sample = up_block(sample, latent_embeds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1755, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1766, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/unet_causal_3d_blocks.py", line 795, in forward
    hidden_states = upsampler(hidden_states)
                    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1755, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1766, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/unet_causal_3d_blocks.py", line 194, in forward
    hidden_states = self.conv(hidden_states)
                    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1755, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1766, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/Documents/ComfyUI/custom_nodes/comfyui-hunyuanvideowrapper/hyvideo/vae/unet_causal_3d_blocks.py", line 78, in forward
    return self.conv(x)
           ^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1755, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1766, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/zefresk/.local/share/mamba/envs/comfyui/lib/python3.12/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(
           ^^^^^^^^^
torch.OutOfMemoryError: Allocation on device 

Got an OOM, unloading all loaded models.
```