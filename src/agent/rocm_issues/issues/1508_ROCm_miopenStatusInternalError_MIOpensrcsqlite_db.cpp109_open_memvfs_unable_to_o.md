# ROCm miopenStatusInternalError /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file

> **Issue #1508**
> **状态**: closed
> **创建时间**: 2021-06-29T03:50:41Z
> **更新时间**: 2021-07-19T05:02:02Z
> **关闭时间**: 2021-07-19T05:02:02Z
> **作者**: Felix-Petersen
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1508

## 描述

## 🐛 Bug

On ROCm 4.2, with PyTorch 1.9.0 installed via 

```shell
pip3 install torch -f https://download.pytorch.org/whl/rocm4.2/torch_stable.html
```

Running https://github.com/pytorch/examples/tree/master/mnist crashes oftentimes with the error below. 
I use an MI50 GPU.
The error sometimes occurs at the very beginning of training, sometimes after the first epoch, sometimes within an epoch and sometimes not at all.

My impression is, that it might have to do with latency or data access.
The Python environment installation is on a data server connected via Infiniband.
The error is thrown from "/infiniband-shared-storage/.env1/lib64/python3.6/site-packages/torch/lib/libMIOpen-12425ccb.so.1".

On this device, I usually have to start my code 1-2 times before it actually works without crashing, but then there seems to be no problem. I have also installed it on a slow shared storage and there the problem is much more severe.

My interpretation of this is that there could be some connection instability for the specific command or that it requires getting the data within a short time frame.

We also have local installations of ROCm / MIOpen on each server ("/opt/rocm/lib/libMIOpen.so.1").
Is it possible to use the local shared object file instead of the one delivered with PyTorch? If yes, how can I do that?
(I tried it, but deleting and creating a symlink does not work)


```
MIOpen(HIP): Warning [FindWinogradSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindDataDirectSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindDataImplicitGemmSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindFftSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindWinogradSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindDataDirectSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindDataImplicitGemmSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindFftSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindWinogradSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindDataDirectSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindDataImplicitGemmSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen(HIP): Warning [FindFftSolutions] /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
MIOpen Error: /MIOpen/src/sqlite_db.cpp:109: open memvfs: unable to open database file
Traceback (most recent call last):
  File "main.py", line 137, in <module>
    main()
  File "main.py", line 128, in main
    train(args, model, device, train_loader, optimizer, epoch)
  File "main.py", line 44, in train
    loss.backward()
  File "/home/ssml/petersenf/testing/.env1/lib64/python3.6/site-packages/torch/_tensor.py", line 255, in backward
    torch.autograd.backward(self, gradient, retain_graph, create_graph, inputs=inputs)
  File "/home/ssml/petersenf/testing/.env1/lib64/python3.6/site-packages/torch/autograd/__init__.py", line 149, in backward
    allow_unreachable=True, accumulate_grad=True)  # allow_unreachable flag
RuntimeError: miopenStatusInternalError
```

## To Reproduce

Steps to reproduce the behavior:

On a setup as described above:

1. `wget https://raw.githubusercontent.com/pytorch/examples/master/mnist/main.py`
1. python main.py

## Environment

```
Collecting environment information...
PyTorch version: 1.9.0+rocm4.2
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 4.2.21155-37cb3a34

OS: Scientific Linux release 7.9 (Nitrogen) (x86_64)
GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.3.4

Python version: 3.6 (64-bit runtime)
Python platform: Linux-3.10.0-1160.25.1.el7.x86_64-x86_64-with-redhat-7.9-Nitrogen
Is CUDA available: True
CUDA runtime version: Could not collect
GPU models and configuration: Vega 20
Nvidia driver version: Could not collect
cuDNN version: Could not collect
HIP runtime version: 3.27.5
MIOpen runtime version: 2.11.0

Versions of relevant libraries:
[pip3] numpy==1.19.5
[pip3] torch==1.9.0+rocm4.2
[pip3] torchvision==0.10.0
[conda] Could not collect
```

```
$ yum info rocm-libs

Failed to set locale, defaulting to C
Available Packages
Name        : rocm-libs
Arch        : x86_64
Version     : 4.2.0.40200
Release     : 21.el7
Size        : 4.0 k
Repo        : local-SL7-x86_64--install-repos-rocm
Summary     : Radeon Open Compute (ROCm) Runtime software stack
License     : unknown
Description : DESCRIPTION
            : ===========
            :
            : This is an installer created using CPack (https://cmake.org). No additional installation instructions provided.
```

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-06-30T08:20:31Z)

Thanks @Felix-Petersen for reaching out.
Can you please share me the exact steps(step by step) to reproduce and better understanding of the problem.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-07-08T09:13:11Z)

Hi @Felix-Petersen 
I am waiting for your update.
Can you please share me the exact steps(step by step) to reproduce and better understanding of the problem.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-07-19T05:02:02Z)

As there is no response from user for around 20 days, closing this ticket.
Request user to log a new ticket, if any, with all required details.
Thank you.

---
