# Funky code generation (ROCm 1.7)

> **Issue #320**
> **状态**: closed
> **创建时间**: 2018-02-01T08:07:03Z
> **更新时间**: 2018-08-26T14:48:15Z
> **关闭时间**: 2018-08-25T20:05:46Z
> **作者**: preda
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/320

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

(ROCm 1.7, Ubuntu 17.10, Vega 64).

In my OpenCL kernel, I replaced this block ("old"):
```
  fft4(u);
  shufl(256, lds,   u, 4, 64);
  tabMul(256, trig, u, 4, 64);
  
  fft4(u);
  bar();
  shufl(256, lds,   u, 4, 16);
  tabMul(256, trig, u, 4, 16);
  
  fft4(u);
  bar();
  shufl(256, lds,   u, 4, 4);
  tabMul(256, trig, u, 4, 4);

  fft4(u);
  bar();
  shufl(256, lds,   u, 4, 1);
  tabMul(256, trig, u, 4, 1);

  fft4(u);
```

With this equivalent block ("new"):

```
  for (int s = 6; s >= 0; s -= 2) {
    fft4(u);
    
    if (s != 6) { bar(); }
    shufl (256, lds,  u, 4, 1 << s);
    tabMul(256, trig, u, 4, 1 << s);
  }

  fft4(u);
```
And no other changes. Please remark that these two blocks are exactly and unconditionally equivalent, and a compiler could see that too.

Yet the generated ISA for a kernel using the above block is (comparison old/new):
[carryconv-new.txt](https://github.com/RadeonOpenCompute/ROCm/files/1684627/carryconv-new.txt)
[carryconv-old.txt](https://github.com/RadeonOpenCompute/ROCm/files/1684628/carryconv-old.txt)

Old kernel has:  workitem_vgpr_count = 116
New: workitem_vgpr_count = 45

Also the "new" kernel is about 30% smaller (instruction count), and about 7% faster.

The problem is: the compiler should have generated identical code for the two cases (hopefully the better variant), because the source change here is "immaterial". But as seen here, the compiler displays "chaotic" code generation, random behavior which has major consequences and yet can't be understood or predicted by the developer.

For details / repro, the source is:
https://github.com/preda/gpuowl/blob/387cbf64dc25bf9eb13e0ce613f2c7d699ad053b/gpuowl.cl#L315


---

## 评论 (13 条)

### 评论 #1 — pacxx (2018-02-01T08:28:10Z)

These two code parts may be semantically equivalent but are not equal for the compiler in any case. 

The first code has no control-flow while the second has. The compiler may choose to unroll the loop or may not depending on the heuristics implemented in loop unrolling. There is no optimization that transforms the old code back to the new code (at least i don't know about loop un-unrolling). 

Another thing is inlining: in the first code the compiler may inline all functions in the kernel (or may not depending on the inlining threshold). In the second code inlining the function happens commonly before loop transformations are performed what may explain why you see a reduction in code size and also registers the loop unroll transformation may reject the loop for unrolling because the unrolling would be to exepensive in terms of code size.

From my point of view the code generation is not chaotic at all and the changes to the code cannot considered "immaterial" from the compiler's perspective. The compiler handles what you give it and in this case the manually unrolling of the loop is just the worse implementation which the compiler cannot fix for you.

---

### 评论 #2 — preda (2018-02-01T09:45:57Z)

@pacxx: OK, I see what you say.

But the "loop un-unrolling" (or, let's call it "loop forming") not happening in the "old" block only explains the difference in instruction count, but not the difference in VGPR usage, isn't it?

I mean, even with no loop as in "old", there's nothing keeping the compiler from re-using the VGPRs like in the looped code, even if the compiler does not see a loop. Yet, the compiler doesn't do that, and that's a big problem.

(in practice, VGPR pressure being a worse problem than code size).


---

### 评论 #3 — pacxx (2018-02-01T11:26:09Z)

I looked at your code and regarding VGPR pressure you'r right. 116 VGPRs is way to much in the frist place so there might be an issue with the register liveness here. The "new" code may not triger this problem.


---

### 评论 #4 — preda (2018-02-14T21:33:58Z)

I have a new case. Compare these two exactly equivalent implementations:
A:
```
void fft4KImpl(local T *lds, T2 *u, const G T2 *trig) {
  for (int s = 64; s >= 1; s /= 8) {
    fft8(u);

    if (s != 64) { bar(); }
    shufl (512, lds,  u, 8, s);
    tabMul(512, trig, u, 8, s);
  }
  fft8(u);
}
```
B:
```
void fft4KImpl(local T *lds, T2 *u, const G T2 *trig) {
  for (int s = 6; s >= 0; s -= 3) {
    fft8(u);

    if (s != 6) { bar(); }
    shufl (512, lds,  u, 8, 1 << s);
    tabMul(512, trig, u, 8, 1 << s);
  }
  fft8(u);
}
```

Yet the generated code is radically different, see attached ISA for a kernel that uses this block.
[autoConv-A.txt](https://github.com/RadeonOpenCompute/ROCm/files/1725711/autoConv-A.txt)
[autoConv-B.txt](https://github.com/RadeonOpenCompute/ROCm/files/1725718/autoConv-B.txt)



---

### 评论 #5 — gstoner (2018-02-27T05:20:22Z)


@preda can. you try out Beta 3 just as general test http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.3.tar.bz2   We still have to address the DAL. issue. 

---

### 评论 #6 — preda (2018-03-01T02:43:05Z)

I'll look into this, but please allow a couple of days as I'm a bit busy ATM.

---

### 评论 #7 — jlgreathouse (2018-08-24T00:55:29Z)

Hi @preda 

Any update on this since February? :)

---

### 评论 #8 — preda (2018-08-24T02:44:46Z)

Sorry I forgot about this until you reminded me :)

So I checked now, on ROCm 1.8.2, Vega 64, Ubuntu 18.04, and the issue is still present, meaning:
choosing one or the other option (above) produces significant differences in generated code, in number of VGPR used, number of instructions, and performance.

While both function correctly, I'd say this is a missed optimization opportunity on the part of the compiler (i.e. at least one of the two options is compiled inefficiently).

---

### 评论 #9 — preda (2018-08-24T02:59:46Z)

I attach the two ISA dumps. It seems only the variant without shift (A) is unrolled.
```
// 512x8
void fft4K(local T *lds, T2 *u, const T2 *trig) {
  /*
    // A:
  for (int s = 64; s >= 1; s /= 8) {
    fft8(u);

    if (s != 64) { bar(); }
    shufl (512, lds,  u, 8, s);
    tabMul(512, trig, u, 8, s);
  }
  */

  // B:
  for (int s = 6; s >= 0; s -= 3) {
    fft8(u);
    if (s != 6) { bar(); }
    shufl( 512,  lds, u, 8, 1 << s);
    tabMul(512, trig, u, 8, 1 << s); 
  }

  fft8(u);
}
void fft_WIDTH(local T *lds, T2 *u, Trig trig) {
  fft4K(lds, u, trig);
}

KERNEL(512) fftW(P(T2) io, Trig smallTrig) {
  local T lds[8];
  T2 u[8];

  uint g = get_group_id(0);
  io += 4096 * g;

  read(512, 8, u, io, 0);
  fft_WIDTH(lds, u, smallTrig);  
  write(512, 8, u, io, 0);
}
```
[a.txt](https://github.com/RadeonOpenCompute/ROCm/files/2316863/a.txt)
[b.txt](https://github.com/RadeonOpenCompute/ROCm/files/2316864/b.txt)



---

### 评论 #10 — preda (2018-08-24T03:05:36Z)

To repro: check out gpuowl https://github.com/preda/gpuowl/
make
echo "332345953" > worktodo.txt
mkdir isa
./openowl -fft +5 -dump isa

You should see an output line like this:
FFT 20480K: Width 4096 (512x8), Height 512 (64x8), Middle 5; 15.85 bits/word
confirming that the fft4K is used.


---

### 评论 #11 — preda (2018-08-24T06:41:22Z)

ROCm 1.8.2, Vega64.
Another case of divergent code generation for equivalent source
https://github.com/preda/gpuowl/tree/f52de94331d21b46448d831f61ffac8d3dcfd2e5

The difference is between calling two auxiliary functions from shuflAndMul() vs. inlining them there (see below).

```
< 		workitem_vgpr_count = 146
> 		workitem_vgpr_count = 211
```

```
void shufl(uint WG, local T *lds, T2 *u, uint n, uint f) {
  uint me = get_local_id(0);
  uint m = me / f;
  
  for (int b = 0; b < 2; ++b) {
    if (b) { bar(); }
    for (uint i = 0; i < n; ++i) { lds[(m + i * WG / f) / n * f + m % n * WG + me % f] = ((T *) (u + i))[b]; }
    bar();
    for (uint i = 0; i < n; ++i) { ((T *) (u + i))[b] = lds[i * WG + me]; }
  }
}

void tabMul(uint WG, const T2 *trig, T2 *u, uint n, uint f) {
  uint me = get_local_id(0);
  for (int i = 1; i < n; ++i) { u[i] = mul(u[i], trig[me / f + i * (WG / f)]); }
}

void shuflAndMul(uint WG, local T *lds, const T2 *trig, T2 *u, uint n, uint f) {
#if 1
  uint me = get_local_id(0);
  uint m = me / f;
  
  for (int b = 0; b < 2; ++b) {
    if (b) { bar(); }
    for (uint i = 0; i < n; ++i) { lds[(m + i * WG / f) / n * f + m % n * WG + me % f] = ((T *) (u + i))[b]; }
    bar();
    for (uint i = 0; i < n; ++i) { ((T *) (u + i))[b] = lds[i * WG + me]; }
  }

  for (int i = 1; i < n; ++i) { u[i] = mul(u[i], trig[me / f + i * (WG / f)]); }
#else
  shufl(WG, lds, u, n, f);
  tabMul(WG, trig, u, n, f);
#endif
}
```
[18M_0_gfx900.txt](https://github.com/RadeonOpenCompute/ROCm/files/2317299/18M_0_gfx900.txt)
[18M_0_gfx900.txt](https://github.com/RadeonOpenCompute/ROCm/files/2317300/18M_0_gfx900.txt)


---

### 评论 #12 — jlgreathouse (2018-08-25T20:05:46Z)

Hi @preda 

Thank you for the feedback. We have passed these on to our compiler team as potential tests to look into when working on optimization passes. That said, I can't guarantee that these particular cases will be "fixed" (and I especially can't guarantee that they will ever produce identical code).

As mentioned above, the code itself is not necessarily "unconditionally equivalent" from a compiler's perspective. They are functionally equivalent, but it's not like the compilers we use lift the code up to a purely functional representation before doing optimizations. The empirical representations are different, and thus these functions may take very different paths through the many optimization loops.

If you are really worried about VGPR counts, you may want to look into setting a [max-VGPR attribute](https://clang.llvm.org/docs/AttributeReference.html#amd-gpu-attributes). I can't guarantee this will create faster code (the compiler may start spilling/filling, which is likely always bad). However, it's an option for you to explore.

That said, because we are not tracking this exact piece of code as a "functional bug" per se, I'm going to close this ticket. Nevertheless, thanks for reporting this -- your test samples are useful. :)

---

### 评论 #13 — preda (2018-08-26T14:46:27Z)

@jlgreathouse thank you for pointing out the way to control register counts, I was not aware of that attribute, I'm going to try it out.

About the compiler and generated code -- I'm not fussy about the generated code not being canonicalized, and that was not the point of this issue.

But what I do expect from the compiler is a reliable, consistent optimization. I would call it "reliable quality of the generated code".

If I make an insignificant change in my code, such as (as an exaggerated example) changing
for (int i = 0; i < n; ++i) to for (int i =0; i <= n-1; i++)
and as a result the compiler generates code that is 10% slower or faster,
then I don't trust the compiler anymore. Instead of concentrating on writing the source code, and trusting the compiler to do its job well, I need to verify which of the many equivalent ways to write my code gets compiled to the "fast" version.

But things are getting better IMO, and the quality of the generated code is improving. I'm OK with closing this issue; -- if in the future I'll see serious cases of mis-optimization for equivalent code, I'll file with specifics.

Anyway I'm looking forward to trying 1.9 first, which maybe already fixes some problems.

---
