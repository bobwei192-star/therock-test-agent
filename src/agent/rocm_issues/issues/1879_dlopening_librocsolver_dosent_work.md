# dlopening librocsolver dosent work

> **Issue #1879**
> **状态**: closed
> **创建时间**: 2022-12-19T13:39:16Z
> **更新时间**: 2022-12-21T10:03:11Z
> **关闭时间**: 2022-12-21T10:03:11Z
> **作者**: IMbackK
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1879

## 负责人

- cgmb
- doctorcolinsmith
- TorreZuk

## 描述

the Ubuntu 22.04 packages for rocm 5.4  contain an issue:

dlopening librocsolver.so fails as there is a undefined symbol:
_Z31rocblas_internal_syr2k_templateILb0ELb1EPKfS1_PfE15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiT1_T2_lilS9_lilS8_T3_lili

an objectdump -T of ibrocsolver.so reveals:

```
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi16ELb0ELb1ELb0EffPKfPfE15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSB_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi32ELb0ELb1ELb0EddPKdPdE15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSB_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi32ELb0ELb1ELb1E19rocblas_complex_numIfEfPKS1_PS1_E15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSD_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi32ELb0ELb1ELb1E19rocblas_complex_numIdEdPKS1_PS1_E15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSD_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi16ELb1ELb1ELb0EffPKPKfPKPfE15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSF_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi16ELb1ELb1ELb0EddPKPKdPKPdE15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSF_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi8ELb1ELb1ELb1E19rocblas_complex_numIfEfPKPKS1_PKPS1_E15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSH_lilPKT4_T6_lili
0000000000000000      DF *UND*	0000000000000000  Base        _Z37rocblas_internal_syr2k_her2k_templateILi8ELb1ELb1ELb1E19rocblas_complex_numIdEdPKPKS1_PKPS1_E15rocblas_status_P15_rocblas_handle13rocblas_fill_18rocblas_operation_iiPKT3_T5_lilSH_lilPKT4_T6_lili
```

---

## 评论 (4 条)

### 评论 #1 — saadrahim (2022-12-20T20:11:48Z)

@doctorcolinsmith Can you please triage the issue to the correct team? I believe this is a build issue.

---

### 评论 #2 — TorreZuk (2022-12-21T00:10:10Z)

Looking at solver a similar issue was closed in https://github.com/ROCmSoftwarePlatform/rocSOLVER/issues/230 and a test was added for this use case ( https://github.com/ROCmSoftwarePlatform/rocSOLVER/pull/310 see the bottom and new client test called test-rocsolver-dlopen ) so not how  this problem snuck through.  Would first see if someone on solver side can run that new test on Ubuntu22 docker with a 5.4 installation.  @IMbackK can you confirm rocblas was installed?  Maybe paste your dlopen call as well to help diagnose.  I would first triage this to solver team.

---

### 评论 #3 — cgmb (2022-12-21T01:33:47Z)

This works fine for me in an ubuntu:22.04 container:

```bash
#!/bin/bash

set -eux

cd $HOME
apt -y update
apt -y upgrade
apt -y install wget
wget https://repo.radeon.com/amdgpu-install/5.4.1/ubuntu/jammy/amdgpu-install_5.4.50401-1_all.deb
apt -y install ./amdgpu-install_5.4.50401-1_all.deb 
yes | amdgpu-install --no-dkms --usecase=rocmdev
apt -y install rocsolver rocblas
cat << 'EOF' > test-dlopen.cpp
// test-dlopen.cpp
// hipcc test-dlopen.cpp -ldl -o test_runner
// ./test_runner
#include <dlfcn.h>
#include <iostream>

#define ROCSOLVER_LIB_NAME "/opt/rocm-5.4.1/lib/librocsolver.so.0"

void* open_roc_lib(const char* lib_name) {
  void* handle = dlopen(lib_name, RTLD_NOW | RTLD_LOCAL);
  if (!handle) {
    std::cout << dlerror() << "\n";
    return 0;
  }
  std::cout << "loaded " << lib_name << "\n";
  return handle;
}

int main() {
  void* rocsolver_handle = open_roc_lib(ROCSOLVER_LIB_NAME);
  dlclose(rocsolver_handle);
  return 0;
}
EOF
hipcc test-dlopen.cpp -ldl -o test_runner
./test_runner 
```

However, one thing that does surprise me is that the rocsolver package is listed as having no dependencies... I think this may have been a bug for a while. When I compare the rocSOLVER package and the hipSOLVER package, there seems to be a missing `DEPENDS` argument on the rocSOLVER call to `rocm_package_add_dependencies`:

- rocsolver (wrong):
  - https://github.com/ROCmSoftwarePlatform/rocSOLVER/blob/rocm-5.4.1/CMakeLists.txt#L182
- hipsolver (right):
  - https://github.com/ROCmSoftwarePlatform/hipSOLVER/blob/rocm-5.4.1/CMakeLists.txt#L214

---

### 评论 #4 — IMbackK (2022-12-21T10:03:11Z)

so looks like this was a corruption issue on my end:
ldconfig complains:
`ldconfig: file /opt/rocm/rocsolver/lib/librocsolver.so is truncated.`
so something whent wrong on my machine.
a reinstall seams to have worked, sorry for the noise

---
