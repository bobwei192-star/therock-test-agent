# fclk clock is unsupported ... Aborted (core dumped)

- **Issue #:** 1449
- **State:** closed
- **Created:** 2021-04-09T23:43:46Z
- **Updated:** 2021-04-16T10:49:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/1449

```
rocm-smi -a
========================== Current clock frequencies ===========================
GPU[0]		: dcefclk clock level: 0: (600Mhz)
ERROR: GPU[0] 		: fclk clock is unsupported
GPU[0]		: mclk clock level: 0: (167Mhz)
GPU[0]		: sclk clock level: 0: (852Mhz)
GPU[0]		: socclk clock level: 0: (600Mhz)
python3: /var/tmp/portage/dev-libs/rocm-smi-lib-4.1.0/work/rocm_smi_lib-rocm-4.1.0/src/rocm_smi.cc:898: rsmi_status_t get_frequencies(amd::smi::DevInfoTypes, uint32_t, rsmi_frequencies_t*, uint32_t*): Assertion `f->current == RSMI_MAX_NUM_FREQUENCIES + 1' failed.
Aborted (core dumped)
```

same text error on other case: https://github.com/RadeonOpenCompute/rocm_smi_lib/issues/81

may be reason this case: pp_dpm_fclk interface is only available for Vega20 and later ASICs.

but I have case with this error on GPU Vega 10 Frontier Edition Air