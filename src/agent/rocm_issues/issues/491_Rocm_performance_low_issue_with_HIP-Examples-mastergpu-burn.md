# Rocm performance low issue with HIP-Examples-master/gpu-burn

> **Issue #491**
> **状态**: closed
> **创建时间**: 2018-08-06T08:07:51Z
> **更新时间**: 2023-12-12T21:50:50Z
> **关闭时间**: 2023-12-12T21:50:49Z
> **作者**: J0hnn4J1ang
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/491

## 描述

Hi, 
    I met with rocm1.8 +ubuntu18.04 LTS + 2 cards Ellesmere [Radeon RX 470/480] performance low issue.
    I ran hip example code to burn gpu to check performance,  the code I run is the HIP examples: HIP-Examples-master/gpu-burn. 
    While gpu burnning, rocm-smi showed that MCLK has only 500M, but SCLK increased to 1130MHz from 300MHz in idle.
     I could use rocm-smi -d 1 --setmclk 2 to change MCLK to 2000M, rocm-smi showed it changed to 2000M but performance not increase at all,  I think GPU not really worked at 2000MHz.

     So my question is:
     1. Why gpu performance is slow under gpu-burn, what can I try to increase performance?
     2. Is it related to 500M MCLK  ?
     3. MCLK changed to 2000M not really work, right?
  
idle:

 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   35c     30.178W  300Mhz   500Mhz   0.0%     manual    0%         0%       
  0   34c     32.244W  300Mhz   500Mhz   0.0%     manual    0%         0%       

While burning:

 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   45c     104.171W 1130Mhz  500Mhz   0.0%     manual    0%         0%       
  0   43c     98.192W  1130Mhz  500Mhz   0.0%     manual    0%         0%       

After rocm-smi -d 1 --setmclk 2

 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   38c     32.153W  300Mhz   2000Mhz  0.0%     manual    0%         0%       
  0   36c     34.176W  300Mhz   2000Mhz  0.0%     manual    0%         0%       

---

## 评论 (9 条)

### 评论 #1 — J0hnn4J1ang (2018-08-06T09:51:11Z)

tried rocm1.8.2+ubuntu 16.04, still same issue

---

### 评论 #2 — preda (2018-08-06T11:18:22Z)

I'm not familiar with gpu-burn, but it could be compute-bound vs. memory-bound. That is, maybe it "burns" by doing a lot of fast compute but not much memory read/write. Then the GPU normally lowers the RAM clock because it's not used, and rising it manually doesn't change the observed performance.

---

### 评论 #3 — J0hnn4J1ang (2018-08-06T12:06:09Z)

@preda Thanks for your replay, in gpuburn, it keep doing dimension 512x512 matrix mul, like A * B =C,  and all the 3 matrixs stays in the ddr by calling hipmalloc.  Meanwhile I think  gpu cache and local memory has no enough space to store all the 3 matrix. So for this case, gpu compute unit should access ddr memory alot.  MCLK is critical for the performance.

Below is burn kernel example.

``
int BurnKernel::runComputeKernel()
{
    int err = 0;
    for (int i = 0; mRunKernel && i < mNumIterations; ++i) {
        hipLaunchKernel(
            /* Launch params */
            HIP_KERNEL_NAME(hip_sgemm_kernel),
            dim3(cRowSize/cBlockSize, cRowSize/cBlockSize, 1),
            dim3(cBlockSize,cBlockSize,1), 0, 0,
            /* Kernel params */
            cRowSize, cRowSize, cRowSize, cAlpha,
            mDeviceAdata, cRowSize,
            mDeviceBdata, cRowSize,
            cBeta,
            mDeviceCdata + i*cMatrixSize,
            cRowSize);
    }
    checkError(hipDeviceSynchronize(), "Sync");

    return err;
}
``

---

### 评论 #4 — preda (2018-08-06T13:51:57Z)

Thanks, yes, it may be memory-bound after all. Then I'll let somebody more knowledgeable look into it.

---

### 评论 #5 — J0hnn4J1ang (2018-08-07T02:00:21Z)

@preda Thanks. If you have idea please let me know  what  I could do to confirm the memory-bound factor or  avoid the impact.

---

### 评论 #6 — J0hnn4J1ang (2018-08-08T07:09:11Z)

Add more findings:

If my gpu-burn kernel is a matrix mul kernel, like sgemm below, MCLK stays at 500MHZ. But if my kernel is a simple matrix add kernel as below hip_add_kernel, the MCLK could reach 2000MHZ.
       So my question is, why for  computationally intensive kernel, MCLK stays at lower value? It also need read alot of matrix items,  shouldn't this affect the performance ?

 __global__ void hip_sgemm_kernel(hipLaunchParm lp, const int M,
                                            const int N, const int K,
                                            const float alpha,
                                            float *A, const int lda, float *B,
                                            const int ldb, const float beta,
                                            float *C, const int ldc)
{
        //column major NN
        size_t idx_x = hipBlockIdx_x * hipBlockDim_x + hipThreadIdx_x;
        size_t idx_y = hipBlockIdx_y * hipBlockDim_y + hipThreadIdx_y;
        size_t dim_x = hipGridDim_x * hipBlockDim_x;
        size_t myIdx = idx_y * dim_x + idx_x;

        float local_c = beta * C[myIdx];
        for(int k = 0; k < K; k++) {
          local_c += alpha * A[ idx_y + k * K] * B[ idx_x * K + k];
        }
        C[myIdx] = local_c;
}

__global__ void hip_add_kernel(hipLaunchParm lp, const int M,
                                            const int N, const int K,
                                            const float alpha,
                                            float *A, const int lda, float *B,
                                            const int ldb, const float beta,
                                            float *C, const int ldc)
{
        //column major NN
        size_t idx_x = hipBlockIdx_x * hipBlockDim_x + hipThreadIdx_x;
        size_t idx_y = hipBlockIdx_y * hipBlockDim_y + hipThreadIdx_y;
        size_t dim_x = hipGridDim_x * hipBlockDim_x;
        size_t myIdx = idx_y * dim_x + idx_x;

        float local_c = beta * C[myIdx];
        local_c += alpha * A[ idx_y + 0 * K] * B[ idx_x * K + 0];
        C[myIdx] = local_c;
}



---

### 评论 #7 — ROCmSupport (2021-01-07T08:25:23Z)

Hi @J0hnn4J1ang 
Thanks for logging this issue.
Can you please verify this issue with the latest release ROCm 4.0 and share an update asap.
Thank you.

---

### 评论 #8 — tasso (2023-12-08T17:15:24Z)

Is this still an issue?  If not, can we please close it?

---

### 评论 #9 — tasso (2023-12-12T21:50:49Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
