# Polaris + Rocm 2.6 + TF 

> **Issue #837**
> **状态**: closed
> **创建时间**: 2019-07-09T18:49:55Z
> **更新时间**: 2019-07-10T01:09:57Z
> **关闭时间**: 2019-07-10T01:09:57Z
> **作者**: sos-michael
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/837

## 描述

I don't know if this is a regression or an improvement, but it is a change as a result of rocm 2.6 with no changes to TF so I am reporting it here.

Formerly running: 
TF_ROCM_FUSION_ENABLE=1 python3 tf_cnn_benchmarks.py --num_gpus=10 --batch_size=64 --model=resnet50 --local_parameter_device=cpu --variable_update=parameter_server

would result in an error like:
Memory access fault by GPU node-1 (Agent handle: 0x2b68910) on address 0xadca1b000. Reason: Page not present or supervisor privilege.

now it results in:
Fatal Python error: Segmentation fault
Thread 0x00007f8b825a4680 (most recent call first):
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1407 in _call_tf_sessionrun
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1319 in _run_fn
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1334 in _do_call
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1328 in _do_run
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1152 in _run
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 929 in run
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/training/session_manager.py", line 492 in _try_run_local_init_op
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/training/session_manager.py", line 291 in prepare_session
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/training/supervisor.py", line 730 in prepare_or_wait_for_session
  File "/home/sos/.local/lib/python3.7/site-packages/tensorflow/python/training/supervisor.py", line 993 in managed_session
  File "/usr/lib64/python3.7/contextlib.py", line 112 in __enter__
  File "/home/sos/Downloads/benchmarks-cnn_tf_v1.13_compatible/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 2256 in _benchmark_graph
  File "/home/sos/Downloads/benchmarks-cnn_tf_v1.13_compatible/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 2056 in _benchmark_train
  File "/home/sos/Downloads/benchmarks-cnn_tf_v1.13_compatible/scripts/tf_cnn_benchmarks/benchmark_cnn.py", line 1851 in run
  File "tf_cnn_benchmarks.py", line 68 in main
  File "/home/sos/.local/lib/python3.7/site-packages/absl/app.py", line 251 in _run_main
  File "/home/sos/.local/lib/python3.7/site-packages/absl/app.py", line 300 in run
  File "tf_cnn_benchmarks.py", line 72 in <module>
Segmentation fault (core dumped)

---

## 评论 (2 条)

### 评论 #1 — sunway513 (2019-07-10T00:38:57Z)

Hi @sos-michael , would you refresh your TF whl packages? We have pushed out compatible packages to ROCm2.6 release on PyPI:
https://pypi.org/project/tensorflow-rocm/#history
For TF1.13, please use 1.13.4 whl package, that would be compatible to ROCm2.6 user bit environment:
https://pypi.org/project/tensorflow-rocm/1.13.4/

---

### 评论 #2 — sos-michael (2019-07-10T00:57:51Z)

@sunway513 Thanks for the quick reply! That returned the system to the original error message of:

Memory access fault by GPU node-1 (Agent handle: 0x2b68910) on address 0xadca1b000. Reason: Page not present or supervisor privilege.

I know y'all are working on it, but any word on this? Or maybe some type of workaround in the mean time? It really is a showstopping bug for some of us.

---
