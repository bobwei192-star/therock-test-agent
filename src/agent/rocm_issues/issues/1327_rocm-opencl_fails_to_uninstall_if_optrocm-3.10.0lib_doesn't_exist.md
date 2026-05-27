# rocm-opencl fails to uninstall if /opt/rocm-3.10.0/lib doesn't exist

> **Issue #1327**
> **状态**: closed
> **创建时间**: 2020-12-10T19:04:55Z
> **更新时间**: 2024-01-18T03:30:21Z
> **关闭时间**: 2024-01-18T03:30:21Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1327

## 描述

If a user accidental removed stuff in `/opt`, it should still be possible to uninstall stuff and reinstall them.

But `prerm` script fails.

```
Removing rocm-opencl (3.6Beta-17-g875c1f8-rocm-rel-3.10-27) ...
rmdir: failed to remove '/opt/rocm-3.10.0/lib': No such file or directory
dpkg: error processing package rocm-opencl (--remove):
 installed rocm-opencl package pre-removal script subprocess returned error exit status 1
dpkg: too many errors, stopping
```

Debian testing. But applies to Ubuntu too.


`/var/lib/dpkg/info/rocm-opencl.prerm`:

```bash
#!/bin/bash

set -e

rm_ldconfig() {
  rm -f /etc/ld.so.conf.d/x86_64-rocm-opencl.conf && ldconfig
  rm -f /etc/OpenCL/vendors/amdocl64_31000.icd
}

case "$1" in
  purge)
  ;;
  remove)
    rm -f /opt/rocm-3.10.0/lib/libOpenCL.so
    rm -f /opt/rocm-3.10.0/lib/libOpenCL.so.1
    rm -f /opt/rocm-3.10.0/lib/libOpenCL.so.1.2
    rmdir --ignore-fail-on-non-empty /opt/rocm-3.10.0/lib
    rmdir --ignore-fail-on-non-empty /opt/rocm-3.10.0
    rm_ldconfig
  ;;
  *)
    exit 0
  ;;
esac
```

I think adding `|| true` at the end of `rmdir` lines, maybe would be an option?

Also there is some not-so-pretty handling of some symlinks in `postinst`, that requires this ugly solution in `prerm`. A better way would be to embed these symlinks in the package content itself. This way it will also be removed automatically, and it will trigger `ldconfig` afaik automatically too (or can be configured to do so). It would simplify both `postinst` and `prerm`.


---

## 评论 (8 条)

### 评论 #1 — ROCmSupport (2020-12-11T06:28:11Z)

Thanks @baryluk for reaching out.
Let me work with Packaging team and get back to you asap.
Thank you.

---

### 评论 #2 — baryluk (2021-01-12T14:57:53Z)

FYI. Still the same in rocm 4.0


---

### 评论 #3 — ROCmSupport (2021-11-02T13:05:59Z)

Hi @baryluk 
Can you please check with the latest ROCm 4.5 and update.
Thank you.

---

### 评论 #4 — baryluk (2021-11-03T20:58:26Z)

@ROCmSupport  Still the same in ROCm 4.5

```
$ sudo rm -rf /opt/
$ sudo apt purge rocm-opencl
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  afl++-clang comgr hsa-rocr hsa-rocr-dev hsakmt-roct-dev rocm-core
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  rocm-opencl*
0 upgraded, 0 newly installed, 1 to remove and 305 not upgraded.
After this operation, 1,549 kB disk space will be freed.
Do you want to continue? [Y/n] 
(Reading database ... 906019 files and directories currently installed.)
Removing rocm-opencl (2.0.0.40500-56) ...
rmdir: failed to remove '/opt/rocm-4.5.0/lib': No such file or directory
dpkg: error processing package rocm-opencl (--remove):
 installed rocm-opencl package pre-removal script subprocess returned error exit status 1
dpkg: too many errors, stopping
abort-remove
Errors were encountered while processing:
 rocm-opencl
Processing was halted because there were too many errors.
E: Sub-process /usr/bin/dpkg returned an error code (1)
```


---

### 评论 #5 — ROCmSupport (2021-11-10T10:27:29Z)

I informed packaging team to prioritize this. Thank you.

---

### 评论 #6 — ROCmSupport (2022-02-08T10:03:43Z)

Hi @baryluk 
Good news, fix is made and its pushed.
Can you please check and update asap by verifying it on ROCm 4.5 or 4.5.x builds.
Thank you.

---

### 评论 #7 — tasso (2023-12-20T00:01:42Z)

Is this issue fixed with the latest ROCm?  If so, can you please close it?  Thanks!

---

### 评论 #8 — nartmada (2024-01-18T03:30:21Z)

Closing this ticket as there is no response from @baryluk.  Please re-open if this issue still exists with latest ROCm 6.0.0.  Thanks.

---
