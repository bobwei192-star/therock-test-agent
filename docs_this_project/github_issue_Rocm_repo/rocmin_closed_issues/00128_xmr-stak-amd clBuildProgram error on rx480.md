# xmr-stak-amd clBuildProgram error on rx480

- **Issue #:** 128
- **State:** closed
- **Created:** 2017-06-15T11:00:48Z
- **Updated:** 2018-10-11T23:40:09Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/128

I am getting clBuildProgram error when running xmr-stak-amd (opencl monero miner).
The issue is reported also here: https://github.com/fireice-uk/xmr-stak-amd/issues/48

The error is
```
[2017-06-13 12:25:15] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
```
here is the full log
```
$ ./bin/xmr-stak-amd config.txt 
[2017-06-13 12:25:12] : Compiling code and initializing GPUs. This will take a while...
Profiling is not available
[2017-06-13 12:25:12] : Device 0 work size 8 / 256.
clang version 4.0 
Target: amdgcn-amd-amdhsa-opencl
Thread model: posix
InstalledDir: /opt/rocm/opencl/bin/x86_64
[2017-06-13 12:25:15] : Error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram.
Build log:
warning: argument unused during compilation: '-I .'
error: unable to execute command: Segmentation fault (core dumped)
error: clang frontend command failed due to signal (use -v to see invocation)
note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated run script.
note: diagnostic msg: Error generating preprocessed source(s) - no preprocessable inputs.
/opt/rocm/opencl/bin/x86_64/clang[0x217c00a]
/opt/rocm/opencl/bin/x86_64/clang[0x217a3be]
/opt/rocm/opencl/bin/x86_64/clang[0x217a510]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x11390)[0x7f19c6640390]
/opt/rocm/opencl/bin/x86_64/clang[0x13d53e4]
/opt/rocm/opencl/bin/x86_64/clang[0x13b88aa]
/opt/rocm/opencl/bin/x86_64/clang[0x1743007]
/opt/rocm/opencl/bin/x86_64/clang[0x20cbcea]
/opt/rocm/opencl/bin/x86_64/clang[0x20cbd83]
/opt/rocm/opencl/bin/x86_64/clang[0x20cc77f]
/opt/rocm/opencl/bin/x86_64/clang[0x598456]
/opt/rocm/opencl/bin/x86_64/clang[0x59a8a3]
/opt/rocm/opencl/bin/x86_64/clang[0x576ceb]
/opt/rocm/opencl/bin/x86_64/clang[0x8ed2ae]
/opt/rocm/opencl/bin/x86_64/clang[0x8c2ad5]
/opt/rocm/opencl/bin/x86_64/clang[0x5720bd]
/opt/rocm/opencl/bin/x86_64/clang[0x56f208]
/opt/rocm/opencl/bin/x86_64/clang[0x52326a]
/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf0)[0x7f19c6286830]
/opt/rocm/opencl/bin/x86_64/clang[0x5694c1]
Stack dump:
0.	Program arguments: /opt/rocm/opencl/bin/x86_64/clang -cc1 -triple amdgcn-amd-amdhsa-opencl -emit-obj -disable-free -disable-llvm-verifier -discard-value-names -main-file-name t_19803_47.bc -mrelocation-model static -mthread-model posix -mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases -target-cpu fiji -dwarf-column-info -debugger-tuning=gdb -resource-dir /opt/rocm/opencl/bin/lib/clang/4.0 -O3 -fdebug-compilation-dir /home/gsedej/git/xmr-stak-amd -ferror-limit 19 -fmessage-length 192 -cl-kernel-arg-info -fobjc-runtime=gcc -fdiagnostics-show-option -vectorize-loops -vectorize-slp -mllvm -amdgpu-internalize-symbols -mllvm -amdgpu-early-inline-all -o /tmp/t_19803_47-8cf830.o -x ir /tmp/AMD_19803_32/t_19803_47.bc 
1.	Code generation
2.	Running pass 'Function Pass Manager' on module '/tmp/AMD_19803_32/t_19803_47.bc'.
3.	Running pass 'SI Fix SGPR copies' on function '@cn0'
Error: Creating the executable failed: Compiling LLVM IRs to executable
```

Can I get more log/debug?

