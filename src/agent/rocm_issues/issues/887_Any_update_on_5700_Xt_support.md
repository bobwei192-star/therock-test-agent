# Any update on 5700 Xt support?

> **Issue #887**
> **状态**: closed
> **创建时间**: 2019-09-13T03:10:06Z
> **更新时间**: 2025-09-09T17:32:08Z
> **关闭时间**: 2021-01-29T13:13:21Z
> **作者**: devnarekm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/887

## 描述

Just curious if you have any plans on supporting the 5700 Xt card in the near future. As of now I haven't seen it in the supported GPUs list. Would be nice to also have it included!

---

## 评论 (100 条)

### 评论 #1 — kentrussell (2019-09-25T16:19:26Z)

There are different levels of support in ROCm, since it's an entire stack, which makes this a difficult question to answer. 

1-Kernel support. This usually comes pretty quickly from upstream, and is already there in its infancy. The basic code is there, and there is work going on to thoroughly test the kernel functionality
2-Thunk support. This is usually pretty quick too, since it's mostly just adding the chip information, and then adding any weird quirks that the HW has (shader engine distribution, SDMA queues, etc)
3-Runtime support. This usually takes longer as there is a lot of testing to go on
4-Official ROCm support - Once we have 1-3 supported, we need to run the full gambit of tests and applications against the stack. This requires a lot of time, and a lot of bug-fixes. Once this is done, that's when we add it to the Supported GPUs list. 

So there may be some partial support for it right now, or it might work almost perfectly. It's all a bit of a crapshoot until we update the documentation, as we haven't tested everything to fulfill our exit criteria for supporting a GPU. You can always try it out, and post PRs to help to support them in the interim, though. We always like help from the community!

---

### 评论 #2 — Moading (2019-09-25T16:49:08Z)

Hi, in my experience GPUs listed as "supported" have no guarantee to work properly. I have opend a few issues here and the speed at which theses issues are fixed is extremely disappointing. The most annoying thing is missing OpenCL 2.0 support for hardware that is still beeing sold (gfx803).

I have zero confidence that the latest hardware will have OpenCL 2.0 support in ROCm, therefore I am not buying new hardware. There would be more business for AMD if the drivers delivered better OpenCL support.

---

### 评论 #3 — EwoutH (2019-10-08T12:21:39Z)

@kentrussell Could you create a new issue for us to track Navi integration? You could create a task list to mark the process:

- [ ] 1-Kernel support
- [ ] 2-Thunk support
- [ ] 3-Runtime support
- [ ] 4-Official ROCm support

```
- [ ] 1-Kernel support
- [ ] 2-Thunk support
- [ ] 3-Runtime support
- [ ] 4-Official ROCm support
```

---

### 评论 #4 — onfoot (2019-10-11T09:57:35Z)

I'm new here, and don't know anything about anything, so it's perfectly fine that I chip in. ;) I'm interested in ROCm since I'm currently buying the 5700 XT for myself and wanted, aside from gaming, to play around with PyTorch and Tensorflow.

Seems like kernel support [has been merged in on Sep 23rd](https://www.phoronix.com/scan.php?page=news_item&px=Navi-10-Linux-Firmware-Git), Thunk has support for Navi 10 since July, so we're getting there.

---

### 评论 #5 — EwoutH (2019-12-12T21:11:04Z)

@aak-amd @zhang2amd @Rmalavally @kentrussell Any updates about Navi/RDNA support?

---

### 评论 #6 — mritunjaymusale (2020-01-21T09:16:47Z)

Bump.
Still wondering if the support is there or not?

#998 

---

### 评论 #7 — jemzipx (2020-03-02T14:09:55Z)

It is kind of sad that AMD has forgotten Navi users. I have found a temporary solution to use my RX 5700XT for deep learning with rather astonishing results. I thought I should share it here. Using Linux kernel 5.6rc and AMDGPU PRO driver I was able to set up OpenCL 2.0 on Manjaro Linux. Then I installed PlaidML which supports opencl devices. After that, I set Keras backend to PlaidML and just used Keras. I ran some benchmarks and the results are just amazing. It outperforms my 12C/24T Ryzen 3900 CPU by a massive margin. While it takes more than 12 minutes to train MobileNet on Ryzen 3900X, it takes less than a minute on Radeon 5700XT.  Here are the Inference latency and Time/FPS comparison in mobilenet benchmark:

```
RX 5700 XT GPU:
-----------------------------------------------------------------------------------------
Network Name         Inference Latency         Time / FPS          
-----------------------------------------------------------------------------------------
mobilenet                  22.00 ms                  19.68 ms / 50.80 fps

Ryzen 3900X CPU:
-----------------------------------------------------------------------------------------
Network Name         Inference Latency         Time / FPS          
-----------------------------------------------------------------------------------------
mobilenet                  695.84 ms                 695.56 ms / 1.44 fps
```   
![pladiml-bench](https://user-images.githubusercontent.com/41994943/75683598-08dbe780-5cca-11ea-9b11-8adce90925d0.png)

And for those who prefer to see a working example, here is a CNN trained on MNIST in Keras using RX 5700XT:

![keras-cnn](https://user-images.githubusercontent.com/41994943/77228214-645a1080-6bb8-11ea-8a6c-b299b8d2b7ad.jpg)



---

### 评论 #8 — FiCacador (2020-03-02T15:16:02Z)

ROCm-OpenCL-Runtime 3.1 changes introduced ROC_GFX10, that's Navi!
It still isn't listed as supported on the official documentation, but neither is any non deprecated Linux kernel...
Has anyone already tried 3.1 with Navi?

---

### 评论 #9 — jemzipx (2020-03-03T08:37:22Z)

The Navi support seems to be a work in progress. There are no clear instructions on how to compile ROCm from scratch anyway. I downloaded all their sources codes using Google Repo tool and there are at least 40 different projects to compile separately! I couldn't find any easy way to automate the building process. There is a project that is  supposed to automate the build process but has not been updated in the past few years. If the guys at AMD can illuminate us on how to automate ROCm compilation, it would be greatly appreciated.  

---

### 评论 #10 — lrie (2020-03-10T20:15:24Z)

There is no or no complete Navi support in ROCM 3.1 .
Tested with Radeon 5700XT, ROCM 3.1 and Tensorflow 2.1

`
gpu-user@gpu-server:~/benchmarks/scripts/tf_cnn_benchmarks$ python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=64 --model=resnet50
WARNING:tensorflow:From /home/gpu-user/.local/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:88: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
2020-03-10 19:45:39.130116: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
2020-03-10 19:45:39.155823: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3099670000 Hz
2020-03-10 19:45:39.156223: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x4ed3e10 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-03-10 19:45:39.156330: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-03-10 19:45:39.159225: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-03-10 19:45:39.193370: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties:
pciBusID: 0000:2b:00.0 name: Device 731f     ROCm AMD GPU ISA: gfx1010
coreClock: 0.1GHz coreCount: 40 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-03-10 19:45:39.235125: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-10 19:45:39.236629: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-10 19:45:39.237930: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-10 19:45:39.238294: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-10 19:45:39.238463: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-10 19:45:39.238596: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-10 19:45:39.238658: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0
2020-03-10 19:45:39.238695: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N
2020-03-10 19:45:39.238890: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7524 MB memory) -> physical GPU (device: 0, name: Device 731f, pci bus id: 0000:2b:00.0)
TensorFlow:  2.1
Model:       resnet50
Dataset:     imagenet (synthetic)
Mode:        training
SingleSess:  False
Batch size:  64 global
             64 per device
Num batches: 100
Num epochs:  0.00
Devices:     ['/gpu:0']
NUMA bind:   False
Data format: NCHW
Optimizer:   sgd
Variables:   parameter_server

Generating training model
WARNING:tensorflow:From /home/gpu-user/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:134: conv2d (from tensorflow.python.layers.convolutional) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.keras.layers.Conv2D` instead.
W0310 19:45:39.282001 139982497593152 deprecation.py:323] From /home/gpu-user/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:134: conv2d (from tensorflow.python.layers.convolutional) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.keras.layers.Conv2D` instead.
WARNING:tensorflow:From /home/gpu-user/.local/lib/python3.6/site-packages/tensorflow_core/python/layers/convolutional.py:424: Layer.apply (from tensorflow.python.keras.engine.base_layer) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
W0310 19:45:39.284210 139982497593152 deprecation.py:323] From /home/gpu-user/.local/lib/python3.6/site-packages/tensorflow_core/python/layers/convolutional.py:424: Layer.apply (from tensorflow.python.keras.engine.base_layer) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.__call__` method instead.
WARNING:tensorflow:From /home/gpu-user/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:266: max_pooling2d (from tensorflow.python.layers.pooling) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.MaxPooling2D instead.
W0310 19:45:39.321026 139982497593152 deprecation.py:323] From /home/gpu-user/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:266: max_pooling2d (from tensorflow.python.layers.pooling) is deprecated and will be removed in a future version.
Instructions for updating:
Use keras.layers.MaxPooling2D instead.
Initializing graph
WARNING:tensorflow:From /home/gpu-user/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2267: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
W0310 19:45:41.986801 139982497593152 deprecation.py:323] From /home/gpu-user/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:2267: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
2020-03-10 19:45:42.372816: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1573] Found device 0 with properties:
pciBusID: 0000:2b:00.0 name: Device 731f     ROCm AMD GPU ISA: gfx1010
coreClock: 0.1GHz coreCount: 40 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-03-10 19:45:42.373062: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-03-10 19:45:42.373111: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-03-10 19:45:42.373155: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-03-10 19:45:42.373201: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-03-10 19:45:42.373313: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1697] Adding visible gpu devices: 0
2020-03-10 19:45:42.373361: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1096] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-03-10 19:45:42.373398: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102]      0
2020-03-10 19:45:42.373431: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] 0:   N
2020-03-10 19:45:42.373560: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1241] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7524 MB memory) -> physical GPU (device: 0, name: Device 731f, pci bus id: 0000:2b:00.0)
terminate called after throwing an instance of 'std::runtime_error'
  what():  No device code available for function: _ZN10tensorflow7functor28FillPhiloxRandomKernelLaunchINS_6random27TruncatedNormalDistributionINS2_19SingleSampleAdapterINS2_12PhiloxRandomEEEfEEEEvS5_PNT_17ResultElementTypeExS8_, for agent: gfx1010
Fatal Python error: Aborted
`

---

### 评论 #11 — Ge0rges (2020-03-19T15:48:09Z)

Any update on the status of this issue?

---

### 评论 #12 — SlausB (2020-03-19T17:59:26Z)

I'm not a **ROCm** user, but I tried installing it just to get **OpenCL** working because as I found somewhere that it's how **ROCm** works on **AMD** devices: through **OpenCL**. So **ROCm** supposed to set **OpenCL** up, but failed in my case. Eventually, I got **OpenCL** working on **Ubuntu 18.04**, but I think it should work on any distro (only kernel version matters): https://askubuntu.com/questions/1209725/how-to-get-opencl-support-for-navi10-gpus-from-amd <-- that's how I managed to achieve it.
So I think if you guys set **OpenCL** up on your setup, **ROCm** should also work properly with **RX5700** (navi10-12)
I hope it helps ^^

---

### 评论 #13 — lrie (2020-03-19T18:07:20Z)

@SlavMFM 
As mentioned, I was able to install ROCm 3.1 and thus OpenCL. 
clinfo results look fine.
So there is Navi support, but it is not really functional. 
Look at the error above:
`No device code available for function: `
This seems to point to some not fully implemented libraries or missing assembler snippets.
A bit like a car without engine.

---

### 评论 #14 — SlausB (2020-03-19T18:45:33Z)

Interesting. Was you able to run some raw **OpenCL** examples to verify it's working properly? I once had "fake" **OpenCL** setup where `clinfo` was printing even GPU name (Radeon RX5700xt), but actual **opencl** functions from within **C++** wasn't working. I just can't imagine how **ROCm** could utilize AMD GPUs rather just through **OpenCL**, so it it's working, **ROCm** should work too, hmm...

---

### 评论 #15 — jemzipx (2020-03-19T18:51:50Z)

@SlavMFM As far as I know, AMD provides two seperate OpenCL 2.0 implementations. One in ROCm and another in AMDGPU PRO driver. I have tested the OpenCL 2.0 in AMDGPU PRO and can confirm it works fine (see my post above). Although, getting OpenCL to work does not guarantee that ROCm would work too.

---

### 评论 #16 — SlausB (2020-03-19T19:26:32Z)

@jemzipx cool! I'm surprised **amdgpu-pro** drivers can be actually installed ^^ - you just get **kernel 5.6** and install **amdgpu-pro** on top of it?
Btw, there is at least another *offician* support: **mesa** drivers where **AMD** devs directly implement their GPUs support, for example navi14 was implemented half-a-year before GPUs release: https://lists.freedesktop.org/archives/mesa-dev/2019-August/222273.html - that's how I got **OpenCL** working in my case: with **mesa-19.3** driver (which can stack on **> kernel 5.4**, but not **5.6**).

---

### 评论 #17 — jemzipx (2020-03-20T06:53:42Z)

@SlavMFM that is right. I installed amdgpu-pro on top of kernel 5.6rc in Manjaro (should work in Arch too). I tried Mesa before (actually that was the first thing I tried) but Mesa's OpenCL version was 1.2 which is quite old and kind of outdated. As far as I can tell, OpenCL 2.0 support for Navi can only be found in AMDGPU-PRO and ROCm. 

---

### 评论 #18 — SlausB (2020-03-20T09:47:11Z)

@jemzipx you think it'll work only on **Manjaro** and **Arch** and won't work on other distros like **Ubuntu**? Would like to try it on **Ubuntu** later.
I'm currently having **mesa-19.3** and it [claims](https://paste.ubuntu.com/p/rF7B3VVgks/) 2.1 platform and 2.0 device; not sure if it's practically 2.0 though.

---

### 评论 #19 — jemzipx (2020-03-20T11:35:58Z)

@SlavMFM It should work on all distros. I have only tested Manjaro personally. I'm also curious to know how it plays on Ubuntu. BTW, have you tested Keras/PlaidML with your Mesa OpenCL on Ubuntu? Please give it a go and let us know the result.

---

### 评论 #20 — mritunjaymusale (2020-03-25T15:07:03Z)

[Update]
I was able to compile and install pytorch using the latest ROCm 3.1.1 using [this guide](https://github.com/ROCmSoftwarePlatform/pytorch/issues/581). 
But I don't know how to install custom modules like DCNv2 that are C++ extensions of pytorch.
There was some prompt I kept getting everytime I used pytorch, I can't remember, neither can I test it since I'm afk.
All in all, things are looking better for Navi gpus, still no idea on when the official support will come through.

---

### 评论 #21 — Rmalavally (2020-03-29T22:23:48Z)

AMD ROCm is validated for GPU compute hardware such as AMD Radeon Instinct GPUs. Other AMD cards may work, however, they are not officially supported at this time. We appreciate your feedback and we will consider it for future versions of ROCm. 

Regards,
Roopa

---

### 评论 #22 — FiCacador (2020-03-29T23:41:08Z)

I don't think anyone here is asking for validation or even official support. All that Navi owners and potential buyers would like is for it to somehow work, now several months after it's release, just like it would work for them from day zero if they have got, say, a RTX 2070 using CUDA.
People understand that the resources are limited, that it's open software, that it's a new architecture, that it's not focused on computing... but after so much time without support or even confirmation that it will ever come, it looks like individuals with interest in these kind of projects that don't require validation and also game on the side unfortunately have only one choice and it's not AMD. Which is understandable from a business perspective, only too bad for those customers to have less options on the market.

---

### 评论 #23 — foolnotion (2020-03-29T23:52:51Z)

let's just call it AMD on the compute market is a joke at the moment and the only option for the consumer is to go nvidia. 

---

### 评论 #24 — jemzipx (2020-03-30T05:48:15Z)

@Rmalavally That is a very disappointing answer from an AMD's representative. The thing is that, Nvidia's success was due to the fact that every college gamer kid with their consumer-based GTX/RTX card could run deep learning algorithms as well. There are many of us that do not want to rely on Nvidia's propriety CUDA and would prefer to use open standards like OpenCL etc. This is a great business opportunity for AMD and is the one that matters more than designing graphic cards for next-gen xbox and playstation. We hope AMD change its approach to consumer-grade cards. 

---

### 评论 #25 — valeriob01 (2020-03-30T06:50:31Z)

> @Rmalavally That is a very disappointing answer from an AMD's representative. The thing is that, Nvidia's success was due to the fact that every college gamer kid with their consumer-based GTX/RTX card could run deep learning algorithms as well. There are many of us that do not want to rely on Nvidia's propriety CUDA and would prefer to use open standards like OpenCL etc. This is a great business opportunity for AMD and is the one that matters more than designing graphic cards for next-gen xbox and playstation. We hope AMD change its approach to consumer-grade cards.

This is not the first time we get disappointing answers from AMD, We ALL hope AMD change its approach to consumer-grade cards, and its approach to Radeon Instinct MI50 selling strategy for consumers too, not only for businesses.

---

### 评论 #26 — lrie (2020-03-30T09:16:35Z)

Well let's face it:
Jen-Hsun Huang said: "Nvidia is a Software Company," 
If you look at their stock chart, that may have been a wise decision.

If AMD decides to put all their effort on fancy 7nm tech, but does not want to spend the money for software developers, we just have to swallow that pill and move on.

---

### 评论 #27 — valeriob01 (2020-03-30T14:24:16Z)

> Well let's face it:
> Jen-Hsun Huang said: "Nvidia is a Software Company,"
> If you look at their stock chart, that may have been a wise decision.
> 
> If AMD decides to put all their effort on fancy 7nm tech, but does not want to spend the money for software developers, we just have to swallow that pill and move on.

it would be a bitter pill to swallow however...


---

### 评论 #28 — jemzipx (2020-04-04T12:19:51Z)

They released ROCm 3.3.0 today but (as we all expected) there is no official support for Navi yet :( All it takes for them is to hire someone to work on this full-time for a few weeks but apparently AMD has more pressing issues at the moment. Thank you AMD for ignoring your loyal supporters. 

---

### 评论 #29 — marcelocf (2020-04-05T03:57:28Z)

PLEASE do complete navi10 support! I bought this card just because of opensource support (bought in release day). Not having it feels like I paid for the full price of the card, but I can only use half of it.

---

### 评论 #30 — himanshugoel2797 (2020-04-06T11:29:54Z)

Yes, I agree. Please support navi10. It's absurd and disappointing that the latest and current flagship hardware still doesn't support rocm 6+ months after release and doesn't even have a timeline for it. At this rate might just have to begrudgingly go with Nvidia next generation.

It doesn't need to be support in the workstation cards sense, but atleast in the "you can use this card for ROCm applications" sense.

---

### 评论 #31 — Dantali0n (2020-04-11T12:39:25Z)

Hello, I think the only reasonable way we could expect widespread adoption of ROCm if it is supported by all AMD cards just like Nvidia's CUDA. The era of GPGPU compute is shifting more and more applications and developers are realizing when not gaming these cards can significantly improve the performance of many applications. ROCm can only be relied upon by developers if it is supported by all cards otherwise they would be better of writing OpenCL or something that generates to SPIR-V and than compiling to vulkan or similar.

By not supporting all cards you are effectively wasting the entire developing effort of ROCm and all the time of the employees and contributors who worked on it. Please, I encourage AMD to heavily reconsider their stance.

---

### 评论 #32 — Anton-Kyrychek (2020-04-23T10:03:14Z)

@jemzipx 
Hey, I'm trying to make  my rx5700xt work  the same as you did(but on Ubuntu 18.04). I installed 5.7rc2 kernel,  I have a question  how did you install AMDGPU PRO? I find a lot of problems with dependencies when i tried to do it(which may or may not be connected to Ubuntu).

---

### 评论 #33 — jemzipx (2020-04-23T12:35:34Z)

@Anton-Kyrychek I installed AMDGPU PRO through AUR (which is more specific to Arch Linux and it's derivatives like Manjaro). The installation was quite easy and the dependencies were resolved by Makepkg and Pacman automatically (nothing special was done on my side). I tried it only on 5.6 though. Not sure how it plays on 5.7rc. 

---

### 评论 #34 — PhilipDeegan (2020-04-27T15:24:29Z)

> AMD ROCm is validated for GPU compute hardware such as AMD Radeon Instinct GPUs. Other AMD cards may work, however, they are not officially supported at this time. We appreciate your feedback and we will consider it for future versions of ROCm.
> 
> Regards,
> Roopa

You may want to update the docs: 
https://github.com/RadeonOpenCompute/ROCm

> "Vega 10" chips, such as on the AMD Radeon RX Vega 64 and Radeon Instinct MI25

It does not suggest Navi support, but Vega is fine.

---

### 评论 #35 — Ge0rges (2020-04-27T15:32:37Z)

@Anton-Kyrychek could you let us know if you are successful in using the RX 5700 XT card on ubuntu, and if so what steps you followed? Looking to use it with pytorch on ubuntu 19.

---

### 评论 #36 — Anton-Kyrychek (2020-04-28T10:41:17Z)

@Ge0rges I was not, I'm not that smart with drivers. 

---

### 评论 #37 — mritunjaymusale (2020-04-28T15:38:44Z)

@Ge0rges 
try this method, this is what I have used with little success 
https://github.com/ROCmSoftwarePlatform/pytorch/issues/581

---

### 评论 #38 — Ge0rges (2020-04-29T18:22:46Z)

@mritunjaymusale that worked for you on the 5700XT?

---

### 评论 #39 — mritunjaymusale (2020-04-29T19:08:13Z)

@Ge0rges  yes it worked for me.

---

### 评论 #40 — limapedro (2020-04-30T00:29:05Z)

I've been following ROCm for a long time, I don't know a lot about the team behind, but it seems like AMD doesn't really care about us yet, GPU computing will be a huge part of the software stack, I see no reason to buy AMD GPUs at the moment, maybe they'll support Big Navi, unfortunately, AMD is years behind the competition in this area, imagine how many developers and consumers would benefit from AMD's adoption of GPU computing, anyway I'll continue to follow this thread and see if AMD change its ways in the near future. 

---

### 评论 #41 — xinyazhang (2020-04-30T23:00:09Z)

I really do not think this is the right strategy to market rocm by only focusing on Radeon Instinct.

The most common choices in my lab (and nearby labs) are GTX 1080Ti and 2080 RTX. The AI lab in our department has a cluster with Titan V GPUs, but nobody in my University, as far as I know, ever purchased the Tesla product line from NVIDIA for deep learning.

It's not difficult to realize the fact that deep learning researchers/developers always start with customer grade cards, and they may never consider the professional grade cards due to high costs.
A professional-market-only approach will not bring new professional developers/researchers, ironically.

---

### 评论 #42 — Ge0rges (2020-05-01T13:54:01Z)

@mritunjaymusale I've been able to compile pytorch with ROCm as per your link. However tests fail because HIP gives an `hipErrorNoDevice` error. Were you able to solve that?

---

### 评论 #43 — mritunjaymusale (2020-05-01T13:58:56Z)

@Ge0rges I got the rocBlas error that's hinting to the device driver i believe this has to do with rocm not fully supporting the navi cards. 
I think we might have to compile rocm from scratch itself and see if it even accepts navi cards 

---

### 评论 #44 — Ge0rges (2020-05-01T14:10:48Z)

@mritunjaymusale Ah so it never worked for you I guess? I'll let you know if I have success compiling ROCm.

---

### 评论 #45 — Ge0rges (2020-05-01T15:00:50Z)

I wonder if anyone has gotten Pytorch to work with RX 5700XT through OpenCL similarly to @jemzipx 

---

### 评论 #46 — jemzipx (2020-05-01T17:26:39Z)

@Ge0rges AFAIK, PyTorch does not support OpenCL. In fact, PyTorch developers have been quite hostile towards OpenCL so far:
pytorch/pytorch#488

---

### 评论 #47 — KellieOwczarczak (2020-05-08T21:47:03Z)

I am certainly struggling to really understand where this stands. I am looking to build an AMD machine for ROCm development purposes and am considering the RX 5700XT vs a Radeon VII. Really sounds like the VII is the way to go as there still is not Navi support. Do I have that right?

---

### 评论 #48 — KellieOwczarczak (2020-05-08T22:40:27Z)

@mritunjaymusale Got the NVidia already. Wanting to do the AMD more for exploration, and understanding what is possible if that makes sense. Shoot, in a perfect world, I would do the ROCm in macOS, but truth is that's too much trouble to be worthwhile. But, thanks for more or less confirming that the VII is what I should go with for the AMD machine. ;)

---

### 评论 #49 — Djip007 (2020-05-09T20:01:11Z)

@ThemysciraData
now supported card here:
https://github.com/RadeonOpenCompute/ROCm#supported-gpus
for low GPU RX580 ... for highend card Radeon VII  (or Instinct card...)
(RX 5700XT  when supported will be slower than Radeon VII )
Note: new GCC10 (https://gcc.gnu.org/gcc-10/changes.html) support offoading with old Fiji or the never VEGA 10/VEGA 20 (no support for polaris now...)

---

### 评论 #50 — KellieOwczarczak (2020-05-09T20:16:12Z)

@Djip007 I appreciate the link, but what makes you think I had not already looked at it? 

---

### 评论 #51 — Djip007 (2020-05-11T16:40:39Z)

> @Djip007 I appreciate the link, but what makes you think I had not already looked at it?

Because I was sleeping when I read your last post... read a question... with isn't ;)
Sorry

---

### 评论 #52 — EwoutH (2020-05-12T17:09:07Z)

I never expected it to get this bad. It's just sad. Can't wait for Ampere at this point.

---

### 评论 #53 — jemzipx (2020-05-13T11:42:53Z)

@EwoutH Exactly. AMD is making a huge mistake and they don't even know it. They have already lost a lot of customers because of this. What kind of company treats the customers of their flagship desktop GPU product like this? What is even more sad is that I have to use PlaidML (which is written by AMD's arch rival: Intel) to do some basic deep learning on 5700XT. There is absolutely NO solution by AMD to do deep learning on 5700XT and this is just devastating.

---

### 评论 #54 — Tzigamm (2020-05-13T22:26:29Z)

Just saw the articles about how the new Radeon VII Pro gpu is based on vega, which may mean the next pro architecture will be based on navi. If AMD really only plans on supporting pro gpus we might actually never get support for our flagship cards.

Granted this is based on too much assumptions but I really don't like that we have to **guess**. I just wish AMD would talk to us about these things, the amount of unanswered questions about this card is phenomenal

---

### 评论 #55 — Qwertie- (2020-05-14T00:58:35Z)

It's pretty sad that this has been ignored. The 5700xt is such a great bit of hardware let down by such poor software. At this point it seems that if that if you ever want to use your gpu for more than gaming then nvidia is the only real option.

---

### 评论 #56 — jamcinnes2 (2020-05-14T01:11:42Z)

Same here. Great card for flight sims. Was planning to use it for compute also. Guess I will ebay it.

---

### 评论 #57 — truesamurai (2020-05-14T12:50:35Z)

I have a 5500XT which is also Navi. I am new to this, would this be an alternative : https://math.dartmouth.edu/~sarunas/amdgpu.html 

---

### 评论 #58 — Tzigamm (2020-05-14T12:53:33Z)

@sh1va73 It should work yes, I know people on ubuntu/arch use a somewhat similar solution (using amdgpu-pro for opencl and amdgpu for the rest) although I'm not sure if it's against AMD's TOS or not

---

### 评论 #59 — FiCacador (2020-05-14T14:02:14Z)

@sh1va73 yes that would work, I have done it on an Ubuntu based distro and I have a similar situation now on an Arch based distro where only the necessary components (opencl-amdgpu-pro-pal from AUR and it's dependencies) of the amdgpu-pro proprietary package are installed.

Unfortunately AMD doesn't provide the display driver and the opencl driver in separate packages, which prevents Linux distros from packaging and redistributing only the opencl part (AUR provides just a script that builds the packages on the user's computer, so no infringement).

And sadly AMD hasn't open sourced (yet?) it's opencl driver. If they were to do that and contribute it to the mesa library, anyone would be able to easily install it on any Linux distro and lots of ROCm complaints from people who only want a working open source opencl driver would have been avoided.

---

### 评论 #60 — limapedro (2020-05-14T14:25:32Z)

Today we got a lot of news in the HPC segment, will AMD have any event related to HPC and ML soon?

---

### 评论 #61 — Dantali0n (2020-05-14T14:42:23Z)

> Today we got a lot of news in HPC segment, will AMD have any event related to HPC and ML soon?

Maybe when they launch RDNA 2 cards which should be within 1 to 2 months.

---

### 评论 #62 — himanshugoel2797 (2020-05-14T17:09:39Z)

> Today we got a lot of news in HPC segment, will AMD have any event related to HPC and ML soon?

AMD have a virtual event relating to GPUOpen's relaunch tomorrow, so maybe there we'll get more info on what's coming up. They do have a new library for machine learning inference for instance.

---

### 评论 #63 — BloodBlight (2020-05-18T17:29:53Z)

@Rmalavally 
AMD Spent millions developing and advertising navi, and customers are buying it!  Why would you then not support it?!?  I'm sorry, but that is a poor answer at best and really feels like a stab in the back!

---

### 评论 #64 — limapedro (2020-05-20T00:37:51Z)

@BloodBlight They could also support Windows, there is no date release for a version that works on Windows, today we got news about the competition bringing their accelarator to Windows through WSL, I think Rocm could to something similar, they just need to work with Microsoft on this one too.

---

### 评论 #65 — limapedro (2020-05-27T16:46:25Z)

Hey everybody just saw this on my timeline, I think there's still hope. 
As soon as I test this I'll be posting updates.
https://twitter.com/AMDRyzen/status/1265681670918688768

---

### 评论 #66 — Dantali0n (2020-05-27T18:24:13Z)

> Hey everybody just saw this on my timeline, I think there's still hope.
> As soon as I test this I'll be posting updates.
> https://twitter.com/AMDRyzen/status/1265681670918688768

I think you read that wrong, it explicitly states **vega** graphics which are **GCN** micro-architecture and already supported by ROCm. The 5700xt is of the newer **RDNA** micro-architecture.

---

### 评论 #67 — limapedro (2020-05-27T19:33:08Z)

@Dantali0n In the demo the guy was using a Vega 9 Graphics, I don't think neither Vega 9 or 11 runs on Rocm, with regarding the RX 5700 XT if I not mistaken the idea is to run on top of DirectX 12, they stated multiple GPU vendors support, again they're still a lot of unknown details. But this seems promising to the ML community.

---

### 评论 #68 — Anton-Kyrychek (2020-05-28T10:25:14Z)

@limapedro if that means that AMD will release drivers to Open Source it would be great, but i feel it's going to be the case where i have AMD r3 2200G (a CPU for 50$) which will be able to do ML coz it has integrated Vega, and RX 5700 XT will not be able to do it coz it's navi

---

### 评论 #69 — pavhl (2020-05-28T10:28:09Z)

@Anton-Kyrychek In their announcement video Microsoft stated that there will be "Hardware accelerated training supported on any DirectX 12 GPU".
Looks like it won't depend on ROCm and my guess is that it won't be open source. Their WSL2 VM probably uses the DirectX API of Windows.

---

### 评论 #70 — limapedro (2020-05-28T17:20:21Z)

@Crash129 Exactly, I  almost certain that it'll support ONNX, so models could be deployed in a wide range of platforms, I think AMD is working with Microsoft on  this, there were some discussions, DirectX seems robust enough to add ML ops on it, the cool thing about this is that almost every device will be able to be hardware accelerated for ML. Hopefully AMD will now be a viable option for ML on Windows as well.

https://groups.google.com/a/tensorflow.org/forum/#!topic/developers/UzOZ5BAnOa4

---

### 评论 #71 — ridvan5005 (2020-05-30T18:07:15Z)

I couldn't believe what I read. I bought a Radeon 5600 xt without knowing them. Doesn't AMD offer anything other than gaming right now? I hope that the update will come for Navi 10 as soon as possible.

---

### 评论 #72 — BloodBlight (2020-05-30T20:05:51Z)

Frankly, I was within 30 days and just returned my 5700 XT... It didn't do the one thing I really bought it for, so... So just to be clear, @Rmalavally, you have lost a long term customer (one who also builds data centers and used AMD for over a decade at home), and you will be hard pressed to win me back... I was truly excited about the prospect of moving away from Big Green at work! But frankly, I am underwhelmed by your new Vega offering, and your point of entry into the market (what Navi should have been) sucks!

---

### 评论 #73 — jemzipx (2020-06-04T10:40:31Z)

AMD released 3.5.0 today with no Navi support. This is getting ridiculous but above all it looks intentional. It is almost one year since first Navi release. Roughly 70% of Navi support is already in the code base so they need to just work out the remaining 30%. The question is why are they unwilling to complete Navi support? Could it be because they are ashamed of the poor compute performance of their current 5700XT flagship desktop GPU against nvidia's GPUs?  Whatever the reason is, it sounds more like a marketing/management decision and not due to lack of resources or developers. By the look of it, they are holding back supporting RDNA on ROCm until at least Big Navi release. 

---

### 评论 #74 — limapedro (2020-06-04T12:58:54Z)

@jemzipx Well, the good news in that Directml seems to be a better option over Rocm, AMD is years late with their GPU support for Deep Learning, Big Navi will probably be out by november depending on how good it performs and the fact that by then tensorflow-directml should be out, I will consider buying AMD cards, either way let's watch things to play out in the next months I guess.

---

### 评论 #75 — marcelocf (2020-06-05T00:45:37Z)

@limapedro sadly directml is not an option for Linux users. The only reason I went AMD this time was the opensource drivers.

This morning I realized that another player is coming with (hopefully) opensource drivers - Intel. And those guys seem to have a better track record on releasing Linux support in a timely matter. Sad for my navi card, but looking forward to see what the competition will bring to this space.

---

### 评论 #76 — limapedro (2020-06-05T15:10:49Z)

@marcelocf Yeah this solution wouldn't work on linux. Hopefuly this will open AMD's eyes.

---

### 评论 #77 — jemzipx (2020-06-05T18:02:54Z)

@limapedro DirectML looks exciting but I don't see myself switching to windows anytime soon.

@marcelocf Intel has been doing some really cool stuff in deep learning recently. Their oneDNN is already in great shape (works like a charm on AMD cpus as well) and they have been developing PlaidML for some years now. PlaidML is the only OpenCL deep learning framework that is actively developed and also works great with Navi cards. The irony is that Intel's libraries provide best deep learning solution for AMD hardware! I am not an Intel fan but you got to give them props for supporting open source. 

---

### 评论 #78 — 0rzech (2020-06-05T20:57:55Z)

> AMD ROCm is validated for GPU compute hardware such as AMD Radeon Instinct GPUs. Other AMD cards may work, however, they are not officially supported at this time. We appreciate your feedback and we will consider it for future versions of ROCm.

@Rmalavally This makes it really hard, if not impossible, for me to consider my last year's 5700 XT purchase money well spent now.

> The only reason I went AMD this time was the opensource drivers.

@marcelocf That was the main selling point for me too. I thought ROCm would include Navi and that's why OpenCL was not added to open-source AMDGPU Linux driver. Tough luck.

---

### 评论 #79 — Djip007 (2020-06-05T22:30:10Z)

For OpenCL look like the close source driver is working for 5700XT...

For me the question is why all (most?) open-source DNN (TensorFlow/Pytorch...) have only CUDA close source support... 
May be OpenCL-next (ie Vulkan-compulte?) may help... some day... 

For my laptop https://www.asus.com/TUF-Gaming/ASUS-TUF-Gaming-FX505DY/ with 
Ryzen 3550H + RX560 work with tensorflow-rocm pretty good

But like you I dream with the last DELL laptop https://www.dell.com/en-us/shop/laptops/new-15-special-edition/spd/g-series-15-5505-laptop 
with Ryzen4800H+RX5600M... 

Other dream is with Ryzen 4x00U (or the Picasso 3x00U...) have the possibility to use the Vega APU with rocm for compute (OpenCL work... not HIP...)

---

### 评论 #80 — jemzipx (2020-06-06T11:02:31Z)

@Djip007 The PyTorch team claims that OpenCL performance is far inferior to CUDA (a claim I highly doubt). They also believe that OpenCL is abandoned by most hardware manufactures. With AMD focusing on HIP, Nvidia on CUDA, only Intel is fully dedicated to supporting OpenCL. With the underwhelming release of OpenCL 3.0 it seems like even Khronos Group is not taking its own standard seriously. 

---

### 评论 #81 — marcelocf (2020-06-06T11:12:59Z)

Machine Learning is not the only application for OpenCL, though. I want to use it primarily in blender with cycles.

---

### 评论 #82 — limapedro (2020-06-06T11:58:29Z)

@marcelocf That a very interesting take, there's a bunch of programs that use OpenCL, so much so that I don't think that OpenCL would lose support anytime soon, in this case maybe if Khronos added some ML ops onto OpenCL, it could become a ML runtime standard, even more so than Rocm, Directml and Cuda.

---

### 评论 #83 — Djip007 (2020-06-06T15:31:58Z)

OpenCL is not dead... 
rocm2.0 have update to OpenCL2.0...
new rocm3.5 have juste been update to OpenCL2.2
so not update for RDNA... but big update for OpenCL (C++ support...)

---

### 评论 #84 — justxi (2020-06-07T13:18:07Z)

@Djip007 Which GPU is needed to use OpenCL 2.2?

---

### 评论 #85 — Djip007 (2020-06-11T17:40:54Z)

with rocm official liste:
https://github.com/RadeonOpenCompute/ROCm#supported-gpus

---

### 评论 #86 — limapedro (2020-06-17T17:35:45Z)

Why everyone, just an update on tensorflow-directml, yesterday a pypi went public, although it still doesn't work, I will keep an eye on it, anyone interested as well? I would like to test this one AMD GPUs and see how good it performs. Especially the RTX 2070 Super vs RX 5700 XT.

https://pypi.org/project/tensorflow-directml/0.0.1.dev0/

---

### 评论 #87 — PeterNjeim (2020-06-21T05:59:24Z)

Hello,

My friend has an RX 5700 XT. Just wanted to share that I tested his PC with DirectML and it worked! The only problem is that it doesn't support TensorFlow 2 yet, so you're stuck on 1.15 (or whatever the last version of TensorFlow 1 is).

I know this isn't the solution everyone wanted, as it requires Windows 10 even though it does work on Linux, just WSL2 specifically. I didn't test it in WSL2 though, I just ran it natively in Windows, following Microsoft's official instructions.

Hopefully it works on other Navi cards, take care.

---

### 评论 #88 — mthxx (2020-06-21T13:35:56Z)

I am anxiously awaiting support for the 5700xt. I've been unable to use Davinci Resolve since upgrading to an Ubuntu 20.04 base since the propriety OpenCL drivers don't support 20.04. 

I've been relegated to using alternative video editing software in the meantime which has proven to be less functional, buggier, and slower and it's beginning to cost me. I've been avoiding purchasing an Nvidia GPU and have gone out of my way to support AMD for their support of open source drivers. But I know for a fact that I can return my workflow too normal by switching too Nvidia.

---

### 评论 #89 — sofiageo (2020-06-21T14:59:14Z)

> upgrading to an Ubuntu 20.04 base since the propriety OpenCL drivers don't support 20.04.

I know nothing about Davinci Resolve but the AMD drivers are made for 20.04, it's even in the file name. https://drivers.amd.com/drivers/linux/amdgpu-pro-20.20-1089974-ubuntu-20.04.tar.xz

---

### 评论 #90 — limapedro (2020-06-21T17:13:35Z)

@PeterNjeim Nice, I still wasn't able to run tensorflow-benchmark on directml, but since every directX 12 device will be capable of running tensorflow-directml, the number of devices that can be tested is huge. I still don't know about multi-gpu training, I think that multi_gpu from keras in TF 1.15 should work.

---

### 评论 #91 — PeterNjeim (2020-06-21T17:41:02Z)

> @PeterNjeim Nice, I still wasn't able to run tensorflow-benchmark on directml

That is because TensorFlow doesn't recognize DirectML devices as GPU's, but rather "DML"s. Basically, you have to manually edit the Python and replace most instances of "GPU" to "DML". You can't do this automatically, because some functions directly have the word "gpu" in them, and so you can't replace them, and some functions have the word "cuda" in them, and so you'll have to comment those out (well I think you do, not sure).

It's a very hacky solution by Microsoft, and make sure to comment out all of the GPU checks (some scripts check to see if a GPU is connected, you'll have to skip that check as you know yourself that your GPU is connected, but it's just via DML). Also, remember that you can't run anything that requires TF2.

Hopefully you'll be able to run whatever you need using these steps.

---

### 评论 #92 — PeterNjeim (2020-06-21T17:50:39Z)

I recommend using DirectML's own samples as they're known to work: https://github.com/microsoft/DirectML/tree/master/TensorFlow

However I tried running the squeezenet one and the tracing part failed, and judging by the errors I recieved, I'm pretty sure it's due to the fact I wasn't using WSL2, as it was trying to execute Linux command line arguments. So if you want to try those, you may want to be using WSL2 instead of native Windows 10.

---

### 评论 #93 — limapedro (2020-06-21T18:37:14Z)

@PeterNjeim Thanks, I'll try these changes.

---

### 评论 #94 — hexvalid (2020-06-26T06:55:12Z)

Any updates for 5700 XT Support?

---

### 评论 #95 — hbfs (2020-07-05T05:49:10Z)

Not gonna happen. Not officially anyway. 
AMD is diverging gaming and compute workloads to two different product lines. Arcturus is the next compute card

It would be nice to have a specific compute card given gaming and compute workloads are diverging.. but the lack of a second hand market after considering product cadence and TCO, specifically $/watt makes me question the business decision. e.g. Last gen, mining only, GPU cards are worthless. Not only does it cripple resale value, its a big ewaste problem.

nVIDIA is doing similar but keeping CUDA available on the Geforce lineup. This is fantastic for students, individual researchers and anyone else without a budget to spend $$$$ on enterprise hardware. The Geforce line continues to retain value which also allows those same researchers an upgrade path towards those enterprise cards once their research bears fruit (and revenue). 

This is also possible due to nVIDIA's software. AMD software needs some finessing so that maybe another reason to separate gaming and compute.

---

### 评论 #96 — MasonProtter (2020-08-03T17:06:38Z)

Just to chime in with my own anecdote: I'm a physicist with an nvidia card that I bought for gaming. It's incredibly useful to be able to prototype CUDA workflows on my personal card and just learn the ins and outs of GPU programming with it before running something more serious on a cluster. I would never be able to justify buying myself a CDNA card just for compute, but I could justify buying myself an RDNA card for gaming and occasional compute. Crippling it's compute performance is fine, so long as it actually runs with official support. Just not supporting ROCm it means I probably can't switch to AMD's RDNA cards even though I would really like to. 

---

### 评论 #97 — jpsamaroo (2020-08-03T17:13:59Z)

As the maintainer of the Julia language's [AMDGPU compute stack](https://github.com/JuliaGPU/AMDGPU.jl), I'm saddened to see how AMD is dragging their feet on support for this card, as well as hearing whispers of the possibility for loss of support for "consumer" cards in ROCm going forward. I personally only have access to consumer Polaris and Vega AMD GPUs, and if those cards did not work in ROCm, I don't think I would have ever started working on the above-linked stack, and would have sold my GPUs for NVidia GPUs instead.

It's important that AMD realizes how open source *really* works: random people from all over the world come together to build something that helps everyone. When the tools that such open source software utilizes are cheap and accessible to "regular" consumers, and the software is supported on and designed for these devices, then users have an incentive to buy those devices, install the software, report issues, and eventually send improvements upstream. Without those users, you end up with a software stack that only works on big clusters (and just barely, at that), is performant only on the problems that grants or budgets have paid for, and lack of uptake in both the enterprise and in smaller businesses and communities.

I hope that AMD will reconsider its strategy and put human resources onto getting the Navi line supported ASAP, and more importantly, ensure that *all* future consumer cards are properly supported by ROCm.

---

### 评论 #98 — acowley (2020-08-03T18:17:05Z)

There are [signs](https://github.com/ROCm-Developer-Tools/HIP/pull/2103) that AMD has shifted to more of a source release model than open source development. That is surely disappointing, but not inextricably tied to the lack of Navi support. The observation that widespread availability of ROCm support (i.e. consumer hardware) has value is important even if AMD does not want to use an OSS development model.

---

### 评论 #99 — VladUshakov1995 (2020-08-04T13:36:18Z)

Wow, this guy did what we could not... and wrote a [blog post](https://www.preining.info/blog/2020/05/switching-from-nvidia-to-amd-including-tensorflow/) about it 

---

### 评论 #100 — xuhuisheng (2020-08-05T00:01:01Z)

I found https://github.com/smartbitcoin/MyROCm uploaded a custom binary supporting 5700xt base on rocm-3.0.6.
related issues : https://github.com/RadeonOpenCompute/ROCm/issues/938  https://github.com/RadeonOpenCompute/ROCm/issues/1003

---
