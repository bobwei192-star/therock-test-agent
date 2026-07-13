# Meaning of VALUBusy counter

- **Issue #:** 1620
- **State:** closed
- **Created:** 2021-11-18T10:39:06Z
- **Updated:** 2022-04-07T08:20:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/1620

Hi, we have a quick (and maybe dumb) question about `VALUBusy` counter. Here's its formula from [metrics.xml](https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/test/tool/metrics.xml)
```
100*SQ_ACTIVE_INST_VALU*4/SIMD_NUM/GRBM_GUI_ACTIVE
```
`SIMD_NUM` here stands for all SIMDs in GPU i.e. `simds_per_cu * cu_num`.

Does `*4` term stand for number of SIMDs per single CU? If yes, does `VALUBusy` count cases when only some (even just 1) out of 4 SIMDs are processing a vector instruction, whereas others may be stalled ?