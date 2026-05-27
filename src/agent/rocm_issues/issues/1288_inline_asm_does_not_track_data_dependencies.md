# inline asm does not track data dependencies

> **Issue #1288**
> **状态**: closed
> **创建时间**: 2020-11-13T10:50:40Z
> **更新时间**: 2020-11-16T16:31:49Z
> **关闭时间**: 2020-11-16T16:31:49Z
> **作者**: jjotero
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1288

## 描述

The following single-thread kernel gives wrong results on `timer`
```cuda
__global__ void myKernel(float * buffer, uint64_t * timer)
{
    uint64_t start, end;
    asm volatile("s_memtime %0" : "=r"(start));

    //... do some work on buffer here ...
    
    asm volatile("s_memtime %0" : "=r"(end));
    timer[0] = end-start;
}
```
It seems that the compiler does not track the data dependencies on the variable `end`, and the write to `timer[0]` occurs before `s_memtime` has returned the clock value. Here are the instructions from the second `asm` until the end of the kernel.
```isa
        ...
        s_memtime s[4:5]                                           // 00000000108C: C0900100 00000000
        s_sub_u32 s2, s4, s2                                       // 000000001094: 80820204
        s_subb_u32 s3, s5, s3                                      // 000000001098: 82830305
        s_waitcnt vmcnt(0)                                         // 00000000109C: BF8C0F70
        v_mov_b32_e32 v0, s0                                       // 0000000010A0: 7E000200
        v_mov_b32_e32 v2, s2                                       // 0000000010A4: 7E040202
        v_mov_b32_e32 v1, s1                                       // 0000000010A8: 7E020201
        v_mov_b32_e32 v3, s3                                       // 0000000010AC: 7E060203
        global_store_dwordx2 v[0:1], v[2:3], off                   // 0000000010B0: DC748000 007F0200
        s_endpgm 
```
Here `s_sub_u32 s2, s4, s2` and ` s_subb_u32 s3, s5, s3` run before `s[4:5]` have been filled with the right data. This of course can be fixed by replacing the asm code to 
```isa
 asm volatile ("s_memtime %0;\n"
               "s_waitcnt lgkmcnt(0);"  
               : "=r"(end)); 
```
My question here is, should the `s_waitcnt` instruction be inserted by the compiler, or is that something the user should take care of?

This was run on a Vega 20 card.

---

## 评论 (5 条)

### 评论 #1 — rkothako (2020-11-13T11:10:29Z)

Thanks @jjotero for reaching out.
We will get back to you soon on this.
Thank you.

---

### 评论 #2 — rkothako (2020-11-16T06:37:17Z)

Hi @jjotero 
Contacted developer and shared his inputs on this.

There is a __builtin_readcyclecounter() builtin that can be used to query the cycle counter.
We always recommend to use of inline asm should always be a last resort. And it is certainly not needed in this case.  

If you wish memory fences, you can/should add them explicitly.  And this is NOT by inserting an inline as s_waitcnt!

Hope this helps.


---

### 评论 #3 — jjotero (2020-11-16T09:49:03Z)

Hi @rkothako 
I'm aware of `__builtin_readcyclecounter()`, that's basically the same as calling `clock()`, right? I know that for the above example the inline asm is not needed, but this example is just a reproducer to show my point. As far as I know, memory fences are used to ensure consistency across multiple threads, but this is a single thread kernel, so it shouldn't be needed here.

Below is the ISA code using `__builtin_readcyclescounter()` instead of the inline asm. It turns out that what the builtin function does is adding a `s_waitcnt`. The only difference with the my inline asm fix from above is that now there are a few other instructions in between to hide the latency of `s_memtime`, which is exactly what I'm trying to prevent by using inline asm.

```asm
        ...
        s_memtime s[4:5]                                           // 00000000108C: C0900100 00000000                                                    
        s_waitcnt vmcnt(0)                                         // 000000001094: BF8C0F70 
        v_mov_b32_e32 v0, s0                                       // 000000001098: 7E000200                                                             
        v_mov_b32_e32 v1, s1                                       // 00000000109C: 7E020201                                                             
        s_waitcnt lgkmcnt(0)                                       // 0000000010A0: BF8CC07F                                                             
        s_sub_u32 s2, s4, s2                                       // 0000000010A4: 80820204                                                             
        s_subb_u32 s3, s5, s3                                      // 0000000010A8: 82830305                                                             
        v_mov_b32_e32 v2, s2                                       // 0000000010AC: 7E040202                                                             
        v_mov_b32_e32 v3, s3                                       // 0000000010B0: 7E060203                                                             
        global_store_dwordx2 v[0:1], v[2:3], off                   // 0000000010B4: DC748000 007F0200                                                    
        s_endpgm 
```
All this is fine, but I'm just wondering if after inserting the `s_memtime` asm inline, it should be the compiler inserting the `s_waitcnt` or the user.

---

### 评论 #4 — b-sumner (2020-11-16T15:52:28Z)

The compiler does not "look inside" the assembler template.  All of its decisions are based on the qualifiers, operands, and clobbers.

If optimizations are enabled, it is only a matter of luck when attempts to time a group of source statements are successful.

---

### 评论 #5 — jjotero (2020-11-16T16:31:49Z)

Hi @b-sumner 
All clear now. Thanks!

---
