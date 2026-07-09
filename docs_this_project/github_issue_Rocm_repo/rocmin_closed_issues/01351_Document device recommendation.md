# Document device recommendation

- **Issue #:** 1351
- **State:** closed
- **Created:** 2020-12-30T08:55:51Z
- **Updated:** 2024-01-24T15:41:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1351

The documentation currently states that there are "supported" and "not officially supported" GPUs for ROCm:

<https://github.com/RadeonOpenCompute/ROCm#supported-gpus>

As recently stated, there are a set of devices which are recommended for use with ROCm:

> As complete support of ROCm works with gfx9 devices like Vega64, MI50(Vega 20), Radeon 7, recommend to use this type of card only.

_Originally posted by @ROCmSupport in https://github.com/RadeonOpenCompute/ROCm/issues/1148#issuecomment-747849233_

I suggest using this wording in the documentation, as it more closely conveys the distinction between such hardware, that might work ("supported") and such hardware, that should to work ("recommended").