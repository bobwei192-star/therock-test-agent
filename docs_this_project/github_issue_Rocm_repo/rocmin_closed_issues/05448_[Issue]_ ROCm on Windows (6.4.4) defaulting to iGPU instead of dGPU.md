# [Issue]: ROCm on Windows (6.4.4) defaulting to iGPU instead of dGPU

- **Issue #:** 5448
- **State:** closed
- **Created:** 2025-09-30T07:00:43Z
- **Updated:** 2025-12-30T15:47:29Z
- **Labels:** AMD Radeon RX 7900 XTX, status: triage
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5448

### Problem Description

(base) PS C:\Users\10649> (Get-WmiObject Win32_OperatingSystem).Version
10.0.26100
(base) PS C:\Users\10649>   (Get-WmiObject win32_Processor).Name
AMD Ryzen 5 9600X 6-Core Processor
(base) PS C:\Users\10649>   (Get-WmiObject win32_VideoController).Name
Parsec Virtual Display Adapter
OrayIddDriver Device
Microsoft Remote Display Adapter
AMD Radeon(TM) Graphics
AMD Radeon RX 7900 XTX

<img width="1641" height="562" alt="Image" src="https://github.com/user-attachments/assets/c1bf02ff-d079-499d-ae0b-0522f8fcf8ee" />

<img width="2081" height="604" alt="Image" src="https://github.com/user-attachments/assets/852b8104-15ad-433c-89bf-2dec79cd331c" />

Cant find my gpu

### Operating System

10.0.26100

### CPU

9600x

### GPU

Rx 7900 xtx

### ROCm Version

6.4.50101-9a6572ae7

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_