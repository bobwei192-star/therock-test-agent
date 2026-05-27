# make rocm work with "ASUS TUF505DY"

> **Issue #750**
> **状态**: closed
> **创建时间**: 2019-03-20T23:59:33Z
> **更新时间**: 2023-12-18T18:52:17Z
> **关闭时间**: 2023-12-18T18:52:17Z
> **作者**: Djip007
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/750

## 描述

I am the happy owner of the new "ASUS TUF505DY" notebook. it have the new "AMD Ryzen 5 3550H" (With Vega/Raven GPU) CPU and a "Radeon RX560X" GPU

I manage to instal Fedora29 (no success with Centos7...) I know it is not et suported OS... but i like to help
I will update all firmware ( picasso firmware) for Ryzen APU from the linux-firmware repo.
I build the last kernel (5.0.3) patching kfd_device.c with the id of the Raven:

```
diff --git a/drivers/gpu/drm/amd/amdkfd/kfd_device.c b/drivers/gpu/drm/amd/amdkfd/kfd_device.c
index 8be9677c0c07..73e722cc6ae2 100644
--- a/drivers/gpu/drm/amd/amdkfd/kfd_device.c
+++ b/drivers/gpu/drm/amd/amdkfd/kfd_device.c
@@ -319,6 +319,7 @@ static const struct kfd_deviceid supported_devices[] = {
        { 0x9875, &carrizo_device_info },       /* Carrizo */
        { 0x9876, &carrizo_device_info },       /* Carrizo */
        { 0x9877, &carrizo_device_info },       /* Carrizo */
+       { 0x15D8, &raven_device_info },         /* Raven */
        { 0x15DD, &raven_device_info },         /* Raven */
 #endif
        { 0x67A0, &hawaii_device_info },        /* Hawaii */
```

after that the dmesg look good: (I am not sure it have to be done like this...)
```
> dmesg | grep kfd
[    2.492929] kfd kfd: Allocated 3969056 bytes on gart
[    2.494745] kfd kfd: added device 1002:67ef
[    2.653922] kfd kfd: Allocated 3969056 bytes on gart
[    2.654235] kfd kfd: added device 1002:15d8
```

after some install of centos rpm (rocm2.2) rocminfo report:
```
hsa api call failure at line 952, file: /home/philou/tmp/rocm/rocminfo/rocminfo.cc. Call returned 4104
```

after read some issus report I uninstall all rocm rpm and clone rocm repo (master branche):
```
> ROCT-Thunk-Interface
> ROCR-Runtime
> rocminfo
```

all are build with DEBUG for use with gdb.

I Path ROCT-Thunk-Interface to add device 1002:15d8 (Raven...)

```
#> ROCT-Thunk-Interface
diff --git a/src/topology.c b/src/topology.c
index c7f8a28..c4b9e98 100644
--- a/src/topology.c
+++ b/src/topology.c
@@ -200,6 +200,7 @@ static struct hsa_gfxip_table {
        { 0x69A3, 9, 0, 4, 1, "Vega12", CHIP_VEGA12 },
        { 0x69Af, 9, 0, 4, 1, "Vega12", CHIP_VEGA12 },
        /* Raven */
+       { 0x15D8, 9, 0, 2, 0, "Raven", CHIP_RAVEN },
        { 0x15DD, 9, 0, 2, 0, "Raven", CHIP_RAVEN },
        /* Vega20 */
        { 0x66A0, 9, 0, 6, 1, "Vega20", CHIP_VEGA20 },
```

and track rocminfo with gdb.
I finish in 'ROCT-Thunk-Interface'/src/openclose.c
```
HSAKMT_STATUS HSAKMTAPI hsaKmtOpenKFD(void)
{
	HSAKMT_STATUS result;
	int fd;
	HsaSystemProperties sys_props;

	pthread_mutex_lock(&hsakmt_mutex);

	/* If the process has forked, the child process must re-initialize
	 * it's connection to KFD. Any references tracked by kfd_open_count
	 * belong to the parent
	 */
	if (is_forked_child())
		clear_after_fork();

	if (kfd_open_count == 0) {
		init_vars_from_env();

		fd = open(kfd_device_name, O_RDWR | O_CLOEXEC);

// > fd = -1...
// > errno = EAGAIN
```

I find in 'drivers/gpu/drm/amd/amdkfd/kfd_device.c' it can be probleme with reset...

I don't know how to debug inside kfd kernel module (i need more time with google ;))

With dmesg I have many reset...
```
[   14.164505] amdgpu 0000:01:00.0: GPU pci config reset
[   29.774100] amdgpu 0000:01:00.0: GPU pci config reset
[   36.345021] amdgpu 0000:01:00.0: GPU pci config reset
```

[dmesg-5.0.3.txt](https://github.com/RadeonOpenCompute/ROCm/files/2990489/dmesg-5.0.3.txt)


---

## 评论 (21 条)

### 评论 #1 — Djip007 (2019-03-22T00:29:08Z)

OK I add some trace in "drivers/gpu/drm/amd/amdkfd/kfd_device.c" to track the lock...
dmesg give:
```
[    2.640380] kfd kfd: Allocated 3969056 bytes on gart
[    2.642222] kfd kfd: kfd_resume 1002:67ef
[    2.642590] kfd kfd: added device 1002:67ef
[    2.794867] kfd kfd: Allocated 3969056 bytes on gart
[    2.794964] kfd kfd: kfd_resume 1002:15d8
[    2.795207] kfd kfd: added device 1002:15d8
[   14.689643] kfd kfd: kgd2kfd_suspend 1002:67ef
[   14.689650] kfd kfd: kfd_locked++ 1002:67ef
[   28.151503] kfd kfd: kgd2kfd_resume 1002:67ef
[   28.151506] kfd kfd: kfd_resume 1002:67ef
[   28.151548] kfd kfd: kfd_locked-- 1002:67ef
[   37.695902] kfd kfd: kgd2kfd_suspend 1002:67ef
[   37.695908] kfd kfd: kfd_locked++ 1002:67ef
[   38.407090] kfd kfd: kgd2kfd_resume 1002:67ef
[   38.407092] kfd kfd: kfd_resume 1002:67ef
[   38.407133] kfd kfd: kfd_locked-- 1002:67ef
[   45.264709] kfd kfd: kgd2kfd_suspend 1002:67ef
[   45.264716] kfd kfd: kfd_locked++ 1002:67ef
[  164.478025] kfd kfd: kfd_is_locked => 1
```
if I don't make mistake:
 - 1002:15d8  is the RAVEN eGPU
 - 1002:67ef is the RX560X ...
so after some suspend/resume on the RX560... it finish with a suspend...
the last trace is when I call rocminfo => result in global lock => EAGAIN in open(/dev/kfd)

now I know what happen... but not why
That's all for today... 

---

### 评论 #2 — jlgreathouse (2019-03-22T00:31:50Z)

Hi @Djip007 

I'll note that, at this time, [iGPU + dGPU configurations are not supported in ROCm](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-450692695). As such, I suspect that that may be part of the underlying issue you're seeing. If you would like to use ROCm on your laptop, you may try disabling either the integrated or discrete GPU in your BIOS.

---

### 评论 #3 — Djip007 (2019-03-24T16:59:57Z)

Ok some more news.
I know wy /dev/kdf is lock...
```
[philou@localhost rocm]$ cat /sys/bus/pci/drivers/amdgpu/*/power/control
dGPU > auto
iGPU > on
[philou@localhost rocm]$ cat /sys/bus/pci/drivers/amdgpu/*/power/runtime_status
dGPU > suspended
iGPU > active
```
the dGPU is suspend after 5s... 
after activated : 
```
echo on | sudo tee /sys/bus/pci/drivers/amdgpu/0000\:01\:00.0/power/control
``` 
it is much good... (but us 2W more power ;) ):
```
[zzzz@localhost rocm]$ ./rocminfo/build/rocminfo 
LoadLib(libhsa-ext-finalize64.so.1) failed: libhsa-ext-finalize64.so.1: cannot open shared object file: No such file or directory
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 3550H with Radeon Vega Mobile Gfx
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
    L1:                      32(0x20) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Frequency (MHz):2100                               
  BDFID:                   1280(0x500)                        
  Compute Unit:            8(0x8)                             
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    8388224(0x7ffe80) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx902                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 5592(0x15d8)                       
  Cacheline Size:          64(0x40)                           
  Max Clock Frequency (MHz):1200                               
  BDFID:                   1280(0x500)                        
  Compute Unit:            11(0xb)                            
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Waves Per CU:            160(0xa0)                          
  Max Work-item Per CU:    10240(0x2800)                      
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx902+xnack    
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
Agent 3                  
*******                  
  Name:                    gfx803                             
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26607(0x67ef)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Frequency (MHz):1223                               
  BDFID:                   256(0x100)                         
  Compute Unit:            14(0xe)                            
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Waves Per CU:            40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max number Of fbarriers Per Workgroup:32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    4194304(0x400000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx803          
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
rocminfo: /home/philou/tmp/rocm/ROCR-Runtime/src/core/runtime/amd_memory_region.cpp:68: static void amd::MemoryRegion::FreeKfdMemory(void*, size_t): Assertion `status == HSAKMT_STATUS_SUCCESS' failed.
Abandon (core dumped)


[zzzz@localhost rocm]$ clinfo 
LoadLib(libhsa-ext-finalize64.so.1) failed: libhsa-ext-finalize64.so.1: cannot open shared object file: No such file or directory
malloc(): invalid size (unsorted)
Abandon (core dumped)
```
well like @jlgreathouse point it is an other probleme...

---

### 评论 #4 — Djip007 (2019-03-24T17:17:00Z)

Next. I don't have option (as may other) have option to deactivate GPU in BIOS...
To "remove" dGPU I had a look on how to use pciePassTrough for VM... (https://wiki.archlinux.org/index.php/PCI_passthrough_via_OVMF#Isolating_the_GPU)
I build my kernel with "vfio_pci" buildin ...
```
#add in boot kernel param:
vfio-pci.ids=1002:67ef
```
and evry thing work (rocminfo & clinfo... test with dacktable)
I don't succes with activate only dGPU... but may be impossible lock like is use PRIM MUXless... 

---

### 评论 #5 — Djip007 (2019-03-24T17:21:49Z)

So next I'll try make rocm work with dGPU on centosVM with pcipassthrough...
Is it possible to mainline the Raven (id=0x15D8) in next release?

---

### 评论 #6 — Djip007 (2019-04-12T01:14:55Z)

Picasso id is on the way.
https://cgit.freedesktop.org/~agd5f/linux/commit/?h=drm-fixes-5.1&id=e7ad88553aa1d48e950ca9a4934d246c1bee4be4


---

### 评论 #7 — Djip007 (2019-05-14T19:39:08Z)

After apply my patch (https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-491582954) on kernel 5.1.1 on fedora 30 I manage to reinstall rocm (version 2.4)

what I did:
- Add ROCm repos like for Centos.
- insall:
 > dnf install rocm-opencl
 > dnf install rocm-smi
 > dnf install rocminfo 
 > dnf install hsakmt-roct
 > dnf remove hsakmt

hsakmt need to be remove  => fedora have old version buildin (=> hsakmt.x86_64   1.0.6-8.rocm2.0.0.fc30  @fedora)

rocminfo is pik from fedora repo... 

some come from ROCm repo other from fedora:
```
sudo dnf list installed | grep roc
hsa-rocr-dev.x86_64                               1.1.9_68_gc862c1cf-1                    @ROCm                             
hsakmt-roct.x86_64                                1.0.9_139_g126c93b-1                    @ROCm                             
rocm-opencl.x86_64                                1.2.0-2019050359                        @ROCm                             
rocm-smi.x86_64                                   1.0.0_129_g71924de-1                    @ROCm                             
rocminfo.x86_64                                   1.0.0-2.fc30                            @fedora      
```
with that and kernel param : "amdgpu.rocm_mode=3" (ie raven iGPU in use)
rocminfo & clinfo success

with that and kernel param : "amdgpu.rocm_mode=2" (ie RX560X dGPU in use)
rocminfo & clinfo success
juste like before the GPU is in suspend stat nead to turn it on:
`echo on | sudo tee /sys/bus/pci/drivers/amdgpu/0000\:01\:00.0/power/control`

----------------------------------------
Note: 'dnf install rocm-dev' because of hcc depend 
```
 Problème: package rocm-dev-2.4.25-1.x86_64 requires hcc, but none of the providers can be installed
  - conflicting requests
  - nothing provides pth needed by hcc-1.3.19174-1.x86_64
```
may be can be remove from this package dependency (can make sense on this deprecated package)

---

### 评论 #8 — sos-michael (2019-05-26T05:03:45Z)

this will do to solve that problem:
https://copr.fedorainfracloud.org/coprs/fatka/pth/monitor/

>  Problème: package rocm-dev-2.4.25-1.x86_64 requires hcc, but none of the providers can be installed
>   - conflicting requests
>   - nothing provides pth needed by hcc-1.3.19174-1.x86_64
> ```
> 
> may be can be remove from this package dependency (can make sense on this deprecated package)



---

### 评论 #9 — Djip007 (2019-05-28T21:19:32Z)

next test on fedora30:
thanks @sos-michael

install rocm lib for tensorflow
```
sudo dnf copr enable fatka/pth 
sudo dnf install pth
sudo dnf install rocm-libs
sudo dnf install miopen-hip
sudo dnf install cxlactivitylogger
```

install rocm-tensorflow in virtual env.
and jupyter notebook (for simple test.)
```
python3.7 -m venv ./rocm
source ./rocm/bin/activate
pip install --upgrade pip
pip install tensorflow-rocm
pip install jupyter notebook
```

start jupyter?
```
jupyter notebook
```

test sample code:
```
import tensorflow as tf

hello = tf.Variable("hello world")

sess = tf.Session()
init = tf.global_variables_initializer()

sess.run(init)
sess.run(hello)
```
result for dGPU
=> 

```
WARNING:tensorflow:From /home/philou/Developpement/python/rocm/lib64/python3.7/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.

b'hello world'
```

It work... (yes I know... et very simple test...)

but on iGPU it failed:
```
FailedPreconditionError: Failed to memcopy into scratch buffer for device 0
```
not sure if it have or not... but look like it try to alloc to much memory (31Go of my 32Go...) more than the 3/8 allowed... don't know if it can be correct... and where...
any way not that bad for this fedora test.

```
name: AMD Ryzen 5 3550H with Radeon Vega Mobile Gfx
AMDGPU ISA: gfx902
memoryClockRate (GHz) 1.2
pciBusID 0000:05:00.0
Total memory: 32.00GiB
Free memory: 31.75GiB
2019-05-28 23:07:05.516984: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1642] Adding visible gpu devices: 0
2019-05-28 23:07:05.516995: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1053] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-05-28 23:07:05.517000: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1059]      0 
2019-05-28 23:07:05.517006: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1072] 0:   N 
2019-05-28 23:07:05.517047: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1189] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 30886 MB memory) -> physical GPU (device: 0, name: AMD Ryzen 5 3550H with Radeon Vega Mobile Gfx, pci bus id: 0000:05:00.0)
2019-05-28 23:07:09.110206: E tensorflow/stream_executor/rocm/rocm_driver.cc:461] failed to memset memory: HIP_ERROR_InvalidValue
```


---

### 评论 #10 — benkenobi007 (2019-07-04T07:03:57Z)

> To "remove" dGPU I had a look on how to use pciePassTrough for VM... (https://wiki.archlinux.org/index.php/PCI_passthrough_via_OVMF#Isolating_the_GPU)
I build my kernel with "vfio_pci" buildin 

@Djip007 Did the PCI passthrough disable the dGPU or did it consider the iGPU to be the only provider ?

Further, I feel that it would be more beneficial to have a switch similar to DRI_PRIME to change the active GPU depending on the need. Is this feasible ?

---

### 评论 #11 — Djip007 (2019-07-20T14:16:04Z)

@benkenobi007 sorry did not see your post..
pci path through disable GPU for the host only VM guest can use it.

For DRI_PRIME like I have a patch here: (but you have to chose at boot-time)
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-491582954

It make chose if iGPU or dGPU is assigne to rocm at boot time. that way both GPU is usable for OpenGL/Vulkan... 

(but I thing you find it ;)... )

May be I have to make a new poste for this Patch et try to make it upsteam... (If someone can help point what process to follow to try made it upsteam)

---

### 评论 #12 — alfabuster (2019-09-07T14:29:16Z)

@Djip007 I have the same laptop. And I tried to install rocm on Ubuntu 19.04. Resault is broken system.
Problem is absent support from AMD for rx560x on linux systems.

I wrote to amd on this topic, they answered like this...

> Thank you for the email,
Currently we donot have the support, At this point of time I cannot comment on the future releasing,I will make a note of this issue and report to the driver team
Thanks for contacting AMD

Do you have any good news?


---

### 评论 #13 — Djip007 (2019-09-07T19:24:55Z)

RX560X work with rocm, problem is with the mix on iGPU+dGPU.
I dont know which kernel use Ubuntu (I use Fedora) ...

More info/patch here:
https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-520846346

May be you can point it to AMD... 
Anyway can you report some of your error log to be sur it is the same problem?

---

### 评论 #14 — alfabuster (2020-03-27T07:59:52Z)

Unfortunately not. I delete my Ubuntu distro. 

But, are you sure on Fedora Rocm is work properly?  If it is maybe possible to launch Davinci Resolve on Fedora now, because without it, I've got crash on start... 

---

### 评论 #15 — Djip007 (2020-04-18T23:45:03Z)

use it with tensorflow like that:
```
podman run -it \
    --network=host \
    --device=/dev/kfd \
    --device=/dev/dri \
    --ipc=host \
    --shm-size 16G \
    -v $PWD:/root/home\
    rocm/tensorflow:latest
```
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/935

(with the patch: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-615980464 ...)

I don't test recently local install... but use to make darktable working with OpenCL 

---

### 评论 #16 — ROCmSupport (2021-01-07T11:11:29Z)

Hi @Djip007 
Is the issue gone with the recent releases? Please share some update on this.
Thank you.

---

### 评论 #17 — Mireuz13 (2021-01-21T01:59:10Z)

Sorry for the question @Djip007 , but ill gonna install Fedora because on Ubuntu 20.04 ROCM dont run in this laptot... I am very noob in Linux, can u explain me how i use the patch you upload on Fedora 33? and this patch automatically take the RX560X and disable Vega?. Need another driver to install maybe or just be okey with POLARIS 11? and need install the package on rocm, because in rocm documentation page say " newer versions of Ubuntu may not be compatible with the rock-dkms kernel driver. In this case, you can exclude the rocm-dkms and rock-dkms packages" and this version on UBUNTU use a Kernel 5.8

Thanks for the time to answer me , Have a great day 

---

### 评论 #18 — Shreyashwaghe (2021-04-30T20:59:34Z)

@Djip007 did you tried the new rocm 4.0 or 4.1 release, rocm got official (beta) support from pytorch. 
I have acer nitro 5 ryzen 2500u, radeon rx vega 8 and radeon rx560x. I am trying on ubuntu 20.04, not able to get it work.
I dont mind switching distros, or other things, i just want this rocm to get it work on rx560x, so i can use the beta supported pytorch

---

### 评论 #19 — Djip007 (2021-04-30T21:28:08Z)

Hello All...
Sorry didn't see last comment... I need some time to test with the APU+rx560X with resent rocm release...
I had some sucess with a old RX480 (other POLARIS) + Ryzen 9 3900X and rocm-4.0...
In that case I use Fedora with default kernel and rocm create with centos8+rocm4.0+jupyterlab&tensorflow-rocm...

Trie to have some times to test and report result...  

(For the APU+RX560X need to pach the kernel https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66#issuecomment-743742192 to chose the GPU to use ... And I have the patch for kernel 5.10 & 5.11 if needed... but think the patch for 5.9 kernel work on last kernel...)

---

### 评论 #20 — tasso (2023-12-11T14:42:52Z)

Has this issue been resolved?  If so, can we please close it?

---

### 评论 #21 — tasso (2023-12-18T18:52:17Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
