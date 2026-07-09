# rocminfo shows 16 GT/s on two GPUs and 8 GT/s on two (lspci shows all 4 at 16GT/s)

- **Issue #:** 2020
- **State:** closed
- **Created:** 2023-04-05T19:06:07Z
- **Updated:** 2024-06-19T20:23:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/2020

I am seeing something weird. I have 4 Radeon PRO W6800 cards and when I install two of them, I get 16 GT/s (see 2gpu-lspci.txt and 2gpu-rocmsmi.txt) but when I install all 4 of them then lspci gives me the "correct" transfer rates (16 GT/s) but rocminfo says only 2 of them have 16 GT/s and the other 2 have 8 GT/s. 

I wonder if this causes some issues with the driver being able to transfer data from host to GPUs and back? My program (I am doing a long running ML training session) crashes after 12 hours. 

[2gpu-rocmsmi.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162222/2gpu-rocmsmi.txt)
[2gpu-lspci.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162223/2gpu-lspci.txt)
[4gpu-lspci.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162224/4gpu-lspci.txt)
[4gpu-rocmsmi.txt](https://github.com/RadeonOpenCompute/ROCm/files/11162225/4gpu-rocmsmi.txt)
