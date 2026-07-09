# [Issue]: Segmentation fault after several seconds of run time while looping a kernel that uses the "new" operator

- **Issue #:** 5726
- **State:** closed
- **Created:** 2025-11-30T07:16:32Z
- **Updated:** 2025-12-29T03:26:08Z
- **Labels:** status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5726

### Problem Description

I kept getting a segfault when looping a kernel, that contained a `new` operator, multiple times. Whenever my program ran for around 7-10 seconds, it stopped, with a segmentation fault in the `amdhip64_6.dll` file. Oddly, the number of times that I executed the kernel didn't seem to matter. If I hard-coded a one second delay between separate kernel executions, it would execute 8 or 9 times before stopping. If I used a two second delay instead, it would execute 4 or 5 times, but still give a segmentation fault after the same amount of run time. This issue only occurs when using the `new` operator in the kernel; as soon as I stop using `new`, the code finishes executing without an error, but even a single `new` causes it to crash. (Even something like `double* x = new double(2)` causes a crash.) Running the same code as in the kernel, but on the host instead, works fine.

I'm curious why this is, as the HIP documentation states that device memory ["can also be allocated within a kernel using `malloc` or `new`."](https://rocmdocs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/device_memory.html#device-memory)
For context, I am relatively new to coding with HIP and C++ in general so I am not sure if this actually is a bug. **If it is intended/not a bug, I am sorry for reporting it as one**, and I would love to learn why this error occurs. However, this definitely seems like unintended behavior to me.

The code below causes a segmentation fault after around 7-10 seconds of run time, regardless of how many times the kernel is actually executed. The segmentation fault does not occur if the array is allocated with `arr[3]` as opposed to using the `new` operator. The error also still occurs when using `delete[]` to deallocate `arr` after executing the kernel.

### Operating System

Windows 11 10.0.26100

### CPU

AMD Ryzen 7 8845HS w/ Radeon 780M Graphics

### GPU

AMD Radeon 780M Graphics

### ROCm Version

ROCm 6.2

### ROCm Component

HIP

### Steps to Reproduce

Loop a kernel, that uses the `new` operator to allocate memory, at least 10 times with a second-long pause between each kernel execution.

Here are steps for recreating the error:

Save as `Main.hip`:
```
#include <hip/hip_runtime.h>
#include <thread>
#include <iostream>

__global__ void new_allocation() {
    double* arr = new double[3];
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;
    printf("\n%f, %f, %f", arr[0], arr[1], arr[2]);
}

int main() {
    for (int i = 0; i < 30; i++) {
        new_allocation<<<1, 1, 0, hipStreamDefault>>>();
        hipDeviceReset();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    return 0;
}
```


Then run this file using the following commands (replace `gfx1103` with your own GPU's architecture).

Compile with:
`hipcc -o a.exe -w --offload-arch=gfx1103 -mprintf-kind=buffered Main.hip`

and run with:
`.\a.exe`


My batch file for compiling and running looks like this:
```
call hipcc -o a.exe -w --offload-arch=gfx1103 -mprintf-kind=buffered Main.hip
.\a.exe
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

This is the stack trace of the segmentation fault that I get when running the code:
```
Exception Code: 0xC0000005
#0 0x00007ffa36f7728a (C:\WINDOWS\SYSTEM32\amdhip64_6.dll+0x41728a)
#1 0x00007ffa36f95175 (C:\WINDOWS\SYSTEM32\amdhip64_6.dll+0x435175)
#2 0x00007ffa36ee99ef (C:\WINDOWS\SYSTEM32\amdhip64_6.dll+0x3899ef)
#3 0x00007ffa36ea767f (C:\WINDOWS\SYSTEM32\amdhip64_6.dll+0x34767f)
#4 0x00007ffadf56e8d7 (C:\WINDOWS\System32\KERNEL32.DLL+0x2e8d7)
#5 0x00007ffadf80c53c (C:\WINDOWS\SYSTEM32\ntdll.dll+0x8c53c)
```

Additionally, WinDBG shows this when the segmentation fault occurs:
```
(7d4.5b84): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
amdhip64_6!hipHccModuleLaunchKernel+0xd2ffa:
00007ffa`2715728a 488b5808        mov     rbx,qword ptr [rax+8] ds:00000003`04200008=????????????????
0:005> g
```