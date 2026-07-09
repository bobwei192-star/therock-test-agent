# Doesn't ROCm support AMD's integrated GPU (APU)?

- **Issue #:** 2216
- **State:** closed
- **Created:** 2023-06-02T10:37:03Z
- **Updated:** 2025-12-11T06:58:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/2216

I have an AMD Ryzen 5 5600G processor which has an integrated GPU, and I do not have a separate graphics card. Am using `Linux Mint 21` Cinnamon.  
I installed PyTorch with this command `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2
` and according to posts on a forum, running the following command is supposed to tell me if PyTorch can use ROCm to perform CUDA equivalent processing.  
```
import torch.cuda
print(f'CUDA available? : {torch.cuda.is_available()}')
```
The output is `False`.  
   
PyTorch redirects people to this repository's readme page to check for compatible GPU information, but I didn't see any. So for the sake of anyone searching for this info:  
1. Could you publish a list of what hardware you support and which can be used with PyTorch or any other deep learning library, as an alternative to CUDA?  
2. Could you please support integrated GPU's? Mine is supposed to be as powerful as an NVidia GT 1030. When it is so powerful, it just isn't right to expect Users to purchase a separate graphics card. I do hope ROCm bridges NVidia's monopoly on CUDA.  
  
---
**Update:** Tried [this script](https://gist.github.com/damico/484f7b0a148a0c5f707054cf9c0a0533) too, but the output is 
```
Checking ROCM support...
Cannot find rocminfo command information. Unable to determine if AMDGPU drivers with ROCM support were installed.
```  
Tried installing ROCm via instructions on [this](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.1/page/How_to_Install_ROCm.html) page (tried with the `deb` file for bionic and focal).  
On running `sudo rocminfo`, I get:  
```
ROCk module is loaded
Segmentation fault
```
On running `rocminfo`:  
```
ROCk module is loaded
Unable to open /dev/kfd read-write: Permission denied
navin is not member of "render" group, the default DRM access group. Users must be a member of the "render" group or another DRM access group in order for ROCm applications to run successfully.
```
 [This script](https://gist.github.com/damico/484f7b0a148a0c5f707054cf9c0a0533) now outputs:  
```
Checking ROCM support...
BAD: No ROCM devices found.
Checking PyTorch...
GOOD: PyTorch is working fine.
Checking user groups...
Cannot find rocminfo command information. Unable to determine if AMDGPU drivers with ROCM support were installed.
```
