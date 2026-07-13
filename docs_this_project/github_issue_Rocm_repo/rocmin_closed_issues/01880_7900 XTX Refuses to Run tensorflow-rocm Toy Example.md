# 7900 XTX Refuses to Run tensorflow-rocm Toy Example

- **Issue #:** 1880
- **State:** closed
- **Created:** 2022-12-24T10:58:17Z
- **Updated:** 2024-08-22T15:35:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/1880

### Issue Type

Bug

### Tensorflow Version

Tensorflow-rocm v2.11.0-3797-gfe65ef3bbcf 2.11.0

### rocm Version

5.4.1

### Custom Code

Yes

### OS Platform and Distribution

Archlinux: Kernel 6.1.1

### Python version

3.10

### GPU model and memory

7900 XTX 24GB

### Current Behaviour?

I am not entirely sure whether this is an upstream (ROCM) issue, or with Tensorflow-rocm specifically, so I am reporting it to both repo's. A toy example refuses to run and dumps core. I would have expected it to train successfully.


### Standalone code to reproduce the issue

```
import tensorflow as tf
import numpy as np

features = np.random.randn(10000,25)
targets = np.random.randn(10000)

model = tf.keras.Sequential([
     tf.keras.layers.Dense(1)
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.MeanSquaredError())

model.fit(x=features, y=targets)
```


### Relevant log output

```
[jaap@Jaap-Desktop code]$ pipenv run python testNN.py
2022-12-24 11:18:37.178811: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
python: /build/hsa-rocr/src/ROCR-Runtime-rocm-5.4.1/src/core/runtime/amd_gpu_agent.cpp:339: void rocr::AMD::GpuAgent::AssembleShader(const char*, AssembleTarget, void*&, size_t&) const: Assertion `code_buf != NULL && "Code buffer allocation failed"' failed.
```
