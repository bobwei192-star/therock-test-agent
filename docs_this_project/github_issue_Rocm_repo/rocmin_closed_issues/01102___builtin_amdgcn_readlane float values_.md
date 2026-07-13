# __builtin_amdgcn_readlane float values?

- **Issue #:** 1102
- **State:** closed
- **Created:** 2020-05-08T10:18:18Z
- **Updated:** 2020-09-14T01:29:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1102

Hi,

I would like to do `v_readlane_b32` on float values. `v_readlane_b32` doesn't really care about the type (as long as it's 32 bit), but `__builtin_amdgcn_readlane` does.

Is there something (or override) like:
```c++
float __builtin_amdgcn_readlane(float src, uint lane);

// Besides uint __builtin_amdgcn_readlane(uint src, uint lane);
```
Or let `llvm.amdgcn.readlane` work on float values?

<br>

I tried this (compile error):
```c++
extern float __llvm_amdgcn_readlane(float src, uint lane) __asm("llvm.amdgcn.readlane");
```

<br>

I also tried a bit with inlining LLVM `bitcast`, but without fortune :(

Thanks a lot!