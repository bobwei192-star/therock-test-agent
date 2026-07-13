# Difference between hip_bfloat16 and __hip_bfloat16?

- **Issue #:** 2534
- **State:** closed
- **Created:** 2023-10-09T00:42:40Z
- **Updated:** 2024-11-14T19:14:11Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2534

I'm using ROCm 5.7. Currently there are two datatypes for `bfloat16` -- `hip_bfloat16` and `__hip_bfloat16`. They seem to be defined respectively as

```
struct __hip_bfloat16 {
  unsigned short data;
};
```
(in `/opt/rocm-5.7.0/include/hip/amd_detail/amd_hip_bf16.h`) and

```
struct hip_bfloat16
{
    __hip_uint16_t data;
   // ...
};
```
(in `/opt/rocm-5.7.0/include/hip/amd_detail/amd_hip_bfloat16.h`).

Unfortunately there doesn't seem to be an out-of-the box way to convert between them. Some of the HIP operations expect `hip_bfloat16` and others expect `__hip_bfloat16`.

Would it be possible to either define an automatic conversion between them, or get rid of one of them? Also if there is any guidance on how to convert between them manually in the mean time, that would be helpful (I'm trying to do it by just creating the respective struct and assigning the `data` field). I didn't find more details about it in the docs :)

Your help is very much appreciated.