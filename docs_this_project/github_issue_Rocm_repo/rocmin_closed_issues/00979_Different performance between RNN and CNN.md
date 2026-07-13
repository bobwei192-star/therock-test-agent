# Different performance between RNN and CNN

- **Issue #:** 979
- **State:** closed
- **Created:** 2019-12-23T02:17:09Z
- **Updated:** 2020-01-09T16:16:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/979

When I run the classical  model Seq2seq in my machine with this [program,](https://github.com/keon/seq2seq) I found that the program consits of RNN structures with the same parameters is far slower than NVIDIA platform even the Float32 performance of the Radeon 7 is greater than 1080ti. But the perfromance is proved in CNN operations that the Radeon 7 is faster than 1080ti in official pytorch examples [mnist.](https://github.com/pytorch/examples/tree/master/mnist) Here is the comparation table:

||Radeon 7|1080ti|
|---|---|---|
|Epoch|6|6|
|Concurrency platform|ROCm 2.9|CUDA 10.0|
|Deep learning software|MIOpen 2.1|cuDNN 7.5|
|Pytorch|1.3.1|1.3.1|
|Seq2seq time|19min|10min|
|Mnist time|2min39s|3min59s|

I also try myself experiments that consist more complex RNN structure and large datasets. The program costs **2** hours per epoch in 1080ti and **9** hours per epoch in Radeon 7 with the same parameters. Of course, I am happy to see that others can give more test in more complex RNN and CNN models.
In nvidia cuDNN official [website](https://developer.nvidia.com/cudnn), we can see the performance in sequence model achieve a large increment between the different version of cuDNN. Should our MIOpen library need more optimization in RNN operation?
More discussion can be found in this issue. [link](https://github.com/ROCmSoftwarePlatform/pytorch/issues/546)