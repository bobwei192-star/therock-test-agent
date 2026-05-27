# Radeon VII recurring error with gpuOwl PRP

> **Issue #873**
> **状态**: closed
> **创建时间**: 2019-08-23T05:24:41Z
> **更新时间**: 2023-12-18T22:24:46Z
> **关闭时间**: 2023-12-18T22:24:45Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/873

## 描述

At first I have ignored this error thinking it was a buggy gpu, but now with the second Radeon VII it is happening exactly the same error: all-zero residues, like if the program is reading from some wrong location, or a memory page has been evicted underneath.
(non-zero residues redacted).
System: Debian 10

2019-08-23 07:08:23 90166123    73860000 81.91%;  996 us/sq; ETA 0d 04:31; xxxxxxxxxxxxxxxx
2019-08-23 07:08:33 90166123    73870000 81.93%;  996 us/sq; ETA 0d 04:30; xxxxxxxxxxxxxxxx
 2019-08-23 07:08:43 90166123    73880000 81.94%;  993 us/sq; ETA 0d 04:29; 0000000000000000                                                 
 2019-08-23 07:08:53 90166123    73890000 81.95%;  992 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:03 90166123    73900000 81.96%;  992 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:13 90166123    73910000 81.97%;  991 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:23 90166123    73920000 81.98%;  992 us/sq; ETA 0d 04:29; 0000000000000000                                                 
2019-08-23 07:09:33 90166123    73930000 81.99%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:09:43 90166123    73940000 82.00%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:09:53 90166123    73950000 82.01%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:10:03 90166123    73960000 82.03%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:10:12 90166123    73970000 82.04%;  992 us/sq; ETA 0d 04:28; 0000000000000000                                                 
2019-08-23 07:10:22 90166123    73980000 82.05%;  991 us/sq; ETA 0d 04:27; 0000000000000000                                                 
2019-08-23 07:10:32 90166123    73990000 82.06%;  991 us/sq; ETA 0d 04:27; 0000000000000000                                                 
2019-08-23 07:10:43 90166123 EE 74000000 82.07%;  992 us/sq; ETA 0d 04:27; 0000000000000000 (check 1.10s)                                   
2019-08-23 07:10:43 90166123.owl loaded: k 73000000, block 1000, res64 xxxxxxxxxxxxxxxx
2019-08-23 07:10:55 90166123    73010000 80.97%; 1133 us/sq; ETA 0d 05:24; xxxxxxxxxxxxxxxx


---

## 评论 (9 条)

### 评论 #1 — valeriob01 (2019-08-23T15:34:55Z)

1. This error happens only with Radeon VII, other gpu models never seen this error;
2. The two gpus are on different mainboards;
3. One system runs on Debian and ROCm 2.7, the other system runs on Ubuntu and ROCm 2.7;
4. The error happened even with ROCm 2.4.


---

### 评论 #2 — valeriob01 (2019-09-07T16:55:56Z)

https://github.com/preda/gpuowl/issues/63

---

### 评论 #3 — valeriob01 (2019-09-13T09:06:59Z)

Triggered during computation:


![20190913_104547](https://user-images.githubusercontent.com/25838910/64850871-8d508600-d616-11e9-97a5-c31e8b9e7713.jpg)


---

### 评论 #4 — sunway513 (2019-10-07T03:58:34Z)

@valeriob01 , can you provide the full dmesg after the issue been observed? You can use this cmd:
`dmesg &> ~/dmesg.txt` and attach the txt file. 
Besides, can you share the steps to trigger the issue? 

---

### 评论 #5 — valeriob01 (2019-10-07T04:21:41Z)

> @valeriob01 , can you provide the full dmesg after the issue been observed? You can use this cmd:
> `dmesg &> ~/dmesg.txt` and attach the txt file.
> Besides, can you share the steps to trigger the issue?

I am sorry no, the story is that I have gone further and installed Debian 10.1, and ROCm 2.9, since then the error seems to be disappeared.

---

### 评论 #6 — valeriob01 (2019-10-07T06:37:56Z)

Regarding the steps to trigger the issue, just run gpuowl and watch the output. I would go so far to admit I use gpuowl as an indicator of GPU health, it may very well someday become the "mprime stress test " equivalent for GPUs.


---

### 评论 #7 — valeriob01 (2019-12-18T06:15:10Z)

Today the fault happened again after months of absence, here is a photo:
![Screenshot from 2019-12-18 08-09-58](https://user-images.githubusercontent.com/25838910/71060552-13c0ba80-2166-11ea-99d9-127fb35264dc.png)


---

### 评论 #8 — tasso (2023-12-12T22:59:01Z)

Is this issue still reproducible?  If not, can we please close it?  Thanks!

---

### 评论 #9 — tasso (2023-12-18T22:24:45Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
