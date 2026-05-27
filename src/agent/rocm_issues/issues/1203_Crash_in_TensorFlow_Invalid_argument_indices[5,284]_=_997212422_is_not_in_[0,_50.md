# Crash in TensorFlow: "Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)" in classification tutorial

> **Issue #1203**
> **状态**: closed
> **创建时间**: 2020-08-25T13:26:50Z
> **更新时间**: 2021-01-26T10:46:55Z
> **关闭时间**: 2020-12-29T08:44:04Z
> **作者**: kroll-j
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1203

## 描述

I'm working through the basic tutorials on the TensorFlow website. In the second tutorial, I get a weird crash. This is the tutorial: https://www.tensorflow.org/tutorials/keras/text_classification 
I'm trying to run the solution provided here: https://github.com/tensorflow/examples/blob/master/community/en/text_classification_solution.ipynb

I get output like this:
```
tf.__version__: 2.3.0
Found 8000 files belonging to 4 classes.
Using 6400 files for training.
2020-08-25 15:09:14.920446: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
2020-08-25 15:09:14.930506: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:08:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.366GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-08-25 15:09:14.932126: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-25 15:09:14.932805: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-25 15:09:14.936516: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-08-25 15:09:14.936658: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-08-25 15:09:14.936727: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-08-25 15:09:14.936940: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-08-25 15:09:14.941538: I tensorflow/core/platform/profile_utils/cpu_utils.cc:104] CPU Frequency: 3593240000 Hz
2020-08-25 15:09:14.942285: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f412c8674e0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-08-25 15:09:14.942302: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-08-25 15:09:14.943684: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f412c713100 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-08-25 15:09:14.943694: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], AMDGPU ISA version: gfx803
2020-08-25 15:09:15.181846: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1734] Found device 0 with properties: 
pciBusID: 0000:08:00.0 name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590]     ROCm AMD GPU ISA: gfx803
coreClock: 1.366GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 0B/s
2020-08-25 15:09:15.181918: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-25 15:09:15.181936: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libMIOpen.so
2020-08-25 15:09:15.181951: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocfft.so
2020-08-25 15:09:15.181966: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocrand.so
2020-08-25 15:09:15.182062: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
2020-08-25 15:09:15.182086: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-08-25 15:09:15.182095: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      0 
2020-08-25 15:09:15.182103: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 0:   N 
2020-08-25 15:09:15.182238: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7700 MB memory) -> physical GPU (device: 0, name: Ellesmere [Radeon RX 470/480/570/570X/580/580X/590], pci bus id: 0000:08:00.0)
Found 8000 files belonging to 4 classes.
Using 1600 files for validation.
Found 8000 files belonging to 4 classes.
2020-08-25 15:09:15.624322: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:15.625583: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:15.630665: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:15.632282: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
 ========== calling model.fit()
2020-08-25 15:09:16.676462: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:16.695113: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
Epoch 1/5
2020-08-25 15:09:16.899558: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:16.905277: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library librocblas.so
2020-08-25 15:09:16.905468: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
191/200 [===========================>..] - ETA: 0s - accuracy: 0.3212 - loss: 1.37282020-08-25 15:09:24.206187: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
199/200 [============================>.] - ETA: 0s - accuracy: 0.3232 - loss: 1.37212020-08-25 15:09:24.285358: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:24.303358: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:24.352910: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
2020-08-25 15:09:24.356064: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:505] ROCm Fusion is enabled.
Traceback (most recent call last):
  File "solution.py", line 87, in <module>
    history = model.fit(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 108, in _method_wrapper
    return method(self, *args, **kwargs)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 1123, in fit
    val_logs = self.evaluate(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 108, in _method_wrapper
    return method(self, *args, **kwargs)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/keras/engine/training.py", line 1379, in evaluate
    tmp_logs = test_function(iterator)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/def_function.py", line 780, in __call__
    result = self._call(*args, **kwds)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/def_function.py", line 814, in _call
    results = self._stateful_fn(*args, **kwds)
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 2829, in __call__
    return graph_function._filtered_call(args, kwargs)  # pylint: disable=protected-access
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 1843, in _filtered_call
    return self._call_flat(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 1923, in _call_flat
    return self._build_call_outputs(self._inference_function.call(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/function.py", line 545, in call
    outputs = execute.execute(
  File "/home/user/.local/lib/python3.8/site-packages/tensorflow/python/eager/execute.py", line 59, in quick_execute
    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,
tensorflow.python.framework.errors_impl.InvalidArgumentError: 2 root error(s) found.
  (0) Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)
	 [[node sequential/embedding/embedding_lookup (defined at solution.py:87) ]]
	 [[sequential/embedding/embedding_lookup/_10]]
  (1) Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)
	 [[node sequential/embedding/embedding_lookup (defined at solution.py:87) ]]
0 successful operations.
0 derived errors ignored. [Op:__inference_test_function_2262]

Errors may have originated from an input operation.
Input Source operations connected to node sequential/embedding/embedding_lookup:
 sequential/embedding/embedding_lookup/2185 (defined at /usr/lib/python3.8/contextlib.py:113)

Input Source operations connected to node sequential/embedding/embedding_lookup:
 sequential/embedding/embedding_lookup/2185 (defined at /usr/lib/python3.8/contextlib.py:113)

Function call stack:
test_function -> test_function

2020-08-25 15:09:24.456958: W tensorflow/core/kernels/data/cache_dataset_ops.cc:798] The calling iterator did not fully read the dataset being cached. In order to avoid unexpected truncation of the dataset, the partially cached contents of the dataset will be discarded. This can happen if you have an input pipeline similar to `dataset.cache().take(k).repeat()`. You should use `dataset.take(k).cache().repeat()` instead.
```

The numbers in ```(0) Invalid argument:  indices[5,284] = 997212422 is not in [0, 5001)``` vary, that is, the index and the invalid value change from one run to the next. The time it takes until it bails out also varies; sometimes it bombs in the first Epoch, sometimes the second, etc. Once the whole ```model.fit()``` call ran through, and after that, I seemed to be able to use the model just fine. But in ~95% of cases, it crashes.

I tried to run it in Docker as well as on a ROCm installation on Debian bullseye, with the same result. Upgrading from linux 5.8 to 5.9-rc2 didn't change anything, either. I'm using upstream kernel drivers as I had problems installing the DKMS module. When I set ```HIP_VISIBLE_DEVICES=-1```, forcing the example to run on the CPU, it works just fine. Could this be a bug in ROCm? Something wrong with my installation?

---

## 评论 (28 条)

### 评论 #1 — kroll-j (2020-08-27T09:07:38Z)

I was able to install rocm-dkms with the 3.7 release. That made no change though, I still get the same crashes.

I would really like to get over this problem. Anything I can do to debug this? Is there any more information needed from my side? Any ideas, pointers?

---

### 评论 #2 — xuhuisheng (2020-08-27T09:43:57Z)

ubuntu 20.04
rocm 3.7
python 3.8 (anaconda)
tensorflow 2.3.0
gfx803 rx580
using docker

failured everytime on rocm-3.7.0

```
tensorflow.python.framework.errors_impl.InvalidArgumentError: 2 root error(s) found.
  (0) Invalid argument:  indices[3,36] = 991268494 is not in [0, 5001)
	 [[node sequential/embedding/embedding_lookup (defined at test2.py:74) ]]
	 [[sequential/embedding/embedding_lookup/_10]]
  (1) Invalid argument:  indices[3,36] = 991268494 is not in [0, 5001)
	 [[node sequential/embedding/embedding_lookup (defined at test2.py:74) ]]
```

Its weired, using same hardware without docker, switch to ubuntu 18.04 and rocm 3.5.1, try 5 times, didnot meet the error yet.

update 1:
Same error on ubuntu 20.04, rocm 3.7 without docker. maybe this is the bug of rocm 3.7 for gfx803. hadnot gfx900 or gfx906 to test.

---

### 评论 #3 — kroll-j (2020-08-28T10:06:08Z)

@xuhuisheng thanks for your reply. So it is reproducible for at least 2 users in several environments. 

So how do we get this information to the AMD developers? They don't seem to be monitoring github issues...

---

### 评论 #4 — xuhuisheng (2020-09-03T03:22:23Z)

I reinstall miopen-2.4.0 from ROCm-3.5.0, overwrite the miopen-2.6.0 from ROCm-3.7.0.
http://repo.radeon.com/rocm/apt/3.5.1/pool/main/m/miopen-hip/
Then the error had gone. So It may be something broken in miopen-2.6.0 for gfx803.
Found an issue about gfx803 from miopen https://github.com/ROCmSoftwarePlatform/MIOpen/issues/135

update: not problem of miopen, reinstall miopen-2.4.0 to the wrong directory, so the tf used cpu to run the test, after correct the directory to the /opt/rocm/, the invalid argument error still there.

update1: Complied rocBLAS with BUILD_WITH_TENSILE_HOST=false, then the problem resolved. I will do more test for gfx803 on rocm-3.7.0. This seems the new tensile client is invalid on gfx803.

---

### 评论 #5 — kroll-j (2020-09-10T14:39:40Z)

Thanks for you research so far, @xuhuisheng! What side effects will building with BUILD_WITH_TENSILE_HOST=false have? Degraded performance?

---

### 评论 #6 — xuhuisheng (2020-09-11T05:04:41Z)

@jkroll20 Dont know the real effect yet. The BUILD_WITH_TENSILE_HOST is set to false until rocm-3.7.0. So we wont meet the issue before.
The new and old clients are totally separated source codes, and both of them exsits a long time. Looks like AMD never test new tensile client under gfx803.
The new tensile client will add Kernel.hsaco and TensileLibrary_gfx803.co into rocBLAS.deb, the images will be imported by tensorflow on runtime.  I guess there could be some improvement on new tensile client. But it isnot easy to dig.

update:
Testing BUILD_WITH_TENSILE_HOST true/false for text_classicfication.
BUILD_WITH_TENSILE_HOST=false 3s/15ms per epoch
BUILD_WITH_TENSILE_HOST=true  3s/16ms per epoch - there is 10% chance to success on my gfx803 with new tensile client.
Since the last modify of r9nano_x.yaml is 2 years ago. The new client looks like wont make performance improvement on gfx803.

---

### 评论 #7 — kroll-j (2020-10-11T11:10:52Z)

The issue is still present in rocm 3.8.

---

### 评论 #8 — kroll-j (2020-10-12T10:10:11Z)

@Rmalavally @jedwards-AMD @aak-amd @jlgreathouse 
This issue makes ROCm fail on simple tasks such as the TensorFlow tutorials on the RX580, which is on the list of [supported hardware](https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support). It is present in rocm 3.7 and 3.8. It is reproducible by at least two users, @xuhuisheng and me. Do you need more information? Anything else we can do to help fixing this? The bug should be easy to reproduce, as described in the top-level post.

---

### 评论 #9 — kroll-j (2020-10-12T12:58:49Z)

> @jkroll20 Dont know the real effect yet. The BUILD_WITH_TENSILE_HOST is set to false until rocm-3.7.0. So we wont meet the issue before.
> The new and old clients are totally separated source codes, and both of them exsits a long time. Looks like AMD never test new tensile client under gfx803.
> The new tensile client will add Kernel.hsaco and TensileLibrary_gfx803.co into rocBLAS.deb, the images will be imported by tensorflow on runtime. I guess there could be some improvement on new tensile client. But it isnot easy to dig.
> 
> update:
> Testing BUILD_WITH_TENSILE_HOST true/false for text_classicfication.
> BUILD_WITH_TENSILE_HOST=false 3s/15ms per epoch
> BUILD_WITH_TENSILE_HOST=true 3s/16ms per epoch - there is 10% chance to success on my gfx803 with new tensile client.
> Since the last modify of r9nano_x.yaml is 2 years ago. The new client looks like wont make performance improvement on gfx803.

I tried to build rocBLAS in a rocm3.8 container without the tensile host as a workaround, and I couldn't even get it to compile. Following the [build instructions](https://github.com/ROCmSoftwarePlatform/rocBLAS/wiki/1.Build), here is what I did:

```
git clone -b master https://github.com/ROCmSoftwarePlatform/rocBLAS.git
cd rocBLAS
./install.sh -i --no-tensile-host
```

And I got this output:

```
[...]
Generating kernels: Done.
*
Compiling source kernels: Launching 16 threads...
Compiling source kernels: Done.
# Kernel Building elapsed time = 1586.4 secs
# Writing Solutions
[|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||] 100% (18.6 secs elapsed)
# Writing Library Logic
Traceback (most recent call last):
  File "/root/src/rocBLAS/build/release/virtualenv/lib/python3.6/site-packages/Tensile/bin/TensileCreateLibrary", line 38, in <module>
    TensileCreateLibrary()
  File "/root/src/rocBLAS/build/release/virtualenv/lib/python3.6/site-packages/Tensile/TensileCreateLibrary.py", line 1371, in TensileCreateLibrary
    writeLogic(outputPath, logicData, solutionWriter)
  File "/root/src/rocBLAS/build/release/virtualenv/lib/python3.6/site-packages/Tensile/TensileCreateLibrary.py", line 564, in writeLogic
    assert(not problemType["UseInitialStridesCD"])
AssertionError
CMake Error at build/release/virtualenv/lib/python3.6/site-packages/Tensile/Source/TensileCreateLibrary.cmake:115 (message):
  Error generating kernels
Call Stack (most recent call first):
  library/src/CMakeLists.txt:55 (TensileCreateLibraryCmake)


-- Configuring incomplete, errors occurred!
See also "/root/src/rocBLAS/build/release/CMakeFiles/CMakeOutput.log".
+ check_exit_code 1
+ ((  1 != 0  ))
+ exit 1
```

I also tried building the rocm-3.8.0 tag instead of master, to no avail.

@xuhuisheng you seem to have gotten it to build with BUILD_WITH_TENSILE_HOST=false somehow. Could you please describe what you did?

---

### 评论 #10 — xuhuisheng (2020-10-12T17:13:29Z)

@jkroll20 
For ROCm-3.7, just `bash install.sh -i -a gfx803 -r`. `-a gfx803` only including gfx803 architecture, and will speed up compiling, `-r` is --no-tensile-host.
For ROCm-3.8, have to delete gfx803's asm files `rm library/src/blas3/asm_full/r9nano*`, then execute `bash install.sh -i -a gfx803 -r`.
Didn't test on the latest master codes, I will go on testing when there are new versions releasing.
I tested success on ubuntu-20.04.


---

### 评论 #11 — suvrodeep (2020-10-23T01:52:45Z)

Now we have 3 users who can reproduce the issue @jkroll20 @xuhuisheng 

---

### 评论 #12 — xuhuisheng (2020-10-23T02:03:16Z)

@suvrodeep 
My adivse is downgrade to rocm-3.5.1, the repo url is <http://repo.radeon.com/rocm/apt/3.5.1>.
If you had a gfx900(vega 56/64) or gfx906(radeon vii), please have a test and feedback if this is just gfx803's bug.

---

### 评论 #13 — suvrodeep (2020-10-23T02:11:20Z)

Thanks for your input @xuhuisheng. I'll try with ver. 3.5.1. I read @jkroll20 wasn't able to resolve the issue with reinstalling mi-open from 3.5.0 so I was reluctant to give it a try. I will do a fresh install of 3.5.1 however and post my results.

Also I don't have a gfx900 or gfx906 so unfortunately I'll not be able to test on those

---

### 评论 #14 — suvrodeep (2020-10-23T23:49:59Z)

@xuhuisheng  The rocm 3.5.1.package dependency tree seems broken for rocm-dkms and rocm-libs

---

### 评论 #15 — xuhuisheng (2020-10-24T00:14:17Z)

@suvrodeep i had installed 3.5.1 on ubuntu18.04 and ubuntu 20.04. tested successfully with tensorflow-rocm and pytorch.

3.5.1 need 'sudo apt install hipsparse rccl' manually to run tf

remember uninstall current rocm first, as after 3.3 rocm need fresh installation because of multi version bug, i guess.

it does have a ld problem on tensorflow-rocm, need export LD_LIBRARY_PATH=/opt/rocm/lib


---

### 评论 #16 — suvrodeep (2020-10-24T02:56:43Z)

@xuhuisheng Thanks for getting back! I figured my Ubuntu 18.04 installatiion was somehow corrupted so upgraded to 20,04. What I did after adding the repo was this
`sudo apt install rocm-dev rocm-dkms rocm-libs rocm-smi rocm-opencl rocm-utils` but it kept giving me dependency errors.
Guess I need to just install rocm-dkms and then install the other packages one by one manually and then hipsparse rccl.

"3.5.1 need 'sudo apt install hipsparse rccl' manually to run tf" Yes that was an error tf was throwing after I managed to get it installed somewhat the first time.

"it does have a ld problem on tensorflow-rocm, need export LD_LIBRARY_PATH=/opt/rocm/lib" - Thanks for the headsup!

"remember uninstall current rocm first, as after 3.3 rocm need fresh installation because of multi version bug, i guess." - Yes I did purge every rocm package from the system deleted their filed in opt/rocm* and then started over

Btw they have released Rocm 3.9. Do you reckon the issue could be gone in that version ?

---

### 评论 #17 — xuhuisheng (2020-10-24T11:41:39Z)

sudo apt install rocm-dkms is fine. I cannot remember there is package named rocm-opencl, it couldbe the reason.

rocm3.9 isnot published offically, in fact, i am not sure whether 3.9 is a public release or kept as an internal release.

I will check this problem while next release published. But I cannot see any commits on new tensile client on gfx803 .

---

### 评论 #18 — suvrodeep (2020-10-25T02:06:30Z)

I am doing a fresh install of rocm 3.5.1 now on Ubuntu 20.04 as suggested by @xuhuisheng . Exactly followed this:
To add gpg key and repo I did this:
`wget -q -O - http://repo.radeon.com/rocm/apt/3.5.1/rocm.gpg.key | sudo apt-key add -`
`echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/3.5.1/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list`

And then did this:
1. `sudo apt update`
2. `sudo apt install rocm-dkms`
3. `sudo usermod -a -G video $LOGNAME`
4. `sudo usermod -a -G render $LOGNAME`
5. `echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf` (Mentioned in ROCM official installation guide)
    `echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf`
    `echo 'EXTRA_GROUPS=render' | sudo tee -a /etc/adduser.conf` (Required for 20.04)
6. `sudo apt install hipsparse rccl`
7. `export LD_LIBRARY_PATH=/opt/rocm/lib` (as mentioned by @xuhuisheng)

Then restarted the system. It looked like it installed itself correctly judging by the verbose output in the terminal. I did not add the necessary paths to the PATH variable since they were already added, which I verified by `ECHO $PATH` However when I run rocminfo I get this:
`rocminfo: error while loading shared libraries: libhsakmt.so.1: cannot open shared object file: No such file or directory`

`clinfo` also does not work but `rocm-smi` runs fine with syntax error warnings but I guess this is due to the default python version in Ubuntu 20.04 being 3.8.5 instead of 3.6.9 in Ubuntu 18.04

Any ideas how to install the missing shared library ?

![Screenshot from 2020-10-25 02-49-25](https://user-images.githubusercontent.com/27533081/97097237-a5466600-166e-11eb-8baa-7c6d7f9d1f09.png)


---

### 评论 #19 — xuhuisheng (2020-10-25T03:28:01Z)

The location of `libhsakmt.so.1` is `/opt/rocm/lib/libhsakmt.so.1`
Try `sudo ldconfig` refresh ldconfig cache.

And I miss one package named miopen-hip, after `sudo apt install -y rocm-dkms`, we should run `sudo apt install -y hipsparse rccl miopen-hip` then `sudo ldconfig`

And I tested /opt/rocm/bin/rocm-smi, it just show some warnings, if you didnot want to see that warning logs, could `sudo vi /opt/rocm/bin/rocm-smi`, change `is` to `==`

I tested tensorflow-rocm-2.3.1, looks like it neednot `export LD_LIBRARY_PATH=/opt/rocm/lib` anymore, I will recheck it later.

---

### 评论 #20 — suvrodeep (2020-10-25T18:28:12Z)

@xuhuisheng  Thanks for your comment. I did install `miopen-hip` after that.  However its been an ordeal for me to setup rocm 3.5.1. Long story short I did not find any file named `libhsakmt.so.1` anywhere on my system. Turns out its from a package called `hsa-kmt-roct ` which is the ROCT Thunk Interface. I manually cloned the repo from GitHub and generated the .deb packages and copied the contents over to `opt/rocm/lib` and created the necessary symlinks. Now `rocminfo` and `clinfo` worked fine.

I tried `import tensorflow as tf` and `print(tf.__version__)` in the terminal python console and it worked as well. Generally it shows output that the GPU has been initialized and such but it showed no output when importing.

Then I went on to PyCharm to try out my code but threw the same error it was throwing when `hipsparse` was not installed which was weird
`ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory` because it was right there in 

Now curious I installed Jupyter and tried there. import worked fine and my scode worked fine too. Suspicious however if it was using the GPU at all I tried to list the devices and voila! NO PHYSICAL GPU detected. Only CPU, XLA_CPU and XLA_GPU.  Code to list devices was:

`tf.config.experimental.list_physical_devices(device_type=None)`

I have tried reinstalling hipsparse by `sudo apt reinstall hipsrarse` but did not resolve anything. At this point I am not sure what else to try. Any pointers would be highly appreciated.

UPDATE: I was able to reproduce the `ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory` because it was right there in  both in terminal console and Jupyter with `export LB_LIBRARY_PATH=/opt/rocm/lib`. I will now try without it

---

### 评论 #21 — suvrodeep (2020-10-25T18:33:15Z)

Same issue without exporting the LB_LIBRARY_PATH variable. I was able to make it work with LD_LIBRARY PATH instead. maybe it was a typo @xuhuisheng . However now it defaults to CPU and cannot detect the GPU. I uninstalled tensorflow-rocm 2.3.1 and installed 2.2.0 as mentioned here 

[https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md](url)

Pycharm however still cannot find `libhipsparse.so.0` though its right there in`/opt/rocm/lib`
@sunway513  Do you have any suggestions on how to resolve this

---

### 评论 #22 — suvrodeep (2020-10-25T21:26:03Z)

UPDATE: I am now able to run TF 2.3.1 with rocm 3.5.1 with GPU enabled. Turns out I had to install `rocblas rocrand rocfft` as well in addition to `hipsparse rccl miopen-hip`. GREAT SUCCESS! 

Thank you @xuhuisheng for all the help. Much appreciated. I will write a detailed doc to do a clean install of rcom versions 3.5 and above. Not closing this issue since the driver level error for `gfx803` remains with version rocm 3.8

---

### 评论 #23 — xuhuisheng (2020-10-26T02:02:32Z)

@suvrodeep Itis a typo for LD_LIBRARY_PATH, I had corrected. thanks point out.
I find the reason I missed rocm-libs, `sudo apt install -y rocm-libs` that will automate includes rocblas, rocrand, rocfft.

```
|--rocm-dkms
  |--rock-dkms
    \--rock-dkms-firmware
  \--rocm-dev
    |--hsa-rocr-dev
    |--hsa-ext-rocr-dev
    |--rocm-device-libs
    |--llvm-amdgpu
    |--hip-base
    |--hip-doc
    |--hip-rocclr
    |--hip-samples
    |--rocm-gdb
    |--rocm-smi
    |--rocm-smi-lib64
    |--hsakmt-roct
    |--hsakmt-roct-dev
    |--hsa-amd-aqlprofile
    |--comgr
    |--rocm-debug-agent
    |--rocm-cmake
    |--rocprofiler-dev
    |--roctracer-dev
    |--rocm-dbgapi
    \--rocm-utils
      |--rocminfo
      \--rocm-clang-ocl
|--rocm-libs
  |--rocfft
  |--rocrand
  |--rocblas
  |--hipblas
  |--rocsparse
  |--hipsparse
  |--rocalution
  |--rocprim
  |--rocthrust
  |--hipcub
  \--rocsolver
|--miopen-hip
  |--rocm-utils
  |--hip-hcc
  \--rocm-opencl-dev
\--rccl

```

---

### 评论 #24 — suvrodeep (2020-10-31T04:17:10Z)

Much thanks! I just upgraded my hard drive and had to do a fresh install of Ubuntu 20.04. I will try rocm-libs instead of installing them manually

---

### 评论 #25 — ROCmSupport (2020-12-16T10:48:57Z)

Hi @jkroll20,
Is this issue still open?
Recommend to check with the latest ROCm 3.10 and update me the progress.
Thank you.

---

### 评论 #26 — suvrodeep (2020-12-28T02:11:31Z)

This issue is resolved with ROCM ver 3.5.1 and tensorflow-rocm version 2.3.1, Python 3.8 and Ubuntu 20.04. This setup has been working well with gfx803 (Radeon RX580). Have not tested with ROCM 3.10

---

### 评论 #27 — ROCmSupport (2020-12-29T08:44:04Z)

Thanks @suvrodeep for the update.
This issue can be closed now then.

---

### 评论 #28 — boriswinner (2021-01-26T10:46:55Z)

Here is my guide to downgrade to ROCm 3.5.1 + TensorFlow 2.2:
https://github.com/boriswinner/RX580-rocM-tensorflow-ubuntu20.4-guide

---
