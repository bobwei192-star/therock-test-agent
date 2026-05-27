# Can't use ROCm without root privilege. With root, GPU fan spins very fast and only normalizes with a complete shutdown

> **Issue #810**
> **状态**: closed
> **创建时间**: 2019-06-04T01:09:05Z
> **更新时间**: 2019-06-05T02:04:18Z
> **关闭时间**: 2019-06-05T02:04:18Z
> **作者**: o-alquimista
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/810

## 描述

Applications run as normal user cannot detect `amdocl64` and make use of my GPU. Running them as root allows them to use the GPU, but introduces a problem with the GPU fan. It starts spinning unusually fast and do not stop until a reboot is performed.

[See this issue](https://github.com/hashcat/hashcat/issues/2050). I am running Ubuntu 18.04.2 with an AMD RX 560 4GB graphics device.

My user is part of the **video** group. I have followed [these instructions](https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository) precisely.

---

## 评论 (1 条)

### 评论 #1 — o-alquimista (2019-06-05T02:04:18Z)

The problem seems to be solved with a newer version of Hashcat. Closing.

---
