# OpenCL compile failure with inline assembly for Polaris

- **Issue #:** 392
- **State:** closed
- **Created:** 2018-04-23T10:20:01Z
- **Updated:** 2018-10-24T04:34:07Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/392

Below is a kernel that fails to compile for Polaris (mcpu=gfx803).  This kernel compiles and functions correctly for Vega (mcpu=gfx900).  Attempting to compile for Polaris produces the following error: `error: couldn't allocate output register for constraint 'v' at line 104`  I believe all instructions/features used in the assembly are GCN 1.2 compatible and should compile for Polaris.

```
inline short2 mad_short2(short2 a, short2 b, short2 c)
{
    short2 result;
     __asm (
            "v_mul_lo_u16_sdwa  %[result], %[a],        %[b] dst_sel:WORD_0 dst_unused:UNUSED_PRESERVE src0_sel:WORD_0 src1_sel:WORD_0\n"
            "v_mul_lo_u16_sdwa  %[result], %[a],        %[b] dst_sel:WORD_1 dst_unused:UNUSED_PRESERVE src0_sel:WORD_1 src1_sel:WORD_1\n"
            "v_add_u16_sdwa     %[result], %[result],   %[c] dst_sel:WORD_0 dst_unused:UNUSED_PRESERVE src0_sel:WORD_0 src1_sel:WORD_0\n"
            "v_add_u16_sdwa     %[result], %[result],   %[c] dst_sel:WORD_1 dst_unused:UNUSED_PRESERVE src0_sel:WORD_1 src1_sel:WORD_1\n"
            : [result] "=&v" (result)
            : [a] "v" (a), [b] "v" (b), [c] "v" (c)
            );
    
    return result; 
}   
    
__kernel 
void mad_test(__global uint4 *data)
{   
    short2 a = {-1235,-7};
    short2 b = {-15,20000};
    short2 c = {-34,-41};
    short2 result = mad_short2(a,b,c);

    printf("result : %x\n", as_uint(result));
    printf("ref    : %x\n", as_uint(a * b + c));
}
```