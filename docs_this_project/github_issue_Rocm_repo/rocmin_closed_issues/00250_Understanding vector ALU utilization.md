# Understanding vector ALU utilization

- **Issue #:** 250
- **State:** closed
- **Created:** 2017-11-12T22:09:46Z
- **Updated:** 2018-04-10T00:32:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/250

What is the best tool to analyze VALU utilization in an OpenCL kernel ?  

In my kernel, each work item `i` performs `Ni` passes through its data buffer `Bi`.  So, two work items may diverge while each item is running through its pass, and they also may diverge when they have a different number of passes, when the work item with fewer passes is waiting for the others to finish. 

I would like to understand what factor hurts the utilization the most.  

