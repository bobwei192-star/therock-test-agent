# [Issue]: Memory access fault by GPU node-2 (Agent handle: 0x5640a8bb1980) on address 0x7feea09c5000. Reason: Page not present or supervisor privilege.

- **Issue #:** 2804
- **State:** closed
- **Created:** 2024-01-12T21:34:41Z
- **Updated:** 2024-09-17T17:48:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/2804

###LOOK TO MY LAST COMMENT
I do believe those will be the outputs you need, and might be more useful

### Problem Description

Happens after running about 6-10 iterations of any of the latter python scripts, essentially if im doing something with the gpu i figure it is only a matter of time before it throws, i havent tested it but im guessing there is likely possiblity, Ive tried quite a few things as well. I know that inherently this may not be a rocm issue, but i think w.e is going on with the gpu is in your ballpark of knowing how to fix.

```
Memory access fault by GPU node-2 (Agent handle: 0x5640a8bb1980) on address 0x7feea09c5000. Reason: Page not present or supervisor privilege.

Unable to open /dev/kfd read-write: Invalid argument
admin is member of render group
```

Note: I have been running this setup for over a week now testing and carrying on and before I did what I did, i had generated 200 images roughly, with no issues at all and all the images were good. 

### Operating System

Fedora 39 && CentOS 7

### CPU

AMD Ryzen Threadripper 1900X 8-Core Processor

### GPU

AMD Radeon RX 6750

### Other

Docker

### ROCm Version

ROCm 5.6.0

### ROCm Component

ROCm

### Steps to Reproduce

cmds are in additional information

1. run docker: this happens in a fresh container aswell, installed as supplied
2. login as user, run script, any of them after the initial point of this issue happen
3. after the script is running and through...(6-10 iterations? i realized thats about how many it would have been at when i ran the cmd) a few iterations, in another tty run ```sudo docker attach```

What have I done since, and during:

After This happened it locked up both ttys, but they were joined, i could type and the stdio of both seemed to have been linked. typed in one is showed on the other,  with formatting, ie, enter, table, etc all seem to work, i hit ctrl-c a bunch of times and ^C showed up on both. 

I went back to the host sytem and tried to kill the container, which didnt work
I tried to kill docker, and it also would work
**nothing fancy here docker image kill <id> && systemctl stop docker

when i tried to run rocminfo thats where the kfd error came from

this is when i figured there was something stuck in memory and maybe a reboot would be enough to get it to free up, so i from a terminal restarted. The computer froze at some point in the shutdown, resulting in a hard boot. It came back just fine, I started docker all the same ways as supplied, logged in, enter the python env, and ran the script, but now I was getting those dreaded out of memory issues. which i wasnt getting before. given i had run this several hundred times. 

after messing around with it, trying to change cmd line args, and the script, i decided maybe a proper reboot would be enough, the gpus are visable, rocminfo is working, torch and cuda and see the gpus, so i rebooted, without failure in the shutdown

**the system wont shut down after this happens

the issue presisted there after, eventually i figured out that if i run the base script, it seems that my OOM issues go away and i can run all three scripts, but after they are ran 6-10 times the Fault Error Happens.

after that i sout help online to find a mention on here about 

```
export HCC_SERIALIZE_KERNEL=0x3
export HCC_SERIALIZE_COPY=0x3
export HIP_TRACE_API=0x2
[then re-run your application]

More tips are listed here: https://rocm-documentation.readthedocs.io/en/latest/Other_Solutions/Other-Solutions.html
```
OH WAIT i never tried it after i got the system stable only after the issue happens.(going to do this after i post this)

but there wont even run... it cant find ANY gpus(there are two and the second one still does register properly on rocm-smi, this is after the error as I have managed to get things to close out and be killed without rebooting

![Screenshot](https://github.com/ROCm/ROCm/assets/32893554/bed3af67-0de7-44a4-bc35-0b20bfb166d6)

The next step was a complete reinstall of the docker setup on centos, again supplied in additional
only to produce the same issues(minus OOM) everything works mint for abotu 6-10 iterations then it faults


I will be trying my scripts here before long targetting my second gpu and see if the issues are on both gpus are just one(i was only using one at the time this started)

I will also run the suggestion from the other post with a stable system and see if that does anything and will post the results

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    41029664(0x2721020) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    41029664(0x2721020) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    41029664(0x2721020) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3800                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    41262736(0x2759e90) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    41262736(0x2759e90) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    41262736(0x2759e90) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 3                  
*******                  
  Name:                    gfx1031                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 6750 XT              
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      3072(0xc00) KB                     
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29663(0x73df)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2880                               
  BDFID:                   2816                               
  Internal Node ID:        2                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 115                                
  SDMA engine uCode::      80                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1031         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*******                  
Agent 4                  
*******                  
  Name:                    gfx1031                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 6750 XT              
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    3                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      3072(0xc00) KB                     
    L3:                      98304(0x18000) KB                  
  Chip ID:                 29663(0x73df)                      
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2880                               
  BDFID:                   17408                              
  Internal Node ID:        3                                  
  Compute Unit:            40                                 
  SIMDs per CU:            2                                  
  Shader Engines:          2                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 115                                
  SDMA engine uCode::      80                                 
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GLOBAL; FLAGS:                     
      Size:                    12566528(0xbfc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 3                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1031         
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done *** 
```

### Additional Information

```
echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";

OS:
NAME="Fedora Linux"
VERSION="39 (Thirty Nine)"
```

```
echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;

CPU: 
model name	: AMD Ryzen Threadripper 1900X 8-Core Processor
```

```
GPU:
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Marketing Name:          AMD Ryzen Threadripper 1900X 8-Core Processor
  Name:                    gfx1031                            
  Marketing Name:          AMD Radeon RX 6750 XT              
      Name:                    amdgcn-amd-amdhsa--gfx1031         
  Name:                    gfx1031                            
  Marketing Name:          AMD Radeon RX 6750 XT              
      Name:                    amdgcn-amd-amdhsa--gfx1031 

```


Commands Run on a Base Docker File with the docker cmd to start container & to run script
```
yum update -y
sudo yum install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm
yum install -y rocm-info make gcc openssl-devel bzip2-devel libffi-devel sudo python-virtualenv conda

curl -O https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
tar -xf Python-3.8.10.tgz 
rm !$
mv Python-3.8.10 /opt
cd /opt/Python-3.8.10

./configure --enable-optimizations
make altinstall

useradd -m admin
usermod -aG wheel admin
usermod -aG video admin
passwd admin

su - admin

conda create --name pytorch-env python=3.8.10
conda activate pytorch-env

conda install -c conda-forge cudatoolkit=11.3
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.6/

python -c 'import torch; print(torch.cuda.is_available())'
python -c 'import torch; print(torch.cuda.device_count())'

########################################################################
### This is for sd-xl ^^^ above is just for pytorch-rocm
#########################################################################
yum install mesa-libGLw
pip install --upgrade --upgrade-strategy only-if-needed accelerate transformers diffusers einops pytorch_lightning omegaconf opencv-python

#run my script (gc)
garbage_collection_threshold:0.6,max_split_size_mb:256
PYTORCH_CUDA_ALLOC_CONF=garbage_collection_threshold:0.9,max_split_size_mb:128 HSA_OVERRIDE_GFX_VERSION=10.3.0 python script.py

########################################################################
### Docker stuff
#########################################################################

##starts container from image(with opens)
sudo docker run -it --mount type=bind,source=./stable-diffusion-xl-base-1.0,target=/home/admin/sd-xl-1.0 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host <image_id>
```

Python Script Running at failure
```
import torch
import random
import gc
from diffusers import StableDiffusionXLPipeline, StableDiffusionXLImg2ImgPipeline
from diffusers.utils import load_image
from pathlib import Path
from datetime import datetime
import os

generator = torch.Generator("cuda")
generator.seed()
pipe = StableDiffusionXLPipeline.from_pretrained(
    "./", torch_dtype=torch.float16
)

refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "./",
    torch_dtype=torch.float16,
    text_encoder_2=pipe.text_encoder_2,
    vae=pipe.vae,
    variant="fp16"
)

img_name = "some_set"

prompt = "something"
prompt_2 = "something else"
n1 = "something negitive"
n2 = "something else negitive"

pipe.enable_model_cpu_offload()
refiner.enable_model_cpu_offload()

print("GENERATING PICTUREs:___________________________________________________________________________")
for i in range(200):
    print(f'IMAGE:{i}; ________________________________________________________________________START::')

    image = pipe(
        prompt, prompt_2, negitive_prompt=n1, negitive_prompt_2=n2, guidance_scale=9.5,
        num_inference_steps=50, denoising_end=0.6, output_type="latent", generator=generator
    ).images

    image = refiner(prompt, prompt_2, negitive_prompt=n1, negitive_prompt_2=n2, image=image,
        num_inference_steps=50, denoising_start=0.6).images
    
    dir = f'../{img_name}'
    if not os.path.exists(f'{dir}'):
        os.makedirs(f'{dir}')

    now = datetime.now()
    time_stamp = now.strftime("%m_%d_%Y_%H_%M_%S")
    image[0].save(f'../{img_name}/{img_name}{time_stamp}.png')

    torch.cuda.empty_cache()
    gc.collect()    

    print(f'IMAGE:{i}; ________________________________________________________________________END::')

```

Basic Sdxl Pipeline script
```
import torch
import gc
from diffusers import StableDiffusionXLPipeline, StableDiffusionXLImg2ImgPipeline
from diffusers.utils import load_image

pipe = StableDiffusionXLPipeline.from_pretrained(
    "./", torch_dtype=torch.float16
)

refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "./",
    torch_dtype=torch.float16,
    text_encoder_2=pipe.text_encoder_2,
    vae=pipe.vae,
    variant="fp16"
)

pipe.enable_model_cpu_offload()
refiner.enable_model_cpu_offload()

prompt = "a photo of an astronaut riding a horse on mars, photo realistic, 4k"
prompt_2 = ""
n1 = "bad quality, cartoon, painting, blurry, blurry faces"
n2 = ""

image = pipe(prompt, prompt_2, negitive_prompt=n1, negitive_prompt_2=n2, guidance_scale=9.5, num_inference_steps=50).images[0]

image.save("../img.png")

```

Basic Base+Refiner Pipeline
```
import torch
import gc
from diffusers import StableDiffusionXLPipeline, StableDiffusionXLImg2ImgPipeline
from diffusers.utils import load_image

pipe = StableDiffusionXLPipeline.from_pretrained(
    "./", torch_dtype=torch.float16
)

refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "./",
    torch_dtype=torch.float16,
    text_encoder_2=pipe.text_encoder_2,
    vae=pipe.vae,
    variant="fp16"
)

pipe.enable_model_cpu_offload()
refiner.enable_model_cpu_offload()

prompt = "a photo of an astronaut riding a horse on mars, photo realistic, 4k"
prompt_2 = ""
n1 = "bad quality, cartoon, painting, blurry, blurry faces"
n2 = ""

image = pipe(prompt, prompt_2, negitive_prompt=n1, negitive_prompt_2=n2, guidance_scale=9.5, num_inference_steps=50, denoising_end=0.8, output_type="latent").images

image = refiner(prompt, prompt_2, negitive_prompt=n1, negitive_prompt_2=n2, image=image, num_inference_steps=50, denoising_start=0.8).images[0]

image.save("../img.png")

```