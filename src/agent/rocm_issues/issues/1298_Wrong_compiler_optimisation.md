# Wrong compiler optimisation

> **Issue #1298**
> **状态**: closed
> **创建时间**: 2020-11-19T19:19:13Z
> **更新时间**: 2020-11-23T16:07:32Z
> **关闭时间**: 2020-11-20T17:39:16Z
> **作者**: jjotero
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1298

## 描述

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

---

## 评论 (6 条)

### 评论 #1 — b-sumner (2020-11-19T22:26:35Z)

The ISA above looks like the ISA for the Latency1 variant.

The first waitcnt makes s[0:1] and s[2:3] ready, and the second waitcnt makes s[6:7] ready.  The 3rd waitcnt is introduced by the compiler to make s[0:1] ready, because it does not look in the inline asm instruction template and doesn't "know" that waitcnts are present there.  The only information the compiler has is provided by the inline asm constraints.

I don't see anything wrong with the Latency1 ISA.  What is your program printing?


---

### 评论 #2 — jjotero (2020-11-20T08:44:42Z)

The program prints the following
```bash
Clocks (wrong) 3024
Clocks (right) 40
```
where the output from `Clocks (wrong)` changes every time.

---

### 评论 #3 — b-sumner (2020-11-20T17:39:16Z)

@jjotero I think you are making incorrect assumptions.  If you look carefully at the ISA for Latency2, you will see there there are no scalar memory operations before the first s_memtime.  As I mentioned earlier, the first waitcnt in the Latency1 code is waiting for an s_load_dwordx2 in addition to the s_memtime.  Those two operations can complete out of order,  The s_memtime completes quickly, but if the load misses, it will take a long time and the first waitcnt waits for it to complete.

There is no compiler issue here.  And these complexities are just one reason why we strongly encourage developers to use inline asm only as a last option when absolutely necessary.

---

### 评论 #4 — b-sumner (2020-11-20T17:46:23Z)

@jjotero I meant to thank you earlier for the lovely short example code.  That really helped speed up reaching a conclusion!

---

### 评论 #5 — jjotero (2020-11-23T09:16:18Z)

@b-sumner I'd appreciate if you could expand on those incorrect assumptions you say I'm making. I do share with you that developers should avoid asm as much as possible, but I'm just trying to expose the latency of `s_memtime` and inline asm is the only way to do so.
What I don't understand with the ISA shown above is why the `v_mov_b32_e32 v3, s7` is after the last `s_waitcnt`. Shouldn't that be in between `v_mov_b32_e32 v2, s6` and that last `s_waitcnt`? Both `s6` and `s7` have the result from the last `s_memtime`, so I see no reason why there would be a `s_waitcnt` in between. But even if that isn't the issue, why does the Latency1 gives wrong results? I'd just like to know which would be the right way to write such code.

---

### 评论 #6 — b-sumner (2020-11-23T16:07:31Z)

@jjotero why are you concerned about the position of the mov of s7 to v3?  It is correct to place there is it not?

Also, what makes you believe that Latency1 is giving the wrong answer?  I already explained that is including the time of the first load which could be very expensive.

---
