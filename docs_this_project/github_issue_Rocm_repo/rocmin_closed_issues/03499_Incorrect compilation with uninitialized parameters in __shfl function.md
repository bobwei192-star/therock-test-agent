# Incorrect compilation with uninitialized parameters in __shfl function

- **Issue #:** 3499
- **State:** closed
- **Created:** 2024-08-02T18:57:06Z
- **Updated:** 2024-12-03T23:34:27Z
- **Labels:** Verified Issue, 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3499

The compiler may incorrectly compile a program that uses the `__shfl(var, srcLane, width)` function when one of the parameters to the function is undefined along some path to the function. For most functions, uninitialized inputs cause undefined behavior.

>Note:
>
>The `-Wall` compilation flag prompts the compiler to generate a warning if a variable is uninitialized along some path.

As a workaround, initialize the parameters to __shfl. For example:

```
unsigned long istring = 0 // Initialize the input to __shfl
return __shfl(istring, 0, 64)
```