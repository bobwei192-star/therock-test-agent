# Feature request: list all supported AMD video cards.

> **Issue #1700**
> **状态**: closed
> **创建时间**: 2022-03-07T11:34:17Z
> **更新时间**: 2022-03-08T20:19:33Z
> **关闭时间**: 2022-03-08T20:19:33Z
> **作者**: NeilduToit13
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1700

## 描述

Per this recent issue: https://github.com/RadeonOpenCompute/ROCm/issues/1683

It "would've been nice to just have a list of all AMD video cards that are currently supported."
This issue was closed after the following link was posted: https://docs.amd.com/bundle/Hardware_and_Software_Reference_Guide/page/Hardware_and_Software_Support.html

I do not understand why this resulted in the issue being closed given that the provided link does not include a _list of all supported AMD video cards_. What is provides is a short list of categories of video cards with one or maybe two examples of each. I don't know what a "Polaris 12" is, and a Google search doesn't reveal a list of "Polaris 12" chips either.

I've spend three days now going through the confusing tangle of documentation on supported hardware and I'm still coming up short. I am going to be buying a new PC tomorrow, I am going to be using it for GPU programming, and I would love to support the open source ROCm instead of Nvidea's proprietary software. But I'm finding it literally impossible to find a card I can buy that I know will support ROCm. Is ROCm intended to be used by consumers at all? Or is this just a data warehouse technology?

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2022-03-07T12:44:02Z)

Hi @NeilduToit13 
Thanks for reaching out.
What I understood is you are looking for each supported card name with 2 examples(with marketing names).
Let me talk to our documentation team on this.
Thank you.


---

### 评论 #2 — Rmalavally (2022-03-07T22:34:40Z)

Hi @NeilduToit13 Please refer to our release notes document for each release. The latest ROCm release v5.0.2 has a list of supported GPUs as of this release. 

Let us know if you cannot find the information you need, and we will work with the BU to provide more details.

AMD ROCm Documentation Team

---

### 评论 #3 — ye-luo (2022-03-07T23:05:08Z)

> The latest ROCm release v5.0.2 has a list of supported GPUs as of this release.

@Rmalavally Prove it. Provide a link if you think it is in the v5.0.2 documentation. 

I didn't have the luck to find such info in the v5.0.2 doc. Instead, v5.0.0 doc does carry a list of GPUs.
Look at https://docs.amd.com/bundle/ROCm_Release_Notes_v5.0/page/About_This_Document.html
![Screenshot from 2022-03-07 16-56-29](https://user-images.githubusercontent.com/1454251/157132382-b6b50935-7273-4a12-8de5-13b7e22682ef.png)
There is no mention of Vega 10.

Look at this
https://docs.amd.com/bundle/Hardware_and_Software_Reference_Guide/page/Hardware_and_Software_Support.html
![Screenshot from 2022-03-07 16-56-57](https://user-images.githubusercontent.com/1454251/157132287-d3e98b16-6e96-45b0-9644-192c518a6160.png)
shown updated today. Still list Vega 10.

Clean this up!




---

### 评论 #4 — Rmalavally (2022-03-08T00:20:49Z)

@ye-luo Thank you for your note. I meant the ROCm Installation Guide v5.0.2. My mistake. 

https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.0.2/page/Prerequisite_Actions.html

ROCm v5.0.2 is a point/patch release, so the Release Notes document consists of specific fixed defects or known issues. If a release has an accompanying Installation Guide, we recommend you refer to this document for details on supported GPUs and other installation-related details.

As always, you can reach out to the ROCm Documentation team if you need more information.

AMD Documentation Team

---

### 评论 #5 — ROCmSupport (2022-03-08T07:36:43Z)

I hope @ye-luo is looking for all list of supported cards(with marketing names) for every Asic family.
@Rmalavally can you please check whether its possible to share this information in our docs.

---

### 评论 #6 — ye-luo (2022-03-08T15:53:44Z)

@ROCmSupport better ask what @NeilduToit13 wants about card details. I was looking for a link which @Rmalavally has already gave and also wanted to point out the discrepancy in the docs about Vega10.

---

### 评论 #7 — NeilduToit13 (2022-03-08T20:19:28Z)

Based on the last link shared, it does look like I'm in the wrong place. None of those cards appear to be consumer-grade cards. So I guess you can close the issue.

---
