# Inconsistent information by rocminfo and Vega FE

- **Issue #:** 454
- **State:** closed
- **Created:** 2018-07-08T04:46:04Z
- **Updated:** 2023-12-18T18:19:07Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/454

Hi,

rocminfo reports:
```
 Name:                    gfx900                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
[...]                   
  Max Clock Frequency (MHz):1600                               
  BDFID:                   2816                               
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE    
```
in Agent section, but

```
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE          
```

in ISA section.

Shouldn't rocm report `Fast F16 Operation: TRUE`?

I believe the issue was already reported as #274 about 6 months ago.