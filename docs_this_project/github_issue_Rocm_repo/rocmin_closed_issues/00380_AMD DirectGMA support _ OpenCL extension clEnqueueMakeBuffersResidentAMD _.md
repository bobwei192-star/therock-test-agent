# AMD DirectGMA support ? OpenCL extension clEnqueueMakeBuffersResidentAMD ?

- **Issue #:** 380
- **State:** closed
- **Created:** 2018-04-04T09:49:13Z
- **Updated:** 2018-05-12T13:09:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/380

Dear all,

does RoCM amdgpu driver actually support DirectGMA ? I can compile but have error in clEnqueueMakeBuffersResidentAMD .
I don't see cl_amd_bus_addressable_memory extension with clinfo ?

in this code 1st line is ok
2nd line fired ERROR


`cl_mem busAddressableBuff_ = clCreateBuffer(context, CL_MEM_BUS_ADDRESSABLE_AMD, 1*1024, 0, &err);
if(err)printf(" error CL_MEM_BUS_ADDRESSABLE_AMD %d\n",err);
 // Get physical address
err = clEnqueueMakeBuffersResidentAMD(queue, 0, &busAddressableBuff_, true, &busAddr_, 0,0,0);
if(err)printf(" ERROR clEnqueueMakeBuffersResidentAMD%d\n",err);`

best regards