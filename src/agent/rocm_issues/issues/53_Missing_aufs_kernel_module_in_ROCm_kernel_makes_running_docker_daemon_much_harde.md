# Missing aufs kernel module in ROCm kernel makes running docker daemon much harder

> **Issue #53**
> **状态**: closed
> **创建时间**: 2016-12-09T07:25:49Z
> **更新时间**: 2017-01-04T14:06:34Z
> **关闭时间**: 2017-01-04T14:06:34Z
> **作者**: ptrkrysik
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/53

## 描述

Current ROCm distribution of Linux kernel (4.6.0-kfd-compute-rocm-rel-1.3-74) doesn't provide kernel module for aufs file system. This makes docker daemon fail when starting and makes the description (https://github.com/RadeonOpenCompute/ROCm-docker) of installation of docker containers on the ROCm kernel incomplete.

systemctl status docker.service
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since pią 2016-12-09 08:22:57 CET; 5s ago
     Docs: https://docs.docker.com
  Process: 2911 ExecStart=/usr/bin/dockerd -H fd:// $DOCKER_OPTS (code=exited, status=1/FAILURE)
 Main PID: 2911 (code=exited, status=1/FAILURE)

gru 09 08:22:56 computer systemd[1]: Starting Docker Application Container Engine...
gru 09 08:22:56 computer dockerd[2911]: time="2016-12-09T08:22:56.334816244+01:00" level=info msg="libcontainerd: new containerd process, pid: 2923"
gru 09 08:22:57 computer dockerd[2911]: time="2016-12-09T08:22:57.394559569+01:00" level=error msg="[graphdriver] prior storage driver \"aufs\" failed: driver not supported"
gru 09 08:22:57 computer dockerd[2911]: time="2016-12-09T08:22:57.394752192+01:00" level=fatal msg="Error starting daemon: error initializing graphdriver: driver not supported"
gru 09 08:22:57 computer systemd[1]: docker.service: Main process exited, code=exited, status=1/FAILURE
gru 09 08:22:57 computer systemd[1]: Failed to start Docker Application Container Engine.
gru 09 08:22:57 computer systemd[1]: docker.service: Unit entered failed state.
gru 09 08:22:57 computer systemd[1]: docker.service: Failed with result 'exit-code'.


---

## 评论 (3 条)

### 评论 #1 — almson (2016-12-09T16:46:27Z)

I have the same problem with zfs modules. I was able to apply the Ubuntu patches (and get a kernel with all of these modules) to the ROCm 1.2 kernel, but couldn't for 1.3. They promised to be working on DKMS support to decouple ROCm from the kernel, but gave no word as to how or when.

---

### 评论 #2 — gstoner (2016-12-14T12:54:03Z)

Base DKMS is in ROCm 1.3,  We are still working on it we have other module that we need to work on.  With 1.4 I see if we can preconfigure AUFS back in the kernel.   Remember ROCm has very advanced driver that support richer memory management then what you have in the base graphics driver to better support compute programing models.  

---

### 评论 #3 — gstoner (2016-12-14T12:59:55Z)

I found it not just ROCm issue but 16.04 with Linux Kernel 4.6.x issue  you see they had to use overlay files system https://github.com/docker/docker/issues/23968 

---
