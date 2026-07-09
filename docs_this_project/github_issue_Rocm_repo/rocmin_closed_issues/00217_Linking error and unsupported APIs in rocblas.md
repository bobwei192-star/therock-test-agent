# Linking error and unsupported APIs in rocblas

- **Issue #:** 217
- **State:** closed
- **Created:** 2017-09-29T11:18:00Z
- **Updated:** 2017-10-06T09:44:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/217

**Background:** 
Porting Mxnet Deep Learning framework to ROCm Platform and migrating from hcblas to rocblas

**Issue:** 
Link error /home/user/workspace/rocblas_integration_latst/mxnet/mshadow/mshadow/./././dot_engine-inl.h:456: undefined reference to `rocblas_hgemm'

/home/user/workspace/rocblas_integration_latst/mxnet/mshadow/mshadow/./././dot_engine-inl.h:456: undefined reference to `rocblas_hgemm'
collect2: error: ld returned 1 exit status
Makefile:302: recipe for target 'bin/im2rec' failed
make: *** [bin/im2rec] Error 1

rocblas_hgemm() function declaration is present at rocblas/include/rocblas-functions.h. But while linking we facing above error. Encountering above error while compiling on nvcc platform.

**Unsupported APIs :**
Unable to find relevant implementation of below APIs:

- hipblasSgemmBatched()
- hipblasDgemmBatched()
- cublasSgemmEx()

Please provide inputs for the above queries.