# Support for Vega 56/64 [ROCm 4.3 / Pytorch]

> **Issue #1572**
> **状态**: closed
> **创建时间**: 2021-09-15T01:37:34Z
> **更新时间**: 2021-12-13T19:05:50Z
> **关闭时间**: 2021-11-02T02:10:20Z
> **作者**: s-marios
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1572

## 描述

Hi,

So, first things first, are Vega 56 GPUs supported?

I'm running pytorch on an lxc container. With a Radeon VII it works fine. But with a Vega 56 I'm getting the following error:
```
(snip)

MIOpen(HIP): Error [SetIsaName] 'amd_comgr_action_info_set_isa_name(handle, isa.c_str())' amdgcn-amd-amdhsa--gfx900:sramecc-:xnack-: INVALID_ARGUMENT (2)
MIOpen(HIP): Error [BuildOcl] comgr status = INVALID_ARGUMENT (2)
MIOpen(HIP): Warning [BuildOcl] amdgcn-amd-amdhsa--gfx900:sramecc-:xnack-
MIOpen Error: /MIOpen/src/hipoc/hipoc_program.cpp:286: Code object build failed. Source: MIOpenIm2d2Col.cl
Traceback (most recent call last):
  File "train2.py", line 100, in <module>
    train(model, optimizer, train_loader, reps_per_epoch, device)
  File "train2.py", line 60, in train
    loss_dict = model(inputs, targets)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torchvision/models/detection/generalized_rcnn.py", line 93, in forward
    features = self.backbone(images.tensors)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torchvision/models/detection/backbone_utils.py", line 44, in forward
    x = self.body(x)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torchvision/models/_utils.py", line 62, in forward
    x = module(x)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/conv.py", line 443, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/usr/local/lib/python3.8/dist-packages/torch/nn/modules/conv.py", line 439, in _conv_forward
    return F.conv2d(input, weight, bias, self.stride,
RuntimeError: miopenStatusUnknownError
```

I've noticed that rocminfo reports `amdgcn-amd-amdhsa--gfx900:xnack-` wheras the above HIP stuff uses `amdgcn-amd-amdhsa--gfx900:sramecc-:xnack-` i.e. `sramecc` doesn't seem to be supported.

I have access to both a Radeon VII/threadripper 3990 and Vega 56/threadripper 2990wx systems and can provide comparisons between them.

Please advise!

---

## 评论 (33 条)

### 评论 #1 — ROCmSupport (2021-09-15T06:03:25Z)

Thanks @s-marios for reaching out.
I will check this for you and get back with an update soon.
Meanwhile can you please share the exact steps to reproduce the problem.
Thank you.

---

### 评论 #2 — s-marios (2021-09-15T07:57:59Z)

I will report detailed steps tomorrow (work day is over), but the gist is this:

0) Using kernel >=5.13 (currently 5.14)
1) setup an Ubuntu:20.04 lxc container (my setup: lxd/snap/debian)
2) pass in /dev/kfd (as unix-char) and /dev/dri (as gpu)
3) add rocm repositories and install rocm-dev only
4) install pytorch using pip
5) run some pytorch code 

Let me know for which steps you need more details and I'll come back to it tomorrow. Again, do note that the Radeon VII setup works fine.

---

### 评论 #3 — s-marios (2021-09-16T01:09:41Z)

Ok, I'm back with a more detailed writeup and sample code for you.

In [setup.txt](https://github.com/RadeonOpenCompute/ROCm/files/7174165/setup.txt) you'll find all the steps I followed to build a (new) LXC container, with the same error results. This can be used as a guide to build an LXC ROCm container. (Edit: line 25 should read as `lxc config device add ml kfd unix-char source=/dev/kfd` not `type=/dev/kfd`)

Below you'll find a minimal example that triggers the problem (I can't attach .py files directly, so I'm pasting it as-is).

```
import torch
import torchvision

device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
print(f"using device: {device}")
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True).to(device)
model.eval()

rand_input = torch.rand(3, 1920, 1080, device=device)
model([rand_input])
```

Looking forward to your thoughts on this.
Cheers,


---

### 评论 #4 — ROCmSupport (2021-09-16T07:00:34Z)

Thanks @s-marios 
I am able to reproduce the problem with Vega64.
From the logs its pointing to MIOpen and so looks like its MIOpen issue. Let me assign to MIOpen team to take a look.
Thank you.

---

### 评论 #5 — s-marios (2021-09-16T07:49:53Z)

> Thanks @s-marios
> I am able to reproduce the problem with Vega64.
> From the logs its pointing to MIOpen and so looks like its MIOpen issue. Let me assign to MIOpen team to take a look.
> Thank you.

Right on! Hoping for a quick resolution, possibly in a point release. Please don't make me wait until ROCm 4.5, pretty please? 

Cheers!

---

### 评论 #6 — ROCmSupport (2021-09-23T09:49:47Z)

Hi @s-marios 
I am not sure about the availability of fix right now, developer is working on it.
Once I hear from him, I will update you.
Thank you.


---

### 评论 #7 — Sigura (2021-10-03T22:12:49Z)

> From the logs its pointing to MIOpen and so looks like its MIOpen issue. Let me assign to MIOpen team to take a look.

Hi @ROCmSupport 

I got the same issue on Vega64, trying to rebuild MIOpen from the source without any result. ~~Could you please share the MIOpen issue number?~~ ROCmSoftwarePlatform/MIOpen#1204

but! those lines work for me

```
import torch
import torchvision

device = torch.device('cuda')
print(f"using device: {device}")
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True).to(device)
model.eval()

rand_input = torch.rand(3, 1920, 1080, device=device)
model([rand_input])

```

---

### 评论 #8 — ffleader1 (2021-10-10T19:20:43Z)

HI
I just want to report that I came across this exact problem.
```
MIOpen(HIP): Warning [SQLiteBase] Unable to read system database file:gfx900_56.kdb Performance may degrade
MIOpen(HIP): Error [SetIsaName] 'amd_comgr_action_info_set_isa_name(handle, isa.c_str())' amdgcn-amd-amdhsa--gfx900:sramecc-:xnack-: INVALID_ARGUMENT (2)
MIOpen(HIP): Error [BuildOcl] comgr status = INVALID_ARGUMENT (2)
MIOpen(HIP): Warning [BuildOcl] amdgcn-amd-amdhsa--gfx900:sramecc-:xnack-
MIOpen Error: /MIOpen/src/hipoc/hipoc_program.cpp:286: Code object build failed. Source: MIOpenIm2d2Col.cl
  0%|          | 0/1000000 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/src/train.py", line 51, in <module>
    main_worker(0, 1, args)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/src/train.py", line 31, in main_worker
    trainer.train()
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/src/trainer/trainer.py", line 108, in train
    pred_img = self.netG(images_masked, masks)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/venv/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/src/model/aotgan.py", line 37, in forward
    x = self.encoder(x)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/venv/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/venv/lib/python3.8/site-packages/torch/nn/modules/container.py", line 139, in forward
    input = module(input)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/venv/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1051, in _call_impl
    return forward_call(*input, **kwargs)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/venv/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 443, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/ffleader1/PycharmProjects/AOT-GAN-for-Inpainting/venv/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 439, in _conv_forward
    return F.conv2d(input, weight, bias, self.stride,
RuntimeError: miopenStatusUnknownError

Process finished with exit code 1
```
That was I error log.

---

### 评论 #9 — Bengt (2021-10-12T22:38:28Z)

Seems like I hit a similar issue here: https://github.com/ryujaehun/pytorch-gpu-benchmark/issues/19

---

### 评论 #10 — Bengt (2021-10-12T22:47:59Z)

So, 4.3 breaks GFX900:

> kernel module from 4.3, which known to have issues with gfx900

Source: <https://github.com/ROCmSoftwarePlatform/MIOpen/issues/1204#issuecomment-940473879>

A downgrade to 4.2 is cumbersome, because AMD depublishes former versions of their packages:

<http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-dkms/>

A fix in MIOpen is in the works, but the urgency is considered to be low:

https://github.com/ROCmSoftwarePlatform/MIOpen/issues/1204

---

### 评论 #11 — xuhuisheng (2021-10-12T23:03:57Z)

Although we cannot download/upgrade ROCm, we could uninstall ROCm and install a lower version by specify the url.
likes <http://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-dkms/>

---

### 评论 #12 — Bengt (2021-10-12T23:34:23Z)

@xuhuisheng Thanks for the hint. I am attempting a downgrade like so:

```bash
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.2/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils && sudo reboot
sudo apt update
sudo apt install --yes rocm-dkms && sudo reboot
```

---

### 评论 #13 — ffleader1 (2021-10-13T02:30:39Z)

I ran into problem at 4.2 though.

On Wed, Oct 13, 2021, 6:34 AM Bengt Lüers ***@***.***> wrote:

> @xuhuisheng <https://github.com/xuhuisheng> Thanks for the hint. I am
> attempting a downgrade like so:
>
> mkdir rocm-debscd rocm-debs
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/h/hip-doc/hip-doc_4.2.21155.5900.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/h/hip-samples/hip-samples_4.2.21155.5900.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/h/hsa-amd-aqlprofile/hsa-amd-aqlprofile_1.0.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/o/openmp-extras/openmp-extras_12.42.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-cmake/rocm-cmake_0.4.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-dbgapi/rocm-dbgapi_0.46.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-debug-agent/rocm-debug-agent_2.0.1.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-device-libs/rocm-device-libs_1.0.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-gdb/rocm-gdb_10.1.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-smi-lib/rocm-smi-lib_2.8.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocm-utils/rocm-utils_4.2.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/h/hsakmt-roct-dev/hsakmt-roct-dev_20210315.0.7.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/rocprofiler-dev/rocprofiler-dev_1.0.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/r/roctracer-dev/roctracer-dev_1.0.0.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/h/hip-base/hip-base_4.2.21155.5900.40200-21_amd64.deb
> wget https://repo.radeon.com/rocm/apt/4.2/pool/main/h/hsakmt-roct/hsakmt-roct_20210315.0.7.40200-21_amd64.deb
> sudo apt install --yes --allow-downgrades ./*.debcd ..
> rm -rf ./rocm-debs/
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1572#issuecomment-941744128>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ADSSGEFU46MAMPDS4C46JBLUGTAYVANCNFSM5EBLCSNA>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
>


---

### 评论 #14 — Bengt (2021-10-13T12:19:31Z)

Yes, me too. Using 4.2 is possible, but it seems to not fix the issue.

---

### 评论 #15 — ThisKwasior (2021-10-13T17:14:03Z)

I am Vega 64 user. I have this issue for about 4 months now.
I use manjaro and back in march it did work properly, I could train tacotron2 models.
When I first saw this issue and one at MIOpen, I got curious and installed Lubuntu 18.04.05.
After tinkering around and downgrading a lot (ROCm 4.0.1/PyTorch 1.8.0 rocm4.0.1/tensorflow-rocm 1.15.9) I was able to inference and train models, which include [tacotron2](https://github.com/NVIDIA/tacotron2) and [vocal-remover](https://github.com/tsurumeso/vocal-remover).

---

### 评论 #16 — Bengt (2021-10-13T17:26:44Z)

Hello, @ThisKwasior! Thanks for your report. I only started using PyTorch on ROCm, so I wouldn't have known about this issue being that old. The issue being several ROCm versions old also explains why downgrading one version did not solve it for @ffleader1 and me.

---

### 评论 #17 — jeffdaily (2021-10-26T21:01:04Z)

Would someone like to try the latest nightly rocm 4.3.1 wheel to see if the issue is resolved?

```
pip3 install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html
```

---

### 评论 #18 — Bengt (2021-10-26T23:11:27Z)

Hi, @jeffdaily! Thanks for prompting me to test the latest nightly. I installed it into my runtime virtual environment using this command:

```
.tox/py38/bin/python -m pip install --upgrade --pre torch torchvision -f https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html
```

That took a little while to download and install because the package is 1.5 GB in size, but it worked fine. I had to adapt my code somewhat to convert data coming from the GPU back to CPU data, as is usual with torch. That fixed a lot of problems for me, but I still run into additional issues, which I am not sure if it is related to the topic of this issue. Deactivating one failing test after the other, I found multiple similar errors like so:

```
Fatal Python error: Aborted

Thread 0x00007fcb243ff700 (most recent call first):
<no Python frame>

Thread 0x00007fcec2a94740 (most recent call first):
  File "/home/bengt/Downloads/DFKI/gitlab.ni.dfki.de/VR/VR.Backend/.tox/py38/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 443 in _conv_forward
  File "/home/bengt/Downloads/DFKI/gitlab.ni.dfki.de/VR/VR.Backend/.tox/py38/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 447 in forward
  [My code here]
  File "/snap/pycharm-professional/260/plugins/python/helpers/pycharm/_jb_pytest_runner.py", line 51 in <module>

Process finished with exit code 134 (interrupted by signal 6: SIGABRT)
```

For full stack traces see: <https://gist.github.com/Bengt/2ab1196267ffa6b42a358ea29569eed2>

---

### 评论 #19 — s-marios (2021-10-27T02:47:41Z)

@jeffdaily I installed the latest wheel with:
`pip3 install --upgrade --pre torch torchvision -f https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html` (the `--upgrade` was necessary).

These are the results:
```
root@ml:~# python3 pytorch_sample.py 
using device: cuda
MIOpen(HIP): Warning [SQLiteBase] Unable to read system database file:gfx900_64.kdb Performance may degrade
MIOpen(HIP): Error [Do] 'amd_comgr_do_action(kind, handle, in.GetHandle(), out.GetHandle())' AMD_COMGR_ACTION_COMPILE_SOURCE_TO_BC: ERROR (1)
MIOpen(HIP): Error [BuildHip] comgr status = ERROR (1)
MIOpen(HIP): Warning [BuildHip] /tmp/comgr-afeb6b/input/naive_conv.cpp:26:10: fatal error: 'hip/hip_fp16.h' file not found
#include <hip/hip_fp16.h>
         ^~~~~~~~~~~~~~~~
1 error generated when compiling for gfx900.

terminate called after throwing an instance of 'miopen::Exception'
  what():  /MIOpen/src/hipoc/hipoc_program.cpp:295: Code object build failed. Source: naive_conv.cpp
Aborted
```
This is the same thing @ThisKwasior  reports here https://github.com/ROCmSoftwarePlatform/MIOpen/issues/1204#issuecomment-946978785 . AFAI can tell, the original issue is "solved", but now we're hitting a new roadblock. 

Is there an issue that tracks the `#include <hip/hip_fp16.h>` error? Feel free to mention it below.


---

### 评论 #20 — jeffdaily (2021-10-27T16:43:59Z)

I may have prematurely asked you to test the nightly wheel.  Wheels are built using a special manylinux docker image and the fix was to build a patched MIOpen for the image.  Our PR was merged, but we did not notice that the new image failed to build.  We're working through those issues now.  Once the image is built correctly and pushed, the nightly wheels will start using it for their build.  I'll keep you posed.

---

### 评论 #21 — jeffdaily (2021-11-01T16:42:54Z)

FYI nightly wheel was updated since I last commented.  Should resolve the miopen issue.  Let us know otherwise.

---

### 评论 #22 — Bengt (2021-11-01T22:54:40Z)

@jeffdaily Thanks for the update. I upgraded the `torch` and `torchvision` packages, like so:

```
.tox/py38/bin/python -m pip uninstall --yes torch torchvision
.tox/py38/bin/python -m pip install torch torchvision -f https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html
```

I have a test that checks for GPU acceleration in torch, like so:

```Python
import socket
from typing import Tuple

from torch import cuda as cuda_or_rocm  # ROCm identifies as CUDA, too.


def test_cuda_rocm_availability():
    # Mock
    hostnames_with_gpus: Tuple[str] = tuple([
        'bengt-desktop',
        'dgx-ol-1',
    ])
    hostname: str = socket.gethostname()
    expected_availability = hostname in hostnames_with_gpus

    # Test
    actual_availability: bool = cuda_or_rocm.is_available()

    # This might fail on weird machines in the future.
    # So print quite verbosely for debugging purposes.
    print(f'[DEBUG] Hostname: {hostname}')
    print(f'[DEBUG] Hostnames with GPUs: {hostnames_with_gpus}')
    print(f'[DEBUG] Hostname in hostnames with GPUs: {expected_availability}')
    print(f'[DEBUG] CUDA availability: {actual_availability}')

    # Assert
    assert actual_availability or \
        actual_availability == expected_availability
```

This test now fails, like so:

```
FAILED            [100%][DEBUG] Hostname: bengt-desktop
[DEBUG] Hostnames with GPUs: ('bengt-desktop', 'dgx-ol-1')
[DEBUG] Hostname in hostnames with GPUs: True
[DEBUG] CUDA availability: False

pytorch/test_cuda_rocm.py:6 (test_cuda_rocm_availability)
(False or False != True)

Expected :True)
Actual   :(False or False
<Click to see difference>

def test_cuda_rocm_availability():
        # Mock
        hostnames_with_gpus: Tuple[str] = tuple([
            'bengt-desktop',
        ])
        hostname: str = socket.gethostname()
        expected_availability = hostname in hostnames_with_gpus
    
        # Test
        actual_availability: bool = cuda_or_rocm.is_available()
    
        # This might fail on weird machines in the future.
        # So print quite verbosely for debugging purposes.
        print(f'[DEBUG] Hostname: {hostname}')
        print(f'[DEBUG] Hostnames with GPUs: {hostnames_with_gpus}')
        print(f'[DEBUG] Hostname in hostnames with GPUs: {expected_availability}')
        print(f'[DEBUG] CUDA availability: {actual_availability}')
    
        # Assert
>       assert actual_availability or \
            actual_availability == expected_availability
E       assert (False or False == True)

pytorch/test_cuda_rocm.py:27: AssertionError
```

I also recreated the virtual environment from scratch using tox, but that did not help.

This is on Ubuntu 20.04.1, ROCm 4.5.0 and a Vega 64.

---

### 评论 #23 — jeffdaily (2021-11-01T23:01:07Z)

> ```
> .tox/py38/bin/python -m pip install torch torchvision -f https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html
> ```

Did you miss the `--pre` option?  It is needed for nightly wheels or you don't get the prerelease version.

---

### 评论 #24 — Bengt (2021-11-01T23:04:05Z)

Yes, I did forget the `--pre` option. I am trying this now:

```
.tox/py38/bin/python -m pip uninstall --yes torch torchvision
.tox/py38/bin/python -m pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html
```

Installation worked and the test which checks for GPU acceleration now also works. Running my whole test suite worked.

This means this package is all good for me. Wow, this was quite a journey. Thanks a lot for making this work!

---

### 评论 #25 — Bengt (2021-11-01T23:40:36Z)

When can we expect the non-preview / stable package versions of `torch` and `torchvision` to work with the latest ROCm stack? A stable version should only require a minimal download and I would expected it on [the getting started page of pytorch.org](https://pytorch.org/get-started/locally/).

---

### 评论 #26 — jeffdaily (2021-11-01T23:59:14Z)

Admittedly, our pytorch wheel availability is deficient.  We missed the cutoff for pytorch 1.10 branching before we got rocm 4.3.1 wheel support added.  During the pytorch 1.10 release process, we released rocm 4.5.  So now the getting started page remains at 4.2, confusingly, even though we are now up to rocm 4.5.  We plan a patch release of rocm 4.5.1 that should be out prior to the next pytorch branching (1.11), but we don't expect a new pytorch until Q1'22.  

A stable version would be a similar size compared to the nightly wheels.

---

### 评论 #27 — s-marios (2021-11-02T02:10:10Z)

Updated to the new nightly wheel using `--pre`, and the sample code finishes without problems! Closing this ticket as fixed.

@jeffdaily just a clarification, are these fixes present in ROCm 4.5?

---

### 评论 #28 — Bengt (2021-11-02T10:59:23Z)

@jeffdaily I understand that releasing with that many dependencies is difficult. What are the next steps under these circumstances? Should the nightly builds of `torch` and `torchvision` move to building against ROCm 4.5.0 instead of ROCm 4.3.1?

I managed to speed up building my code in continuous integration by caching the environment into which the ROCm versions of PyTorch and TorchVision get installed. This may not work for anyone, though. Is there a way to provide smaller packages, which are thus quicker to install for everybody?

By the way, here is the configuration snippet for overwriting the install command in `tox.ini` configuration:

```ini
[testenv]
# Ugly workaround for ROCm not having a PyPI package
install_command =
    pip install \
    --upgrade \
    --pre \
    --find-links https://download.pytorch.org/whl/nightly/rocm4.3.1/torch_nightly.html \
    {opts} {packages}
```

---

### 评论 #29 — jeffdaily (2021-11-02T15:16:29Z)

> just a clarification, are these fixes present in ROCm 4.5?

@s-marios We expect these fixes to be part of ROCm 4.5.1, not 4.5.0. 

> I understand that releasing with that many dependencies is difficult. What are the next steps under these circumstances? Should the nightly builds of torch and torchvision move to building against ROCm 4.5.0 instead of ROCm 4.3.1?

@Bengt we are skipping 4.5 in favor of 4.5.1 when we upgrade the nightly builds of torch and torchvision.  ETA mid December.  Our release cadence is approximately every other month, with patch releases as-needed.  Upgrading CI, wheels, etc. is not trivial, and combined with the aggressive release schedule we try to minimize the churn.  

Concerning the size of the rocm pytorch wheels, we are following the precedent established by the cuda pytorch wheels where the toolkit libraries are bundled into the wheel.  That means if you have rocm 4.5.0 installed on your host and you pip install the rocm 4.3.1 wheel, you get rocm 4.3.1 libs inside the wheel.  We strive to maintain "N-2" backwards compatibility with the rocm kernel driver, so this use case is expected.

---

### 评论 #30 — ROCmSupport (2021-12-13T15:24:26Z)

Good news. I verified and this issue is fixed and no more observed with 4.5.2.
Thank you.

---

### 评论 #31 — Bengt (2021-12-13T15:41:11Z)

@ROCmSupport, that is great to hear. Thanks for supporting our GPUs with an official version again!

There is a tag, but no release, yet for 4.5.2:

https://github.com/RadeonOpenCompute/ROCm/tags

https://github.com/RadeonOpenCompute/ROCm/releases

---

### 评论 #32 — zhang2amd (2021-12-13T18:59:26Z)

ROCm releases are labeled as tags. We may add "Releases" but that's optional. There is no real difference between Tag and Release on github. This ROCm repository does not have binaries. The release notes and all docs are updated on the tags. And there is no good way to automate adding "Release". Please just look for Tags as they are labeled for each releases. We may manually add "Releases" based on the tags or do it later or skip it. Just to answer this question, we added 4.5.2 Release.

---

### 评论 #33 — Bengt (2021-12-13T19:05:50Z)

@zhang2amd cool! Thanks for adding the release. I feel better with that one in place. This makes it clear that 4.5 is no longer the most recent version. So hopefully some more people using Vega 64 cards can avoid this faulty version.

---
