# what is the key issue for GCNs

- **Issue #:** 1456
- **State:** closed
- **Created:** 2021-04-18T04:49:18Z
- **Updated:** 2021-06-04T04:26:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/1456

now i am try to optimize OCL code on GCN GPU, and want to know some VRAM detail.
I cannot understand the GCN's memory archietecture.
nomally,MMU wont affect the memory IO bandwidth if memory  address is page aligned.
but according to the description in https://github.com/RadeonOpenCompute/ROCm/issues/147
2MB fragments  will enhance bandwidth will enhance vega's bandwidth from 260GB/s to 400+GB/s
I check the driver code, it seam that 2MB fragment forcing BO allocated base address being 2MB align, and GMC PTE set fragment according to fragment size.
But it should not affect the bandwidth so much.
during continuous page-align virtual mem loading, the key issue should be memory bank/channel confliction.
why fragmention setting cause so much memory bandwidth diff? 
does it because the translating from virutal to phy address handled by software,  nor hw like cpu's MMU?
BTW: what is the interleaving mode for GCN's memory?
row--bank--channel--col or some other mode?the mode is fixed by hardware or can be adjusted by driver?

thanks