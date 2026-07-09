# opencl .so file missing from post 3.5 installs

- **Issue #:** 1240
- **State:** closed
- **Created:** 2020-09-23T21:42:05Z
- **Updated:** 2020-09-24T01:29:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/1240

I am running Ubuntu 18.04.5 with 5.4 kernel. I have had ROCm installed since version 2.
Whenever I upgrade ROCm since 3.5, the opencl .so files remain in my 3.5 folder.
 
So, even with 3.8, I have to keep 3.5 install folder around to be able to use OpenCL.

Is this correct? For a fresh 3.8 install, which library is used for enabling OpenCL ?