# OpenCL freezes on second GPU

> **Issue #1480**
> **状态**: closed
> **创建时间**: 2021-05-24T22:51:49Z
> **更新时间**: 2021-06-09T20:41:38Z
> **关闭时间**: 2021-06-01T12:01:24Z
> **作者**: ivanmlerner
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1480

## 描述

Hello, I have two RX5500 and opencl seems to hang/freeze when using the second motherboard slot.
Even clinfo freezes when getting information from the second gpu. I have swapped the cards and the issue remains. Both cards are detected properly by opencl, both are run by the processor in this motherboard, and the power supply has plenty of power for both cards. I am running arch linux and I know the distribution and cards are not officially supported, but I'd greatly appreciate some help with this issue.

---

## 评论 (14 条)

### 评论 #1 — preda (2021-05-25T19:25:48Z)

If you do a "sudo dmesg" after the freeze, do you see anything interesting towards the end of it?


---

### 评论 #2 — ivanmlerner (2021-05-25T20:30:05Z)

I do, here is the output:

[dmesg_output.txt](https://github.com/RadeonOpenCompute/ROCm/files/6542190/dmesg_output.txt)


---

### 评论 #3 — ThomasA (2021-05-31T14:16:54Z)

I am experiencing issues that sound very similar to this on 2 Instinct MI100 GPUs.

---

### 评论 #4 — ROCmSupport (2021-06-01T12:00:39Z)

Hi @ivanmlerner 
Thanks for reaching out.
We are not officially supporting Navi series of cards right now and also arch linux. So can not share official help.
Am closing this right away.

But have few suggestions and try to help.
Can you please pull out card first card(so called working card) and try to boot with one card only(card in second slot) and update.
Thank you.

---

### 评论 #5 — ivanmlerner (2021-06-01T23:51:33Z)

Hello, I understand, thanks a lot to try and help help me.
I did as instructed and the computer booted properly. OpenCL was also working normally without any output to dmesg.

---

### 评论 #6 — ROCmSupport (2021-06-02T04:10:20Z)

Thanks.
So request you to do the below experiments for better understating of the problem.
1. Keeping one card in first slot only --> clinfo output and dmesg
2. Keeping one card in second slot only --> You already shared info that it working. clinfo output and dmesg needed
3. Keeping one card in first slot and one card in second slot --> clinfo output and dmesg

Thank you.


---

### 评论 #7 — ivanmlerner (2021-06-02T22:02:40Z)

Hello, I did as instructed and here are the outputs:

[dmesg_output_both.txt](https://github.com/RadeonOpenCompute/ROCm/files/6587616/dmesg_output_both.txt)
[clinfo_output_both.txt](https://github.com/RadeonOpenCompute/ROCm/files/6587615/clinfo_output_both.txt)
[dmesg_output_first_only.txt](https://github.com/RadeonOpenCompute/ROCm/files/6587617/dmesg_output_first_only.txt)
[clinfo_output_first_only.txt](https://github.com/RadeonOpenCompute/ROCm/files/6587618/clinfo_output_first_only.txt)
[dmesg_output_second_only.txt](https://github.com/RadeonOpenCompute/ROCm/files/6587619/dmesg_output_second_only.txt)
[clinfo_output_second_only.txt](https://github.com/RadeonOpenCompute/ROCm/files/6587620/clinfo_output_second_only.txt)


---

### 评论 #8 — ROCmSupport (2021-06-03T04:37:51Z)

Hi @ivanmlerner 
No useful information captured from dmesg in single GPU cases.
But in 2 GPU case, IO_PAGE_FAULTs observed and looks like this is related to amdgpu basedriver. Anyway, I am trying to get more information.
clinfo outputs are similar in all cases and clinfo output is not complete, means clinfo did not run completely(Might be due to the non-support of ROCm right now).

---

### 评论 #9 — ROCmSupport (2021-06-03T10:56:40Z)

More update:
I can confirm that issue is caused by amdgpu, I decoded and found further that's the module that threw it. 
But as the issue is related to amdgpu/ROCm, I can not help further as we are not supporting this card officially.
Hope you got it.
Thank you.

---

### 评论 #10 — ivanmlerner (2021-06-03T18:35:34Z)

Thanks a lot for the effort, I do get it. 
Does that mean I need to look for amdgpu support or just wait until the card becomes supported?

---

### 评论 #11 — ROCmSupport (2021-06-04T01:50:17Z)

Hi @ivanmlerner 
Its your call, I can not comment on this :).

---

### 评论 #12 — ivanmlerner (2021-06-08T03:57:06Z)

Hello, I have managed to get it to work. Disabling IOMMU in the BIOS solved the issue.

---

### 评论 #13 — ROCmSupport (2021-06-08T07:35:46Z)

Good to know that IOMMU solves the issue.Thank you.

---

### 评论 #14 — ekondis (2021-06-09T20:41:38Z)

> Hello, I have managed to get it to work. Disabling IOMMU in the BIOS solved the issue.

I faced the same problem (see [issue 1429](https://github.com/RadeonOpenCompute/ROCm/issues/1429)), with different GPU configuration, but the workaround actually worked! Thank you, @ivanmlerner!

---
