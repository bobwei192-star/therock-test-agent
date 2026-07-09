# Any information about PMC blocks in hsa_ven_amd_aqlprofile?

- **Issue #:** 1559
- **State:** closed
- **Created:** 2021-08-19T08:06:43Z
- **Updated:** 2024-02-08T03:48:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1559

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