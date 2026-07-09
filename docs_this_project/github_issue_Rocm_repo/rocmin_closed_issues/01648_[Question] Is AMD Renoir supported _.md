# [Question] Is AMD Renoir supported ?

- **Issue #:** 1648
- **State:** closed
- **Created:** 2021-12-26T13:32:34Z
- **Updated:** 2021-12-28T05:27:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/1648

Dear all,

After reading the documentation I'm a little unsure whether my APU will be supported by ROCm, once it becomes available for my distribution of choice (Debian):

https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support

My system sports an AMD Ryzen 7 4800H CPU (Zen 2 / Renoir) with Radeon Graphics. So far I've been unable to run any OpenCL jobs on it because the libclc-amdgcn package lacks support for this model:

https://packages.debian.org/bullseye/libclc-amdgcn

Could you please shed some light on this issue ?

Best regards,

Samuel