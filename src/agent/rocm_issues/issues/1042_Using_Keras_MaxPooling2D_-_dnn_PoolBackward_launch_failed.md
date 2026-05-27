# Using Keras MaxPooling2D - dnn PoolBackward launch failed

> **Issue #1042**
> **状态**: closed
> **创建时间**: 2020-03-14T17:29:34Z
> **更新时间**: 2021-04-19T12:31:03Z
> **关闭时间**: 2021-04-19T12:31:03Z
> **作者**: AndrewCarterUK
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1042

## 描述

## Introduction

I'm working through a command recognition problem, essentially porting the [TensorFlow audio recognition model](https://github.com/tensorflow/docs/blob/master/site/en/r1/tutorials/sequences/audio_recognition.md) to Keras.

My model code is essentially:

```py
model = Sequential()
model.add(Conv2D(64, (20, 8), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(1, 3)))
model.add(Dropout(dropout))
model.add(Conv2D(64, (10, 4), activation='relu'))
model.add(Dropout(dropout))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dropout(dropout))
model.add(Dense(128, activation='relu'))
model.add(Dropout(dropout))
model.add(Dense(num_classes, activation='softmax'))

sgd = SGD(learning_rate=0.001)

model.compile(loss='categorical_crossentropy', optimizer=sgd)
```

## Error

```
Using TensorFlow backend.
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm_dmix.c:1052:(snd_pcm_dmix_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_dmix.c:1052:(snd_pcm_dmix_open) unable to open slave
2020-03-14 17:18:03.359403: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-03-14 17:18:03.401901: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.268GHz coreCount: 32 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-03-14 17:18:03.435593: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 17:18:03.437477: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-14 17:18:03.439284: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-14 17:18:03.439544: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-14 17:18:03.439640: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-14 17:18:03.439848: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
2020-03-14 17:18:03.443663: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3600090000 Hz
2020-03-14 17:18:03.443942: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x6d99900 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-03-14 17:18:03.443955: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-03-14 17:18:03.444766: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.268GHz coreCount: 32 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-03-14 17:18:03.444791: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 17:18:03.444800: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-14 17:18:03.444808: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-14 17:18:03.444815: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-14 17:18:03.444883: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-14 17:18:03.444919: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-14 17:18:03.444922: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0 
2020-03-14 17:18:03.444925: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N 
2020-03-14 17:18:03.445034: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7539 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X], pci bus id: 0000:26:00.0)
Epoch 1/3
2020-03-14 17:18:09.125710: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 17:18:09.127815: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
MIOpen Error: basic_string::_M_construct null not valid
2020-03-14 17:18:18.021227: E tensorflow/stream_executor/rocm/rocm_dnn.cc:3643] failed to enqueue forward pooling (before backward) on stream: miopenStatusUnknownError
2020-03-14 17:18:18.021263: W tensorflow/core/common_runtime/base_collective_executor.cc:217] BaseCollectiveExecutor::StartAbort Internal: dnn PoolBackward launch failed
	 [[{{node gradients/max_pooling2d_1/MaxPool_grad/MaxPoolGrad}}]]
ERROR:root: dnn PoolBackward launch failed
	 [[node gradients/max_pooling2d_1/MaxPool_grad/MaxPoolGrad (defined at /home/andrew/.local/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:3009) ]] [Op:__inference_keras_scratch_graph_1036]

Function call stack:
keras_scratch_graph
Traceback (most recent call last):
  File "main.py", line 25, in main
    train(args.configuration_file_path, args.checkpoint_file_path)
  File "/home/andrew/Development/Machine Learning/Box Box/boxbox/train.py", line 39, in train
    model.fit_generator(dataset.train_generator(), epochs=3, steps_per_epoch=100, use_multiprocessing=True)
  File "/home/andrew/.local/lib/python3.6/site-packages/keras/legacy/interfaces.py", line 91, in wrapper
    return func(*args, **kwargs)
  File "/home/andrew/.local/lib/python3.6/site-packages/keras/engine/training.py", line 1732, in fit_generator
    initial_epoch=initial_epoch)
  File "/home/andrew/.local/lib/python3.6/site-packages/keras/engine/training_generator.py", line 220, in fit_generator
    reset_metrics=False)
  File "/home/andrew/.local/lib/python3.6/site-packages/keras/engine/training.py", line 1514, in train_on_batch
    outputs = self.train_function(ins)
  File "/home/andrew/.local/lib/python3.6/site-packages/tensorflow_core/python/keras/backend.py", line 3727, in __call__
    outputs = self._graph_fn(*converted_inputs)
  File "/home/andrew/.local/lib/python3.6/site-packages/tensorflow_core/python/eager/function.py", line 1551, in __call__
    return self._call_impl(args, kwargs)
  File "/home/andrew/.local/lib/python3.6/site-packages/tensorflow_core/python/eager/function.py", line 1591, in _call_impl
    return self._call_flat(args, self.captured_inputs, cancellation_manager)
  File "/home/andrew/.local/lib/python3.6/site-packages/tensorflow_core/python/eager/function.py", line 1692, in _call_flat
    ctx, args, cancellation_manager=cancellation_manager))
  File "/home/andrew/.local/lib/python3.6/site-packages/tensorflow_core/python/eager/function.py", line 545, in call
    ctx=ctx)
  File "/home/andrew/.local/lib/python3.6/site-packages/tensorflow_core/python/eager/execute.py", line 67, in quick_execute
    six.raise_from(core._status_to_exception(e.code, message), None)
  File "<string>", line 3, in raise_from
tensorflow.python.framework.errors_impl.InternalError:  dnn PoolBackward launch failed
	 [[node gradients/max_pooling2d_1/MaxPool_grad/MaxPoolGrad (defined at /home/andrew/.local/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:3009) ]] [Op:__inference_keras_scratch_graph_1036]

Function call stack:
keras_scratch_graph
```

If I remove the MaxPooling2D layer, the model trains without error.

```
Using TensorFlow backend.
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm_dmix.c:1052:(snd_pcm_dmix_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_dmix.c:1052:(snd_pcm_dmix_open) unable to open slave
2020-03-14 16:51:51.360499: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-03-14 16:51:51.402676: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.268GHz coreCount: 32 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-03-14 16:51:51.436191: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 16:51:51.438040: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-14 16:51:51.439830: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-14 16:51:51.440079: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-14 16:51:51.440173: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-14 16:51:51.440386: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
2020-03-14 16:51:51.444085: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3600090000 Hz
2020-03-14 16:51:51.444472: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7027770 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-03-14 16:51:51.444494: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-03-14 16:51:51.446061: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.268GHz coreCount: 32 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-03-14 16:51:51.446098: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 16:51:51.446114: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-14 16:51:51.446128: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-14 16:51:51.446141: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-14 16:51:51.446252: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-14 16:51:51.446308: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-14 16:51:51.446317: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0 
2020-03-14 16:51:51.446322: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N 
2020-03-14 16:51:51.446564: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7539 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X], pci bus id: 0000:26:00.0)
Epoch 1/3
2020-03-14 16:51:56.904334: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 16:51:56.906092: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so

  1/100 [..............................] - ETA: 24:48 - loss: 1.5107
  2/100 [..............................] - ETA: 12:19 - loss: 1.5067
  3/100 [..............................] - ETA: 8:47 - loss: 1.5025 
  4/100 [>.............................] - ETA: 6:32 - loss: 1.4817
  5/100 [>.............................] - ETA: 5:12 - loss: 1.4710
  6/100 [>.............................] - ETA: 4:35 - loss: 1.4558
  7/100 [=>............................] - ETA: 3:54 - loss: 1.4454
  8/100 [=>............................] - ETA: 3:36 - loss: 1.4386
  9/100 [=>............................] - ETA: 3:11 - loss: 1.4352
 10/100 [==>...........................] - ETA: 2:59 - loss: 1.4278
```

I'm a bit new to using all these tools so there's a good chance I've done something wrong. I took care to follow all of the instructions installing the system, the only problem I encountered was that one of the packages the documentation told me to install was unavailable, so I've had to use the system without it.

```
andrew@andrew-desktop:~$ sudo apt install rocm-libs miopen-hip cxlactivitylogger
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package cxlactivitylogger
```

The tensorflow audio recognition suite trains without error on the same system.

The line from their model is:

```py
  max_pool = tf.nn.max_pool2d(input=first_dropout,
                              ksize=[1, 2, 2, 1],
                              strides=[1, 2, 2, 1],
                              padding='SAME')
```

Any help much appreciated and thank you for the work on this software.

## System Information
- Keras using TensorFlow backend
- TensorFlow installed version 2.1
- Radeon RX570

```
ROCk module is loaded
andrew is member of video group
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 3600 6-Core Processor  
  Marketing Name:          AMD Ryzen 5 3600 6-Core Processor  
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            12                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16407856(0xfa5d30) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16407856(0xfa5d30) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx803                             
  Marketing Name:          Ellesmere [Radeon RX 470/480/570/570X/580/580X]
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26591(0x67df)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1268                               
  BDFID:                   9728                               
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8388608(0x800000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx803          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
```

```sh
Package: rocm-libs
Version: 3.1.35
Priority: optional
Section: devel
Maintainer: Advanced Micro Devices Inc.
Installed-Size: 13.3 kB
Depends: rocfft, rocrand, rocblas, hipblas, rocsparse, hipsparse, rocalution, rocprim, rocthrust, hipcub
Homepage: https://github.com/RadeonOpenCompute/ROCm
Download-Size: 808 B
APT-Manual-Installed: yes
APT-Sources: http://repo.radeon.com/rocm/apt/debian xenial/main amd64 Packages
Description: Radeon Open Compute (ROCm) Runtime software stack
```

---

## 评论 (4 条)

### 评论 #1 — AndrewCarterUK (2020-03-14T17:58:34Z)

A bit more information from further investigation, one of the things I've been playing with is the batch size - and I've noticed that changing it changes the error.

With a batch size of 10, the error is what I've described above. With a batch size of 100, the error changes to:

```
Using TensorFlow backend.
ALSA lib pcm_dsnoop.c:618:(snd_pcm_dsnoop_open) unable to open slave
ALSA lib pcm_dmix.c:1052:(snd_pcm_dmix_open) unable to open slave
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_dmix.c:1052:(snd_pcm_dmix_open) unable to open slave
2020-03-14 17:50:03.121932: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-03-14 17:50:03.142394: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.268GHz coreCount: 32 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-03-14 17:50:03.208671: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 17:50:03.212648: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-14 17:50:03.216856: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-14 17:50:03.218281: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-14 17:50:03.218412: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-14 17:50:03.218677: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
2020-03-14 17:50:03.224009: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3600090000 Hz
2020-03-14 17:50:03.224338: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x713e530 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-03-14 17:50:03.224362: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-03-14 17:50:03.225262: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties: 
pciBusID: 0000:26:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X]     ROCm AMD GPU ISA: gfx803
coreClock: 1.268GHz coreCount: 32 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: -1B/s
2020-03-14 17:50:03.225303: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 17:50:03.225312: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-14 17:50:03.225319: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-14 17:50:03.225326: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-14 17:50:03.225384: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-14 17:50:03.225419: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-14 17:50:03.225422: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0 
2020-03-14 17:50:03.225425: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N 
2020-03-14 17:50:03.225540: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7539 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X], pci bus id: 0000:26:00.0)
Epoch 1/3
2020-03-14 17:50:10.551604: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-14 17:50:10.557943: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
MIOpen Error: basic_string::_M_construct null not valid
2020-03-14 17:50:20.569479: F tensorflow/stream_executor/rocm/rocm_dnn.cc:2718] Check failed: status == miopenStatusSuccess (7 vs. 0)Unable to find a suitable algorithm for doing backward filter convolution
Aborted (core dumped)
```

Also, the full model runs fine on the CPU with the GPU disabled. 

When I remove the pooling layer, the CPU runs that model much quicker than the GPU does. The GPU takes a couple of minutes to do 100 steps and the CPU does them in about 15s.

---

### 评论 #2 — TheBigJones (2020-04-04T08:58:03Z)

Hello I have the same issue:
Reading package lists... Done
Building dependency tree       
Reading state information... Done
E: Unable to locate package cxlactivitylogger

When I'm trying to import tensorflow I get the following error:
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
Traceback (most recent call last):
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/usr/lib/python3.6/imp.py", line 243, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.6/imp.py", line 343, in load_dynamic
    return _load(spec)
ImportError: librccl.so.1: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow/__init__.py", line 101, in <module>
    from tensorflow_core import *
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/__init__.py", line 40, in <module>
    from tensorflow.python.tools import module_util as _module_util
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow/__init__.py", line 50, in __getattr__
    module = self._load()
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow/__init__.py", line 44, in _load
    module = _importlib.import_module(self.__name__)
  File "/usr/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow.py", line 74, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow.py", line 58, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/home/jonathan/vrocm330/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
  File "/usr/lib/python3.6/imp.py", line 243, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.6/imp.py", line 343, in load_dynamic
    return _load(spec)
ImportError: librccl.so.1: cannot open shared object file: No such file or directory


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/errors

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.

Any ideas?


---

### 评论 #3 — ROCmSupport (2021-04-05T11:53:45Z)

Thanks @AndrewCarterUK for reaching out.
Can you please try with the latest ROCm 4.1 and share me an update.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-04-19T12:31:03Z)

No update for a long time and hope issue is no more observed with 4.1.
Feel free to open a new issue for quick response.
Thank you.

---
