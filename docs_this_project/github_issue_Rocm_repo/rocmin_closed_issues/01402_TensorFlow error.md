# TensorFlow error

- **Issue #:** 1402
- **State:** closed
- **Created:** 2021-03-07T17:27:51Z
- **Updated:** 2021-04-12T07:12:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1402

Hello,
I have problem with training CNN in tensorflow-rocm-2.4.0. The error occurs randomly, sometimes after several iterations of learning CNN and sometimes it appears immediately. This error (complete error log in file **tensor-flow-rocm-error.txt**): 

_Fit:
2021-03-07 17:54:13.140698: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2)
Epoch 1/200
2021-03-07 17:54:14.742459: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libMIOpen.so
2021-03-07 17:54:14.889237: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library librocblas.so
89/89 [==============================] - 141s 2s/step - loss: nan - accuracy: 0.5137 - val_loss: nan - val_accuracy: 0.6555
Epoch 2/200
30/89 [=========>....................] - ETA: 24s - loss: nan - accuracy: 0.6652Memory access fault by GPU node-1 (Agent handle: 0x5f6d730) on address 0x7fb5d8712000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)_

This is my configuration:
_Linux kulich-PC-GPU 5.4.0-66-generic #74~18.04.2-Ubuntu SMP Fri Feb 5 11:17:31 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux_
_RX Vega 64 8GB_

I try to reduce dataset size but the error still occurs. Where can be the problem?  Too complex model?

Another log file is included (**rocminfo.txt** and **dmesg.txt**)
Thank you for your work

[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6097618/dmesg.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/6097619/rocminfo.txt)
[tensor-flow-rocm-error.txt](https://github.com/RadeonOpenCompute/ROCm/files/6097620/tensor-flow-rocm-error.txt)




