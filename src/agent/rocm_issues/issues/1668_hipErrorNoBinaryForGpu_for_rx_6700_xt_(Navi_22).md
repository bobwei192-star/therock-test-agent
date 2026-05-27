# "hipErrorNoBinaryForGpu" for rx 6700 xt (Navi 22)

> **Issue #1668**
> **状态**: closed
> **创建时间**: 2022-02-08T11:33:33Z
> **更新时间**: 2023-03-26T02:08:32Z
> **关闭时间**: 2022-02-18T06:35:22Z
> **作者**: kvirikroma
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1668

## 描述

AFAIK, Navi 21 is supported by ROCm, and some users even were able to replace some values in source code to make a software think that Navi 22 is actually supported (and assuming they don't lie, it really works for them), but for some reason, there's no official support for rx 6700 xt yet. It would be really nice if you let me know if such support is planned. Thanks (=

---

## 评论 (15 条)

### 评论 #1 — aoolmay (2022-02-11T18:55:51Z)

Some did report Navi working, i only got 6800xt/6900xt machines to work using the docker provided in installation manual. No bare metal experience. If you can afford the docker compromise, you should give it a try.

---

### 评论 #2 — xuhuisheng (2022-02-11T23:48:06Z)

6700 may be gfx1031, which is not supported official. You could check by `/opt/rocm/bin/rocminfo`.
If you want gfx1031, you could have to try to compile ROCm from source with AMDGPU_TARGETS=gfx1031.


---

### 评论 #3 — kvirikroma (2022-02-12T10:59:37Z)

@aoolmay Thanks for the advice.
I've tried docker already, but basically what I did to make it work is added host devices (/dev/dri and /dev/kfd) to the container and it worked for my old rx570 (with older versions of rocm). So I think it is the same as doing it on bare metal. At least an error for rx6700xt is the same with docker and without it (hipErrorNoBinaryForGpu).


---

### 评论 #4 — kvirikroma (2022-02-12T11:16:40Z)

@xuhuisheng Thank you for the advice, that sounds promising. I'll probably try it in a few days, but I don't know much about compiling ROCm. I have a lot of packages related to it installed in my system now, do I need to compile each of them separately? And where it would be correct to get sources from? I know about https://github.com/ROCmSoftwarePlatform/ but I'm not sure that I'm on the right way. Could you please send me some guide or documentation on compiling ROCm from the source?

---

### 评论 #5 — xuhuisheng (2022-02-12T22:02:57Z)

@kvirikroma
Here is my building script. <https://github.com/xuhuisheng/rocm-build>


---

### 评论 #6 — kvirikroma (2022-02-13T09:09:58Z)

@xuhuisheng thank you (=

---

### 评论 #7 — aoolmay (2022-02-17T19:10:58Z)

@kvirikroma @xuhuisheng  I've just spotted fresh tensorflow-rocm package, version 2.8.0, in pip. Works on bare metal with 6800xt, installed the driver with "rocm,hip,opencl" and simple pip install tensorflow-rocm. I've yet to test 6900xt, don't have other NAVI cards, i hope it works for you on 6700xt.

---

### 评论 #8 — ROCmSupport (2022-02-18T06:35:22Z)

Hi @kvirikroma 
Thanks for reaching out.
ROCm does not support Navi22 and so can not comment on this.
For supported hardware, please check [https://docs.amd.com/bundle/ROCm_Release_Notes_v5.0/page/About_This_Document.html](url)
Thank you.

---

### 评论 #9 — NJannasch (2022-02-25T16:01:36Z)

For the 6700xt this link might be interesting:
https://www.zhihu.com/question/469674526/answer/2189926640
->
https://www-zhihu-com.translate.goog/question/469674526/answer/2189926640?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=de&_x_tr_pto=wapp


---

### 评论 #10 — kvirikroma (2022-04-27T06:04:07Z)

This is where I stuck after spending some time trying to compile ROCm and TF for gfx1031
https://github.com/ROCmSoftwarePlatform/MIOpen/issues/1528
Update: it is solved now, and I've successfully got ROCm working on my GPU (=

---

### 评论 #11 — arcaspo (2022-05-13T08:16:24Z)

@xuhuisheng Will your build script, https://github.com/xuhuisheng/rocm-build, work for Navi 23? I only see up to navi 21, so if i change AMDGPU_TARGETS to gfx1032 would the build work for the 6600xt?

---

### 评论 #12 — xuhuisheng (2022-05-13T08:30:11Z)

@arcaspo 
You can have a try.
But there are some scripts for gfx1031 in MIOpen, you can refer here: 
<https://github.com/ROCmSoftwarePlatform/MIOpen/pull/1531>

---

### 评论 #13 — arcaspo (2022-05-13T08:55:23Z)

Thanks, I’ll try later :)

---

### 评论 #14 — julianoes (2022-11-17T21:16:17Z)

One more thing to check, make sure the user is in the `video` and `render` group.

```
sudo usermod -a -G video $LOGNAME
sudo usermod -a -G render $LOGNAME
```

Then logout and log back in, and check whether the groups are listed when running `groups`. In my case a reboot was required.

---

### 评论 #15 — SamuelMarks (2023-03-26T02:08:32Z)

@xuhuisheng Open to testing with my Navi 22 [AMD Radeon(TM) RX 6850M XT 12GB GDDR6] on Linux kernel 6.2.8 running Ubuntu 22.10 (soon 23.04?). Going through your repo now.

(any tips from anyone here is most welcome)

---
