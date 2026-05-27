# Docker pulls the ROSM mirror and reports an error

> **Issue #1522**
> **状态**: closed
> **创建时间**: 2021-07-14T06:34:13Z
> **更新时间**: 2021-07-15T13:41:53Z
> **关闭时间**: 2021-07-15T13:41:41Z
> **作者**: gp1322719830
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1522

## 描述

Docker pulls the ROSM mirror to report the following error：
docker: unknown server OS: .

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-07-14T07:15:17Z)

Hi @gp1322719830 
Thanks for reaching out.
For better understanding of problem, can you please share the steps you followed.
Please share all steps to reproduce the problem.
Thank you.

---

### 评论 #2 — gp1322719830 (2021-07-14T07:51:33Z)

> Hi @gp1322719830
> Thanks for reaching out.
> For better understanding of problem, can you please share the steps you followed.
> Please share all steps to reproduce the problem.
> Thank you.

sudo docker pull rocm/tensorflow:latest
sudo docker run -it -v $HOME:/data --privileged --rm --device=/dev/kfd --device=/dev/dri --group-add video rocm/tensorflow:latest 

error:
docker: unknown server OS: .

---

### 评论 #3 — ROCmSupport (2021-07-14T09:27:22Z)

Hi @gp1322719830
I am not able to reproduce this problem.
I have a Ubuntu 20.04.2 machine with Vega10 card in it.
I just did sudo docker run -it -v $HOME:/data --privileged --rm --device=/dev/kfd --device=/dev/dri --group-add video rocm/tensorflow:latest and docker image was pulled.

Digest: sha256:dcd14d6f1c3328eb90a0c1dd71b1693e6a98b68b6597617b88c0af3acabea91d
Status: Downloaded newer image for rocm/tensorflow:latest
root@2baf14b37d2a:/root#

Looks like its the problem with your machine and I guess issue is specific to this kernel. Can you please try on a different machine and a different kernel and update.
Thank you.

---

### 评论 #4 — gp1322719830 (2021-07-15T13:41:53Z)

Solved,thanks!

---
