# cross lane operation `__builtin_amdgcn_readlane`

- **Issue #:** 627
- **State:** closed
- **Created:** 2018-11-27T15:28:34Z
- **Updated:** 2018-12-19T20:21:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/627

I try to use the cross lane operation `__builtin_amdgcn_readlane` in OpenCL on Rocm 1.9 with a VEGA64.
The code is compiling but the result from the operation is always wrong:

```C++
            uint dest;
            uint src = get_local_id(0)  ;
            int lane = (get_local_id(0) + 1) %8 ;
            dest = __builtin_amdgcn_readlane(src,lane);
            __builtin_amdgcn_s_waitcnt(0);
            printf("read %u -> %u|%u\n",get_local_id(0),dest, lane);
```
The result in `dest` is always `1`
```
read 5 -> 1|6
read 6 -> 1|7
read 7 -> 1|0
read 0 -> 1|1
read 1 -> 1|2
```

But must be `(get_local_id(0) + 1) %8`.

If I hard code that all threads must read from lane e.g. 3 `dest = __builtin_amdgcn_readlane(src,3);` the result is for all `4` (correct!!).

I can not find any documentation or examples for the intrinsic. 
1. Could it be that variable lane address are not supported?
2. Is `__builtin_amdgcn_s_waitcnt` required after `__builtin_amdgcn_readlane`?