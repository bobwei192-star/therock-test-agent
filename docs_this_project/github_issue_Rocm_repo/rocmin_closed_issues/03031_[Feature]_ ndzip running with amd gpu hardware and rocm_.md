# [Feature]: ndzip running with amd gpu hardware and rocm?

- **Issue #:** 3031
- **State:** closed
- **Created:** 2024-04-17T14:39:48Z
- **Updated:** 2025-07-08T14:24:30Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/3031

### Suggestion Description

NDzip is a fast zip implementation to GPU.
With fast pci ssd cpu is often not fast enough. 
with GPU 75 GB/s are possible in compression and decompression.

Ndzip better than NVIDIA nvCOMP. nvCOMP is closed source with version 2.3 and higher.

Is ndzip running on amd gpu? Or is something to do by amd ROCm?

See 
https://github.com/celerity/ndzip
https://dps.uibk.ac.at/~fabian/slides/2021-sc21-ndzip-gpu-efficient-lossless-compression-of-scientific-floating-point-data-on-gpus.pdf
https://dps.uibk.ac.at/~fabian/publications/2021-ndzip-gpu-efficient-lossless-compression-of-scientific-floating-point-data-on-gpus.pdf

https://github.com/NVIDIA/nvcomp
https://developer.nvidia.com/blog/accelerating-lossless-gpu-compression-with-new-flexible-interfaces-in-nvidia-nvcomp/
https://developer.nvidia.com/nvcomp




### Operating System

_No response_

### GPU

_No response_

### ROCm Component

where is ROCm gpu Compression tool like rocmZIP?