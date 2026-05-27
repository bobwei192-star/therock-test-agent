# gpuOwl Fails with Memory Access Fault Error

> **Issue #1020**
> **状态**: closed
> **创建时间**: 2020-02-23T16:26:29Z
> **更新时间**: 2020-03-09T06:52:31Z
> **关闭时间**: 2020-03-09T06:52:31Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1020

## 描述

"Issue: gpuOwL is an OpenCL-based program for testing Mersenne numbers for primality. Currently, running gpuOwl for higher probable prime (PRP) values results in a Memory Access Fault error.

Note, the issue is noticed only when using higher PRP values.

Resolution: As a workaround, you may use lower PRP values."

This Resolution is not valid as PRP values are growing.


---

## 评论 (13 条)

### 评论 #1 — Moading (2020-02-24T13:53:04Z)

Hi,
have you tried to track down the problem with rocr_debug_agent? (https://github.com/ROCm-Developer-Tools/rocr_debug_agent)
I had a memory access fault in my application that I tried to find for months without luck. rocr_debug_agent pointed me to the right location in the code.
You need a Vega GPU, older ASICS are not supported.

---

### 评论 #2 — valeriob01 (2020-02-24T15:10:19Z)

> Hi,
> have you tried to track down the problem with rocr_debug_agent? (https://github.com/ROCm-Developer-Tools/rocr_debug_agent)
> I had a memory access fault in my application that I tried to find for months without luck. rocr_debug_agent pointed me to the right location in the code.
> You need a Vega GPU, older ASICS are not supported.

and Radeon VII is supported?


---

### 评论 #3 — Moading (2020-02-24T15:14:38Z)

Yes

---

### 评论 #4 — preda (2020-02-24T20:11:31Z)

At this point I have no indication that there is a memory access error in GpuOwl. Secondly, I am not able to run OpenCL with ROCm 3.0 as discussed here https://github.com/RadeonOpenCompute/ROCm/issues/977 , and as such I can't investigate GpuOwl's behavior on 3.0.

---

### 评论 #5 — valeriob01 (2020-02-25T01:38:41Z)

> At this point I have no indication that there is a memory access error in GpuOwl. Secondly, I am not able to run OpenCL with ROCm 3.0 as discussed here #977 , and as such I can't investigate GpuOwl's behavior on 3.0.

It would be useful if they indicated which PRP values they used for the test.


---

### 评论 #6 — preda (2020-02-28T12:07:15Z)

As mentioned in #977 recently I was able to run with ROCm 3.1. There was no "memory access fault" reported but the computation does not proceed correctly. Basically there is a bug, either in gpuowl or in the OpenCL codegen or somewhere.

---

### 评论 #7 — pramenku (2020-02-29T09:57:32Z)

> 
> 
> As mentioned in #977 recently I was able to run with ROCm 3.1. There was no "memory access fault" reported but the computation does not proceed correctly. Basically there is a bug, either in gpuowl or in the OpenCL codegen or somewhere.

it looks like it may be from application side on ROCm3.1.
We  can give a try below info and see if it helps.

gpuowl : https://github.com/preda/gpuowl 
Commit ID à  305d2b4949b7827af6e394eaf6c7a0d41c1b17c3  --> Pass
Commit ID à  6d275b7130dbcc05d9ca1771fd8ba2522f3b6a75 -->Fail [ first commit that started seeign failure ]

---

### 评论 #8 — preda (2020-02-29T23:44:52Z)

> it looks like it may be from application side on ROCm3.1.
> We can give a try below info and see if it helps.
> 
> gpuowl : https://github.com/preda/gpuowl
> Commit ID à 305d2b4949b7827af6e394eaf6c7a0d41c1b17c3 --> Pass
> Commit ID à 6d275b7130dbcc05d9ca1771fd8ba2522f3b6a75 -->Fail [ first commit that started seeign failure ]

@pramenku Thank you I'll have a look.


---

### 评论 #9 — preda (2020-03-01T12:30:45Z)

If that's fine I'm going to close this issue, because it seems there is no Memory Acccess Error with ROCm 3.1 anymore, so this issue relative to 3.0 seems to have been already fixed in 3.1.
(can't close, I think original author should close)

---

### 评论 #10 — pskumar152 (2020-03-02T09:29:29Z)

No Memory Access Fault issue is observed in ROCm 3.1. 

Verified with the latest gpuowl commit + ROCm 3.1.

**Observations**
kumar@desktop-radeon7:~/Desktop/gpuowl$ ./gpuowl -prp 84682337
2020-03-02 12:57:06 gpuowl v6.11-160-g74b7196-dirty
2020-03-02 12:57:06 Note: not found 'config.txt'
2020-03-02 12:57:06 config: -prp 84682337
2020-03-02 12:57:06 device 0, unique id 'a5de692172dc768b'
2020-03-02 12:57:06 a5de692172dc768b 84682337 FFT 4608K: Width 256x4, Height 64x4, Middle 9; 17.95 bits/word
2020-03-02 12:57:07 a5de692172dc768b OpenCL args "-DEXP=84682337u -DWIDTH=1024u -DSMALL_HEIGHT=256u -DMIDDLE=9u -DWEIGHT_STEP=0x1.09aaaa1a94ac2p+0 -DIWEIGHT_STEP=0x1.ed5ec2690d837p-1 -DWEIGHT_BIGSTEP=0x1.ae89f995ad3adp+0 -DIWEIGHT_BIGSTEP=0x1.306fe0a31b715p-1 -DPM1=0 -DAMDGPU=1 -cl-fast-relaxed-math -cl-std=CL2.0"
2020-03-02 12:57:10 a5de692172dc768b OpenCL compilation in 3.40 s
2020-03-02 12:57:11 a5de692172dc768b 84682337 OK 0 loaded: blockSize 400, 0000000000000003
2020-03-02 12:57:12 a5de692172dc768b 84682337 OK 800 0.00%; 595 us/it; ETA 0d 14:00; d0b20c358eaddcea (check 0.33s)
2020-03-02 12:59:12 a5de692172dc768b 84682337 OK 200000 0.24%; 601 us/it; ETA 0d 14:07; 3ad53bdf0f0dcb10 (check 0.33s)
2020-03-02 13:01:13 a5de692172dc768b 84682337 OK 400000 0.47%; 603 us/it; ETA 0d 14:07; 2fa7256aa0425861 (check 0.33s)

---

### 评论 #11 — seesturm (2020-03-07T10:19:35Z)

I was courious what actually fixed the memory access fault in ROCm 3.1. Didn't find any message from the maintainers on this topic. It appears that the fix is in the firmware blob since I had to update the firmware to the latest one found on linux-firmware.git.

Really a pity that there is no proper changelog for the firmware. One finding from this is that there are certain kind of bugs which cannot be fixed by the open source community despite all the host software being open source. But to be honest, currently there seems to be practically no community outside of AMD for maintaining ROCm.

---

### 评论 #12 — pramenku (2020-03-09T06:51:16Z)

> 
> 
> If that's fine I'm going to close this issue, because it seems there is no Memory Acccess Error with ROCm 3.1 anymore, so this issue relative to 3.0 seems to have been already fixed in 3.1.
> (can't close, I think original author should close)

Thanks for the confirmation.

---

### 评论 #13 — streamhsa (2020-03-09T06:52:31Z)

As per preda, 3.1 doesn't exhibit this issue. so closing this issue.

---
