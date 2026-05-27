# OpenCL shared library overrides signal handling

> **Issue #462**
> **状态**: closed
> **创建时间**: 2018-07-19T20:39:10Z
> **更新时间**: 2018-10-16T13:51:36Z
> **关闭时间**: 2018-10-16T13:51:36Z
> **作者**: alexey-morozov
> **标签**: Under Investigation, Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/462

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

Hi,

we have a problem to use ROCm (1.8.151) OpenCL shared library (Ubuntu 16.04.4 LTS) in our own development environment where we make use of POSIX signal handlers. When calling clGetPlatformIDs function the signal handling of our application process gets overridden that causes problems for the application and finally makes it crashing. A simple CPP example below demonstrates the problem. Are there any specific reasons for the shared library to override the signal handling of the loading process? How can we avoid that?

Thanks for help.

```
// test.cpp
#include <dlfcn.h>
#include <signal.h>
#include <stdio.h>

int main()
{
    auto lib = dlopen("/opt/rocm/opencl/lib/x86_64/libOpenCL.so", RTLD_LAZY);
    auto function = reinterpret_cast<int (*)(unsigned, void *, unsigned *)>(dlsym(lib, "clGetPlatformIDs"));

    unsigned n = 0;
    auto result = function(0, 0, &n); // this function call overrides the current process signal handling

    printf("generating int3 trap\r\n");

    asm("int3"); // normally this induces a trap but here the process will exit silently
}

// compilation: g++ -std=c++11 -o test test.cpp -ldl
// execution: ./test
```

---

## 评论 (7 条)

### 评论 #1 — gstoner (2018-07-20T14:42:07Z)

I have engineering looking at this.   They will be getting back to you about this 

---

### 评论 #2 — alexey-morozov (2018-08-25T18:16:07Z)

any news on the issue?

---

### 评论 #3 — jlgreathouse (2018-08-25T18:48:26Z)

We're tracking this internally. I believe we've identified the issue, and I have a _potential_ workaround that has not gone through review, validation, or testing.

Would you be willing to do a custom build of our OpenCL runtime, apply a highly experimental patch, and see if it fixes your issue without causing you any other problems?

---

### 评论 #4 — alexey-morozov (2018-08-26T07:17:53Z)

Yes, I'm willing to do that and waiting for instructions.

---

### 评论 #5 — jlgreathouse (2018-08-27T20:13:08Z)

Hi @alexey-morozov 

Could you try running the following commands to make a custom OpenCL build with a simple patch in place? Sorry for using sed to do this patch, :)

```shell
mkdir ~/test_opencl
cd ~/test_opencl
mkdir -p ~/bin
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git -b master -m opencl.xml
~/bin/repo sync
cd opencl
sudo apt-get install ocaml ocaml-findlib python-z3 git-svn
mkdir -p build && cd build
sed -i '353i  // In OpenCL applications that call LC, the end-user may want to receive' ../opencl/compiler/llvm/lib/Support/Unix/Signals.inc
sed -i '354i  // a signal that is sent asynchronously, and thus would not be re-raised' ../opencl/compiler/llvm/lib/Support/Unix/Signals.inc
sed -i '355i  // even after returning from the compilation path. Raise it here so that' ../opencl/compiler/llvm/lib/Support/Unix/Signals.inc
sed -i '356i  // the original handler is called.' ../opencl/compiler/llvm/lib/Support/Unix/Signals.inc
sed -i '357i  raise(Sig);' ../opencl/compiler/llvm/lib/Support/Unix/Signals.inc
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make -j `nproc`
```

At this point, you can try using this OpenCL runtime by putting the `~/test_opencl/opencl/build/lib` directory in your LD_LIBRARY_PATH. For example: `LD_LIBRARY_PATH=~/test_opencl/opencl/build/lib ./test`

---

### 评论 #6 — jlgreathouse (2018-10-10T19:20:34Z)

Hi @alexey-morozov 

Have you had a chance to try this yet?

---

### 评论 #7 — alexey-morozov (2018-10-16T13:51:36Z)

Hi @jlgreathouse 

Yes, I've tried it and our IDE still crashed. But we've found a workaround and I would consider the issue closed.

Thanks in any case!

---
