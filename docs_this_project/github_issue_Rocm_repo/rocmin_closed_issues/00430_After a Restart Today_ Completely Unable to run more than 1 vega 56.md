# After a Restart Today, Completely Unable to run more than 1 vega 56

- **Issue #:** 430
- **State:** closed
- **Created:** 2018-06-06T10:56:12Z
- **Updated:** 2018-06-06T12:50:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/430

I have been using 6 vega 56 with asus b250 mining with rocm perfectly for the last two days. I had to restart ubuntu for updates and after that, although rocm recognizes the cards, they dont hash. The only card that hashes is the one on the pcie3.0 slot. I am out of ideas, I have reinstalled ubuntu 10 times nothing, still only one out of 6 cards mine. I am unsure what else to do. Please help. I have even tried with 2 cards only, and only 1 hashes.

Stats GPU 0 - lyra2z: 5.628Mh/s (5.609Mh/s)  
[2018-06-06 03:54:09] Stats GPU 1 - 
[2018-06-06 03:54:09] Stats Total - lyra2z: 5.628Mh/s (5.609Mh/s)  

GPU 0 is always the only card hashing. 0 is on the pcie3.0 slot.

I followed these instructions as usual - which worked perfectly the last two days: https://github.com/RadeonOpenCompute/ROCm

./rocm-smi shows:
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   N/A     N/A      N/A      N/A      0%       N/A       N/A      
  2   35.0c   15.0W    1474Mhz  800Mhz   70.98%   manual    0%       
  0   59.0c   150.0W   1312Mhz  800Mhz   70.98%   manual    0%       
================================================================================
====================           End of ROCm SMI Log          ====================

As you can see only gpu 0 is working. 

Any help is appreciated.

Thank you!