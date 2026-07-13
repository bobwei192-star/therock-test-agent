# [Issue]: rocm-smi shows inconsistent VRAM for partitioned MI300A and MI300X

- **Issue #:** 4750
- **State:** closed
- **Created:** 2025-05-17T06:36:43Z
- **Updated:** 2025-05-21T19:35:32Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4750

### Problem Description

When a MI300A is in a non-SPX mode, rocm-smi shows the memory of each individual partition as `<total_gpu_memory>/<number_of_partitions>`.
When a MI300X is in a non-SPX mode, rocm-smi shows the memory of each individual partition as `<total_gpu_memory>`.

The same happens with amd-smi and when we use the rocm/amd-smi API directly.
I've tried various modes (even NPS4 on the MI300X) and ROCm 6.3 - 6.4.

Is this expected? Or is it a bug?

MI300A SPX mode:

```
$ amd-smi version
AMDSMI Tool: 24.7.1+8dc45db | AMDSMI Library version: 25.1.0.0 | ROCm version: 6.3.3

$ rocm-smi -i


============================ ROCm System Management Interface ============================
=========================================== ID ===========================================
GPU[0]		: Device Name: 		AMD Instinct MI300A
GPU[0]		: Device ID: 		0x74a0
GPU[0]		: Device Rev: 		0x00
GPU[0]		: Subsystem ID: 	0x74a0
GPU[0]		: GUID: 		32223
==========================================================================================
================================== End of ROCm SMI Log ===================================

$ rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK   MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  
==========================================================================================================================
0       1     0x74a0,   32223  32.0°C      127.0W    NPS1, SPX, 0        95Mhz  1300Mhz  0%   auto  550.0W  0%     0%    
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================


$ rocm-smi --showmeminfo vram


============================ ROCm System Management Interface ============================
================================== Memory Usage (Bytes) ==================================
GPU[0]		: VRAM Total Memory (B): 100742320128
GPU[0]		: VRAM Total Used Memory (B): 8388608
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

MI300A TPX mode:

```
$ rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK    MCLK     Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                   
==========================================================================================================================
0       1     0x74a0,   39408  32.0°C      125.0W    NPS1, TPX, 0        94Mhz   1300Mhz  0%   auto  550.0W  0%     0%    
1       2     0x74a0,   8689   32.0°C      125.0W    NPS1, TPX, 1        95Mhz   1300Mhz  0%   auto  550.0W  0%     0%    
2       3     0x74a0,   43505  32.0°C      125.0W    NPS1, TPX, 2        100Mhz  1300Mhz  0%   auto  550.0W  0%     0%    
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================


$ rocm-smi --showmeminfo vram


============================ ROCm System Management Interface ============================
================================== Memory Usage (Bytes) ==================================
GPU[0]		: VRAM Total Memory (B): 33580773376
GPU[0]		: VRAM Total Used Memory (B): 8388608
GPU[1]		: VRAM Total Memory (B): 33580773376
GPU[1]		: VRAM Total Used Memory (B): 8388608
GPU[2]		: VRAM Total Memory (B): 33580773376
GPU[2]		: VRAM Total Used Memory (B): 8388608
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

MI300X SPX mode:

```
$ amd-smi version
AMDSMI Tool: 24.7.1+8dc45db | AMDSMI Library version: 25.1.0.0 | ROCm version: 6.3.3

$ rocm-smi -i


============================ ROCm System Management Interface ============================
=========================================== ID ===========================================
GPU[0]		: Device Name: 		AMD Instinct MI300X OAM
GPU[0]		: Device ID: 		0x74a1
GPU[0]		: Device Rev: 		0x00
GPU[0]		: Subsystem ID: 	0x74a1
GPU[0]		: GUID: 		28851
==========================================================================================
================================== End of ROCm SMI Log ===================================

$ rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK    MCLK    Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  
==========================================================================================================================
0       2     0x74a1,   28851  47.0°C      133.0W    NPS1, SPX, 0        126Mhz  900Mhz  0%   auto  750.0W  0%     0%    
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================
root@7c6438444a9e:/# rocm-smi --showmeminfo vram


============================ ROCm System Management Interface ============================
================================== Memory Usage (Bytes) ==================================
GPU[0]		: VRAM Total Memory (B): 206141652992
GPU[0]		: VRAM Total Used Memory (B): 297771008
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

MI300X QPX mode:

```
$ rocm-smi


============================================ ROCm System Management Interface ============================================
====================================================== Concise Info ======================================================
Device  Node  IDs              Temp        Power     Partitions          SCLK    MCLK    Fan  Perf  PwrCap  VRAM%  GPU%  
              (DID,     GUID)  (Junction)  (Socket)  (Mem, Compute, ID)                                                  
==========================================================================================================================
0       2     0x74a1,   1971   47.0°C      133.0W    NPS1, QPX, 0        126Mhz  900Mhz  0%   auto  750.0W  0%     0%    
1       3     0x74a1,   49074  47.0°C      133.0W    NPS1, QPX, 1        136Mhz  900Mhz  0%   auto  750.0W  0%     0%    
2       4     0x74a1,   14258  47.0°C      133.0W    NPS1, QPX, 2        136Mhz  900Mhz  0%   auto  750.0W  0%     0%    
3       5     0x74a1,   36787  47.0°C      133.0W    NPS1, QPX, 3        153Mhz  900Mhz  0%   auto  750.0W  0%     0%     
==========================================================================================================================
================================================== End of ROCm SMI Log ===================================================

$ rocm-smi --showmeminfo vram


============================ ROCm System Management Interface ============================
================================== Memory Usage (Bytes) ==================================
GPU[0]		: VRAM Total Memory (B): 206141652992
GPU[0]		: VRAM Total Used Memory (B): 297771008
GPU[1]		: VRAM Total Memory (B): 206141652992
GPU[1]		: VRAM Total Used Memory (B): 297771008
GPU[2]		: VRAM Total Memory (B): 206141652992
GPU[2]		: VRAM Total Used Memory (B): 297771008
GPU[3]		: VRAM Total Memory (B): 206141652992
GPU[3]		: VRAM Total Used Memory (B): 297771008
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

### Operating System

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 9654 96-Core Processor

### GPU

MI300A/MI300X

### ROCm Version

6.3.0-6.4.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_