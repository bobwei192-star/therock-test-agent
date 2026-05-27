# roctracer matrixtransport_test example can not run with rocprof

> **Issue #1533**
> **状态**: closed
> **创建时间**: 2021-07-21T20:03:00Z
> **更新时间**: 2022-02-08T13:59:26Z
> **关闭时间**: 2022-02-08T13:59:26Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1533

## 描述

The problem with Makefile in the test utility called MatrixTransport_test is 
ROCM_LIBS appears to be defined to include all lib binaries in the executable.
Then there seems dynamic on the fly loading of libraries under test target with LD_PRELOAD.
But if I run executable alone it will not work since libraries under preload is missing.

if I insert rocprof in the LD_PRELOAD line, it just does not work.
So I inserted all *.so in LD_PRELOAD section to ROCM_LIBS definition to include all *so in the file and build OK.

```
ROC_LIBS  = -Wl,--rpath,${LIB_PATH} \
    $(LIB_PATH)/libroctracer64.so \
    $(LIB_PATH)/libroctx64.so \
    $(LIB_PATH)/libkfdwrapper64.so \
    $(ROCM_PATH)/hip/lib/libamdhip64.so \
    $(ROCM_PATH)/lib/libamdhip64.so \
    $(ROCM_PATH)/rocprofiler/lib/librocprofiler64.so
```

Now I can run it with LD_PRELOAD-ing all these library directly from command line. 
But when i try run with rocprof (created make testp target for this or just run "rocprof ./MatrixTranspose", it still fails:

```
./MatrixTranspose
...
	CopyDeviceToHost	correlation_id(526) time_ns(44252958426514:44252958898300) device_id(0) queue_id(0) bytes(0x0)
	CopyHostToDevice	correlation_id(533) time_ns(44252982401976:44252982888978) device_id(0) queue_id(0) bytes(0x0)
	KernelExecution	correlation_id(536) time_ns(44252983172576:44252983267295) device_id(0) queue_id(0)
	CopyDeviceToHost	correlation_id(537) time_ns(44252985257054:44252985712151) device_id(0) queue_id(0) bytes(0x0)
	CopyHostToDevice	correlation_id(544) time_ns(44253008996492:44253009513874) device_id(0) queue_id(0) bytes(0x0)
	KernelExecution	correlation_id(547) time_ns(44253009794770:44253009886770) device_id(0) queue_id(0)
	CopyDeviceToHost	correlation_id(548) time_ns(44253011963089:44253012423306) device_id(0) queue_id(0) bytes(0x0)

```
make testp (run without preloading + rocprof, fail)
```
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make clean && make && make testp
rm -f ./MatrixTranspose
rm -f MatrixTranspose.o
rm -f /opt/rocm/hip/src/*.o
rm -f ./MatrixTranspose
rm -f MatrixTranspose.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g -I../../inc -I/opt/rocm/roctracer/include -I/opt/rocm/hsa/include/hsa -I/opt/rocm/hsa/include -I/opt/rocm/hip/include -I/opt/rocm/include -DLOCAL_BUILD=1 -DHIP_VDI=0 -DITERATIONS=100 -DAMD_INTERNAL_BUILD=1 -DHIP_TEST=1 --rocm-path=/opt/rocm -c -o MatrixTranspose.o MatrixTranspose.cpp
/opt/rocm/hip/bin/hipcc MatrixTranspose.o -o MatrixTranspose -Wl,--rpath,../../build ../../build/libroctracer64.so ../../build/libroctx64.so ../../build/libkfdwrapper64.so /opt/rocm/hip/lib/libamdhip64.so /opt/rocm/lib/libamdhip64.so /opt/rocm/rocprofiler/lib/librocprofiler64.so
rocprof ./MatrixTranspose
RPL: on '210721_130130' from '/opt/rocm-4.2.0/rocprofiler' in '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test'
RPL: profiling '"./MatrixTranspose"'
RPL: input file ''
RPL: output dir '/tmp/rpl_data_210721_130130_12365'
RPL: result dir '/tmp/rpl_data_210721_130130_12365/input_results_210721_130130'
roctracer: Loading 'libamdhip64.so' failed, (null)
/usr/bin/rocprof: line 272: 12388 Aborted                 (core dumped) "./MatrixTranspose"
File '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test/results.csv' is generating
Makefile:63: recipe for target 'testp' failed
make: *** [testp] Error 134
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# 
```

---

## 评论 (11 条)

### 评论 #1 — ROCmSupport (2021-07-27T07:07:00Z)

Thanks @gggh000 for reaching out.
Let me take a look.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-07-27T12:35:58Z)

This issue can be looked into, once #1532 is resolved

---

### 评论 #3 — gggh000 (2021-08-06T05:56:44Z)

Hi, this appears very similar to #1532 but actually it is very distinct.
On 1532, it is all about building and running MatrixTranspose_test and run OK.
However this issue, once MatrixTranspose_test is run with rocprof. 

Thanks., 

---

### 评论 #4 — gggh000 (2021-08-09T16:57:42Z)

The comment above original no longer builds. It is not certain what I omitted. In the makefile, I had to include roctracer path as include with -I flag but roctracer_hip.h include statement always errors out. It perplexes me because another file called roctracer.h file in the same location includes OK.

```
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make
rm -f ./MatrixTranspose
rm -f MatrixTranspose.o
rm -f /opt/rocm/hip/src/*.o
/opt/rocm/hip/bin/hipcc -g -I../../inc -I/opt/rocm/roctracer/include/hip_ostream_ops.h -I/opt/rocm/hsa/include/hsa -I/opt/rocm/hsa/include -I/opt/rocm/hip/include -I/opt/rocm/include -DLOCAL_BUILD=1 -DHIP_VDI=0 -DITERATIONS=100 -DAMD_INTERNAL_BUILD=1 -DHIP_TEST=1 --rocm-path=/opt/rocm -c -o MatrixTranspose.o MatrixTranspose.cpp
In file included from MatrixTranspose.cpp:234:
../../inc/roctracer_hip.h:41:10: fatal error: 'hip_ostream_ops.h' file not found
#include <hip_ostream_ops.h>
         ^~~~~~~~~~~~~~~~~~~



-FLAGS =-g $(INC_PATH:%=-I%) -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include -I$(ROCM_PATH)/hip/include -I$(ROCM_PATH)/include -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1
+FLAGS =-g $(INC_PATH:%=-I%) \
+    -I$(ROCM_PATH)/roctracer/include/hip_ostream_ops.h \
+    -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include \
+    -I$(ROCM_PATH)/hip/include \
+    -I$(ROCM_PATH)/include \
+    -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1


root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# find /opt -name hip_ostream_ops.h
/opt/rocm-4.2.0/roctracer/include/hip_ostream_ops.h
/opt/rocm-4.2.0/include/roctracer/hip_ostream_ops.h
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# find /opt -name roctracer.h
/opt/rocm-4.2.0/roctracer/include/roctracer.h
/opt/rocm-4.2.0/include/roctracer/roctracer.h


--- a/inc/roctracer_hip.h
+++ b/inc/roctracer_hip.h
@@ -37,11 +37,11 @@ inline static std::ostream& operator<<(std::ostream& out, const char& v) {
 }
 #endif  // __cplusplus
 
-#include <hip/hip_runtime.h>
+#include <roctracer.h>
 #include <hip_ostream_ops.h>
+#include <hip/hip_runtime.h>
 #include <hip/amd_detail/hip_prof_str.h>
 
-#include <roctracer.h>

```

---

### 评论 #5 — gggh000 (2021-08-09T16:59:02Z)

It builds ok after correcting include to take out bolded file name, so this include may need to be necessary to be able to build:

```
-    -I$(ROCM_PATH)/roctracer/include/hip_ostream_ops.h \
+    -I$(ROCM_PATH)/roctracer/include/ \
+    -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include \
+    -I$(ROCM_PATH)/hip/include \
+    -I$(ROCM_PATH)/include \
+    -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1

 test: $(EXECUTABLE)
-       LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so" $(EXECUTABLE)
+       LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so $(ROCM_PATH)/lib/libamdhip64.so" $(EXECUTABLE)

```

---

### 评论 #6 — gggh000 (2021-08-09T17:35:43Z)

Here is my output. I created testp target in the Makefile same as test target except there is rocprof inserted once before PRELOAD statement or before EXECUTABLE itself. Having not be able to use with rocprof seems to defeat the very this example at least partially in that we can not generate trace file i.e. json and open in tracer app i.e. chrome://tracing. 

```

root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make testp
LD_PRELOAD="../../build/libkfdwrapper64.so librocprofiler64.so /opt/rocm/lib/libamdhip64.so" rocprof ./MatrixTranspose
RPL: on '210809_103253' from '/opt/rocm-4.2.0/rocprofiler' in '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test'
RPL: profiling '"./MatrixTranspose"'
RPL: input file ''
RPL: output dir '/tmp/rpl_data_210809_103253_2838'
RPL: result dir '/tmp/rpl_data_210809_103253_2838/input_results_210809_103253'
roctracer: Loading 'libamdhip64.so' failed, (null)
/usr/bin/rocprof: line 272:  2861 Aborted                 (core dumped) "./MatrixTranspose"
File '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test/results.csv' is generating
Makefile:63: recipe for target 'testp' failed
make: *** [testp] Error 134
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# git diff
diff --git a/test/MatrixTranspose_test/Makefile b/test/MatrixTranspose_test/Makefile
index 758f8d9..0ce44e2 100644
--- a/test/MatrixTranspose_test/Makefile
+++ b/test/MatrixTranspose_test/Makefile
@@ -4,8 +4,14 @@ LIB_PATH  ?= $(ROOT_PATH)/build
 ROCM_PATH ?= /opt/rocm
 HIP_VDI ?= 0
 ITERATIONS ?= 100
-
-ROC_LIBS  = -Wl,--rpath,${LIB_PATH} $(LIB_PATH)/libroctracer64.so $(LIB_PATH)/libroctx64.so
+C_TEST=0
+ROC_LIBS  = -Wl,--rpath,${LIB_PATH} \
+    $(LIB_PATH)/libroctracer64.so \
+    $(LIB_PATH)/libroctx64.so \
+    $(LIB_PATH)/libkfdwrapper64.so \
+    $(ROCM_PATH)/hip/lib/libamdhip64.so \
+    $(ROCM_PATH)/lib/libamdhip64.so \
+    $(ROCM_PATH)/rocprofiler/lib/librocprofiler64.so
 
 HIP_PATH ?= $(wildcard /opt/rocm/hip)
 ifeq (,$(HIP_PATH))
@@ -17,7 +23,12 @@ TARGET=hcc
 
 EXECUTABLE=./MatrixTranspose
 OBJECTS = MatrixTranspose.o
-FLAGS =-g $(INC_PATH:%=-I%) -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include -I$(ROCM_PATH)/hip/include -I$(ROCM_PATH)/include -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1
+FLAGS =-g $(INC_PATH:%=-I%) \
+    -I$(ROCM_PATH)/roctracer/include/ \
+    -I$(ROCM_PATH)/hsa/include/hsa -I$(ROCM_PATH)/hsa/include \
+    -I$(ROCM_PATH)/hip/include \
+    -I$(ROCM_PATH)/include \
+    -DLOCAL_BUILD=1 -DHIP_VDI=${HIP_VDI} -DITERATIONS=$(ITERATIONS) -DAMD_INTERNAL_BUILD=1
 
 ifeq ($(C_TEST), 1)
        COMP=${CC}
@@ -46,7 +57,10 @@ $(EXECUTABLE): $(OBJECTS)
        $(HIPCC) $(OBJECTS) -o $@ $(ROC_LIBS)
 
 test: $(EXECUTABLE)
-       LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so" $(EXECUTABLE)
+       LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so $(ROCM_PATH)/lib/libamdhip64.so" $(EXECUTABLE)
+
+testp: $(EXECUTABLE)
+       LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so $(ROCM_PATH)/lib/libamdhip64.so" rocprof $(EXECUTABLE)
 
 clean:
        rm -f $(EXECUTABLE)
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# nano -w Makefile ^C
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make testp
LD_PRELOAD="../../build/libkfdwrapper64.so librocprofiler64.so /opt/rocm/lib/libamdhip64.so" rocprof ./MatrixTranspose
RPL: on '210809_103306' from '/opt/rocm-4.2.0/rocprofiler' in '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test'
RPL: profiling '"./MatrixTranspose"'
RPL: input file ''
RPL: output dir '/tmp/rpl_data_210809_103306_2892'
RPL: result dir '/tmp/rpl_data_210809_103306_2892/input_results_210809_103306'
roctracer: Loading 'libamdhip64.so' failed, (null)
/usr/bin/rocprof: line 272:  2915 Aborted                 (core dumped) "./MatrixTranspose"
File '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test/results.csv' is generating
Makefile:63: recipe for target 'testp' failed
make: *** [testp] Error 134
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# git diff Makefile | grep testp -A 2
+testp: $(EXECUTABLE)
+	LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so $(ROCM_PATH)/lib/libamdhip64.so" rocprof $(EXECUTABLE)
 
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# nano -w Makefile 
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# make testp
rocprof LD_PRELOAD="../../build/libkfdwrapper64.so librocprofiler64.so /opt/rocm/lib/libamdhip64.so" ./MatrixTranspose
RPL: on '210809_103329' from '/opt/rocm-4.2.0/rocprofiler' in '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test'
RPL: profiling '"LD_PRELOAD=../../build/libkfdwrapper64.so librocprofiler64.so /opt/rocm/lib/libamdhip64.so" "./MatrixTranspose"'
RPL: input file ''
RPL: output dir '/tmp/rpl_data_210809_103329_2944'
RPL: result dir '/tmp/rpl_data_210809_103329_2944/input_results_210809_103329'
/usr/bin/rocprof: line 272: LD_PRELOAD=../../build/libkfdwrapper64.so librocprofiler64.so /opt/rocm/lib/libamdhip64.so: No such file or directory
File '/root/ROCm-4.2/roctracer/test/MatrixTranspose_test/results.csv' is generating
Makefile:63: recipe for target 'testp' failed
make: *** [testp] Error 127
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# git diff Makefile | grep testp -A 2
+testp: $(EXECUTABLE)
+	rocprof LD_PRELOAD="$(LIB_PATH)/libkfdwrapper64.so librocprofiler64.so $(ROCM_PATH)/lib/libamdhip64.so" $(EXECUTABLE)
 
root@nonroot-Standard-PC-i440FX-PIIX-1996:~/ROCm-4.2/roctracer/test/MatrixTranspose_test# 

```

---

### 评论 #7 — gggh000 (2021-08-30T07:43:25Z)

any update?

---

### 评论 #8 — ROCmSupport (2021-09-23T11:21:08Z)

Hi @gggh000 
Let me check this on the latest build and will update soon.
Thank you.

---

### 评论 #9 — gggh000 (2021-10-25T19:10:54Z)

any update?

---

### 评论 #10 — ROCmSupport (2021-12-28T05:44:31Z)

Hi @gggh000 
I am not able to reproduce with 4.5.2 + docs.
Can you please give a check and update.
If you still see the same or different issue, can you please share the exact steps to reproduce the problem.
Thank you.

---

### 评论 #11 — ROCmSupport (2022-02-08T13:59:26Z)

Closing this as there is no update for a long time.
Request to file a new issues, if any, for quick resolutions. Thank you.

---
