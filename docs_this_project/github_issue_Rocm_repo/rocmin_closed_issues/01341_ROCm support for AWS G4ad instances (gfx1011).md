# ROCm support for AWS G4ad instances (gfx1011)

- **Issue #:** 1341
- **State:** closed
- **Created:** 2020-12-17T23:08:36Z
- **Updated:** 2021-12-07T18:37:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/1341

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