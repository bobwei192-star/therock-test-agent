# Changing libstdcxx dependency in a minor version release is bad

> **Issue #2030**
> **状态**: closed
> **创建时间**: 2023-04-07T03:51:39Z
> **更新时间**: 2024-10-24T17:52:53Z
> **关闭时间**: 2024-10-24T17:52:35Z
> **作者**: ye-luo
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2030

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Just found out on SLES 15 SP3.
The amdclang shipped with rocm 5.4.0
```
ldd /soft/compilers/rocm/rocm-5.4.0/llvm/bin/clang++
	linux-vdso.so.1 (0x00007ffdc3a8d000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f97aa0cf000)
	librt.so.1 => /lib64/librt.so.1 (0x00007f97a9ec6000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007f97a9cc2000)
	libz.so.1 => /lib64/libz.so.1 (0x00007f97a9aab000)
	libtinfo.so.6 => /lib64/libtinfo.so.6 (0x00007f97a987d000)
	libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007f97a946a000)
	libm.so.6 => /lib64/libm.so.6 (0x00007f97a911f000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f97a8f06000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f97a8b11000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f97aa2f2000)
```
With rocm 5.4.3
```
ldd /soft/compilers/rocm/rocm-5.4.3/llvm/bin/clang++
/soft/compilers/rocm/rocm-5.4.3/llvm/bin/clang++: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /soft/compilers/rocm/rocm-5.4.3/llvm/bin/clang++)
	linux-vdso.so.1 (0x00007ffd15d9f000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fafdc84c000)
	librt.so.1 => /lib64/librt.so.1 (0x00007fafdc643000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007fafdc43f000)
	libz.so.1 => /lib64/libz.so.1 (0x00007fafdc228000)
	libtinfo.so.6 => /lib64/libtinfo.so.6 (0x00007fafdbffa000)
	libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007fafdbbe7000)
	libm.so.6 => /lib64/libm.so.6 (0x00007fafdb89c000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fafdb683000)
	libc.so.6 => /lib64/libc.so.6 (0x00007fafdb28e000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fafdca6f000)
```
The system gcc 7 is not qualified. What is the new requirement? It is gcc 12. That is a huge surprise.

The expectation is no major dependency change in a minor release. So please make it gcc 7 sufficient.
If a newer gcc is needed to build this clang or a later release, **make a conservative choice of gcc version and maximize compatibility**.

On my ubuntu 20.04, rocm clang++ is happy with gcc 9. I would assume the choice of gcc 12 in SLES is an oversight when packaging rocm 5.4.3. I have not checked 5.4.1 or 5.4.2 but please lower the version of gcc dependency.


---

## 评论 (2 条)

### 评论 #1 — ye-luo (2024-02-24T03:58:49Z)

@nartmada this was the source of the pain described https://github.com/ROCm/ROCm/issues/2084

---

### 评论 #2 — jamesxu2 (2024-10-24T17:52:35Z)

Hi @ye-luo, apologies for the delay in responding to your issue.

I think that the discussion in https://github.com/ROCm/ROCm/issues/2084 provided a justification for why the libstdc++ version was increased, though this still should not have gone out in a minor release.

> The expectation is no major dependency change in a minor release. 

We do have internal rules to prevent breaking changes in minor/patch releases, and it seems that in this case we missed that check. I understand your frustration in encountering a breaking change in a minor release and we apologize for the pain that's caused. Thanks for your feedback.



---
