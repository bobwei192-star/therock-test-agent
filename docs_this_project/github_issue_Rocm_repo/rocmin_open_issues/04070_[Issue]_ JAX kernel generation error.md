# [Issue]: JAX kernel generation error

- **Issue #:** 4070
- **State:** open
- **Created:** 2024-12-02T00:47:15Z
- **Updated:** 2025-07-17T03:54:36Z
- **Labels:** Under Investigation, ROCm 6.2.2, MI250X
- **Assignees:** Ruturaj4
- **URL:** https://github.com/ROCm/ROCm/issues/4070

### Problem Description

# Problem description

I am trying to run ColabFold, a scientific machine learning tool built on top of AlphaFold, to predict protein structure given a sequence of amino-acids. The following kernel generation problem arises on very large problem instances where a single GCD's memory is not enough. 

AlphaFold uses JAX/XLA to offload operations to GPUs.

```
:3:hip_module.cpp           :74  : 305270480312 us: [pid:312732 tid:0x15533460c740]  hipModuleGetFunction ( 0x7ffd650e5788, 0x559d78ba0e70, Cijk_Ailk_Bljk_SB_MT128x96x16_MI32x32x2x1_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASM_ASAE01_ASCE01_ASEM1_AAC0_BL1_BS1_CLR0_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS1_ELFLR0_EMLL0_FSSC10_FL0_GLVWA2_GLVWB2_GRCGA1_GRCGB1_GRPM1_GRVW2_GSU1_GSUASB_GLS0_ISA90a_IU1_K1_KLA_LBSPPA0_LBSPPB128_LPA0_LPB4_LDL1_LRVW4_LWPMn1_LDW0_FMA_MIAV1_MDA2_MO40_MMFGLC_MKFGSU256_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR2_PLR9_SIA1_SS0_SU0_SUM0_SUS0_SCIUI1_SPO0_SRVW0_SSO4_SVW4_SNLL0_TSGRA0_TSGRB0_TT1_96_TLDS1_UMLDSA0_UMLDSB1_U64SL1_USFGROn1_VAW1_VSn1_VW1_VWB1_VFLRP0_WSGRA0_WSGRB0_WS64_WG128_2_1_WGM15 ) 
:1:hip_code_object.cpp      :624 : 305270480327 us: [pid:312732 tid:0x15533460c740] Cannot find the function: Cijk_Ailk_Bljk_SB_MT128x96x16_MI32x32x2x1_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASM_ASAE01_ASCE01_ASEM1_AAC0_BL1_BS1_CLR0_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS1_ELFLR0_EMLL0_FSSC10_FL0_GLVWA2_GLVWB2_GRCGA1_GRCGB1_GRPM1_GRVW2_GSU1_GSUASB_GLS0_ISA90a_IU1_K1_KLA_LBSPPA0_LBSPPB128_LPA0_LPB4_LDL1_LRVW4_LWPMn1_LDW0_FMA_MIAV1_MDA2_MO40_MMFGLC_MKFGSU256_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR2_PLR9_SIA1_SS0_SU0_SUM0_SUS0_SCIUI1_SPO0_SRVW0_SSO4_SVW4_SNLL0_TSGRA0_TSGRB0_TT1_96_TLDS1_UMLDSA0_UMLDSB1_U64SL1_USFGROn1_VAW1_VSn1_VW1_VWB1_VFLRP0_WSGRA0_WSGRB0_WS64_WG128_2_1_WGM15 
:1:hip_module.cpp           :84  : 305270480339 us: [pid:312732 tid:0x15533460c740] Cannot find the function: Cijk_Ailk_Bljk_SB_MT128x96x16_MI32x32x2x1_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASM_ASAE01_ASCE01_ASEM1_AAC0_BL1_BS1_CLR0_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS1_ELFLR0_EMLL0_FSSC10_FL0_GLVWA2_GLVWB2_GRCGA1_GRCGB1_GRPM1_GRVW2_GSU1_GSUASB_GLS0_ISA90a_IU1_K1_KLA_LBSPPA0_LBSPPB128_LPA0_LPB4_LDL1_LRVW4_LWPMn1_LDW0_FMA_MIAV1_MDA2_MO40_MMFGLC_MKFGSU256_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR2_PLR9_SIA1_SS0_SU0_SUM0_SUS0_SCIUI1_SPO0_SRVW0_SSO4_SVW4_SNLL0_TSGRA0_TSGRB0_TT1_96_TLDS1_UMLDSA0_UMLDSB1_U64SL1_USFGROn1_VAW1_VSn1_VW1_VWB1_VFLRP0_WSGRA0_WSGRB0_WS64_WG128_2_1_WGM15 for module: 0x78ba0e70
:3:hip_module.cpp           :85  : 305270480350 us: [pid:312732 tid:0x15533460c740] hipModuleGetFunction: Returned hipErrorNotFound : 
:3:hip_error.cpp            :36  : 305270480362 us: [pid:312732 tid:0x15533460c740]  hipGetLastError (  ) 
:3:hip_module.cpp           :74  : 305270480374 us: [pid:312732 tid:0x15533460c740]  hipModuleGetFunction ( 0x7ffd650e5788, 0x559d7aa260b0, Cijk_Ailk_Bljk_SB_MT128x96x16_MI32x32x2x1_SN_1LDSB0_APM1_ABV0_ACED0_AF0EM1_AF1EM1_AMAS0_ASE_ASGT_ASLT_ASM_ASAE01_ASCE01_ASEM1_AAC0_BL1_BS1_CLR0_DTLA0_DTLB0_DTVA0_DTVB0_DVO0_ETSP_EPS1_ELFLR0_EMLL0_FSSC10_FL0_GLVWA2_GLVWB2_GRCGA1_GRCGB1_GRPM1_GRVW2_GSU1_GSUASB_GLS0_ISA90a_IU1_K1_KLA_LBSPPA0_LBSPPB128_LPA0_LPB4_LDL1_LRVW4_LWPMn1_LDW0_FMA_MIAV1_MDA2_MO40_MMFGLC_MKFGSU256_NTA0_NTB0_NTC0_NTD0_NEPBS0_NLCA1_NLCB1_ONLL1_OPLV0_PK0_PAP0_PGR2_PLR9_SIA1_SS0_SU0_SUM0_SUS0_SCIUI1_SPO0_SRVW0_SSO4_SVW4_SNLL0_TSGRA0_TSGRB0_TT1_96_TLDS1_UMLDSA0_UMLDSB1_U64SL1_USFGROn1_VAW1_VSn1_VW1_VWB1_VFLRP0_WSGRA0_WSGRB0_WS64_WG128_2_1_WGM15 ) 
:3:hip_module.cpp           :88  : 305270480397 us: [pid:312732 tid:0x15533460c740] hipModuleGetFunction: Returned hipSuccess : 
:3:hip_module.cpp           :470 : 305270480415 us: [pid:312732 tid:0x15533460c740]  hipExtModuleLaunchKernel ( 0x0x559d7d771340, 768, 66, 1, 256, 1, 1, 0, stream:0x559d688e6a50, char array:<null>, 0x7ffd650e57d0, event:0, event:0, 0 ) 
:3:rocvirtual.cpp           :798 : 305270480430 us: [pid:312732 tid:0x15533460c740] Arg0:  Tensor2dSizeA = val:110592
:3:rocvirtual.cpp           :798 : 305270480442 us: [pid:312732 tid:0x15533460c740] Arg1:  Tensor2dSizeB = val:2427264
:3:rocvirtual.cpp           :798 : 305270480453 us: [pid:312732 tid:0x15533460c740] Arg2:  AddressD = val:23372033148928
:3:rocvirtual.cpp           :798 : 305270480465 us: [pid:312732 tid:0x15533460c740] Arg3:  AddressC = val:23372033148928
--
:3:hip_graph.cpp            :1024: 305757611363 us: [pid:312732 tid:0x15533460c740]  hipGraphAddKernelNode ( 0x559d777c1cb0, 0x559d7f33a2c0, 0x7ffd650ed648, 1, 0x7ffd650ed2c0 ) 
:3:hip_graph_internal.cpp   :129 : 305757611376 us: [pid:312732 tid:0x15533460c740] [hipGraph] Add KernelNode(0x559d887c3bf0)
:3:hip_graph.cpp            :1036: 305757611388 us: [pid:312732 tid:0x15533460c740] hipGraphAddKernelNode: Returned hipSuccess : 
:3:hip_graph.cpp            :1024: 305757611403 us: [pid:312732 tid:0x15533460c740]  hipGraphAddKernelNode ( 0x559d777c1cb8, 0x559d7f33a2c0, 0x7ffd650ed648, 1, 0x7ffd650ed2c0 ) 
:3:hip_graph_internal.cpp   :129 : 305757611426 us: [pid:312732 tid:0x15533460c740] [hipGraph] Add KernelNode(0x559d83e52510)
:3:hip_graph.cpp            :1036: 305757611439 us: [pid:312732 tid:0x15533460c740] hipGraphAddKernelNode: Returned hipSuccess : 
:3:hip_graph.cpp            :1024: 305757611454 us: [pid:312732 tid:0x15533460c740]  hipGraphAddKernelNode ( 0x559d777c1cc0, 0x559d7f33a2c0, 0x7ffd650ed648, 1, 0x7ffd650ed2c0 ) 
:3:hip_graph.cpp            :1036: 305757611467 us: [pid:312732 tid:0x15533460c740] hipGraphAddKernelNode: Returned hipErrorInvalidConfiguration : 
E0904 10:53:24.344123  312732 pjrt_stream_executor_client.cc:2826] Execution of replica 0 failed: INTERNAL: Failed to add kernel node to a HIP graph: hipError_t(9)

```
In previous work, we worked with AMD devs to implement Managed Memory support (https://github.com/ROCm/ROCm/issues/3364) to run these large problem instances in the first place.

# Steps to reproduce

The software has been built in a container: `singularity pull colabfold.sif docker://quay.io/dipietrantonio/colabfold:v8`

Here is the Dockerfile: https://github.com/PawseySC/pawsey-containers/blob/cdp-colabfold/colabfold/colabfold.dockerfile 

Input file: https://github.com/user-attachments/files/16229258/1IH7.7.a3m.txt (remove the .txt extension)

We want the software to run on a MI250X, which are the GPUs powering the Setonix supercomputer at Pawsey Supercomputing Research Centre. We know that the same test case runs on a MI300 because it has enough memory to hold the entire computation in its GPU memory.

Script to run the test case:

```
A3M=1IH7.7.a3m # input is a multiple sequence alignment 
OUT=$MYSCRATCH/colabfold-out-1IH7.7 # name of the output directory 

# define colabfold container 
containerImage=/path/to/colabfold.sif


export SINGULARITYENV_XLA_PYTHON_CLIENT_PREALLOCATE=false
export SINGULARITYENV_TF_FORCE_UNIFIED_MEMORY="1"
export SINGULARITYENV_XLA_PYTHON_CLIENT_MEM_FRACTION="4.0"
export SINGULARITYENV_XLA_PYTHON_CLIENT_ALLOCATOR="platform"
export SINGULARITYENV_TF_FORCE_GPU_ALLOW_GROWTH="true"

openssl s_client -connect api.colabfold.com:443 

# Run colab container
singularity exec --rocm  $containerImage \
        colabfold_batch --num-recycle 5 --pair-mode unpaired --model-type alphafold2_multimer_v3 --num-models 3 $A3M $OUT
```


### Operating System

Ubuntu 22 (in a container)

### CPU

AMD Milan (zen3) CPU

### GPU

MI250X

### ROCm Version

ROCm 6.2.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

This ticket is a continuation of https://github.com/ROCm/ROCm/issues/3364 