# Missing header. <CXLActivityLogger.h>

- **Issue #:** 327
- **State:** closed
- **Created:** 2018-02-04T13:48:38Z
- **Updated:** 2018-04-16T01:43:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/327

After a clean install of Ubuntu and the ROCm stack, I moved towards install hipCaffe. 
I got an error because /opt/rocm/include/hip/hip_profile.h calls for CXLActivityLogger.h. 

I'm posting this here rather than in the Caffe issues or user group because hip_profile.h is part of the ROCm install. 
Did I miss something? I found the missing header in https://github.com/GPUOpen-Tools/common-src-AMDTActivityLogger Is that supposed to be part of the ROCm install as well, or is it a separate post-install step? 