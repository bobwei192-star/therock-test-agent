# ROCm programs hangs with Vega 20 (MI 50)

- **Issue #:** 1386
- **State:** closed
- **Created:** 2021-02-19T15:00:45Z
- **Updated:** 2021-03-11T19:59:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1386

Hi,

I have recently installed ROCm v4.0.0 on a server running 2 Vega 20 GPUs (MI 50).

The clinfo command locks up like the issues #484 #1326. The difference is I have to force the restart of the server to have access to the agents after the program locks. The bug.tar.gz locks also and the output is in the output.txt file. I thought it was only with OpenCL programs but it happens also with Tensorflow scripts.

The two GPUs are not connected with XGMi. The motherboard uses the latest BIOS available. The issue happened with Ubuntu 18.04 (Linux kernel 4.15) and 20.04 (Linux kernel 5.4.0-65).

[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010742/rocminfo.txt)
[bug.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/6010743/bug.tar.gz)
[output.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010744/output.txt)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010745/clinfo.txt)
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6010746/dmesg.txt)
