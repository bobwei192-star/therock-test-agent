# Planned future hardware support W6600 (Navi 23)?

> **Issue #1694**
> **状态**: closed
> **创建时间**: 2022-02-27T19:28:48Z
> **更新时间**: 2024-04-06T00:35:01Z
> **关闭时间**: 2024-04-06T00:35:01Z
> **作者**: ddkn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1694

## 描述

As per comment https://github.com/RadeonOpenCompute/ROCm/issues/1617#issuecomment-1049297130 to ensure there is separate issues for each family of GPU's. Is there support or any plans to add the W6600 (Navi 23) GPUs to the ROCm 5.x line?

If not, is there a more decisive list of GPU's that are compatible with ROCm 5.x? As it seems many cards available are the RDNA2 and RDNA1 cards available on the market.

---

## 评论 (10 条)

### 评论 #1 — ROCmSupport (2022-03-03T10:54:10Z)

Hi @ddkn 
Thanks for reaching out.
Currently we are not supporting Navi23 right now for ROCm.
Anyhow, I will talk to product team on this and get some update once.
Thank you.


---

### 评论 #2 — ddkn (2022-03-07T01:38:30Z)

Hi @ROCmSupport,

Thanks for getting back to me. It would be nice to support the new Pro cards, as I have interest in using PyTorch, and/or C++ with the card. Having something that isn't perfectly high end but useful on a budget is nice like the W6600.

Looking forward to hearing what people have to say!

---

### 评论 #3 — pioto1225 (2022-06-10T05:10:58Z)

Hi @ROCmSupport 

Are there any updates on this? I recently bought RX 6600 XT and the tensorflow does not work.
The lack of compute support and missing roadmap seem to be the biggest pain points on otherwise impressive RDNA class hardware.

Best regards,
Piotr

---

### 评论 #4 — langyuxf (2022-06-22T06:43:16Z)

@ddkn You can refer to https://github.com/RadeonOpenCompute/ROCm/issues/1756 

---

### 评论 #5 — m-reuter (2022-09-19T14:16:12Z)

I would also like to hear about any updates. We develop neural networks in pytorch for medical image analysis with users around the world. We would love to also support AMD cards (of course Nvidia and now also already Apple silicon GPUs are working nicely). We have a W6600 for development and testing, but cannot use it due to missing ROCm support. Thanks for any efforts in this direction.

---

### 评论 #6 — langyuxf (2022-09-20T00:52:30Z)

@m-reuter https://github.com/RadeonOpenCompute/ROCm/issues/1756

---

### 评论 #7 — m-reuter (2022-09-20T06:45:13Z)

@xfyucg thanks, I realised too late that that also includes the W6600. However I am on Ubuntu 20.4 with a 5.14 kernel where install fails. Will open another issue for that. 

---

### 评论 #8 — brewfalconenterprises (2023-02-26T20:13:31Z)

After much trial-and-error and following similar threads, here's the cocktail that I finally got to work on Ubuntu 22.04 bare metal with Navi23 (6600XT). (Both PyTorch and Tensorflow from the command line)

    ROCm 5.4.2
    Python 3.9 (may need to separately install distutils)
    tensorflow-rocm
    pytorch5.2

Environment variables:

    PYTHONPATH=/usr/bin/python3.9
    ROCM_PATH=/opt/rocm
    HSA_OVERRIDE_GFX_VERSION=10.3.0


---

### 评论 #9 — abhimeda (2024-01-23T19:54:59Z)

@ddkn Hi, is your issue resolved on the latest ROCm? Can we close this ticket?


---

### 评论 #10 — nartmada (2024-04-06T00:35:01Z)

Apologies for not following up.  

W6600 is not supported officially but @brewfalconenterprises has provided a workaround.
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html

Closing the ticket for now.

---
