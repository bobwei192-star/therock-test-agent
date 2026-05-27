# With version 2.9 of rocm and Ubuntu 18.04 hipMalloc has a seg fault allocating a struct member.

> **Issue #905**
> **状态**: closed
> **创建时间**: 2019-10-09T19:13:27Z
> **更新时间**: 2023-12-13T10:23:27Z
> **关闭时间**: 2023-12-13T10:23:26Z
> **作者**: ncr0zier
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/905

## 描述

The line where hipMalloc is being used to allocate a struct member has a segmentation fault under rocm 2.9, but previously worked under the last several versions of ROCm.

#define PIXELS_PER_LINE 1024
#define LINE_BYTES_UINT32 PIXELS_PER_LINE   * sizeof(uint32_t)

struct BaselineData
{
    uint32_t* minLine;
};

void initBaselineData_d(struct BaselineData *& data)
{
  std::cout << "HIP_CHECK(hipMalloc(&data,sizeof(struct BaselineData)));"         << std::endl;
  HIP_CHECK(hipMalloc(&data,sizeof(struct BaselineData)));
  std::cout << "HIP_CHECK(hipMalloc(&(data->minLine), LINE_BYTES_UINT32));"       << std::endl;
HIP_CHECK(hipMalloc(&(data->minLine), LINE_BYTES_UINT32));
}

---

## 评论 (5 条)

### 评论 #1 — ghost (2019-10-10T12:42:06Z)

Hi there,
I have tried to the similar scenario and found no issue on rocm 2.9 with gfx803 and gfx906 .
For further investigation, could you please provide us the following details:
1) Config details(gpu, motherboard,etc)
2) environment setting if any
3) If possible could you provide us the code to have a look into
4) I have tried, the following code, you may as well modify and give which can repro the issue


#include<iostream>

#include "hip/hip_runtime.h"
#include "hip/hip_runtime_api.h"

using namespace std;

#define HIPCHECK(error)\
    {  \
        hipError_t localError = error;   \
        if ((localError != hipSuccess)){ \
          printf("Error received is: %s",hipGetErrorString(localError));} \
    }



struct Exp
{
uint32_t *val;
};

void Alloc_mem(Exp *&);

int main()
{
void *ptr;
cout<<"Size of struct Exp is: "<<sizeof(Exp)<<endl;
Exp *strt_ptr;
Alloc_mem(strt_ptr);


}


void Alloc_mem(struct Exp *&ptr)
{

HIPCHECK(hipMalloc(&ptr,sizeof(struct Exp)));

cout<<"ptr-val: "<<ptr->val<<endl;
HIPCHECK(hipMalloc(&(ptr->val), sizeof(uint32_t)*1024));
cout<<"ptr-val: "<<ptr->val<<endl;
}




---

### 评论 #2 — ncr0zier (2019-10-10T14:33:41Z)

1. gfx900, Gigabyte Z370, 8700k.
2. I didn't make any changes to the rocm environment after it was installed.
3. (Put this here because of GitHub formatting)
4. I made some changes to what you posted so it would compile and I got a seg fault at the same place, allocating memory for a struct member.

#include "hip/hip_runtime.h"
#include "hip/hip_runtime_api.h"

using namespace std;

#define HIPCHECK(error) \\
{ \\
    hipError_t localError = error; \\
    if ((localError != hipSuccess)){  \\
      printf("Error received is: %s",hipGetErrorString(localError));} \\
}

struct Exp
{
  uint32_t *val;
};

void Alloc_mem(Exp *&);

int main()
{
  void *ptr;
  cout<<"Size of struct Exp is: "<<sizeof(Exp)<<endl;
  Exp *strt_ptr;
  Alloc_mem(strt_ptr);
  return 0;
}

void Alloc_mem(struct Exp *&ptr)
{
  HIPCHECK(hipMalloc(&ptr,sizeof(struct Exp)));
  cout << "ptr-val: " << ptr->val << endl;
  HIPCHECK(hipMalloc(&(ptr->val), sizeof(uint32_t)*1024));
  cout << "ptr-val: " << ptr->val << endl;
}

---

### 评论 #3 — ghost (2019-10-11T08:00:36Z)

I have tried on my local setup with gfx900 both single and multi gpu config but could not repro the issue.
We are keen to address the issue, for which could you please let us know the following:
1) Did u install rocm2.9 on fresh OS? If upgraded, from which version to rocm2.9
2) Did u upgrade your OS after installing the rocm2.9 driver?
3) In your earlier  message you said that you did small changes in the code I provided, could you please paste the modified code you used to repro the issue bcz I could not find much of a difference in the code you pasted in the last message.

---

### 评论 #4 — ncr0zier (2019-10-12T03:29:13Z)

I upgraded from rocm 2.8 to 2.9. It wasn't a clean install. I installed a lot of updates at the same time I installed rocm 2.9. The code I used was posted in my second second in this thread. I had to make changes because what you posted had syntax errors.

---

### 评论 #5 — nartmada (2023-12-12T23:14:27Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.

---
