# 7900 XTX Pytorch Issues

> **Issue #1977**
> **状态**: closed
> **创建时间**: 2023-03-20T17:37:56Z
> **更新时间**: 2024-07-02T19:11:47Z
> **关闭时间**: 2024-07-02T19:11:47Z
> **作者**: tedtroxell
> **标签**: application:pytorch
> **URL**: https://github.com/ROCm/ROCm/issues/1977

## 标签

- **application:pytorch** (颜色: #bfdadc)

## 描述

Like a few others who have posted here I have a 7900 XTX, which isn't officially supported by the ROCm stack. I've looked on line, but I haven't found any information on when to expect support for that device. I'm currently using PyTorch and although I can install torch so it recognizes that there is a GPU, it segfaults whenever a tensor is placed onto the gpu similar to the issue submitted [here](https://github.com/RadeonOpenCompute/ROCm/issues/1973).

I find it disappointing that the 7900 XTX was released 3 months ago and 3 versions of ROCm 5.4.x have been released without support for this.

Is there any reasonably stable way to get pytorch to run on a 7900 XTX? If not, how long are we expected to wait to be able to do so?



---

## 评论 (12 条)

### 评论 #1 — KylinC (2023-03-21T01:13:17Z)

I went to the same situation, but I can put the tensor on RX7900xtx, but segment fault when I operated it (add, multiply). I tried to build a docker, or build pytorch from source, but all crashed.


---

### 评论 #2 — littlewu2508 (2023-03-23T07:49:56Z)

There are some discussions in https://github.com/RadeonOpenCompute/ROCm/issues/1880, including trying pytorch

---

### 评论 #3 — hongxiayang (2023-12-04T19:01:24Z)

@tedtroxell Please check below documentation about how to install pytorch/ROCm on 7900XTX.

https://rocm.docs.amd.com/projects/radeon/en/latest/index.html

https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/install-pytorch.html



---

### 评论 #4 — briansp2020 (2023-12-04T19:13:14Z)

@hongxiayang 
What is the difference in installing ROCm using
1. https://repo.radeon.com/amdgpu-install/23.20.00.48/ubuntu/jammy/amdgpu-install_5.7.00.48.50700-1_all.deb 
2. https://repo.radeon.com/amdgpu-install/5.7/ubuntu/jammy/amdgpu-install_5.7.50700-1_all.deb
3. https://rocm.docs.amd.com/en/latest/deploy/linux/quick_start.html
Not sure why there are 2 different amdgpu-install script with different version number.


---

### 评论 #5 — hongxiayang (2023-12-05T20:45:28Z)

Please use 1) instead of 2) for your case because of the first one has the power management fix.


---

### 评论 #6 — briansp2020 (2023-12-06T04:49:22Z)

@hongxiayang
If amdgpu-install_5.7.00.48.50700-1_all.deb has more fixes, does it mean that [amdgpu-install_5.7.50702-1_all.deb](https://repo.radeon.com/amdgpu-install/5.7.2/ubuntu/jammy/amdgpu-install_5.7.50702-1_all.deb), which was released later, have the fix as well?

Anyway, my question is not which one to use. But why have two different version number schemes 23.20.00.48 and 5.7? It just seems confusing for no good reason.

---

### 评论 #7 — hongxiayang (2023-12-06T13:25:02Z)

cc @saadrahim 

---

### 评论 #8 — hongxiayang (2023-12-06T13:37:25Z)

Hi, @briansp2020: sorry for if that caused confusion.   I saw that 1) is mentioned in below steps in the documentation. Is there some place in the documentation that mentioned 2)?  
![image](https://github.com/RadeonOpenCompute/ROCm/assets/62075498/ed9958a8-4e3f-468d-bdb0-057655a53e2c)


---

### 评论 #9 — briansp2020 (2023-12-06T14:37:24Z)

https://rocm.docs.amd.com/en/latest/deploy/linux/installer/install.html

5.7.1 is the official version number scheme that ROCm has been using as long as I've been following ROCm development and I've been following it ever since 1.0 was released. I saw 23.20.00.02 a few weeks ago on Twitter when support for 7900XTX was announced. Though I know now where it came from (it is the version number scheme the graphics driver team uses, right?), it was very confusing when I first saw it (https://twitter.com/briansp2020/status/1714068351176020310), and felt that it was unnecessary and showed a lack of planning and communication within AMD about how to bring ROCm to consumer products. I'm pretty sure most people who have been following ROCm development for more than a year are more familiar with the 5.7.1 format and would be confused by the 23.20.00.02 scheme.
Anyway, I think AMD needs 1 version number scheme that rules them all or, at least, should communicate clearly that there is a ROCm distribution version number and a graphics driver version number and how they relate to each other. Or maybe the ROCm distribution version should be treated separately as has been the case so far and only mention the 23.20... as the version number of the script that installs ROCm components that match the driver distribution.
just my 2c

---

### 评论 #10 — briansp2020 (2023-12-06T14:59:00Z)

https://repo.radeon.com/amdgpu-install/

I see that both version number's been in use for a while.  I think AMD should
1. stick to ROCm version number only
or
1. release 1 script with both ROCm and driver version number. 
2. clearly indicate that ROCm version number and GPU driver version numbers are two different things and how they should always go together.

NVidia has a separate driver version number and CUDA version number as well. but they don't use the driver version when talking CUDA and they don't talk CUDA version number when talking about driver release. The twit I saw was talking about a ROCm release but mentioned the driver version, which is why I got confused. So, I think this is more of a communication/documentation issue than anything else.


---

### 评论 #11 — ppanchad-amd (2024-05-10T18:32:00Z)

@tedtroxell Can you please test with latest ROCm 6.1.1? If resolved, please close the ticket. Thanks!

---

### 评论 #12 — ppanchad-amd (2024-07-02T19:11:47Z)

@tedtroxell Closing ticket. Please re-open if you still see the same issue with the latest ROCm 6.1.2 Thanks!

---
