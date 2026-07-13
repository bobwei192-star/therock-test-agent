# Support your GPUs for 8+ years, like Nvidia does, including gfx906 GPUs

- **Issue #:** 2308
- **State:** closed
- **Created:** 2023-06-30T07:48:02Z
- **Updated:** 2024-10-13T15:42:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/2308

I was utterly amazed to read this in the ROCm 5.6 [release notes](https://rocm.docs.amd.com/en/latest/CHANGELOG.html#rocm-5-6-0):

> - AMD Instinct MI50, Radeon Pro VII, and Radeon VII products (collectively referred to as gfx906 GPUs) will be entering the maintenance mode starting Q3 2023. This will be aligned with ROCm 5.7 GA release date.
>   - No new features and performance optimizations will be supported for the gfx906 GPUs beyond ROCm 5.7
>   - Bug fixes / critical security patches will continue to be supported for the gfx906 GPUs till Q2 2024 (End of Maintenance [EOM])(will be aligned with the closest ROCm release)

The Vega 20 GPU (gfx906) is barely 5 years old. Even more, the Radeon VII, Radeon Pro VII and Instinct MI50 are still being sold!

If you want to know why everyone is going with Nvidia, there are a lot of them, but what they do at least well is they support they GPUs.

In the CUDA 12.x release from December 2022, Nvidia also [dropped support](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-libraries) for some GPUs:

> Support for the following compute capabilities is removed for all libraries:
> - sm_35 (Kepler)
> - sm_37 (Kepler)

Yes, you read that right, _Kepler_ GPUs. These are 2014 products. Not 2019 products like you're dropping.

So, hereby I would you strongly urge to not force us all to Nvidia again, by properly supporting your products.