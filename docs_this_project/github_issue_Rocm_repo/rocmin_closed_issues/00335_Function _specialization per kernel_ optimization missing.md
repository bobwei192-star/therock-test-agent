# Function "specialization per kernel" optimization missing

- **Issue #:** 335
- **State:** closed
- **Created:** 2018-02-14T20:14:15Z
- **Updated:** 2018-02-14T21:20:47Z
- **URL:** https://github.com/ROCm/ROCm/issues/335

Ubuntu 17.10, Vega64, OpenCL, ROCm 1.7 and "OpenCL head build".

An important optimization, that I call "function specialization", is missing/broken. See this example:
A:
```
void funWith1() {
  // do something using parameter value "1".
}

void funWith2() {
  // do something using parameter value "2".
}

kernel void kernWith1() { funWith1(); }

kernel void kernWith2() { funWith2(); }
```

B:
```
void dispatch(uint N) {
  if (N == 1) {
    funWith1();
  } else if (N == 2) {
    funWith2();
  }
}

kernel void kernWith1() { dispatch(1); }

kernel void kernWith2() { dispatch(2); }
```

The problem is that case A is optimized better then case B. Likely this is because in case B, the "dispatch()" function is invoked with various arguments (i.e. non-constant), which disables the specialization that is done for a constant argument situation.

But note that, even in case B, the call to dispatch() is done with constant arguments *per-kernel*. If dispatch() would be compiled into one-version-per-kernel, there would be no problem to specialize and optimize it just as well as case A.

"function specialization" would mean: during compilation, duplicate and specialize dispatch() into two functions -- each invoked with constant arguments -- and optimize accordingly.

The workaround I can do right now is:
```
#ifdef COMPILE_KERN1
kernel void kernWith1() { dispatch(1); }
#endif

#ifdef COMPILE_KERN2
kernel void kernWith2() { dispatch(2); }
#endif
```

And invoke the compiler twice, compiling only one kernel each time, which allows proper specialization of dispatch(). The drawback is that this way of using the compiler, in addition to being cumbersome, is much slower than it needs to be.