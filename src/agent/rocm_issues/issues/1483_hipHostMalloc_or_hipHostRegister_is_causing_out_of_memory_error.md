# hipHostMalloc or hipHostRegister is causing out of memory error.

> **Issue #1483**
> **状态**: closed
> **创建时间**: 2021-05-28T05:32:27Z
> **更新时间**: 2021-07-01T05:38:31Z
> **关闭时间**: 2021-07-01T05:38:31Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1483

## 描述

On MI-25, hipMalloc is OK, but I see hipHostRegister returns 2 which by definition appears to be:
hipErrorOutOfMemory 

looking at /root/ROCm-4.2/HIP/build/include/hip/hip_runtime_api.h
typedef enum __HIP_NODISCARD hipError_t {
    hipSuccess = 0,  ///< Successful completion.
    hipErrorInvalidValue = 1,  ///< One or more of the parameters passed to the API call is NULL
                               ///< or not in an acceptable range.
    hipErrorOutOfMemory = 2,

Here is the code compiled by hipcc <filename> on ROCm4.2 installed Ubuntu 1804 machine:
```

#include <stdio.h>
#include <stdbool.h>
#include "hip/hip_runtime.h"

#define ALLOC_NORMAL 1
#define ALLOC_PAGE_LOCKED 2
#define SIZE (10*1024*1024)

float hip_mem_alloc_test(int size, bool up, int allocType) {
    int debug = 0, stat = 0;
    hipEvent_t start, stop;
    int *a, *dev_a;
    float elapsedTime;

    if (debug) {
        printf("hip_mem_alloc_test: entered.\n");
        printf("creating events...");
    }

    hipEventCreate( &start);
    hipEventCreate( &stop);

    if (debug)
        printf("allocating on host...");

    if (allocType == ALLOC_PAGE_LOCKED) {
        stat = hipHostRegister((void**)&a, size * sizeof(*a), hipHostRegisterDefault);
        if (stat != hipSuccess) {
            printf("Err: hipHostRegister failed with code: %d.", stat);
            return 0;
        }
        hipHostMalloc((void**)&a, size * sizeof(*a), hipHostRegisterDefault);
        if (stat != hipSuccess) {
            printf("Err: hipHostMalloc failed with code: %d.", stat);
            return 0;
        }
    } else if  (allocType == ALLOC_NORMAL ) {
        a = (int*) malloc(size*sizeof(a));
    }

    if (debug)
        printf("allocating on gpu...");

    hipMalloc((void**)&dev_a, size * sizeof(&dev_a));

    hipEventRecord( start, 0);
    for (int i = 0; i < 100 ; i ++ ) {
        if (up) {
            hipMemcpy(dev_a, a, size * sizeof(a), hipMemcpyHostToDevice);
        } else {
            hipMemcpy(a, dev_a, size * sizeof(a), hipMemcpyDeviceToHost);
        }

    }
    hipEventRecord(stop, 0);
    hipEventSynchronize(stop);
    hipEventElapsedTime( &elapsedTime, start, stop);
    return elapsedTime;
}

int main()
{
    float elapsedTime;
    printf("main: entered.\n");

    float MB  = (float)100 * SIZE * sizeof(int) / 1024 / 1024;
    elapsedTime = hip_mem_alloc_test(SIZE, true, ALLOC_NORMAL);
    printf("Time using hipMalloc: %3.1f ms.\n", elapsedTime);
    printf("\tMB/s during copy up: %3.1f.\n", MB / (elapsedTime / 1000));

    elapsedTime = hip_mem_alloc_test(SIZE, false, ALLOC_NORMAL);
    printf("Time using hipMalloc: %3.1f ms.\n", elapsedTime);
    printf("\tMB/s during copy down: %3.1f.\n", MB / (elapsedTime / 1000));

    elapsedTime = hip_mem_alloc_test(SIZE, true, ALLOC_PAGE_LOCKED);
    if (elapsedTime != 0) {
        printf("Time using hipHostMalloc: %3.1f ms.\n", elapsedTime);
        printf("\tMB/s during copy up: %3.1f.\n", MB / (elapsedTime / 1000));
    } else {
        printf("Returned 0...\n");
    }

    elapsedTime = hip_mem_alloc_test(SIZE, false, ALLOC_PAGE_LOCKED);
    if (elapsedTime != 0) {
        printf("Time using hipHostMalloc: %3.1f ms.\n", elapsedTime);
        printf("\tMB/s during copy down: %3.1f.\n", MB / (elapsedTime / 1000));
    } else {
        printf("Returned 0...\n");
    }

}

```

With resulting output being:
```

main: entered.
Time using hipMalloc: 1211.5 ms.
        MB/s during copy up: 3301.8.
Time using hipMalloc: 1152.7 ms.
        MB/s during copy down: 3470.1.
Err: hipHostRegister failed with code: 2.Returned 0...
Err: hipHostRegister failed with code: 2.Returned 0...
root@guest:/git.co/dev-learn/rocm/hip/cuda-conversion/p188#

```

---

## 评论 (9 条)

### 评论 #1 — ROCmSupport (2021-06-04T06:53:49Z)

Thanks @gggh000 for reaching out.
I will take a quick look and update you.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-06-04T07:00:49Z)

Hi @gggh000 
Can you please share the exact steps you followed to replicate the same.
Thank you.

---

### 评论 #3 — gggh000 (2021-06-04T18:21:23Z)

it is pretty simple. with rocm4.2 installed and hipcc build and installed (also 4.2), I built the small benchmark utility above:
hipcc <filename>; ./a.out

---

### 评论 #4 — ROCmSupport (2021-06-15T06:36:37Z)

Hi @gggh000 
Not able to generate properly.
Do we need to add any flags? Can you please share your exact command line to generate the executable to run the program, which is helpful for me.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-06-18T05:09:46Z)

Hi @gggh000 
I resolved local issue and am able to compile the code successfully now.
Executed it and able to reproduce the issue like you.

taccuser@taccuser-GA-990FXA-UD5:~$ ./sample
main: entered.
Time using hipMalloc: 3420.7 ms.
        MB/s during copy up: 1169.3.
Time using hipMalloc: 1736.7 ms.
        MB/s during copy down: 2303.2.
**Err: hipHostRegister failed with code: 2.Returned 0...
Err: hipHostRegister failed with code: 2.Returned 0...**



---

### 评论 #6 — ROCmSupport (2021-06-18T10:38:40Z)

I am able to reproduce with 4.0 and 4.1 also.

So when I run the application with log level, feels like **its mostly an application issue** as its not able to allocate memory.
Please check the source once.


:3:hip_event.cpp            :249 : 0853955870 us: 3463 : [7fd907a1e880] hipEventElapsedTime: Returned hipSuccess : Elapsed Time = , 1143.34
Time using hipMalloc: 1143.3 ms.
        MB/s during copy down: 3498.5.
:3:hip_event.cpp            :218 : 0853955877 us: 3463 : [7fd907a1e880] hipEventCreate ( 0x7ffe97a79c48 )
:3:hip_event.cpp            :220 : 0853955881 us: 3463 : [7fd907a1e880] hipEventCreate: Returned hipSuccess : event:0xefc880
:3:hip_event.cpp            :218 : 0853955885 us: 3463 : [7fd907a1e880] hipEventCreate ( 0x7ffe97a79c30 )
:3:hip_event.cpp            :220 : 0853955887 us: 3463 : [7fd907a1e880] hipEventCreate: Returned hipSuccess : event:0xefc910
:3:hip_memory.cpp           :702 : 0853955894 us: 3463 : [7fd907a1e880] hipHostRegister ( 0x7ffe97a79c28, 41943040, 0 )
**:1:rocdevice.cpp            :1692: 0853955992 us: Failed creating memory
:1:memory.cpp               :328 : 0853955996 us: Video memory allocation failed!
:1:memory.cpp               :292 : 0853955998 us: Can't allocate memory size - 0x02800000 bytes!
:3:hip_memory.cpp           :713 : 0853956016 us: 3463 : [7fd907a1e880] hipHostRegister: Returned hipErrorOutOfMemory :
Err: hipHostRegister failed with code: 2.Returned 0...
:3:hip_event.cpp            :218 : 0853956023 us: 3463 : [7fd907a1e880] hipEventCreate ( 0x7ffe97a79c48 )
:3:hip_event.cpp            :220 : 0853956026 us: 3463 : [7fd907a1e880] hipEventCreate: Returned hipSuccess : event:0xefcbf0
:3:hip_event.cpp            :218 : 0853956029 us: 3463 : [7fd907a1e880] hipEventCreate ( 0x7ffe97a79c30 )
:3:hip_event.cpp            :220 : 0853956032 us: 3463 : [7fd907a1e880] hipEventCreate: Returned hipSuccess : event:0xefcc80
:3:hip_memory.cpp           :702 : 0853956037 us: 3463 : [7fd907a1e880] hipHostRegister ( 0x7ffe97a79c28, 41943040, 0 )
:1:rocdevice.cpp            :1692: 0853956064 us: Failed creating memory
:1:memory.cpp               :328 : 0853956068 us: Video memory allocation failed!
:1:memory.cpp               :292 : 0853956070 us: Can't allocate memory size - 0x02800000 bytes!
:3:hip_memory.cpp           :713 : 0853956075 us: 3463 : [7fd907a1e880] hipHostRegister: Returned hipErrorOutOfMemory :
Err: hipHostRegister failed with code: 2.Returned 0...**


---

### 评论 #7 — gggh000 (2021-06-18T17:19:33Z)

after rocm 4.3 installed it appears to working. at least not crashing. 

---

### 评论 #8 — ROCmSupport (2021-06-23T04:56:39Z)

Thanks @gggh000 for the latest observations.
But ROCm 4.3 is not released yet and did you try with 4.2 or some other rocm version?
Please confirm.

And also can you please clarify whether you have made any changes to the source code so that app starts working?
Please share.

Thank you.

---

### 评论 #9 — ROCmSupport (2021-07-01T05:38:31Z)

I am closing this now as the issue is fixed with the latest ROCm 4.2
Thank you.

---
