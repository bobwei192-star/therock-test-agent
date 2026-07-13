# Increased invalid results rate on SETI@Home compared to Windows

- **Issue #:** 423
- **State:** closed
- **Created:** 2018-05-22T12:28:14Z
- **Updated:** 2021-01-05T10:56:54Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/423

A user on the SETI@Home forums has reported an increased a significantly higher rate of inconclusive and invalid SETI@Home workunits on their system using an RX Vega 64 when running Linux + ROCm 1.8 compared to the same hardware on Windows (to be honest, that system has 0 invalids on Windows compared to quite a few on Linux).

[Link to thread](https://setiathome.berkeley.edu/forum_thread.php?id=82949)

The host using Linux + ROCm [Link](https://setiathome.berkeley.edu/show_host_detail.php?hostid=8365846) (Oddly enough, here the GPU is identified as AMD Device 687f instead of AMD Radeon RX Vega)
The host using Windows [Link](https://setiathome.berkeley.edu/show_host_detail.php?hostid=8507353)

Don't really have much diagnostic info, but something seems to be messing with the computation compared to Windows - I think this might be worth looking at.


