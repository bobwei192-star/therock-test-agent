# Radeon GPU Profiler support?

- **Issue #:** 1143
- **State:** closed
- **Created:** 2020-06-09T09:30:32Z
- **Updated:** 2020-06-25T13:45:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1143

I was trying to profile some OpenCL code using the Radeon GPU Profiler (RGP), while using ROCm and had no success doing so. In the end I assumed, that it might have been because I am not using the closed source AMD driver on Linux.

I know there is the `rocprof`, however, compared to RGP, it can be cumbersome to display the data in a similar fashion to the built in GUI of RGP. 

If RGP should work with ROCm, then I have a problem seeing the "Active Processes" after connecting successfully. 
If RGP is not currently supposed to work with ROCm, are there then any plans to "integrate" the two? Maybe get RGP to understand the .csv files that rocprof outputs.
Or could ROCm rocprof get its own GUI similar to RGP or the now deprecated CodeXL?