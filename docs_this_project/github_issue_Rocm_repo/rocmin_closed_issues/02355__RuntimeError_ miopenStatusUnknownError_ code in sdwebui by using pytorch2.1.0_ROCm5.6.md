# "RuntimeError: miopenStatusUnknownError" code in sdwebui by using pytorch2.1.0+ROCm5.6

- **Issue #:** 2355
- **State:** closed
- **Created:** 2023-07-30T06:01:15Z
- **Updated:** 2023-07-31T01:36:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/2355

GPU: 7900xtx
version of sdwebui: v1.5.1
version of pytorch: https://download.pytorch.org/whl/nightly/rocm5.6
Failed to generate pictures after swiching the pytorch from https://evshiron.github.io/ to pytorch.org. 
It used to work well with evshiron's pytorch version with ROCm5.6.
But still have response when key  in "rocm-smi"  code.
So I don't know whether there is a bug on bytorch or rocm or my steps :(
![截图 2023-07-30 13-59-15](https://github.com/RadeonOpenCompute/ROCm/assets/104998459/50980e4e-85d9-4da4-8420-d4483cdb7995)
