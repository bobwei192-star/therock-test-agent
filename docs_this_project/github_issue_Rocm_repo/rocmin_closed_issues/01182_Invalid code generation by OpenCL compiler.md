# Invalid code generation by OpenCL compiler

- **Issue #:** 1182
- **State:** closed
- **Created:** 2020-07-23T15:00:23Z
- **Updated:** 2021-04-08T11:48:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1182

I suspect the OpenCL compiler in ROCm 3.5 is generating invalid code for the kernel below.  The kernel is tricky in that it uses `goto` to escape from doubly-nested loops, and from inspecting the generated HSA assembly (where I'm not an expert) it looks like the compiler mistakenly detects the `goto`s as a distinct loop nesting, and (I think) mistakenly terminates the kernel early by jumping to the label when it shouldn't.  With both NVIDIA OpenCL and [oclgrind](https://github.com/jrprice/Oclgrind) the program below prints `10`, but it prints `0` with ROCm, which suggests that the final memory write is not executed at all.  The code is heavily simplified from a compiler-generated kernel, so the names are pretty bad and it doesn't compute anything sensible.  The `goto`s are used to implement bounds checking.

Here is the (purely boilerplate) host code, `reproduce.c`: https://gist.github.com/athas/babe7b1572d47a38ca9245ea1e72edfd

Here is the device code, `reproduce.cl`: https://gist.github.com/athas/def24345a9fa433c396a1dd31e28f63a

Put them in the same directory and compile with `gcc reproduce.c -o reproduce -lOpenCL`.  Then:

```
$ ./reproduce
0
$ oclgrind ./reproduce
10
```
