# amdgpu kworker CPU usage growing in time

> **Issue #1059**
> **状态**: closed
> **创建时间**: 2020-03-26T11:44:08Z
> **更新时间**: 2020-04-25T07:21:56Z
> **关闭时间**: 2020-04-25T07:21:56Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1059

## 描述

With RadeonVII (but likely independent of the specific GPU model)
With Linux 2.4.x, 2.5.x, 2.6.x, with ROCm 2.10 and 3.1 (and likely earlier versions too),
when running an OpenCL process for a long time (tens of hours, days),

there are visible (e.g. in "top") root threads "kworker" that take up an amount of CPU that slowly increases over time until reaching 100% (i.e. one core) per kworker. The number of kworker threads is equal to the number of GPUs. Stopping all of the OpenCL apps (on *all* the GPUs) resets these kworkers to 0, from where they start climbing up again.

```
  973 root      20   0       0      0      0 I  35.9   0.0   4:15.28 kworker/1:0-events                                                                                                        
 2477 root      20   0       0      0      0 I  34.9   0.0   0:33.77 kworker/5:34-events
```

After stopping *all* opencl apps and re-starting all again:

```
  650 root      20   0       0      0      0 I   2.3   0.0   8:19.30 kworker/3:3-events                                                                                                        
 3148 root      20   0       0      0      0 I   2.3   0.0   0:01.40 kworker/6:1-events 
```

It appears to me that these "kworker" are related to the amdgpu kernel driver. If so, this may be an amdgpu issue instead of a ROCm one.

One way to repro is to run gpuowl for a long time (many hours), ideally two instances on a system with 2 GPUs, and you should see the kworker average CPU usage growing in time.


---

## 评论 (8 条)

### 评论 #1 — valeriob01 (2020-03-26T13:41:35Z)

I have noticed the same thing with Debian Buster and ROCm 2.10 and gpuowl.

---

### 评论 #2 — fxkamd (2020-03-26T15:05:58Z)

Are there any messages in "dmesg" about hanging kernel worker threads?

Can you get more details about the code causing the CPU usage with "perf top"?

Which kernel and driver version are you using? The DKMS kernel module or the upstream one?

---

### 评论 #3 — valeriob01 (2020-03-26T15:17:43Z)

Debian Buster kernel 4.19 - ROCm 2.10

![image](https://user-images.githubusercontent.com/25838910/77663388-49ebb280-6f7d-11ea-8d6b-aef9fcd745ba.png)


---

### 评论 #4 — fxkamd (2020-03-26T15:34:35Z)

That "perf top" is not very helpful. It's showing the kernel CPU usage in a spin-lock. I'd need to know where it's called from. Does "perf top -g" work?

I fixed a similar problem recently that was caused by the code that frees memory at process termination. But your description of increasing CPU usage with a long running application sounds like a different issue, unless the application starts and terminates multiple processes.

If you want to try it out, you could apply it manually to /usr/src/amdgpu/... and rebuild your dkms kernel module with dkms remove/build/install commands.

This is the patch:
```
commit 27f098d17ca7e6a24a35a192d00ab2e1462034b9
Author: Felix Kuehling <Felix.Kuehling@amd.com>
Date:   Wed Mar 4 15:57:23 2020 -0500

    drm/amdkfd: Signal eviction fence on process destruction (v2)
    
    Otherwise BOs may wait for the fence indefinitely and never be destroyed.
    
    v2: Signal the fence right after destroying queues to avoid unnecessary
        delaye-delete in kfd_process_wq_release
    
    Signed-off-by: Felix Kuehling <Felix.Kuehling@amd.com>
    Reviewed-by: xinhui pan <xinhui.pan@amd.com>
    Acked-by: Christian König <christian.koenig@amd.com>

diff --git a/drivers/gpu/drm/amd/amdkfd/kfd_process.c b/drivers/gpu/drm/amd/amdkfd/kfd_process.c
index 22abdbc6dfd7..c92285fbba8a 100644
--- a/drivers/gpu/drm/amd/amdkfd/kfd_process.c
+++ b/drivers/gpu/drm/amd/amdkfd/kfd_process.c
@@ -641,6 +641,11 @@ static void kfd_process_notifier_release(struct mmu_notifier *mn,
 
        /* Indicate to other users that MM is no longer valid */
        p->mm = NULL;
+       /* Signal the eviction fence after user mode queues are
+        * destroyed. This allows any BOs to be freed without
+        * triggering pointless evictions or waiting for fences.
+        */
+       dma_fence_signal(p->ef);
 
        mutex_unlock(&p->mutex);
 

```

---

### 评论 #5 — valeriob01 (2020-03-26T15:55:04Z)

> If you want to try it out, you could apply it manually to /usr/src/amdgpu/... and rebuild your dkms kernel module with dkms remove/build/install commands.

That is out of question, the system is in production.

But here is perf top -g
![image](https://user-images.githubusercontent.com/25838910/77667435-7bb34800-6f82-11ea-9419-946dd598c556.png)


---

### 评论 #6 — fxkamd (2020-03-26T16:07:57Z)

OK.  I see TTM delayed BO cleanup functions in the list. That points to the same problem I fixed with that patch.

There are other patches coming that rework the delayed BO freeing and improve the handling of KFD fences in that situation. I believe this will address the issue you're seeing.

---

### 评论 #7 — valeriob01 (2020-03-29T09:18:52Z)

> OK. I see TTM delayed BO cleanup functions in the list. That points to the same problem I fixed with that patch.
> 
> There are other patches coming that rework the delayed BO freeing and improve the handling of KFD fences in that situation. I believe this will address the issue you're seeing.

Ok but I still use ROCm 2.10 as installing ver 3.1 failed for me multiple times. There is an issue with clGetDeviceId returning -1.


---

### 评论 #8 — preda (2020-04-25T07:21:55Z)

This issue seems fixed in Linux kernel 5.6.7 and 5.7.0-rc2 . @fxkamd thank you!


---
