# need asm instruction set for AMD

- **Issue #:** 1209
- **State:** closed
- **Created:** 2020-09-01T11:06:12Z
- **Updated:** 2024-10-06T08:04:19Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/1209

Hi  ,

Here is the asm example for  Nvidia .

_device__ inline void load_streaming_double2(double2 &a, const double2* addr)
  {   
    // double x, y;
    asm("ld.cs.global.v2.f64 {%0, %1}, [%2+0];" : "=d"(x), "=d"(y) : __PTR(addr));
    // a.x = x;  a.y = y;
  }
 I could find any asm instruction set for AMD,
 Can you please help me reference documents or  asm instruction set for  AMD .


Regards,
Srinivas
