# Support Ubuntu 21.04 (Hirsute Hippo)

> **Issue #1460**
> **状态**: closed
> **创建时间**: 2021-04-25T17:02:01Z
> **更新时间**: 2021-09-08T14:36:10Z
> **关闭时间**: 2021-04-25T17:05:59Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1460

## 描述

The version [21.04 (Hirsute Hippo) of Ubuntu is now current](https://lists.ubuntu.com/archives/ubuntu-announce/2021-April/000268.html) and should therefore be supported.

---

## 评论 (15 条)

### 评论 #1 — Bengt (2021-04-25T17:03:59Z)

... but it won't:

> ROCm officially supports LTS versions of Ubuntu only.
> All other versions(other than LTS) might work with ROCm but there will not be any official support.

Source: https://github.com/RadeonOpenCompute/ROCm/issues/1263#issuecomment-720264016

---

### 评论 #2 — ROCmSupport (2021-04-26T02:39:29Z)

Thanks @Bengt for reaching out.
Yes, ROCm officially supports LTS versions of Ubuntu only.
Thank you.

---

### 评论 #3 — Bengt (2021-04-26T11:04:19Z)

Thanks, @ROCmSupport for confirming the status quo of the support. I hope this issue helps others in searching for this information.

---

### 评论 #4 — Dan-RAI (2021-05-17T15:54:37Z)

Did someone manage to get it running under 21.04 ? 

I tried using the Kernel drivers and rocm-dev + rock-dkms-firmware only and had some initial success. However, after another update and reboot it is not working anymore, and so far I did not succeed in getting it back into working order:

[    1.426118] [drm] amdgpu kernel modesetting enabled.
[    1.427051] amdgpu: Ignoring ACPI CRAT on non-APU system
[    1.427342] amdgpu: Topology: Add CPU node
[    1.427536] amdgpu 0000:2f:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[    1.427548] amdgpu 0000:2f:00.0: amdgpu: Fatal error during GPU init
[    1.428245] amdgpu: probe of 0000:2f:00.0 failed with error -12






---

### 评论 #5 — Dan-RAI (2021-05-19T10:58:56Z)

Ok, I found the problem:

SR-IOV support needs to be disabled in BIOS. 

After this the Kernel amdgpu driver works together with rocm-dev under Ubuntu 21.04  



---

### 评论 #6 — erkinalp (2021-06-24T08:21:50Z)

Precompiled packages fail due to dependency on missing Python 3.8.

---

### 评论 #7 — Bengt (2021-06-24T09:49:02Z)

@erkinalp That sounds interesting. Please file a new issue about that.

---

### 评论 #8 — erkinalp (2021-06-24T09:59:01Z)

@Bengt That issue is specific to 21.04, which is unsupported.

---

### 评论 #9 — Bengt (2021-06-24T10:17:44Z)

Still, a documentation of the issue you are having would be nice to have for debugging and discussing workarounds. So, in any case, please provide details either here or in a separate issue.

---

### 评论 #10 — xuhuisheng (2021-06-24T10:21:22Z)

@erkinalp
Which package report python3.8 error? I think I can try investigating.

---

### 评论 #11 — erkinalp (2021-06-24T11:06:16Z)

@xuhuisheng `rocm-gdb` depends on `libpython3.8`, which does not exist on 21.04. The earliest Python 3 version available on Ubuntu 21.04 is Python 3.9.

---

### 评论 #12 — Dan-RAI (2021-06-24T15:49:20Z)

just compile and install python3.8 by hand ... ( I have rocm running under 21.04 )

---

### 评论 #13 — erkinalp (2021-06-24T16:31:23Z)

I would rather port `rocm-gdb` to Python 3.9 instead. Because Python 3.8 will is not going to exist in 22.04 anyway.

---

### 评论 #14 — xuhuisheng (2021-06-24T16:45:19Z)

The rocm-gdb is not a key component. Actually we can run pytorch / tensorflow without it. But the rocm-devs contains a dependency to rocm-gdb.
It didn't provide a cmakefiles.txt, so I didn't know how to create a deb package from source.
Should we build the source codes with configure/make, and make deb manually?

---

### 评论 #15 — almereyda (2021-09-04T23:04:32Z)

@Dan-RAI Could you offer more details of your installation procedure? I'm wondering, because I'm not sure if you used a packaged ROCm ([4.2 for pytorch on Docker](https://www.amd.com/en/technologies/infinity-hub/pytorch)), or compiled it by yourself (at a specific version tag?) to omit the `apt` warning:

```shell
$ apt install rocm-dkms
...
Die folgenden Pakete haben unerfüllte Abhängigkeiten:
 rocm-gdb : Hängt ab von: libpython3.8 ist aber nicht installierbar
E: Probleme können nicht korrigiert werden, Sie haben zurückgehaltene defekte Pakete.
```

Above, you also spoke about `rocm-dev`, yet that also depends on `rocm-gdb` and trying to install it yields the same error.

Eventually it is possible to work around `apt` altogether, by building and running Python3.8 and ROCm completely from source?

---

Following some [specific instructions for installing Python 3.8 via a PPA on Ubuntu 21.04](https://brennan.io/2021/06/21/deadsnakes-hirsute/) and with [package pinning](https://gist.github.com/JPvRiel/8ae81e21ce6397a0502fedddca068507) of certain other `bionic` packages, which this version depends upon, `rocm-dev` installs.

<details>

<summary>`/etc/apt/sources.list.d/rocm.list`</summary>

```
deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.3.1/ ubuntu main
```

</details>

<details>

<summary>`/etc/apt/sources.list.d/deadsnakes.list`</summary>

```
deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu/ focal main
deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu/ bionic main
```

</details>

<details>

<summary>`/etc/apt/sources.list.d/bionic.list`</summary>

```
deb [ arch=amd64 ] http://de.archive.ubuntu.com/ubuntu/ bionic main
```

</details>

<details>

<summary>`/etc/apt/preferences.d/preferences`</summary>

```
Explanation: Prevent installing from deadsnakes repo.
Package: *
Pin: release o=LP-PPA-deadsnakes
Pin-Priority: -1

Explanation: Allow installing python 3.{6,7} from deadsnakes/focal
Package: *python3.6* *python3.7*
Pin: release o=LP-PPA-deadsnakes,n=focal
Pin-Priority: 500

Explanation: Allow installing python 3.8 from deadsnakes/bionic
Package: *python3.8*
Pin: release o=LP-PPA-deadsnakes,n=bionic
Pin-Priority: 500

Package: *
Pin: release n=bionic
Pin-Priority: -1

Package: *libffi6* *libmpdec2* *libreadline7*
Pin: release n=bionic
Pin-Priority: 500
```

</details>

```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3B4FE6ACC0B21F32
apt update
apt install rocm-dev
```

---

Verify with:

```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```

---

Which, after rebooting, results in a system stuck in `vga` mode, with no `amdgpu` present anymore.

```
# root @ ganglion in ~ [16:26:28] C:130
$ dmesg | rg amdgpu  

# root @ ganglion in ~ [16:26:34] C:1
```

`apt remove 'rocm*' libffi6 libmpdec2 libreadline7 python3.8 && apt autoremove` is our friend, then.

---
