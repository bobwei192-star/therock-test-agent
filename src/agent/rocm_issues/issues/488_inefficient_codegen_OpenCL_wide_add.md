# inefficient codegen: OpenCL wide add

> **Issue #488**
> **状态**: closed
> **创建时间**: 2018-08-02T12:09:14Z
> **更新时间**: 2023-12-18T18:41:44Z
> **关闭时间**: 2023-12-18T18:41:43Z
> **作者**: preda
> **标签**: Under Investigation, Compiler Performance Issue
> **URL**: https://github.com/ROCm/ROCm/issues/488

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Compiler Performance Issue** (颜色: #8ff442)

## 描述

This is a 3-word-wide add-with-carry in OpenCL:
```
uint3 add(uint3 a, uint3 b) {
  ulong x = a.x + (ulong) b.x;
  ulong y = a.y + (ulong) b.y + (x >> 32);
  uint  z = a.z + b.z + (y >> 32);
  return (uint3) (x, y, z);
}
```
This code can be compiled to 3 v_add instructions (with carry-in/carry-out as appropriate). But this is what is generated:
```
	v_add_co_u32_e32 v2, vcc, v7, v4                           // 000000003D74: 32040907
	v_addc_co_u32_e64 v0, s[0:1], 0, 0, vcc                    // 000000003D78: D11C0000 01A90080
	s_waitcnt vmcnt(1)                                         // 000000003D80: BF8C0F71
	v_add_co_u32_e32 v3, vcc, v8, v5                           // 000000003D84: 32060B08
	v_addc_co_u32_e64 v5, s[0:1], 0, 0, vcc                    // 000000003D88: D11C0005 01A90080
	v_add_co_u32_e32 v3, vcc, v3, v0                           // 000000003D90: 32060103
	v_addc_co_u32_e32 v0, vcc, 0, v5, vcc                      // 000000003D94: 38000A80
	v_add_u32_e32 v4, v9, v6                                   // 000000003D98: 68080D09
	v_add_u32_e32 v4, v4, v0
```
Which is 8 adds.

Apparently the compiler does not understand the carry expressed in OpenCL as widening add.

Below is the expected ISA snippet:
```
	v_add_co_u32_e32 v2, vcc, v4, v7                           // 000000003D74: 32040F04
	v_addc_co_u32_e32 v3, vcc, v5, v8, vcc                     // 000000003D78: 38061105
	v_addc_co_u32_e32 v4, vcc, v6, v9, vcc                     // 000000003D7C: 38081306
```

---

## 评论 (8 条)

### 评论 #1 — gstoner (2018-08-02T12:35:21Z)

Can you send me email.

Get Outlook for iOS<https://aka.ms/o0ukef>

________________________________
From: Mihai Preda <notifications@github.com>
Sent: Thursday, August 2, 2018 7:09 AM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: [RadeonOpenCompute/ROCm] inefficient codegen: OpenCL wide add (#488)


This is a 3-word-wide add-with-carry in OpenCL:

uint3 add(uint3 a, uint3 b) {
  ulong x = a.x + (ulong) b.x;
  ulong y = a.y + (ulong) b.y + (x >> 32);
  uint  z = a.z + b.z + (y >> 32);
  return (uint3) (x, y, z);
}


This code can be compiled to 3 v_add instructions (with carry-in/carry-out as appropriate). But this is what is generated:

        v_add_co_u32_e32 v2, vcc, v7, v4                           // 000000003D74: 32040907
        v_addc_co_u32_e64 v0, s[0:1], 0, 0, vcc                    // 000000003D78: D11C0000 01A90080
        s_waitcnt vmcnt(1)                                         // 000000003D80: BF8C0F71
        v_add_co_u32_e32 v3, vcc, v8, v5                           // 000000003D84: 32060B08
        v_addc_co_u32_e64 v5, s[0:1], 0, 0, vcc                    // 000000003D88: D11C0005 01A90080
        v_add_co_u32_e32 v3, vcc, v3, v0                           // 000000003D90: 32060103
        v_addc_co_u32_e32 v0, vcc, 0, v5, vcc                      // 000000003D94: 38000A80
        v_add_u32_e32 v4, v9, v6                                   // 000000003D98: 68080D09
        v_add_u32_e32 v4, v4, v0


Which is 8 adds.

Apparently the compiler does not understand the carry expressed in OpenCL as widening add.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/488>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuV5VPNJmQcFSQhiFaX6DK5le8D_Aks5uMuvsgaJpZM4VsKaS>.


---

### 评论 #2 — b-sumner (2018-08-02T14:24:56Z)

Thanks.  We'll look into this.

---

### 评论 #3 — preda (2018-08-03T07:31:06Z)

@gstoner : my email is mhpreda@gmail.com

---

### 评论 #4 — foobar2019 (2019-01-20T20:25:21Z)

This seems like llvm backend trouble. Another repro on stock driver:

![image](https://user-images.githubusercontent.com/46652535/51444604-d22b5380-1cf9-11e9-9c85-a3499fefb334.png)

(should be just single add, followed by 7 addc)

---

### 评论 #5 — ROCmSupport (2021-01-07T07:27:10Z)

Hi @preda
Thanks for reaching out.
Can you please verify with the latest ROCm 4.0 and update the status asap.
Thank you.

---

### 评论 #6 — arsenm (2022-12-29T21:27:31Z)

Some work is in flight to address this https://reviews.llvm.org/D138814

---

### 评论 #7 — tasso (2023-12-11T17:06:37Z)

Has this issue been fixed? If so, can we please close it?

---

### 评论 #8 — tasso (2023-12-18T18:41:43Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the last request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
