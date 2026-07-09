# [Issue]: `amd-smi partition` returns `N/A` for almost all fields

- **Issue #:** 4477
- **State:** open
- **Created:** 2025-03-10T19:49:42Z
- **Updated:** 2025-06-25T15:38:54Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4477

### Problem Description

What information is supposed to be returned from `amd-smi partition`?

When I run `amd-smi partition` I get the following:

```
~$ amd-smi partition
CURRENT_PARTITION:
GPU_ID       MEMORY  ACCELERATOR_TYPE  ACCELERATOR_PROFILE_INDEX  PARTITION_ID  
0            NPS1    N/A               N/A                        N/A
1            NPS1    N/A               N/A                        N/A
2            NPS1    N/A               N/A                        N/A
3            NPS1    N/A               N/A                        N/A
GPU: 0
    MEMORY_PARTITION:
        CAPS: N/A
        CURRENT: NPS1

GPU: 1
    MEMORY_PARTITION:
        CAPS: N/A
        CURRENT: NPS1

GPU: 2
    MEMORY_PARTITION:
        CAPS: N/A
        CURRENT: NPS1

GPU: 3
    MEMORY_PARTITION:
        CAPS: N/A
        CURRENT: NPS1


ACCELERATOR_PARTITION_PROFILES:
GPU_ID       PROFILE_INDEX  MEMORY_PARTITION_CAPS  ACCELERATOR_TYPE  PARTITION_ID  NUM_PARTITIONS  NUM_RESOURCES  RESOURCE_INDEX  RESOURCE_TYPE  RESOURCE_INSTANCES  RESOURCES_SHARED  
0            N/A            N/A                    N/A               N/A           0               N/A            N/A             N/A            N/A                 N/A
1            N/A            N/A                    N/A               N/A           0               N/A            N/A             N/A            N/A                 N/A
2            N/A            N/A                    N/A               N/A           0               N/A            N/A             N/A            N/A                 N/A
3            N/A            N/A                    N/A               N/A           0               N/A            N/A             N/A            N/A                 N/A
```

which basically only tells me that all four devices are using one NUMA node per socket.

I get similar outputs for MI210 and W7800. Is this intended behavior?



### Operating System

Rocky Linux 9.5 (Blue Onyx) x86_64

### CPU

4 x AMD Instinct MI300A Accelerator (192) @ 3.70 GHz

### GPU

4 x AMD Instinct MI300A Accelerator, 1 x AMD Instinct MI210 Accelerator, 1 x AMD Radeon PRO W7800

### ROCm Version

ROCm 6.3.3

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_