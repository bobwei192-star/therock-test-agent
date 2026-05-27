# DaVinci Resolve (since ROCm 2.2)

> **Issue #768**
> **状态**: closed
> **创建时间**: 2019-04-14T18:32:38Z
> **更新时间**: 2024-08-15T14:14:53Z
> **关闭时间**: 2024-08-15T14:10:23Z
> **作者**: beatboxa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/768

## 描述

ROCm 2.3 appears not to work with DaVinci Resolve, where 2.2 seems to have worked.  Launching with 2.3 seems to cause a segmentation fault.  (Note:  Other software works fine with ROCm 2.3).

See [this](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=56878&start=1400#p498899) post, describing ROCm 2.3 failing for DaVinci Resolve.

See [this](https://youtu.be/nuXsElMbtmI?t=803) for ROCm 2.2 working for DaVinci Resolve with linux-kernel 4.18.  Also note that this user only installed the rocm-utils package (which includes OpenCL), while the documentation recommends installing rocm-dev for only OpenCL.  However, installing rocm-dev in ROCm 2.2 prevented my linux-kernels 4.18 - 5.0 from booting.  I was unaware that this entire package was not needed.

_Unfortunately, the Debian repositories seem to have removed the older versions, making it difficult to revert to 2.2 on Debian-based systems like Ubuntu (where normally one could just select an older version from an installer)._  **(Updated:  See below)**

My requests are:

1. Please update the documentation to remove the step of installing rocm-dev for OpenCL-only installations.
2. _Please provide the older ROCm 2.2 in the debian respositories for users who wish to easily control, revert, and test various versions with various software_  **(Updated:  See below)**
3. Please identify and fix the root cause of DaVinci Resolve failing to work with ROCm 2.3

Note:
For testing, Davinci Resolve can be downloaded for free from their website [here](https://www.blackmagicdesign.com/support/).

It is designed for red-hat-based systems; but it can be easily installed on Debian-based systems (like Ubuntu), using [these instructions](http://www.danieltufvesson.com/makeresolvedeb).

---

## 评论 (48 条)

### 评论 #1 — beatboxa (2019-04-15T14:48:30Z)

For anyone with a similar issue, I was able to figure out a temporary solution on my own:

After some exploring in my browser, I found the second repository:
`http://repo.radeon.com/rocm/apt/2.2/`
(As opposed to http://repo.radeon.com/rocm/apt/debian/      Note that "2.2" replaces "debian" in the directory structure)

So I added this to my sources.  I now have both sources.

Then, I used Synaptic Package Manager to downgrade all opencl packages (under rocm-utils) to version 2.2.  To do this, I first viewed the properties of each package, got a list of dependencies (other packages that would also need to be downgraded), and then downgraded those packages.  Only the OpenCL packages required downgrading.  Afterwards, I rebooted.

DaVinci Resolve now works.  I also checked other applications like Darktable:  they work too.

This is a temporary workaround, since version 2.3 still crashes DaVinci Resolve and the instructions could be further improved.

---

### 评论 #2 — walterav1984 (2019-04-16T06:46:37Z)

Good to hear you got DR16 working in the past with rocm still trying the same on Debian Buster.

Could you post what version of AMDGPU driver "kernel boot arguments" you are using, and if you installed some AMDGPU pro extra's or PPA's with newer mesa/driver?

Its still unclear to me if DR15 was working fine with rocm 2.2 and or 2.3 but only DR16beta is not working with rocm 2.3 or also broken on rocm 2.2?

---

### 评论 #3 — beatboxa (2019-04-16T08:52:02Z)

I am not KristijanZic at bmd forum, but I did find that user's posts very informative.  And I am using DaVinci Resolve 16-beta.  This was the first time I tried to get DR working, because of the ROCm update that would work with kernel 4.18.  My previous attempt at installing ROCm prevented my system from booting (I think due to dkms).

But for clarity, here is what I tested the past few days:
-DR15 + ROCm 2.3 (didn't work)
-DR16 + ROCm 2.3 (didn't work)
-DR16 + ROCm 2.2 (works)

Earlier today, I also tried ROCm 2.3 once again, and DR16 hung again.  With no other changes, by reverting to ROCm 2.2, DR16 worked again.  The complete list of rocm package versions that I am currently using (which work properly) are:
- rocm-clang-ocl (0.4.0-7ce124f)
- rocm-opencl (1.2.0-2019030702)
- rocm-opencl-dev (1.2.0-2019030702)
- rocm-utils (2.2.31)
- rocminfo (1.0.0)

I'd recommend that you use Synaptic package manager to confirm or install these specific versions.

I'm happy to provide what I can to help debug, though I should warn you I am not very technical.  I am happy to run commands and provide output.

Here is my system hardware/software:

-Ubuntu 18.04.2 hwe (4.18.0-17-lowlatency)
    -(I am not using a mainline/custom kernel.  This is the "official" Ubuntu kernel for 18.04 & 18.10.  Any kernel after 4.17 should work the same, and I believe Debian Buster has 4.19.)

-AMD Vega 64 ("Vega10" - 8GB vram)
    -amdgpu drivers ([padoka/mesa repository](https://launchpad.net/~paulo-miguel-dias/+archive/ubuntu/mesa)) - version 4.5 Mesa 19.1.0-devel
    -(not using amdgpu-pro.  I previously tried, but it did not work at all with my 4.18 kernel, and it generally did not perform well on linux-kernel 4.15).

-AMD FX 8370 (8-core @ 4000Mhz)

-Asus Crosshair IV Formula motherboard
     -(using PCIe 2.0 x16 slot)
     --32GB DDR3 (running at 1600Mhz)

I think what you mean by "kernel boot arguments" is my grub line?  Here it is:
`GRUB_CMDLINE_LINUX="radeon.si_support=0 radeon.cik_support=0 amdgpu.si_support=1 amdgpu.cik_support=1 acpi=ht"`

I also added these options under my xorg.conf:
`Option "Accelmethod" "glamor" 
Option "DRI" "3"
Option "TearFree" "true"`

One thing I think is crucial is to ensure you are running the amdgpu driver.  You should be able to use the command:
`inxi -Gx`

This may not be relevant, but one thing that could be interesting is that I fall under the GFX9 PCIe atomics exception.

I hope this is helpful, but please let me know if I can provide more information or help.

---

### 评论 #4 — KristijanZic (2019-04-18T18:56:15Z)

Hi, I'm KristijanZic from BMD forums.

Basically I'm running into same issue as @beatboxa and that is that ROCm 2.3 update broke DaVinci Resolve on my system. Updating DR to v16 didn't help. 
Also I need to use ROCm since AMDGPU-PRO works only on CentOS, it makes Ubuntu and Fedora unbootable, monitors even loose signal form gpu so amdgpu-pro is out of the question for me :/

I've tested DR16 with ROCm 2.3 on stock Ubuntu 18.04, Ubuntu 18.10, Ubuntu 19.04, Fedora 29, CentOS 7 and my personal installation that has mesa from [Padoka PPA](https://launchpad.net/~paulo-miguel-dias/+archive/ubuntu/mesa), ROCm 2.3 and the latest mainline kernel. The same issue is happening on all of those distros. DR crashes on splash screen.

[This is the DaVinci Resolve generated logs archive on Ubuntu](https://drive.google.com/file/d/1uPZR3liC01ZNBkrUOpAvsxBkdz4dXdpW/view?usp=sharing)

[This is the generated logs archive on CentOS](
https://drive.google.com/file/d/1puheRfIt5tcZiquC2uf1ZJoZVVGVlD2R/view?usp=sharing)


Here's my **/etc/default/grub**
```
GRUB_DEFAULT=0
GRUB_TIMEOUT_STYLE=hidden
GRUB_TIMEOUT=0
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
```

**neofetch of my personal installation:**
```
OS: Ubuntu 18.10 x86_64 
Kernel: 5.0.8-050008-generic 
Uptime: 23 mins 
Packages: 2359 (dpkg), 40 (flatpak), 44 (snap) 
Shell: bash 4.4.19 
Resolution: 1680x1050, 1920x1200 
DE: GNOME 3.30.2 
WM: GNOME Shell 
WM Theme: Adwaita 
Theme: Yaru [GTK2/3] 
Icons: Yaru [GTK2/3] 
Terminal: gnome-terminal 
CPU: AMD Ryzen Threadripper 1900X 8- (16) @ 3.800GHz 
GPU: AMD ATI Radeon RX Vega 64 
Memory: 3481MiB / 15959MiB 

```

From the commands that @beatboxa said are working for him; only **rocminfo** command works for me:
**rocminfo:**
```
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (number of timestamp)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3800                               
  BDFID:                   0                                  
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16342048KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16342048KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    AMD Ryzen Threadripper 1900X 8-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0                                  
  Queue Min Size:          0                                  
  Queue Max Size:          0                                  
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768KB                            
  Chip ID:                 0                                  
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):3800                               
  BDFID:                   0                                  
  Compute Unit:            8                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16342048KB                         
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128                                
  Queue Min Size:          4096                               
  Queue Max Size:          131072                             
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16KB                               
  Chip ID:                 26751                              
  Cacheline Size:          64                                 
  Max Clock Frequency (MHz):1750                               
  BDFID:                   17408                              
  Compute Unit:            64                                 
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64                                 
  Workgroup Max Size:      1024                               
  Workgroup Max Size Per Dimension:
    Dim[0]:                  67109888                           
    Dim[1]:                  1140851712                         
    Dim[2]:                  0                                  
  Grid Max Size:           4294967295                         
  Waves Per CU:            40                                 
  Max Work-item Per CU:    2560                               
  Grid Max Size per Dimension:
    Dim[0]:                  4294967295                         
    Dim[1]:                  4294967295                         
    Dim[2]:                  4294967295                         
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224KB                          
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64KB                               
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Dimension: 
        Dim[0]:                  67109888                           
        Dim[1]:                  1024                               
        Dim[2]:                  16777217                           
      Workgroup Max Size:      1024                               
      Grid Max Dimension:      
        x                        4294967295                         
        y                        4294967295                         
        z                        4294967295                         
      Grid Max Size:           4294967295                         
      FBarrier Max Size:       32                                 
*** Done ***   
```

**clinfo**
```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (2862.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 1
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Vega 10 XT [Radeon RX Vega 64]
  Device Topology:				 PCI[ B#68, D#0, F#0 ]
  Max compute units:				 64
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1750Mhz
  Address bits:					 64
  Max memory allocation:			 7287183769
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 26751
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 1024
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 Yes
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 8573157376
  Constant buffer size:				 7287183769
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 65536
  Max pipe arguments:				 16
  Max pipe active reservations:			 16
  Max pipe packet size:				 2992216473
  Max global variable size:			 7287183769
  Max global variable preferred total size:	 8573157376
  Max read/write image args:			 64
  Max on device events:				 1024
  Queue on device max size:			 8388608
  Max on device queues:				 1
  Queue on device preferred size:		 262144
  SVM capabilities:				 
    Coarse grain buffer:			 Yes
    Fine grain buffer:				 Yes
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:				 
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:				 
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:				 
    Out-of-Order:				 Yes
    Profiling :					 Yes
  Platform ID:					 0x7f3cd2a94f70
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2862.0 (HSA1.1,LC)
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 2.0 
  Extensions:					 cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```

DR seems to be finding everything it needs :O
**ldd /opt/resolve/bin/resolve**
```
linux-vdso.so.1 (0x00007ffc44b3d000)
	libc++.so.1 => /opt/resolve/bin/./../libs/libc++.so.1 (0x00007fe43ccaa000)
	libc++abi.so.1 => /opt/resolve/bin/./../libs/libc++abi.so.1 (0x00007fe43ca7b000)
	libcudart.so.10.0 => /opt/resolve/bin/./../libs/libcudart.so.10.0 (0x00007fe43c801000)
	libcublas.so.10.0 => /opt/resolve/bin/./../libs/libcublas.so.10.0 (0x00007fe438269000)
	libnvrtc.so.10.0 => /opt/resolve/bin/./../libs/libnvrtc.so.10.0 (0x00007fe436c4d000)
	libQt5Concurrent.so.5 => /opt/resolve/bin/./../libs/libQt5Concurrent.so.5 (0x00007fe436c47000)
	libQt5Core.so.5 => /opt/resolve/bin/./../libs/libQt5Core.so.5 (0x00007fe436667000)
	libQt5Gui.so.5 => /opt/resolve/bin/./../libs/libQt5Gui.so.5 (0x00007fe4360ed000)
	libQt5Multimedia.so.5 => /opt/resolve/bin/./../libs/libQt5Multimedia.so.5 (0x00007fe436009000)
	libQt5Network.so.5 => /opt/resolve/bin/./../libs/libQt5Network.so.5 (0x00007fe435eb6000)
	libQt5OpenGL.so.5 => /opt/resolve/bin/./../libs/libQt5OpenGL.so.5 (0x00007fe435e51000)
	libQt5Sql.so.5 => /opt/resolve/bin/./../libs/libQt5Sql.so.5 (0x00007fe435d0a000)
	libQt5Svg.so.5 => /opt/resolve/bin/./../libs/libQt5Svg.so.5 (0x00007fe435cb1000)
	libQt5Widgets.so.5 => /opt/resolve/bin/./../libs/libQt5Widgets.so.5 (0x00007fe435634000)
	libQt5Xml.so.5 => /opt/resolve/bin/./../libs/libQt5Xml.so.5 (0x00007fe4355eb000)
	libQt5XmlPatterns.so.5 => /opt/resolve/bin/./../libs/libQt5XmlPatterns.so.5 (0x00007fe435157000)
	libGLU.so.1 => /usr/lib/x86_64-linux-gnu/libGLU.so.1 (0x00007fe434ec6000)
	libGL.so.1 => /usr/lib/x86_64-linux-gnu/libGL.so.1 (0x00007fe434e32000)
	fusionscript.so => /opt/resolve/bin/./../libs/Fusion/fusionscript.so (0x00007fe43480a000)
	libluajit-5.1.so.2 => /opt/resolve/bin/./../libs/libluajit-5.1.so.2 (0x00007fe43458b000)
	libtbbmalloc.so.2 => /opt/resolve/bin/./../libs/libtbbmalloc.so.2 (0x00007fe43434c000)
	libtbbmalloc_proxy.so.2 => /opt/resolve/bin/./../libs/libtbbmalloc_proxy.so.2 (0x00007fe434145000)
	libXxf86vm.so.1 => /usr/lib/x86_64-linux-gnu/libXxf86vm.so.1 (0x00007fe433f3f000)
	libfreetype.so.6 => /usr/lib/x86_64-linux-gnu/libfreetype.so.6 (0x00007fe433c8b000)
	libXext.so.6 => /usr/lib/x86_64-linux-gnu/libXext.so.6 (0x00007fe433a79000)
	libSM.so.6 => /usr/lib/x86_64-linux-gnu/libSM.so.6 (0x00007fe433871000)
	libICE.so.6 => /usr/lib/x86_64-linux-gnu/libICE.so.6 (0x00007fe433656000)
	libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6 (0x00007fe43351a000)
	libbz2.so.1 => /lib/x86_64-linux-gnu/libbz2.so.1 (0x00007fe433507000)
	libxml2.so.2 => /usr/lib/x86_64-linux-gnu/libxml2.so.2 (0x00007fe43335f000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe4331d2000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe4331cc000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fe4331c2000)
	libavformat.so.57 => /opt/resolve/bin/./../libs/libavformat.so.57 (0x00007fe432dc6000)
	libavcodec.so.57 => /opt/resolve/bin/./../libs/libavcodec.so.57 (0x00007fe43185e000)
	libavutil.so.55 => /opt/resolve/bin/./../libs/libavutil.so.55 (0x00007fe4315eb000)
	libMXF.so => /opt/resolve/bin/./../libs/libMXF.so (0x00007fe4312cf000)
	libfraunhoferdcp.so => /opt/resolve/bin/./../libs/libfraunhoferdcp.so (0x00007fe42b61a000)
	libSMDK-Linux-x64.so.4.17 => /opt/resolve/bin/./../libs/libSMDK-Linux-x64.so.4.17 (0x00007fe42b2de000)
	libmp4decMT.so => /opt/resolve/bin/./../libs/libmp4decMT.so (0x00007fe42afac000)
	libmp4encMT.so => /opt/resolve/bin/./../libs/libmp4encMT.so (0x00007fe42aa40000)
	libsonyxavcenc.so => /opt/resolve/bin/./../libs/libsonyxavcenc.so (0x00007fe42a7d3000)
	liblog4cxx.so.10 => /opt/resolve/bin/./../libs/liblog4cxx.so.10 (0x00007fe42a2ba000)
	libaprutil-1.so.0 => /opt/resolve/bin/./../libs/libaprutil-1.so.0 (0x00007fe42a090000)
	libapr-1.so.0 => /opt/resolve/bin/./../libs/libapr-1.so.0 (0x00007fe429e5a000)
	libopencv_calib3d.so.3.4 => /opt/resolve/bin/./../libs/libopencv_calib3d.so.3.4 (0x00007fe429a98000)
	libopencv_core.so.3.4 => /opt/resolve/bin/./../libs/libopencv_core.so.3.4 (0x00007fe42959a000)
	libopencv_dnn.so.3.4 => /opt/resolve/bin/./../libs/libopencv_dnn.so.3.4 (0x00007fe429027000)
	libopencv_features2d.so.3.4 => /opt/resolve/bin/./../libs/libopencv_features2d.so.3.4 (0x00007fe428d74000)
	libopencv_flann.so.3.4 => /opt/resolve/bin/./../libs/libopencv_flann.so.3.4 (0x00007fe428b08000)
	libopencv_highgui.so.3.4 => /opt/resolve/bin/./../libs/libopencv_highgui.so.3.4 (0x00007fe4288ff000)
	libopencv_imgcodecs.so.3.4 => /opt/resolve/bin/./../libs/libopencv_imgcodecs.so.3.4 (0x00007fe4286ce000)
	libopencv_imgproc.so.3.4 => /opt/resolve/bin/./../libs/libopencv_imgproc.so.3.4 (0x00007fe4280fc000)
	libopencv_ml.so.3.4 => /opt/resolve/bin/./../libs/libopencv_ml.so.3.4 (0x00007fe427e44000)
	libopencv_objdetect.so.3.4 => /opt/resolve/bin/./../libs/libopencv_objdetect.so.3.4 (0x00007fe427bf6000)
	libopencv_video.so.3.4 => /opt/resolve/bin/./../libs/libopencv_video.so.3.4 (0x00007fe4279aa000)
	libopencv_videoio.so.3.4 => /opt/resolve/bin/./../libs/libopencv_videoio.so.3.4 (0x00007fe427791000)
	libcudnn.so.7 => /opt/resolve/bin/./../libs/libcudnn.so.7 (0x00007fe412176000)
	libSonyRawDev.so.3 => /opt/resolve/bin/./../libs/libSonyRawDev.so.3 (0x00007fe411cd1000)
	libOpenCL.so.1 => /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1 (0x00007fe411ac9000)
	libgvc.so.6 => /opt/resolve/bin/./../libs/libgvc.so.6 (0x00007fe411828000)
	libcgraph.so.6 => /opt/resolve/bin/./../libs/libcgraph.so.6 (0x00007fe411612000)
	libcdt.so.5 => /opt/resolve/bin/./../libs/libcdt.so.5 (0x00007fe41140d000)
	libxdot.so.4 => /opt/resolve/bin/./../libs/libxdot.so.4 (0x00007fe411206000)
	libpathplan.so.4 => /opt/resolve/bin/./../libs/libpathplan.so.4 (0x00007fe410ffe000)
	libArriRawSDK.so.6 => /opt/resolve/bin/./../libs/libArriRawSDK.so.6 (0x00007fe40fcc7000)
	libcodexhdedecoder.so.2 => /opt/resolve/bin/./../libs/libcodexhdedecoder.so.2 (0x00007fe40fabb000)
	libgvcodec.so => /opt/resolve/bin/./../libs/libgvcodec.so (0x00007fe40f894000)
	libCrmSdk.so.2.2 => /opt/resolve/bin/./../libs/libCrmSdk.so.2.2 (0x00007fe40d5d1000)
	libid3-3.8.so.3 => /opt/resolve/bin/./../libs/libid3-3.8.so.3 (0x00007fe40d392000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe40d371000)
	libssl.so.1.0.0 => /opt/resolve/bin/./../libs/libssl.so.1.0.0 (0x00007fe40d0fb000)
	libcrypto.so.1.0.0 => /opt/resolve/bin/./../libs/libcrypto.so.1.0.0 (0x00007fe40cca6000)
	librsvg-2.so.2 => /usr/lib/x86_64-linux-gnu/librsvg-2.so.2 (0x00007fe40cc6d000)
	libCg.so => /opt/resolve/bin/./../libs/libCg.so (0x00007fe40bd05000)
	libCgGL.so => /opt/resolve/bin/./../libs/libCgGL.so (0x00007fe40bb82000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe40bb68000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe40b97e000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fe43cf93000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fe40b7f4000)
	libGLX.so.0 => /usr/lib/x86_64-linux-gnu/libGLX.so.0 (0x00007fe40b7be000)
	libGLdispatch.so.0 => /usr/lib/x86_64-linux-gnu/libGLdispatch.so.0 (0x00007fe40b701000)
	libpng16.so.16 => /usr/lib/x86_64-linux-gnu/libpng16.so.16 (0x00007fe40b4cf000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fe40b2b2000)
	libuuid.so.1 => /lib/x86_64-linux-gnu/libuuid.so.1 (0x00007fe40b2a9000)
	libbsd.so.0 => /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007fe40b090000)
	libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007fe40b067000)
	libicuuc.so.60 => /usr/lib/x86_64-linux-gnu/libicuuc.so.60 (0x00007fe40acb0000)
	liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007fe40aa8a000)
	libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007fe40aa7f000)
	libasound.so.2 => /usr/lib/x86_64-linux-gnu/libasound.so.2 (0x00007fe40a983000)
	libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007fe40a946000)
	libcrypt.so.1 => /lib/x86_64-linux-gnu/libcrypt.so.1 (0x00007fe40a90c000)
	libcudart.so.7.5 => /opt/resolve/bin/./../libs/libcudart.so.7.5 (0x00007fe40a6ac000)
	libgdk_pixbuf-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgdk_pixbuf-2.0.so.0 (0x00007fe40a686000)
	libgio-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0 (0x00007fe40a4e2000)
	libpangocairo-1.0.so.0 => /usr/lib/x86_64-linux-gnu/libpangocairo-1.0.so.0 (0x00007fe40a4d3000)
	libpangoft2-1.0.so.0 => /usr/lib/x86_64-linux-gnu/libpangoft2-1.0.so.0 (0x00007fe40a4ba000)
	libpango-1.0.so.0 => /usr/lib/x86_64-linux-gnu/libpango-1.0.so.0 (0x00007fe40a46d000)
	libgobject-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0 (0x00007fe40a419000)
	libfontconfig.so.1 => /usr/lib/x86_64-linux-gnu/libfontconfig.so.1 (0x00007fe40a3d4000)
	libcairo.so.2 => /usr/lib/x86_64-linux-gnu/libcairo.so.2 (0x00007fe40a2b4000)
	libcroco-0.6.so.3 => /usr/lib/x86_64-linux-gnu/libcroco-0.6.so.3 (0x00007fe40a079000)
	libglib-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0 (0x00007fe409f5c000)
	libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007fe409d56000)
	libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007fe409b50000)
	libicudata.so.60 => /usr/lib/x86_64-linux-gnu/libicudata.so.60 (0x00007fe407fa7000)
	libgmodule-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0 (0x00007fe407fa1000)
	libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x00007fe407d79000)
	libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007fe407d5c000)
	libmount.so.1 => /lib/x86_64-linux-gnu/libmount.so.1 (0x00007fe407d03000)
	libharfbuzz.so.0 => /usr/lib/x86_64-linux-gnu/libharfbuzz.so.0 (0x00007fe407c50000)
	libthai.so.0 => /usr/lib/x86_64-linux-gnu/libthai.so.0 (0x00007fe407c45000)
	libfribidi.so.0 => /usr/lib/x86_64-linux-gnu/libfribidi.so.0 (0x00007fe407c28000)
	libffi.so.6 => /usr/lib/x86_64-linux-gnu/libffi.so.6 (0x00007fe407a1e000)
	libpixman-1.so.0 => /usr/lib/x86_64-linux-gnu/libpixman-1.so.0 (0x00007fe407779000)
	libxcb-shm.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-shm.so.0 (0x00007fe407774000)
	libxcb-render.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-render.so.0 (0x00007fe407765000)
	libXrender.so.1 => /usr/lib/x86_64-linux-gnu/libXrender.so.1 (0x00007fe40755b000)
	libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007fe4074e5000)
	libblkid.so.1 => /lib/x86_64-linux-gnu/libblkid.so.1 (0x00007fe407494000)
	libgraphite2.so.3 => /usr/lib/x86_64-linux-gnu/libgraphite2.so.3 (0x00007fe407467000)
	libdatrie.so.1 => /usr/lib/x86_64-linux-gnu/libdatrie.so.1 (0x00007fe407260000)
```

---

### 评论 #5 — beatboxa (2019-04-18T20:49:09Z)

@KristijanZic 

Until this is resolved, I'd recommend that for now you do what I did:  Downgrade to ROCm 2.2, which allows DR16 and other applications to work.

Here's how I got it working:
1)  I added the archived 2.2 ROCm respository.  To add this repository, I ran:
`echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/2.2/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list`
(You'll note I have simply replaced "debian" with "2.2" in the official ROCm instructions).

2)  Run Synaptic Package Manager.  You'll want to look at only the packages from this repository.  On the bottom left, click "Origin", and then look for "Ubuntu 16.04/main (repo.radeon.com)" in the list above this button.

3)  You should only have 5 packages installed, that I listed in my post above.  Make sure you don't have additional packages installed if you don't need them.  And make sure the version numbers are the same.  If they are not, then select the package that is too new (probably will be rocm-utils), then click on "Package" in the menu, and then click "Force version."  Then "Apply" the installation in Synaptic to perform the downgrade operation.

For convenience, those packages are:
- rocm-clang-ocl (0.4.0-7ce124f)
- rocm-opencl (1.2.0-2019030702)
- rocm-opencl-dev (1.2.0-2019030702)
- rocm-utils (2.2.31)
- rocminfo (1.0.0)


4)  Because we are back on 2.2, follow the "upstream driver" instructions.  So this just means you now need to execute the following from a command line:
`echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules`

And I believe that should be it.  I don't think you'll even need to reinstall DaVinci Resolve.

This is how you get amdgpu (padoka) + OpenCL (ROCm) + DaVinci Resolve + linux-kernel 4.17 or later working.

---

### 评论 #6 — KristijanZic (2019-04-18T20:57:49Z)

Alright, I'm going to test this on 19.04 right now.
Do we know what's exactly causing the issue?

Also, how do Fusion effects work for you on ROCm 2.2? For example Fusion 3D titles, any glitches, tearing or artefacts? That's how it worked for me with DR15 + ROCm 2.2

---

### 评论 #7 — beatboxa (2019-04-18T21:43:13Z)

I do not know what's causing it, but it does appear related to 2.3.  Specifically, there are only 3 different related packages between the repositories:

- rocm-opencl
- rocm-opencl-dev
- rocm-utils

I doubt that DaVinci directly uses rocm-utils, so my guess is that there is some issue in rocm-opencl (or dev).

The version differences in rocm-opencl are:
ROCm 2.3:  rocm-opencl (1.2.0-2019040843)
ROCm 2.2:  rocm-opencl (1.2.0-2019030702)

So perhaps something changed in rocm-opencl between March & April to cause this.

I have not done much work with Fusion FX yet, so I have not noticed any tearing or artifacts; but the other basic parts of DR16 that I've used so far (import/export, grading, motion (including optical flow)) appear to work fine so far.

---

### 评论 #8 — KristijanZic (2019-04-19T02:05:02Z)

So that workaround did the trick!
I did the fresh installation of 19.04 and installed ROCm 2.2 with upstream kernel drivers and DaVinci Resolve 16.

DR has an issue with welcome screen at first launch where it shows solid black welcome screen and freezes the machine. Manual reboot of the machine is required but after that it seems to work nominally, the Fusion FX effects and all. In fact the best experience with DR on Ubuntu so far. I just hope ROCm 2.4 fixes the issue that 2.3 has.

This is still an open issue tho since ROCm 2.3 clearly has a bug somewhere but the workaround will do for now.

---

### 评论 #9 — zelikos (2019-04-19T18:27:34Z)

Downgrading to the ROCm 2.2 versions of rocm-opencl and rocm-opencl-dev works for me as well. Resolve fails to launch with ROCm 2.3, on several different OS, kernel, and driver configurations, with and without the rock-dkms package.

OSes tested: elementary OS 5.0; Ubuntu 18.04, 18.10, and 19.04
Kernel versions tested: 4.15, 4.18, 5.0

System 1:
CPU: Ryzen 7 1700
GPU: RX 570 8GB

System 2:
CPU: Ryzen 5 1400
GPU: RX 570 4GB

With the workaround (ROCm 2.3, using rocm-opencl & -dev from 2.2), Resolve successfully launches. However:

1. On Resolve 15, Fusion FX don't work well; they're very slow to render, and have glitches and artifacts with them. Resolve 16 does not have this problem. Additionally, when testing AMDGPU-pro with Resolve 15 on Ubuntu 18.04.1, I had no issues with Fusion FX.

2. With kernel 4.18 and without rock-dkms, there are playback issues in Resolve 16. The timeline moves along just fine, but the preview windows fail to display anything. Thumbnails in the project bin display normally, as does the preview on the Fairlight page. This issue doesn't occur when using rock-dkms on 4.15 or 4.18, or by using kernel 5.0 without rock-dkms.

3. Resolve 16, with any kernel/rock-dkms combination, frequently causes my entire system to slow down. This issue may be an issue with Resolve 16 rather than ROCm, though, due to it still being in beta; possibly related to [this post](https://forum.blackmagicdesign.com/viewtopic.php?f=32&t=89724) on the BMD forum. Resolve 15 does not have this problem.

---

### 评论 #10 — thesleort (2019-05-08T11:15:18Z)

This appears to still be a problem in ROCm 2.4.

As previously mentioned, it is possible to still run Davinci Resolve with 2.2, but that is a workaround.

---

### 评论 #11 — KristijanZic (2019-05-14T02:32:17Z)

I can confirm that the problem still persists in the ROCm 2.4.

---

### 评论 #12 — KristijanZic (2019-05-22T07:36:48Z)

The problem is still present even with the new DaVinci Resolve 16 Beta 3

---

### 评论 #13 — johnr14 (2019-05-27T16:40:42Z)

Glad to finally having found this as I have the same problems. DR 15 stopped working at some point on Ubuntu, then upgraded to 19.04, 19.10 and tried many things to make it work again even upgraded to DR16 beta. I have Vega64 on Threadripper and it segfault also, so bug confirmed. 

Also downgrading kernel 5.1 to 4.15-4.19 with rocm prevents the computer from booting. 
I get a black, non responsive screen, after grub. Should this be opened as a second bug ?

Thanks

---

### 评论 #14 — sysrq-reisub (2019-06-04T15:54:42Z)

DKMS of rocm-dkms 2.2 fails to build on 19.10 (Kernel 5.0) while 2.3 and 2.4 compiles fine, but gives the issue with Resolve

EDIT: I didn't knew dkms was not needed, I confirm 2.2 works

---

### 评论 #15 — sysrq-reisub (2019-06-08T14:11:41Z)

Still an issue on 2.5 

---

### 评论 #16 — sysrq-reisub (2019-07-04T14:38:28Z)

Looks like it's working fine for me with the latest release

---

### 评论 #17 — beatboxa (2019-07-04T18:43:01Z)

@Lukypie 
Which versions & specs did you get it working on?  Previously, you mentioned that ROCm 2.5 did not work, but that appears to be the latest release.

---

### 评论 #18 — sysrq-reisub (2019-07-05T00:26:12Z)

> @Lukypie
> Which versions & specs did you get it working on? Previously, you mentioned that ROCm 2.5 did not work, but that appears to be the latest release.

I probably got confused, since I use the Ubuntu repository it probably wasn't updated 

---

### 评论 #19 — charlesportwoodii (2019-07-09T12:59:06Z)

EDIT2:

The llvm ir issue stopped working on it's own and now resolve is crashing at `looking for control surfaces`. I'm not sure why I was getting the llvm ir issues in the first place however. GDB indicates it's still a problem with libOpenGL.so.1

```
Thread 241 "GUI Thread" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffeff680700 (LWP 19515)]
0x0000000000000000 in ?? ()
(gdb) bt
#0  0x0000000000000000 in  ()
#1  0x00007fffcba85cf2 in  () at /opt/rocm/opencl/lib/x86_64/libOpenCL.so.1
#2  0x0000000005bc844f in  ()
#3  0x0000000005bcce43 in  ()
#4  0x0000000005b3cc1e in  ()
#5  0x00000000020217bc in  ()
#6  0x0000000002025b7d in  ()
#7  0x00007fffc71346db in start_thread (arg=0x7ffeff680700) at pthread_create.c:463
#8  0x00007fffc525788f in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
```

EDIT:

While I clearly was able to get this working 2 days ago resolve now crashes on launch with an llvm ir error with `/tmp`. I'm not exactly sure why it worked once then stopped working. What's more strange is that the previously working 2.2 driver no longer works either. I now get the following error:

```
10 warnings generated.
[0x7f45b5c93b00] | Fairlight            | INFO  | 2019-07-11 16:54:38,295 | 00.00.00.852(000): Running Fairlight (r011733-88fe9f3)
[0x7f45b5c93b00] | UI.GLContext         | INFO  | 2019-07-11 16:54:38,307 | Creating shared OpenGL context for this thread (2 total).
[0x7f45b5c93b00] | UI.GLContext         | INFO  | 2019-07-11 16:54:38,310 | Initialized OpenGL 4.5 (requested 2.0) on device 'X.Org Radeon RX 580 Series (POLARIS10, DRM 3.30.0, 5.1.16-050116-generic, LLVM 8.0.0)'
[0x7f44f82fb700] | UI.GLContext         | INFO  | 2019-07-11 16:54:38,310 | Creating shared OpenGL context for this thread (3 total).


==========[CRASH DUMP]==========
Please send this to support:

#TIME Thu Jul 11 16:54:38 2019 - Uptime 00:00:01 (hh:mm:ss)
#PROGRAM_NAME DaVinci Resolve v16.0.0b.040 (Linux/Clang)

/opt/resolve/bin/resolve() [0x5091879]
/opt/resolve/bin/resolve() [0x509106a]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x12890) [0x7f45bfb5c890]
Signal Number = 11

================================
error: unable to rename temporary '/tmp/t_22395_33-de6a8f-565d13ae.o.tmp' to output file '/tmp/t_22395_33-de6a8f.o': 'No such file or directory'
1 error generated.
[0x7f455667c700] | DVIP                 | ERROR | 2019-07-11 16:54:38,932 | Build Status: -2
[0x7f455667c700] | DVIP                 | ERROR | 2019-07-11 16:54:38,932 | Build Options:  -w -cl-mad-enable -cl-fast-relaxed-math -Dz323df50901b485739bf3a3b9a84c73b0 -Dz6e436e44fad709e7c0aa0046bd091019 -Dzc229ce7b384e9cbe83e58608fba7c36d -Dzbf151cb3ebc5bf415353c53eba44db8c
[0x7f455667c700] | DVIP                 | ERROR | 2019-07-11 16:54:38,932 | Build Log: 
 Error: Creating the executable from LLVM IRs failed.

terminate called after throwing an instance of 'DVIP::DVIPBuildException'
  what():  DVIP Exception: Kernel build failure
 - API: OpenCL
 - Call stack:
     /opt/resolve/bin/resolve() [0x5b54324]
     /opt/resolve/bin/resolve() [0x5b3292d]
     /opt/resolve/bin/resolve() [0x5b332d1]
     /opt/resolve/bin/resolve() [0x5bcb416]
     /opt/resolve/bin/resolve() [0x5bcbfb9]
     /opt/resolve/bin/resolve() [0x5bcc76d]
     /opt/resolve/bin/resolve() [0x6093c93]
     /opt/resolve/bin/resolve() [0x58580a1]
     /opt/resolve/bin/resolve() [0x585861b]
     /opt/resolve/bin/resolve() [0x53cc60a]
     /opt/resolve/bin/resolve() [0x53a3818]
     /opt/resolve/bin/resolve() [0x53a3e69]
     /opt/resolve/bin/resolve() [0x53a2cf6]
     /lib/x86_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f45bfb516db]
 - Kernel name: Algorithm Packer
 - Build log:
     Error: Creating the executable from LLVM IRs failed.
     


==========[CRASH DUMP]==========
Please send this to support:

#TIME Thu Jul 11 16:54:38 2019 - Uptime 00:00:02 (hh:mm:ss)
#PROGRAM_NAME DaVinci Resolve v16.0.0b.040 (Linux/Clang)

/opt/resolve/bin/resolve() [0x5091879]
/opt/resolve/bin/resolve() [0x509106a]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x12890) [0x7f45bfb5c890]
/lib/x86_64-linux-gnu/libc.so.6(gsignal+0xc7) [0x7f45bdb91e97]
/lib/x86_64-linux-gnu/libc.so.6(abort+0x141) [0x7f45bdb93801]
/opt/resolve/bin/resolve(_ZN9__gnu_cxx27__verbose_terminate_handlerEv+0x15d) [0x70fc03d]
/opt/resolve/bin/../libs/libc++abi.so.1(+0x22036) [0x7f45f02ff036]
/opt/resolve/bin/../libs/libc++abi.so.1(+0x219d7) [0x7f45f02fe9d7]
/opt/resolve/bin/resolve() [0x58581ea]
/opt/resolve/bin/resolve() [0x585861b]
/opt/resolve/bin/resolve() [0x53cc60a]
/opt/resolve/bin/resolve() [0x53a3818]
/opt/resolve/bin/resolve() [0x53a3e69]
/opt/resolve/bin/resolve() [0x53a2cf6]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f45bfb516db]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f45bdc7488f]
Signal Number = 6

================================
````

------

I haven't done much past the splash screen but as of rocm 2.6 running kernel 5.1.16 on Ubuntu 18.04 LTS I am able to launch resolve and have it detect my graphics card _if_ I start resolve as root.

```
sudo /opt/resolve/bin/resolve
```

Unfortunately resolve crashes if I don't run it as root. The fix proposed in https://github.com/RadeonOpenCompute/ROCm/issues/823 didn't resolve the issue for me.

I just have `rocm-opencl` and `rocm-opencl-dev` installed, no need for `rocm-dkms` at this time.

![Screenshot from 2019-07-09 07-57-07](https://user-images.githubusercontent.com/630969/60889675-2f22b380-a21f-11e9-92ed-42a7b0d0a1bd.png)



---

### 评论 #20 — beatboxa (2019-12-22T19:32:10Z)

@btspce Isn't your list of packages just rocm2.2?

When I tried the instructions in your linked thread, I couldn't get 3.0 working.

---

### 评论 #21 — btspce (2019-12-22T20:01:33Z)

3.0 is not working. I made an error in an previous comment and ended up with both 2.2 repo and 3.0 in my rocm.repo after switching back and forth a few times. I have deleted my previous comment that stated that this was fixed. I was using 2.2 when I thought I had installed 3.0 due to this.

---

### 评论 #22 — btspce (2020-03-05T07:00:34Z)

This has now been broken for nearly a year on multiple releases. Can a dev at AMD please check what happened between 2.2 and 2.3 and solve this issue so all users of Davinci Resolve can move on from ROCm 2.2?

---

### 评论 #23 — btspce (2020-04-21T09:47:54Z)

ROCm 3.3 is now working on Davinci with Raven Ridge 2700u and hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm from ROCm 2.9 repo on Fedora 31

---

### 评论 #24 — beatboxa (2020-05-29T06:30:26Z)

> ROCm 3.3 is now working on Davinci with Raven Ridge 2700u and hsa-ext-rocr-dev-1.1.9-122-ge5c4efb1-Linux.rpm from ROCm 2.9 repo on Fedora 31

I think I recently upgraded my linux kernel to 5.3, and it seems that DaVinci had been crashing since.  So I tried upgrading to ROCm 3.3 (with hsa 1.1.9-122), and mine doesn't appear to be working for me.  DaVinci Resolve crashes immediately.

The way I "upgraded" rocm was to install rocm-dev ("Upstream kernel"), and then downgrade hsa to the version you listed.  I don't think I removed the previous version.   Instructions were here:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu

Which linux kernel (and rocm package versions) are you running?  Would you be able to guide me through how you upgraded rocm & got it working, please?


EDIT:  I've cleaned up and reinstalled DaVinci Resolve and done a clean install of rocm.  DaVinci hangs.  I think I've narrowed down the problem, but I still need help if you wouldn't mind.

rocm appears installed correctly according to rocminfo.

However, running clinfo does output information but hangs.  Specifically, the file /etc/OpenCL/vendors/amdocl64.icd seems to cause it to hang.  Moving this file allows clinfo to run and complete; but DaVinci crashes on startup.  Keeping this file doesn't cause a crash but does cause everything to hang (never actually completing).  Any thoughts?


EDIT 2:
**Got it working**.  I had to install dkms (via rocm-dkms).  I did not have to downgrade hsa.  So now, I am running on:

- AMD FX (8350)
- PCIe 2.0 (x16 slot on a Crosshair IV Formula motherboard)
- Vega 64
- Ubuntu 18.04.4 (LTS)
- kernel 5.3.x
- rocm 3.3 (no overrides / downgrades)
- DaVinci Resolve 16.2.2

---

### 评论 #25 — ghost (2020-06-05T08:39:39Z)

Rocm-dkms 3.5 broke Davinci and Blender for me, I'm on Ubuntu MATE 20.04 with Linux 5.04 running on a RX 480

---

### 评论 #26 — helloworld1 (2020-06-06T15:07:56Z)

Same. Rocm 3.5 broke davinci resolve on CentOS 7. The davinci resolve launches fine but all video previews are blank but audio works fine. Downgrading to 3.3 and everything works. 

---

### 评论 #27 — beatboxa (2020-06-07T15:39:10Z)

@Utopanic @helloworld1 Can you describe how you updated to ROCm 3.5, and in particular which packages got installed?

From the installation docs, it appears that ROCm 3.5 has yet another architectural overhaul that might require a clean installation.  In particular, it seems that 3.5 has modularized and separated the firmware & kernel into their own packages (while 3.3 had them together in the same package).

My guess is that a simple package update won't install or configure correctly, and just want to confirm that both the dkms and firmware packages were installed clean?

(I haven't yet tried 3.5).

---

### 评论 #28 — ghost (2020-06-07T16:49:59Z)

@beatboxa I have installed rocm-dkms and then upgraded it vi apt-upgrade. I'm kind of a noob, how do I clean install it?

---

### 评论 #29 — helloworld1 (2020-06-07T22:15:19Z)

@beatboxa Yes I did a full clean install. I have removed all the packages and made sure /opt/rocm and /opt/rocm-3.3.0 is removed. Then I installed rocm 3.5.0 on CentOS 7.8. I have verified clinfo and rocminfo works fine. Davinci Resolve detects OpenCL fine but the preview screen is just blank. 

I then installed rocm 3.3.0 along with 3.5.0 but link /opt/rocm to /opt/rocm-3.3.0. Davinci Resolve works fine again with correct preview and functionality.

---

### 评论 #30 — beatboxa (2020-06-08T21:21:25Z)

@Utopanic I am pretty much a noob as well, but per helloworld1, it looks like 3.5 doesn't work even with a clean install.

For reference, what I've done in the past is use Synaptic Package Manager to show me all packages installed from a specific source/repository (the rocm repository in this case).  Within Synaptic, you can also choose to uninstall them; or you can pick specific versions to install if you set up multiple repositories from the same source (eg. all of these versions:   http://repo.radeon.com/rocm/apt/ 

After uninstalling, I would then go and clear the appropriate directories, which you can find here:
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#amd-rocm-multiversion-installation

I believe the only directory that needs to be cleaned after uninstall is just /opt/rocm

ROCm 3.3 and later added the ability to install multiple versions of ROCm or its components at the same time.  I don't remember if I ever did this successfully or understood how to do it properly, but you basically make links to the version you are using (and you can probably use multiple repositories + synaptic to install multiple versions of rocm).  It is described better in the "Multiversion Installation" above.

Personally, I stayed on 2.2 until mine stopped working (which I believe was due to Linux kernel updates) and a bit after others confirmed that a new version worked (3.3 in this case).  Now that I'm on 3.3 and it works, I'll probably stay on this version until there is some real reason to upgrade.

FYI, I believe there also appear to be issues with the newest kernels or Ubuntu 20.04, for example (and it's not officially supported yet anyway): https://github.com/RadeonOpenCompute/ROCm/issues/1117

I hope the devs are tracking these combinations of regressions and future compatibilities.


---

### 评论 #31 — beatboxa (2020-11-10T22:26:05Z)

I tried to upgrade to DaVinci Resolve 17 beta; but this did not launch, likely due to the ROCm 3.3 / OpenCL.  DaVinci Resolve 17 might require newer versions of OpenCL than DaVinci Resolve 16.

In the install notes for ROCm 3.9, they state a clean install is required for 3.3 or older.  I am running multiversion; but when I try to install dev3.9 (multiversion), it asks me to remove the following 3.3 components:
- hcc
- hip-hcc
- hsa-ext-rocr-dev

Has anyone tried this already, before I break my system?

Specifically:
Has anyone gotten DaVinci Resolve 17 working with ROCm 3.3?
Has anyone gotten 3.3 & 3.9 installed together (multi-version)?
Has anyone tested 3.9 with any version of DaVinci Resolve?

Any help is appreciated.  I am trying to keep a single thread going so people have one place for answers.

**EDIT**:  I tried it.  ROCm 3.9 does not appear to work.  Also, it was a pain trying to revert back to ROCm 3.3.

---

### 评论 #32 — KristijanZic (2020-11-12T21:14:10Z)

@beatboxa No, I've tested Resolve 17 on a clean ubuntu 20.04 installation both with AMDGPU-PRO and ROCm. I can install it but it crashes as soon as it loads any media. So yeah, it's 99.9% the drivers fault. 

We've been reporting these problems for years now. I guess they don't test and they don't care. I regret ever buying this Vega 64 Liquid FE GPU only to be constantly dealing with this. It has costed me more than it's weight in gold.

---

### 评论 #33 — beatboxa (2020-11-13T14:08:13Z)

@KristijanZic I agree.  AMD's driver support here is ridiculous.  For the past 20 years I've only ever used AMD / ATI GPUs (including my current Vega64, in this thread), but I think I'm done now.  It's just so stupid that we can't run software, despite hardware capabilities, due to bad drivers.

Just to recap this thread:

Since this thread was started, **only 2 versions of rocm have ever worked with DaVinci Resolve**:  2.2 & 3.3.  That's it.  All the versions in-between or after broke.

- rocm 2.2 worked 1.5 years ago
- rocm 2.3 broke support.  To fix it, one had to turn off the repository, or manually lock versions (which causes all kinds of dependency issues and locks with fundamental software, like linux kernel versions).
- rocm 3.3 was the next version that worked, which was released over 1 year later and was a complete rearchitecture, requiring a complete clean install.  Great.  Except, this is now outdated & does not work with Davinci 17.
- rocm is 3.9 is current, but it does not work.  This is (also) a re-architecture (as was 3.5) and requires a complete clean install from any version 3.3 or earlier.  If you do try to upgrade to 3.9, it is very difficult to go back to 3.3, since the repositories, package names, and dependencies have changed since 3.3 was the current version.  This is despite supposedly having a "multi-version" install, since the paths & architectures have changed so much between 3.3 & 3.9.

These ROCm drivers are the bottleneck on my machine.  I am still running Ubuntu 18.04 due to reports of limited compatibility of ROCm on 20.04.  And despite this, no ROCm version works (at all) with the latest DaVinci Resolve; and the latest ROCm version doesn't work with any version of DaVinci Resolve.

Lesson learned:  if I buy a flagship AMD GPU for video editing, it will be roughly 1 year behind in software compatibility, which defeats the purpose of buying a flagship GPU.  Even though I am using this personally for video editing, I am in the ML industry, and there is a clear bias toward using nVIDIA cards such that I have not worked with any customers who use AMD GPU's.  Now I see why.

I am planning to build a new editing machine in the next year, and I think it will be AMD CPU + nVIDIA GPU.  I have lost patience & faith that this ROCm team knows what it is doing, given all of the re-architectures, regressions, bugs, lack of communication, and slow progress.

---

### 评论 #34 — helloworld1 (2020-11-13T19:27:14Z)

Also tested Rocm 3.9 on CentOS 7. Davinci 17b1 installs fine but won't start and crashed on "GPUDetect". Clearly it freezes and crashes on Rocm since `/opt/rocm/lib/libhsa-runtime64.so` is in the trace.

```
0x7f33d75a3300 | Main                 | INFO  | 2020-11-13 19:22:56,777 | Running DaVinci Resolve v17.0.0b.0007 (Linux/Clang)
0x7f33d75a3300 | Main                 | INFO  | 2020-11-13 19:22:56,777 | BMD_BUILD_UUID 3425bbf0-101b-434d-8fbc-0985de6f6f3b
0x7f33d75a3300 | Main                 | INFO  | 2020-11-13 19:22:56,777 | BMD_GIT_COMMIT 0674653c726c6b3b45527e211d44db730eff2d5c
0x7f33d75a3300 | GPUDetect            | INFO  | 2020-11-13 19:22:56,778 | Starting GPUDetect
0x7f33d75a3300 | GPUDetect            | ERROR | 2020-11-13 19:22:56,828 | X11 logs not found.
0x7f33d75a3300 | Main                 | INFO  | 2020-11-13 19:24:41,258 | Caught termination signal SIGINT, triggering termination routine


==========[CRASH DUMP]==========
Please send this to support:

#TIME Fri Nov 13 19:24:41 2020 - Uptime 00:00:00 (hh:mm:ss)
#PROGRAM_NAME DaVinci Resolve v17.0.0b.0007 (Linux/Clang)
#BMD_BUILD_UUID 3425bbf0-101b-434d-8fbc-0985de6f6f3b
#BMD_GIT_COMMIT 0674653c726c6b3b45527e211d44db730eff2d5c
#BMD_UTIL_VERSION 17.0.0b.0007
#OS Linux

/opt/resolve/bin/resolve() [0x47119a9]
/opt/resolve/bin/resolve() [0x254d081]
/lib64/libpthread.so.0(+0xf630) [0x7f3409d59630]
/opt/resolve/bin/../libs/libgpudetect.so(+0x3bfe4) [0x7f3409b1efe4]
/opt/resolve/bin/../libs/libgpudetect.so(+0x449cf) [0x7f3409b279cf]
/opt/resolve/bin/../libs/libgpudetect.so(+0x1bb02) [0x7f3409afeb02]
/opt/resolve/bin/../libs/libgpudetect.so(+0x1b055) [0x7f3409afe055]
/opt/resolve/bin/resolve() [0x254ad04]
/opt/resolve/bin/resolve() [0x25482bb]
/lib64/libc.so.6(__libc_start_main+0xf5) [0x7f33ea96f555]
/opt/resolve/bin/resolve() [0x254739b]
Signal Number = 2
==========[CRASH DUMP]==========
Please send this to support:

#TIME Fri Nov 13 19:24:41 2020 - Uptime 00:00:00 (hh:mm:ss)
#PROGRAM_NAME DaVinci Resolve v17.0.0b.0007 (Linux/Clang)
#BMD_BUILD_UUID 3425bbf0-101b-434d-8fbc-0985de6f6f3b
#BMD_GIT_COMMIT 0674653c726c6b3b45527e211d44db730eff2d5c
#BMD_UTIL_VERSION 17.0.0b.0007
#OS Linux

/opt/resolve/bin/resolve() [0x47119a9]
/opt/resolve/bin/resolve() [0x254d081]
/lib64/libpthread.so.0(+0xf630) [0x7f3409d59630]
/lib64/libc.so.6(ioctl+0x7) [0x7f33eaa42307]
/opt/rocm/lib/../lib64/libhsakmt.so.1(+0xb058) [0x7f33c9a23058]
/opt/rocm/lib/../lib64/libhsakmt.so.1(hsaKmtWaitOnMultipleEvents+0xde) [0x7f33c9a1d6de]
/opt/rocm/lib/libhsa-runtime64.so.1(+0x6c3b5) [0x7f33ca0eb3b5]
/opt/rocm/lib/libhsa-runtime64.so.1(+0x53e8a) [0x7f33ca0d2e8a]
/opt/rocm/lib/libhsa-runtime64.so.1(+0x65640) [0x7f33ca0e4640]
/opt/rocm/lib/libhsa-runtime64.so.1(+0x166c7) [0x7f33ca0956c7]
/lib64/libpthread.so.0(+0x7ea5) [0x7f3409d51ea5]
/lib64/libc.so.6(clone+0x6d) [0x7f33eaa4b8dd]
Signal Number = 2


```

---

### 评论 #35 — BloodyIron (2020-11-13T19:32:44Z)

@adilad any chance we can get you to chime into this?

---

### 评论 #36 — dbarbi1 (2020-11-22T14:10:32Z)

I went down this rabbit hole again. I'm on Fedora 33, and installed ROCm 3.9 using the instructions from [here](https://rigtorp.se/notes/rocm/) to get around the python dependency issue. I'm able to start Davinci Resolve 16.2 and things seem to work with 1 huge exception, I dont get video in the Preview window!

I can see thumbnails, I get audio, just no video. I can even do things in the fusion tab, and see the output of my effects there, but not the source input... Editing works fine Coloring works fine... Delivery works fine and the videos come out as you would expect... Video is set to display for the track (referring to the sneaky per track button to turn on/off video).

Here is the error i see in the logs repeated over and over:
`[0x7f41e307c640] | DVIP                 | ERROR | 2020-11-21 21:42:06,624 | Failed to register OpenGL object for OpenCL interop: CL_MEM_OBJECT_ALLOCATION_FAILURE.
[0x7f41e307c640] | DVIP                 | ERROR | 2020-11-21 21:42:06,624 | Failed to register GLIO compute interop mapper.
[0x7f43f5d486c0] | UI.GLIO              | WARN  | 2020-11-21 21:42:06,625 | Failed to get texture for Handle68, job was aborted.`

Note that I had to install aomp-amdgpu to get clinfo reporting the correct info and resolve to open.

Resolve 17 beta 2 opens but doesn't display thumbnails or video and eventually crashes.

---

### 评论 #37 — beatboxa (2020-11-23T01:03:33Z)

Resolve 16 is fairly stable and functional for me using ROCm 3.3 (though on Ubuntu...my specs are above).

ROCm 3.9, however, does not work for me.  I'd recommend you try 3.3 if you are going to be using DaVinci Resolve 16; and for version 17, we might need to wait a bit.  You can see above that as far back as ROCm 3.5 appears to have broken quite a bit, including previews for several people, which seems similar to the issues you are running into.

---

### 评论 #38 — dbarbi1 (2020-11-23T02:09:11Z)

I tried with 3.3 today after reading this post, and while Resolve launches it doesn't work for me. Resolve throws a GPU error (error code 59 I believe), and the thumbnails dont render properly and I dont get video in the preview window. Maybe I did something wrong, or didn't install a package?

---

### 评论 #39 — helloworld1 (2020-11-23T02:17:37Z)

@dharbi1 I have exactly the same problem with rocm higher than 3.3. It launches fine but the video preview is blank.

---

### 评论 #40 — beatboxa (2020-11-23T02:32:07Z)

One note:  the previews in Resolve typically take a few minutes to get going (I believe by default, they may get resampled and then cached, and remember, they can be huge and very resource intensive.  This happens fluidly in the background).  You may be able to "resolve" this with some settings, perhaps?  Relevant settings I can think of are in resolve preferences > System > Memory & GPU.  Also, Media Storage (for disk read/write performance).  And decode options.  Then, under User > Playback Settings.

Depending on the combination of your system specs & video sizes, you may want to give it a few minutes.  My system specs (as listed above) often take a few minutes, using 32GB ram with a Vega 64.

---

### 评论 #41 — beatboxa (2020-11-23T02:44:04Z)

As I've been exploring the differences between DaVinci Resolve 16 & 17, I think I may see one primary difference.  When launching resolve 17, I get the following relevant portions in the log files (This is all using ROCm 3.3):

[0x7f2ef69d22c0] | Main                 | INFO  | 2020-11-22 21:08:02,442 | Running DaVinci Resolve v17.0.0b.0009 (Linux/Clang)
[0x7f2ef69d22c0] | Main                 | INFO  | 2020-11-22 21:08:02,442 | BMD_BUILD_UUID cc27b577-2232-4b14-93a4-7d70edf7796a
[0x7f2ef69d22c0] | Main                 | INFO  | 2020-11-22 21:08:02,442 | BMD_GIT_COMMIT b9db89f8c530fdab7e72ffa9d9e39e2040011a81
[0x7f2ef69d22c0] | GPUDetect            | INFO  | 2020-11-22 21:08:02,445 | Starting GPUDetect

^ I cancelled when it hung there, as it consistenly has.  Whereas on Resolve 16.2.2, here is what I get:

[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,495 | Running DaVinci Resolve v16.2.2.012 (Linux/Clang)
[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,496 | Updating display GPU information...
[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,593 | Detecting Main Display properties
[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,602 | Process to detect main display has finished
**[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,616 | Fallback process to detect main display has finished**
[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,616 | GPU Name = 'Vega 10 XT [Radeon RX Vega 64]', Main display = 0
[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,617 | Not GLmap capable. GPUs: 1 discrete, 0 integrated, 0 external. Auto mapping, OpenCL processing, main display not on external GPU.
[0x7fe76e7ab100] | Main                 | INFO  | 2020-11-22 21:14:16,617 | Setting LsManager.3.NumGPUs = 1

ie. on Resolve 17, it hangs on "Starting GPUDetect," and on Resolve 16, it appears there's some sort of fallback process, where if the primary process to identify the GPU crashes or fails, an alternate method is used.  And this alternate "fallback" method might be the one that has been picking up the GPU.  Perhaps this is nvidia CUDA primary, and then fallback is OpenCL or something?

I don't know if this is a ROCm thing or a DaVinci Resolve 17 thing, since ideally, ROCm would work with the primary method.  But does this make sense to anyone here?  Is anyone also on the BlackMagic forums who has an answer from there?

---

### 评论 #42 — dbarbi1 (2020-11-23T02:56:03Z)

Ok, so I went back and tried with ROCm 3.3 and things are working now with Resolve 16. I suppose that I missed a few of the ROCm packages needed when I tried the first time. Just in case it helps someone else, I'll paste my instructions below.

I gave Resolve 17 a try, but it didn't work. It launches, but the clips and previews are blank, and then after a few minutes it crashes.

Instructions I used to install ROCm 3.3 in Fedora 33:
```
Create the /etc/yum.repos.d/rocm.repo with the following:
[ROCm]
name=ROCm
baseurl=http://repo.radeon.com/rocm/yum/3.3/
enabled=1
gpgcheck=0

download and force install hcc
sudo dnf download hcc
sudo rpm -ifvh hcc... --nodeps

sudo dnf install aomp-amdgpu.x86_64 comgr.x86_64 hip-base.x86_64 hip-doc.x86_64 hip-samples.x86_64 hipblas.x86_64 hipcub.x86_64 hipsparse.x86_64 hsa-amd-aqlprofile.x86_64 hsa-rocr-dev.x86_64 hsakmt-roct.x86_64 hsakmt-roct-devel.x86_64 miopen-hip.x86_64 rocalution.x86_64 rocblas.x86_64 rocfft.x86_64 rocm-clang-ocl.x86_64 rocm-cmake.x86_64 rocm-dev.x86_64 rocm-device-libs.x86_64 rocm-libs.x86_64 rocm-opencl.x86_64 rocm-opencl-devel.x86_64 rocm-utils.x86_64 rocprim.x86_64 rocprofiler-dev.x86_64 rocrand.x86_64 rocsolver.x86_64 rocsparse.x86_64 rocthrust.x86_64 roctracer-dev.x86_64

make sure '/etc/OpenCL/vendors' only has one icd.

symlink /opt/rocm to /opt/rocm-3.3.0 if it isn't already
ln -s /opt/rocm-3.3 rocm
```

---

### 评论 #43 — BloodyMess (2022-03-16T03:59:27Z)

I've got DaVinci Resolve 17.4.5 build 7 mostly working on elementary 5.1.7 (ubuntu 18.04), with a radeon RX590.

Blender Cycles is working fine now.

Here's a demo of the results:
https://youtu.be/u_TQaArfROE

---

### 评论 #44 — BloodyIron (2022-03-16T14:40:14Z)

So ROCm is now 5.0.2 and I can't actually tell if AMD Consumer GPUs will have OpenCL offloading support at all... what's going on?

---

### 评论 #45 — ppanchad-amd (2024-05-07T19:47:38Z)

@beatboxa Sorry for the lack of response.  Please check with ROCm 6.1.0. If resolved, please close ticket. Thanks!

---

### 评论 #46 — beatboxa (2024-05-14T20:51:11Z)

@ppanchad-amd I have since purchased an nvidia GPU for a new audio/video workstation (and it works), due specifically to this issue.  But I do still use the machine referred to in this thread.  I believe that machine is still on rocm 3.3, as that was the latest version that worked for me in over the 5 years since I first opened this ticket in April 2019 (it is now May 2024).

I will find time to check if the issue is resolved and update this issue with the results.  It may take a bit, because I also have to find time to read up on how to reverse the changes, should the machine fail to boot, since this happened so frequently during previous upgrades that I had to hold back any upgrades to AMD's rocm.

---

### 评论 #47 — harkgill-amd (2024-07-09T19:03:35Z)

Hi @beatboxa, jumping from #1397. Did you get a chance to try out DaVinci Resolve with ROCm since your last comment on this issue? I was not able to reproduce any of the older issues seen in the thread above.

---

### 评论 #48 — harkgill-amd (2024-08-15T14:10:23Z)

I will close out this ticket as the original issue of DaVinci Resolve failing has since been resolved. @beatboxa if you do encounter any issues with DaVinci Resolve on ROCm 6.1.3, please create a new GitHub issue and we can investigate it further from there. Thanks!

---
