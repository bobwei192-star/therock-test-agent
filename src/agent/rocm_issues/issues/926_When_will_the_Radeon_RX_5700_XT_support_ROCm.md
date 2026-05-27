# When will the Radeon RX 5700 XT support ROCm

> **Issue #926**
> **状态**: closed
> **创建时间**: 2019-11-02T01:52:27Z
> **更新时间**: 2020-03-15T13:22:23Z
> **关闭时间**: 2019-11-04T21:10:52Z
> **作者**: omerferhatt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/926

## 描述

I purchased the RX 5700 XT and was planning to use it in my ML projects. But I realized that the card has not yet received ROCm support. Is there a scheduled release date? If not, I will return the card back to the store. Hopefully, it will be answered quickly and precisely.

---

## 评论 (4 条)

### 评论 #1 — seesturm (2019-11-02T11:19:25Z)

AFAIK the most accurate statement currently available is [this comment](https://github.com/RadeonOpenCompute/ROCm/issues/819#issuecomment-532886041). My interpretation of the comment is that nobody official is willing to give a hint when it will be released. In principle it could even take years before it is supported.

Between the lines it looks like as if they intend to eventually support Navi. But personally I wouldn't buy a Navi card if I want to do ML within the next months.

---

### 评论 #2 — omerferhatt (2019-11-02T19:19:20Z)

Thank you for your reply. I'm sorry to hear that. I am going to return my card.

---

### 评论 #3 — nuliknol (2020-03-06T17:49:24Z)

>I am going to return my card.

@omerferhatt 
so why can't you code the kernels of your ML projects with OpenCL ?


---

### 评论 #4 — ashishchoure23 (2020-03-15T13:22:23Z)

Why returning, use plaidML with Keras. It works like charm.

---
