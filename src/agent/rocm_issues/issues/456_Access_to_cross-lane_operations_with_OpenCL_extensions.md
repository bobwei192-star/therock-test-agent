# Access to cross-lane operations with OpenCL extensions

> **Issue #456**
> **状态**: open
> **创建时间**: 2018-07-12T00:27:25Z
> **更新时间**: 2026-02-24T17:07:15Z
> **作者**: axeldavy
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/456

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hi,

Intel has a very useful extension:
cl_intel_subgroups

Which enables inside a subgroup (a wavefront) to shuffle items, do reduce operations, etc.

According to https://gpuopen.com/amd-gcn-assembly-cross-lane-operations/
Recent AMD hardware can do the same, and even better.

I know this functionnality is available via HSA or inline assembly, but there is no OpenCL extension supported by AMD for that. Assembly is not a good solution for an OpenCL developper, as the assembly might need to be updated for new cards or for bug workarounds. Please make it an extension !

Features I'd like to have: shuffle, fine grained reduction operations. For example reduction among work items 0, 8, 16, etc, and 1, 9, 17, etc you get the idea, or reduction among 0-7, 8-15, etc. This type of fine grained reduction would be very useful. Going through LDS is possible, but for a reduction operation, you need several lds reads, and using the cross lane operations would be much faster.

---

## 评论 (10 条)

### 评论 #1 — ghost (2018-07-22T15:59:55Z)

There is a amd extention for that if I recal it was in the 2.7 branch of the AMD SDK

---

### 评论 #2 — axeldavy (2018-07-22T16:09:18Z)

If there used to be such an extension, well it doesn't seem there anymore (and I was unable to find any info on it).

---

### 评论 #3 — ROCmSupport (2021-01-07T06:33:04Z)

Thanks @axeldavy for reaching out.
I will check with OpenCL team and get back to you asap.
Thank you.

---

### 评论 #4 — tasso (2023-12-08T17:06:02Z)

Is this still an issue?  If not, can we please close it?

---

### 评论 #5 — axeldavy (2023-12-08T19:12:31Z)

To the best of my knowledge, this is still an issue.
Yours.

---

### 评论 #6 — tasso (2023-12-08T19:39:34Z)

Thanks for the reply! 

@ROCmSupport Have we got a response from the OpenCL team?  If so; what was there response?  Also, please advise next steps? Thanks!

---

### 评论 #7 — nartmada (2024-01-02T16:17:24Z)

@axeldavy, I have reached out to the internal team for feedback.  Extending OpenCL is on their TODO list but at a low priority.  We are currently keeping this ticket opened and will re-visit in 2024 Q2.  Thanks.

---

### 评论 #8 — nartmada (2024-10-16T21:08:15Z)

@axeldavy, unfortunately Extending OpenCL is still a low priority.  We will keep this ticket opened and will revisit the priority in 2025.  Thanks.

---

### 评论 #9 — mambastudio (2025-08-20T05:03:16Z)

Damn. Things like these, almost a decade later, are what motivates someone to go to other vendors. Cool algorithms that deal with single kernel scan from gpus that have no capability on forward progress guarantee such as from a [paper released a few weeks ago](https://dl.acm.org/doi/10.1145/3694906.3743326) would take advantage of this. 

---

### 评论 #10 — octaveoclx (2026-02-24T17:07:14Z)

AI (Deepseek) provides possible unified example functions （could be incorrect).

```
float subgroup_shuffle(float val, uint lane) {
  // --- 1. Check for Qualcomm Adreno GPU first ---
  // cl_qcom_subgroup_shuffle is a Qualcomm extension and must be explicitly enabled
  #ifdef __QCOM_ADRENO__
    // Ensure the extension is enabled in the kernel:
    // #pragma OPENCL EXTENSION cl_qcom_subgroup_shuffle : enable

    // Here we use the full subgroup width (the entire wave) with an xor-style shuffle.
    // You can also choose other directions (e.g., qcom_sub_group_shuffle_up/down) and width modes.
    return qcom_sub_group_shuffle_xor(val, lane, CLK_SUB_GROUP_SHUFFLE_WIDTH_WAVE_SIZE_QCOM, 0.0f);
    // Note: The last parameter default_value is returned if the requested lane is invalid.

  // --- 2. AMD GCN architecture (e.g., RDNA, CDNA series) ---
  #elif defined(__AMDGCN__)
    // Use AMD built-in for shuffle. Lane must be converted to a byte offset.
    return __builtin_amdgcn_ds_bpermute(lane * 4, val);

  // --- 3. NVIDIA CUDA architecture (e.g., Volta and newer Blackwell) ---
  #elif defined(__NVCC__) || defined(__NVVM__)
    // Use the CUDA shuffle instruction. 0xFFFFFFFF means all active threads participate.
    return __shfl_sync(0xFFFFFFFF, val, lane);

  // --- 4. Intel subgroup extensions (Intel Gen9, Xe architecture, Arc series) ---
  #elif defined(INTEL_SUBGROUP)
    // Use Intel's official subgroup shuffle function.
    return intel_sub_group_shuffle(val, lane);

  // --- 5. Fallback: if no specific platform detected, provide a portable but possibly slower implementation ---
  #else
    // This is a simulation using local memory inside the workgroup to ensure the code works on any OpenCL device.
    // Note: Its performance is far lower than hardware-supported shuffle operations.
    // Get the local ID and size of the current subgroup (assuming subgroup extension support).
    // If the device does not support subgroups, you need more complex logic; here we simplify.
    #warning "No optimized subgroup shuffle implementation, falling back to local memory simulation."
    uint sub_group_local_id = get_sub_group_local_id();
    uint sub_group_size = get_sub_group_size();
    
    // Use local memory as a temporary buffer for data exchange.
    local float shuffle_tmp[128]; // Assume maximum subgroup size does not exceed 128.
    
    // Write the current work-item's value to local memory for others to read.
    shuffle_tmp[sub_group_local_id] = val;
    
    // Barrier ensures all writes are completed, then read the target lane's data.
    barrier(CLK_LOCAL_MEM_FENCE);
    float result = shuffle_tmp[lane];
    barrier(CLK_LOCAL_MEM_FENCE); // Cleanup barrier to prevent conflicts in subsequent use.
    
    return result;
  #endif
}
```
```

float subgroup_reduce_add(float val) {
    // --- Qualcomm Adreno (using cl_qcom_subgroup_shuffle) ---
    #ifdef __QCOM_ADRENO__
        #pragma OPENCL EXTENSION cl_qcom_subgroup_shuffle : enable
        return qcom_sub_group_reduce_add(val, CLK_SUB_GROUP_SHUFFLE_WIDTH_WAVE_SIZE_QCOM, 0.0f);

    // --- AMD GCN / RDNA (ROCm) ---
    #elif defined(__AMDGCN__)
        // AMD does not support standard sub_group_shuffle functions;
        // instead, we use the underlying hardware intrinsics.
        uint lane = get_sub_group_local_id();      // lane index within wavefront
        uint size = get_sub_group_size();          // wavefront size (typically 64)

        // Reduction using "shuffle down" semantics via ds_bpermute
        for (uint offset = size >> 1; offset > 0; offset >>= 1) {
            // Read value from lane (lane + offset). Note: ds_bpermute uses byte addressing.
            float other = __builtin_amdgcn_ds_bpermute((lane + offset) * 4, val);
            // Only lanes with index < offset accumulate the incoming value.
            // Lanes with index >= offset keep their current value (they will be idle later).
            if (lane < offset) {
                val += other;
            }
        }
        // Broadcast the final sum from lane 0 to all lanes in the wavefront.
        val = __builtin_amdgcn_ds_bpermute(0, val);
        return val;

    // --- NVIDIA CUDA ---
    #elif defined(__NVCC__) || defined(__NVVM__)
        // Warp-level reduction using shuffle down
        for (int offset = 16; offset >= 1; offset >>= 1) {
            val += __shfl_down_sync(0xFFFFFFFF, val, offset);
        }
        // Broadcast result from lane 0 to all lanes
        val = __shfl_sync(0xFFFFFFFF, val, 0);
        return val;

    // --- Intel Subgroups ---
    #elif defined(INTEL_SUBGROUP)
        // Intel built-in reduction – already returns the same value to all work‑items.
        return sub_group_reduce_add(val);

    // --- Fallback: use standard OpenCL subgroup extensions if available ---
    #else
        #ifdef cl_khr_subgroup_reduction
            // Standard cross‑vendor subgroup reduction
            return sub_group_reduce_add(val);
        #else
            // Manual reduction via local memory, followed by a broadcast.
            uint sub_group_size     = get_sub_group_size();
            uint sub_group_local_id = get_sub_group_local_id();
            local float tmp[128];   // assume max subgroup size ≤ 128

            tmp[sub_group_local_id] = val;
            barrier(CLK_LOCAL_MEM_FENCE);

            for (uint offset = sub_group_size / 2; offset > 0; offset >>= 1) {
                if (sub_group_local_id < offset) {
                    tmp[sub_group_local_id] += tmp[sub_group_local_id + offset];
                }
                barrier(CLK_LOCAL_MEM_FENCE);
            }

            // Broadcast the result (tmp[0]) to all work‑items in the subgroup.
            val = tmp[0];
            barrier(CLK_LOCAL_MEM_FENCE);
            tmp[sub_group_local_id] = val;   // not strictly necessary, but keeps all lanes in sync
            barrier(CLK_LOCAL_MEM_FENCE);
            val = tmp[sub_group_local_id];
            return val;
        #endif
    #endif
}
```
```

// Returns the minimum value among all active work-items in the current subgroup (wavefront/warp)
float subgroup_reduce_min(float val) {
    // ---- 1. Standard OpenCL subgroup reduction extension (cl_khr_subgroup_reduction) ----
    #ifdef cl_khr_subgroup_reduction
        #pragma OPENCL EXTENSION cl_khr_subgroup_reduction : enable
        return sub_group_reduce_min(val);

    // ---- 2. Qualcomm Adreno specific extension ----
    #elif defined(__QCOM_ADRENO__)
        #pragma OPENCL EXTENSION cl_qcom_subgroup_shuffle : enable
        // Use full subgroup width, return FLT_MAX for invalid lanes (to avoid affecting the min)
        return qcom_sub_group_reduce_min(val,
                                          CLK_SUB_GROUP_SHUFFLE_WIDTH_WAVE_SIZE_QCOM,
                                          FLT_MAX);

    // ---- 3. AMD GCN/RDNA (ROCm) low-level builtins ----
    #elif defined(__AMDGCN__)
        uint lane = get_sub_group_local_id();   // Index of the current lane within the subgroup
        uint size = get_sub_group_size();       // Subgroup size (typically 64)

        // Tree reduction: start from size/2 and halve each step
        for (uint offset = size >> 1; offset > 0; offset >>= 1) {
            // Use ds_bpermute to read data from lane (lane + offset)
            float other = __builtin_amdgcn_ds_bpermute((lane + offset) * 4, val);
            // Only lanes with index < offset participate in the merge
            if (lane < offset) {
                val = min(val, other);
            }
        }
        // Broadcast the final min value from lane 0 to all lanes
        val = __builtin_amdgcn_ds_bpermute(0, val);
        return val;

    // ---- 4. NVIDIA CUDA platform (via __shfl instructions) ----
    #elif defined(__NVCC__) || defined(__NVVM__)
        // Warp-level reduction, warp size fixed at 32
        for (int offset = 16; offset >= 1; offset >>= 1) {
            float other = __shfl_down_sync(0xFFFFFFFF, val, offset);
            val = min(val, other);
        }
        // Broadcast the final result from lane 0
        val = __shfl_sync(0xFFFFFFFF, val, 0);
        return val;

    // ---- 5. Intel subgroup extension ----
    #elif defined(INTEL_SUBGROUP)
        #pragma OPENCL EXTENSION cl_intel_subgroups : enable
        return intel_sub_group_reduce_min(val);

    // ---- 6. Generic fallback: simulation using local memory ----
    #else
        uint sub_group_size     = get_sub_group_size();
        uint sub_group_local_id = get_sub_group_local_id();
        // Local memory buffer (assuming max subgroup size ≤ 128 work-items)
        local float tmp[128];

        tmp[sub_group_local_id] = val;
        barrier(CLK_LOCAL_MEM_FENCE);

        // Reduction loop
        for (uint offset = sub_group_size >> 1; offset > 0; offset >>= 1) {
            if (sub_group_local_id < offset) {
                tmp[sub_group_local_id] = min(tmp[sub_group_local_id],
                                              tmp[sub_group_local_id + offset]);
            }
            barrier(CLK_LOCAL_MEM_FENCE);
        }

        // Broadcast the result (tmp[0]) to all work-items in the subgroup
        val = tmp[0];
        barrier(CLK_LOCAL_MEM_FENCE);
        tmp[sub_group_local_id] = val;          // Write back for broadcast
        barrier(CLK_LOCAL_MEM_FENCE);
        val = tmp[sub_group_local_id];          // All threads get the same minimum value
        return val;
    #endif
}
```

---
