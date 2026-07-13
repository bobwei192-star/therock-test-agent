# build error with gcc 7.3 at Ubuntu 18.04

- **Issue #:** 586
- **State:** closed
- **Created:** 2018-10-24T06:53:37Z
- **Updated:** 2018-10-24T06:54:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/586

  CC [M]  drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.o
drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c: In function ‘init_user_pages’:
drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c:635:3: error: implicit declaration of function ‘release_pages’; did you mean ‘release_task’? [-Werror=implicit-function-declaration]
   release_pages(mem->user_pages, bo->tbo.ttm->num_pages);
   ^~~~~~~~~~~~~
   release_task