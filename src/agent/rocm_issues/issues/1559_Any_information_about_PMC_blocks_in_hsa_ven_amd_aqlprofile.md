# Any information about PMC blocks in hsa_ven_amd_aqlprofile?

> **Issue #1559**
> **状态**: closed
> **创建时间**: 2021-08-19T08:06:43Z
> **更新时间**: 2024-02-08T03:48:37Z
> **关闭时间**: 2024-02-08T03:48:37Z
> **作者**: WyldeCat
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1559

## 描述

Because rocprofiler doesn't support GFX10 (gfx1010 or gfx1030), I searched ROCm (4.2.0) header files for clues and found some enum about GFX10 at (rocm/include/hsa/hsa_ven_amd_aqlprofile.h) .

Is there any information about what those PMC blocks are?
```
  // GFX10 added blocks
  HSA_VEN_AMD_AQLPROFILE_BLOCK_NAME_GL1A = 26,
  HSA_VEN_AMD_AQLPROFILE_BLOCK_NAME_GL1C = 27,
  HSA_VEN_AMD_AQLPROFILE_BLOCK_NAME_GL2A = 28,
  HSA_VEN_AMD_AQLPROFILE_BLOCK_NAME_GL2C = 29,
  HSA_VEN_AMD_AQLPROFILE_BLOCK_NAME_GCR = 30,
  HSA_VEN_AMD_AQLPROFILE_BLOCK_NAME_GUS = 31,

  HSA_VEN_AMD_AQLPROFILE_BLOCKS_NUMBER
} hsa_ven_amd_aqlprofile_block_name_t;
```

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-08-23T05:40:19Z)

Thanks @WyldeCat for reaching out.
I will work with hsa developer and share an update on this.
Thank you.

---

### 评论 #2 — abhimeda (2024-01-02T15:49:37Z)

Is this still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #3 — nartmada (2024-01-27T04:20:32Z)

Hi @WyldeCat, do you still need this ticket to be opened?  Do you still need the PCM blocks info?  Thanks.

---

### 评论 #4 — nartmada (2024-02-08T03:48:37Z)

Closing this ticket as it is stale.  @WyldeCat, please re-open if you still need info on PCM blocks.  Thanks.

---
