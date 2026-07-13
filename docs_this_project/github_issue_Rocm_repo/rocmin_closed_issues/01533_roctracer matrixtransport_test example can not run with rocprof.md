# roctracer matrixtransport_test example can not run with rocprof

- **Issue #:** 1533
- **State:** closed
- **Created:** 2021-07-21T20:03:00Z
- **Updated:** 2022-02-08T13:59:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/1533

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