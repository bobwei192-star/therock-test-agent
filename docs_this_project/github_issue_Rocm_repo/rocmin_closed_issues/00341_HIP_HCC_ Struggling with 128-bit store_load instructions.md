# HIP/HCC: Struggling with 128-bit store/load instructions

- **Issue #:** 341
- **State:** closed
- **Created:** 2018-02-20T18:18:42Z
- **Updated:** 2018-06-03T14:41:25Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/341

I am struggling to utilize global/flat load/store **dwordx4** instructions via HIP / HCC under ROCm 1.7. The problems are as follows:

~~### 1. dwordx4 instructions are apparently not generated for (some?) HIP vector types
Without writing inline assembly, the obvious way to get the compiler to emit 128-bit memory instructions would be to use 128-bit wide types. This did not work for me with `ulonglong2` and I think neither with `uint4`. The only type that reliably gets dwordx4 ops is `__uint128_t`, which is *not portable to CUDA.*~~

### 2. Writing dwordx4 inline asm gives "invalid in/output constraint"
Even with `__uint128_t`, directly writing asm to do a 128-bit mem instructions (because you want to add glc/slc flags, maybe) does not work.
```cpp
__uint128_t dst;
asm volatile( "global_load_dwordx4 %0, %1, off glc slc" : "=v" (dst) : "r" (address) );
```
This code gives **error: couldn't allocate output register for constraint 'v'**. Same for the store instruction. The only way I’ve found to make this work is to explicitly move your 32-bit pieces into contiguous registers before the instruction, and then just use them explicitly, like this:
```cpp
uint32_t data[4];
fill_data(data);
asm volatile(
                "v_mov_b32 v27, %1\n\t"
                "v_mov_b32 v28, %2\n\t"
                "v_mov_b32 v29, %3\n\t"
                "v_mov_b32 v30, %4\n\t"
                "global_store_dwordx4 %0, v[27:30], off\n\t"
                :
                : "r" (address), "v" (data[0]), "v" (data[1]), "v" (data[2]), "v" (data[3])
                : "v27", "v28", "v29", "v30", "memory" );
```
Which is obviously pretty clunky and costs you registers.

### 3. (How) does the explicit register constraint work?
In the [LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html) there is a small note about AMDGPU asm constraints.
>r: A 32 or 64-bit integer register.
>[0-9]v: The 32-bit VGPR register, number 0-9.
>[0-9]s: The 32-bit SGPR register, number 0-9.

I’ve tried to utilize it like this (to get around problem number 2), but to no avail:
```cpp
uint32_t data[4];
fill_data(data);
asm volatile(
                "global_store_dwordx4 %0, v[6:9], off\n\t"
                :
                : "r" (address), "6v" (data[0]), "7v" (data[1]), "8v" (data[2]), "9v" (data[3])
                : "memory" );
```
The error message is 
>invalid input constraint '6v' in asm
____
If you need more complete code samples in order to reproduce this, please let me know. :) 