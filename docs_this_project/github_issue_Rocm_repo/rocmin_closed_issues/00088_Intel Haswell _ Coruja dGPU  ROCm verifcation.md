# Intel Haswell + Coruja dGPU  ROCm verifcation

- **Issue #:** 88
- **State:** closed
- **Created:** 2017-02-22T12:12:23Z
- **Updated:** 2017-07-02T01:47:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/88

Hi, 
I try to run ROCm vector_copy on Intel Haswell + Coruja dGPU combination. Vector_copy works fine. But i am suspecting with Virtual CRAT table creation .

Do we need separate BIOS to support CRAT table for Intel Haswell ?


[    4.691934] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    4.718973] AMD IOMMUv2 functionality not available on this system
[    4.747848] CRAT table not found
[    4.774840] Virtual CRAT table created for CPU
[    4.932931] Parsing CRAT table with 1 nodes
[    4.958942] Creating topology SYSFS entries
[    4.985162] Topology: Add CPU node
[    5.011497] Finished initializing topology
[    5.039518] kfd kfd: Initialized module