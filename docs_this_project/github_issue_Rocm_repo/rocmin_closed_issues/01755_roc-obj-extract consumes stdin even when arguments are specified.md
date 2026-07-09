# roc-obj-extract consumes stdin even when arguments are specified.

- **Issue #:** 1755
- **State:** closed
- **Created:** 2022-06-16T21:20:32Z
- **Updated:** 2024-01-25T02:42:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/1755

roc-obj-extract consumes stdin due to a coding error.    While it works interactively, if you 
script roc-object-extract, it  will try consuming stdin, and be confused by the input.

The fix to this is to check for argv having arguments, and NOT push stdin before argv in 
this case.     This is the patch I used to not read stdin when arguments are present after 
option parsing.   If you pipe roc-obj-ls to the modified roc-obj-extract with a  awk '{print $3;}' 
to select the URI, it works in that mode as well.

[roc-obj-extract.patch.txt](https://github.com/RadeonOpenCompute/ROCm/files/8922431/roc-obj-extract.patch.txt)
