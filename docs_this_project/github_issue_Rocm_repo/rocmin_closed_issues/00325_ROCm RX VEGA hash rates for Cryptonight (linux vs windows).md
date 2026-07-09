# ROCm RX VEGA hash rates for Cryptonight (linux vs windows)

- **Issue #:** 325
- **State:** closed
- **Created:** 2018-02-03T23:44:51Z
- **Updated:** 2021-01-05T09:52:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/325

Going to start a new issue in hopes to find a solution to the performance of cryptonight mining on linux under ROCm, as we continue to lag behind the windows aug 23rd blockchain drivers by 35%.

### 

GPUs - RX Vega 64

Running Aug 23 blockchain drivers on windows, I see 1900h cryptonight, and 39Mh ethash.
Running ROCm 1.7 on ubuntu, I see 1250h cryptonight, and 39Mh ethash.

So the fact that I can get like rates on ethash means the opencl stack is just as good as windows.

I gave windows 64GB of virtual memory and ubuntu 64GB of swap. Tested amdkfd.noretry 1 and 0.

Any other recommendations on things to try?
