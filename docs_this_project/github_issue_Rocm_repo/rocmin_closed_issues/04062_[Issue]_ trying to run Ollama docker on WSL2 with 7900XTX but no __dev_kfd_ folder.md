# [Issue]: trying to run Ollama docker on WSL2 with 7900XTX but no "/dev/kfd" folder

- **Issue #:** 4062
- **State:** closed
- **Created:** 2024-11-28T09:25:53Z
- **Updated:** 2024-12-12T14:58:40Z
- **Labels:** Under Investigation, ROCm 6.2.3, AMD Radeon 7900XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4062

### Problem Description

I can confirm that I have installed the ROCm and PyTorch on WSL correctly (according to the official document and this: https://github.com/ROCm/ROCm/issues/3563), as all post install checks are passed (rocminfo command works and pytorch retuen "True" for checking CUDA). but when I run "docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
", it says "ERROR:  /dev/kfd no such file or directory". 

However I have came across this issue: https://github.com/ROCm/ROCm/issues/3734, so I substitute "--device /dev/kfd" to "--device /dev/dxg", it still cannot recognize the GPU and run the model on CPU. But if I just installed the .exe from Ollama official website, that one does utilize the GPU. 

And I have also came across to this: https://github.com/ollama/ollama/issues/5275, which it basically says it is expected to have no directory called "/dev/kfd" by following the instructions, but I haven't try the poster's method for fear that the system would break. So is this a recognized issue and will be fixed in future or I am doing something wrong?  

P.S. I am sorry that I have deleted all the setups because it got me frustrated, but I will do this again and post the log of not finding the GPU here shortly after.

### Operating System

Ubuntu 22.04.5 LTS (WSL2) / Ubuntu 24.04.1 LTS (WSL2)

### CPU

Ryzen R7-7700X

### GPU

AMD Radeon 7900XTX

### ROCm Version

ROCm 6.2.3 / ROCm 6.1.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_