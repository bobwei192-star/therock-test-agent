# NaN loss using Keras Sequential model and mse as loss metric

- **Issue #:** 1264
- **State:** closed
- **Created:** 2020-10-23T01:36:27Z
- **Updated:** 2021-01-26T10:47:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/1264

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
