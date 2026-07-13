# Wrong compiler optimisation

- **Issue #:** 1298
- **State:** closed
- **Created:** 2020-11-19T19:19:13Z
- **Updated:** 2020-11-23T16:07:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/1298

The code below uses inline `asm` to expose the latency of reading the clocks. However, the kernel `clockLatency1` gives wrong results when compiling with `-O2` or above. Rewriting the code as shown in `clockLatency2` gives the correct results. 
```cuda
#include <iostream>
#include <hip/hip_runtime.h>
#include <cstdint>

/*
 *
 * ROCm 3.9
 *
 * --amdgpu-target=gfx906
 */

__global__ void clockLatency1(uint64_t *c)
{
    /* This does not work with -O2 and above */
    asm volatile ("s_memtime %[a];\n\t"
                  "s_waitcnt lgkmcnt(0);\n\t"
                  "s_memtime %[b];\n\t"
                  "s_waitcnt lgkmcnt(0);\n\t"
                  :[a]"=r"(c[0]), [b]"=r"(c[1]) :: "memory");
}

__global__ void clockLatency2(uint64_t *c)
{
    /* This works */
    uint64_t c0, c1;
    asm volatile ("s_memtime %[a];\n\t"
                  "s_waitcnt lgkmcnt(0);\n\t"
                  "s_memtime %[b];\n\t"
                  "s_waitcnt lgkmcnt(0);\n\t"
                  "s_mov_b64 %[c] %[a];\n\t"
                  "s_mov_b64 %[d] %[b];\n\t"
                  "s_waitcnt lgkmcnt(0);\n\t"
                  : [a]"=s"(c0), [b]"=s"(c1), [c]"=r"(c[0]), [d]"=r"(c[1]) :: "memory");
}

int main()
{
  uint64_t c[2];
  uint64_t *c_d;
  hipMalloc((void**)&c_d, sizeof(uint64_t)*2);

  // Wrong clock latency
  clockLatency1<<<1,1>>>(c_d);
  hipDeviceSynchronize();
  hipMemcpyDtoH(c, c_d, sizeof(uint64_t)*2);
  std::cout << "Clocks (wrong) " << (c[1]-c[0]) << std::endl;
  
  // Right clock latency
  clockLatency2<<<1,1>>>(c_d);
  hipDeviceSynchronize();
  hipMemcpyDtoH(c, c_d, sizeof(uint64_t)*2);
  std::cout << "Clocks (right) " << (c[1]-c[0]) << std::endl;

  hipFree(c_d);
  return 0;
}
```
Inspecting the ISA code from `clockLatency1`(with `-O3`) we can see that `s_waitcnt lgkmcng(0)` is misplaced ahead of `v_mov_b32_e32 v3, s7`. However, the kernel `clockLatency2` enforces the right ordering, which is why it gives the correct results.
```asm
0000000000001000 <_Z12clockLatencyPm$local>:
        s_load_dwordx2 s[0:1], s[4:5], 0x0                         // 000000001000: C0060002 00000000
        s_memtime s[2:3]                                           // 000000001008: C0900080 00000000
        s_waitcnt lgkmcnt(0)                                       // 000000001010: BF8CC07F
        s_memtime s[6:7]                                           // 000000001014: C0900180 00000000
        s_waitcnt lgkmcnt(0)                                       // 00000000101C: BF8CC07F
        v_mov_b32_e32 v0, s2                                       // 000000001020: 7E000202
        v_mov_b32_e32 v1, s3                                       // 000000001024: 7E020203
        v_mov_b32_e32 v2, s6                                       // 000000001028: 7E040206
        s_waitcnt lgkmcnt(0)                                       // 00000000102C: BF8CC07F
        v_mov_b32_e32 v5, s1                                       // 000000001030: 7E0A0201
        v_mov_b32_e32 v3, s7                                       // 000000001034: 7E060207
        v_mov_b32_e32 v4, s0                                       // 000000001038: 7E080200
        global_store_dwordx4 v[4:5], v[0:3], off                   // 00000000103C: DC7C8000 007F0004
        s_endpgm 
```