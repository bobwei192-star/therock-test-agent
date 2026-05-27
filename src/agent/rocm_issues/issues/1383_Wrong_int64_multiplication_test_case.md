# Wrong int64 multiplication test case

> **Issue #1383**
> **状态**: closed
> **创建时间**: 2021-02-16T13:23:06Z
> **更新时间**: 2024-01-12T13:13:10Z
> **关闭时间**: 2024-01-12T13:13:10Z
> **作者**: develancer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1383

## 描述

AMD OpenCL compiler used for RX 5700 XT with ROCM 4.0.1 sometimes generates invalid code for integer multiplication.

The self-contained example is here: https://github.com/develancer/amd-opencl-test-case

Disabling all compiler optimizations does not help.

---

## 评论 (26 条)

### 评论 #1 — ROCmSupport (2021-02-17T07:18:11Z)

Thanks @develancer for reaching out.
I tried the same code on Vega20(MI50) + ROCm 4.0 and am able to reproduce the issue.

The output is same as below from ROCm 3.5 to ROCm 4.0
77262ca4b90e3fcb55f32ba92841024688802f53e75b16196c399de799377ba7

But the output is different in ROCm 3.3
3c7beaf9aafd3e3990b4d1a7a65338417296facf06209627f93941ffcb607414

Can you please share some info like what is this output and what to understand more from output.
Based on your information, I will work on it and move this ticket to next level.

I request you to remove 5700 XT from the title and description as its not specific to it and its observed in all hardware mostly.

Thank you.

---

### 评论 #2 — develancer (2021-02-17T08:23:55Z)

Edited as requested. Thanks for taking time to reproduce this bug.

The output is a result of some abstract secp256k1 elliptic curve computations. Essentially, it calculates the group inverse of the product of z[0]…z[511] where z[i] is a z-element of the Jacobian form of the sum of prec[0]…prec[i], with prec being the included precomputed table. All calculations are performed on the secp256k1 elliptic curve.

As you can see, it does not have any intuitive interpretation. Unfortunately, it cannot be simplified, as any simpler test case I tried to come up with would not exhibit the same behavior anymore.

However, the calculations are 100% deterministic and don't include any undefined behavior. The correct result (as computed on NVidia GPUs or CPUs through POCL) should be
```
bbde464b6355ee6de6deba5ae860f8a66524937eee81dde224a0214efd795d09
```

---

### 评论 #3 — develancer (2021-02-17T11:59:06Z)

Forgot to notify you so here it goes: @ROCmSupport

---

### 评论 #4 — ROCmSupport (2021-02-18T05:39:48Z)

Thanks @develancer for the additional information.
I will assign to dev. Thank you.

---

### 评论 #5 — ROCmSupport (2021-02-18T05:48:31Z)

Latest update:
I have assigned to OpenCL compiler team and he will start looking into it.
I will keep you posting.
Thank you.

---

### 评论 #6 — develancer (2021-03-08T13:06:02Z)

@ROCmSupport Any news on this one?

---

### 评论 #7 — ROCmSupport (2021-03-08T15:21:56Z)

Hi @develancer 
I am working with dev, let me share an update very soon.
Thank you.

---

### 评论 #8 — develancer (2021-03-24T08:28:35Z)

@ROCmSupport Feel free to share an update ;-)

---

### 评论 #9 — develancer (2021-04-13T16:13:42Z)

Hi @ROCmSupport, just wanted to remind you it's been a month since the last update.

---

### 评论 #10 — ROCmSupport (2021-04-16T11:52:12Z)

I pinged developer and waiting for the update
Most probably issue will be fixed in ROCm 4.3.
Thank you.

---

### 评论 #11 — develancer (2021-05-17T12:34:20Z)

Hi @ROCmSupport, another month has passed, so I wonder whether we have any timeframe for this fix?

Just wanted to emphasize that since the compiler generates invalid code in this case, it may as well do so in many different scenarios, most of which may slip undetected in various professional or scientific applications.

---

### 评论 #12 — ROCmSupport (2021-05-31T11:11:36Z)

Hi @develancer 
Most likely it will be fixed with/before ROCm 4.4.

---

### 评论 #13 — develancer (2021-08-18T20:15:49Z)

Hi @ROCmSupport, is the fix still expected to happen with ROCm 4.4, or has the schedule changed?

---

### 评论 #14 — ROCmSupport (2021-08-19T12:48:01Z)

Hi @develancer 
I reached developer on the same and will provide an update asap once I hear from them.
Thank you

---

### 评论 #15 — develancer (2021-09-29T07:43:53Z)

Hi @ROCmSupport, another month has passed — I suspect the developer is on holiday?
My question from 18 Aug is still valid.

---

### 评论 #16 — ROCmSupport (2021-09-29T12:31:28Z)

Hi @develancer 
As per the latest information, fix will be part of 5.0. Thank you.

---

### 评论 #17 — develancer (2021-11-30T16:24:32Z)

@ROCmSupport Do you have any timeframe for the wide availability of ROCm 5.0?

---

### 评论 #18 — ROCmSupport (2021-12-01T09:10:09Z)

I am sure that patches/fixes are ready, let me check with the developer on 5.0 tracker. Thank you.

---

### 评论 #19 — develancer (2021-12-15T13:04:06Z)

@ROCmSupport Hello again! Were you able to check with the developer on this matter?

---

### 评论 #20 — ROCmSupport (2021-12-15T13:47:27Z)

I just pinged the developer, waiting for the response. 

---

### 评论 #21 — develancer (2022-01-03T12:12:21Z)

Happy New Year @ROCmSupport!
We will soon have the anniversary of this bug report.
PS. Still waiting for the ping to return from that developer.

---

### 评论 #22 — ROCmSupport (2022-01-25T10:41:21Z)

Hi @develancer 
Good news. Fix is ready and its part of our internal builds already. ROCm 5.1 will have the fix.
5.1 will be released very soon in next few days and I request to verify once 5.1 is out.
Thank you.

---

### 评论 #23 — develancer (2022-03-11T21:08:09Z)

Hi @ROCmSupport,
Any timeframe for the release of 5.1?

---

### 评论 #24 — ROCmSupport (2022-03-14T08:56:16Z)

Hi @develancer 
Request to wait for a month(approx.).

---

### 评论 #25 — nartmada (2024-01-04T05:52:58Z)

Hi @develancer, apologies for the slow/lack of response :( Can you please check latest ROCm 6.0.0 to confirm the issue is gone?  If  issue is no longer reproducible, please close the ticket.  Thanks.

---

### 评论 #26 — develancer (2024-01-12T13:13:10Z)

Hi @ROCmSupport,
It’s been several years and I don’t have the card anymore.
I switched to NVIDIA and I recommend everyone else to do the same.

---
