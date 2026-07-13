# [Issue]: Undefined reference to ncurses libraries

- **Issue #:** 3574
- **State:** closed
- **Created:** 2024-08-13T03:13:38Z
- **Updated:** 2024-08-14T15:57:28Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.1.0, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3574

### Problem Description

When compiling a very simple test program, whenever I link to any external library (i.e. anything not hip), I am getting the following error

```
/usr/bin/ld: /opt/rocm/lib/libamd_comgr.so.2: undefined reference to `tigetnum@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm/lib/libamd_comgr.so.2: undefined reference to `del_curterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm/lib/libamd_comgr.so.2: undefined reference to `setupterm@NCURSES6_TINFO_5.0.19991023'
/usr/bin/ld: /opt/rocm/lib/libamd_comgr.so.2: undefined reference to `set_curterm@NCURSES6_TINFO_5.0.19991023'
```



### Operating System

Ubuntu 22.04

### CPU

Ryzen 7900X

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.2.0, ROCm 6.1.0

### ROCm Component

HIP

### Steps to Reproduce

Unpack the following file: [rocm-ex.zip](https://github.com/user-attachments/files/16593948/rocm-ex.zip)

Run the following
```
mkdir build
cmake ..
make
```

Note, currently the cmake file uses opencv libraries as the external library, feel free to change that.

It **will** compile if you remove line 46 of the `CMakeLists.txt` file.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

I suspect it is something extremely small that I am doing incorrectly in my cmake but I can't figure out what it is for the life of me.