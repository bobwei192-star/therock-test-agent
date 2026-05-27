# The rocm-dkms doesn't install on Ubuntu 16.04 inside Docker

> **Issue #459**
> **状态**: closed
> **创建时间**: 2018-07-19T10:01:57Z
> **更新时间**: 2019-09-01T18:34:38Z
> **关闭时间**: 2018-07-19T21:52:49Z
> **作者**: adamradocz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/459

## 描述

Hi,

I've tried to install the rocm-dkms  package inside a Docker container, but it throws the following error:
```
Setting up rock-dkms (1.8-151) ...
Loading new amdgpu-1.8-151 DKMS files...
First Installation: checking all kernels...
dpkg: warning: version '*-*' has bad syntax: version number does not start with digit
It is likely that 4.15.0-23-generic belongs to a chroot's host
Building for architecture x86_64
Setting up rocm-device-libs (0.0.1) ...
Setting up rocm-smi (1.0.0-42-g0ae1c36) ...
Setting up rocm-dev (1.8.151) ...
Setting up rocm-dkms (1.8.151) ...
tee: /etc/udev/rules.d/kfd.rules: No such file or directory
KERNEL=="kfd", MODE="0666"
dpkg: error processing package rocm-dkms (--configure):
 subprocess installed post-installation script returned error exit status 1
Setting up libnuma-dev:amd64 (2.0.11-1ubuntu1.1) ...
Processing triggers for libc-bin (2.23-0ubuntu10) ...
Processing triggers for systemd (229-4ubuntu21.2) ...
Errors were encountered while processing:
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```


The Dockerfile looks like this:

```
FROM ubuntu:16.04

# Install ROCm Driver
RUN curl -sL http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | apt-key add - && \
    sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list' && \
    apt-get update && apt-get install -y --no-install-recommends \
    rocm-dkms && \
# Cleaning up
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*
```

---

## 评论 (6 条)

### 评论 #1 — sunway513 (2018-07-19T19:14:12Z)

@adamradocz , you are right, the rocm-dkms package is not supposed to be installed inside docker container, you should use rocm-dev instead. 
Please note the rocm-dkms meta package includes rock-dkms, which is the one need to be installed in your bare metal system.  

---

### 评论 #2 — adamradocz (2018-07-19T21:52:49Z)

Thank you very much!

---

### 评论 #3 — aadibajpai (2019-09-01T17:48:19Z)

So from inside docker, just `rocm-dev` is needed for ROCm to work?

---

### 评论 #4 — sunway513 (2019-09-01T18:19:21Z)

@aadibajpai , that's correct. Rocm-dkms meta-package includes rock-dkms package.
Rock-dkms package contains the kernel driver, firmware -- those shall be installed outside of the docker container and on your bare metal system. 

---

### 评论 #5 — aadibajpai (2019-09-01T18:21:54Z)

@sunway513 I see, so I do need `rocm-dkms` but outside of docker itself. Is it possible to make it work with the default linux drivers? I see it in the guide but I don't think it works from inside the docker container.

---

### 评论 #6 — sunway513 (2019-09-01T18:34:37Z)

@aadibajpai , rock-dkms package is required for Linux kernel version 4.17 and older (3.10.x, 4.13.x, etc). For those linux kernel builds newer than 4.18, please consult with the following doc:
https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels
To your question, the kernel drivers are actually decoupled with docker containers in some circumstances.
For example, the stock rocm2.7 docker container would work as long as your kernel driver has been properly configured, such as by deploying the following options:

- 4.13 + rock-dkms from rocm2.7 
- 4.18 + rock-dkms from rocm2.7
- 5.0





---
