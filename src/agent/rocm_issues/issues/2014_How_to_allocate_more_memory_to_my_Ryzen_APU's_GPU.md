# How to allocate more memory to my Ryzen APU's GPU?

> **Issue #2014**
> **状态**: closed
> **创建时间**: 2023-04-03T09:00:56Z
> **更新时间**: 2025-02-04T23:40:33Z
> **关闭时间**: 2023-11-09T10:20:52Z
> **作者**: winstonma
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2014

## 描述

I am running AMD 6800U on my Ubuntu 22.04 and I installed the AMD driver. I checked that the default system would allocate 512MB RAM to VRAM to the GPU.

I followed [some instruction](https://github.com/RadeonOpenCompute/ROCm/issues/1756#issuecomment-1159603527) from other github issue to create a rocm/pytorch docker image and it has no problem detecting my GPU but it has problem running sample program, due to `OutOfMemoryError`.

```
torch.cuda.OutOfMemoryError: HIP out of memory. Tried to allocate 2.00 MiB (GPU 0; 512.00 MiB total capacity; 150.39 MiB already allocated; 312.00 MiB free; 168.00 MiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_HIP_ALLOC_CONF
```

So my guess is ROCm support APU but I just need to allocate more system memory to my GPU before going into the docker environment. Are there any people who know how to modify the memory allocation of AMD APU? Thanks in advance

---

## 评论 (59 条)

### 评论 #1 — ye-luo (2023-04-03T15:16:30Z)

An alternative route is to change the UMA buffer to 2GB in your BIOS.

---

### 评论 #2 — winstonma (2023-04-03T15:21:22Z)

Thanks. I tried to find this setting inside BIOS with no luck.

It seems to me that [AMD APU memory setting can be modified inside the windows ](https://community.amd.com/t5/graphics/increase-vram/m-p/538890) but I have no knowledge of the corresponding configuration within Linux.

---

### 评论 #3 — Ristovski (2023-05-27T11:00:58Z)

It appears ROCm does not take into account dynamic VRAM GTT allocation on APUs (handled by amdkfd?).

For example on my system:
```
[    3.524465] [drm] amdgpu: 64M of VRAM memory ready
[    3.524466] [drm] amdgpu: 15916M of GTT memory ready.
```

This means the iGPU could allocate up to 16GB of VRAM, however due to the small dedicated VRAM (64MB) that is _reserved_ for the iGPU, ROCm processes fail to allocate memory.

This also seems to propagate to OpenCL:
```
$ clinfo |grep -i memory
  Global memory size                              67108864 (64MiB)
  Global free memory (AMD)                        65536 (64MiB) 65536 (64MiB)
  Global memory channels (AMD)                    4
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Max memory allocation                           57042528 (54.4MiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
```

This is NOT the case for OpenGL tho (snippet of `glxinfo -B`):
```
Memory info (GL_ATI_meminfo):
    VBO free memory - total: 206 MB, largest block: 206 MB
    VBO free aux. memory - total: 15138 MB, largest block: 15138 MB
    Texture free memory - total: 206 MB, largest block: 206 MB
    Texture free aux. memory - total: 15138 MB, largest block: 15138 MB
    Renderbuffer free memory - total: 206 MB, largest block: 206 MB
    Renderbuffer free aux. memory - total: 15138 MB, largest block: 15138 MB
Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 256 MB
    Total available memory: 16172 MB
```

---

### 评论 #4 — winstonma (2023-05-28T07:35:34Z)

@Ristovski Thanks for the answer

I think this is a needed feature (otherwise all the APU would be ROCm-compatible but it doesn't work due to the memory allocation problem).

I am not sure if this should be fixed on the driver level or the ROCm level (or both).

---

### 评论 #5 — asbachb (2023-06-12T02:42:38Z)

This bug is indeed super annoying. Most laptop models only provide limited settings regarding UMA buffer size. So ROCm is quite limited or useless for APUs on Linux.

---

### 评论 #6 — winstonma (2023-06-12T06:29:11Z)

Thanks @asbachb I plan to just use my laptop just to do some primitive testing with a subset of data. I didn't plan to some fancy calculation with all the data. But since I am using Ryzen CPU I think I could still get acceleration using the GPU with the subset.

Current I guess everything is working except the memory allocation.

---

### 评论 #7 — asbachb (2023-06-12T06:37:54Z)

Just for reference some guy got some quite good results: (compared to CPU only): https://www.gabriel.urdhr.fr/2022/08/28/trying-to-run-stable-diffusion-on-amd-ryzen-5-5600g/

But he is able to set his VRAM to 16GB.

---

### 评论 #8 — winstonma (2023-06-12T07:45:38Z)

May I share what I saw in Windows envoirnment?

My laptop has 16GB of memory. This is what is being shown inside task manager
![image](https://github.com/RadeonOpenCompute/ROCm/assets/1215090/fba8d680-fade-426c-b75b-dbd9c2f07c63)

It shows that the 
* Dedicated GPU memory is 512MB
* Shared GPU memory is 7.6GB
* GPU memory is 8.1GB (It should be 7.6GB+512MB)

While I play GTA it shows that I have 8GB of GPU memory. I would wonder if it is possible that the ROCm would have the similar fashion, "thinking" that my GPU has 8GB of GPU memory.

But when I reboot back to my Ubuntu it shows that my GPU has 512MB of memory, which I guess that's the dedicated GPU memory that you can view in Windows. However in the application perspective it sees 8GB of memory, to me it should be the same as ROCm application should be able to see that my system should have 8GB of GPU memory, similar to GTA result in Windows.

It seems to me there is a missing piece in between.

---

### 评论 #9 — winstonma (2023-06-12T08:01:15Z)

@asbachb Sorry I forgot to answer the question in your post. First of all thank you very much.

I read the post and the author said that he modified the memory sharing behavior in BIOS. Which I don't have this settings in my laptop. Also in the previous answer the windows application sees the total GPU memory, not just the dedicated memory.

---

### 评论 #10 — randomstuff (2023-06-12T20:35:09Z)

@winstonma, I'm the author of the "Stable diffusion on an AMD Ryzen 5 5600G" post. Yes, sadly, I did not find any way to  increase the VRAM allocated to the iGPU without going to the BIOS/motherboard firmware.

---

### 评论 #11 — winstonma (2023-06-13T01:17:46Z)

@randomstuff Thanks. But sadly the BIOS of my laptop doesn't have the VRAM allocation option. So I wonder if there are ways to increase the dedicated memory on system level (similar to [Regedit in Windows](https://www.lifewire.com/increase-vram-on-a-windows-pc-5072150))

---

### 评论 #12 — pomoke (2023-07-27T06:53:00Z)

PyTorch  will work with replaced allocator which uses `hipHostMalloc`. I have a working snippet at <https://github.com/pomoke/torch-apu-helper>.

---

### 评论 #13 — winstonma (2023-08-14T02:29:41Z)

For all who is interested in increasing dedicated memory in system, I wrote an article [Unlocking GPU Memory Allocation on AMD Ryzen™ APU](https://medium.com/p/e27b75905056) and thought that method I could adjust the amount of dedicated GPU memory, even the BIOS doesn't provide that option.

---

### 评论 #14 — winstonma (2023-08-14T03:51:37Z)

> PyTorch will work with replaced allocator which uses `hipHostMalloc`. I have a working snippet at https://github.com/pomoke/torch-apu-helper.

Thanks.

I currently using alternative ways to unlock the BIOS, modify the amount of GPU dedicated memory to 8GB. After that I could run [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) using the [above method](https://github.com/RadeonOpenCompute/ROCm/issues/2014#issuecomment-1676583451) without any problem.

Also I cloned your repo, created `alloc.so` and add your code snippet in the launch.py of [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/master/launch.py). When I start running stable diffusion then it starts with a warning (but it can start):

```
Warning: caught exception 'CUDAPluggableAllocator does not yet support getDeviceStats. If you need it, please file an issue describing your use case.', memory monitor disabled
```

However when I start generating image I got the following error:

```
RuntimeError: CUDAPluggableAllocator does not yet support getDeviceStats. If you need it, please file an issue describing your use case.
```

I guess it's due to the fact that [CUDAPluggableAllocator couldn't provide all API](https://github.com/pytorch/pytorch/blob/c1cc74c7daa2156dd20406607dbee934be68f3a5/torch/csrc/cuda/CUDAPluggableAllocator.cpp#L191) which is required by the application yet. And thus no image is being generated. I am not sure if I miss anything. @pomoke not sure if you feel free to try running stable-diffusion-webui on your APU and see if that works. Thanks

Finally, I guess this is the memory auto-allocation should be the right direction. In Windows the system would auto-allocate the system memory to the GPU based on the software used. I guess PyTorch/ROCm should be talking to the system to auto-allocate a share of system memory to the GPU on demand. I just filed a [feature request in PyTorch](https://github.com/pytorch/pytorch/issues/107605), really wish they could request GPU memory from AMD APU.

---

### 评论 #15 — winstonma (2023-11-09T10:20:53Z)

In conclusion, there are several solutions for other AMD APU user

- [Override the BIOS settings to allocate more memory](https://github.com/RadeonOpenCompute/ROCm/issues/2014#issuecomment-1676583451). This method like the old days that you set your dedicated video memory in BIOS. More VRAM means less system memory.
- [torch-apu-helper](https://github.com/RadeonOpenCompute/ROCm/issues/2014#issuecomment-1653012878) uses the the Unified Memory Architecture (UMA), the APU would be able to allocate the memory from the system dynamically. It is a good demo but this way would not get all API working (e.g. getDeviceStats). If you are using application based on PyTorch, it would be likely that it would not work. I [filed an issue on PyTorch](https://github.com/pytorch/pytorch/issues/107605), hopefully they can add native AMD APU support.

---

### 评论 #16 — pomoke (2023-11-11T11:00:13Z)

Generally, we still need something like what we get on Tegra (Such as Jetson Developer Kit). CUDA on Tegra is capable of allocating GTT properly.

---

### 评论 #17 — winstonma (2023-11-13T04:26:24Z)

Yes I think the problem now is the torch-apu-helper shows that PyTorch could grab system memory from the system as video memory. However I think it still need more PyTorch API porting so we can say this way is PyTorch ready. Not sure AMD or PyTorch would make this possible in the future.

---

### 评论 #18 — gwyllion92 (2024-01-01T23:35:50Z)

> Yes I think the problem now is the torch-apu-helper shows that PyTorch could grab system memory from the system as video memory. However I think it still need more PyTorch API porting so we can say this way is PyTorch ready. Not sure AMD or PyTorch would make this possible in the future.

Hi, I'm trying to follow your guide [https://winstonhyypia.medium.com/amd-apu-how-to-modify-the-dedicated-gpu-memory-e27b75905056](url) but when I run this command _SA_OVERRIDE_GFX_VERSION=10.3.0 python test-rocm.py_

I get this message: 
_Command "python" not found. Maybe your meant:
  "python3" command from the deb package "python3".
  the "python" command from the deb package "python-is-python3"._
  
  So I changed the command to _HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 test-rocm.py_
  
 But I get this message now:
 _Traceback (most recent call last):
  File "/home/myUser/test-rocm.py", line 1, in <module>
    import torch, grp, pwd, os, subprocess
ModuleNotFoundError: No module named 'torch'_

I can't find any solution, and I'm not a programmer person.

**Thanks for your time!**


---

### 评论 #19 — winstonma (2024-01-02T00:13:38Z)

> > Yes I think the problem now is the torch-apu-helper shows that PyTorch could grab system memory from the system as video memory. However I think it still need more PyTorch API porting so we can say this way is PyTorch ready. Not sure AMD or PyTorch would make this possible in the future.
> 
> Hi, I'm trying to follow your guide [https://winstonhyypia.medium.com/amd-apu-how-to-modify-the-dedicated-gpu-memory-e27b75905056](url) but when I run this command _SA_OVERRIDE_GFX_VERSION=10.3.0 python test-rocm.py_
> 
> I get this message: _Command "python" not found. Maybe your meant: "python3" command from the deb package "python3". the "python" command from the deb package "python-is-python3"._
> 
> So I changed the command to _HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 test-rocm.py_
> 
> But I get this message now: _Traceback (most recent call last): File "/home/myUser/test-rocm.py", line 1, in import torch, grp, pwd, os, subprocess ModuleNotFoundError: No module named 'torch'_
> 
> I can't find any solution, and I'm not a programmer person.
> 
> **Thanks for your time!**

First of all, you need to make sure that you are
1. Running Linux (I personally prefer Ubuntu LTS but any major linux release would do)
2. You are running Ryzen APU, you can go to [AMD APU Website](https://www.amd.com/en/products/specifications/apu) and see if you can find your CPU

For PyTorch installation you need to check the PyTorch Official website. Here are the steps:

1. Go to [PyTorch Official Website](https://pytorch.org/get-started/locally/)
2. Scroll down a bit. You will see the widget like the one below
![image](https://github.com/ROCm/ROCm/assets/1215090/b34133a5-9574-49e8-aeca-c1efcb1b7dc3)
Just choose the option like the above image
3. You will get the command you need at the end. Then just copy and paste the command on your terminal. Then wait til the installation is completed
4. After PyTorch is installed, you can rerun the test script again

---

### 评论 #20 — gwyllion92 (2024-01-02T01:05:01Z)

> > > Yes I think the problem now is the torch-apu-helper shows that PyTorch could grab system memory from the system as video memory. However I think it still need more PyTorch API porting so we can say this way is PyTorch ready. Not sure AMD or PyTorch would make this possible in the future.
> > 
> > 
> > Hi, I'm trying to follow your guide [https://winstonhyypia.medium.com/amd-apu-how-to-modify-the-dedicated-gpu-memory-e27b75905056](url) but when I run this command _SA_OVERRIDE_GFX_VERSION=10.3.0 python test-rocm.py_
> > I get this message: _Command "python" not found. Maybe your meant: "python3" command from the deb package "python3". the "python" command from the deb package "python-is-python3"._
> > So I changed the command to _HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 test-rocm.py_
> > But I get this message now: _Traceback (most recent call last): File "/home/myUser/test-rocm.py", line 1, in import torch, grp, pwd, os, subprocess ModuleNotFoundError: No module named 'torch'_
> > I can't find any solution, and I'm not a programmer person.
> > **Thanks for your time!**
> 
> First of all, you need to make sure that you are
> 
>     1. Running Linux (I personally prefer Ubuntu LTS but any major linux release would do)
> 
>     2. You are running Ryzen APU, you can go to [AMD APU Website](https://www.amd.com/en/products/specifications/apu) and see if you can find your CPU
> 
> 
> For PyTorch installation you need to check the PyTorch Official website. Here are the steps:
> 
>     1. Go to [PyTorch Official Website](https://pytorch.org/get-started/locally/)
> 
>     2. Scroll down a bit. You will see the widget like the one below
>        ![image](https://private-user-images.githubusercontent.com/1215090/293612351-b34133a5-9574-49e8-aeca-c1efcb1b7dc3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQxNTUyMjIsIm5iZiI6MTcwNDE1NDkyMiwicGF0aCI6Ii8xMjE1MDkwLzI5MzYxMjM1MS1iMzQxMzNhNS05NTc0LTQ5ZTgtYWVjYS1jMWVmY2IxYjdkYzMucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MDEwMiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDAxMDJUMDAyMjAyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MDdjZjdmYTNlNjgzMGEwNDQyMTc3MGQ4OGMxZDFkZmE4YjFkMzU2MzYwMjU1MjI5Njk0NDJlNTEyZjVkZTkzYyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.Sci9x2SI3xvOmpY82FKL4XLMMQjVcbHlUta_Lg5GmiM)
>        Just choose the option like the above image
> 
>     3. You will get the command you need at the end. Then just copy and paste the command on your terminal. Then wait til the installation is completed
> 
>     4. After PyTorch is installed, you can rerun the test script again

Hi, thanks for your fast response.

I run the command and I get this message: 
_Checking ROCM support...
Cannot find rocminfo command information. Unable to determine if AMDGPU drivers with ROCM support were installed._

So that means that I'm stuck with 512mb vram? (My bios don't have the option to modify it ).

---

### 评论 #21 — winstonma (2024-01-02T03:41:08Z)

`rocminfo` exist only after AMD Graphic Driver is installed. You need to run the following command to install the AMD Driver

# Option 1
Here is the official installation guide from [AMD](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html#package-man-ubuntu). I think it should work for everybody

# Option 2

```bash
# Install AMD Driver
TEMP_FOLDER="/tmp"
TEMP_DRIVER_HTML="amd-driver.html"
DISTRO_CODENAME=$(lsb_release --codename --short)

# Find the package URL from AMD website
AMD_DRIVER_URL="https://www.amd.com/en/support/linux-drivers"
URL_RESPONSE=$(wget -U 'Mozilla/5.0' -qO- ${AMD_DRIVER_URL})
AMD_DEB_URL=$(echo $URL_RESPONSE | grep -o 'https://[^ "<]*.deb' | grep $DISTRO_CODENAME | head -1)
FILENAME=$(basename $AMD_DEB_URL)

# Download and install the driver package
wget -P $TEMP_FOLDER $AMD_DEB_URL
sudo dpkg -i $TEMP_FOLDER/$FILENAME
rm $TEMP_FOLDER/$FILENAME

amdgpu-install -y --usecase=rocm
```

After the AMD Graphic driver is installed, you can run the test script again. You can also find this snippet inside the document that I wrote.

By the way I suggest you running the following command first, I would like to ensure your APU could be supported

```bash
$ lscpu | grep "Model name"
```



---

### 评论 #22 — edt-xx (2024-01-02T14:57:03Z)

> It appears ROCm does not take into account dynamic VRAM GTT allocation on APUs (handled by amdkfd?).
> 
> For example on my system:
> 
> ```
> [    3.524465] [drm] amdgpu: 64M of VRAM memory ready
> [    3.524466] [drm] amdgpu: 15916M of GTT memory ready.
> ```
> 
> This means the iGPU could allocate up to 16GB of VRAM, however due to the small dedicated VRAM (64MB) that is _reserved_ for the iGPU, ROCm processes fail to allocate memory.
> 
> This also seems to propagate to OpenCL:

If you use the mesa rusticl opencl driver you will find that it uses the GTT memory as well as the VRAM.  



---

### 评论 #23 — gwyllion92 (2024-01-04T02:51:43Z)

> `rocminfo` exist only after AMD Graphic Driver is installed. You need to run the following command to install the AMD Driver
> 
> ```shell
> # Install AMD Driver
> TEMP_FOLDER="/tmp"
> TEMP_DRIVER_HTML="amd-driver.html"
> DISTRO_CODENAME=$(lsb_release --codename --short)
> 
> # Find the package URL from AMD website
> AMD_DRIVER_URL="https://www.amd.com/en/support/linux-drivers"
> URL_RESPONSE=$(wget -U 'Mozilla/5.0' -qO- ${AMD_DRIVER_URL})
> AMD_DEB_URL=$(echo $URL_RESPONSE | grep -o 'https://[^ "<]*.deb' | grep $DISTRO_CODENAME | head -1)
> FILENAME=$(basename $AMD_DEB_URL)
> 
> # Download and install the driver package
> wget -P $TEMP_FOLDER $AMD_DEB_URL
> sudo dpkg -i $TEMP_FOLDER/$FILENAME
> rm $TEMP_FOLDER/$FILENAME
> 
> amdgpu-install -y --usecase=rocm
> ```
> 
> After the AMD Graphic driver is installed, you can run the test script again. You can also find this snippet inside the document that I wrote.
> 
> By the way I suggest you running the following command first, I would like to ensure your APU could be supported
> 
> ```shell
> $ lscpu | grep "Model name"
> ```

Hi, after I run _amdgpu-install -y --usecase=rocm_  , I get this _WARNING: amdgpu dkms failed for running kernel_


---

### 评论 #24 — winstonma (2024-01-04T04:37:01Z)

I guess the reason the AMD Graphics Driver doesn't officially support default Ubuntu kernel or your kernel is too old. I think you should run the following step to install the latest default Ubuntu kernel:

```bash
sudo apt update
sudo apt install linux-generic-hwe-22.04
```

Then reboot your system, and wait for the GRUB boot menu comes up. Once in the GRUB menu, select the `Advanced options for Ubuntu` using the arrow keys and press Enter. Then select the default Ubuntu kernel (in my system it is `Ubuntu, with Linux 6.2.0-39-generic`).

Then go back to terminal and check what kernel is running on your system (this is my output to let you know what is the expected output):
```bash
$ awk -F\' '/menuentry / {print $2}' /boot/grub/grub.cfg 
Ubuntu
Ubuntu, with Linux 6.6.8-zabbly+
Ubuntu, with Linux 6.6.8-zabbly+ (recovery mode)
Ubuntu, with Linux 6.2.0-39-generic
Ubuntu, with Linux 6.2.0-39-generic (recovery mode)

Memory test (memtest86+x64.efi, serial console)
Windows Boot Manager (on /dev/nvme0n1p1)
UEFI Firmware Settings
```

The installed kernel is listed between Ubuntu and the extra line (so in my system it is `Linux 6.6.8-zabbly+` and `Linux 6.2.0-39-generic`, ignore the `recovery mode` option). If you see not only `Linux 6.2.0-39-generic` is installed, remove that kernel (please check [this guide](https://linuxconfig.org/how-to-remove-old-kernels-on-ubuntu) for reference.

The default system for installing AMD Graphic Driver should have the output similar to this:
```bash
$ awk -F\' '/menuentry / {print $2}' /boot/grub/grub.cfg 
Ubuntu
Ubuntu, with Linux 6.2.0-39-generic
Ubuntu, with Linux 6.2.0-39-generic (recovery mode)

Memory test (memtest86+x64.efi, serial console)
Windows Boot Manager (on /dev/nvme0n1p1)
UEFI Firmware Settings
```

Only one default Ubuntu kernel.

After you make sure everything is fine. Then reinstall the AMD Graphics Driver

```bash
amdgpu-uninstall
amdgpu-install -y --usecase=rocm
```

After AMD Graphic Card driver is installed. You can install back the kernel of your choice (or you can stick with the default kernel which is fine).

AMD driver developer always stated that their driver are tested (only) on the default system (specific version of Linux running the default kernel). Therefore installing or upgrading the AMD Driver is a pain on my ass because I am not using default kernel. I need to boot to the default kernel, remove the custom kernel, remove the old graphic driver, install the new graphic driver, install back the custom kernel, reboot back to the custom kernel. It's really painful.

---

### 评论 #25 — winstonma (2024-01-04T04:51:29Z)

> If you use the mesa rusticl opencl driver you will find that it uses the GTT memory as well as the VRAM.

Just wonder if Pytorch use GTT if I use the mesa rusticl opencl driver. If mesa rusticl opencl driver doesn't work with Pytorch don't use GTT then I still have to use this BIOS modification method to make Pytorch (or Stable Diffusion in my case) work.

---

### 评论 #26 — segurac (2024-02-17T20:42:42Z)

Hi, working on the great initiative of https://github.com/pomoke/torch-apu-helper
I have created this other code that would let us run any PyTorch code and force to use hipHostMalloc without changing a single line of code.

The way it works, it uses LD_PRELOAD to load the functions hipMalloc and hipFree before ROCm runtime and therefore is able to intercept those function calls and then forward them to hipHostMalloc and hipHostFree. hipHostMalloc uses GTT memory and there's no need to change VRAM in the BIOS.

`LD_PRELOAD=./libforcegttalloc.so  HSA_OVERRIDE_GFX_VERSION=9.0.0 python your_pytorch_python_script.py`

Check the code if you think it may be useful.
https://github.com/segurac/force-host-alloction-APU



---

### 评论 #27 — DocMAX (2024-02-25T22:15:51Z)

Doesn't work on ollama :-(

---

### 评论 #28 — pappacena (2024-04-02T01:20:19Z)

@segurac great job! I've done some tests, and your memory allocator worked quite well!

To make it easier for future travellers, I've created this [PyPI package](https://pypi.org/project/pytorch-rocm-gtt/) with your code, so anyone can overcome the memory limitation by running this:

```
!pip install pytorch_rocm_gtt
import pytorch_rocm_gtt
pytorch_rocm_gtt.patch()
```

After that, I'm able to allocate way more than the 512MB dedicated to my Radeon 760M iGPU with something like this:
```
>>> torch.rand(1024 * 1024 * 600, dtype=torch.float32, device="cuda") * 10000
tensor([5880.2114, 1243.6473, 3648.3640,  ..., 3309.8118, 6534.8770,
        6562.5479], device='cuda:0')
```

---

### 评论 #29 — DerRehberg (2024-04-13T08:45:03Z)

Can someone give me a command line tutorial to use more than 2GB with Stable Diffusion? I managed to run it and it almost generated the picture. But I only got 2GB of VRAM and it doesn't have enough video memory to finish the picture. I'm alreadys thinking about download windows to allocate more if possible. It stops right before I can see the finished images.  Newbie on Arch here, I'm happy than I can run Ollama with APU Support, would love Stable Diffusion too. My System seems to use almost 1 GB of it, even after a blank restart.

---

### 评论 #30 — winstonma (2024-04-13T09:24:16Z)

@DerRehberg Which CPU are you running? Could you print the result of the following command? This is the output from my system:

```
$glxinfo -B
...
Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 512 MB
    Total available memory: 8126 MB
    Currently available dedicated video memory: 57 MB
...
```

---

### 评论 #31 — DerRehberg (2024-04-13T09:37:34Z)

@winstonma 
Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 2048 MB
    Total available memory: 12977 MB
    Currently available dedicated video memory: 1531 MB


AMD Ryzen 7 5825U

Currently testing generating in CPU Mode, but it's 30 times slower, atleast it feels like it

---

### 评论 #32 — winstonma (2024-04-13T09:53:15Z)

@DerRehberg Based on your output your system I think you dedicated 2GB of memory to BIOS. Could you check one more thing? I would like to see the GTT memory allowed.

```
$ sudo dmesg | grep amdgpu | grep drm
[    3.929856] [drm] amdgpu kernel modesetting enabled.
[    3.954417] [drm] amdgpu: 512M of VRAM memory ready
[    3.954419] [drm] amdgpu: 7614M of GTT memory ready.
[    4.271639] [drm] Initialized amdgpu 3.57.0 20150101 for 0000:03:00.0 on minor 0
[    4.283886] fbcon: amdgpudrmfb (fb0) is primary device
[    5.698795] amdgpu 0000:03:00.0: [drm] fb0: amdgpudrmfb frame buffer device
```

I think you need to first disable the dedicated memory. Please use feel free to read [Unlocking GPU Memory Allocation on AMD Ryzen™ APU? - Prepare the bootable USB drive](https://medium.com/p/e27b75905056#3fc7) then go to the next section and set it back to AUTO
- Go to Device Manager→AMD CBS→NBIO Common Option→GFX Configuration
- In Integrated Graphics Controller, select `Auto` (I am not sure the correct wording but don't use `Force`)
- In UMA Mode, select `Auto` (I am not sure the correct wording but don't use `UMA_SPECIFIED`)

After set it back to auto then you can use [force-host-alloction-APU](https://github.com/segurac/force-host-alloction-APU) with Pytorch to run stable diffusion on your Graphic Card.

Please leave message if you still have question.

---

### 评论 #33 — DerRehberg (2024-04-13T10:34:20Z)

@winstonma 
Can you give me a detailed instruction how to use force-host-alloction-apu on arch with stable diffusion?

[    5.278774] [drm] amdgpu kernel modesetting enabled.
[    5.392349] [drm] amdgpu: 2048M of VRAM memory ready
[    5.392352] [drm] amdgpu: 10929M of GTT memory ready.
[    6.617177] [drm] Initialized amdgpu 3.57.0 20150101 for 0000:03:00.0 on minor 1
[    6.624152] fbcon: amdgpudrmfb (fb0) is primary device
[    6.667498] amdgpu 0000:03:00.0: [drm] fb0: amdgpudrmfb frame buffer device
[ 1557.803120]  amdgpu_drm_ioctl+0x4e/0x90 [amdgpu]
[ 1557.803120]  amdgpu_drm_ioctl+0x4e/0x90 [amdgpu]

I wouldn't even know how to compile

---

### 评论 #34 — winstonma (2024-04-13T10:49:55Z)

@DerRehberg I think you should have 10GB of memory. But you better 

```bash
# Replace your PyTorch CPU version with PyTorch ROCm version
$ pip uninstall torch torchvision torchaudio
$ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7

# Go to your Stable Diffusion folder

# Compile the library
$ git clone https://github.com/segurac/force-host-alloction-APU.git
$ CUDA_PATH=/usr/ HIP_PLATFORM="amd" hipcc force-host-alloction-APU/forcegttalloc.c -o force-host-alloction-APU/libforcegttalloc.so  -shared -fPIC
$ sudo mv force-host-alloction-APU/libforcegttalloc.so /usr/local/lib
$ rm -rf force-host-alloction-APU

# Check your HSA_OVERRIDE_GFX_VERSION value
$ rocminfo | grep gfx
  Name:                    gfx1030                            
      Name:                    amdgcn-amd-amdhsa--gfx1030    

# Run stable diffusion (Please update HSA_OVERRIDE_GFX_VERSION based on the previous output)
$ LD_PRELOAD=libforcegttalloc.so HSA_OVERRIDE_GFX_VERSION=10.3.0 python launch.py
```

---

### 评论 #35 — DerRehberg (2024-04-13T10:51:49Z)

@winstonma Pip uninstall says I should use the AUR xd
Also I've set my GFX Version already in /etc/enviroments
also




LD_PRELOAD=libforcegttalloc.so python launch.py
ERROR: ld.so: object 'libforcegttalloc.so' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
ERROR: ld.so: object 'libforcegttalloc.so' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
ERROR: ld.so: object 'libforcegttalloc.so' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
Python 3.11.8 (main, Feb 12 2024, 14:50:05) [GCC 13.2.1 20230801]
Version: v1.9.0
Commit hash: adadb4e3c7382bf3e4f7519126cd6c70f4f8557b
Installing clip
Traceback (most recent call last):
  File "/home/vacanickel/stable-diffusion-webui/launch.py", line 48, in <module>
    main()
  File "/home/vacanickel/stable-diffusion-webui/launch.py", line 39, in main
    prepare_environment()
  File "/home/vacanickel/stable-diffusion-webui/modules/launch_utils.py", line 393, in prepare_environment
    run_pip(f"install {clip_package}", "clip")
  File "/home/vacanickel/stable-diffusion-webui/modules/launch_utils.py", line 143, in run_pip
    return run(f'"{python}" -m pip {command} --prefer-binary{index_url_line}', desc=f"Installing {desc}", errdesc=f"Couldn't install {desc}", live=live)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vacanickel/stable-diffusion-webui/modules/launch_utils.py", line 115, in run
    raise RuntimeError("\n".join(error_bits))
RuntimeError: Couldn't install clip.
Command: "/usr/bin/python" -m pip install https://github.com/openai/CLIP/archive/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip --prefer-binary
Error code: 1
stderr: ERROR: ld.so: object 'libforcegttalloc.so' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
ERROR: ld.so: object 'libforcegttalloc.so' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try 'pacman -S
    python-xyz', where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Arch-packaged Python package,
    create a virtual environment using 'python -m venv path/to/venv'.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip.
    
    If you wish to install a non-Arch packaged Python application,
    it may be easiest to use 'pipx install xyz', which will manage a
    virtual environment for you. Make sure you have python-pipx
    installed via pacman.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.


---

### 评论 #36 — DerRehberg (2024-04-13T14:23:44Z)

@winstonma Why can't it load libforcegttalloc?

EDIT: Got it working by using the full path, but it crashes my whole apu, my kde desktop and stable diffusion
HW Exception by GPU node-1 (Agent handle: 0x632d71637310) reason :GPU Hang

Any Fix?



---

### 评论 #37 — pappacena (2024-04-13T14:43:32Z)

@DerRehberg I also have this exact random "GPU Hang" while testing mistral-7b (including my KDE crashing). One thing that helped *a little bit* was increasing the dedicated memory in BIOS (I can only increase to 2GB, and mistral-7b uses way more than that, but libforcegttalloc allows the extra allocation).

I still have this crash some times, but it appears to be less frequent this way.

---

### 评论 #38 — winstonma (2024-04-13T15:18:35Z)

@DerRehberg @pappacena Do you think replacing the `/lib/firmware` with latest version would help? ([instruction](https://tutorialforlinux.com/2022/12/21/how-to-update-linux-firmware-on-ubuntu-22-04-guide/2/)). At least my laptop get smooth VP9 decode and sleep of death problem is gone after updating the firmware folder. So I personally think it's worth to try.

---

### 评论 #39 — DerRehberg (2024-04-13T15:20:55Z)

@winstonma I think my firmware is actually up to date
@pappacena My Stable Diffusion crashes but Ollama works with it

---

### 评论 #40 — winstonma (2024-04-13T22:41:23Z)

The system [firmware](https://wiki.ubuntu.com/Kernel/Firmware) (including wifi/bluetooth/chipset) is different from the firmware of the motherboard. I would recommend you to take a look. It fixes several problems of my laptop after me not using the [linux-firmware](https://packages.ubuntu.com/jammy-updates/linux-firmware) (which is 2 years old on Ubuntu Jammy) comes from the system and use the git version. I think there are some advantage using the latest linux-firmware and kernel but still it is up to you.

---

### 评论 #41 — DerRehberg (2024-04-14T06:05:55Z)

I use Arch @winstonma 

---

### 评论 #42 — pomoke (2024-04-14T15:50:44Z)

Use ROCm 5.7 for Vega-based iGPUs. Versions from ROCm 6.0 will break things as they dropped support for GCN without explicit error message.

---

### 评论 #43 — DerRehberg (2024-04-27T17:08:54Z)

Well ROCM works with any Software I can imagine on my APU with Version 6. But Stable Diffusion just plainly nicely gives me an out of memory error @pomoke 

---

### 评论 #44 — winstonma (2024-04-28T07:44:07Z)

@DerRehberg It is just a distracting story.

I just installed Ubuntu 24.04 and find out I don't need to install AMD ROCm Driver in order to get everything working.

I also checked your system and it seems to me that you also don't need to install AMD ROCm Driver. It seems to me that you only need to install [hip-runtime-amd](https://archlinux.org/packages/extra/x86_64/hip-runtime-amd/files/), compile force-host-allocation and everything should be working without the need of ROCm Driver.

---

### 评论 #45 — DerRehberg (2024-04-30T08:40:51Z)

@winstonma Well I got that package installed. Still crashes on me

---

### 评论 #46 — winstonma (2024-04-30T16:38:23Z)

@DerRehberg Yeah this is a distracting story. As I guessed it wouldn't fix your problem but it would make the installation easier as it no longer need to install graphic driver.

BTW I find this [article](https://qiita.com/asfdrwe/items/7ba1aa2251b3e34c9f8a) which the user run Stable Diffusion on Ryzen 5600G. I think Google Translate would be your friend.

---

### 评论 #47 — DerRehberg (2024-05-01T13:35:47Z)

@winstonma Google Translate Page doesn't support Japanese. And honestly. I just generate with my fucking cpu because I don't care anymore. If I use forcegtt my whole system crashes with stable diffusion

---

### 评论 #48 — DerRehberg (2024-05-01T13:53:23Z)

@winstonma I found an english article, I would love to try it but at the checking script if rocm works I get an libtorch_cpu error. When Updating torchvision-rocm i also get an error: ImportError: /usr/lib/libtorch_cpu.so: undefined symbol: cblas_gemm_f16f16f32

Idk if anything is fucked up rn

---

### 评论 #49 — DerRehberg (2024-05-05T10:58:29Z)

@winstonma Found it out. I only need to downgrade hip-runtime-amd to 5.7.1 and Stable Diffusion works with libforcegtt even tho the rest is at 6

---

### 评论 #50 — winstonma (2024-05-05T13:33:55Z)

Great to hear. That matched my experience on Ubuntu 24.04 too. No need to install ROCm package and DKMS modules. To me using the new way doesn't provide any performance benefit, just easier installation.

Just wonder if it fix the problem you faced?

 

---

### 评论 #51 — DerRehberg (2024-05-08T11:17:24Z)

@winstonma Well I tried downgrading all packages to 5.7.1 and it crashed on me. Updating everything except runtime worked for me, idk why tho

---

### 评论 #52 — winstonma (2024-05-26T02:20:20Z)

Just saw [Linux 6.10 Improves AMD ROCm Compute Support For "Small" Ryzen APUs](https://www.phoronix.com/news/Linux-6.10-AMDKFD-Small-APUs). Although @segurac patch works flawlessly, I still think the AMD should provide native support. Hopefully using 6.10 would no longer require additional library. 

EDIT: Just ran Linux Kernel 6.10-rc1 on my 6800U laptop. As expected I can run stable diffusion without using custom mod like [force-host-alloction-APU](https://github.com/segurac/force-host-alloction-APU) or BIOS modification. AMD eventually fix this problem!

---

### 评论 #53 — Snuupy (2024-07-21T23:57:37Z)

@winstonma which distro are you using?

> EDIT: Just ran Linux Kernel 6.10-rc1 on my 6800U laptop. As expected I can run stable diffusion without using custom mod like [force-host-alloction-APU](https://github.com/segurac/force-host-alloction-APU) or BIOS modification. AMD eventually fix this problem!



---

### 评论 #54 — winstonma (2024-07-22T02:00:00Z)

@Snuupy I am using Ubuntu 24.04.

By the way Linux 6.9.9 backported this feature already (You can check commit 8d656c in the [changelog](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.9.9)). The default kernel of Ubuntu 24.04 is 6.8 but I upgraded the kernel using Zabbly kernel, you can follow [this instruction](https://ubuntuhandbook.org/index.php/2023/11/linux-kernel-6-6-ubuntu-2204-2004/) to install kernel. It works on the previous version of Ubuntu LTS too.

FYI Linux Kernel 6.10 has a [green block while playing video bug](https://gitlab.freedesktop.org/drm/amd/-/issues/3437) on my device so I am still using 6.9 right now.

---

### 评论 #55 — Snuupy (2024-07-22T02:46:10Z)

@winstonma Thank you for such an informative reply! I didn't know Zabbly 6.9.9 backported this, thanks! I will try upgrading my kernel 😄 

Also, I didn't know rocm worked on 24.04, I thought rocm was only officially supported on LTS releases?

Looks like the latest kernel on Zabbly is 6.9.10 on my 22.04 LTS install. Downloading from HF now...

---

### 评论 #56 — winstonma (2024-07-22T03:20:43Z)

@Snuupy After the kernel support I no longer need to install AMD Driver. I guess you could try uninstall the driver and reinstall the driver if anything doesn't work for you.

As it takes time for the driver team to test on distro, I think it make sense for them to support only on LTS release. But again on Ubuntu 24.04 I didn't install AMD Driver. I only install latest 6.9 kernel and everything just work.

By the way if you want to improve the performance there is a small trick, you can use [RyzenAdj](https://github.com/FlyGoat/RyzenAdj) to adjust the `vrmmax-current`. I use my AMD 6800U as an example. The default value is 90mA but I changed it to 105mA. After that I could get 10-15% increase in stable diffusion. You can try that too.

---

### 评论 #57 — Snuupy (2024-07-22T04:46:24Z)

@winstonma I just installed the 6.9.10 kernel on my 22.04 LTS machine. In my BIOS for my UM780 (7840HS) I set VRAM to 16GB. In `amdgpu_top` I see: `VRAM: 16384 MiB` and `GTT: 23984 MiB`.

I am testing this model, 27B (29 GiB) https://huggingface.co/bartowski/Big-Tiger-Gemma-27B-v1-GGUF/resolve/main/Big-Tiger-Gemma-27B-v1-Q8_0.gguf in ollama/open-webui

I originally thought it would max out the VRAM and then use GTT (~16GB in VRAM, say the remaining ~13GB in GTT allocation). Instead however, I am seeing this:

```
ollama       | llm_load_tensors: offloading 22 repeating layers to GPU
ollama       | llm_load_tensors: offloaded 22/47 layers to GPU
ollama       | llm_load_tensors:      ROCm0 buffer size = 12624.05 MiB
ollama       | llm_load_tensors:        CPU buffer size = 27591.06 MiB
```

Where the ~12GB is loaded into GTT and VRAM usage is still at 0. Is this expected and what you see as well when you load your models?

Do you think I would benefit from changing the BIOS VRAM to say, 512 MB/1GB? It looks like GTT allocation size is 0.5*(RAM-VRAM) size.

Edit: This may be an Ollama issue: https://github.com/ollama/ollama/issues/5471

---

### 评论 #58 — winstonma (2024-07-22T10:25:43Z)

@Snuupy I think you can set your VRAM to AUTO (and by default it should be 512MB). If there is no AUTO option then you might need to follow [this article](https://winstonhyypia.medium.com/amd-apu-how-to-modify-the-dedicated-gpu-memory-e27b75905056) to create a bootable USB thumb drive, boot the system using USB thumb drive, and then go to Device Manager→AMD CBS→NBIO Common Option→GFX Configuration and set the Integrated Graphics Controller value to AUTO.

Also the max GTT memory would be half of your system memory. But I think you can change the value (please check [this comment](https://github.com/pytorch/pytorch/issues/107605#issuecomment-2178940189) for more information). I never try that so please contact the commenter if that doesn't work.

Lastly you can check the amount GTT memory by running the command:
```bash
$ sudo dmesg | grep 'amdgpu.*memory'
[    4.828206] [drm] amdgpu: 512M of VRAM memory ready
[    4.828209] [drm] amdgpu: 7614M of GTT memory ready.
```

And this is the output from my laptop. If you set your BIOS VRAM to AUTO then you should also see that the output of the above VRAM value is 512M.

---

### 评论 #59 — nikelborm (2025-02-04T23:33:47Z)

@Vuepress-hue1 seems like the actual source (not AI crap): https://stackoverflow.com/questions/34233853/im-trying-to-read-a-line-from-a-file-in-c-and-dynamically-allocate-memory-but-t

UPD: which is not in any way relevant to the issue itself as I found out only after I wrote my response to the bot above

---
