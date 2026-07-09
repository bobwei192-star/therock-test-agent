# Support for Vega 56/64 [ROCm 4.3 / Pytorch]

- **Issue #:** 1572
- **State:** closed
- **Created:** 2021-09-15T01:37:34Z
- **Updated:** 2021-12-13T19:05:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1572

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