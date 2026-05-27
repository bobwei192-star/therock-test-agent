# Regression in rocm 5.3 and newer for gfx1010

> **Issue #2527**
> **状态**: closed
> **创建时间**: 2023-10-05T20:01:29Z
> **更新时间**: 2024-11-14T19:08:39Z
> **关闭时间**: 2024-11-14T19:08:39Z
> **作者**: DGdev91
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2527

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Since when pytorch 2 was officially released, i wasn't able to run it on my 5700XT, while i was previously able to use it just fine on pytorch 1.13.1 by setting "export HSA_OVERRIDE_GFX_VERSION=10.3.0"
There are many reporting the same issue on the 5000 series, like for example
https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/6420

--precison-full and --no-half are also needed because the card seems like can't use fp16 on linux/rocm, as already reported here https://github.com/RadeonOpenCompute/ROCm/issues/1857

i also read about the PCI atomics requirement, following this issue https://github.com/pytorch/pytorch/issues/103973
....But that doesn't seems to be my case. the command "grep flags /sys/class/kfd/kfd/topology/nodes/*/io_links/0/properties" returns:
```
/sys/class/kfd/kfd/topology/nodes/0/io_links/0/properties:flags 3
/sys/class/kfd/kfd/topology/nodes/1/io_links/0/properties:flags 1
```
Also, i tried to compile pytorch using the new "-mprintf-kind=buffered" flag, but it didn't change anything.



Finally, i recently found out that pytorch 2 works just fine on gfx1010 if that's compiled by rocm 5.2, as suggested here https://github.com/pytorch/pytorch/issues/106728


