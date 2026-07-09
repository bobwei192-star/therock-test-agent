# roc-obj searches for llvm-tools in wrong place

- **Issue #:** 1814
- **State:** closed
- **Created:** 2022-09-29T13:27:26Z
- **Updated:** 2024-02-09T15:22:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/1814

Using roc-obj in current 5.2.3 gives an error
``` shell
~/$ /opt/rocm/bin/roc-obj -d test
error: could not find llvm-objdump in /opt/rocm-5.2.3/bin /opt/rocm-5.2.3/bin/../../llvm/bin or PATH
```

Inspection shows that the search path is wrong, it should be `/opt/rocm-5.2.3/bin/../llvm/bin`. Line 140
``` shell
  for dir in "$BASE_DIR" "${HIP_CLANG_PATH:-"$BASE_DIR/../../llvm/bin"}"; do
```
of `roc-obj` script should be fixed to 
``` shell
  for dir in "$BASE_DIR" "${HIP_CLANG_PATH:-"$BASE_DIR/../llvm/bin"}"; do
```
After such a change it runs smoothly.
