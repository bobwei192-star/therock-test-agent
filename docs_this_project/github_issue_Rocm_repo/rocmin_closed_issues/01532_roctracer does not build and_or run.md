# roctracer does not build and/or run

- **Issue #:** 1532
- **State:** closed
- **Created:** 2021-07-21T17:32:53Z
- **Updated:** 2024-01-11T04:21:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1532

I had build going by changing Makefile as follows but make test still fails due to missing library:
Rocm4.2 on ubuntu1804:

```
diff --git a/test/MatrixTranspose_test/Makefile b/test/MatrixTranspose_test/Makefile
index 758f8d9..aeb65d3 100644
--- a/test/MatrixTranspose_test/Makefile
+++ b/test/MatrixTranspose_test/Makefile
@@ -5,6 +5,7 @@ ROCM_PATH ?= /opt/rocm
 HIP_VDI ?= 0
 ITERATIONS ?= 100
 
 ROC_LIBS  = -Wl,--rpath,${LIB_PATH} $(LIB_PATH)/libroctracer64.so $(LIB_PATH)/libroctx64.so
 
 HIP_PATH ?= $(wildcard /opt/rocm/hip)
@@ -17,7 +18,7 @@ TARGET=hcc
 
 EXECUTABLE=./MatrixTranspose
 OBJECTS = MatrixTranspose.o
-FLAGS =-g $(INC_PATH:%=-I%) -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include -I$(ROCM_PATH)/hip/include -I$(ROCM_PATH)/include -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1
+FLAGS =-g $(INC_PATH:%=-I%) -I$(ROCM_PATH)/roctracer/include -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include -I$(ROCM_PATH)/hip/include -I$(ROCM_PATH)/include -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1
 
 ifeq ($(C_TEST), 1)
        COMP=${CC}
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make test
LD_PRELOAD="../../build/libkfdwrapper64.so librocprofiler64.so" ./MatrixTranspose
# INIT #############################
roctracer: Loading 'libamdhip64.so' failed, (null)
Aborted (core dumped)
Makefile:50: recipe for target 'test' failed
make: *** [test] Error 134
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# 

```
