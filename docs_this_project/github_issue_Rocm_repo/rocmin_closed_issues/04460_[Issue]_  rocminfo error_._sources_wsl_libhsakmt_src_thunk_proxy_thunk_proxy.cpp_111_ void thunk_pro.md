# [Issue]:  rocminfo error:./sources/wsl/libhsakmt/src/thunk_proxy/thunk_proxy.cpp:111: void thunk_proxy::QueryAdapterInfo(D3DKMT_HANDLE, ATIADAPTERINFO*): Assertion `ret == STATUS_SUCCESS' failed

- **Issue #:** 4460
- **State:** closed
- **Created:** 2025-03-07T11:31:06Z
- **Updated:** 2025-05-21T02:49:21Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4460

### Problem Description

1. Follow the instructions at https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html to install.
2. execute "rocminfo"
3. print:
WSL environment detected.
rocminfo: ./sources/wsl/libhsakmt/src/thunk_proxy/thunk_proxy.cpp:111: void thunk_proxy::QueryAdapterInfo(D3DKMT_HANDLE, ATIADAPTERINFO*): Assertion `ret == STATUS_SUCCESS' failed.
Aborted (core dumped)



### Operating System

WSL-Ubuntu24.04

### CPU

AMD 5900x

### GPU

AMD 7900XTX

### ROCm Version

ROCm 6.3.4

### ROCm Component

_No response_

### Steps to Reproduce

1. Follow the instructions at https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html to install.
2. execute "rocminfo"
3. print:
```
WSL environment detected.
rocminfo: ./sources/wsl/libhsakmt/src/thunk_proxy/thunk_proxy.cpp:111: void thunk_proxy::QueryAdapterInfo(D3DKMT_HANDLE, ATIADAPTERINFO*): Assertion `ret == STATUS_SUCCESS' failed.
Aborted (core dumped)
```
![Image](https://github.com/user-attachments/assets/80576668-af84-4efe-a8a9-f8de147bbf43)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

still print:
```
WSL environment detected.
rocminfo: ./sources/wsl/libhsakmt/src/thunk_proxy/thunk_proxy.cpp:111: void thunk_proxy::QueryAdapterInfo(D3DKMT_HANDLE, ATIADAPTERINFO*): Assertion `ret == STATUS_SUCCESS' failed.
Aborted (core dumped)
```

### Additional Information

AMD GPU driver version: 25.3.1
WSL version： 2.4.11.0
kernel version： 5.15.167.4-1
WSLg version： 1.0.65
MSRDC version： 1.2.5716
Direct3D version： 1.611.1-81528511
DXCore version： 10.0.26100.1-240331-1435.ge-release
Windows version： 10.0.26100.3323

![Image](https://github.com/user-attachments/assets/8d56b925-6ca2-4dfe-81f4-c4cf36334c21)