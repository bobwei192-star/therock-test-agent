# Driver loaded but still getting error 4104

> **Issue #693**
> **状态**: closed
> **创建时间**: 2019-01-30T15:09:10Z
> **更新时间**: 2019-02-06T00:19:38Z
> **关闭时间**: 2019-01-30T17:11:28Z
> **作者**: CyberShadow
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/693

## 描述

Hi, I'm trying to get the ROCm stack working on the following system:

- Distribution: Arch Linux
- Kernel: 4.20.3-arch1-1-ARCH (distro package)
- GPU: Vega 10 XL/XT [Radeon RX Vega 56/64] (rev c1)
- CPU: Intel(R) Core(TM) i7-4960X CPU @ 3.60GHz
- Motherboard: Gigabyte X79S-UP5

I understand that `amdkfd` was merged into `amdgpu` in 4.20, which is why it's not in `lsmod`:

```console
$ lsmod | grep amd
amdgpu               3756032  39
chash                  16384  1 amdgpu
amd_iommu_v2           20480  1 amdgpu
gpu_sched              36864  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   110592  1 amdgpu
drm_kms_helper        208896  1 amdgpu
drm                   499712  10 gpu_sched,drm_kms_helper,amdgpu,ttm
```

The CPU/MB are pretty old, but the driver isn't complaining in dmesg, so looks like this combination (Ivy Bridge-E) should be supported?

```console
$ dmesg | grep -i kfd
[   10.381974] kfd kfd: Allocated 3969056 bytes on gart
[   10.382148] kfd kfd: added device 1002:687f
```

However, I'm still getting `hsa api call failure at line 900` / `Call returned 4104` from the `rocminfo` binary. strace shows:

```
ioctl(3, _IOC(_IOC_READ|_IOC_WRITE, 0x4b, 0x19, 0x10), 0x7ffcd47c7f10) = -1 EINVAL (Invalid argument)
ioctl(3, AMDKFD_IOC_GET_PROCESS_APERTURES, 0x7ffcd47c7f20) = 0
ioctl(3, _IOC(_IOC_WRITE, 0x4b, 0x21, 0x8), 0x7ffcd47c80b0) = -1 EINVAL (Invalid argument)
```

Any advice or pointers towards further narrowing this down would be appreciated. Thanks!

---

## 评论 (9 条)

### 评论 #1 — jlgreathouse (2019-01-30T17:00:20Z)

Are you in the `video` group? What happens if you run `rocminfo` while you are root?

---

### 评论 #2 — CyberShadow (2019-01-30T17:00:54Z)

Sorry, forgot to mention I was running `rocminfo` as root.

---

### 评论 #3 — jlgreathouse (2019-01-30T17:11:27Z)

With the obvious check not fixing things, I must note that we do not technically offer official support for Arch in this repo. Our official support is limited to Ubuntu, RHEL, and CentOS.

That said, there are [community efforts](https://github.com/clapbr/arch-rocm/issues/1) to get ROCm working on Arch, so you mean want to check with them.

We have [open feature requests](https://github.com/RadeonOpenCompute/ROCm/issues/294) for ROCm to work on Arch, so I'm going to close this issue to prevent duplicates. Please keep an eye on those other issues for info on ROCm+Arch.

---

### 评论 #4 — CyberShadow (2019-01-30T17:12:30Z)

I don't see why this would be a distribution-specific issue, but your call. Thanks for your time.

---

### 评论 #5 — jlgreathouse (2019-01-30T17:31:38Z)

The error you're seeing from rocminfo means that "something in a very tall stack of software, firmware, and hardware did not work".

It could be a driver issue (I don't have time to dig into what Arch has backported into this release of 4.20), an issue with the Thunk or ROCR user-level software (I don't know where you got these, as we do not distribute binaries for Arch), system configuration (e.g. we normally require `/dev/kfd` to be in the `video` group so that it can get access to the GPU for normal users -- I don't personally know how Arch sets up the video subsystem to know whether there is something we need to change for user-level software to access the ROCm GPU resources).

Basically, hunting down exactly what's going on with your system has a high probability of going through a lot of system-specific software and configuration. Because we don't officially support Arch, there's not really any resources we can spend figuring our potentially Arch-specific problems with your setup.

---

### 评论 #6 — CyberShadow (2019-01-30T17:59:03Z)

No problem. But, for what it's worth, allow me to address some of those:

> I don't have time to dig into what Arch has backported into this release of 4.20

I'm happy to look into that for you:

```console
$ git log v4.20.3..v4.20.3-arch1
commit 352ffa235e4cd8c6aec04665e9ac46a6441130c8 (tag: v4.20.3-arch1)
Author: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
Date:   Wed Jan 16 23:02:50 2019 +0100

    Arch Linux kernel v4.20.3-arch1

commit 397c8073979b2a9be90b6059552cd53cfbee0e48
Author: Serge Hallyn <serge.hallyn@canonical.com>
Date:   Fri May 31 19:12:12 2013 +0100

    add sysctl to disallow unprivileged CLONE_NEWUSER by default
    
    Signed-off-by: Serge Hallyn <serge.hallyn@ubuntu.com>
    [bwh: Remove unneeded binary sysctl bits]
    Signed-off-by: Daniel Micay <danielmicay@gmail.com>
```

> an issue with the Thunk or ROCR user-level software (I don't know where you got these, as we do not distribute binaries for Arch),

I'm using the binary from the Docker container (I've tried running it inside the container, give the container the necessary privileges as documented, and running it directly). However, I don't see why that would matter, unless the `ioctl` interface is unstable.

> system configuration (e.g. we normally require `/dev/kfd` to be in the `video` group so that it can get access to the GPU for normal users -- I don't personally know how Arch sets up the video subsystem to know whether there is something we need to change for user-level software to access the ROCm GPU resources).

`/dev/kfd` is owned by `root:render` here, and my user is in the `render` group, but that shouldn't matter when running things with UID=0, right?

In any case, I'm happy to dig into things, especially if it means contributing something back or improving Arch support. I may try booting into a supported distribution and seeing if things work there; if so, it would be a matter of narrowing down the differences in the involved components.

---

### 评论 #7 — PetarKirov (2019-01-31T07:42:23Z)

In order to rule possible hardware issues out, you could boot into one of the supported distros and follow the official instructions. If say Ubuntu ends up working on your system, you could then try bisect the differences of the ROCm stack running there with your own Arch system.

Also, AFAIK, in contrast to other ROCm supported GPUs, Vega is special in that work on the firmware was done to support working on motherboards without PCIe atomics. Meaning that, (AFAIU) it should support a bit more CPU/Motherboard setups, so I don't see an obvious reason preventing you from running ROCm on a system with your hardware.
You should be able to find more info on that in some of the older issues in this repo.

---

### 评论 #8 — CyberShadow (2019-02-05T23:43:57Z)

> I may try booting into a supported distribution and seeing if things work there; if so, it would be a matter of narrowing down the differences in the involved components.

I've now done this. Here is what I learned:

- The "Call returned 4104" error is indeed very generic, and occurs even if `/dev/kfd` is completely missing.
  - `strace` is the first step towards narrowing down issues.
  - A troubleshooting checklist, diagnostic tool, or more verbose error messages might be worthwhile, considering how many issues have been filed so far with this single error message.
- There are a LOT of components and packages involved! Many more than I expected.
- The packages I had found for Arch Linux were all created by different users, and unsurprisingly things were packaged very differently than AMD's Ubuntu PPA. Looks like this ugly mess was what caused the error I had originally seen. Probably, any serious effort to package for Arch Linux will require close coordination and a single party managing all relevant packages.
- Fortunately, all relevant components are very neatly isolated in `/opt/rocm`. Mounting / copying this directory from an Ubuntu installation allows everything to work just fine from Arch Linux, even with the latest kernel / upstreamed drivers. The only other thing was the files in `/etc/ld.so.conf.d`, but they can be substituted by setting `LD_LIBRARY_PATH`.
- Still don't know why the Docker images didn't work, but as things work without Docker, at this point it is an unnecessary complication.

So, probably the easiest way to use ROCm on Arch Linux:
- Set up an Ubuntu 18.04 chroot
- Install the necessary packages there
- Bind-mount `/opt/rocm` from the chroot to the real system
- Ensure `/dev/kfd` is present and writable by the current user
- Copy all files mentioning `/opt/rocm` from `/etc/ld.so.conf.d/` from chroot to host system, then run `sudo ldconfig`
  **OR**
  run commands with e.g. 
  ```
  LD_LIBRARY_PATH=/opt/rocm/hiprand/lib:/opt/rocm/hsa-amd-aqlprofile/lib:/opt/rocm/hsa/lib:/opt/rocm/lib:/opt/rocm/libhsakmt/lib:/opt/rocm/opencl/lib/x86_64:/opt/rocm/rocprofiler/lib:/opt/rocm/rocrand/lib
   ```

There is [an issue with TensorFlow / Python 3.7](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/308), but using `pip2` / `python2` works for the time being.

With this, the Keras examples work! `addition_rnn.py` seems to be about 10x faster than on CPU for me.

---

### 评论 #9 — jlgreathouse (2019-02-06T00:19:25Z)

@CyberShadow Thanks for looking into this, and writing down the directions you followed to get a working ROCm installation going on your Arch installation. I apologize that I was unable to give you much guidance towards fixing this. As you've seen, there are a lot of moving parts, and my ignorance of Arch would probably have just wasted a bunch of your time.

That said, coming back to give your workarounds and steps are a big help to the community, so thank you very much. I hope that, eventually, we can get community-supported Arch installation directions moved into our distribution install scripts that are part of the [Experimental ROC project](https://github.com/RadeonOpenCompute/Experimental_ROC).

---
