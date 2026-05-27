# OpenCL codegen: make use of the GCN VOP3 output modifiers

> **Issue #1021**
> **状态**: closed
> **创建时间**: 2020-02-24T10:35:49Z
> **更新时间**: 2021-05-09T19:54:12Z
> **关闭时间**: 2021-05-09T19:54:12Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1021

## 描述

The GCN VOP3 instructions offer an output modifier which is a multiplication by 0.5, 2, or 4 *for free*. OTOH the generated code for OpenCL never uses these output modifiers. This is a pity -- the generated code does not use GCN to its full power.

Please enable OMOD (output modifiers) in the generated code, at least when compiling with -cl-fast-relaxed-math.


---

## 评论 (12 条)

### 评论 #1 — preda (2020-02-24T11:32:15Z)

To illustrate, this OpenCL fragment
```
  // double a = ...
  double b = 4 * (a * a);
```
Is compiled to
```
v_mul_f64 v[2:3], v[2:3], v[2:3]
v_mul_f64 v[2:3], v[2:3], 4.0
```
but the second instruction becomes unnecessary if OMOD were used.

---

### 评论 #2 — b-sumner (2020-02-24T15:36:34Z)

@preda output modifiers are not compatible with denorms so at a minimum the options would have to include -cl-denorms-are-zero.  However, we have no plans to support denorm flushing for double precision where most users care more about accuracy.

---

### 评论 #3 — preda (2020-02-24T20:05:03Z)

what about users that request both -cl-fast-relaxed-math and -cl-denorms-are-zero ? I think it's pretty explicit that they are fine with flushed denorms, and that they care more about speed than accuracy.

Anyway, there should be a way to get really high performance GCN code generated, which ideally does not involve writing the GCN instructions by hand.


---

### 评论 #4 — b-sumner (2020-02-24T20:36:34Z)

Yes, we can consider enabling modifiers with that combination.  I have to admit it's pretty surprising that you're OK with flushing denorms in double precision work.  Why are you using double precision at all if you don't care about accuracy (I do know that precision and accuracy are completely different topics).

---

### 评论 #5 — preda (2020-02-25T11:33:21Z)

Here is an article discussing denormals: https://blogs.mathworks.com/cleve/2014/07/21/floating-point-denormals-insignificant-but-controversial-2/

In double-precission, denormals come into play for numbers with magnitude under 10^-308. It is possible that in gpuowl's case we commonly work with larger-magnitude values, in which situation the "flush denorms" has no impact on accuracy.

We use double precission because we need as many bits of precission per value as possible, and DP offers more than twice bits of mantissa compared to SP (I think 53 vs. 24). Of course DP is significantly slower than SP, but in our case it still pays offs to use DP.

BTW it may turn out that DP performance is an advantage of AMD GPUs compared to the competition; that's one more reason to push for really well optimized code out of the compiler, able to show what the hardware is capable of.


---

### 评论 #6 — ROCmSupport (2021-04-19T12:51:49Z)

Hi @preda 
Thanks for reaching out.
Can you please check and update on this with ROCm 4.1.
Feel free to share an update or close this issue, if no more relevant.
Thank you.

---

### 评论 #7 — preda (2021-04-19T13:38:05Z)

@ROCmSupport I can not try out ROCm 4.1 because it does not recognize my GPU (Radeon VII) anymore with the standard linux kernel (I can use any kernel between 5.4.x and 5.12.x, but apparently none works); this setup was working with earlier ROCm releases and was broken in 4.1. I'm waiting for a new ROCm release that works with the mainline amdgpu driver.

But coming back to the issue here, why do you ask me to re-check -- do you have any indication that this issues may have been fixed?


---

### 评论 #8 — valeriob01 (2021-04-19T14:30:46Z)

@preda I am using kernel 5.4 and it works, not sure if upstream driver ...


---

### 评论 #9 — ROCmSupport (2021-04-20T05:25:24Z)

Hi @preda 
Many changes went into ROCm 4.x code and found that many issues resolved too, hence I asked.

Thank you.

---

### 评论 #10 — preda (2021-04-27T10:01:06Z)

@b-sumner did the team enable OMOD with -cl-fast-relaxed-math and -cl-denorms-are-zero, as you previously said you might consider doing? if you confirm that yes (i.e. that some work was done in that direction), I'll check and confirm on 4.1. Otherwise, @ROCmSupport for sure it didn't "fix itself" on ROCm 4.1 simply because there were many changes in ROCm 4.1


---

### 评论 #11 — b-sumner (2021-04-27T16:53:07Z)

We have a review out for an option to disable IEEE mode that would likely need to be accompanied by -fno-honor-nans to get the desired effect, but it is currently stalled.

---

### 评论 #12 — preda (2021-05-09T19:54:12Z)

Merge into #1405 

---
