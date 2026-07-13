# *** stack smashing detected ***: <unknown> terminated

- **Issue #:** 960
- **State:** closed
- **Created:** 2019-12-09T17:44:28Z
- **Updated:** 2019-12-21T16:20:48Z
- **URL:** https://github.com/ROCm/ROCm/issues/960

**ubuntu** 18.04.3  **kernel** 5.0.37
rocm 2.10.14 can't work.

code:
```
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```

error:
```
2019-12-10 01:34:21.442336: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
*** stack smashing detected ***: <unknown> terminated
```

