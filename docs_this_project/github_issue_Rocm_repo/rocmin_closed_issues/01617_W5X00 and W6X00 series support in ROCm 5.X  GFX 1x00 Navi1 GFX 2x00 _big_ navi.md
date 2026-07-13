# W5X00 and W6X00 series support in ROCm 5.X  GFX 1x00 Navi1 GFX 2x00 "big" navi

- **Issue #:** 1617
- **State:** closed
- **Created:** 2021-11-15T15:00:41Z
- **Updated:** 2023-01-09T02:55:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1617

Without asking for a specific date, we've now seen 5.0 announced during the latest keynote, and we've also had our expectations set for  Navi 1 and Navi 2 support in the "early" 5.x series. What timeframe can we reasonably expect each of RDNA1 and RDNA2 to be enabled in the ROCm stack?

see #1595 , #1592 #1547 #1544 #1539 etc. 

I realize that writing a compute stack for a nascent language is no small feat, all the while trying to meet the deadlines for MI_2X0 support, and while getting the Frontier software stack ready. 

All the same, I don't really care about that, since I can't perform any initial development on my workstation before deploying to clusters that need HIP/ROCm. 

We're over 2 years in for RDNA1 and this week marks 2 years since the W5700 first started shipping (and consequently landed on my desk). 

This isn't news to anyone, but a typical workflow is to develop on the workstation, train/compute in the cloud, then inference at the edge. 

We currently have no good way of doing  the first step outside of: 

A) Using aging hardware that becomes less and less relevant every quarter.
B) Putting an MI100 Server class card in a workstation chassis, 3d printing/manufacturing some sort of high airflow low noise bracket to force enough air through the card to keep it operating correctly. 

That or we use hip as an intermediary to cuda, at which point we may as well just be using DPCT/dpcpp from oneAPI and target anything from AVX to SYCL to FPGA etc. 