# Request for a test on W6800 and VII PRO

> **Issue #1722**
> **状态**: closed
> **创建时间**: 2022-04-09T19:37:26Z
> **更新时间**: 2022-05-09T20:06:04Z
> **关闭时间**: 2022-05-09T20:06:04Z
> **作者**: aoolmay
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1722

## 描述

Hello,
I'm suffering poor parallel task performance with 6800XTs and 6900XT. It's becoming such a problem that i started considering purchasing W6800 or VII PRO for certain workloads, IF they handle multiple tasks better.

My request is as follows: run on W6800 and VII PRO any small keras/tensorflow task concurrently in multiples of 2x, 3x, 4x and 5x. MNIST keras example will work fine for this test : https://keras.io/examples/vision/mnist_convnet/ or use anything you have at hand that won't take too much of your time.
I need report on epoch time and step time for each task in those configurations, preferably with ROCm 5.x.

You will need to add some memory management code just after loading tensorflow module:
```
from tensorflow.compat.v1.keras.backend import set_session
config = tensorflow.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.95 / XXX # XXX being equal to number of concurrent tasks in test
set_session(tensorflow.compat.v1.Session(config=config))

```
