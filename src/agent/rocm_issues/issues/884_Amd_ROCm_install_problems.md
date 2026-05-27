# Amd ROCm install problems

> **Issue #884**
> **状态**: closed
> **创建时间**: 2019-09-12T07:30:51Z
> **更新时间**: 2021-07-09T08:05:56Z
> **关闭时间**: 2021-07-09T08:04:08Z
> **作者**: ITfirewall
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/884

## 描述

     Hi  Rocm Team,

     I 'm new with Amd ROCm drivers. In the old times I was able to run computing applications with catalsty drivers. 
***Using Ubuntu 16.04 full updated and upgraded.
     
     I cant install ROCm.  Have some problems in commands or in the repositorys??????

     I tried to install the ROCm driver in ubuntu,  following the guide on the page:
     
  ''Ubuntu Support - installing from a Debian repository''
The following directions show how to install ROCm on supported Debian-based systems such as Ubuntu 18.04. These directions may not work as written on unsupported Debian-based distributions. For example, newer versions of Ubuntu may not be compatible with the rock-dkms kernel driver. As such, users may want to skip the rocm-dkms and rock-dkms packages, as described above, and instead use the upstream kernel driver.

  *First make sure your system is up to date
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot

  *Add the ROCm apt repository
    For Debian-based systems like Ubuntu, configure the Debian ROCm repository as follows:
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key
sudo apt-key add - echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main'
sudo tee /etc/apt/sources.list.d/rocm.list

I typed in terminal:

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key 

******this command ABOVE work right, got and showed the key numbers in terminal.

***The next command BELOW dont work,   after I typed it,,  dont show nothing,, still stuck.........''

sudo apt-key add - echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main'

What is happening?????
What I need to do??

Please, If have a more right way to install ROCm in ubuntu, talk to me, I 'm trying many times with no success.  I have one RX Vega 56 (Vega 10), and I will get a new RX Vega 64 too!!

I appreciated all help.


---

## 评论 (18 条)

### 评论 #1 — heero-yuy (2019-09-12T08:40:13Z)

HI,

May you confrim the following type is OK? Thanks :

# wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -

# echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list



---

### 评论 #2 — ITfirewall (2019-09-14T04:25:32Z)

 Hi  Heero-yuy,  

 The commands above are working 100%.  Sorry for the delay (I was in business). 

 Almost in the end of install, it showed in terminal a message about ''possible missing files''. however I checked the install with the commands in ROCm page and it showed the driver installed right in Ubuntu.

 I will do a fresh install to check again (Ubuntu full updated/upgraded + ROCm driver only) and I will test a tool with ROCm driver to see the performance. 

Thank you.
 I 'll be back.

---

### 评论 #3 — ITfirewall (2019-09-17T18:35:29Z)

 Hi Heero-yu,  

 I did a fresh install in Ubuntu 18.04, full updated & upgraded, last ROCm installed 100% right.

 After I installed the tool (like I said in message above) and start testing it, I noticed some error with OPEN CL (ROCm) in the middle of the test.
  
 I went to IRC channel (free node) from the developer of the tool to talk with the admins / users about the error. They said this error is strange because I am using the right software + hardware and the other people using RX Vegas 10 (both gpus 56 and 64) never had or reported this error before.
   
 Something changed in the ROCm driver since '' 2.7.....''  is causing the problem.
 What can be??
 Someone are using RX Vegas 10 with older ROCm drivers (2.6 , 2.5....) ??
  
    

---

### 评论 #4 — heero-yuy (2019-09-19T01:06:53Z)

Hi,

Please let me know with following information:

1. for Ubuntu 18.04.3 Desktop, the default Kernel for HWE is 5.0, which is not useful for ROCm dkms, so if you can, please type the command and provide the version number: 

# uname -r

2. For some reasons, it seems that the newer generation of CPU which is equipped OpenCL 2.1 may cause the openCL error by querying deviceid, but it should be fixed on ROCm 2.7.1,if you can, please type the command and provide the CPU model:

# lscpu

Thanks,
Heero.

---

### 评论 #5 — ITfirewall (2019-09-20T04:23:19Z)

 Hi  Heero-yuy,
 
 Whats your hardware + O.S. and ROCm  ??  
 I tried today with Ubuntu 16.04 (kernel 4.15...) full updated & upgraded + ROCm 2.7.1 (last) and I got the same error with OpenCL in that tool.
 What can be??
  
 Info below ubuntu 18.04 LTS:
knight@Knight-One:~$ uname -r
5.0.0-27-generic

knight@Knight-One:~$ lscpu
Architecture:        x86_64 CPU 
op-mode(s):          32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):                      4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):                  1
NUMA node(s):         1 
Vendor ID:                GenuineIntel
CPU family:               6
Model:                      94
Model name:          Intel(R) Core(TM) i5-6600 CPU @ 3.30GHz
Stepping:                   3
CPU MHz:                  800.085
CPU max MHz:         3900.0000
CPU min MHz:           800.0000
BogoMIPS:                6624.00
Virtualization:             VT-x
L1d cache:                   32K
L1i cache:                     32K
L2 cache:                    256K
L3 cache:                   6144K
NUMA node0 CPU(s):    0-3
Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp md_clear flush_l1d
knight@Knight-One:~$ 

Thank you.

---

### 评论 #6 — heero-yuy (2019-09-20T08:25:37Z)

HI,

Your CPU is Skylake-S, shouldn't have problem due to support only OpenCL 2.0...
May you provide what result when you execute /opt/rocm/bin/rocminfo & /opt/rocm/bin/rocm-smi ?

Thanks,
Heero.

---

### 评论 #7 — ITfirewall (2019-09-21T20:57:35Z)

 Hi Heero-yuy,
 
 I will try ROCm 2.6 in ubuntu 16.04 to see what happen with that Tool.
The big question is what is causing the OpenCL problem.......

 Info below ubuntu 18.04 LTS:

 knight@Knight-One:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
knight is member of video group
=====================    
HSA System Attributes    
=====================    
Runtime Version: 1.1
System Timestamp Freq.: 1000.000000MHz
Sig. Max Wait Duration: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model: LARGE                              
System Endianness: LITTLE                             
==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                  Intel(R) Core(TM) i5-6600 CPU @ 3.30GHz
  Marketing Name: Intel(R) Core(TM) i5-6600 CPU @ 3.30GHz
  Vendor Name:     CPU                                
  Feature:               None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode: NEAR                               
  Max Queue Number: 0(0x0)                             
  Queue Min Size:        0(0x0)                             
  Queue Max Size:        0(0x0)                             
  Queue Type:              MULTI                              
  Node:                        0                                  
  Device Type:              CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3900                               
  BDFID:                         0                                  
  Internal Node ID:         0                                  
  Compute Unit:             4                                  
  SIMDs per CU:             0                                  
  Shader Engines:            0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                         16352956(0xf986bc) KB              
      Allocatable:              TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:       4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                         16352956(0xf986bc) KB              
      Allocatable:               TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:       4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                          gfx900                             
  Marketing Name:          Vega 10 XT [Radeon RX Vega 64]     
  Vendor Name:              AMD                                
  Feature:                        KERNEL_DISPATCH                    
  Profile:                          BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:     128(0x80)                          
  Queue Min Size:            4096(0x1000)                       
  Queue Max Size:            131072(0x20000)                    
  Queue Type:                  MULTI                              
  Node:                    1                                  
  Device Type:              GPU                                
  Cache Info:              
    L1:                               16(0x10) KB                        
  Chip ID:                         26751(0x687f)                      
  Cacheline Size:                64(0x40)                           
  Max Clock Freq. (MHz):   1590                               
  BDFID:                            768                                
  Internal Node ID:                   1                                  
  Compute Unit:                      56                                 
  SIMDs per CU:                        4                                  
  Shader Engines:                      4                                 
  Shader Arrs. per Eng.:              1                                  
  WatchPts on Addr. Ranges:     4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:            FALSE                              
  Wavefront Size:                   64(0x40)                           
  Workgroup Max Size:        1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:            40(0x28)                           
  Max Work-item Per CU:     2560(0xa00)                        
  Grid Max Size:                   4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                          8372224(0x7fc000) KB               
      Allocatable:                TRUE                               
      Alloc Granule:             4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:          FALSE                              
    Pool 2                   
      Segment:                    GROUP                              
      Size:                            64(0x40) KB                        
      Allocatable:                 FALSE                              
      Alloc Granule:             0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:          FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                           amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                        HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                            TRUE                               
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
knight@Knight-One:~$ 
knight@Knight-One:~$ /opt/rocm/bin/rocm-smi
====ROCm System Management Interface=
GPU  Temp   AvgPwr  SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
  0    36.0c  4.0W    852Mhz  167Mhz  37.65%  auto  180.0W    4%   0%    
====End of ROCm SMI Log=
knight@Knight-One:~$ 

Thank you.

---

### 评论 #8 — heero-yuy (2019-09-22T09:23:53Z)

Hi,
 As my throught, That's a different on Ubuntu 16.04/18.04 which is following:

16.04 : Kerenl 4.4 / HWE Kernel 4.15 (under supported with ROCm)
18.04 : Kernel 4.15 / HWE Kernel 5.0 (5.0 still has problem with ROCm)

if confirmed 18.04 has problem by openCL clinfo discovered, it's better to downgrade kernel to the supported version.

Thanks,
Heero.

---

### 评论 #9 — ITfirewall (2019-09-23T06:58:29Z)

Hi heero-yuy,
Lets start again....... friend
I tried with a fresh install, Ubuntu 16.04 (kernel 4.15) updated & upgraded + ROCm 2.7.1 driver. I 'm getting this error with the tool, I did a benchmark:
''''clBuildProgram(): CL_BUILD_PROGRAM_FAILURE''"

* Device #1: Kernel /home/knight/Hashcat/hashcat-4.2.1/OpenCL/m02500-pure.cl build failed - proceeding without this device.

* I tried 3 versions of the same tool, 4.2.1 , 5.0.0 and the last 5.1.0. The problem isn't in the tool, had other people running hashcat with ROCm drivers some months ago and I saw it!!
  Where is the error and how I can fix it???

 Thank you.   

---

### 评论 #10 — heero-yuy (2019-09-26T03:03:00Z)

Hi,

I need time to check the hashcat with openCL processing & compling, thanks!

---

### 评论 #11 — ITfirewall (2019-10-10T16:35:42Z)

Hi heero-yuy, how are you??

Did you test hashcat with OpenCL (ROCm) processing & compling??

** I 'm waiting a solution for the problem. Since those day, I 'm trying to fix the problem.

Ty.

---

### 评论 #12 — heero-yuy (2019-10-11T08:56:58Z)

Hi,

I've checked that the Ubuntu 18.04.3 with ROCm 2.9 is workable by Hashcat 5.1.0 with following:

Kernel : 4.15.0-65
ROCm 2.9
GPU : RX470 & RX550

Logs:

agito@agito-B85M-D3V:~/Downloads/hashcat-5.1.0$ ./example0.sh 
hashcat (v5.1.0) starting...

/sys/bus/pci/devices/0000:01:00.0/hwmon/hwmon2/pwm1: No such file or directory

OpenCL Platform #1: Advanced Micro Devices, Inc.
================================================
* Device #1: gfx803, 1740/2048 MB allocatable, 8MCU

Dictionary cache hit:
* Filename..: example.dict
* Passwords.: 128416
* Bytes.....: 1069601
* Keyspace..: 128416

Hashes: 6494 digests; 6494 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Temperature abort trigger set to 90c

INFO: Removed 1781 hashes found in potfile.

Dictionary cache hit:
* Filename..: example.dict
* Passwords.: 128416
* Bytes.....: 1069601
* Keyspace..: 134653935616

Cracking performance lower than expected?        

* Append -O to the commandline.
  This lowers the maximum supported password- and salt-length (typically down to 32).

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Update your OpenCL runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

[s]tatus [p]ause [b]ypass [c]heckpoint [q]uit => q

                                                 
Session..........: hashcat
Status...........: Quit
Hash.Type........: MD5
Hash.Target......: example0.hash
Time.Started.....: Fri Oct 11 16:56:08 2019 (11 secs)
Time.Estimated...: Fri Oct 11 16:59:46 2019 (3 mins, 27 secs)
Guess.Base.......: File (example.dict), Right Side
Guess.Mod........: Mask (?a?a?a?a) [4], Left Side
Guess.Queue.Base.: 1/1 (100.00%)
Guess.Queue.Mod..: 1/1 (100.00%)
Speed.#1.........:   616.9 MH/s (6.39ms) @ Accel:64 Loops:32 Thr:256 Vec:1
Recovered........: 1781/6494 (27.43%) Digests, 0/1 (0.00%) Salts
Recovered/Time...: CUR:N/A,N/A,N/A AVG:0,0,0 (Min,Hour,Day)
Progress.........: 6769606656/134653935616 (5.03%)
Rejected.........: 0/6769606656 (0.00%)
Restore.Point....: 0/1048576 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:51648-51680 Iteration:0-32
Candidates.#1....: saricesarcro -> 6o92cezdb
Hardware.Mon.#1..: Temp: 46c Core:1183MHz Mem:1750MHz Bus:0

Started: Fri Oct 11 16:56:06 2019
Stopped: Fri Oct 11 16:56:20 2019




---

### 评论 #13 — heero-yuy (2019-10-11T08:58:15Z)

And, currently I don't have Vega64 GPU on my own, maybe someone have time to try this, thanks!

May you tell us that prefer to manually complie the hashcat instead of use the binary version already for ROCm?

---

### 评论 #14 — ITfirewall (2019-10-13T09:03:13Z)

Hi heero-yuy, 

I tried both of them before and I got error in OpenCL with ROCm 2.7 , 2.7.1, 2.7.2 and 2.8 in Ubuntu 16.04 Kernel 4.15.

Now, I 'll try the new ROCm 2.9 in Ubuntu 16.04 full updated & upgraded to see if it works.

I 'll be back with the info.

Thank you.   

---

### 评论 #15 — ITfirewall (2020-01-06T06:42:31Z)

Hi heero-yuy, how are you?

Long long time... I didn't come here, but I tested sometime ago the ROCm 2.9 in ubuntu 16.04 and the same problems still, ''OpenCL error'''!!! (I was working in other country, far from my home.)

I can't belive, ROCm devs. don't fix the problems with OpenCL!!! 
I see a lot of people having problems in ''Issues page''!!
What developers are doing???

Ty.

---

### 评论 #16 — heero-yuy (2020-01-07T01:05:12Z)

Hi,
Until now the ROCm 3.0 released with openCL module can't be operated on some situation from inplace upgrade by package manager, and if available, please use the Ubuntu 18.04.3 with new install ROCm package, thanks!

---

### 评论 #17 — ITfirewall (2021-07-09T06:06:09Z)

Hi heero-yuy, how are you?

Long long time... I didn't come here because I got a new job.... hard times, friend.

How is the new ROCm 4.2??   Is it working right out the box on Ubuntu 18.04 LTS ????  

Which video-card model are you using??   

I 'm coming back to test some stuff in the next weeks (IT tasks).

Thank you for all the help.

---

### 评论 #18 — ROCmSupport (2021-07-09T08:04:08Z)

Hi @ITfirewall 
Thanks for reaching out.
All ROCm installation problems resolved now.
The latest ROCm 4.2 is a well matured one which supports many latest features, please follow @ https://github.com/RadeonOpenCompute/ROCm, it works perfect with Ubuntu 18.04 LTS.
ROCm supports Vega10/MI25, Vega20/MI50, MI100 cards officially.
Request you to try with the latest ROCm 4.2 and reach us for any queries. File new issues, for faster/quick resolution.
Thank you.

---
