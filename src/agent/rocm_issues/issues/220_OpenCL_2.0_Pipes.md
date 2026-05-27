# OpenCL 2.0 Pipes ?

> **Issue #220**
> **状态**: closed
> **创建时间**: 2017-09-30T12:53:47Z
> **更新时间**: 2019-02-08T17:12:46Z
> **关闭时间**: 2019-02-08T17:12:46Z
> **作者**: boxerab
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/220

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Does ROCm have a pipe implementation? Or an ETA for when it will be implemented ?

Thanks!

---

## 评论 (16 条)

### 评论 #1 — gstoner (2017-09-30T14:09:22Z)

PIPE and DeviceEnqueue are not implemented in the current version OpenCL  In Nov we have. OpenCL 2.1 support with both features



---

### 评论 #2 — boxerab (2017-09-30T20:52:19Z)

Great, looking forward to 2.1 support.  I'm curious about how pipes are going to be implemented. 
I have a large kernel with two complex pieces that could be separated by pipes into two different kernels.
But, I need to understand the overhead involved in using pipes over regular buffers.

Could I use a pipe in the inner loop of a kernel, and get decent performance? 

Actually, I want to use two pipes : kernel 1 writes a byte to pipe1, and then waits for kernel 2 to process 
the byte and send another back in pipe 2.

If the kernels are running concurrently, and the bytes are cached rather than written to global memory,
I am hoping that performance could be good.





---

### 评论 #3 — ekondis (2017-10-01T06:47:50Z)

@gstoner It's great to hear that OpenCL 2.1 will be supported! Does this imply also SPIR-V kernel consumption?

@boxerab This sounds having very tightly dependent kernels. I wouldn't expect this configuration to exhibit high performance.

---

### 评论 #4 — nevion (2017-10-01T07:31:28Z)

@ekondis Tightly dependent kernels is the raison d'etre of pipes!  Cuts  host communication out of the loop and allows for multi-stage kernels which allows them to optimize away re-reading of global memory/inputs as the phases of the kernel change... kind of difficult to explain because some of this are higher level changes you may not immediately expect with the tool but it's really interesting what it enables if it works right.

---

### 评论 #5 — boxerab (2017-10-01T12:49:53Z)

Thanks guys. So, yes, my question can be rephrased as: can two tightly coupled kernels use pipes to communicate and still get good performance?  My feeling is that is won't be possible, but hoping to be surprised! 

---

### 评论 #6 — gstoner (2017-10-01T14:28:46Z)

The current pipes spec is not optimal. There are strong opinion in my team it should have been left out of the 2.0 spec until they invested more time to get it correct. FPGA venders needed it

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Aaron Boxer <notifications@github.com>
Sent: Sunday, October 1, 2017 7:49:54 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] OpenCL 2.0 Pipes ? (#220)


Thanks guys. So, yes, my question can be rephrased as: can two tightly coupled kernels use pipes to communicate and still get good performance? My feeling is that is won't be possible, but hoping to be surprised!

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/220#issuecomment-333374471>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuY2nuuDHvencuVYWBiRQf9eN6JlLks5sn4pygaJpZM4PpjQg>.


---

### 评论 #7 — nevion (2017-10-01T14:54:18Z)

@gstoner Is there anything you can identify as what was lacking or what should've been left out?  It is clear it came out need to unify altera's and xillinx's proprietary pipes implementation (and the ubiquity of pipes in general on that arch) but I've never heard from the GPU side why those same concepts and framework didn't translate well to GPU land.

---

### 评论 #8 — oscarbg (2017-10-09T15:02:51Z)

@gstoner so you know if Windows OpenCL driver will get OpenCL 2.1 support in Nov too?
I say because preview drivers from new 17.40 branch are avaiable for Windows Insider and seems OpenCL 2.0 still?

---

### 评论 #9 — gstoner (2017-10-09T15:36:09Z)

17.40 will not support OpenCl 2.1 

---

### 评论 #10 — oscarbg (2017-10-09T16:45:27Z)

thanks.. then what branch we are talking about? 17.50 by end of year? or Windows will has no plans for 2.1 this year?


---

### 评论 #11 — gstoner (2017-11-13T14:45:22Z)

@boxerab Pipes did not make it into the OpenCL release for 1.7 I working with the Dev to get it back on track few other projects sidetracked this feature 

---

### 评论 #12 — oscarbg (2017-11-14T00:38:17Z)

and OpenCL 2.0 feature: enqueue_kernel? it's in 1.7?

---

### 评论 #13 — boxerab (2017-11-14T01:27:06Z)

@gstoner thanks for the update. Looking forward to 1.7

---

### 评论 #14 — oscarbg (2018-04-11T03:49:12Z)

@boxerab seeing you closed the issue is full OpenCL 2.0 done on ROCM driver right now?
sorry for asking again but OpenCL 2.0 enqueue_kernel is also done? 

---

### 评论 #15 — boxerab (2018-04-11T11:32:41Z)

Just got tired of waiting :) Will re-open.

---

### 评论 #16 — jlgreathouse (2019-02-08T17:12:46Z)

Hi @boxerab 

Pipes and device enqueue should work as of ROCm 2.0, depending on which GPU you have.

---
