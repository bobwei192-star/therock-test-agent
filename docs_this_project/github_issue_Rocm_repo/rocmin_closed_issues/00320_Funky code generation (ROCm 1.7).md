# Funky code generation (ROCm 1.7)

- **Issue #:** 320
- **State:** closed
- **Created:** 2018-02-01T08:07:03Z
- **Updated:** 2018-08-26T14:48:15Z
- **Labels:** Compiler Functional Bug
- **URL:** https://github.com/ROCm/ROCm/issues/320

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
