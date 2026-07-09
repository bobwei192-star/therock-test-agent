# pp_dpm_set_power_profile_state was not implemented

- **Issue #:** 63
- **State:** closed
- **Created:** 2016-12-31T13:59:23Z
- **Updated:** 2017-07-02T17:17:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/63

Hello,

Recently, I installed ROCm1.4 and tried to run my codes which could run on ROCm1.3.0.
I can compile my C++ code with HCC, and could run it in the first trial. At the same time I got the following message on the dmesg.
pp_dpm_set_power_profile_state was not implemented

From the second trial to run my executable, I got the segmentation error.

So, I am suspecting that the above message can be related to this segmentation error.

Does anyone know about it?

In my code, I am just using matrix calculation together with If statements in the parallel_for loop.

Best regards,
Nandinbaatar Tsog (Nabar)