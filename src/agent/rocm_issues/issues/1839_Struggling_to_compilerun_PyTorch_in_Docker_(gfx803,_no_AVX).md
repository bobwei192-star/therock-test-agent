# Struggling to compile/run PyTorch in Docker (gfx803, no AVX)

> **Issue #1839**
> **状态**: closed
> **创建时间**: 2022-10-14T12:11:21Z
> **更新时间**: 2024-05-09T16:30:43Z
> **关闭时间**: 2024-05-09T16:30:43Z
> **作者**: AN3223
> **标签**: application:pytorch
> **URL**: https://github.com/ROCm/ROCm/issues/1839

## 标签

- **application:pytorch** (颜色: #bfdadc)

## 描述

Hi!

I'm trying to compile PyTorch from source within the `rocm/pytorch:latest-base` Docker image by following the instructions in the docs ([here](https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.3/page/Frameworks_Installation.html) under option 3).

I run `env PYTORCH_ROCM_ARCH=gfx803 ./.jenkins/pytorch/build.sh` and eventually I end up with this error:

```
[ 92%] Linking CXX executable ../bin/MaybeOwned_test
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
collect2: error: ld returned 1 exit status
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
collect2: error: ld returned 1 exit status
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
```

Trying to work around the tests being unable to link, I run `env PYTORCH_ROCM_ARCH=gfx803 ATEN_NO_TEST=1 BUILD_TEST=0 ./.jenkins/pytorch/build.sh`:

```
[ 97%] Linking CXX executable ../../../../bin/torch_shm_manager
[100%] Built target torch_python
Consolidate compiler generated dependencies of target functorch
Consolidate compiler generated dependencies of target nnapi_backend
[100%] Built target nnapi_backend
[100%] Built target functorch
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm-5.3.0/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
collect2: error: ld returned 1 exit status
make[2]: *** [caffe2/torch/lib/libshm/CMakeFiles/torch_shm_manager.dir/build.make:118: bin/torch_shm_manager] Error 1
make[1]: *** [CMakeFiles/Makefile2:6477: caffe2/torch/lib/libshm/CMakeFiles/torch_shm_manager.dir/all] Error 2
make: *** [Makefile:146: all] Error 2
```
libtinfo is installed:

```
jenkins@desktop:/sd/pytorch$ apt search libtinfo
Sorting... Done
Full Text Search... Done
libtinfo5/now 6.2-0ubuntu2 amd64 [installed,local]
  shared low-level terminfo library (legacy version)

libtinfo6/now 6.2-0ubuntu2 amd64 [installed,local]
  shared low-level terminfo library for terminal handling

jenkins@desktop:/sd/pytorch$ ldd /opt/rocm-5.3.0/lib/libamd_comgr.so.2
	linux-vdso.so.1 (0x00007fffdbbd8000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fb06bd89000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fb06bd83000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fb06bd60000)
	libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6 (0x00007fb06bd30000)
	libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fb06bb4e000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fb06b9fd000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fb06b9e2000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb06b7f0000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fb0742b6000)
jenkins@desktop:/sd/pytorch$ ls -l /lib/x86_64-linux-gnu/libtinfo.so.6
lrwxrwxrwx 1 root root 15 Feb 26  2020 /lib/x86_64-linux-gnu/libtinfo.so.6 -> libtinfo.so.6.2
jenkins@desktop:/sd/pytorch$ ls -l /lib/x86_64-linux-gnu/libtinfo.so.6.2
-rw-r--r-- 1 root root 192032 Feb 26  2020 /lib/x86_64-linux-gnu/libtinfo.so.6.2
```

---

## 评论 (7 条)

### 评论 #1 — AN3223 (2022-10-16T13:51:08Z)

Progress report: I can successfully _compile_ PyTorch using the older `rocm/pytorch:rocm5.2_ubuntu20.04_py3.7_pytorch_1.11.0_base` image. So it seems like something may be wrong with the most recent `latest-base` image.

Actually _running_ PyTorch is more difficult. I'm receiving a SIGILL in `librocblas` when I try to compile torchvision (SIGILLs during `import torch`):

```
(gdb) run
Starting program: /opt/conda/bin/python setup.py install
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[Detaching after fork from child process 9591]

Program received signal SIGILL, Illegal instruction.
0x00007fffc45d92d0 in __cxx_global_var_init.1 () from /opt/rocm-5.2.0/lib/librocblas.so.0
(gdb) bt
#0  0x00007fffc45d92d0 in __cxx_global_var_init.1 () from /opt/rocm-5.2.0/lib/librocblas.so.0
```

<details>

<summary>More backtrace...</summary>

```
#1  0x00007ffff7fe0b9a in call_init (l=<optimized out>, argc=argc@entry=3, argv=argv@entry=0x7fffffffe578, env=env@entry=0x7fffffffe598) at dl-init.c:72
#2  0x00007ffff7fe0ca1 in call_init (env=0x7fffffffe598, argv=0x7fffffffe578, argc=3, l=<optimized out>) at dl-init.c:30
#3  _dl_init (main_map=0x555555d754d0, argc=3, argv=0x7fffffffe578, env=0x7fffffffe598) at dl-init.c:119
#4  0x00007ffff7da5985 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:182
#5  0x00007ffff7fe50cf in dl_open_worker (a=a@entry=0x7fffffffbcf0) at dl-open.c:758
#6  0x00007ffff7da5928 in __GI__dl_catch_exception (exception=<optimized out>, operate=<optimized out>, args=<optimized out>) at dl-error-skeleton.c:208
#7  0x00007ffff7fe460a in _dl_open (file=0x7ffff68e6ad0 "/opt/conda/lib/python3.7/site-packages/torch/_C.cpython-37m-x86_64-linux-gnu.so", mode=-2147483646, 
    caller_dlopen=<optimized out>, nsid=-2, argc=3, argv=0x7fffffffe578, env=0x7fffffffe598) at dl-open.c:837
#8  0x00007ffff7faf34c in dlopen_doit (a=a@entry=0x7fffffffbf10) at dlopen.c:66
#9  0x00007ffff7da5928 in __GI__dl_catch_exception (exception=exception@entry=0x7fffffffbeb0, operate=<optimized out>, args=<optimized out>)
    at dl-error-skeleton.c:208
#10 0x00007ffff7da59f3 in __GI__dl_catch_error (objname=0x555555957ae0, errstring=0x555555957ae8, mallocedp=0x555555957ad8, operate=<optimized out>, 
    args=<optimized out>) at dl-error-skeleton.c:227
#11 0x00007ffff7fafb59 in _dlerror_run (operate=operate@entry=0x7ffff7faf2f0 <dlopen_doit>, args=args@entry=0x7fffffffbf10) at dlerror.c:170
#12 0x00007ffff7faf3da in __dlopen (file=<optimized out>, mode=<optimized out>) at dlopen.c:87
#13 0x000055555575924c in _PyImport_FindSharedFuncptr (prefix=0x55555578e408 "PyInit", shortname=0x7ffff6909590 "_C", 
    pathname=0x7ffff68e6ad0 "/opt/conda/lib/python3.7/site-packages/torch/_C.cpython-37m-x86_64-linux-gnu.so", fp=0x0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/dynload_shlib.c:96
#14 0x000055555577f0c8 in _PyImport_LoadDynamicModuleWithSpec (spec=0x7ffff685c950, fp=0x0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/importdl.c:129
#15 0x000055555577f313 in _imp_create_dynamic_impl.isra.15 (file=0x0, spec=0x7ffff685c950)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/import.c:2174
#16 _imp_create_dynamic (module=<optimized out>, args=<optimized out>, nargs=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/clinic/import.c.h:289
#17 0x000055555569d452 in _PyMethodDef_RawFastCallDict (method=0x555555885040 <imp_methods+320>, self=0x7ffff7a35cb0, args=0x7ffff685c8e8, nargs=1, 
    kwargs=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:530
#18 0x000055555571c4e1 in _PyCFunction_FastCallDict (kwargs=0x7ffff685d230, nargs=<optimized out>, args=0x7ffff685c8e8, func=0x7ffff7a4e7d0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:585
#19 PyCFunction_Call (kwargs=0x7ffff685d230, args=0x7ffff685c8d0, func=0x7ffff7a4e7d0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:789
#20 do_call_core (kwdict=0x7ffff685d230, callargs=0x7ffff685c8d0, func=0x7ffff7a4e7d0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4641
#21 _PyEval_EvalFrameDefault (f=0x7ffff6e56210, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3191
#22 0x000055555566ce85 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff6e56210) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#23 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, 
    kwnames=0x0, kwargs=0x7ffff7906ea0, kwcount=0, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x7ffff7a3b300, qualname=0x7ffff7a3b300)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3930
#24 0x000055555568ccd3 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff7906e90, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:433
#25 0x00005555556d39c5 in call_function (pp_stack=0x7fffffffc6c8, oparg=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#26 0x000055555571b702 in _PyEval_EvalFrameDefault (f=0x7ffff7906d00, throwflag=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3093
#27 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff7906d00) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#28 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#29 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff6e56710, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#30 0x00005555556d39c5 in call_function (pp_stack=0x7fffffffc8b8, oparg=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#31 0x0000555555717601 in _PyEval_EvalFrameDefault (f=0x7ffff6e56590, throwflag=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3110
#32 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff6e56590) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#33 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#34 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff795eb80, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#35 0x0000555555717395 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#36 _PyEval_EvalFrameDefault (f=0x7ffff795ea00, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3124
#37 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff795ea00) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#38 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#39 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x55555594bd10, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#40 0x0000555555717395 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#41 _PyEval_EvalFrameDefault (f=0x55555594bb60, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3124
#42 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x55555594bb60) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#43 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#44 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff6a3abe8, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#45 0x0000555555717395 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#46 _PyEval_EvalFrameDefault (f=0x7ffff6a3aa50, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3124
#47 0x000055555566e436 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff6a3aa50) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#48 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#49 _PyFunction_FastCallDict (kwargs=0x0, nargs=<optimized out>, args=<optimized out>, func=0x7ffff7a4fa70)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:322
#50 _PyObject_FastCallDict (callable=0x7ffff7a4fa70, args=<optimized out>, nargs=<optimized out>, kwargs=0x0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:98
#51 0x000055555566f43d in object_vacall (callable=0x7ffff7a4fa70, vargs=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:1200
#52 0x0000555555697253 in _PyObject_CallMethodIdObjArgs (obj=<optimized out>, name=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:1250
#53 0x0000555555668039 in import_find_and_load (abs_name=0x7ffff68ddcb0) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/import.c:1652
#54 PyImport_ImportModuleLevelObject (name=0x7ffff68ddcb0, globals=<optimized out>, locals=<optimized out>, fromlist=0x7ffff6d27310, level=0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/import.c:1764
#55 0x000055555571a0e2 in import_name (level=0x5555558b83a0 <small_ints+160>, fromlist=0x7ffff6d27310, name=0x7ffff68ddcb0, f=0x555555d5aac0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4770
#56 _PyEval_EvalFrameDefault (f=0x555555d5aac0, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:2600
#57 0x000055555566ce85 in PyEval_EvalFrameEx (throwflag=0, f=0x555555d5aac0) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#58 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, 
    kwnames=0x0, kwargs=0x0, kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x0, qualname=0x0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3930
#59 0x000055555572bbc0 in PyEval_EvalCodeEx (closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwcount=0, kws=0x0, argcount=0, args=0x0, locals=0x7ffff699ec80, 
    globals=0x7ffff699ec80, _co=0x7ffff68dac00) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3959
#60 PyEval_EvalCode (locals=0x7ffff699ec80, globals=0x7ffff699ec80, co=0x7ffff68dac00)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:524
#61 builtin_exec_impl.isra.12 (locals=0x7ffff699ec80, globals=0x7ffff699ec80, source=0x7ffff68dac00)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/bltinmodule.c:1079
#62 builtin_exec (module=<optimized out>, args=<optimized out>, nargs=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/clinic/bltinmodule.c.h:283
#63 0x000055555569d452 in _PyMethodDef_RawFastCallDict (method=0x555555885b20 <builtin_methods+480>, self=0x7ffff7a95d10, args=0x7ffff68dce28, nargs=2, 
    kwargs=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:530
#64 0x000055555571c4e1 in _PyCFunction_FastCallDict (kwargs=0x7ffff694b640, nargs=<optimized out>, args=0x7ffff68dce28, func=0x7ffff7a9ce10)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:585
#65 PyCFunction_Call (kwargs=0x7ffff694b640, args=0x7ffff68dce10, func=0x7ffff7a9ce10)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:789
#66 do_call_core (kwdict=0x7ffff694b640, callargs=0x7ffff68dce10, func=0x7ffff7a9ce10)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4641
#67 _PyEval_EvalFrameDefault (f=0x555555ab45a0, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3191
#68 0x000055555566ce85 in PyEval_EvalFrameEx (throwflag=0, f=0x555555ab45a0) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#69 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, 
    kwnames=0x0, kwargs=0x7ffff69f4b08, kwcount=0, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x7ffff7a3b300, qualname=0x7ffff7a3b300)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3930
#70 0x000055555568ccd3 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff69f4af0, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:433
#71 0x00005555556d39c5 in call_function (pp_stack=0x7fffffffd768, oparg=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#72 0x000055555571b702 in _PyEval_EvalFrameDefault (f=0x7ffff69f4960, throwflag=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3093
#73 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff69f4960) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#74 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#75 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff6a23b88, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#76 0x00005555556d39c5 in call_function (pp_stack=0x7fffffffd958, oparg=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#77 0x0000555555717601 in _PyEval_EvalFrameDefault (f=0x7ffff6a23a00, throwflag=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3110
#78 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff6a23a00) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#79 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#80 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x555555bd1970, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#81 0x0000555555717395 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#82 _PyEval_EvalFrameDefault (f=0x555555bd17c0, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3124
#83 0x000055555568c8d7 in PyEval_EvalFrameEx (throwflag=0, f=0x555555bd17c0) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#84 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#85 _PyFunction_FastCallKeywords (func=<optimized out>, stack=0x7ffff6a3ade8, nargs=<optimized out>, kwnames=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:408
#86 0x0000555555717395 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4616
#87 _PyEval_EvalFrameDefault (f=0x7ffff6a3ac50, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3124
#88 0x000055555566e436 in PyEval_EvalFrameEx (throwflag=0, f=0x7ffff6a3ac50) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#89 function_code_fastcall (globals=<optimized out>, nargs=<optimized out>, args=<optimized out>, co=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:283
#90 _PyFunction_FastCallDict (kwargs=0x0, nargs=<optimized out>, args=<optimized out>, func=0x7ffff7a4fa70)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:322
#91 _PyObject_FastCallDict (callable=0x7ffff7a4fa70, args=<optimized out>, nargs=<optimized out>, kwargs=0x0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:98
#92 0x000055555566f43d in object_vacall (callable=0x7ffff7a4fa70, vargs=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:1200
#93 0x0000555555697253 in _PyObject_CallMethodIdObjArgs (obj=<optimized out>, name=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Objects/call.c:1250
#94 0x0000555555668039 in import_find_and_load (abs_name=0x7ffff789b3b0) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/import.c:1652
#95 PyImport_ImportModuleLevelObject (name=0x7ffff789b3b0, globals=<optimized out>, locals=<optimized out>, fromlist=0x55555588e010 <_Py_NoneStruct>, level=0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/import.c:1764
#96 0x000055555571a0e2 in import_name (level=0x5555558b83a0 <small_ints+160>, fromlist=0x55555588e010 <_Py_NoneStruct>, name=0x7ffff789b3b0, f=0x555555944df0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:4770
#97 _PyEval_EvalFrameDefault (f=0x555555944df0, throwflag=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:2600
#98 0x000055555566ce85 in PyEval_EvalFrameEx (throwflag=0, f=0x555555944df0) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:547
#99 _PyEval_EvalCodeWithName (_co=<optimized out>, globals=<optimized out>, locals=<optimized out>, args=<optimized out>, argcount=<optimized out>, 
    kwnames=0x0, kwargs=0x0, kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x0, qualname=0x0)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3930
#100 0x000055555566e273 in PyEval_EvalCodeEx (closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwcount=0, kws=0x0, argcount=0, args=0x0, 
    locals=<optimized out>, globals=<optimized out>, _co=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:3959
#101 PyEval_EvalCode (co=<optimized out>, globals=<optimized out>, locals=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/ceval.c:524
#102 0x000055555577bc82 in run_mod (mod=<optimized out>, filename=<optimized out>, globals=0x7ffff7a14b90, locals=0x7ffff7a14b90, flags=<optimized out>, 
    arena=<optimized out>) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/pythonrun.c:1037
#103 0x0000555555785e1e in PyRun_FileExFlags (fp=0x5555558bc310, filename_str=<optimized out>, start=<optimized out>, globals=0x7ffff7a14b90, 
    locals=0x7ffff7a14b90, closeit=1, flags=0x7fffffffe300) at /home/builder/tkoch/workspace/python_1648536129212/work/Python/pythonrun.c:990
#104 0x000055555578600b in PyRun_SimpleFileExFlags (fp=0x5555558bc310, filename=<optimized out>, closeit=1, flags=0x7fffffffe300)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Python/pythonrun.c:429
#105 0x00005555557870fa in pymain_run_file (p_cf=0x7fffffffe300, filename=0x5555558bf5c0 L"setup.py", fp=0x5555558bc310)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Modules/main.c:462
#106 pymain_run_filename (cf=0x7fffffffe300, pymain=0x7fffffffe410) at /home/builder/tkoch/workspace/python_1648536129212/work/Modules/main.c:1652
#107 pymain_run_python (pymain=0x7fffffffe410) at /home/builder/tkoch/workspace/python_1648536129212/work/Modules/main.c:2913
#108 pymain_main (pymain=0x7fffffffe410) at /home/builder/tkoch/workspace/python_1648536129212/work/Modules/main.c:3460
#109 0x000055555578718c in _Py_UnixMain (argc=<optimized out>, argv=<optimized out>)
    at /home/builder/tkoch/workspace/python_1648536129212/work/Modules/main.c:3495
#110 0x00007ffff7c69083 in __libc_start_main (main=0x555555645060 <main>, argc=3, argv=0x7fffffffe578, init=<optimized out>, fini=<optimized out>, 
    rtld_fini=<optimized out>, stack_end=0x7fffffffe568) at ../csu/libc-start.c:308
#111 0x000055555572c03a in _start ()
```

</details>

It's an AVX instruction that is causing the error, my CPU (Pentium G4560) does not have AVX support:

```
(gdb) display/i $pc
1: x/i $pc
=> 0x7fffc45d92d0 <__cxx_global_var_init.1>:	vmovsd -0xcfec620(%rip),%xmm0        # 0x7fffb75eccb8
```

I guess I will try recompiling librocblas to see if I can make any progress there.

---

### 评论 #2 — AN3223 (2022-10-17T06:15:13Z)

Compiled rocBLAS with debug symbols:

```
Program received signal SIGILL, Illegal instruction.
__cxx_global_var_init.3(void) () at /sd/rocBLAS/library/src/blas_ex/rocblas_trsv_inverse.hpp:14
14      static const T zero = T(0);
```

Also tried compiling without Tensile to see what would happen:
```
Traceback (most recent call last):
File "setup.py", line 12, in <module>
	import torch
	File "/opt/conda/lib/python3.7/site-packages/torch/__init__.py", line 199, in <module>
		from torch._C import *  # noqa: F403
	ImportError: /opt/rocm/lib/librocsolver.so.0: undefined symbol: _Z36rocblas_internal_trsm_workspace_sizeILi128ELb0EfE15rocblas_status_13rocblas_side_18rocblas_operation_iiiiPmS3_S3_S3_S3_
```

---

### 评论 #3 — hliuca (2023-05-11T16:47:17Z)

it looks for libncurses-dev. you may modify build.ninja and add -lncurses to LINK_LIBRARIES.

---

### 评论 #4 — pruthvistony (2023-07-30T20:50:21Z)

@AN3223 ,
The above errors are related libtinfo. You can get some info at - https://github.com/ROCmSoftwarePlatform/pytorch/blob/rocm5.7_internal_testing/cmake/Dependencies.cmake#L1237

Let us know if you are still having issues, if not I will close this issue.

---

### 评论 #5 — Dreamail (2023-08-13T07:11:56Z)

I have the same issue in ubuntu:22.04 docker image

---

### 评论 #6 — Dreamail (2023-08-13T08:31:43Z)

cherry-pick bd7979244f79a8841509220e0327a156d0380414 fix my issue

---

### 评论 #7 — hongxiayang (2023-12-04T19:05:21Z)

gfx803 is not officially supported. Please check the supported GPUs and gfx targets in this documentation:

https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html


---
