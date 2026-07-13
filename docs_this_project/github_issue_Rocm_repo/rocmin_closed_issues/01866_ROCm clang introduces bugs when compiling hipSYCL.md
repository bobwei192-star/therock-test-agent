# ROCm clang introduces bugs when compiling hipSYCL

- **Issue #:** 1866
- **State:** closed
- **Created:** 2022-11-23T19:52:01Z
- **Updated:** 2024-03-11T01:52:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/1866

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
