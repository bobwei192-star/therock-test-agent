# roctracer does not build and/or run

> **Issue #1532**
> **状态**: closed
> **创建时间**: 2021-07-21T17:32:53Z
> **更新时间**: 2024-01-11T04:21:35Z
> **关闭时间**: 2024-01-11T04:21:35Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1532

## 描述

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


---

## 评论 (7 条)

### 评论 #1 — gggh000 (2021-07-21T17:47:32Z)

Following modification in test/MatrixTranspose_test make it working both build and run:

```
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# git diff
diff --git a/test/MatrixTranspose_test/Makefile b/test/MatrixTranspose_test/Makefile
index 758f8d9..c796f5b 100644
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
@@ -46,7 +47,7 @@ $(EXECUTABLE): $(OBJECTS)
        $(HIPCC) $(OBJECTS) -o $@ $(ROC_LIBS)
 
 test: $(EXECUTABLE)
-       LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so" $(EXECUTABLE)
+       LD_PRELOAD="$(ROCM_PATH)/lib/libamdhip64.so $(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so" $(EXECUTABLE)
 
 clean:
        rm -f $(EXECUTABLE)

root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# 
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# 



---

### 评论 #2 — ROCmSupport (2021-07-27T07:06:07Z)

Thanks @gggh000 for reaching out.
Let me take a look.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-07-27T12:32:35Z)

I am also not able to compile the test locally.
taccuser@taccuser-GA-990FXA-UD5:~/roctracer/test/MatrixTranspose_test$ make
rm -f ./MatrixTranspose
rm -f MatrixTranspose.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g -I../../inc -I/opt/rocm/roctracer/include -I/opt/rocm/hsa/include/hsa -I/opt/rocm/hsa/include -I/opt/rocm/hip/include -I/opt/rocm/include -DLOCAL_BUILD=1 -DHIP_VDI=0 -DITERATIONS=100 -DAMD_INTERNAL_BUILD=1 -DHIP_TEST=1 --rocm-path=/opt/rocm -c -o MatrixTranspose.o MatrixTranspose.cpp
/opt/rocm/hip/bin/hipcc MatrixTranspose.o -o MatrixTranspose -Wl,--rpath,../../build ../../build/libroctracer64.so ../../build/libroctx64.so
clang-12: error: no such file or directory: '../../build/libroctracer64.so'
clang-12: error: no such file or directory: '../../build/libroctx64.so'
make: *** [Makefile:46: MatrixTranspose] Error 1


---

### 评论 #4 — gggh000 (2021-07-27T23:17:03Z)

This is as I found out, you want to build the roctracer first before building matrix test. That would those *.so files. Or you can modify Makefile to point to one in the /opt/rocm directory. 
```
clang-12: error: no such file or directory: '../../build/libroctracer64.so'
clang-12: error: no such file or directory: '../../build/libroctx64.so'

```
That itself was tricky:
I had to following prior:
```
apt install rpm
pip3 install cppheaderparser
invoke build.sh
```

---

### 评论 #5 — ROCmSupport (2022-02-08T13:51:23Z)

I am still able to reproduce this problem with 4.5 code and increased the severity of this issue and assigned to dev.

---

### 评论 #6 — abhimeda (2024-01-02T15:51:13Z)

Is the issue still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #7 — nartmada (2024-01-11T04:21:35Z)

According to the internal ticket associated with this issue, we need to build roctracer before building the test app.  

---
