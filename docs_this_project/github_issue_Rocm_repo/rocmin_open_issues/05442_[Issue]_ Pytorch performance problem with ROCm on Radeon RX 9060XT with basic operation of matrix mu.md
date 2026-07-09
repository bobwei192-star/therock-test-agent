# [Issue]: Pytorch performance problem with ROCm on Radeon RX 9060XT with basic operation of matrix multiplication

- **Issue #:** 5442
- **State:** open
- **Created:** 2025-09-28T17:31:14Z
- **Updated:** 2025-11-14T15:18:27Z
- **Labels:** status: triage
- **Assignees:** adityas-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5442

### Problem Description

I have good ROCm performance for matrix dimensions: sizes = [512, 1024, 2048, 4096] but bad performance for matrix dimensions: sizes = [500, 1000, 2000, 3000, 4000, 5000]
I used pytorch.matmul() but the situation is similar using pytorch.mm().

<img width="800" height="600" alt="Image" src="https://github.com/user-attachments/assets/8b816bf0-aeab-4cda-8eee-6b39e277e79b" />

<img width="800" height="600" alt="Image" src="https://github.com/user-attachments/assets/3ee33fb2-a6d0-44b9-ae73-47f1ca0a14a6" />

### Operating System

Ubuntu  24.04.3 LTS (Noble Numbat)

### CPU

12th Gen Intel(R) Core(TM) i5-12500

### GPU

AMD Radeon RX 9060 XT    gfx1200

### ROCm Version

ROCm 7.0.1

### ROCm Component

_No response_

### Steps to Reproduce

[matmul_benchmark.py](https://github.com/user-attachments/files/22584163/matmul_benchmark.py)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.14.14 is loaded
=====================    
 
[rocminfo.txt](https://github.com/user-attachments/files/22584180/rocminfo.txt)

### Additional Information

_No response_