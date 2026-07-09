# Crash in TensorFlow: "Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)" in classification tutorial

- **Issue #:** 1203
- **State:** closed
- **Created:** 2020-08-25T13:26:50Z
- **Updated:** 2021-01-26T10:46:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1203

I'm working through the basic tutorials on the TensorFlow website. In the second tutorial, I get a weird crash. This is the tutorial: https://www.tensorflow.org/tutorials/keras/text_classification 
I'm trying to run the solution provided here: https://github.com/tensorflow/examples/blob/master/community/en/text_classification_solution.ipynb

I get output like this:
```
tf.__version__: 2.3.0
Found 8000 files belonging to 4 classes.
Using 6400 files for training.
2020-08-25 15:09:14.920446: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
2020-08-25 15:09:14.930506: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:08:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.366GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-08-25 15:09:14.932126: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-25 15:09:14.932805: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-25 15:09:14.936516: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-08-25 15:09:14.936658: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-08-25 15:09:14.936727: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-08-25 15:09:14.936940: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-08-25 15:09:14.941538: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 3593240000 Hz
2020-08-25 15:09:14.942285: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f412c8674e0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-08-25 15:09:14.942302: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-08-25 15:09:14.943684: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f412c713100 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-08-25 15:09:14.943694: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], AMDGPU ISA version: gfx803
2020-08-25 15:09:15.181846: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:08:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.366GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-08-25 15:09:15.181918: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-25 15:09:15.181936: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-25 15:09:15.181951: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-08-25 15:09:15.181966: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-08-25 15:09:15.182062: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-08-25 15:09:15.182086: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-08-25 15:09:15.182095: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      0 
2020-08-25 15:09:15.182103: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 0:   N 
2020-08-25 15:09:15.182238: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7700 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], pci bus id: 0000:08:00.0)
Found 8000 files belonging to 4 classes.
Using 1600 files for validation.
Found 8000 files belonging to 4 classes.
2020-08-25 15:09:15.624322: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:15.625583: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:15.630665: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:15.632282: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
 ========== calling model.fit()
2020-08-25 15:09:16.676462: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:16.695113: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
Epoch 1/5
2020-08-25 15:09:16.899558: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:16.905277: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-25 15:09:16.905468: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
191/200 [===========================>..] - ETA: 0s - accuracy: 0.3212 - loss: 1.37282020-08-25 15:09:24.206187: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
199/200 [============================>.] - ETA: 0s - accuracy: 0.3232 - loss: 1.37212020-08-25 15:09:24.285358: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:24.303358: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:24.352910: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:24.356064: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
Traceback (most recent call last):
  File "solution.py", line 87, in <module>
    history = model.fit(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 108, in _method_wrapper
    return method(self, *args, **kwargs)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 1123, in fit
    val_logs = self.evaluate(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 108, in _method_wrapper
    return method(self, *args, **kwargs)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 1379, in evaluate
    tmp_logs = test_function(iterator)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/def_function.py", line 780, in __call__
    result = self._call(*args, **kwds)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/def_function.py", line 814, in _call
    results = self._stateful_fn(*args, **kwds)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 2829, in __call__
    return graph_function._filtered_call(args, kwargs)  # pylint: disable=protected-access
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 1843, in _filtered_call
    return self._call_flat(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 1923, in _call_flat
    return self._build_call_outputs(self._inference_function.call(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 545, in call
    outputs = execute.execute(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/execute.py", line 59, in quick_execute
    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,
tensorflow.python.framework.errors_impl.InvalidArgumentError: 2 root error(s) found.
  (0) Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)
	 [[node sequential/embedding/embedding_lookup (defined at solution.py:87) ]]
	 [[sequential/embedding/embedding_lookup/_10]]
  (1) Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)
	 [[node sequential/embedding/embedding_lookup (defined at solution.py:87) ]]
0 successful operations.
0 derived errors ignored. [Op:__inference_test_function_2262]

Errors may have originated from an input operation.
Input Source operations connected to node sequential/embedding/embedding_lookup:
 sequential/embedding/embedding_lookup/2185 (defined at /usr/lib/python3.8/contextlib.py:113)

Input Source operations connected to node sequential/embedding/embedding_lookup:
 sequential/embedding/embedding_lookup/2185 (defined at /usr/lib/python3.8/contextlib.py:113)

Function call stack:
test_function -> test_function

2020-08-25 15:09:24.456958: W tensorflow/core/kernels/data/cache_dataset_ops.cc:798] The calling iterator did not fully read the dataset being cached. In order to avoid unexpected truncation of the dataset, the partially cached contents of the dataset will be discarded. This can happen if you have an input pipeline similar to `dataset.cache().take(k).repeat()`. You should use `dataset.take(k).cache().repeat()` instead.
```

The numbers in ```(0) Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)``` vary, that is, the index and the invalid value change from one run to the next. The time it takes until it bails out also varies; sometimes it bombs in the first Epoch, sometimes the second, etc. Once the whole ```model.fit()``` call ran through, and after that, I seemed to be able to use the model just fine. But in ~95% of cases, it crashes.

I tried to run it in Docker as well as on a ROCm installation on Debian bullseye, with the same result. Upgrading from linux 5.8 to 5.9-rc2 didn't change anything, either. I'm using upstream kernel drivers as I had problems installing the DKMS module. When I set ```HIP_VISIBLE_DEVICES=-1```, forcing the example to run on the CPU, it works just fine. Could this be a bug in ROCm? Something wrong with my installation?