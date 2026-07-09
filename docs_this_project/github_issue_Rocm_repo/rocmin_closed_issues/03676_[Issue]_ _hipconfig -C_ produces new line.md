# [Issue]: `hipconfig -C` produces new line

- **Issue #:** 3676
- **State:** closed
- **Created:** 2024-09-04T15:34:57Z
- **Updated:** 2024-09-05T07:10:20Z
- **Labels:** Under Investigation, AMD Instinct MI300X, AMD Instinct MI300A, AMD Instinct MI250X, ROCm 6.0.0, ROCm 5.7.1, ROCm 5.6.0, ROCm 5.7.0, ROCm 6.1.0, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3676

### Problem Description

```shell
$ echo "'$(/opt/rocm-5.5.1/bin/hipconfig.pl -C)'"
' -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-5.5.1/include -I/opt/rocm-5.5.1/llvm/bin/../lib/clang/16.0.0 '
$ echo "'$(/opt/rocm-5.7.1/bin/hipconfig.pl -C)'"
' -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/lus/home/softs/rocm/5.7.1/include -I/lus/home/softs/rocm/5.7.1/llvm/lib/clang/17.0.0
 '
```

Notice the new line on the second command ? This is because at some ponit between 5.5.1 and 5.7.1, hipconfig changed its way of finding include path.
![image](https://github.com/user-attachments/assets/327ae8c3-a2ce-40f4-887b-61a7108e8d5f)

clang returns a new line:
```
$ /opt/rocm/6.0.0//llvm/bin/clang++ --print-resource-dir
/lus/home/softs/rocm/6.0.0/lib/llvm/lib/clang/17.0.0
```

I believe a strip of white space chars should be done both before and after what clangs return.

### Operating System

RHEL

### GPU

AMD Instinct MI300X, AMD Instinct MI300A, AMD Instinct MI250X

### ROCm Version

ROCm 6.1.0, ROCm 6.0.0, ROCm 5.7.1, ROCm 5.7.0, ROCm 5.6.0
