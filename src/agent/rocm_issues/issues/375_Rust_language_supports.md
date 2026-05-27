# Rust language supports

> **Issue #375**
> **状态**: closed
> **创建时间**: 2018-03-30T04:15:06Z
> **更新时间**: 2023-09-27T16:18:36Z
> **关闭时间**: 2021-01-05T10:17:04Z
> **作者**: ulinlong
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/375

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Is there any posible to publish a rust crate that can be used safely

---

## 评论 (7 条)

### 评论 #1 — Hoeze (2018-10-27T15:45:35Z)

Yes, please!

---

### 评论 #2 — tanekere (2020-01-03T05:38:55Z)

Won't be too hard either. Rust has amazing C FFI and I don't see much c++ here. But I'm still new to ML and I might be wrong but i would love to see a ROCm crate. 

---

### 评论 #3 — dishankjindal1 (2020-05-12T21:02:51Z)

yes please, AMD is making cheap and affordable hardware. And now Apple is moving forward with everything AMD. RCOm make much more sense now.

---

### 评论 #4 — bzm3r (2020-10-29T01:08:12Z)

How easy/difficult is this? What's involved?

---

### 评论 #5 — omac777 (2020-11-19T21:01:01Z)

https://forums.xilinx.com/t5/Xilinx-Xclusive-Blog/AMD-and-Xilinx-Demonstrate-Converged-ROCm-Runtime-Technology/ba-p/1175091

I would love to see ROCm support Rust-lang via some crates that can empower developers to use the CPU, GPU and FPGA to its fullest extent.  There have been efforts to plunk in Rust-lang within GPU kernels, but very limited in terms of capabilities(no looping nor conditionals, no ability to peer-to-peer share data between CPU, GPU, FPGA-NVM-E storage).

Rust-lang could help make all those capabilities safer, easier and ultimately more performant.

---

### 评论 #6 — ROCmSupport (2021-01-05T10:17:04Z)

Hi @ulinlong and all,
Currently we are not supporting rust-lang with ROCm.
Please keep checking our documentation for any changes in future.
Thank you.

---

### 评论 #7 — PTFOPlayer (2023-09-27T16:18:36Z)

Good news everyone, I am working on bindings for Rocm (currently starting with rocm_smi_lib, crate name is the same) for rust.

In future I will also work on hip and other rocm functionalities.

I am also working on making an installer for Rocm, because the current form is annoying 

---
