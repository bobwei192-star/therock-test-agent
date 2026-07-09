# Info about cl_amd_assembly_program?

- **Issue #:** 405
- **State:** closed
- **Created:** 2018-05-08T05:22:39Z
- **Updated:** 2018-05-09T04:13:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/405

Hi,
finally installed ROCM 1.7.2 on Ubuntu 18.04 via kernel 4.13 from PPA..
now seeing clinfo I see:
version  2576.0 (HSA1.1,LC)
and a new extension  cl_amd_assembly_program ..
searching seems it has clCreateProgramWithAssemblyAMD but quick inspection 
on api/opencl/amdocl/cl_program.cpp doesn't reveal many details..

that allows inline assembly?
also there is some sample of using it?

thanks..
