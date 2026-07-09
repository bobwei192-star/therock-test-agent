# OpenCL discrepency (ROCm 1.6-115 vs Catalyst)

- **Issue #:** 178
- **State:** closed
- **Created:** 2017-08-07T09:40:33Z
- **Updated:** 2018-02-16T16:22:43Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/178

MIOpenGEMM generates OpenCL kernels based on ~20 hyper-parameters. Almost all of generated kernels compile and give correct results on ROCm. But occasionally a combination of hyper-parameters will give a  kernel which either

(1) gives incorrect results on ROCm, but correct on Catalyst. An example is here
https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/blob/develop/rocm1/incorrect1.cpp

(2) hangs in clBuildProgram on ROCm, but compiles fine on Catalyst. An example is here 
https://github.com/ROCmSoftwarePlatform/MIOpenGEMM/blob/develop/rocm1/hangs1.cpp

I can't pinpoint the problem, it seems to arise from a complex interaction of hyper-parameters. 
Not sure what info I can provide? 