# How to run from Docker container?

> **Issue #33**
> **状态**: closed
> **创建时间**: 2016-09-27T07:18:29Z
> **更新时间**: 2016-09-27T13:21:04Z
> **关闭时间**: 2016-09-27T13:21:04Z
> **作者**: almson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/33

## 描述

Is it possible to install and run ROCm from a docker container provided that the correct kernel is loaded?

I am running Ubuntu 16.04 and would like to install and use ROCm from a 14.04 container. I've tried using kernel 4.8.0rc8 (built from yakkety master/next) and starting docker container with `docker run -it --device=/dev/kfd <image id>`. `/opt/rocm/bin/rocm-smi -a` sees the GPU. However, vector_copy fails with `Getting a gpu agent failed.`. Debugging shows that it doesn't find any agents.


---

## 评论 (2 条)

### 评论 #1 — gstoner (2016-09-27T11:42:58Z)

Yes.. https://github.com/RadeonOpenCompute/ROCm-docker/blob/master/README.md

On Sep 27, 2016, at 2:18 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:

Is it possible to install and run ROCm from a docker container provided that the correct kernel is loaded?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/33, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DubxhlVWBWoc38GhaFHxgP80yYZSPks5quMNGgaJpZM4KHVMa.


---

### 评论 #2 — almson (2016-09-27T13:21:04Z)

Thank you. I got it to work after building and installing the correct kernel.


---
