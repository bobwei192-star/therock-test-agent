# Vega FE slow OpenCL performance for Mining applications

- **Issue #:** 147
- **State:** closed
- **Created:** 2017-07-03T22:14:05Z
- **Updated:** 2018-08-24T00:47:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/147

Vega FE has very slow OpenCL performance under ROCm 1.6 and Ubuntu 16.04. Card Boots and initialized properly, and confirmed that Vega is running at full clocks during openCL tests via SMI utility. 

Performance is about 20% of what is achieved under same OpenCL app under windows driver. 

Same performance is also verified under AMDGPU-PRO with ROCm package installed. 