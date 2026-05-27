# https://rocm.github.io/install.html vs https://rocm.github.io/ROCmInstall.html 

> **Issue #328**
> **状态**: closed
> **创建时间**: 2018-02-04T16:52:36Z
> **更新时间**: 2024-02-29T18:05:15Z
> **关闭时间**: 2018-02-04T16:59:03Z
> **作者**: Mandrewoid
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/328

## 描述

What is the difference, which is correct, and why do both exist?
https://rocm.github.io/install.html
https://rocm.github.io/ROCmInstall.html

---

## 评论 (7 条)

### 评论 #1 — gstoner (2018-02-04T16:58:22Z)

You're looking at the source to the website,  One document superseded the other this. Correct one   https://rocm.github.io/ROCmInstall.html



---

### 评论 #2 — Mandrewoid (2018-02-04T17:11:33Z)

Thank you

---

### 评论 #3 — Mandrewoid (2018-02-04T17:19:01Z)

@gstoner  I don't know if you changed something, but https://rocm.github.io/install.html is now 404. This is the first google search result for "Rocm website"  It is also still linked to from the "getting started" button. For SEO purposes I think having it be a redirect would be better than just removing

---

### 评论 #4 — gstoner (2018-02-04T20:23:02Z)

fixed

---

### 评论 #5 — ferlix9o (2018-07-07T11:33:42Z)

Hi @Mandrewoid 

i red that u manage to use the Vega FE with rocm, would u mind to tell me if it worked straight out of the box ? i am struggling a lot with it, my computecpp_info tell me is missing SPIR support.

sry for the intrusion ! but i would really appreciate a bit of help !

---

### 评论 #6 — gstoner (2018-07-07T14:42:15Z)

@ferlix9o   SPIR is not supported on ROCm OpenCL currently.   Here is more info on SPIR https://www.khronos.org/spir/ The application you have is compiled to SPIR object. 

---

### 评论 #7 — roycewilliams (2024-02-29T18:05:14Z)

For future searchers, at this writing neither install.html nor ROCmInstall.html exist. Docs have been relocated to:

https://rocm.docs.amd.com/en/latest/

... with Linux-specific steps here:

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/

---
