# HIP error: hipErrorNoDevice amdih/pytorch:rocm4.2_ubuntu18.04_py3.6_pytorch_1.9.0 

> **Issue #1666**
> **状态**: closed
> **创建时间**: 2022-02-07T10:38:06Z
> **更新时间**: 2022-02-09T09:24:21Z
> **关闭时间**: 2022-02-09T09:14:43Z
> **作者**: neqkir
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1666

## 描述

Code produces HIP error: hipErrorNoDevice in 

```
#Training
learn.fit_one_cycle(3, lr_max=3e-5, cbs=fit_cbs)
```

while rocminfo confirms there are GPUs (not provided the details for confidentiality reason)

[fine-tuning-bart-text-summarization.txt](https://github.com/RadeonOpenCompute/ROCm/files/8014462/fine-tuning-bart-text-summarization.txt)


---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2022-02-07T12:30:02Z)

Thanks for reaching out.
Can you please share the details of GPU, OS, kernel version and dmesg output.
Thank you.

---

### 评论 #2 — neqkir (2022-02-09T08:10:32Z)

CNDA2 architecture, Ubuntu

Error is the following

```
Exception raised from deviceCount at /var/lib/jenkins/pytorch/aten/src/ATen/hip/impl/HIPGuardImplMasqueradingAsCUDA.h:102 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x68 (0x7f69ad843fc8 in /opt/conda/lib/python3.6/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0x59a09c (0x7f653816d09c in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_hip.so)
frame #2: torch::autograd::Engine::start_device_threads() + 0xa0 (0x7f6575b48740 in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so)
frame #3: <unknown function> + 0xf907 (0x7f69c1df2907 in /lib/x86_64-linux-gnu/libpthread.so.0)
frame #4: torch::autograd::Engine::initialize_device_threads_pool() + 0xdd (0x7f6575b4702d in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so)
frame #5: torch::autograd::Engine::execute_with_graph_task(std::shared_ptr<torch::autograd::GraphTask> const&, std::shared_ptr<torch::autograd::Node>, torch::autograd::InputBuffer&&) + 0x3b (0x7f6575b4b00b in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so)
frame #6: torch::autograd::python::PythonEngine::execute_with_graph_task(std::shared_ptr<torch::autograd::GraphTask> const&, std::shared_ptr<torch::autograd::Node>, torch::autograd::InputBuffer&&) + 0x49 (0x7f6762733d39 in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so)
frame #7: torch::autograd::Engine::execute(std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&, std::vector<at::Tensor, std::allocator<at::Tensor> > const&, bool, bool, bool, std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&) + 0x5b4 (0x7f6575b4d184 in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_cpu.so)
frame #8: torch::autograd::python::PythonEngine::execute(std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&, std::vector<at::Tensor, std::allocator<at::Tensor> > const&, bool, bool, bool, std::vector<torch::autograd::Edge, std::allocator<torch::autograd::Edge> > const&) + 0x6a (0x7f6762733c9a in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so)
frame #9: THPEngine_run_backward(_object*, _object*, _object*) + 0xe2c (0x7f6762734c1c in /opt/conda/lib/python3.6/site-packages/torch/lib/libtorch_python.so)
```
<omitting python frames>


---

### 评论 #3 — ROCmSupport (2022-02-09T09:14:43Z)

Thanks for the update @neqkir 
ROCm supports MI100(CDNA) GPUs only from CDNA family  so far. Please check our supported hardware section for more information: https://github.com/RadeonOpenCompute/ROCm#supported-gpus
As ROCm(4.2/4.x) does not support CDNA2 GPUs, things will break there.

CDNA2 GPUs will be supported very soon officially and I request to wait for some time.
Thank you.

---
