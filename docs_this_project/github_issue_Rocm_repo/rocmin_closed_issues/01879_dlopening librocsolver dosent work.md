# dlopening librocsolver dosent work

- **Issue #:** 1879
- **State:** closed
- **Created:** 2022-12-19T13:39:16Z
- **Updated:** 2022-12-21T10:03:11Z
- **Assignees:** cgmb, doctorcolinsmith, TorreZuk
- **URL:** https://github.com/ROCm/ROCm/issues/1879

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