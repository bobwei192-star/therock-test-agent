# Poor performance of LuxMark 3.1 HOTEL scene in ROCm 3.8

- **Issue #:** 1253
- **State:** closed
- **Created:** 2020-10-05T18:31:07Z
- **Updated:** 2021-01-05T04:12:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1253

ROCm 3.8 on Linux 5.7.6, with upstream amdgpu driver.

LuxMark 3.1 can be downloaded here: https://github.com/LuxCoreRender/LuxMark/releases/download/luxmark_v3.1/luxmark-linux64-v3.1.tar.bz2

I am running a AMD Radeon R9 Fury X (FIJI, gfx803).

To successfully render the bundled HOTEL scene, you might need to disable `-cl-fast-relaxed-math` in luxmark Options menu, otherwise LLVM might crash or the resulting image will be misrednered.

On my Fury X, this scene renders at about 10.38Mrays/s in about 121 seconds, resulting in a score of 1970.

http://luxmark.info/node/8425 - score: 1970  (stock 1050MHz)

rocm-smi shows me temp < 60°C at all time, and 100% GPU load, and SCLK of 1050MHz at all times.

Reruning few times, I got 1970, 1990, 1989.

Enabling `-cl-fast-relaxed-math` increases tracing to 11.43Mrays/s, but the resulting image is incorrect, and GPU does crashes often (GPU fault detected: 147, trying to read from addr 0x0), resulting in program termination. But the increase would be only of about 10%. So by extrapolating about 2190.

Compared this to the same GPU with same clock speeds from Windows users, this is about half the expected performance:

http://luxmark.info/node/1921 - score: 3054
http://luxmark.info/node/147 - score: 3742
http://luxmark.info/node/1449 - score: 3614
http://luxmark.info/node/2507 - score: 3577
http://luxmark.info/node/1086  - score: 4183  (OC 1197MHz)

I also noticed that Windows reports Local memory: 32kiB, but the Linux with ROCm 3.8 says Local memory: 64kiB

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5329384/clinfo.txt)
[clinfo-rocm.txt](https://github.com/RadeonOpenCompute/ROCm/files/5329385/clinfo-rocm.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/5329386/rocminfo.txt)
