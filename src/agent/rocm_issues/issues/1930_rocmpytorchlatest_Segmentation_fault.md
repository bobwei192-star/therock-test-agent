# rocm/pytorch:latest Segmentation fault

> **Issue #1930**
> **状态**: closed
> **创建时间**: 2023-03-12T09:19:12Z
> **更新时间**: 2023-07-04T10:25:51Z
> **关闭时间**: 2023-03-12T22:42:26Z
> **作者**: leagueofsoups
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1930

## 描述

Hi! I have problem with my radeon rx570, can anybody help with debug?

```
uname -a
Linux devel-desktop 5.19.0-35-generic #36~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Feb 17 15:17:25 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.2 LTS"

docker run -it  --security-opt seccomp=unconfined  --network=host  --device=/dev/kfd  --device=/dev/dri  --group-add=video  --ipc=host  --cap-add=SYS_PTRACE  --shm-size 8G  rocm/pytorch:latest bash

python3
import torch
torch.cuda.is_available() == True #True
torch.cuda.device_count() == 1 # True
torch.cuda.current_device() == 0 # True
torch.cuda.get_device_name(torch.cuda.current_device()) == "Radeon RX 570 Series" # True

tensor = torch.randn(2, 2)
res = tensor.to(0)
print(res)
Segmentation fault (core dumped)
```

backtrace
```
Thread 1 "python3" received signal SIGSEGV, Segmentation fault.
0x00007fb4d0e534c5 in ?? () from /opt/rocm/lib/libamdhip64.so.5
(gdb) bt
#0  0x00007fb4d0e534c5 in ?? () from /opt/rocm/lib/libamdhip64.so.5
#1  0x00007fb4d0e5364d in ?? () from /opt/rocm/lib/libamdhip64.so.5
#2  0x00007fb4d0e543f3 in ?? () from /opt/rocm/lib/libamdhip64.so.5
#3  0x00007fb4d0e068dc in ?? () from /opt/rocm/lib/libamdhip64.so.5
#4  0x00007fb4d0fbd25e in ?? () from /opt/rocm/lib/libamdhip64.so.5
#5  0x00007fb4d0f89a76 in ?? () from /opt/rocm/lib/libamdhip64.so.5
#6  0x00007fb4d0f8f947 in hipLaunchKernel () from /opt/rocm/lib/libamdhip64.so.5
#7  0x00007fb4d360b1f4 in void at::native::gpu_kernel_impl<at::native::AbsFunctor<float> >(at::TensorIteratorBase&, at::native::AbsFunctor<float> const&) ()
   from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_hip.so
#8  0x00007fb4d36003d4 in at::native::abs_kernel_cuda(at::TensorIteratorBase&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_hip.so
#9  0x00007fb4fa686125 in at::Tensor& at::native::unary_op_impl_with_complex_to_float_out<at::native::abs_stub>(at::Tensor&, at::Tensor const&, at::native::abs_stub&, bool) [clone .constprop.0] ()
   from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#10 0x00007fb4d2e63cde in at::(anonymous namespace)::(anonymous namespace)::wrapper_out_abs_out(at::Tensor const&, at::Tensor&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_hip.so
#11 0x00007fb4fabed3bc in at::_ops::abs_out::call(at::Tensor const&, at::Tensor&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#12 0x00007fb4fa685fc5 in at::native::abs(at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#13 0x00007fb4fb23e355 in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (at::Tensor const&), &at::(anonymous namespace)::(anonymous namespace)::wrapper__abs>, at::Tensor, c10::guts::typelist::typelist<at::Tensor const&> >, at::Tensor (at::Tensor const&)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&) ()
   from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#14 0x00007fb4fab9a0d3 in at::_ops::abs::redispatch(c10::DispatchKeySet, at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#15 0x00007fb4fc65e2ce in torch::autograd::VariableType::(anonymous namespace)::abs(c10::DispatchKeySet, at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#16 0x00007fb4fc65e9e8 in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (c10::DispatchKeySet, at::Tensor const&), &torch::autograd::VariableType::(anonymous namespace)::abs>, at::Tensor, c10::guts::typelist::typelist<c10::DispatchKeySet, at::Tensor const&> >, at::Tensor (c10::DispatchKeySet, at::Tensor const&)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#17 0x00007fb4fabe58b7 in at::_ops::abs::call(at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#18 0x00007fb4fa60a615 in at::native::isfinite(at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#19 0x00007fb4fb436c65 in c10::impl::wrap_kernel_functor_unboxed_<c10::impl::detail::WrapFunctionIntoFunctor_<c10::CompileTimeFunctionPointer<at::Tensor (at::Tensor const&), &at::(anonymous namespace)::(anonymous namespace)::wrapper__isfinite>, at::Tensor, c10::guts::typelist::typelist<at::Tensor const&> >, at::Tensor (at::Tensor const&)>::call(c10::OperatorKernel*, c10::DispatchKeySet, at::Tensor const&) ()
   from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#20 0x00007fb4fae9d057 in at::_ops::isfinite::call(at::Tensor const&) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_cpu.so
#21 0x00007fb503ad4b6c in torch::autograd::THPVariable_isfinite(_object*, _object*, _object*) () from /opt/conda/lib/python3.8/site-packages/torch/lib/libtorch_python.so
#22 0x000055780196e00e in cfunction_call_varargs (func=0x7fb36c8f0c70, args=<optimized out>, kwargs=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:743
#23 0x000055780196313f in _PyObject_MakeTpCall (callable=0x7fb36c8f0c70, args=<optimized out>, nargs=<optimized out>, keywords=<optimized out>)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:159
#24 0x0000557801a0ddd4 in _PyObject_Vectorcall (kwnames=0x0, nargsf=<optimized out>, args=0x557807aa85d8, callable=0x7fb36c8f0c70)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:125
#25 call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=0x557801cb9710) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4963
#26 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:3469
#27 0x00005578019ff7e7 in PyEval_EvalFrameEx (throwflag=0, f=0x557807aa8400) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:741
#28 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:284
#29 _PyFunction_Vectorcall (func=<optimized out>, stack=<optimized out>, nargsf=<optimized out>, kwnames=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:411
#30 0x00005578019eb698 in _PyObject_FastCallDict (kwargs=0x0, nargsf=<optimized out>, args=0x7ffdda710f70, callable=0x7fb34d77b790) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:96
#31 _PyObject_Call_Prepend (kwargs=0x0, args=0x5578019ff630 <_PyFunction_Vectorcall>, obj=0x0, callable=0x7fb34d77b790) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:888
#32 slot_tp_init (self=self@entry=0x7fb50b6d9e20, args=args@entry=0x7fb50b75d6d0, kwds=kwds@entry=0x0) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/typeobject.c:6790
#33 0x0000557801962fa8 in type_call (kwds=0x0, args=0x7fb50b75d6d0, type=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/typeobject.c:994
#34 _PyObject_MakeTpCall (callable=0x5578062c3db0, args=<optimized out>, nargs=<optimized out>, keywords=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:159
#35 0x0000557801a0d89f in _PyObject_Vectorcall (kwnames=0x0, nargsf=<optimized out>, args=0x7fb34b025780, callable=0x5578062c3db0)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:125
#36 call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=0x557801cb9710) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4963
#37 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:3500
#38 0x00005578019ff7e7 in PyEval_EvalFrameEx (throwflag=0, f=0x7fb34b0255e0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:741
#39 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:284
#40 _PyFunction_Vectorcall (func=<optimized out>, stack=<optimized out>, nargsf=<optimized out>, kwnames=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:411
#41 0x0000557801a090bb in _PyObject_Vectorcall (kwnames=0x0, nargsf=<optimized out>, args=0x557807c3d148, callable=0x7fb34d77ba60)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:127
#42 call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=0x557801cb9710) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4963
#43 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:3500
--Type <RET> for more, q to quit, c to continue without paging--
#44 0x00005578019ff0ff in PyEval_EvalFrameEx (throwflag=0, f=0x557807c3ced0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:741
#45 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7fb34d7d60e8, kwargs=0x7fb34c888b80, kwcount=1, kwstep=1, 
    defs=0x0, defcount=0, kwdefs=0x7fb34d7ffac0, closure=0x0, name=0x7fb34d77acf0, qualname=0x7fb34d77acf0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4298
#46 0x00005578019ffbc4 in _PyFunction_Vectorcall (func=<optimized out>, stack=0x7fb34c888b78, nargsf=<optimized out>, kwnames=<optimized out>)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:436
#47 0x0000557801a09eb0 in _PyObject_Vectorcall (kwnames=0x7fb34d7d60d0, nargsf=<optimized out>, args=<optimized out>, callable=0x7fb34d77bc10)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:127
#48 call_function (kwnames=0x7fb34d7d60d0, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4963
#49 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:3515
#50 0x00005578019ff0ff in PyEval_EvalFrameEx (throwflag=0, f=0x7fb34c8889f0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:741
#51 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x7fb36c5de778, kwargs=0x7fb34ca669c8, kwcount=1, kwstep=1, 
    defs=0x0, defcount=0, kwdefs=0x7fb34d77c140, closure=0x0, name=0x7fb50b49d8f0, qualname=0x7fb50b49d8f0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4298
#52 0x00005578019ffbc4 in _PyFunction_Vectorcall (func=<optimized out>, stack=0x7fb34ca669c0, nargsf=<optimized out>, kwnames=<optimized out>)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:436
#53 0x0000557801a09eb0 in _PyObject_Vectorcall (kwnames=0x7fb36c5de760, nargsf=<optimized out>, args=<optimized out>, callable=0x7fb34d77bca0)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:127
#54 call_function (kwnames=0x7fb36c5de760, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4963
#55 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:3515
#56 0x00005578019ff0ff in PyEval_EvalFrameEx (throwflag=0, f=0x7fb34ca66840) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:741
#57 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x7ffdda711978, kwcount=0, kwstep=1, defs=0x0, 
    defcount=0, kwdefs=0x7fb36c8f5a80, closure=0x0, name=0x7fb50b8a1170, qualname=0x7fb36c7cfcf0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4298
#58 0x00005578019ffbc4 in _PyFunction_Vectorcall (func=<optimized out>, stack=0x7ffdda711970, nargsf=<optimized out>, kwnames=<optimized out>)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/call.c:436
#59 0x000055780196dc92 in _PyObject_Vectorcall (callable=0x7fb36c4c0310, args=<optimized out>, nargsf=<optimized out>, kwnames=0x0)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:127
#60 0x000055780196dcf3 in _PyObject_FastCall () at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:147
#61 call_unbound_noarg (unbound=<optimized out>, func=<optimized out>, self=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/typeobject.c:1465
#62 0x0000557801a54c25 in slot_tp_repr (self=0x7fb34b825db0) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/typeobject.c:6485
#63 0x00005578019f1f62 in object_str (self=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/typeobject.c:3837
#64 0x00005578019814a1 in PyObject_Str (v=0x7fb34b825db0) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/object.c:593
#65 0x00005578019ab13c in PyFile_WriteObject (v=0x7fb34b825db0, f=<optimized out>, flags=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/fileobject.c:131
#66 0x00005578019d86f7 in builtin_print (self=<optimized out>, args=0x7fb34c970d50, nargs=1, kwnames=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/bltinmodule.c:1867
#67 0x000055780196d4e4 in cfunction_vectorcall_FASTCALL_KEYWORDS (func=func@entry=0x7fb50b86ebd0, args=args@entry=0x7fb34c970d50, nargsf=<optimized out>, kwnames=kwnames@entry=0x0)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Objects/methodobject.c:441
#68 0x0000557801a090bb in _PyObject_Vectorcall (kwnames=0x0, nargsf=<optimized out>, args=0x7fb34c970d50, callable=0x7fb50b86ebd0)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Include/cpython/abstract.h:127
#69 call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>, tstate=0x557801cb9710) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4963
#70 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:3500
#71 0x00005578019fe600 in PyEval_EvalFrameEx (throwflag=0, f=0x7fb34c970be0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:741
#72 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, kwnames=0x0, kwargs=0x0, kwcount=0, kwstep=2, defs=0x0, defcount=0, 
    kwdefs=0x0, closure=0x0, name=0x0, qualname=0x0) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4298
#73 0x00005578019ffeb3 in PyEval_EvalCodeEx (closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwcount=0, kws=0x0, argcount=0, args=0x0, locals=<optimized out>, globals=<optimized out>, _co=<optimized out>)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:4327
#74 PyEval_EvalCode (co=<optimized out>, globals=<optimized out>, locals=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/ceval.c:718
#75 0x0000557801a74622 in run_eval_code_obj (co=0x7fb50b819710, globals=0x7fb50b82cf00, locals=0x7fb50b82cf00) at /opt/conda/conda-bld/python-split_1648465063888/work/Python/pythonrun.c:1166
#76 0x0000557801a851d2 in run_mod (mod=<optimized out>, filename=<optimized out>, globals=0x7fb50b82cf00, locals=0x7fb50b82cf00, flags=<optimized out>, arena=<optimized out>)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Python/pythonrun.c:1188
#77 0x0000557801938f48 in PyRun_InteractiveOneObjectEx (fp=fp@entry=0x7fb50bb00980 <_IO_2_1_stdin_>, filename=filename@entry=0x7fb50b6e72f0, flags=flags@entry=0x7ffdda711e48)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Python/pythonrun.c:263
#78 0x00005578019390e8 in PyRun_InteractiveLoopFlags (fp=fp@entry=0x7fb50bb00980 <_IO_2_1_stdin_>, filename_str=filename_str@entry=0x557801af4a7b "<stdin>", flags=flags@entry=0x7ffdda711e48)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Python/pythonrun.c:125
#79 0x0000557801939182 in PyRun_AnyFileExFlags (fp=0x7fb50bb00980 <_IO_2_1_stdin_>, filename=0x557801af4a7b "<stdin>", closeit=0, flags=0x7ffdda711e48)
    at /opt/conda/conda-bld/python-split_1648465063888/work/Python/pythonrun.c:84
#80 0x000055780193945a in pymain_run_stdin (cf=0x7ffdda711e48, config=0x557801cb8a10) at /opt/conda/conda-bld/python-split_1648465063888/work/Modules/main.c:530
#81 pymain_run_python (exitcode=0x7ffdda711e40) at /opt/conda/conda-bld/python-split_1648465063888/work/Modules/main.c:619
#82 Py_RunMain () at /opt/conda/conda-bld/python-split_1648465063888/work/Modules/main.c:695
--Type <RET> for more, q to quit, c to continue without paging--
#83 0x0000557801a88c29 in Py_BytesMain (argc=<optimized out>, argv=<optimized out>) at /opt/conda/conda-bld/python-split_1648465063888/work/Modules/main.c:1127
#84 0x00007fb50b938083 in __libc_start_main (main=0x557801939ea0 <main>, argc=1, argv=0x7ffdda712048, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7ffdda712038)
    at ../csu/libc-start.c:308
#85 0x0000557801a2bad7 in _start ()

```

---

## 评论 (9 条)

### 评论 #1 — leagueofsoups (2023-03-12T22:42:26Z)

Solution:
1. I found my architecture `rocminfo | grep gfx`
2. rebuild pytorch with PYTORCH_ROCM_ARCH
https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.3/page/Frameworks_Installation.html (Option 3: Install PyTorch Using PyTorch ROCm Base Docker Image)
..By default in the rocm/pytorch:latest-base, PyTorch builds for gfx900, gfx906, gfx908, gfx90a, and gfx1030 architectures simultaneously...
For check current arch libtorch_hip.so:
```
TORCHDIR=$( dirname $( python3 -c 'import torch; print(torch.__file__)' ) )
roc-obj-ls -v $TORCHDIR/lib/libtorch_hip.so 
```
3. torch.cuda.is_available() return False, without sudo 
    https://github.com/RadeonOpenCompute/ROCm/issues/1770#issuecomment-1415395501 


---

### 评论 #2 — KylinC (2023-03-16T11:49:31Z)

THX, it works!!!

---

### 评论 #3 — UmutAlihan (2023-04-23T15:04:14Z)

> Solution:
> 
> 1. I found my architecture `rocminfo | grep gfx`
> 2. rebuild pytorch with PYTORCH_ROCM_ARCH
>    https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.3/page/Frameworks_Installation.html (Option 3: Install PyTorch Using PyTorch ROCm Base Docker Image)
>    ..By default in the rocm/pytorch:latest-base, PyTorch builds for gfx900, gfx906, gfx908, gfx90a, and gfx1030 architectures simultaneously...
>    For check current arch libtorch_hip.so:
> 
> ```
> TORCHDIR=$( dirname $( python3 -c 'import torch; print(torch.__file__)' ) )
> roc-obj-ls -v $TORCHDIR/lib/libtorch_hip.so 
> ```
> 
> 3. torch.cuda.is_available() return False, without sudo
>    [[Question] How make GPU device visible for pytorch with ROCm? #1770 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1770#issuecomment-1415395501)



this was exactly what I needed the perfect solution

thank you very much!!

---

### 评论 #4 — fireyan8 (2023-05-25T12:05:00Z)

Hallo,
my GPU is GFX803,
at this step,
7.  Build PyTorch using the following command:

./.jenkins/pytorch/build.sh

no such file error.

What should i do

---

### 评论 #5 — jithunnair-amd (2023-06-12T20:40:50Z)

> Hallo, my GPU is GFX803, at this step, 7. Build PyTorch using the following command:
> 
> ./.jenkins/pytorch/build.sh
> 
> no such file error.
> 
> What should i do

`.jenkins` directory has been moved to `.ci` in latest PyTorch code.

---

### 评论 #6 — fxmarty (2023-06-30T07:23:08Z)

Hi, it would be very helpful if PyTorch rocm would work by default when installing from pip in g4ad AWS EC2 instances (that use v520 => gfx1010) @rocmsupport

Having to install from source on the only available AMD GPU instance on AWS is painful.

---

### 评论 #7 — jithunnair-amd (2023-06-30T07:27:33Z)

> Hi, it would be very helpful if PyTorch rocm would work by default when installing from pip in g4ad AWS EC2 instances (that use v520 => gfx1010) @ROCmSupport
> 
> Having to install from source on the only available AMD GPU instance on AWS is painful.

Hi @fxmarty, does the `HSA_OVERRIDE_GFX_VERSION=10.3.0` solution suggested in https://github.com/RadeonOpenCompute/ROCm/issues/1770#issuecomment-1415395501 not work with pip wheels?

---

### 评论 #8 — fxmarty (2023-06-30T07:36:21Z)

Thank you! Instead of a segmentation fault, now python hangs when accessing GPU memory - while `rocm-smi`'s `GPU%` shows 99% usage. Is the use of `HSA_OVERRIDE_GFX_VERSION` dangerous? Is it similar to pretending to be sm_80 instead of sm_86 for example?).

As in https://bugs.archlinux.org/task/78306, the issue is only when accessing memory.

Let me know if I should open an issue in pytorch or rocm repo for this request. It could also be an issue in my install though.

---

### 评论 #9 — Mr-Ples (2023-07-04T06:56:06Z)

noob question, but do i have to repeat the setup steps above every time i start the docker container? is there no way to persist the steps above?

i guess this docker file would make it persist:

```
    # Use the ROCm PyTorch image as the base
    FROM rocm/pytorch:latest

    # gfx803 support
    RUN cd ~
    RUN git clone https://github.com/pytorch/pytorch.git
    RUN cd pytorch
    RUN git submodule update --init --recursive

    ENV PYTORCH_ROCM_ARCH=gfx803
    RUN ./.ci/pytorch/build.sh

    RUN ..
```

---
