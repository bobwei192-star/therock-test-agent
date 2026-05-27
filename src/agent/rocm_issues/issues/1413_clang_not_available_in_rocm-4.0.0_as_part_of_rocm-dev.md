# clang not available in rocm-4.0.0 as part of rocm-dev

> **Issue #1413**
> **状态**: closed
> **创建时间**: 2021-03-21T08:51:31Z
> **更新时间**: 2021-03-22T08:47:28Z
> **关闭时间**: 2021-03-22T08:47:28Z
> **作者**: drajarshi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1413

## 描述

Hello

I installed rocm-dev  as below:

_$ sudo yum install rocm-dev_

The install was successful. 
_[ec2-user@ip-172-31-35-60 llvm]$ sudo yum list installed | grep rocm-dev
rocm-dev.x86_64                 4.0.0.40000-23.el7             @ROCm            
rocm-device-libs.x86_64         1.0.0.637_rocm_rel_4.0_23_db8c0c3-1_

I want to build and run the veccopy example program.
However, clang which is required for this, is not available as part of the rocm-4.0.0 package.

_[ec2-user@ip-172-31-35-60 llvm]$ pwd
/opt/rocm-4.0.0/llvm
[ec2-user@ip-172-31-35-60 llvm]$ ls -l bin/
total 6120
-rwxr-xr-x 1 root root 4077712 Dec 14 11:19 flang1
-rwxr-xr-x 1 root root 2186696 Dec 14 11:19 flang2_

What do I need to do in order to install clang? 
This issue is not seen with rock-dkms or AOMP however, I can not install any of them since I want only the userspace code for rocm.

Thanks
Rajarshi Das

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-03-22T08:42:56Z)

Thanks @drajarshi for reaching out.
Let me check and get back to you soon.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-03-22T08:47:28Z)

Hi @drajarshi 
clang is part of llvm package and so you can check under /opt/rocm/llvm/bin
Hope this helps.
Thank you.

taccuser@taccuser-All-Series:/opt/rocm/llvm/bin$ ls
aompcc                    clang-include-fixer    flang2              llvm-cfi-verify  llvm-gsymutil           llvm-objcopy     llvm-symbolizer
bugpoint                  clang-move             git-clang-format    llvm-config      llvm-ifs                llvm-objdump     llvm-tblgen
c-index-test              clang-nvlink-wrapper   gputable.txt        llvm-cov         llvm-install-name-tool  llvm-opt-report  llvm-undname
**clang**                     clang-offload-bundler  hmaptool            llvm-c-test      llvm-jitlink            llvm-pdbutil     llvm-xray
**clang++**                   clang-offload-wrapper  ld64.lld            llvm-cvtres      llvm-lib                llvm-profdata    modularize
clang-12                  clang-query            ld.lld              llvm-cxxdump     llvm-libtool-darwin     llvm-ranlib      mygpu
clang-apply-replacements  clang-refactor         llc                 llvm-cxxfilt     llvm-link               llvm-rc          mymcpu
clang-build-select-link   clang-rename           lld                 llvm-cxxmap      llvm-lipo               llvm-readelf     opt
clang-change-namespace    clang-reorder-fields   lld-link            llvm-diff        llvm-lto                llvm-readobj     pp-trace
clang-check               clang-scan-deps        lli                 llvm-dis         llvm-lto2               llvm-reduce      sancov
clang-cl                  clang-tidy             llvm-addr2line      llvm-dlltool     llvm-mc                 llvm-rtdyld      sanstats
clang-cpp                 diagtool               llvm-ar             llvm-dwarfdump   llvm-mca                llvm-size        scan-build
clangd                    dsymutil               llvm-as             llvm-dwp         llvm-ml                 llvm-split       scan-view
clang-doc                 find-all-symbols       llvm-bcanalyzer     llvm-elfabi      llvm-modextract         llvm-stress      split-file
clang-extdef-mapping      flang                  llvm-bitcode-strip  llvm-exegesis    llvm-mt                 llvm-strings     verify-uselistorder
clang-format              flang1                 llvm-cat            llvm-extract     llvm-nm                 llvm-strip       wasm-ld


---
