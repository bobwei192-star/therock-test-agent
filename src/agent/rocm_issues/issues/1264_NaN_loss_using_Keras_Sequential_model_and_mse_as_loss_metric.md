# NaN loss using Keras Sequential model and mse as loss metric

> **Issue #1264**
> **状态**: closed
> **创建时间**: 2020-10-23T01:36:27Z
> **更新时间**: 2021-01-26T10:47:02Z
> **关闭时间**: 2020-11-03T00:36:37Z
> **作者**: suvrodeep
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1264

## 描述

**System information**
**- Have I written custom code (as opposed to using a stock example script provided in TensorFlow)**: Yes
**- OS Platform and Distribution (e.g., Linux Ubuntu 16.04)**: Ubuntu 18.04
**- Mobile device (e.g. iPhone 8, Pixel 2, Samsung Galaxy) if the issue happens on mobile device**: No
**- TensorFlow installed from (source or binary)**: ROCM repository
**- TensorFlow version (used command below)**: 2.3.0

`python -c "import tensorflow as tf; print(tf.version.GIT_VERSION, tf.version.VERSION)"`

**- Python version**: 3.6.9
**- Bazel version (if compiling from source)**:
**- GCC/Compiler version (if compiling from source)**:
**- CUDA/cuDNN version**: ROCM 3.8 (3.8-30)
**- GPU model and memory**: RX 580 8GB

**Describe the current behavior**
I am experiencing an issue with a Keras Sequential model for a regression problem. All losses are NaN. It seems like a float32 overflow in memory. Occasionally the script also hangs while training, on a random epoch. I have tested the tf_cnn_benchmarks script with resnet50 which works fine but this simple code does not

**Describe the expected behavior**
Expected behavior can be found by running the Google Colab notebook. Only way I could get it to produce any values is if I have only 1 neuron per layer. Any new suggestions are most welcome

**Standalone code to reproduce the issue**
`import tensorflow as tf`
`from keras.models import Sequential`
`from keras.layers import Dense`
`from keras import backend`
`from keras import Input`
`import numpy as np`
`import pandas as pd`
`from sklearn.model_selection import train_test_split`
`from sklearn.preprocessing import MinMaxScaler`
`from sklearn import datasets`

`# function to synthetically generate data`
`def generate_data():`
`    X, y, coef = datasets.make_regression(n_samples=10000, n_features=30, n_informative=10, coef=True)`
`    y = np.reshape(y, newshape=[10000, 1])`
`    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)`

`    # normalizing input features`
`    scaler = MinMaxScaler()`
`    scaler.fit(X_train)`
`    X_train = scaler.transform(X_train)`
`    X_test = scaler.transform(X_test)`

`    return X_train, y_train, X_test, y_test, coef`

`# get data`
`X_train, y_train, X_test, y_test, coef = generate_data()`
`print("Coefficients: {}".format(coef))`

`# build model`
`backend.clear_session()`
`model = Sequential()`

`model.add(Input(shape=(30,)))`
`model.add(layer=Dense(4, activation='relu'))`
`model.add(layer=Dense(4, activation='relu'))`
`model.add(layer=Dense(4, activation='relu'))`
`model.add(layer=Dense(1))`

`model.compile(optimizer='rmsprop', loss='mse')`

`# training the model. This is the line that causes the issue`
`model.fit(x=X_train, y=y_train, epochs=200, batch_size=100, steps_per_epoch=70,  verbose=1)`

Provide a reproducible test case that is the bare minimum necessary to generate
the problem. If possible, please share a link to Colab/Jupyter/any notebook.
[https://colab.research.google.com/drive/1XjhtC7x1Sn2K313Os1_5kfyXogoKlDa6?usp=sharing](url)

**Other info / logs** Include any logs or source code that would be helpful to
diagnose the problem. If including tracebacks, please include the full
traceback. Large logs and files should be attached.


---

## 评论 (5 条)

### 评论 #1 — suvrodeep (2020-10-23T01:38:06Z)

Raised the issue in the tensorflow-upstream repo for ROCM but unfortunately did not receive a response. Had the the same exact issue with ROCM Tensorflow Docker image which leads me to think there is no issue with my ROCM installation
![Screenshot from 2020-10-23 03-32-07](https://user-images.githubusercontent.com/27533081/96946336-5e2a6a80-14e0-11eb-8a3b-2aa52751da2a.png)



---

### 评论 #2 — xuhuisheng (2020-10-23T02:16:56Z)

Duplicate of:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/1105
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/1144

Maybe related:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/1106
https://github.com/RadeonOpenCompute/ROCm/issues/1203

---

### 评论 #3 — rkothako (2020-11-02T06:49:47Z)

Hi @suvrodeep,
Can you please close this ticket as the issue likely to be an TF issue as per @xuhuisheng (as per above comment).
Please share an update on this.
Thank you.

---

### 评论 #4 — suvrodeep (2020-11-03T00:36:22Z)

Closing this issue as it has been resolved elsewhere.

Summary: There is a memory/FP32 issue with ROCM 3.7 and above for gfx803 cards (Polaris 10) which are RX 480/580 etc. Please downgrade to ROCM 3.5.1 for correct operation. tensorflow-rocm==2.3.1 tested and working with Ubuntu 20.04 and python 3.8

Please follow link for detailed information regarding the solution:
[https://github.com/RadeonOpenCompute/ROCm/issues/1203#issuecomment-716214449](url)

---

### 评论 #5 — boriswinner (2021-01-26T10:47:02Z)

Here is my guide to downgrade to ROCm 3.5.1 + TensorFlow 2.2:
https://github.com/boriswinner/RX580-rocM-tensorflow-ubuntu20.4-guide

---
