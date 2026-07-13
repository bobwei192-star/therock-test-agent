# [Issue]: Out of memory during fine-tuning

- **Issue #:** 3579
- **State:** closed
- **Created:** 2024-08-13T22:34:19Z
- **Updated:** 2024-09-04T14:28:23Z
- **Labels:** Under Investigation, AMD Instinct MI250X, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3579

### Problem Description

I am attempting to fine-tune Llama2 following the official documentation [here](https://rocm.docs.amd.com/en/latest/how-to/llm-fine-tuning-optimization/single-gpu-fine-tuning-and-inference.html) on a machine equipped with 4 MI 250X GPUs. Despite strictly adhering to the instructions, the fine-tuning process failed on both single GPU and multiple GPU configurations.



### Operating System

Red Hat Enterprise Linux(Docker: Ubuntu)

### CPU

AMD EPYC 7A53

### GPU

AMD Instinct MI250X

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

https://rocm.docs.amd.com/en/latest/how-to/llm-fine-tuning-optimization/single-gpu-fine-tuning-and-inference.html and https://rocm.docs.amd.com/en/latest/how-to/llm-fine-tuning-optimization/multi-gpu-fine-tuning-and-inference.html

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

[rocminfo.txt](https://github.com/user-attachments/files/16605974/rocminfo.txt)


### Additional Information

_No response_