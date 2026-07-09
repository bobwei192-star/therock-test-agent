# atomicMax(double) crashes

- **Issue #:** 1441
- **State:** closed
- **Created:** 2021-04-06T02:57:15Z
- **Updated:** 2021-04-07T12:13:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/1441

Due to there is no atomicMax(double *address, const double val) api in hip, so implements it based on atomicCAS as follow:

```
__device__ __forceinline__ double AtomicDouble(double *address, const double val)
  if (*address >= val) {
    return *address;
  }

  unsigned long long int *const address_as_ull =            // NOLINT
      reinterpret_cast<unsigned long long int *>(address);  // NOLINT
  unsigned long long int old = *address_as_ull, assumed;    // NOLINT

  do {
    assumed = old;
    if (__longlong_as_double(assumed) >= val) {
      break;
    }

    old = atomicCAS(address_as_ull, assumed, __double_as_longlong(val));
  } while (assumed != old);
}
```

But it will crashes as follow:
```
:0:rocdevice.cpp            :2303: 609892899575 us: Device::callbackQueue aborting with status: 0x1016
```

It seems the AtomicDouble() is no problem, but after it will crashes.


The source code is https://github.com/PaddlePaddle/Paddle/pull/32049,

and
```
$ cd Paddle/build
$ ctest -R test_segment_ops -V
```

