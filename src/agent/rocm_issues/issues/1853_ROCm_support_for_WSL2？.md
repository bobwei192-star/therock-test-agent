# ROCm support for WSL2？

> **Issue #1853**
> **状态**: closed
> **创建时间**: 2022-11-03T09:51:26Z
> **更新时间**: 2025-06-09T16:02:55Z
> **关闭时间**: 2024-07-12T13:16:52Z
> **作者**: bf109f4
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1853

## 描述

MIcrosoft only provide a few  kernels of the operate systems for wsl2. Will you consider to support wsl2 in following updates?

---

## 评论 (13 条)

### 评论 #1 — Bejadin (2023-07-29T12:22:09Z)

估计得先支持windows，后面才会考虑wsl

---

### 评论 #2 — abhimeda (2024-01-30T04:03:10Z)

@bf109f4  Hi, is this resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #3 — phubner (2024-02-28T04:12:23Z)

I have been running into dkms errors on WSL2 ubuntu 22.04.04. So I would say this is still not resolved.

I commented on  #2933 about it.

After running `sudo amdgpu-install --usecase=rocm -y` I get `WARNING: amdgpu dkms failed for running kernel`

```
uname -m && cat /etc/*release
x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.4 LTS"
PRETTY_NAME="Ubuntu 22.04.4 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```


---

### 评论 #4 — Headcrabed (2024-03-30T14:02:57Z)

Seems amd is working on that wsl2 support now. In rocm 6.0.6 installer, there is a usecase option for wsl2, but I haven't tried that yet.

---

### 评论 #5 — ColorfulRhino (2024-03-30T14:29:21Z)

> Seems amd is working on that wsl2 support now. In rocm 6.0.6 installer, there is a usecase option for wsl2, but I haven't tried that yet.

Finally! Let's hope this will actually work in the not too distant future.

---

### 评论 #6 — fermathamilton (2024-04-12T01:07:51Z)

Hi,

I am running into this same issue. This is my GPU model.

![image](https://github.com/ROCm/ROCm/assets/165560138/0a273ac5-4352-42df-b702-4da6deb45ac5)

Any idea when version 6.0.6 will be available? 

![image](https://github.com/ROCm/ROCm/assets/165560138/01daf9bf-3267-44a0-ac0a-2852d97ac739)

Thank you in advance!

---

### 评论 #7 — gabemorris12 (2024-04-23T22:38:34Z)

> Seems amd is working on that wsl2 support now. In rocm 6.0.6 installer, there is a usecase option for wsl2, but I haven't tried that yet.

I'm not seeing a 6.0.6 version on the site. It goes from 6.0.2 to 6.1.

<img width="1804" alt="image" src="https://github.com/ROCm/ROCm/assets/73252281/2b714151-f774-4ebd-a24f-380571b5e718">


---

### 评论 #8 — Headcrabed (2024-06-21T06:30:59Z)

https://community.amd.com/t5/ai/new-amd-rocm-6-1-software-for-radeon-release-offers-more-choices/ba-p/688840
So WSL support would be ready at rocm 6.1.3

---

### 评论 #9 — ColorfulRhino (2024-06-21T11:21:48Z)

> https://community.amd.com/t5/ai/new-amd-rocm-6-1-software-for-radeon-release-offers-more-choices/ba-p/688840 So WSL support would be ready at rocm 6.1.3

That would be wesome if it works!

---

### 评论 #10 — Headcrabed (2024-06-21T14:22:52Z)

More information here: https://gist.github.com/tonykero/8ceb62868378ee11e36b07f975731d26?permalink_comment_id=5095961#gistcomment-5095961


---

### 评论 #11 — harkgill-amd (2024-07-11T18:49:11Z)

Hi @bf109f4, the beta release for WSL with ROCm is now out. Please see [Install Radeon Software for WSL with ROCm](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html) for more information. Can we close out this ticket?

---

### 评论 #12 — bf109f4 (2024-07-11T23:17:47Z)

sure。please turn it out



---Original---
From: ***@***.***&gt;
Date: Fri, Jul 12, 2024 02:49 AM
To: ***@***.***&gt;;
Cc: ***@***.******@***.***&gt;;
Subject: Re: [ROCm/ROCm] ROCm support for WSL2？ (Issue #1853)




 
Hi @bf109f4, the beta release for WSL with ROCm is now out. Please see Install Radeon Software for WSL with ROCm for more information. Can we close out this ticket?
 
—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you were mentioned.Message ID: ***@***.***&gt;

---

### 评论 #13 — Headcrabed (2025-06-09T16:02:54Z)

Btw currently all RDNA4 cards+NAVI31/32 RDNA3 cards are supported by WSL2 now: https://rocm.docs.amd.com/projects/radeon/en/latest/docs/compatibility/wsl/wsl_compatibility.html

---
