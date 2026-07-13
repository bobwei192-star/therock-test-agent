# atomicAnd doesn't seem to work in this code

- **Issue #:** 848
- **State:** closed
- **Created:** 2019-07-18T05:47:40Z
- **Updated:** 2024-05-23T15:30:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/848

Attached is a C++ source file for HIP that doesn't seem to work as expected. 

[test_output.txt](https://github.com/RadeonOpenCompute/ROCm/files/3404896/test_output.txt)
[test.cpp.txt](https://github.com/RadeonOpenCompute/ROCm/files/3404897/test.cpp.txt)
[test-000-gfx900.isa.txt](https://github.com/RadeonOpenCompute/ROCm/files/3404940/test-000-gfx900.isa.txt)

I compile with: 
     /opt/rocm/hip/bin/hipcc test.cpp  -o test -I.

Attached are the CPP file, the output (just from standard out), and the gcn-assembly file created from "extractkernel -i test".

The expected output is for all bits to be set to zero. However, all bits remain 0xFFFFFFFF after the code is run. I've "extraced" three variables into the "DebugHelp" array, which should make this code easier to understand. These three are set with the following procedure: 

        if(__ockl_activelane_u32() == 0){
            // These three debug-help functions will print
            // bitNum: 0x3f
            // BitNum_idx: 1
            // bitNum_bit: 0xfffffffe
            // So at very least, bitmask[1] should have the bottom bit clear
            // from the atomicAnd earlier. But not even that bit is clear
            debug_help[0] = bitNum;
            debug_help[1] = bitNum_idx;
            debug_help[2] = ~bitNum_bit;
            __threadfence_block();
            tail -= numBitsRemoved;
        }

Given the output, I would expect bitmask[1] to have at least one bit clear. But alas, bitmask[1] is still all 0xFFFFFFFF after the procedure ends. The key bug seems to be: 

        // This atomic and here doesn't seem to work at all
        // The bits stay at "1" despite this atomicAnd running
        atomicAnd(&bitmask[bitNum_idx], ~bitNum_bit);

Line 25.

I've checked the assembly: 

    v_lshrrev_b32_e64 v6, v3, s6                               // 0000000011D0: D1100006 00000D03
    v_lshlrev_b32_e32 v3, 2, v1                                // 0000000011D8: 24060282
    v_add_co_u32_e32 v3, vcc, s2, v3                           // 0000000011DC: 32060602
    v_addc_co_u32_e32 v4, vcc, v4, v2, vcc                     // 0000000011E0: 38080504
    v_not_b32_e32 v2, v6                                       // 0000000011E4: 7E045706
    global_atomic_and v[3:4], v2, off                          // 0000000011E8: DD208000 007F0203
    v_cmp_eq_u32_e32 vcc, 0, v5                                // 0000000011F0: 7D940A80
    s_and_saveexec_b64 s[10:11], vcc                           // 0000000011F4: BE8A206A
    s_cbranch_execz BB0_6                                      // 0000000011F8: BF880011

It appears that the "global_atomic_and" is in fact created. "v2" was "logical-not" in the line before (v_not_b32_e32), so v2 probably correlates to the bitNum_bit variable.

I thought this might be a global data-race, so I forced an s_waitcnt with: 

        asm volatile(
            "s_waitcnt vmcnt(0) lgkmcnt(0) \n"
            );

This didn't seem to fix anything however.

-----------


	 rocminfo 
	=====================    
	HSA System Attributes    
	=====================    
	Runtime Version:         1.1
	System Timestamp Freq.:  1000.000000MHz
	Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
	Machine Model:           LARGE                              
	System Endianness:       LITTLE                             

	==========               
	HSA Agents               
	==========               
	*******                  
	Agent 1                  
	*******                  
	  Name:                    AMD Ryzen Threadripper 1950X 16-Core Processor
	  Vendor Name:             CPU                                
	  Feature:                 None specified                     
	  Profile:                 FULL_PROFILE                       
	  Float Round Mode:        NEAR                               
	  Max Queue Number:        0                                  
	  Queue Min Size:          0                                  
	  Queue Max Size:          0                                  
	  Queue Type:              MULTI                              
	  Node:                    0                                  
	  Device Type:             CPU                                
	  Cache Info:              
		L1:                      32768KB                            
	  Chip ID:                 0                                  
	  Cacheline Size:          64                                 
	  Max Clock Frequency (MHz):3400                               
	  BDFID:                   0                                  
	  Compute Unit:            16                                 
	  Features:                None
	  Pool Info:               
		Pool 1                   
		  Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
		  Size:                    16379596KB                         
		  Allocatable:             TRUE                               
		  Alloc Granule:           4KB                                
		  Alloc Alignment:         4KB                                
		  Acessible by all:        TRUE                               
		Pool 2                   
		  Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
		  Size:                    16379596KB                         
		  Allocatable:             TRUE                               
		  Alloc Granule:           4KB                                
		  Alloc Alignment:         4KB                                
		  Acessible by all:        TRUE                               
	  ISA Info:                
		N/A                      
	*******                  
	Agent 2                  
	*******                  
	  Name:                    AMD Ryzen Threadripper 1950X 16-Core Processor
	  Vendor Name:             CPU                                
	  Feature:                 None specified                     
	  Profile:                 FULL_PROFILE                       
	  Float Round Mode:        NEAR                               
	  Max Queue Number:        0                                  
	  Queue Min Size:          0                                  
	  Queue Max Size:          0                                  
	  Queue Type:              MULTI                              
	  Node:                    1                                  
	  Device Type:             CPU                                
	  Cache Info:              
		L1:                      32768KB                            
	  Chip ID:                 0                                  
	  Cacheline Size:          64                                 
	  Max Clock Frequency (MHz):3400                               
	  BDFID:                   0                                  
	  Compute Unit:            16                                 
	  Features:                None
	  Pool Info:               
		Pool 1                   
		  Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
		  Size:                    16479856KB                         
		  Allocatable:             TRUE                               
		  Alloc Granule:           4KB                                
		  Alloc Alignment:         4KB                                
		  Acessible by all:        TRUE                               
		Pool 2                   
		  Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
		  Size:                    16479856KB                         
		  Allocatable:             TRUE                               
		  Alloc Granule:           4KB                                
		  Alloc Alignment:         4KB                                
		  Acessible by all:        TRUE                               
	  ISA Info:                
		N/A                      
	*******                  
	Agent 3                  
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
	  Node:                    2                                  
	  Device Type:             GPU                                
	  Cache Info:              
		L1:                      16KB                               
	  Chip ID:                 26751                              
	  Cacheline Size:          64                                 
	  Max Clock Frequency (MHz):1630                               
	  BDFID:                   17152                              
	  Compute Unit:            64                                 
	  Features:                KERNEL_DISPATCH 
	  Fast F16 Operation:      FALSE                              
	  Wavefront Size:          64                                 
	  Workgroup Max Size:      1024                               
	  Workgroup Max Size Per Dimension:
		Dim[0]:                  67109888                           
		Dim[1]:                  1124074496                         
		Dim[2]:                  0                                  
	  Grid Max Size:           4294967295                         
	  Waves Per CU:            40                                 
	  Max Work-item Per CU:    2560                               
	  Grid Max Size per Dimension:
		Dim[0]:                  4294967295                         
		Dim[1]:                  4294967295                         
		Dim[2]:                  4294967295                         
	  Max number Of fbarriers Per Workgroup:32                                 
	  Pool Info:               
		Pool 1                   
		  Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
		  Size:                    8372224KB                          
		  Allocatable:             TRUE                               
		  Alloc Granule:           4KB                                
		  Alloc Alignment:         4KB                                
		  Acessible by all:        FALSE                              
		Pool 2                   
		  Segment:                 GROUP                              
		  Size:                    64KB                               
		  Allocatable:             FALSE                              
		  Alloc Granule:           0KB                                
		  Alloc Alignment:         0KB                                
		  Acessible by all:        FALSE                              
	  ISA Info:                
		ISA 1                    
		  Name:                    amdgcn-amd-amdhsa--gfx900          
		  Machine Models:          HSA_MACHINE_MODEL_LARGE            
		  Profiles:                HSA_PROFILE_BASE                   
		  Default Rounding Mode:   NEAR                               
		  Default Rounding Mode:   NEAR                               
		  Fast f16:                TRUE                               
		  Workgroup Max Dimension: 
			Dim[0]:                  67109888                           
			Dim[1]:                  1024                               
			Dim[2]:                  16777217                           
		  Workgroup Max Size:      1024                               
		  Grid Max Dimension:      
			x                        4294967295                         
			y                        4294967295                         
			z                        4294967295                         
		  Grid Max Size:           4294967295                         
		  FBarrier Max Size:       32                                 
	*** Done ***             


	hipcc --version
	HIP version: 1.5.19255
	HCC clang version 9.0.0 (/data/jenkins_workspace/compute-rocm-rel-2.6/external/hcc-tot/clang fff0bd8ccc310cbfec5e3e1bf516b81412081a71) (/data/jenkins_workspace/compute-rocm-rel-2.6/external/hcc-tot/compiler a42c925d178d2a3cd6541769279b736c56b3f935) (based on HCC 1.3.19242-7496b9e-fff0bd8-a42c925 )
	Target: x86_64-unknown-linux-gnu
	Thread model: posix
	InstalledDir: /opt/rocm/hcc/bin
