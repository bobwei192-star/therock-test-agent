# Met problems using hipcub.hpp

> **Issue #2045**
> **状态**: closed
> **创建时间**: 2023-04-14T03:37:31Z
> **更新时间**: 2023-04-17T14:44:30Z
> **关闭时间**: 2023-04-17T08:47:54Z
> **作者**: DesmonDay
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2045

## 负责人

- MathiasMagnus

## 描述

Hi, recently I need to use ROCm to compile PaddlePaddle. But I met this problem:
<img width="993" alt="96159e6e67a407900b5515b4b67063a9" src="https://user-images.githubusercontent.com/20554008/231935393-79e50863-27df-4404-83b8-5f0a16c63eeb.png">


However, I have already include the corresponding head files:
<img width="308" alt="1b26b9662d2a067e3e55c9929f25be0f" src="https://user-images.githubusercontent.com/20554008/231935183-acb43699-38ce-43db-bffd-936951706673.png">

I check the hipcub.hpp, which includes the util_type.cuh file. But it cannot find the hipcub::Traits. Can anyone help?

---

## 评论 (2 条)

### 评论 #1 — saadrahim (2023-04-14T14:12:11Z)

@MathiasMagnus can you please redirect to the appropriate developer?

---

### 评论 #2 — sbalint98 (2023-04-17T14:44:30Z)

Hi, the root of the problem is that this namespace alias is not allowed in C++ in case the NVIDIA platform is used. Since all the CUB headers are included by `hipcub.hpp` for that platform, the `cub` namespace will also be defined. According to the [C++ reference](https://en.cppreference.com/w/cpp/language/namespace_alias), using an already existing namespace as an alias is not allowed.

There are a few options how to handle this situation:

* Only use the cub alias in case the target platform is AMD. The platform can be detected using the `__HIP_PLATFORM_AMD__` and the `__HIP_PLATFORM_NVIDIA__` macros. In this particular situation this could look as the following:

```
#ifdef PADDLE_WITH_HIP
#include <hipcub/hipcub.hpp>

#ifdef __HIP_PLATFORM_AMD__
namespace cub = hipcub;
#endif

#endif 
```

* Alternatively, switching to the `hipcub` namespace would be cleaner. However, I assume that is not preferable since paddle should work with CUB without any modifications.

* A possible compromise solution could be to use the namespace defined as a macro: That way, it would be possible to switch to the `hipcub` namespace when `PADDLE_WITH_HIP` is defined.

* Omit naming the namespace and use `using namespace cub;` or `using namespace hipcub;` based on the platform

* Use a 3rd namespace, which is neither cub nor hipcub. 

---
