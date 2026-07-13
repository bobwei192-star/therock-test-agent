# GPU Hang on Radeon Pro W7900

- **Issue #:** 6137
- **State:** closed
- **Created:** 2026-04-09T09:06:02Z
- **Updated:** 2026-04-16T08:41:25Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6137

I am using the AMR Radeon Pro W7900 GPU for flow simulations with the software AMR-Wind.

AMR-Wind: https://github.com/Exawind/amr-wind

Randomly during my simulations i get this error:

HW Exception by GPU node-1 (Agent handle: 0x1b0fc990) reason :GPU Hang
[windteammitarbeiter:08475] *** Process received signal ***
[windteammitarbeiter:08475] Signal: Aborted (6)
[windteammitarbeiter:08475] Signal code: (-6)
[windteammitarbeiter:08475] [ 0] /lib/x86_64-linux-gnu/libc.so.6(+0x45330)[0x750502245330]
[windteammitarbeiter:08475] [ 1] /lib/x86_64-linux-gnu/libc.so.6(pthread_kill+0x11c)[0x75050229eb2c]
[windteammitarbeiter:08475] [ 2] /lib/x86_64-linux-gnu/libc.so.6(gsignal+0x1e)[0x75050224527e]
[windteammitarbeiter:08475] [ 3] /lib/x86_64-linux-gnu/libc.so.6(abort+0xdf)[0x7505022288ff]
[windteammitarbeiter:08475] [ 4] /opt/rocm-6.4.3/lib/libhsa-runtime64.so.1(+0x2cce7)[0x75050142cce7]
[windteammitarbeiter:08475] [ 5] /opt/rocm-6.4.3/lib/libhsa-runtime64.so.1(+0xa22ac)[0x7505014a22ac]
[windteammitarbeiter:08475] [ 6] /opt/rocm-6.4.3/lib/libhsa-runtime64.so.1(+0x39251)[0x750501439251]
[windteammitarbeiter:08475] [ 7] /lib/x86_64-linux-gnu/libc.so.6(+0x9caa4)[0x75050229caa4]
[windteammitarbeiter:08475] [ 8] /lib/x86_64-linux-gnu/libc.so.6(+0x129c6c)[0x750502329c6c]
[windteammitarbeiter:08475] *** End of error message ***

I also opened an issue in the AMR-Wind Github repository:
https://github.com/Exawind/amr-wind/issues/1884

The developers there pointed out that this might not be an AMR-Wind issue, but something else. Maybe someone here is able to help me, i am unsure if this is even the right place for this issue.

Some other information:
OS: Ubuntu 24.04 LTS
ROCm: 6.4.3

I am happy to provide any other information that might be needed.