# Suboptimal GROMACS performance on Vega

- **Issue #:** 222
- **State:** closed
- **Created:** 2017-10-06T01:18:23Z
- **Updated:** 2018-09-17T21:59:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/222

The main kernel (force-only, name-pattern nbnxn_kernel_*_*_F_opencl_gfxXXX) runs up to 22% slower on Vega than on Fiji. Other kernels are a mixed bag. One of the likely contributors is that most kernels end up using quite a bit more registers when compiled for gfx900, e.g.

nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl_gfx803 registers: 81, 54
nbnxn_kernel_ElecEw_VdwLJCombGeom_F_opencl_gfx900 registers: 85, 54

nbnxn_kernel_ElecEw_VdwLJCombGeom_VF_opencl_gfx803  registers: 84, 68
nbnxn_kernel_ElecEw_VdwLJCombGeom_VF_opencl_gfx900 registers 93, 68

For the former "F" kernels, performance across the relevant range of input sizes:
```
Input	Kernel time/iteration (ms)
size	Fiji	Vega	
0.96	0.0727	0.0615	84.59%
1.5	0.1018	0.0799	78.49%
3	0.1165	0.0995	85.41%
6	0.1539	0.169	109.81%
12	0.2582	0.2987	115.69%
24	0.4327	0.5242	121.15%
48	0.7794	0.9545	122.47%
96	1.4489	1.7762	122.59%
192	2.7754	3.3861	122.00%
384	5.6074	6.7722	120.77%
768	11.0613	13.5129	122.16%
1536	21.6894	26.646	122.85%
3072	43.3131	53.2424	122.92%

```
