# How to allocate more memory to my Ryzen APU's GPU?

- **Issue #:** 2014
- **State:** closed
- **Created:** 2023-04-03T09:00:56Z
- **Updated:** 2025-02-04T23:40:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/2014

I am running AMD 6800U on my Ubuntu 22.04 and I installed the AMD driver. I checked that the default system would allocate 512MB RAM to VRAM to the GPU.

I followed [some instruction](https://github.com/RadeonOpenCompute/ROCm/issues/1756#issuecomment-1159603527) from other github issue to create a rocm/pytorch docker image and it has no problem detecting my GPU but it has problem running sample program, due to `OutOfMemoryError`.

```
torch.cuda.OutOfMemoryError: HIP out of memory. Tried to allocate 2.00 MiB (GPU 0; 512.00 MiB total capacity; 150.39 MiB already allocated; 312.00 MiB free; 168.00 MiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_HIP_ALLOC_CONF
```

So my guess is ROCm support APU but I just need to allocate more system memory to my GPU before going into the docker environment. Are there any people who know how to modify the memory allocation of AMD APU? Thanks in advance