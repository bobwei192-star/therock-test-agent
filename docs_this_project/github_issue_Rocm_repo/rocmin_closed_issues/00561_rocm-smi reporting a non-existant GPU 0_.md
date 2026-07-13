# rocm-smi reporting a non-existant GPU 0?

- **Issue #:** 561
- **State:** closed
- **Created:** 2018-09-27T13:14:01Z
- **Updated:** 2019-03-11T16:26:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/561

On my system with ROCm 1.9, I see the following output from `rocm-smi`:
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A        N/A
  1   55c     15.0W    852Mhz   167Mhz   10.98%   auto      0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```

Is the non-existent GPU 0 an artifact of the CPU being enumerated as an HSA agent?  Might be less confusing to filter it out of rocm-smi output.