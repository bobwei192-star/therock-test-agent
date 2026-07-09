# hipErrorNoBinaryForGpu: Unable to find code object for all current devices!

- **Issue #:** 1623
- **State:** closed
- **Created:** 2021-11-22T19:57:24Z
- **Updated:** 2024-03-11T13:41:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/1623

Hi, I have installed tensorflow on ROCm in my Ubuntu 20.04 distro.
I have followed all the step provided in the official ROCm [page](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html).

I also have installed tensorflow-rocm following the guide [here](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html).

I am now trying to execute a very simple python script to test my tensorflow library:
`import tensorflow as tf`
`tf.add(1, 2).numpy()`

but instead of the result I get this error:

> "hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
> Canceled` (core dump created)

My configuration is:
_AMD Ryzen 5 3600
AMD Radeon RX 5600 XT_

Can you help me finding a solution? thanks
