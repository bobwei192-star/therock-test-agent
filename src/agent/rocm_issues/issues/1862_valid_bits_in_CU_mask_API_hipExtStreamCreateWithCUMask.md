# valid bits in CU mask API hipExtStreamCreateWithCUMask

> **Issue #1862**
> **状态**: closed
> **创建时间**: 2022-11-19T03:17:47Z
> **更新时间**: 2023-01-16T21:17:15Z
> **关闭时间**: 2023-01-16T21:17:14Z
> **作者**: horrorChen
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1862

## 描述

I am trying to figure out which bit in cuMask array is valid. In the [head file](https://github.com/ROCm-Developer-Tools/HIP/blob/develop/include/hip/hip_runtime_api.h#:~:text=hipError_t%20hipExtStreamCreateWithCUMask(hipStream_t*%20stream%2C%20uint32_t%20cuMaskSize%2C%20const%20uint32_t*%20cuMask)%3B) of HIP, the annotation says the front bits work.

```cpp
/**
 * @brief Create an asynchronous stream with the specified CU mask.
 *
 * @param[in, out] stream Pointer to new stream
 * @param[in ] cuMaskSize Size of CU mask bit array passed in.
 * @param[in ] cuMask Bit-vector representing the CU mask. Each active bit represents using one CU.
 * The first 32 bits represent the first 32 CUs, and so on. If its size is greater than physical
 * CU number (i.e., multiProcessorCount member of hipDeviceProp_t), the extra elements are ignored.
 * It is user's responsibility to make sure the input is meaningful.
 * @return #hipSuccess, #hipErrorInvalidHandle, #hipErrorInvalidValue
 *
 * Create a new asynchronous stream with the specified CU mask.  @p stream returns an opaque handle
 * that can be used to reference the newly created stream in subsequent hipStream* commands.  The
 * stream is allocated on the heap and will remain allocated even if the handle goes out-of-scope.
 * To release the memory used by the stream, application must call hipStreamDestroy.
 *
 *
 * @see hipStreamCreate, hipStreamSynchronize, hipStreamWaitEvent, hipStreamDestroy
 */
hipError_t hipExtStreamCreateWithCUMask(hipStream_t* stream, uint32_t cuMaskSize, const uint32_t* cuMask);
```

But by my experiment testing matrix multiply on gfx906 which has 60 CUs, the performance of case I use mask1 is near to mask2, as well as half of mask3. As a result I think the valid bits are `{0xffffffff, 0x0fffffff}` rather than `{0xffffffff, 0xfffffff0}`.
```cpp
    uint32_t mask1[2] = {0xf0000000, 0xf0000000};    // 2 * f
    uint32_t mask2[2] = {0xf0000000, 0x00000000};    // 1 * f
    uint32_t mask3[2] = {0xf0000000, 0x0000000f};    // 2 * f
```

The same question of gfx908 which has 120 CUs, are the CUs corresponding to the following CU mask?
```cpp 
    uint32_t mask[4] = {0xffffffff, 0xffffffff, 0xffffffff, 0x00ffffff};
```

Thank you very much!

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2023-01-14T00:05:14Z)

Hi @horrorChen -- I believe the comment is correct, though perhaps things appear a bit confusing due to endianness of the code you're writing.

Your `mask1` array initialization sets bits 28-31 of the first uint32_t in the array, and bits 28-31 of the second uint32_t in the array. If you start counting from the lowest-order bit of the lowest entry in the array, this means that you have bits 28-31 and 60-63 set in `mask1`. Because you only have 60 CUs, the mask only ends up using bits 28-31. In the 4-shader-engine gfx906, this ends up enabling SE0:CU7, SE1:CU7, SE2:CU7, and SE3:CU7.

Your `mask2` array initialization sets bits 28-31 of the first uint32_t in the array. Like above, this enables SE0:CU7, SE1:CU7, SE2:CU7, and SE3:CU7.

Your `mask3` array initialization sets bits 28-31 of the first uint32_t in the array, and bits 0-3 of the second uint32_t in the array. Again counting from the lowest-order bit of the lowest entry in the array, this means you have bits 28-35 set in `mask3`. With a 60 CU gfx906, you now have 8 CUs enabled: SE0:CU7-8, SE1:CU7-8, SE2:CU7-8, and SE3:CU7-8, 

Because both `mask1` and `mask2` contain 4 active CUs and `mask3` contains 8 active CUs, I think your performance results make sense.

Your mask for gfx908 appears to be correct for a fully-enabled 120 CU gfx908.

---

### 评论 #2 — horrorChen (2023-01-14T05:52:05Z)

> Hi @horrorChen -- I believe the comment is correct, though perhaps things appear a bit confusing due to endianness of the code you're writing.
> 
> Your `mask1` array initialization sets bits 28-31 of the first uint32_t in the array, and bits 28-31 of the second uint32_t in the array. If you start counting from the lowest-order bit of the lowest entry in the array, this means that you have bits 28-31 and 60-63 set in `mask1`. Because you only have 60 CUs, the mask only ends up using bits 28-31. In the 4-shader-engine gfx906, this ends up enabling SE0:CU7, SE1:CU7, SE2:CU7, and SE3:CU7.
> 
> Your `mask2` array initialization sets bits 28-31 of the first uint32_t in the array. Like above, this enables SE0:CU7, SE1:CU7, SE2:CU7, and SE3:CU7.
> 
> Your `mask3` array initialization sets bits 28-31 of the first uint32_t in the array, and bits 0-3 of the second uint32_t in the array. Again counting from the lowest-order bit of the lowest entry in the array, this means you have bits 28-35 set in `mask3`. With a 60 CU gfx906, you now have 8 CUs enabled: SE0:CU7-8, SE1:CU7-8, SE2:CU7-8, and SE3:CU7-8,
> 
> Because both `mask1` and `mask2` contain 4 active CUs and `mask3` contains 8 active CUs, I think your performance results make sense.
> 
> Your mask for gfx908 appears to be correct for a fully-enabled 120 CU gfx908.

Thanks a lot for your reply!

So it is just a counterintuitive problem of byte order. 

And I think it can be helpful if an example or a documation entry about CU mask is given since there is hardly any information about the API.

---

### 评论 #3 — jlgreathouse (2023-01-16T21:17:14Z)

Thank you for the recommendation. We will take it into account when updating our documentation. I'm going to close this thread since I believe we've addressed your original question.

---
