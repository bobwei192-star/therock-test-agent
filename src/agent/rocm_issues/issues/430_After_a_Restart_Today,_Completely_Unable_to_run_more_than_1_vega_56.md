# After a Restart Today, Completely Unable to run more than 1 vega 56

> **Issue #430**
> **状态**: closed
> **创建时间**: 2018-06-06T10:56:12Z
> **更新时间**: 2018-06-06T12:50:50Z
> **关闭时间**: 2018-06-06T12:50:50Z
> **作者**: sayyiditow
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/430

## 描述

I have been using 6 vega 56 with asus b250 mining with rocm perfectly for the last two days. I had to restart ubuntu for updates and after that, although rocm recognizes the cards, they dont hash. The only card that hashes is the one on the pcie3.0 slot. I am out of ideas, I have reinstalled ubuntu 10 times nothing, still only one out of 6 cards mine. I am unsure what else to do. Please help. I have even tried with 2 cards only, and only 1 hashes.

Stats GPU 0 - lyra2z: 5.628Mh/s (5.609Mh/s)  
[2018-06-06 03:54:09] Stats GPU 1 - 
[2018-06-06 03:54:09] Stats Total - lyra2z: 5.628Mh/s (5.609Mh/s)  

GPU 0 is always the only card hashing. 0 is on the pcie3.0 slot.

I followed these instructions as usual - which worked perfectly the last two days: https://github.com/RadeonOpenCompute/ROCm

./rocm-smi shows:
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   N/A     N/A      N/A      N/A      0%       N/A       N/A      
  2   35.0c   15.0W    1474Mhz  800Mhz   70.98%   manual    0%       
  0   59.0c   150.0W   1312Mhz  800Mhz   70.98%   manual    0%       
================================================================================
====================           End of ROCm SMI Log          ====================

As you can see only gpu 0 is working. 

Any help is appreciated.

Thank you!

---

## 评论 (10 条)

### 评论 #1 — issie81 (2018-06-06T11:14:06Z)

i am having more or less same issue, i use ROCM the cards are seen in linux even miner detects yet it only hashes with 1 card, also using Vega 56.. Software for Vegas seems to be abit weak:(

---

### 评论 #2 — sayyiditow (2018-06-06T11:42:35Z)

But this just started today, it was working perfectly, 6 vegas for 2 days continuous. 

---

### 评论 #3 — issie81 (2018-06-06T11:48:25Z)

that is really strange so i would blame this on the os? (since after update it didnt work).. i assume you mine with Tdxminer, do you mine with Rocm 1.7.1 or the new 1.8.1?
this has to have an easy fix..

---

### 评论 #4 — sayyiditow (2018-06-06T12:20:03Z)

tdxminer, rocm 1.8.151. Yes same here, it must have been the system update. Not sure when we can get a fix :(

---

### 评论 #5 — gstoner (2018-06-06T12:41:56Z)

Your issue is in 1.8.1,  we found a bug with SDMA firmware had to turn back on PCIe Atomics,  they are working on a fix for it in the SDMA firmware.   But we needed to address an issue with REHL/CENTOS 7.5 support to simplify 

You need to  disable the SDMA which go back to PCIe atomic free mode  to do this you must set HSA_ENABLE_SDMA=0





---

### 评论 #6 — sayyiditow (2018-06-06T12:43:40Z)

Hi @gstoner how do we set that? Sorry not so good with ubuntu. Thanks so much.

---

### 评论 #7 — sayyiditow (2018-06-06T12:45:49Z)

Ah it is done on the terminal. Nevermind. Trying it now.

---

### 评论 #8 — sayyiditow (2018-06-06T12:48:15Z)

I can confirm that HSA_ENABLE_SDMA=0 works perfectly. I have set it up on the "startup applications" All gpus hashing. Thanks @gstoner !

---

### 评论 #9 — gstoner (2018-06-06T12:50:19Z)

You use 
export HSA_ENABLE_SDMA=0

I also cleaned up the language on the Readme. 

One thing you can look at is all the debug flags for ROCm here 
http://rocm-documentation.readthedocs.io/en/latest/Other_Solutions/Other-Solutions.html

---

### 评论 #10 — sayyiditow (2018-06-06T12:50:50Z)

Thank you!

---
