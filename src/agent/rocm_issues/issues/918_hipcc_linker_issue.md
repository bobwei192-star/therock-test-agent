# hipcc linker issue

> **Issue #918**
> **状态**: closed
> **创建时间**: 2019-10-22T13:33:49Z
> **更新时间**: 2023-12-18T17:14:59Z
> **关闭时间**: 2023-12-18T17:14:58Z
> **作者**: mn265
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/918

## 描述

I am having one hip project in which i came across following scenario:

I have two cuda files(hipyfied) with same name in following file structure:
1) /root/tmp/file.cu
2) /root/tmp/in/file.cu
[sample.zip](https://github.com/RadeonOpenCompute/ROCm/files/3755949/sample.zip)

which have different implementation they are not identical.
While compiling i did not get any error but after linking in my .so it is
linking second file twice which i have verified using nm command.
I have created sample code for above scenario which is also failing with same reason.

How to reproduce:
hipcc -c f1.cpp f2.cpp
hipcc -c test/f1.cpp
hipcc f1.o f2.o test/f1.o -o -shared libf.so

please find sample code attached 

---

## 评论 (4 条)

### 评论 #1 — yulingao (2022-06-29T17:28:54Z)

I encountered the same problem. how did you solve it?

---

### 评论 #2 — mn265 (2022-06-29T19:15:07Z)

When I was working for project there was one workaround we tried in which we just renamed second file and issue was resolved 

---

### 评论 #3 — nartmada (2023-12-12T23:47:33Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #4 — nartmada (2023-12-18T17:14:58Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
