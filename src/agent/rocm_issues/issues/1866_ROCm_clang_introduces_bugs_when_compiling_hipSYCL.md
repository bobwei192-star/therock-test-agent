# ROCm clang introduces bugs when compiling hipSYCL

> **Issue #1866**
> **状态**: closed
> **创建时间**: 2022-11-23T19:52:01Z
> **更新时间**: 2024-03-11T01:52:36Z
> **关闭时间**: 2024-03-11T01:52:36Z
> **作者**: misos1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1866

## 描述

**This problem does not happen when compiling with vanilla clang-15. It only happens when compiling with ROCm custom modified clang-15 included in ROCm installation (which is what is `hipcc` command actually invoking).**

ROCm clang compiler causes bugs which seem like some thread-safety problems in otherwise valid and well-working programs.

hipSYCL is built using `cmake -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm ..`.
This program is compiled using `syclcc --hipsycl-targets='hip:gfx900' -Ofast main.cpp`:
```
#include <sycl/sycl.hpp>

int main()
{
	sycl::queue q;
	while(true)
	{
		q.single_task([](){}).wait();
	}
}
```
Possible outcomes:
```
free(): corrupted unsorted chunks
Aborted (core dumped)
```
```
malloc(): unsorted double linked list corrupted
Aborted (core dumped)
```
```
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff5d96859 in __GI_abort () at abort.c:79
#2  0x00007ffff5e0126e in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff5f2b298 "%s\n") at ../sysdeps/posix/libc_fatal.c:155
#3  0x00007ffff5e092fc in malloc_printerr (str=str@entry=0x7ffff5f2dad8 "malloc(): unsorted double linked list corrupted") at malloc.c:5347
#4  0x00007ffff5e0c2ec in _int_malloc (av=av@entry=0x7ffff5f60b80 <main_arena>, bytes=bytes@entry=152) at malloc.c:3744
#5  0x00007ffff5e0e299 in __GI___libc_malloc (bytes=152) at malloc.c:3066
#6  0x00007ffff619db39 in operator new(unsigned long) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#7  0x00007ffff7d04e2c in hipsycl::rt::dag_builder::build_node(std::unique_ptr<hipsycl::rt::operation, std::default_delete<hipsycl::rt::operation> >, hipsycl::rt::requirements_list const&, hipsycl::rt::execution_hints const&) () from /usr/local/bin/../lib/libhipSYCL-rt.so
#8  0x00007ffff7d05d42 in hipsycl::rt::dag_builder::add_command_group(std::unique_ptr<hipsycl::rt::operation, std::default_delete<hipsycl::rt::operation> >, hipsycl::rt::requirements_list const&, hipsycl::rt::execution_hints const&) () from /usr/local/bin/../lib/libhipSYCL-rt.so
#9  0x00007ffff7d05e93 in hipsycl::rt::dag_builder::add_kernel(std::unique_ptr<hipsycl::rt::operation, std::default_delete<hipsycl::rt::operation> >, hipsycl::rt::requirements_list const&, hipsycl::rt::execution_hints const&) () from /usr/local/bin/../lib/libhipSYCL-rt.so
#10 0x0000000000213d43 in main ()
```

Nothing like that happens when is hipSYCL built using vanilla clang-15 (for example using `cmake -DLLVM_DIR=/usr/lib/llvm-15/cmake ..`).


---

## 评论 (5 条)

### 评论 #1 — ashutom (2022-11-25T06:11:52Z)

@misos1 ,  Should that not be a problem of `syclcc's runtime` ?

  

---

### 评论 #2 — alexschroeter (2023-01-06T20:08:43Z)

I tried your example with ROCm 5.3.3 and hipSYCL v0.9.3 and it works. Have you tried specifying the C/CXX Compiler with you hipSYCL installation?

cmake -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm/ -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang ..



---

### 评论 #3 — misos1 (2023-01-09T15:49:04Z)

> cmake -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm/ -DCMAKE_CXX_COMPILER=/opt/rocm/llvm/bin/clang++ -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang ..

I got the same results (crash).

I have ROCm 5.4.0 and hipSYCL from develop branch concretely commit https://github.com/illuhad/hipSYCL/commit/53937c6e908446bfd639a5e8ab7548e5f698b102

I also tested a combination of ROCm 5.4.0 and hipSYCL v0.9.3 and I still got crashes.


---

### 评论 #4 — abhimeda (2024-01-30T04:05:34Z)

@misos1  Hi, is this resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #5 — nartmada (2024-03-11T01:52:36Z)

Closing the ticket as no response from @misos1.  Please re-open if you still observe this issue in latest ROCm 6.0.2.  Thanks.

---
