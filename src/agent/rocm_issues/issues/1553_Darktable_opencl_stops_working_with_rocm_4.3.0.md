# Darktable opencl stops working with rocm 4.3.0

> **Issue #1553**
> **状态**: closed
> **创建时间**: 2021-08-10T17:54:52Z
> **更新时间**: 2021-08-16T04:07:57Z
> **关闭时间**: 2021-08-16T04:07:56Z
> **作者**: Aceler
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1553

## 描述

4.1.0 worked fine. Here is the log from darktable-cltest:

[dt-cltest.txt](https://github.com/RadeonOpenCompute/ROCm/files/6963505/dt-cltest.txt)


---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-08-11T09:59:49Z)

Thanks @Aceler for reaching out.
Can you please share the exact steps to reproduce the problem.
So that I will check it locally and help you with all of the information.
Request you to share the outputs of **/opt/rocm/bin/rocminfo** and **/opt/rocm/opencl/bin/clinfo**
Thank you.

---

### 评论 #2 — Aceler (2021-08-11T12:01:31Z)

Sure.

One day I find out, that rocm debian/ubuntu repository is no longer works, because it moves from `https://repo.radeon.com/rocm/apt/debian/ **xenial** main` to `https://repo.radeon.com/rocm/apt/debian/ **ubuntu** main`.

I found instructions here: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu

They said, that I need a complete uninstallation of previous ROCm versions. So I removed rocm4.1.0, made a purge and installed a followed packages from the new place:
```
libnuma-dev
rocm-opencl
```
I also got several packages as a dependencies:
```
Start-Date: 2021-08-10  18:45:58
Commandline: apt-get -y install rocm-opencl
Requested-By: aceler (1000)
Install: hsa-rocr-dev:amd64 (1.3.0.40300-52, automatic), hsakmt-roct:amd64 (20210520.3.071986.40300-52, automatic), rocm-opencl:amd64 (2.0.0.40300-52), libelf-dev:amd64 (0.176-1.1build1, automatic), comgr:amd64 (2.1.0.40300-52, automatic)
End-Date: 2021-08-10  18:46:00
```

I use an upstream kernel, so `/etc/udev/rules.d/70-kfd.rules` is configured accordingly.

Then, I launched darktable-cltest and got this.

Darktable is installed from the official Darktable OBS: `https://software.opensuse.org/download.html?project=graphics:darktable&package=darktable`

Here are log files you asked for:
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6968174/clinfo.txt)
[romcinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6968175/romcinfo.txt)


---

### 评论 #3 — Aceler (2021-08-11T12:02:50Z)

And i forgot to mention that I am on Ubuntu 20.04 LTS.

---

### 评论 #4 — iszotic (2021-08-13T15:23:58Z)

Have you tried setting LD_LIBRARY_PATH='/opt/rocm/opencl/lib/'? that worked for me in blender

---

### 评论 #5 — ROCmSupport (2021-08-16T04:07:56Z)

Thank you much @Aceler for sharing all of the information and logs, really helpful to understand the problem better.
I got to know from the logs that its unable to generate executable from Intermediate representation of code: Error: **Creating the executable from LLVM IRs failed.**
The reason for this is that you are using a non-supported ROCm card which can not generate the executable/codes as expected.
You are using Ellesmere(gfx803), which is not supported by ROCm and hence code might not work.
Recommend to use a supported GPU, as per [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Hope this helps.
Feel free to open a new issue, if any, for fast resolution.
Thank you.


---
