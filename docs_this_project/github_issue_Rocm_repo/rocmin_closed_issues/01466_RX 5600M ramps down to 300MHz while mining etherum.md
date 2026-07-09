# RX 5600M ramps down to 300MHz while mining etherum

- **Issue #:** 1466
- **State:** closed
- **Created:** 2021-05-04T10:22:58Z
- **Updated:** 2021-05-05T10:09:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/1466

## Brief summary of the problem:
  When I try to mine ethereum using the RX5600M on my Dell G5 15 SE the GPU clock ramps down to its lowest P-state (300MHz)

## Hardware description:
 - CPU: Ryzen 5 4600H
 - GPU: RX 5600M
 - System Memory: 8+16GB
 - Display(s): Laptop screen
 - Type of Diplay Connection: eDP

## System information:
 - Distro name and Version: openSUSE Tumbleweed 20210429
 - Kernel version: 5.12.0-1-defalut
 - Custom kernel: From openSUSE main repositories
 - AMD package version: Mesa 21.0.1 Rocm 4.1.0

## How to reproduce the issue:
 run `teamredminer -a ethash --url=stratum+tcp://asia1.ethermine.org:4444 -u <YOUR-ETH-WALLET-ID>- p x -d 0  --eth_config=A432`
It successfully initializes the GPU but ramps the clock speeds down to 300MHz. I don't know if other Rocm/OpenCL workloads have the same behaviour. Games dont exhibit this behaviour and run at proper clock speeds

I've also reported the bug on drm/amd https://gitlab.freedesktop.org/drm/amd/-/issues/1587