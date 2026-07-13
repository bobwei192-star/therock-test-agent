# Run ROCm with two AMD GPU's

- **Issue #:** 1168
- **State:** closed
- **Created:** 2020-06-28T20:02:28Z
- **Updated:** 2020-12-17T04:32:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1168

Hey, 

I am trying to install a second AMD GPU on my machine to run machine learning problems. 

My setup:

Motherboard: Asus Prime Z270-P
CPU: Intel Core i5-7500
Graphics: Radeon RX 570 Series (POLARIS10, DRM 3.37.0, 5.3.0-61-generic, LLVM 9.0.0)
GPU 0: MSI Ellesmere [Radeon RX 470/480/570/570X/580/580X]
GPU 1: ASUS Ellesmere [Radeon RX 470/480/570/570X/580/580X]
ROCm Version: Version: 3.5.1-34
Linux OS: Ubuntu 18.04.1
Kernel: 5.3.0-61-generic
ROCm installation guide: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html
ROCm-tensorflow instructions: pip3 install tensorflow-rocm
tensorflow version: 2.2.0

Running "rocm-smi -s" I see the two GPUs (added above). 

Running dmesg I see it's rejecting atomics: dmesg | grep kfd
[    1.460499] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    1.461213] kfd kfd: amdgpu: added device 1002:67df
[    1.487376] kfd kfd: amdgpu: skipped device 1002:67df, PCI rejects atomics

I don't understand the PCIe atomics to be honest, but I have read about it a few times and I thought that was relative to the CPU/GPU of which I though I was good? In my motherboard BIOS I set it to Gen3 for the PCIe slots. My GPU's are connected into PCIEX16_1 and PCIEX16_2 where the GPU in PCIEX16_1 is working. 
 
Testing the working GPU: I am running a virtual environment. I tested rocm tensorflow on the resnet50 after I download the tensorflow benchmark: "python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=64 --model=resnet50" and in another tab I am running: "watch -n 1 rocm-smi" and I see GPU [0] running and I get results returned from the benchmark test (20 images a second lol)

But when I try --num_gpus=2 I get a long list of errors. 

Is there any solution to run two GPUs with ROCm that I am not doing? Why is it rejecting atomics but working on one of the GPU's? Is my motherboard the issue? Maybe reset my motherboard bios to default? 

Thank you all for your help!
