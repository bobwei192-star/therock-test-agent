# [Error on PyTorch] Memory access fault by GPU node-4. Reason: Page not present or supervisor privilege.

> **Issue #1262**
> **状态**: closed
> **创建时间**: 2020-10-18T17:20:23Z
> **更新时间**: 2020-10-30T09:53:40Z
> **关闭时间**: 2020-10-30T09:53:39Z
> **作者**: mfkasim1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1262

## 描述

I am implementing a incomplete gamma function in PyTorch in CPU and CUDA, but I always have a problem with a test with ROCm in PyTorch's CI.
The log can be found [here](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-linux-bionic-rocm3.8-py3.6-test2/1723/console) (search for `test_igamma_common_cuda_float64`) with some of the log:

    21:18:17 test_igamma_common_cuda_float32 (__main__.TestTorchDeviceTypeCUDA) ... ok
    21:18:18 test_igamma_common_cuda_float64 (__main__.TestTorchDeviceTypeCUDA) ... Memory exception on virtual address 0x7f32775e8000, node id 4 : Page not present
    21:18:18 Address does not belong to a known buffer
    21:18:18 Memory access fault by GPU node-4 (Agent handle: 0x55d2eee23120) on address 0x7f32775e8000. Reason: Page not present or supervisor privilege.

My pull request can be seen [here](https://github.com/pytorch/pytorch/pull/46183) with the CUDA implementation of the function can be seen [here](https://github.com/pytorch/pytorch/pull/46183/files?file-filters%5B%5D=.cpp&file-filters%5B%5D=.cu&file-filters%5B%5D=.cuh&file-filters%5B%5D=.h&file-filters%5B%5D=.py&file-filters%5B%5D=.rst&file-filters%5B%5D=.yaml#diff-279bf1f9943ed149363f7e7a5e2710fd50c913ac70ea7f29d54a095777fbb571).

I'm not sure why the error happens. Strangely, it works well with `float32`.

---

## 评论 (8 条)

### 评论 #1 — ghost (2020-10-19T05:22:18Z)

Hi @mfkasim1 , 

    Thank you for filling the ticket.

    Could you kindly share more details about your system(CI node from the hardware prospective)? and output log of  "/opt/rocm/bin/rocminfo".

---

### 评论 #2 — mfkasim1 (2020-10-19T09:52:36Z)

Hi @ashutoshamd, I'm afraid I don't have access to know the specs and the logs. All I can see is just everything from [this page](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-linux-bionic-rocm3.8-py3.6-test2/1723/console).

---

### 评论 #3 — ghost (2020-10-23T06:39:17Z)

Hi @mfkasim1,

From the logs, I was able to get the configuration details of the H/W & S/W. 
I took Upstream PyTorch & pulled your patch to it & I tried to compile & test, but unable to get test generated.


```

root@taccuser-All-Series:/var/lib/jenkins/pytorch# python3.6 test/test_torch.py TestTorchDeviceTypeCPU.test_igamma_common_cuda_float32
E
======================================================================
ERROR: test_igamma_common_cuda_float32 (unittest.loader._FailedTest)
----------------------------------------------------------------------
AttributeError: type object 'TestTorchDeviceTypeCPU' has no attribute 'test_igamma_common_cuda_float32'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
root@taccuser-All-Series:/var/lib/jenkins/pytorch# grep -rn test_igamma_common_cuda_float32 *
root@taccuser-All-Series:/var/lib/jenkins/pytorch#


```

Also, I did ran the test bench  .jenkins/pytorch/test.sh  , but there also, I could not see any "_igamma_common_cuda" , in the logs  for both passed / failed test.

I did test with after removing this[ commit ](https://github.com/pytorch/pytorch/pull/46183/commits/c22072616d09c31742a215edbba86e7863335a85)  : "Skip ROCm CUDA test" 

and currently my file stands like this 

```

17392         half_prec = dtype in [torch.bfloat16, torch.float16]
17393         for input0, input1 in inputs:
17394             actual = torch.igamma(input0, input1)
17395             if half_prec:
17396                 input0 = input0.to(torch.float)
17397                 input1 = input1.to(torch.float)
17398             expected = scipy.special.gammainc(input0.cpu().numpy(), input1.cpu().numpy())
17399             expected = torch.from_numpy(expected).to(dtype)
17400             self.assertEqual(actual, expected)
17401
17402     @dtypesIfCPU(torch.float16, torch.bfloat16, torch.float32, torch.float64)
17403     @dtypes(torch.float32, torch.float64)
17404     @unittest.skipIf(not TEST_SCIPY, "SciPy not found")
17405     @onlyOnCPUAndCUDA
17406     def test_igamma_common(self, device, dtype):
17407         # test igamma for reasonable range of values
17408         loglo = -4  # approx 0.018
17409         loghi = 4  # approx 54.6
17410         self._helper_test_igamma(loglo, loghi, device, dtype)
17411
17412     @dtypesIfCPU(torch.float16, torch.bfloat16, torch.float32, torch.float64)
17413     @dtypes(torch.float32, torch.float64)
17414     @onlyOnCPUAndCUDA
17415     def test_igamma_edge_cases(self, device, dtype):
17416         tkwargs = {"dtype": dtype, "device": device}
17417         infs = torch.zeros((3,), **tkwargs) + float("inf")
17418         zeros = torch.zeros((3,), **tkwargs)
17419         ones = torch.ones((3,), **tkwargs)
17420         zero_to_large = torch.tensor([0., 1., 1e3], **tkwargs)


```
Still the result is same.
What is that we are missing here?

---

### 评论 #4 — mfkasim1 (2020-10-23T09:27:18Z)

Hi @ashutoshamd, I think the test should be called `TestTorchDeviceTypeCUDA.test_igamma_common_cuda_float32`.

---

### 评论 #5 — ghost (2020-10-29T13:52:36Z)

Hi @mfkasim1 ,   I tried again.  It runs fine on the same hardware/software as per your logs.


```
root@taccuser-All-Series:/var/lib/jenkins/pytorch# python3.6 test/test_torch.py  TestTorchDeviceTypeCUDA.test_igamma_common_cuda_float64
.
----------------------------------------------------------------------
Ran 1 test in 1.848s

OK
root@taccuser-All-Series:/var/lib/jenkins/pytorch# python3.6 test/test_torch.py  TestTorchDeviceTypeCUDA.test_igamma_common_cuda_float32
.
----------------------------------------------------------------------
Ran 1 test in 1.529s

OK

```

All works fine for me.

Do you have any other info for reproduction scenario? 

---

### 评论 #6 — mfkasim1 (2020-10-29T17:05:56Z)

Hmmm.. did you remove the `@skipCudaIfROCm` line on the test?
I added it there because I was not sure how to fix it.
If you did remove it, I can try to remove it later in another PR to PyTorch.

---

### 评论 #7 — ghost (2020-10-30T05:53:25Z)

Yes, as shown above my file is in the current state as shown.
It is running the test without any failure for me.


---

### 评论 #8 — mfkasim1 (2020-10-30T09:53:39Z)

Thanks for trying this and sorry I can't give you more information about the reproduction.
I will close this issue until I can get more info to reproduce the error.

---
