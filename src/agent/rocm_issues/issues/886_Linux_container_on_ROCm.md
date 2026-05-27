# Linux container on ROCm

> **Issue #886**
> **状态**: closed
> **创建时间**: 2019-09-12T11:41:09Z
> **更新时间**: 2024-02-23T18:23:06Z
> **关闭时间**: 2019-11-13T21:03:32Z
> **作者**: smithakihide
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/886

## 描述

Hello, thank you to read this issue.

How can I use ROCm in a Linux container, called [LXC](https://linuxcontainers.org/)?
If you know any about this topic, please tell me.

---

## 评论 (6 条)

### 评论 #1 — Bengt (2019-09-15T00:40:58Z)

There are docker images for ROCm Tensorflow upstream. Do these work for you?

---

### 评论 #2 — smithakihide (2019-09-17T17:46:42Z)

Thank you for replying.
I have not tried Docker image of ROCm Tensorflow yet because it is not in my interest.
I would like to use ROCm in my original program with C++. Using Tensorflow is not my purpose. So although there might be docker images other than for Tensorflow, even in the case, I would like to use LXC for system container, not Docker.

---

### 评论 #3 — sunway513 (2019-10-01T19:48:00Z)

Hi @smithakihide , does the following rocm dev docker work for you:
https://hub.docker.com/r/rocm/dev-ubuntu-18.04

---

### 评论 #4 — extraymond (2020-02-20T12:54:10Z)

> Hello, thank you to read this issue.
> 
> How can I use ROCm in a Linux container, called [LXC](https://linuxcontainers.org/)?
> If you know any about this topic, please tell me.

Hi! I've tried setting up rocm in a lxd container.
Here's the needed setup if anyone is interested.

After setting up rocm the way would've done on the host, assumed the following:
1. you are in the video group
2. you've allow /dev/kfd to be access by video group.

We can now use lxd's config device option to expose the host's devices with the correct permission so that the guest container can access it as a non-root user.

```bash
lxc config device add $container_name $kfd_device_name_you_want unix-char gid=${gid_of_group_video} source=/dev/kfd mode=666
lxc config device add $container_name $gpu_name gid=${gid_of_group_video}
```

So for example my config would have these two devices:
```yaml
devices:
  gpu:
    gid: "44"
    type: gpu
  kfd:
    gid: "44"
    mode: "666"
    source: /dev/kfd
    type: unix-char

```

![Screenshot from 2020-02-20 20-51-56](https://user-images.githubusercontent.com/707176/74935375-17e9ac80-5423-11ea-8944-6bffacff2d2a.png)

![Screenshot from 2020-02-20 20-53-27](https://user-images.githubusercontent.com/707176/74935380-1ae49d00-5423-11ea-8f0a-0c2ca12af868.png)


---

If you want to specifically configure gpu to be exposed to the guest:
![https://lxd.readthedocs.io/en/stable-3.0/containers/#type-gpu](https://lxd.readthedocs.io/en/stable-3.0/containers/#type-gpu)

---

### 评论 #5 — smithakihide (2020-02-21T02:34:02Z)

really? thank you very much to tell me your trial!.

I' ll try it too.

---

### 评论 #6 — DocMAX (2024-02-23T18:22:59Z)

I can't make kfd work in lcx container...
```
root@ollama:~# rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Operation not permitted
root is member of render group
```

---
