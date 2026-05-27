# Poor performance of LuxMark 3.1 HOTEL scene in ROCm 3.8

> **Issue #1253**
> **状态**: closed
> **创建时间**: 2020-10-05T18:31:07Z
> **更新时间**: 2021-01-05T04:12:33Z
> **关闭时间**: 2021-01-04T08:31:46Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1253

## 描述

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


---

## 评论 (33 条)

### 评论 #1 — baryluk (2020-11-23T17:53:11Z)

Even worse now with ROCm 3.9.

The Mrays/s figures in the status bar are even lower than in ROCm 3.8.

Without `-cl-fast-relaxed-math` , the test completes with correct image, and score: 1700, which is way lower than previous 1970 with same settings.

With `-cl-fast-relaxed-math` (default in LuxMark v3.1) the tests completes without GPU, LLVM or application crash, but it is incorrectly rendered. Score: 1903. So, less than previous expected 2910.


---

### 评论 #2 — ROCmSupport (2020-12-03T12:21:58Z)

Hi @baryluk 
Can you please try with 3.10.
Thank you.

---

### 评论 #3 — baryluk (2020-12-03T22:21:37Z)

~~Tested now with ROCm 3.10 and Linux 5.9.9-1 with upstream amdgpu.~~

~~I see now "Local Memory: 32 Kbytes". So that is a change. Now it is consistent with Windows. I am not sure if it is correct or not, but at least it is consistent.~~

~~As of results in LuxMark v3.1. Well it is worse.~~

~~MRays/s is way higher (unbelievably so), but the end result is wrong, and even worse, and in both modes. (Previously it was at least correct with `-cl-fast-relaxed-math` not enabled).~~

~~With `-cl-fast-relaxed-math` enabled (default for LuxMark v3.1), I am getting 32.3–32.5MRays/s. End score is 30925-31512  (but 499105 pixels (84.62% of all) is wrong).~~

~~With `-cl-fast-relaxed-math` disabled, I am getting 31.9–32.1Mrays/s. End score is 31377–31512 (but 499105 pixels (73.42% of all) is wrong).~~

~~So, actually I would say this is a regression compared to ROCm 3.9.0.~~

~~Even if these MRays/s values are correctly, which are about 3 times what I have seen before, for some reasons the LuxMark end "score" is about 15 times the previous score, not 3 as expected. My guess, it is a bug in LuxMark scoring method. However, it is also possibly that my GPU was not running at 1050MHz all the time in my previous tests. In this runs now, it was at 1050MHz all the time (verified by hwmon entries in sysfs and using `rocm-smi`).~~

~~Also, I am not sure why LuxMark says 499105 pixels are different in both runs (with and without `-cl-fast-relaxed-math`), but reports different percentage, despite the size of the image, and total number of pixels being the same.~~

OOps.

This was with Mesa 20.2.3 Clover / OpenCL 1.1

I will post actual ROCm 3.10 test results soon.

---

### 评论 #4 — baryluk (2020-12-03T23:16:50Z)

@ROCmSupport Slight (2.5%) improvement, but not substantial.

ROCm 3.10 , Linux 5.9.9-1, Platform Version: OpenCL 2.0 AMD-APP (3212.0).

Same system (AMD Radeon R9 Fury X, FIJI, GFX8, gfx803). 64 CU, 1050MHz nominal. Water cooled.

Local Memory: 64KBytes reported by OpenCL for this device in `clinfo` and `LuxMark v3.1`. While this is different than Windows or what Mesa Clover reports, I think it might be actually correct, after referencing some AMD documents. FIJI CU appears to have 64KB of LDS memory. Plus 16KB of L1 cache for scalar data, and 32KB of L1 cache for vector data, shared across 4 CUs. That is my guess, and it kind of matches what `rocminfo` is showing too.

HOTEL scene as before.

With `-cl-fast-relaxed-math` (default) , ≈11.3MRays/s, end score: 2159–2171. (519669 different pixels, 88.11% bad pixels. On a different run 519505 different pixels, 88.08% bad pixels)

Without `-cl-fast-relaxed-math`, ≈10.6MRays/s, end score: 2021–2027. (154251 different pixels, 26.15% bad pixels. On a different run 154118 difference pixels, 26.13% bad pixels)

I would say the results slightly (about 2.5%) better than before, but not that much. It is basically the same as before (in ROCm 3.8), and still substantially lower compared to Windows.

GPU core and memory clock frequencies are stable during the run (as confirmed by hwmon files in sysfs and `rocm-smi`).

My results for 3.9 might have been incorrect, due to unstable clocks, because of this kernel / GPU BIOS bug https://gitlab.freedesktop.org/drm/amd/-/issues/936 . I didn't monitor the GPU clocks fully at the time before, so I can't confirm if it was the case.


---

### 评论 #5 — ROCmSupport (2020-12-04T09:56:49Z)

Thanks @baryluk for the update.
As per current resources we have, we are not in a position to validate gfx8 in a full scale like gfx9.
We have limited test coverage on gfx8.
Hence the delay in responding issues specific to gfx8.
Please stay tuned for the more updates.


---

### 评论 #6 — ableeker (2020-12-05T13:45:08Z)

I can confirm this issue with Luxmark 3.1 on a gfx9, a gfx900 RX Vega 64.

With cl-fast-relaxed-math enabled, I get 15 MRays/sec, and a score of 2882. However, image validation fails with 88.51% incorrectly rendered pixels. The rendered image is visually clearly incorrect as well, very pale, and noisy.

With cl-fast-relaxed-math disabled, I get 14 MRays/sec, and a score of 2695. This time, image validation is successful with 21.44% pixels rendered incorrectly. The visual result is correct as well.

The other 2 scenes, luxball and neumann, render incorrectly as well with cl-fast-relaxed-math enabled, and correctly with this option disabled.

---

### 评论 #7 — baryluk (2020-12-06T04:48:36Z)

> I can confirm this issue with Luxmark 3.1 on a gfx9, a gfx900 RX Vega 64.
> 
> With cl-fast-relaxed-math enabled, I get 15 MRays/sec, and a score of 2882. However, image validation fails with 88.51% incorrectly rendered pixels. The rendered image is visually clearly incorrect as well, very pale, and noisy.
> 
> With cl-fast-relaxed-math disabled, I get 14 MRays/sec, and a score of 2695. This time, image validation is successful with 21.44% pixels rendered incorrectly. The visual result is correct as well.
> 
> The other 2 scenes, luxball and neumann, render incorrectly as well with cl-fast-relaxed-math enabled, and correctly with this option disabled.

HI @ableeker . This bug is specifically about the performance. Can you tell if the results you are gettings are significantly lower than Windows?

For the correctness issues you check the other bug - https://github.com/RadeonOpenCompute/ROCm/issues/1145  

---

### 评论 #8 — ableeker (2020-12-06T14:31:20Z)

I see, I didn't make that clear, Windows is much faster. With cl-fast-relaxed-math disabled I'm getting about 35 M/Rays/sec, and a score of 6500.

Interestingly, amdgpu 20.45, which is now using ROCr, shows the same behaviour, cl-fast-relaxed-math needs to be disabled to render correctly, but is as fast as 20.40, which didn't use ROC and rendered correctly, and Windows.

---

### 评论 #9 — perestoronin (2020-12-06T20:47:17Z)

> ROCm 3.10 , Linux 5.9.9-1, Platform Version: OpenCL 2.0 AMD-APP (3212.0).

please retry with Linux 5.4.81, I have same troubles in degradate performance minus 30% with all Linux 5.7+, but Linux 5.4* work perfectly !

---

### 评论 #10 — baryluk (2020-12-07T08:23:39Z)

@perestoronin What numbers you are getting on LuxMark 3.1 HOTEL scene? Which GPU.

---

### 评论 #11 — baryluk (2020-12-07T08:24:08Z)

> I see, I didn't make that clear, Windows is much faster. With cl-fast-relaxed-math disabled I'm getting about 35 M/Rays/sec, and a score of 6500.
> 
> Interestingly, amdgpu 20.45, which is now using ROCr, shows the same behaviour, cl-fast-relaxed-math needs to be disabled to render correctly, but is as fast as 20.40, which didn't use ROC and rendered correctly, and Windows.

Thank you. That is super helpful to know!

---

### 评论 #12 — ableeker (2020-12-09T18:34:23Z)

My bad, amdgpu-pro 20.45, that's using ROCr now, is as slow as ROCm 3.10, I get 15 MRays/sec, and a score of 2800.

With amdgpu-pro 20.40, that's NOT using ROCr, I get 30 MRays/sec, and a score of 5700. And I don't have to disable cl-fast-relaxed-math.

That's with a gfx900, a Vega 64.

---

### 评论 #13 — baryluk (2020-12-10T16:11:28Z)

> My bad, amdgpu-pro 20.45, that's using ROCr now, is as slow as ROCm 3.10, I get 15 MRays/sec, and a score of 2800.
> 
> With amdgpu-pro 20.40, that's NOT using ROCr, I get 30 MRays/sec, and a score of 5700. And I don't have to disable cl-fast-relaxed-math.
> 
> That's with a gfx900, a Vega 64.

That is interesting. Unfortunately I can't install amdgpu-pro 20.40 on my system. amdgpu module fails to compile with kernel 5.9.9 and 5.9.11 that I have on my Debian testing machine.

I will try the non-pro version later, once I clean up the mess.

---

### 评论 #14 — baryluk (2020-12-10T18:53:07Z)

Ok. I managed to test the opencl driver from amdgpu-pro 20.40, but forcing it to install and ignore some dependencies, and configuring paths. It actually worked with upstream amdgpu kernel driver from Linux 5.9.9.

Indeed, performance is better with amdgpu-pro 20.40!

I also tested 20.45 and performance is almost the same as 20.40, if not faster actually.

AMD Radeon R9 Fury X (FIJI, GFX8, gfx803).

HOTEL scene:

| Driver           | AMD-APP | Kernel | Local Memory |                 Options |     MRays/s | Score | Bad pixels          |
|------------------|---------|-------:|-------------:|-------------------------|------------:|------:|--------------------:|
| ROCm 2.7         |  2949.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` | 9.71-9.72 |  1864 |     160559 / 27.22% |
| ROCm 2.7         |  2949.0 | 5.9.9  |        64KiB |                         | 9.84-9.85 |  1872 |     160531 / 27.22% |
| ROCm 2.7         |  2949.0 | 5.9.9  |        64KiB |   `-cl-strict-aliasing` | 9.85-9.86 |  1876 |     160426 / 27.20% |
| ROCm 3.0         |  3052.0 | 5.9.9  |          n/a |                     n/a |        n/a  |   n/a |     **No GPU**          |
| ROCm 3.1         |  3084.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` |        9.87 |  1874 |     162309 / 27.52% |
| ROCm 3.1         |  3084.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` |        9.88 |  1891 |     160559 / 27.22% |
| ROCm 3.1         |  3084.0 | 5.9.9  |        64KiB |                         |   9.47-9.48 |  1817 |     166098 / 28.16% |
| ROCm 3.1         |  3084.0 | 5.9.9  |        64KiB |                         |        9.48 |  1823 |     164167 / 27.83% |
| ROCm 3.3         |  3098.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` |        9.69 |  1866 |     162238 / 27.51% |
| ROCm 3.3         |  3098.0 | 5.9.9  |        64KiB |                         |       10.11 |  1939 |     158938 / 26.95% |
| ROCm 3.5         |  3137.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` | 11.43-11.46 |  2170 | **!!! 519695 / 88.11%** |
| ROCm 3.5         |  3137.0 | 5.9.9  |        64KiB |                         | 10.38-10.42 |  1983 |     157322 / 26.67% |
| ROCm 3.7         |  3182.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` | 11.43-11.46 |  2170 | **!!! 519701 / 88.11%** |
| ROCm 3.7         |  3182.0 | 5.9.9  |        64KiB |                         | 10.38-10.42 |  1986 |     157503 / 26.70% |
| ROCm 3.8         |  3186.0 | 5.7.6  |        64KiB | `-cl-fast-relaxed-math` |      ≈11.43 | ≈2190 |     **crash**           |
| ROCm 3.8         |  3186.0 | 5.7.6  |        64KiB |                         |      ≈10.38 |  1970 |     pass            |
| ROCm 3.8         |  3186.0 | 5.7.6  |        64KiB |                         |      ≈10.38 |  1990 |     pass            |
| ROCm 3.8         |         | 5.7.6  |        64KiB |                         |      ≈10.38 |  1989 |     pass            |
| ROCm 3.8         |  3186.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` | 11.43-11.47 |  2172 | **!!! 519610 / 88.10%** |
| ROCm 3.8         |  3186.0 | 5.9.9  |        64KiB |                         | 10.38-10.41 |  1988 |     153966 / 26.10% |
| ROCm 3.8         |  3186.0 | 5.9.9  |        64KiB |   `-cl-strict-aliasing` | 10.38-10.41 |  1989 |     153077 / 26.12% |
| ROCm 3.9         |         | 5.7.6  |        64KiB | `-cl-fast-relaxed-math` |             |  1903 |     pass            |
| ROCm 3.9         |         | 5.7.6  |        64KiB |                         |             |  1700 |     pass            |
| ROCm 3.9         |  3204.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` | 11.28-11.30 |  2154 | **!!! 519713 / 88.11%** |
| ROCm 3.9         |  3204.0 | 5.9.9  |        64KiB |                         | 10.58-10.61 |  2030 |     154061 / 26.12% |
| ROCm 3.9         |  3204.0 | 5.9.9  |        64KiB |   `-cl-strict-aliasing` | 10.58-10.61 |  2026 |     153974 / 26.11% |
| ROCm 3.10        |  3212.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` |       ≈11.3 |  2171 | **!!! 519669 / 88.11%** |
| ROCm 3.10        |  3212.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` |       ≈11.3 |  2159 | **!!! 519505 / 88.08%** |
| ROCm 3.10        |  3212.0 | 5.9.9  |        64KiB | `-cl-fast-relaxed-math` |       ≈11.28 |  2156 | **!!! 519681 / 88.11%** |
| ROCm 3.10        |  3212.0 | 5.9.9  |        64KiB |                         |       ≈10.6 |  2027 |     154251 / 25.13% |
| ROCm 3.10        |  3212.0 | 5.9.9  |        64KiB |                         |       ≈10.6 |  2021 |     154118 / 26.13% |
| ROCm 3.10        |  3212.0 | 5.9.9  |        64KiB |                         |       ≈10.59 |  2027 |     154000 / 26.11% |
| ROCm 4.0        |  3212.0 | 5.9.11  |        64KiB | `-cl-fast-relaxed-math` |       ≈11.32 |  2154 | **!!! 519572 / 88.11%** |
| ROCm 4.0        |  3212.0 | 5.9.11  |        64KiB |                         |       ≈10.64 |  2024 |     154150 / 26.13% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB | `-cl-fast-relaxed-math` |      ≈19.26 |  3663 |     112859 / 19.31% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB | `-cl-fast-relaxed-math` | 19.20-19.28 |  3672 |     1111794 / 18.95% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB | `-cl-fast-relaxed-math` | 19.29–19.31 |  3664 |     112973 / 19.15% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB | `-cl-fast-relaxed-math` `-cl-strict-aliasing` | 19.18-19.28 |  3656 |     114521 / 19.42% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB |                         |      ≈19.91 |  **3798** |     110243 / 18.69% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB |                         | 19.83-19.95 |  3794 |     110060 / 18.66% |
| amdgpu-pro 20.40 |  3180.7 | 5.9.9  |        32KiB |   `-cl-strict-aliasing` | 19.85-30.05 |  3799 |     110128 / 18.67% |
| amdgpu-pro 20.45 |  3188.4 | 5.9.9  |        32KiB | `-cl-fast-relaxed-math` | **19.29–19.31** |  **3682** |     111620 / 18.92% |
| amdgpu-pro 20.45 |  3188.4 | 5.9.9  |        32KiB |                         | **20.09–20.11** |  3869 |     108931 / 18.47% |
| amdgpu-pro 20.45 |  3188.4 | 5.9.9  |        32KiB |   `-cl-strict-aliasing` | **20.07-20.10** |  **3873** |     108832 / 18.45% |



Yes, the result WITHOUT `-cl-fast-relaxed-math` is actually faster when using `amdgpu-pro`! Strange.

And yes, all results 3663 - 3798, are higher than any reported Windows results from the luxmark website (3742). Wonderful.

Now question is, why the ROCm shows so worse performance. And why amdgpu-pro 20.45 for some also shows worse performance.

It looks it might be due to the Local memory reporting. The amdgpu-pro 20.40 reports 32KBytes, just like Windows. The ROCm reports 64KBytes, which feels wrong. But it could be also something else, like actual generated code.

PS. Note to myself and others. It is good idea to to clean / remove these directories after install of different version: `~/.AMD/GLCache /tmp/kernel_cache/LUXCORE_1.5 ~/.cache/AMD ~/.cache/mesa_shader_cache ~/.cache/radv_builtin_shaders64 /tmp/DiskCache/`

---

### 评论 #15 — ableeker (2020-12-11T00:11:25Z)

I only need OpenCL, so I can install only the OpenCL part from amdgpu 20.40 without kernel module like so:

`amdgpu-install --headless --no-dkms --opencl=pal`

That `--no-dkms` will make sure dkms isn't used.

You should be able to install 20.45 in a similar way, like so:

`amdgpu-install --headless --no-dkms --opencl=rocr`

But it isn't not working with 20.45, that is, it's ignoring `--no-dkms`, and will still try to compile a kernel module, and will fail after a bit. In my cast that's because I'm running Ubuntu 20.10 with kernel 5.8. However, if I then just remove amdgpu-dkms, OpenCL will still work.

---

### 评论 #16 — ableeker (2020-12-11T00:14:34Z)

I believe amdgpu 20.45 is doing much worse than 20.40, because 20.45 is now using ROC as well, while 20.40 didn't.

ROCr, the runtime of ROC, is actually a new feature of 20.45.

---

### 评论 #17 — baryluk (2020-12-11T12:11:57Z)

> I believe amdgpu 20.45 is doing much worse than 20.40, because 20.45 is now using ROC as well, while 20.40 didn't.
> 
> ROCr, the runtime of ROC, is actually a new feature of 20.45.

Fair, but as I said, the amdgpu-pro 20.45 is not slower for me on AMD Radeon RX Fury X (FIJI, gfx803). It looks GPU dependent.


---

### 评论 #18 — amartincolby (2020-12-12T21:47:40Z)

I'm working through similar issues as those mentioned here right now. I have a Vega Frontier Edition Air. I'm running Ubuntu 20.04 with the 5.4.0-58-generic kernel because I had previously been trying to get the proprietary drivers to work. Performance of the Luxball and Neumann are as expected: ~26k for Luxball, ~17.5k for Neumann. The Hotel Lobby, though, is half of what it should be at ~2.3k. The problems with the `dkms` flag being ignored has been noted on other boards as well, @ableeker. I am completely unable to get the proprietary drivers working, so ROCm is my only hope at the moment.

---

### 评论 #19 — amartincolby (2020-12-14T02:58:51Z)

@baryluk When you say non-pro, do you mean the Vega consumer driver package, like Vega 64 instead of Vega Frontier?

---

### 评论 #20 — amartincolby (2020-12-15T03:50:10Z)

@baryluk So there is no difference? The driver package that I downloaded has the base script, `amdgpu-install`, but it specifically states that unless I select headless installation, it will install pro support, and as such it fails every time. But even if I select headless, it tries to install `amdgpu-pro-pin`, which fails the OS check.

---

### 评论 #21 — amartincolby (2020-12-17T02:52:48Z)

Honestly, I would be fine with the performance regression for now if Blender worked, which is what I am ultimately interested in. Sadly, Blender is also completely broken, as can be seen in connected issues #1210, #1106, and even older yet still open like #772. I understand that priorities are hard to manage, especially when dealing with software of such complexity, but AMD has long pushed the OpenCL performance of their cards as a selling point, and people who use a lot of OpenCL are much more likely to be using Linux. For gaming drivers, alright. Probably 1% of gamers use Linux, whereas 97% use Windows. I can appreciate focusing on Windows. But workstation demographics are probably 25% Linux or more. That's a huge hunk of users.

Thank you for the offer of the package, but I guess I will wait until they release the pro version of their drivers for Ubuntu 20. Hopefully I'll be able to go completely open source on my driver stack next year.

---

### 评论 #22 — baryluk (2020-12-26T03:02:05Z)

@amartincolby This bug is about LuxMark 3.1 HOTEL scene in ROCm. For other issue, please open separate issue. Would be good to remove off-topic comments. Thanks in advance.



---

### 评论 #23 — amartincolby (2020-12-26T03:05:06Z)

@baryluk I wasn't intending that to be a report about Blender performance, only to reference OpenCL rendering in general. That was me attempting to express understanding with the difficulties of software development while also indicating my disappointment with OpenCL performance and stability.

---

### 评论 #24 — baryluk (2020-12-26T03:06:58Z)

> @baryluk I wasn't intending that to be a report about Blender performance, only to reference OpenCL rendering in general. That was me attempting to express understanding with the difficulties of software development while also indicating my disappointment with OpenCL performance and stability.

That is pointless and derails the discussion. Let's try to make the job of ROCm devs as easy as possible instead.

---

### 评论 #25 — amartincolby (2020-12-26T03:47:28Z)

@baryluk I disagree that it is pointless. I am a consumer of this product. I am offering my reports on it.

---

### 评论 #26 — ROCmSupport (2021-01-04T08:31:46Z)

AMD ROCm dropped supporting gfx8 officially from ROCm 4.0 as per https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support.
Hence closing this issue.
Thank you.

---

### 评论 #27 — baryluk (2021-01-04T11:19:08Z)

@ROCmSupport How long is GFX9 going to be supported? Where is the support roadmap / policy?

---

### 评论 #28 — xuhuisheng (2021-01-04T11:51:41Z)

@baryluk 
Maybe the lifecyle of gfx9 is longer. CDNA - aka MI100, gfx908 is GFX9 family series. GCN with 64 wavefront is more suitable for computation. But ROCm team is leak of testing resources.

Not long times before, people said AMD wont support gaming card like navi10, because ROCm will only support computing card like MI100. But AMD shows good news about there is a supporting plan on 2021 for navi. Now, I am total cannot understand the future plan of ROCm. 

---

### 评论 #29 — xuhuisheng (2021-01-04T12:00:48Z)

@baryluk 
BTW, I am curious one thing, did you met the gfx803 problems on gfx803 after ROCm-3.7, I noticed you are using fury X - fiji which have 64 cu.
My card RX580 Polaris10 only have 36 cu. I want to find out if the difference of cu number caused the problem of gfx803 issues.
If you have time, could you try this samples on tensorflow? thank you.

```
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

X = tf.fill((300, 5), 5)
Y = tf.fill((300, 5), 10)

model = tf.keras.Sequential()
model.add(Dense(5))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

epochs = 150
batch_size = 32

print("Fitt...")
#with tf.device('/CPU:0'):#To test on GPU
model.fit(X, Y, batch_size=batch_size, epochs=epochs)

print("Evaluate...")
model.evaluate(X, Y)

print("Predict...")
result = model.predict(tf.fill((1, 5), 5))
print(result)

```

---

### 评论 #30 — ROCmSupport (2021-01-04T12:06:52Z)

Hi @baryluk 
I can not talk about gfx9 long term plans at this moment.
Thank you.

---

### 评论 #31 — baryluk (2021-01-04T16:14:14Z)

> Hi @baryluk
> I can not talk about gfx9 long term plans at this moment.
> Thank you.

Is there any AMD manufactured GPU that I can buy, and have it supported by ROCm for next 5 years?


---

### 评论 #32 — amartincolby (2021-01-05T01:50:21Z)

This is disappointing. AMD is still selling professional-grade gfx8 cards on their website.

---

### 评论 #33 — xuhuisheng (2021-01-05T04:10:08Z)

The price of MI100 is $7,377.27. I dont think it suitable for individual customer. Maybe it is just a joke.
http://www.shopblt.com/cgi-bin/shop/shop.cgi?action=thispage&thispage=011004001501_B8ND723P.shtml


---
