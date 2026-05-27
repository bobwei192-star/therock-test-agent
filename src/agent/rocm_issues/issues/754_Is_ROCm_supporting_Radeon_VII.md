# Is ROCm supporting Radeon VII?

> **Issue #754**
> **状态**: closed
> **创建时间**: 2019-04-02T11:09:14Z
> **更新时间**: 2019-04-03T13:43:07Z
> **关闭时间**: 2019-04-02T21:04:50Z
> **作者**: ghostplant
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/754

## 描述

Seems like the ROCm performance on Radeon VII is even worse than Vega 64.

Is ROCm WELL supporting Radeon VII?
What kernel version/driver is needed (e.g. Linux image 5.0) ?

Thanks!

---

## 评论 (18 条)

### 评论 #1 — briansp2020 (2019-04-02T12:33:09Z)

_> Seems like the ROCm performance on Radeon VII is even worse than Vega 64._

What makes you say that? People are reporting pretty good performance using Radeon VII and TensorFlow.
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/173#issuecomment-466230523

---

### 评论 #2 — ghostplant (2019-04-02T12:36:16Z)

@briansp2020 Seems like Ubuntu 16.04 doesn't even detect the correct vendor name for this model.
Should I update to a new kernel?

```sh
$ lspci | grep VGA
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 66af (rev c1)
```

---

### 评论 #3 — hyc3z (2019-04-02T12:40:38Z)

As far as I know, Ubuntu 16.04 LTS with kernel 4.18.0 isn’t working properly with post-Vega cards, and rock-DKMS will fail to build with that kernel. Just update to newer kernel version.You can even try Ubuntu disco with kernel5.0




| |
hyc
邮箱：tubao9hao@126.com
|

Signature is customized by Netease Mail Master

On 04/02/2019 20:36, ghostplant wrote:

@briansp2020 Seems like Ubuntu 16.04 doesn't even detect the correct vendor name for this model.
Should I update to a new kernel?

$ lspci | grep VGA
root@amdgpu:~/gfx-client/onnx_rocmrt_docker# lspci | grep VGA
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 66af (rev c1)

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub, or mute the thread.

---

### 评论 #4 — ghostplant (2019-04-02T12:42:44Z)

@Hycdog Thanks, if I install linux-image-5.0, should I purge the installation of `rock-dkms`?

---

### 评论 #5 — hyc3z (2019-04-02T12:54:07Z)

You may check out the full installation document here:
https://github.com/RadeonOpenCompute/ROCm

> These meta-packages are not required but may be useful to make it easier to install ROCm on most systems. Some users may want to skip certain packages. For instance, a user that wants to use the upstream kernel drivers (rather than those supplied by AMD) may want to skip the `rocm-dkms` and `rock-dkms` packages, and instead directly install `rocm-dev`.

So yes, if the kernel driver can detect your card correctly, you should directly install `rocm-dev` and follow the steps afterwards.



---

### 评论 #6 — ghostplant (2019-04-02T14:12:24Z)

@Hycdog Hi, I upgrade my Ubuntu to use `Linux image 5.0.0`, and also install the latest rocm-dev via apt-get. But rocminfo couldn't detect it, and hip applications failed to run as well:
```sh
root@amdgpu:~# uname -a
Linux amdgpu 5.0.0-8-generic #9-Ubuntu SMP Tue Mar 12 21:58:11 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
root@amdgpu:~# apt policy rocm-dev
rocm-dev:
  Installed: 2.2.31
  Candidate: 2.2.31
  Version table:
 *** 2.2.31 500
        500 http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
        100 /var/lib/dpkg/status
root@amdgpu:~# lsmod | grep amdgpu
amdgpu               3534848  0
chash                  16384  1 amdgpu
amd_iommu_v2           20480  1 amdgpu
gpu_sched              32768  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   102400  1 amdgpu
drm_kms_helper        180224  1 amdgpu
drm                   479232  4 gpu_sched,drm_kms_helper,amdgpu,ttm
root@amdgpu:~# lspci | grep VGA
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 66af (rev c1)
root@amdgpu:~# /opt/rocm/bin/rocminfo
hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.2/rocminfo/rocminfo.cc. Call returned 4104
```

---

### 评论 #7 — ghostplant (2019-04-02T14:35:50Z)

After upgrading Linux kernel to 5.0, the device file `/dev/dri` is missing, even through amdgpu could be found by `lsmod | grep amdgpu`.

---

### 评论 #8 — hyc3z (2019-04-02T15:31:39Z)

Did you reboot your system after installing rocm-dev？A reboot is needed to make it work.




| |
hyc
邮箱：tubao9hao@126.com
|

Signature is customized by Netease Mail Master

On 04/02/2019 22:35, ghostplant wrote:

Note that after upgrading Linux kernel to 5.0, this device file /dev/dri is missing, even through amdgpu could be found by lsmod | grep amdgpu.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub, or mute the thread.

---

### 评论 #9 — ghostplant (2019-04-02T15:37:55Z)

@Hycdog Yes, it works just now by upgrading linux-firmware as well. However, even if I uses Linux 5.0 + rocm-dev 2.2, the benchmark is still around 30%-40% worse than Vega64, any explanations or root-causes? Radeon VII should have 10% more TFlops than Vega 64.

---

### 评论 #10 — hyc3z (2019-04-02T15:42:32Z)

@ghostplant 

> @Hycdog Yes, it works just now by upgrading linux-firmware as well. However, even if I uses Linux 5.0 + rocm-dev 2.2, the benchmark is still around 30%-40% worse than Vega64, any explanations or root-causes? Radeon VII should have 10% more TFlops than Vega 64.

I’m not sure ,but maybe you can check out
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/173
for some performance comparison?

---

### 评论 #11 — sebpuetz (2019-04-02T16:49:41Z)

Upstream drivers come with [quite a drop in performance for Radeon VII.](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/329) Up until the most recent (5.0.5, I believe?), all kernels brought the same performance regression.  If you want a properly working (fast) GPU, you probably have to downgrade to 4.15 and install rocm-dkms.

---

### 评论 #12 — ghostplant (2019-04-02T16:58:08Z)

@sebpuetz Thank you. I have tested both `Ubuntu 16.04 + Linux kernel 4.15 + rock-dkms` and `Ubuntu 16.04 + Linux kernel 5.0` have very bad ROCm performance, so I am afraid that `Ubuntu 18.04 + Linux kernel 4.15 + rock-dkms` could be the same.
Do you think the solution of root-cause is just by using Ubuntu 18.04? It just looks strange.

---

### 评论 #13 — alexpattyn (2019-04-02T19:46:41Z)

@ghostplant I wanted to ask what did you use to upgrade to the 5.0 kernel? I have been having issues with missing firmware on 18.04 and 18.10 with the 4.18 kernel. And then did you install the whole ROCm stack? Since it only supports <4.18 until ROCm 2.3 I believe.

Edit: I have a radeon vii. I also haven't had firmware issues with Fedora 29 using the 5.0 kernel, however ROCm isn't supported in Fedora beyond 2.0 that is in the repos, so I am looking to use ubuntu for now. 

---

### 评论 #14 — sebpuetz (2019-04-02T20:02:07Z)

> @sebpuetz Thank you. I have tested both `Ubuntu 16.04 + Linux kernel 4.15 + rock-dkms` and `Ubuntu 16.04 + Linux kernel 5.0` have very bad ROCm performance, so I am afraid that `Ubuntu 18.04 + Linux kernel 4.15 + rock-dkms` could be the same.
> Do you think the solution of root-cause is just by using Ubuntu 18.04? It just looks strange.

@ghostplant Never used 16.04, so I can't say much about it

>Edit: I have a radeon vii. I also haven't had firmware issues with Fedora 29 using the 5.0 kernel, however ROCm isn't supported in Fedora beyond 2.0 that is in the repos, so I am looking to use ubuntu for now.

@koenigjaeger What's performance on benchmarks with ROCm 2.0 and the upstream kernel? This issue contains some references
 ROCmSoftwarePlatform/tensorflow-upstream#173

---

### 评论 #15 — alexpattyn (2019-04-02T20:38:00Z)

@sebpuetz I was never able to get ROCm from github working due to the missing firmware I believe and then in fedora I only had OpenCL from Mesa available. 

Then ROCm version from fedora's repos is only at 2.0 and using clinfo I could only see my ryzen 5 + vega 8 available with OpenCL 1.2 and Vega 20 was once again only using OpenCL 1.1 (so I can't really test any real OpenCL code). I also believe the ROCm in fedoras repos is only a part of and not the whole stack.

---

### 评论 #16 — jlgreathouse (2019-04-02T21:04:50Z)

> @briansp2020 Seems like Ubuntu 16.04 doesn't even detect the correct vendor name for this model.
> Should I update to a new kernel?

`sudo update-pciids` will pull a new PCI ID naming list. the command you ran doesn't really have anything to do with your kernel version.

In any case, it seems that you've taken your performance question over to the `tensorflow-upstream` issue, so I'm going to close this issue.

---

### 评论 #17 — ghostplant (2019-04-03T06:15:23Z)

@sebpuetz I upgrade the Ubuntu linux kernel from this site:
https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.15/

---

### 评论 #18 — alexpattyn (2019-04-03T13:43:07Z)

@ghostplant Thanks, I'll check that out. 

---
