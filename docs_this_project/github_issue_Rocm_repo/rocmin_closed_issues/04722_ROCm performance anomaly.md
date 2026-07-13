# ROCm performance anomaly

- **Issue #:** 4722
- **State:** closed
- **Created:** 2025-05-08T10:51:09Z
- **Updated:** 2025-05-13T17:57:43Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4722

I have elementaryOS/ubuntu 24.04 and  rocm 6.4 setup with gfx1100 on my system following this guide (--usecase=rocm): https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/amdgpu-installer/amdgpu-installer-ubuntu.html

Further, I built llama.cpp on my system using this guide (for HIP build I used `-DGGML_HIP_ROCWMMA_FATTN=ON` option) : https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md 

When I use LM Studio (0.3.15 Build 11), it offers vulkan and rocm runtime options: ROCm llama.cpp (Linux) v1.29.0 and Vulkan llama.cpp (Linux) v1.29.0. I don't know if it employs the rocm installation of the system. 

I loaded a gemma 3 12b (q8) model on the gpu using both runtime options sequentially (ROCm then Vulkan). For a given question asked on both runtime cases I get the following outcome: 

![Image](https://github.com/user-attachments/assets/fb4c06a7-7986-479f-a870-3146cc25d829)

![Image](https://github.com/user-attachments/assets/39cf64b9-f4f1-4cc5-a3e8-e193dbaa1353)

![Image](https://github.com/user-attachments/assets/6d051c5c-19de-431d-b1db-4c2a483a87d3)

ROCm : 16.91 tok/sec, 1514 tokens, 3.49s to first token, Stop reason: EOS Token Found
Vulkan: 24.43 tok/sec, 1514 tokens, 4.93s to first token, Stop reason: EOS Token Found

This outcome is consistently repeatable (within reasonable margins).

I thought that ROCm was supposed to be the faster scheme. Is this an issue with LM Studio or the ROCm installation? 

Much thanks for any time and effort expended shedding light on the issue or any help resolving it. 