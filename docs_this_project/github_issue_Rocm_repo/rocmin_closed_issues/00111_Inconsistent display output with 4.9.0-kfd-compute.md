# Inconsistent display output with 4.9.0-kfd-compute

- **Issue #:** 111
- **State:** closed
- **Created:** 2017-05-03T05:05:53Z
- **Updated:** 2017-10-17T14:03:55Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/111

Hi,

I installed the ROCm 1.5 release today and am experiencing some display issues. Sometimes, the display will come up without issue, other times it will remain black. A few times it came up with only low resolutions available, and I observed the following output while it was starting:

```
[    3.453722] Raw EDID:
[    3.453724]  	00 ff ff ff ff ff ff 00 ff ff ff ff ff ff ff ff
[    3.453726]  	56 50 9e 26 0d 50 54 21 0b 00 d1 c0 d1 fc 81 c0
[    3.453728]  	0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d
[    3.453730]  	01 01 01 01 01 01 37 8b 80 18 71 38 2d 40 58 2c
[    3.453732]  	45 00 dd 0c 11 00 00 1e 00 00 00 fc 00 4e 58 2d
[    3.453734]  	56 55 45 32 34 0a 20 20 20 20 00 00 00 fd 00 1e
[    3.453735]  	90 a2 a2 24 01 00 20 20 20 20 20 20 00 00 00 ff
[    3.453737]  	00 4e 49 58 32 34 31 35 0a 20 20 20 20 20 01 54
[    3.453740] amdgpu 0000:03:00.0: DP-1: EDID invalid.
```

There are many nearly identical messages. Swapping DP outputs or to HDMI didn't change anything.
My system configuration is Intel 5820k on an Asrock Extreme 4 x99, with an RX 480 Reference model w/ Ubuntu 16.04, and monitor is Nixeus VUE24. Please tell me if I can supply any other messages/output that can help. I'm not sure this is exactly a ROCm problem, but I don't see this happen when booting Ubuntu's stock kernel or previously ROCm 1.4's kernel. Thanks!