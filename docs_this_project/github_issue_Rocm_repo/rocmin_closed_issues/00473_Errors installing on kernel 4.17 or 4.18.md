# Errors installing on kernel 4.17 or 4.18

- **Issue #:** 473
- **State:** closed
- **Created:** 2018-07-27T10:03:42Z
- **Updated:** 2021-04-05T07:57:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/473

When attempting ROCm 1.8.2 install on Ubuntu 18.04 with kernel 4.17 or 4.18 (tried both), these are the errors:
Building initial module for 4.18.0-041800rc6-generic
ERROR (dkms apport): kernel package linux-headers-4.18.0-041800rc6-generic is not supported
Error! Bad return status for module build on kernel: 4.18.0-041800rc6-generic (x86_64)
Consult /var/lib/dkms/amdgpu/1.8-192/build/make.log for more information.

/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c: In function ‘amdgpu_pmops_runtime_suspend’:
/var/lib/dkms/amdgpu/1.8-192/build/amd/amdgpu/amdgpu_drv.c:727:2: error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’; did you mean ‘vga_switcheroo_process_delayed_switch’? [-Werror=implicit-function-declaration]
  vga_switcheroo_set_dynamic_switch(pdev, VGA_SWITCHEROO_OFF);