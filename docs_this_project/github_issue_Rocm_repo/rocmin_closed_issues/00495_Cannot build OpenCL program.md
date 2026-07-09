# Cannot build OpenCL program

- **Issue #:** 495
- **State:** closed
- **Created:** 2018-08-10T03:47:30Z
- **Updated:** 2018-08-11T13:32:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/495

I'm using Ubuntu 16.04 and the latest ROCm drivers, with Claymore 11.8 running two Vega64 cards
I've recently installed ROCm, but afterwards cannot run Claymore.  Does anybody know what did i do wrong on the driver install?  I followed the guide here https://rocm.github.io/ROCmInstall.html and I'm using the 4.13 kernel as suggested.

The error message is as below:

```
AMD Cards available: 2
GPU #0: gfx900 (Device 687f), 8176 MB available, 64 compute units (pci bus 5:0:0                               )
GPU #0 recognized as Vega
GPU #1: gfx900 (Device 687f), 8176 MB available, 64 compute units (pci bus 10:0:                               0)
GPU #1 recognized as Vega
POOL/SOLO version
AMD ADL library not found.
Cannot build OpenCL program for GPU 0
Cannot build OpenCL program for GPU 1
GPU #0: algorithm ASM 1
GPU #1: algorithm ASM 1
No NVIDIA CUDA GPUs detected.
Total cards: 2

You can use "+" and "-" keys to achieve best ETH speed, see "FINE TUNING" sectio                               n in Readme for details.

ETH: Stratum - connecting to 'eth-us-west1.nanopool.org' <45.63.61.87> port 9999                                (unsecure)
ETH: Stratum - Connected (eth-us-west1.nanopool.org:9999) (unsecure)
ETHEREUM-ONLY MINING MODE ENABLED (-mode 1)
ETH: eth-proxy stratum mode
Watchdog enabled
Remote management (READ-ONLY MODE) is enabled on port 3333

You did not specify -dcri values directly, so they will be detected automaticall                               y
Automatic detection of best -dcri values started, please wait...

ETH: Authorized
Setting DAG epoch #204...
Setting DAG epoch #204 for GPU1
Create GPU buffer for GPU1
Setting DAG epoch #204 for GPU0
Create GPU buffer for GPU0
GPU0, OpenCL error -48 (0) - cannot create DAG on GPU
GPU1, OpenCL error -48 (0) - cannot create DAG on GPU
Quit signal received...
Quit, please wait...
GPU 0 failed
GPU 1 failed


```