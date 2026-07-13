# gfx1010(RX5000 series) dosen't support fp16 on linux

- **Issue #:** 1857
- **State:** closed
- **Created:** 2022-11-12T17:36:14Z
- **Updated:** 2024-11-14T18:08:41Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/1857

currently using gfx1010.
In the latest version of ROCm, 5.3.2, gfx1010 cannot use fp16 calculations.
An attempt was made to calculate fp16 in the pytorch environment, but it did not work.
Is there a way to force the fp16 calculation in the gfx1010 series?