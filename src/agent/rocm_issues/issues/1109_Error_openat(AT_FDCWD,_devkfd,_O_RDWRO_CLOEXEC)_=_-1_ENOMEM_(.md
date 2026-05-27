# Error: openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (

> **Issue #1109**
> **状态**: closed
> **创建时间**: 2020-05-15T08:51:00Z
> **更新时间**: 2021-06-03T09:37:28Z
> **关闭时间**: 2021-06-03T09:37:28Z
> **作者**: Disidente
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1109

## 描述


Ubuntu 20.04 . Intel i7-2600K (16Gb RAM) - Radeon RX480 6Gb  

sudo /opt/rocm/bin/rocminfo

```ROCk module is loaded
carlos is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```


strace /opt/rocm/bin/rocminfo


```
write(1, "\33[37mcarlos is member of video g"..., 41carlos is member of video group
) = 41
getpid()                                = 3136
openat(AT_FDCWD, "/dev/kfd", O_RDWR|O_CLOEXEC) = -1 ENOMEM (No se pudo asignar memoria)
write(1, "\33[31mhsa api call failure at: /d"..., 101hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
) = 101
write(1, "\33[31mCall returned HSA_STATUS_ER"..., 228Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
) = 228
write(1, "\33[0m", 4)                   = 4
lseek(3, -337, SEEK_CUR)                = -1 ESPIPE (Desplazamiento ilegal)
exit_group(4104)                        = ?
+++ exited with 8 +++
```


---

## 评论 (5 条)

### 评论 #1 — balasundram (2020-05-19T09:15:01Z)

you got any fix?
same issue !!!


---

### 评论 #2 — maomaopangba (2020-07-21T06:16:33Z)

Ubuntu 18.04
5.4.0-42-generic #46~18.04.1-Ubuntu SMP
I have the same issue.
Any update?

---

### 评论 #3 — xuhuisheng (2020-07-21T06:43:03Z)

1. check the permission of /dev/kfd, make sure the loginUser in the group /dev/kfd
2. check the dmesg|grep kfd, make sure kfd not reject the video card

---

### 评论 #4 — ROCmSupport (2021-03-03T11:05:19Z)

Hi @Disidente 
Can you please verify with the latest ROCm 4.0 and share an update asap.
So that I can move this issue to next level.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-06-03T09:37:28Z)

I am closing this as there is no response for more than 2 months.
Feel free to open a new issue, if any.
Thank you.

---
