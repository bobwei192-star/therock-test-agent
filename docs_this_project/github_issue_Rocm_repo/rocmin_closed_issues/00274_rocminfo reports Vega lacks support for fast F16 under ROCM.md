# rocminfo reports Vega lacks support for fast F16 under ROCM..

- **Issue #:** 274
- **State:** closed
- **Created:** 2017-12-20T07:24:04Z
- **Updated:** 2018-06-03T15:24:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/274

don't know is cosmetic issue but you can see
" Fast F16 Operation:      FALSE   "

```
******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26751                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1630                               
  BDFID:                   1024                               
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE   

```