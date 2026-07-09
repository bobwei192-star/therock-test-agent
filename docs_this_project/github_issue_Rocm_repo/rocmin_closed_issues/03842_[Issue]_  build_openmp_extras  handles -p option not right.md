# [Issue]:  build_openmp_extras  handles -p option not right

- **Issue #:** 3842
- **State:** closed
- **Created:** 2024-10-01T09:51:40Z
- **Updated:** 2025-06-19T19:03:51Z
- **Labels:** Under Investigation, AMD Radeon VII, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3842

### Problem Description

The optionsparser in build_openmp_extras.sh sets in lines 42–43  "TARGET"  to "package", but doesn't use $2 to set "MAKETARGET" to given  package format:
'        -p  | --package )
            TARGET="package" ;;'
A coressponding target is not defined in the target selector in lines 666–671:
'case $TARGET in
    (clean) clean_openmp_extras ;;
    (build) build_openmp_extras; package_openmp_extras ;;
    (outdir) print_output_directory ;;
    (*) die "Invalid target $TARGET" ;;
esac'
Given format is ignored, like said above.

### Operating System

Debian 12 Bookworm with Backports

### CPU

AMD Ryzen 5 5600G with Radeon Graphics

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.2.0

### ROCm Component

aomp-extras

### Steps to Reproduce

Open build_openmp_extras.sh in editor, inspect line 42–43 and 666–671.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_