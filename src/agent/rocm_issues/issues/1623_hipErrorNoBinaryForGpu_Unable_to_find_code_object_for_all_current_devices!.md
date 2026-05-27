# hipErrorNoBinaryForGpu: Unable to find code object for all current devices!

> **Issue #1623**
> **状态**: closed
> **创建时间**: 2021-11-22T19:57:24Z
> **更新时间**: 2024-03-11T13:41:15Z
> **关闭时间**: 2021-11-23T04:54:26Z
> **作者**: rdgarce
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1623

## 描述

Hi, I have installed tensorflow on ROCm in my Ubuntu 20.04 distro.
I have followed all the step provided in the official ROCm [page](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html).

I also have installed tensorflow-rocm following the guide [here](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html).

I am now trying to execute a very simple python script to test my tensorflow library:
`import tensorflow as tf`
`tf.add(1, 2).numpy()`

but instead of the result I get this error:

> "hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
> Canceled` (core dump created)

My configuration is:
_AMD Ryzen 5 3600
AMD Radeon RX 5600 XT_

Can you help me finding a solution? thanks


---

## 评论 (12 条)

### 评论 #1 — ROCmSupport (2021-11-23T04:54:26Z)

Thanks @rdgarce for reaching out.
I certainly understood the problem.
**hipErrorNoBinaryForGpu** error is thrown when an unsupported device is used. 
As you are using RX 5600 XT(Navi 10 XLE), which is unsupported with ROCm, output is expected.
For supported hardware, please check @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Request to use supported hardware. Feel free to reach me for any other issues.
Thank you.

---

### 评论 #2 — rdgarce (2021-11-23T13:34:55Z)

@ROCmSupport Any roadmap to consult to know if my GPU Will be supported?

---

### 评论 #3 — ROCmSupport (2021-11-24T04:31:44Z)

Hi @rdgarce 
I am not sure about future plans. I request you to keep checking our documentation for the latest updates.
Thank you.

---

### 评论 #4 — FCLC (2021-11-24T20:13:08Z)

> @ROCmSupport Any roadmap to consult to know if my GPU Will be supported?

For now try and keep an eye on #1617, it's where I'm trying to keep most things related to RDNA 1 and RDNA 2 logged. 

@ROCmSupport has graciously acquiesced to keep the issue open until such a time as Navi is fully supported in the ROCm stack. 

As of now, the next release is expected in early Q1 2022, which should bring support for more cards. 

ROCm support can't officially comment on which ones unfortunately, but my personal suspicion is that the rest of RDNA 2 will most likely be supported in the first batch (5.0 and 5.1), and that we may see support for RDNA 1 W/RX 5(7/6)00 series cards in either the second or third point release of ROCm 5. 

Pure speculation, but that seems to be the direction we're heading in. 

Should the above hold true, the 5600xt would receive support around the March-May 2022 timeframe 

---

### 评论 #5 — rdgarce (2021-11-25T08:22:16Z)

Thanks for the detailed explaination @FCLC .
In the meantime, are there any other possibilities to enable me to use tensorflow for deep learning?
I tried to use PlaidML but it works with a very old version of Keras.
Thanks

---

### 评论 #6 — FCLC (2021-11-25T19:09:41Z)

> Thanks for the detailed explaination @FCLC .
> 
> In the meantime, are there any other possibilities to enable me to use tensorflow for deep learning?
> 
> I tried to use PlaidML but it works with a very old version of Keras.
> 
> Thanks

Not certain about the state of the openCL drivers from the amdradeonPro stack, but they in combination with spirv/sycl could be a path worth exploring.

I'm more in the HPC side than ML/ai/DL, apologies for the lack of insight on this precise topic 

---

### 评论 #7 — Atelis (2021-11-27T06:31:46Z)

> Thanks for the detailed explaination @FCLC .
> In the meantime, are there any other possibilities to enable me to use tensorflow for deep learning?
> I tried to use PlaidML but it works with a very old version of Keras.
> Thanks

Hi, on windows you can use tensorflow-directml, i dont have problems on my 5700xt

I have a guide on my site (atelise.com) 

Hope can help 

---

### 评论 #8 — rdgarce (2021-11-27T12:21:12Z)

Hello @Atelis ,
Thanks for your reply.
I already tried tensorflow-directml but the problem is that I need to compile the models without specifing a loss since I'm implementing DDPG algorithm.

This 2.2.4 keras that is shipped with TF 1.15 does not support this feature because it forces me to provide a loss function when compiling models.

If you know a solution let me know :)

---

### 评论 #9 — yacc143 (2023-06-02T17:39:36Z)

> Thanks @rdgarce for reaching out. I certainly understood the problem. **hipErrorNoBinaryForGpu** error is thrown when an unsupported device is used. As you are using RX 5600 XT(Navi 10 XLE), which is unsupported with ROCm, output is expected. For supported hardware, please check @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url) Request to use supported hardware. Feel free to reach me for any other issues. Thank you.

Sorry, this behaviour, "core dump", is not acceptable behaviour, as it also happens for this code:

```
>>> import torch
>>> torch.cuda.is_available()
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
Canceled` (core dump created)
```

Calling torch.cuda.is_available() to check if a supported GPU to decide if the code should fallback to CPU usage is idiomatic
torch usage.

While it might not be very pythonic to just core dump when unsupported hardware is accessed, shrug.

But aborting when the client code tries to figure out if the hardware is available is not OKAY.

---

### 评论 #10 — ximion (2023-07-07T16:19:30Z)

Yes, this behavior is extremely annoying. I have a MI100 and WX 3100 in my system, and simply because the other GPU *exists*, PyTorch and Tensorflow crash the program when I even just try to list the available devices. The devices should instead simply not be listed, if they are not actually available for use.

---

### 评论 #11 — yacc143 (2023-07-09T12:20:49Z)

> Yes, this behavior is extremely annoying. I have a MI100 and WX 3100 in my system, and simply because the other GPU _exists_, PyTorch and Tensorflow crash the program when I even just try to list the available devices. The devices should instead simply not be listed, if they are not actually available for use.

Call it as it is. It's not "extremely annoying" (well it's that too), it's a bug.

Generally speaking, in the Python community, a module that communicates even a fatal error by aborting and not raising a traceback is considered buggy.

And this is clearly not a situation where the hardware locks up, and the process needs to abort to prevent the system from catching fire. This could be trivially handled by a return value, or if AMD thinks they need to break the convention, then fine, go for an exception.

But as is, if you want to handle all cases:

* on Unix, you could THEORETICALLY fork, and check for the GPU in the child process, and take a sudden death to mean the GPU code path has land mines placed there by AMD. (Theoretically, fork & threads are not great companions, and technically, numpy nowadays might start threads up, immediately upon import.)
* on Windows? Hmmm, run an external small script that only checks if the GPU is available? Well, that would also work for Unix, sigh, but it's a workaround of the type that inspires aggressions.

---

### 评论 #12 — atafra (2024-03-11T13:41:14Z)

@ROCmSupport This behaviour is not acceptable even if the GPU isn't supported by ROCm or there are no binaries for the available supported GPUs. Any application must be able to gracefully handle such a situation. Not every application is completely unusable if no supported ROCm devices are available in the system. Currently the application cannot even query the GPU architecture and gracefully fail because this error is thrown at the first HIP call, which is unnecessary. No code execution is attempted, so this error shouldn't be thrown.

---
