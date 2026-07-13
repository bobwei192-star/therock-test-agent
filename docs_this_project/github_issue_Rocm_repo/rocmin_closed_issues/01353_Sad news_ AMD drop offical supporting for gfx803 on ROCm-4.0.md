# Sad news, AMD drop offical supporting for gfx803 on ROCm-4.0

- **Issue #:** 1353
- **State:** closed
- **Created:** 2020-12-30T10:05:45Z
- **Updated:** 2021-03-08T21:09:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/1353

I noticed that gfx803 had been removed from ROCm-4.0 offical supporting list on 2020-12-19.
https://github.com/RadeonOpenCompute/ROCm/commit/2b7f806b106f2b19036bf8e7af4f3dad7bc6222e#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5L408

Indeed, gfx803 is an old card and ROCm should put limit resources to support new hardwares. The bad part is the only GPU what I have is RX580 which is gfx803. The price of GPU is higher, which I didn't expect. I think I should try to find a way to let my gfx803 work longer by myself.

Feel free to close my gfx803 related issues and pull requests.

* https://github.com/RadeonOpenCompute/ROCm/issues/1265
* https://github.com/ROCmSoftwarePlatform/rocBLAS/issues/1172
* https://github.com/ROCmSoftwarePlatform/rocRAND/pull/159 