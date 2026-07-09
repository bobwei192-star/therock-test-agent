# kernel memory leak? (ROCm 1.6.115)

- **Issue #:** 176
- **State:** closed
- **Created:** 2017-08-02T06:56:24Z
- **Updated:** 2018-06-03T14:54:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/176

Hello,
recently I found out that I am losing RAM and I can't get it back by closing programs. The only bigger change to my system was updating ROCm (kernel 4.9 to 4.11).
Anyone else noticed this issue?
(using ubuntu 16.04)

The following data is after less than 24 hours, and not working with gpu (just desktop, browser and some text editors)
When i close all programs, system is still using around 4 GB of memory
see "total size", kernel is takinga 2.9 GB of memory
slabtop
```
Active / Total Objects (% used)    : 9824285 / 9902782 (99.2%)
 Active / Total Slabs (% used)      : 324643 / 324643 (100.0%)
 Active / Total Caches (% used)     : 74 / 95 (77.9%)
 Active / Total Size (% used)       : 2888893.34K / 2904551.59K (99.5%)
 Minimum / Average / Maximum Object : 0.01K / 0.29K / 18.62K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME                   
2124486 2124486 100%    0.19K 101166       21    404664K kmalloc-192
1569945 1558847  99%    0.10K  40255       39    161020K buffer_head
1084992 1084643  99%    0.25K  33906       32    271248K kmalloc-256
1072192 1072120  99%    0.50K  33506       32    536096K kmalloc-512
1069376 1069376 100%    1.00K  33418       32   1069376K kmalloc-1024
1069320 1069281  99%    0.09K  25460       42    101840K kmalloc-96
1066848 1066848 100%    0.12K  33339       32    133356K kmalloc-128
101976  96939  95%    0.57K   3642       28     58272K radix_tree_node
 96096  87523  91%    0.19K   4576       21     18304K dentry
...
```

amdgpu is using 2.5 GB of memory
```
lsmod | grep amd
amdkfd                212992  1
amd_iommu_v2           20480  1 amdkfd
amdgpu               2523136  254
...
```

meminfo reports 2.6 GB unreclaimable slab (SUnreclaim)
```
cat /proc/meminfo
MemTotal:       16383964 kB
MemFree:         1621620 kB
MemAvailable:    8957684 kB
Buffers:         1057460 kB
Cached:          6388512 kB
...
Slab:            2920576 kB
SReclaimable:     319692 kB
SUnreclaim:      2600884 kB
...
```

Also, i was off work for 2 weeks, the computer was on and slabtop reported used 10GB memory - around 9GB of "SUnreclaim" in meminfo