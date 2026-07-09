# inline asm does not track data dependencies

- **Issue #:** 1288
- **State:** closed
- **Created:** 2020-11-13T10:50:40Z
- **Updated:** 2020-11-16T16:31:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/1288

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