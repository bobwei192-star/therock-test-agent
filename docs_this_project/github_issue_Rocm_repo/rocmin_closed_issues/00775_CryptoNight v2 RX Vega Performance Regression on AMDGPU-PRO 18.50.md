# CryptoNight v2 RX Vega Performance Regression on AMDGPU-PRO 18.50

- **Issue #:** 775
- **State:** closed
- **Created:** 2019-04-18T18:54:58Z
- **Updated:** 2019-04-19T16:33:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/775

So, our good ol’ Vega hashrate issue https://github.com/RadeonOpenCompute/ROCm/issues/325 ended up being solved by using amdgpu-pro 18.30 together with either an older OpenCL compiler version or ROCm-HCC.
As far as I understood, it was basically the firmware shipped with amdgpu-pro that made the difference.
I believe 18.20 did also work. 18.40 still does.

18.50 however sees significantly worse hashrates on cn/2 variants. Interestingly, cn/1 and cn/0 retain full performance.

The critical loop of CryptoNight does reads to random addresses in 2 MB scratchpads and writes back new values.
In cn/0 and cn/1, the reads are 128 bit wide.
In cn/2, they are 4x128 bit wide instead, covering 3 adjacent addresses via XOR. (I.e. what is read is the computed address, as well as `address^1`, `address^2`, `address^3`. There is again a write-back to each of these addresses.)

Just wanted to let you know. I’m of course free to stick with 18.40, and will do so, but perhaps this observation is an indication of a larger problem worth fixing.
Cheers!