# Packages llvm-amdgpu, hsa-amd-aqlprofile still have rocm-3.7.0 in path

> **Issue #1260**
> **状态**: closed
> **创建时间**: 2020-10-15T14:48:15Z
> **更新时间**: 2020-11-03T06:35:44Z
> **关闭时间**: 2020-11-03T06:35:44Z
> **作者**: apalazzi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1260

## 描述

Hi,

I have the rocm packages installed from the repository deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main , however it seems that with the release of 3.8.0 not all packages have been updated to reflect the version change; this results in an error when I run my pytorch app:

```
MIOpen(HIP): Error [ValidateGcnAssemblerImpl] Wrong path to assembler: '/opt/rocm/llvm/bin/clang'. Expect performance degradation.
/opt/rocm-3.8.0/bin/clang-ocl: line 49: /opt/rocm-3.8.0/llvm/bin/clang: No such file or directory
MIOpen Error: /root/driver/MLOpen/src/tmp_dir.cpp:47: Can't execute cd /tmp/miopen-MIOpenIm2d2Col.cl-a714-c510-c4ee-9d34; /opt/rocm-3.8.0/bin/clang-ocl  -DNUM_CH_PER_WG=1 -DNUM_IM_BLKS_X=10 -DNUM_IM_BLKS=380 -DLOCAL_MEM_SIZE=340 -DSTRIDE_GT_1=0 -DTILE_SZ_X=32 -DTILE_SZ_Y=8 -DUSE_IM_OFF_GUARD=1 -DMIOPEN_USE_FP16=0 -DMIOPEN_USE_FP32=1 -DMIOPEN_USE_INT8=0 -DMIOPEN_USE_INT8x4=0 -DMIOPEN_USE_BFP16=0 -DMIOPEN_USE_INT32=0 -DMIOPEN_USE_RNE_BFLOAT16=1 -mcpu=gfx900 -Wno-everything -Xclang -target-feature -Xclang +code-object-v3 MIOpenIm2d2Col.cl -o /tmp/miopen-MIOpenIm2d2Col.cl-a714-c510-c4ee-9d34/MIOpenIm2d2Col.cl.o
Traceback (most recent call last):
  File "train.py", line 162, in <module>
    main()
  File "train.py", line 91, in main
    train(train_loader=train_loader,
  File "train.py", line 129, in train
    predicted_locs, predicted_scores = model(images)  # (N, 8732, 4), (N, 8732, n_classes)
  File "/home/andrea/.local/lib/python3.8/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/home/andrea/src/ai/autodwg-sdd/model.py", line 353, in forward
    conv4_3_feats, conv7_feats = self.base(image)  # (N, 512, 38, 38), (N, 1024, 19, 19)
  File "/home/andrea/.local/lib/python3.8/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/home/andrea/src/ai/autodwg-sdd/model.py", line 58, in forward
    out = F.relu(self.conv1_1(image))  # (N, 64, 300, 300)
  File "/home/andrea/.local/lib/python3.8/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/home/andrea/.local/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 419, in forward
    return self._conv_forward(input, self.weight)
  File "/home/andrea/.local/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 415, in _conv_forward
    return F.conv2d(input, weight, self.bias, self.stride,
RuntimeError: miopenStatusUnknownError
```

Clang is actually under the directory /opt/rocm-3.7.0:
```
andrea@marcopolo:~$ ls /opt/
containerd  rocm  rocm-3.7.0  rocm-3.8.0
andrea@marcopolo:~$ ls /opt/rocm-3.7.0/
hsa  hsa-amd-aqlprofile  lib  llvm
andrea@marcopolo:~$ ls /opt/rocm-3.7.0/llvm/bin/
bugpoint                  clang-query           llvm-addr2line   llvm-elfabi             llvm-objcopy     llvm-undname
c-index-test              clang-refactor        llvm-ar          llvm-exegesis           llvm-objdump     llvm-xray
clang                     clang-rename          llvm-as          llvm-extract            llvm-opt-report  modularize
clang++                   clang-reorder-fields  llvm-bcanalyzer  llvm-gsymutil           llvm-pdbutil     obj2yaml
clang-11                  clang-scan-deps       llvm-c-test      llvm-ifs                llvm-profdata    opt
clang-apply-replacements  clang-tidy            llvm-cat         llvm-install-name-tool  llvm-ranlib      pp-trace
clang-change-namespace    clangd                llvm-cfi-verify  llvm-jitlink            llvm-rc          sancov
clang-check               diagtool              llvm-config      llvm-lib                llvm-readelf     sanstats
clang-cl                  dsymutil              llvm-cov         llvm-link               llvm-readobj     scan-build
clang-cpp                 find-all-symbols      llvm-cvtres      llvm-lipo               llvm-reduce      scan-view
clang-doc                 git-clang-format      llvm-cxxdump     llvm-lto                llvm-rtdyld      verify-uselistorder
clang-extdef-mapping      hmaptool              llvm-cxxfilt     llvm-lto2               llvm-size        wasm-ld
clang-format              ld.lld                llvm-cxxmap      llvm-mc                 llvm-split       yaml2obj
clang-import-test         ld64.lld              llvm-diff        llvm-mca                llvm-stress
clang-include-fixer       llc                   llvm-dis         llvm-ml                 llvm-strings
clang-move                lld                   llvm-dlltool     llvm-modextract         llvm-strip
clang-offload-bundler     lld-link              llvm-dwarfdump   llvm-mt                 llvm-symbolizer
clang-offload-wrapper     lli                   llvm-dwp         llvm-nm                 llvm-tblgen
andrea@marcopolo:~$ wajig whichpkg /opt/rocm-3.7.0 
INSTALLED MATCHES (x1)
----------------------
llvm-amdgpu, hsa-amd-aqlprofile: /opt/rocm-3.7.0
```


---

## 评论 (7 条)

### 评论 #1 — rkothako (2020-10-15T15:09:08Z)

Thanks @apalazzi for the issue logged.
Can you please share the files/folders under /opt/rocm-3.8.0 also.
Like **ls -l /opt/rocm-3.8.0**

---

### 评论 #2 — apalazzi (2020-10-15T15:17:00Z)

Note: this is after uninstalling and reinstalling rocm as described in https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html# :
```
andrea@marcopolo:~$ LC_ALL=C ls -l /opt/rocm-3.8.0/
total 64
drwxr-xr-x  2 root root 4096 Oct 15 17:02 bin
drwxr-xr-x  8 root root 4096 Oct 15 17:02 hip
drwxr-xr-x  4 root root 4096 Oct  8 18:00 hipcub
drwxr-xr-x  4 root root 4096 Oct  8 18:03 hsa
drwxr-xr-x  3 root root 4096 Oct 15 17:02 hsa-amd-aqlprofile
drwxr-xr-x  8 root root 4096 Oct 15 17:02 include
drwxr-xr-x  3 root root 4096 Oct 15 17:04 lib
drwxr-xr-x  4 root root 4096 Oct  8 18:00 miopengemm
drwxr-xr-x  4 root root 4096 Oct 15 17:02 oam
drwxr-xr-x  5 root root 4096 Oct 15 17:02 opencl
drwxr-xr-x  4 root root 4096 Oct  8 18:00 rccl
drwxr-xr-x  5 root root 4096 Oct 15 17:02 rocm_smi
drwxr-xr-x  4 root root 4096 Oct  8 18:00 rocprim
drwxr-xr-x  6 root root 4096 Oct 15 17:02 rocprofiler
drwxr-xr-x  5 root root 4096 Oct 15 17:02 roctracer
drwxr-xr-x 10 root root 4096 Oct 15 17:02 share
andrea@marcopolo:~$ 
```

Is there a way to have a working pytorch environment?


---

### 评论 #3 — rkothako (2020-10-15T15:29:40Z)

Hi @apalazzi 
Looks like un-installation of 3.7 did not go well in your machine.
Can you please try uninstall ROCm completely once again and make sure that all packages are removed before you install 3.8.
Recommend to check sudo dpkg -l | grep hsa  . Replace hsa with hip, llvm, rocm, rock and make sure that all packages are removed. Recommend to do the same for all other additional packages also if you installed anything explictely.

Once you make sure that its clean, now try to install ROCm 3.8.
I hope this helps.

---

### 评论 #4 — apalazzi (2020-10-15T15:39:43Z)

Ok, I'll try again; in the meantime, can someone update the documentation page? If I do as it's described in the page not all the packages are removed:
```
andrea@marcopolo:~/$ sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils
[...removing things...]
andrea@marcopolo:~/git$ ls /opt/
containerd  rocm-3.7.0  rocm-3.8.0
andrea@marcopolo:~/git$ ls /opt/rocm-3.8.0/
bin  hip  hipcub  hsa  include  lib  miopengemm  rccl  rocprim  share
andrea@marcopolo:~/git$ ls /opt/rocm-3.7.0/
hsa  lib  llvm
andrea@marcopolo:~/git$ sudo dpkg -l | grep hsa
ii  hsa-rocr-dev                                     1.2.30800.0-rocm-rel-3.8-30-7c99b7aa                 amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms
ii  hsakmt-roct                                      1.0.9-366-g80210f0                                   amd64        HSAKMT library for AMD KFD support
andrea@marcopolo:~/git$
```


---

### 评论 #5 — rkothako (2020-10-16T04:13:10Z)

Hi @apalazzi,
Please confirm once you uninstall all packages explicitly and able to install 3.8.

---

### 评论 #6 — apalazzi (2020-10-20T15:28:19Z)

Hi,
After uninstalling and reinstalling all the rocm packages, it now works correctly.

---

### 评论 #7 — rkothako (2020-11-02T10:46:27Z)

Thanks @apalazzi for the confirmation. You can close this ticket now.

---
