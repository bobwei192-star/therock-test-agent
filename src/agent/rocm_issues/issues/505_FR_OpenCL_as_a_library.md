# FR: OpenCL as a library

> **Issue #505**
> **状态**: closed
> **创建时间**: 2018-08-19T23:02:41Z
> **更新时间**: 2018-08-24T00:25:32Z
> **关闭时间**: 2018-08-24T00:25:32Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/505

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I understand in the future ROCm may run on top of the standard Linux kernel, unmodified (i.e. without needing a kernel module).

In that situation, I imagine OpenCL as a library, that could be linked into / shipped with an application, that would allow the app to run on a supported Linux system without requiring installing ROCm there.


---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2018-08-23T23:29:37Z)

Hi @preda 

I'm not entirely sure I understand the request. Assuming that in the future most of the ROCm base layers (driver, KFD) are available in a standard Linux distro, you're looking to be able to do something like include libOpenCL.so (and libamdocl64.so, etc) as part of your application so that users don't need to separately install OpenCL?

You should be able to include libOpenCL.so / libamdocl64.so / etc. with your application right now. You may run into problems that any builds of these libraries are going to depend on other things like your libc version, so you may need to worry about what to do when running your application on different distros, versions, etc.

So I guess my confusion about this as a feature request is that OpenCL is "a library" already. :)

That said, I don't know if you'll be able to work with ROCm "out of the box" in that sense. You may need to include the ROCt thunk and ROCr runtime to allow OpenCL to interface to the kernel driver. These are both user-mode components, however.

---

### 评论 #2 — preda (2018-08-24T00:18:35Z)

I'm not familiar with ROCt thunk. From what I understand, it's the user-mode interface that pairs with the ROCk kernel component. If so, isn't ROCt dependent on the ROCk (i.e. changes in ROCk must be accompanied by changes to ROCt). If so, then the ROCt should be installed on a system together with ROCk as the two are paired (i.e. you can't install an arbitrary version of ROCt on top of some fixed ROCk).

So in the "OpenCL liked in as part of the app" scenario above, the ROCt would not be part of the app, but part of the system.

Maybe the ROCr (runtime), if it sits on top of some relatively stable API underneath (ROCt?), could be linked with the app and be considered part of the app.

Maybe this issue can be closed as "already working".


---

### 评论 #3 — gstoner (2018-08-24T00:23:59Z)

when we load an OpenCL package, OpenCL Runtime sits on ROCr, not the Thunk, What you want to do it have them load the particular OpenCL package and your application. you could just create meta package for Ubuntu for this.   We could look at statically linux openCL runtime/VDI layer to your app, remember we still have compiler as well. 

---

### 评论 #4 — gstoner (2018-08-24T00:25:32Z)

The issue right now you need ROCr and Thunk to support the OpenCL language runtime,  this is what talks to base AMDGPU Kernel driver and KFD. 

---
