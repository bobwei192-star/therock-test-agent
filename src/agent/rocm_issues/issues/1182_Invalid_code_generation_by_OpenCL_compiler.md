# Invalid code generation by OpenCL compiler

> **Issue #1182**
> **状态**: closed
> **创建时间**: 2020-07-23T15:00:23Z
> **更新时间**: 2021-04-08T11:48:42Z
> **关闭时间**: 2021-04-08T11:48:42Z
> **作者**: athas
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1182

## 描述

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


---

## 评论 (11 条)

### 评论 #1 — athas (2020-07-23T15:06:02Z)

I am using a Vega 64 in case it matters.

---

### 评论 #2 — b-sumner (2020-07-23T15:19:26Z)

@athas, just to be clear, the result printed by the program is supposed to be 10?  The input to the kernel is constructed so 10 is the only correct answer?  Do you get 10 when you add -O0 to the Build options?

---

### 评论 #3 — athas (2020-07-23T15:29:27Z)

Yes, the result is supposed to be 10.  The first thread writes exactly 10 (in a convoluted way) to a zero-initialised memory block.

Using `-O0` does not change the result.  I do vaguely remember that disabling optimisations made the original program run correctly, but I cannot reproduce that behaviour for this cut-down example.

---

### 评论 #4 — athas (2020-07-23T16:46:59Z)

The use of `CL_MEM_USE_HOST_PTR` does not matter here; I actually intended `CL_​MEM_​COPY_​HOST_​PTR`.

---

### 评论 #5 — b-sumner (2020-07-23T21:08:45Z)

Thanks.  I'm making the change because the spec says: "The result of OpenCL commands that operate on multiple buffer objects created with the same host_ptr or overlapping host regions is considered to be undefined."

---

### 评论 #6 — b-sumner (2020-07-23T21:44:38Z)

I would appreciate it if you could walk me through why you expect global ID 0 to reach the write to "mem_175" and why "x_acc_195" should be 0 at that point.

---

### 评论 #7 — athas (2020-07-23T22:49:52Z)

The only way that global ID 0 could avoid writing to `mem_175` is if it hits one of the `goto` statements, and with the initial memory contents (all zeroes), this cannot possibly happen (specifically, `bounds_check_132` and `bounds_check_151` will always be true, because what's going on here is a binary search).

Apart from following the control flow, which I admit is a bit convoluted, it can also be verified in other ways.  Either by inserting `printf()` statements before the `goto`s (and observing that no printing takes place), or by noting that if the `goto`s are taken, then `local_failure` must be true, yet the `if (local_failure) ...` branch is not taken (this can be verified with printing, or more reliably by writing some distinguished value to memory).

The program is rather sensitive to small changes.  For example, if we insert the following statement before *both* `goto` statements, then the program prints the right result (`10`):

```
((__global int *) mem_175)[get_local_id(0)] = 0;
```

This statement is a no-op, because the memory contents are already zero.  This is what makes me suspect a subtle optimiser bug or something like it.

---

### 评论 #8 — ROCmSupport (2021-01-29T12:02:00Z)

Hi @athas 
Got an update on this issue that: issue is fixed with the latest ROCm code.
I will verify and update more on this.
Thank you.

---

### 评论 #9 — ROCmSupport (2021-01-29T12:13:41Z)

Hi @athas 
Verified with our internal builds and issue is fixed and the changes will be part of next ROCm release.
Same is failing with ROCm 4.0 too, its giving "0" output.

**Output with our internal builds:**

$ gcc reproduce.c -I/opt/rocm/opencl/include -L/opt/rocm/opencl/lib -lOpenCL -o reproduce
$ ./reproduce
10


---

### 评论 #10 — athas (2021-01-29T12:14:55Z)

That is excellent news!  I am now looking very much forward to the next ROCm release.  Thank you!

---

### 评论 #11 — ROCmSupport (2021-04-08T11:48:42Z)

Verified and issue is fixed with 4.1.
Thank you.

---
