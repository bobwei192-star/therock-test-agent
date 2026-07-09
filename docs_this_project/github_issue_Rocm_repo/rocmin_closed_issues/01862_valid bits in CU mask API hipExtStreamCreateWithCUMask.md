# valid bits in CU mask API hipExtStreamCreateWithCUMask

- **Issue #:** 1862
- **State:** closed
- **Created:** 2022-11-19T03:17:47Z
- **Updated:** 2023-01-16T21:17:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/1862

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