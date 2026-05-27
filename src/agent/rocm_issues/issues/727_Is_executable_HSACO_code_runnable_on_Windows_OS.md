# Is executable HSACO code runnable on Windows OS?

> **Issue #727**
> **状态**: closed
> **创建时间**: 2019-03-11T06:20:35Z
> **更新时间**: 2019-03-11T16:22:20Z
> **关闭时间**: 2019-03-11T16:22:20Z
> **作者**: ghostplant
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/727

## 标签

- **Question** (颜色: #cc317c)

## 描述

AMD driver for Windows supports OpenCL 2.1 applications, so I wonder whether HSACO code is compatible bewteen Linux and Windows. Whether it is possible to extract the HSACO code from a Linux ROCm program and import/execute it as an OpenCL kernel code on Windows?

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-11T16:22:20Z)

Hi @ghostplant 

No, HSACO code is not directly compatible with Windows. You could try cracking open the hsaco file (it's basically ELF) and pulling out the kernel descriptor and code. However, I do not personally know:
- If the code you pull out of there will work on the Windows OpenCL runtime
- How you would insert such code into a Windows OpenCL program.

You might try asking the ROCm OpenCL project, but as far as ROCm is concerned, code generated on our runtimes runs on our runtimes.

---
