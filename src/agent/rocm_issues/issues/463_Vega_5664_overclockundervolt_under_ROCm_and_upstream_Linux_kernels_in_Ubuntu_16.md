# Vega 56/64 overclock/undervolt under ROCm and upstream Linux kernels in Ubuntu 16.04/18.04 [How-to]

> **Issue #463**
> **状态**: closed
> **创建时间**: 2018-07-22T09:38:11Z
> **更新时间**: 2018-12-31T23:14:55Z
> **关闭时间**: 2018-12-31T23:14:55Z
> **作者**: evgeniyosipov
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/463

## 描述

Hello,
I want to share with you some information on how to overclock/undervolt GFX9 GPUs (Vega 56/Vega 64) under Ubuntu 16.04 and 18.04:

- Install updates:
```
sudo apt update && sudo apt dist-upgrade -y
sudo reboot
```

- Install ROCm https://github.com/RadeonOpenCompute/ROCm:
```
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install libnuma-dev 
sudo apt install rocm-dkms
sudo usermod -a -G video $LOGNAME 
echo 'SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"' | sudo tee /etc/udev/rules.d/70-kfd.rules
sudo reboot
```
If you have problems with the standard installation of rocm-dkms, install it **without rocm-dkms and rock-dkms packages**  _(verify packages list, it can vary)_:
```
sudo apt install comgr dkms hcc hip_base hip_doc hip_hcc hip_samples hsa-amd-aqlprofile hsa-ext-rocr-dev hsa-rocr-dev hsakmt-roct hsakmt-roct-dev rocm-clang-ocl rocm-dev rocm-device-libs rocm-opencl rocm-opencl-dev rocm-smi rocm-utils rocminfo rocr_debug_agent
```
- Install additional packages:
```
sudo apt install git flex bison libssl-dev cmake libelf-dev libpci-dev pkg-config clinfo lm-sensors htop screen libjansson4 -y
```

- Install M-Bab's kernel https://github.com/M-Bab/linux-kernel-amdgpu-binaries:
```
git --git-dir=/dev/null clone --depth=1 https://github.com/M-Bab/linux-kernel-amdgpu-binaries
cd linux-kernel-amdgpu-binaries
sudo dpkg -i linux-headers*ubuntu*.deb linux-image*ubuntu*.deb firmware-radeon-ucode_*_all.deb
sudo reboot
```

- **(Optional, only if you have problems with M-Bab's kernel)** Compile ROCK-Kernel-Driver (fkxamd/drm-next-wip branch or master branch) and install it:
```
git clone --depth 1 https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver -b fkxamd/drm-next-wip
cd ROCK-Kernel-Driver 
cp /boot/config-`uname -r` .config
yes '' | make oldconfig
make -j `getconf _NPROCESSORS_ONLN` deb-pkg LOCALVERSION=-fxkamd
dpkg -i *deb
sudo reboot
```

- **(Obsolete, ROCm 1.9 is ABI compatible with KFD in upstream Linux kernels)** Compile ROCT-Thunk-Interface (fxkamd/drm-next-wip branch or master branch) and replace original ROCm libhsakmt.so* binaries (or remove all files from /opt/rocm/libhsakmt/lib/ and put compiled files to this folder):
```
git clone --depth 1 https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface -b fxkamd/drm-next-wip
cd ROCT-Thunk-Interface
mkdir -p build
cd build
cmake ..
make
sudo cp -a /opt/rocm/libhsakmt/lib/ /opt/rocm/libhsakmt/lib.bak
sudo cp libhsakmt.so* /opt/rocm/libhsakmt/lib
sudo reboot
```

- Edit grub GRUB_CMDLINE_LINUX_DEFAULT:
```
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram"
sudo update-grub
sudo reboot
```

- Try overclock/undervolt:
```
sudo -i

# Allow manual mode:
echo "manual"> /sys/class/drm/card0/device/power_dpm_force_performance_level

# GPU Clock/Voltage:
# echo "s $STATE_INT $MHz $mVOLT"> /sys/class/drm/card0/device/pp_od_clk_voltage
# for example: 
echo "s 5 1650 960"> /sys/class/drm/card0/device/pp_od_clk_voltage

# HBM2 Memory Clock/Votage:
# echo "m $STATE_INT $MHz $mVOLT"> /sys/class/drm/card0/device/pp_od_clk_voltage
# for example: 
echo "m 3 1015 950"> /sys/class/drm/card0/device/pp_od_clk_voltage

# Check clocks/states
cat /sys/class/drm/card0/device/pp_od_clk_voltage

# Save changes
echo "c"> /sys/class/drm/card0/device/pp_od_clk_voltage 
```
If you want to thank me - please send some BTC **3JS1m8XSvS4fcprByLRuMjjjuck9dne4rm**

Thanks to everyone who shared interesting information on the web.

Please share your experience with other, maybe our world become less hot and more productive )

---

## 评论 (29 条)

### 评论 #1 — evgeniyosipov (2018-07-22T10:04:11Z)

* [Power Table Modification](https://github.com/RadeonOpenCompute/ROCm/issues/463#issuecomment-418597555) and [Power Table Generation](https://github.com/RadeonOpenCompute/ROCm/issues/463#issuecomment-418604330) (tnx to [mdai843](https://github.com/mdai843))
* Useful repos: 
https://github.com/xmrminer01102018/VegaToolsNConfigs
https://github.com/earlvanze/AMD-ROCm-Miner
https://github.com/matszpk/amdcovc
https://github.com/kobalicek/amdtweak


---

### 评论 #2 — Hackintoshihope (2018-07-23T01:49:51Z)

"(you may catch some errors - it's mean that you need to install missing packages for building kernels/packages - simply install it and repeat failed step)"

sudo apt-get install git
sudo apt-get install flex
sudo apt-get install bison
sudo apt-get install libssl-dev
sudo apt-get install cmake
sudo apt-get install libelf-dev
sudo apt-get install libpci-dev

These are what you need to install and to compile.

I have followed all of your steps and have tdxminer working on the new kernel...

Command:
cat /sys/class/drm/card0/device/pp_od_clk_voltage
cat: /sys/class/drm/card0/device/pp_od_clk_voltage: No such file or directory

(This will happen if you have an intel gpu) you must change "card0" to each and every vega you have card1, card2, card3, card4... etc

sudo -i
echo "manual" > /sys/class/drm/card1/device/power_dpm_force_performance_level

echo "m 3 945 905" > /sys/class/drm/card1/device/pp_od_clk_voltage

echo "s 3 1269 935" > /sys/class/drm/card1/device/pp_od_clk_voltage
echo "s 4 1312 955" > /sys/class/drm/card1/device/pp_od_clk_voltage
echo "s 5 1474 985" > /sys/class/drm/card1/device/pp_od_clk_voltage
echo "s 6 1569 1015" > /sys/class/drm/card1/device/pp_od_clk_voltage
echo "s 7 1663 1045" > /sys/class/drm/card1/device/pp_od_clk_voltage

echo "2" > /sys/class/drm/card1/device/pp_sclk_od

cat /sys/class/drm/card1/device/pp_od_clk_voltage

cat /sys/class/drm/card1/device/pp_sclk_od

echo "c" > /sys/class/drm/card1/device/pp_od_clk_voltage

echo "c" > /sys/class/drm/card1/device/pp_sclk_od

However what is interesting is even with all of these changes and configurations and even if you change the clocks and voltages performance will remain identical and power will not decrease or be modified on 16.04. Maybe someone can report something different but this seems to be more of a visual hack then a real one. The PP tables do nothing but appear to change things when in reality nothing is changed.

---

### 评论 #3 — Corpse666 (2018-07-25T20:20:50Z)

4.18.0-rc5 #1 SMP Sun Jul 22 13:52:18 CEST 2018 x86_64 x86_64 x86_64 GNU/Linux
But not 'Ubuntu 16.04', i'm trying 18.04.
Mining is ok, but slower than 16.04.
```
echo "s 5 1663 985" > /sys/class/drm/card1/device/pp_od_clk_voltage
-bash: echo: write error: Invalid argument
```
Why?

---

### 评论 #4 — Hackintoshihope (2018-07-25T21:55:28Z)

Mining was slower when I tried this on 16.04. Also I couldn’t get the overclocking to really work it would simply show that the clocks were changed but performance would not change... nor would power usage at the wall.

Also you need to make sure that command is Sudo and that you have pushed manual performance mode.

---

### 评论 #5 — Corpse666 (2018-07-26T06:11:25Z)

But card already in manual mode.
```
cat /sys/class/drm/card1/device/power_dpm_force_performance_level

manual
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  3   51c     154.0W   1401Mhz  945Mhz   0.0%     manual    0%         0%       
  1   51c     140.0W   1401Mhz  945Mhz   0.0%     manual    0%         0%       
  2   53c     162.0W   1401Mhz  945Mhz   0.0%     manual    0%         0%       
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A        N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```
May be i miss something?
Any why we cannot directly modify pp_table? I try some weeks ago, but my kernel panic.

---

### 评论 #6 — Corpse666 (2018-07-26T06:40:57Z)

Oh! Now it's work.
GRUB_CMDLINE_LINUX_DEFAULT its ok.
I'm add same to GRUB_CMDLINE_LINUX
```
sudo update-grub
sudo update-initramfs -u 

```
```
dmesg | grep BOOT
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-4.18.0-rc5 root=UUID=33aabdec-8ff3-11e8-ad86-6045cba79f13 ro quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-4.18.0-rc5 root=UUID=33aabdec-8ff3-11e8-ad86-6045cba79f13 ro quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram

```
Thanks.

---

### 评论 #7 — Wacholek (2018-08-02T13:47:55Z)

Is it possible to run 4.18.0-rc5 and keep the same hash rate? I used the first post guide 16.04. I can under-volt my Vega but I get lower hash rate about 8%.

---

### 评论 #8 — Hackintoshihope (2018-08-05T21:57:55Z)

Voltage and power consumption does not change with these patches. At the wall measured with a watt meter power consumption is stuck at 300W per card no matter the voltage setting. Did not know is this expected behavior or if Vega support is still in beta?

---

### 评论 #9 — Corpse666 (2018-08-15T09:41:15Z)

Need you help to understand why its happened.
I need to run tdxminer twice on same device(Vega and Ubuntu 16.04.5). 
Its not problem if i run on 1 GPU and 2 GPU's.
I can run it 6 times. Mean twice on d0, twice on d1 and twice on d2, but when i run on d3 i see error "Failed to list OpenCL platforms.".
After 6 tdxminers runs, clinfo also says "Number of platforms 0".
6 tdxminers continue working fine and hashing.
If you understand me, may be you have ideas why its happened?
Why only 6?! May be some settings somewhere?!
I try few kernels, same errors.
I have rig with 5 RX580, no problems to run tdxminer 10 times.

---

### 评论 #10 — mdai843 (2018-09-05T04:42:34Z)

@Hackintoshihope Just some info of my own that I wanted to share. I was also having trouble getting undervolting and applying custom power play tables to work properly. What turned out to be the trick was applying the power play tables via binary to /sys/class/drm/card$1/device/pp_table instead of what is suggested in the OP. 

This person put up a new repo with some useful tools for mining with vega: https://github.com/xmrminer01102018/VegaToolsNConfigs

In it are some scripts and documents on mining at full CNv1 at full speed with up to 6 vegas with custom power play tables. At this time, I was interested only in applying custom power play tables and undervolting for running tdxminer with rocm. In the repo are a few useful tools: SoftPPT-1.0.0.jar and setPPT.sh. SoftPPT-1.0.0.jar will convert hex power play tables to binary. And setPPT.sh will push your binary power play tables to /sys/class/drm/card$1/device/pp_table. Combined, this will allow you to build custom power play tables, convert to binary, and soft deploy them on your cards. 

My two vega FEs stats using this method on the latest rocm:
```
root@vega:~/VegaToolsNConfigs/tools# lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.5 LTS
Release:        16.04
Codename:       xenial

root@vega:~/VegaToolsNConfigs/tools# uname -a
Linux vega 4.18.5 #1 SMP Fri Aug 24 17:51:52 CEST 2018 x86_64 x86_64 x86_64 GNU/Linux

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   58c     145.0W   1408Mhz  1050Mhz  0.0%     manual    0%         0%
  0   51c     146.0W   1408Mhz  1050Mhz  0.0%     manual    0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```

Before, running them at these clocks would always just result in them consuming 220 watts. Now they run at a much more respectable 145 watts (190ish watts at the wall?) 

---

### 评论 #11 — Hackintoshihope (2018-09-05T04:53:05Z)

@mdai843 I’ve waited a long time for confirmation of my issues this post detailed methods to get the functionality to work. But the implementation did nothing of the sort to reduce power. 

If I am understanding correct you were able to modify voltages and get a lower power consumption using additional tweaks you provided? 

Or just by pushing changes instead to this path: /sys/class/drm/card$1/device/pp_table?

I’ve been anxious wanting to implement this. If what you are saying is correct I’m about to cool down my Vegas considerably.  

---

### 评论 #12 — mdai843 (2018-09-05T05:25:25Z)

Some initial testing I did for underclocks and undervolts for rocm 1.8.3 + tdxminer + 4.18 kernel on 2 vega FEs (~120 watts from the wall):

```
[2018-09-04 22:22:07] Stats GPU 0 - lyra2z: 5.245Mh/s (5.244Mh/s)
[2018-09-04 22:22:07] Stats GPU 1 - lyra2z: 5.245Mh/s (5.245Mh/s)
[2018-09-04 22:22:07] Stats Total - lyra2z: 10.490Mh/s (10.489Mh/s)
```
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   50c     93.0W    1138Mhz  800Mhz   0.0%     auto      0%         0%
  0   48c     95.0W    1138Mhz  800Mhz   0.0%     auto      0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```
```
GPU0
GFX Clocks and Power:
        800 MHz (MCLK)
        1134 MHz (SCLK)
        1269 MHz (PSTATE_SCLK)
        800 MHz (PSTATE_MCLK)
        800 mV (VDDGFX)
        89.0 W (average GPU)

GPU Temperature: 48 C
GPU Load: 99 %

UVD: Enabled

VCE: Enabled 

GPU1
GFX Clocks and Power:
        800 MHz (MCLK)
        1134 MHz (SCLK)
        1269 MHz (PSTATE_SCLK)
        800 MHz (PSTATE_MCLK)
        800 mV (VDDGFX)
        91.0 W (average GPU)

GPU Temperature: 50 C
GPU Load: 99 %

UVD: Enabled

VCE: Enabled 
```

```
vega@vega:~/VegaToolsNConfigs/config/PPTDIR$ cat /sys/class/drm/card0/device/pp_od_clk_voltage 
OD_SCLK:
0:        852Mhz        800mV
1:        991Mhz        800mV
2:       1138Mhz        800mV
3:       1138Mhz        800mV
4:       1138Mhz        800mV
5:       1138Mhz        800mV
6:       1138Mhz        800mV
7:       1138Mhz        800mV
OD_MCLK:
0:        167Mhz        800mV
1:        500Mhz        800mV
2:        800Mhz        800mV
3:        500Mhz        800mV
OD_RANGE:
SCLK:     852MHz       2400MHz
MCLK:     167MHz       1500MHz
VDDC:     800mV        1250mV

vega@vega:~/VegaToolsNConfigs/config/PPTDIR$ cat /sys/class/drm/card1/device/pp_od_clk_voltage 
OD_SCLK:
0:        852Mhz        800mV
1:        991Mhz        800mV
2:       1138Mhz        800mV
3:       1138Mhz        800mV
4:       1138Mhz        800mV
5:       1138Mhz        800mV
6:       1138Mhz        800mV
7:       1138Mhz        800mV
OD_MCLK:
0:        167Mhz        800mV
1:        500Mhz        800mV
2:        800Mhz        800mV
3:        500Mhz        800mV
OD_RANGE:
SCLK:     852MHz       2400MHz
MCLK:     167MHz       1500MHz
VDDC:     800mV        1250mV
```

---

### 评论 #13 — mdai843 (2018-09-05T05:31:29Z)

@Hackintoshihope I too have been working on this problem for long and couldn't get it solved. Would be great to confirm my results since this appears to be too good to be true. I combed through everything from tekcomm but never got it sorted out. I finally think this might be it. Again, the method is to generate power play tables in hex form. Convert them to binary. Then to push them to /sys/class/drm/card$1/device/pp_table (included in that repo is a helper script called setPPT.sh). The tools you need for converting hex -> binary are in the repo above. You can generate custom power play tables here: https://docs.google.com/spreadsheets/d/1-rhYsaRXO1ahk3PyrEgT9gXzs7ImAzh-sbqtgwy8HQg/edit#gid=964538665

The hex power play tables need to have all newlines, commas, and back slashes stripped out. I'll try to show a sample of my work here:

For example, the power play table for my test above first looks like:
```

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000]
--
"PP_PhmSoftPowerPlayTable"=hex:B6,02,08,01,00,5C,00,E1,06,00,00,EE,2B,00,00,1B,\
00,48,00,00,00,80,A9,03,00,F0,49,02,00,64,00,08,00,00,00,00,00,00,00,00,00,\
00,00,00,00,00,02,01,5C,00,4F,02,46,02,94,00,9E,01,BE,00,28,01,7A,00,8C,00,\
BC,01,00,00,00,00,72,02,00,00,90,00,A8,02,6D,01,43,01,97,01,F0,49,02,00,71,\
02,02,02,00,00,00,00,00,00,08,00,00,00,00,00,00,00,05,00,07,00,03,00,05,00,\
00,00,00,00,00,00,01,08,20,03,6B,03,6B,03,6B,03,6B,03,6B,03,75,03,83,03,01,\
01,6B,03,01,01,84,03,00,08,60,EA,00,00,00,40,19,01,00,01,80,38,01,00,02,DC,\
4A,01,00,03,90,5F,01,00,04,00,77,01,00,05,90,91,01,00,06,C0,D4,01,00,07,01,\
08,D0,4C,01,00,00,00,80,00,00,00,00,00,00,1C,83,01,00,01,00,00,00,00,00,00,\
00,00,70,A7,01,00,02,00,00,00,00,00,00,00,00,88,BC,01,00,03,00,00,00,00,00,\
00,00,00,38,C1,01,00,04,00,00,00,00,00,00,00,00,88,D5,01,00,05,00,00,00,00,\
01,00,00,00,70,D9,01,00,06,00,00,00,00,01,00,00,00,00,26,02,00,07,00,00,00,\
00,01,00,00,00,00,05,60,EA,00,00,00,40,19,01,00,00,80,38,01,00,00,DC,4A,01,\
00,00,90,5F,01,00,00,00,08,28,6E,00,00,00,2C,C9,00,00,01,F8,0B,01,00,02,80,\
38,01,00,03,90,5F,01,00,04,F4,91,01,00,05,D0,B0,01,00,06,C0,D4,01,00,07,00,\
08,6C,39,00,00,00,24,5E,00,00,01,FC,85,00,00,02,AC,BC,00,00,03,34,D0,00,00,\
04,68,6E,01,00,05,08,97,01,00,06,EC,A3,01,00,07,00,01,68,3C,01,00,00,01,04,\
3C,41,00,00,00,00,00,50,C3,00,00,00,00,00,80,38,01,00,02,00,00,24,71,01,00,\
04,00,00,01,08,00,98,85,00,00,40,B5,00,00,60,EA,00,00,50,C3,00,00,01,80,BB,\
00,00,60,EA,00,00,94,0B,01,00,50,C3,00,00,02,00,E1,00,00,94,0B,01,00,40,19,\
01,00,50,C3,00,00,03,78,FF,00,00,40,19,01,00,88,26,01,00,50,C3,00,00,04,40,\
19,01,00,80,38,01,00,80,38,01,00,50,C3,00,00,05,80,38,01,00,DC,4A,01,00,DC,\
4A,01,00,50,C3,00,00,06,00,77,01,00,00,77,01,00,90,5F,01,00,50,C3,00,00,07,\
90,91,01,00,90,91,01,00,00,77,01,00,50,C3,00,00,01,18,00,00,00,00,00,00,00,\
0B,E4,12,24,13,24,13,32,00,0A,00,54,03,C2,01,C2,01,C2,01,C2,01,C2,01,C2,01,\
90,01,00,00,00,00,00,02,0A,31,07,DC,00,DC,00,DC,00,90,01,00,00,59,00,69,00,\
4A,00,4A,00,5F,00,73,00,73,00,64,00,40,00,90,92,97,60,96,00,90,46,00,00,00,\
00,00,00,00,00,00,00,00,00,00,00,00,00,00,02,02,D4,30,00,00,02,10,60,EA,00,\
00,02,10
```

I stripped out all the non essentials leaving plain hex digits like so:

```
B6020801005C00E1060000EE2B00001B004800000080A90300F0490200640008000000000000000000000000000002015C004F02460294009E01BE0028017A008C00BC0100000000720200009000A8026D0143019701F049020071020202000000000000080000000000000005000700030005000000000000000108200320032003200320032003200320030101200301018403000860EA00000040190100018038010002DC4A010003905F01000400770100059091010006C0D40100070108D04C01000000800000000000001C83010001000000000000000088BC010002000000000000000088BC010003000000000000000088BC010004000000000000000088BC010005000000000100000088BC010006000000000100000088BC0100070000000001000000000560EA00000040190100008038010000DC4A010000905F0100000008286E0000002CC9000001F80B0100028038010003905F010004F491010005D0B0010006C0D401000700086C39000000245E000001FC85000002ACBC00000334D0000004686E0100050897010006ECA30100070001683C01000001043C41000000000050C300000000008038010002000050C300000400000108009885000040B5000060EA000050C300000180BB000060EA0000940B010050C300000200E10000940B01004019010050C300000378FF0000401901008826010050C300000440190100803801008038010050C300000580380100DC4A0100DC4A010050C30000060077010000770100905F010050C300000790910100909101000077010050C300000118000000000000000BE4122413241332000A005403C201C201C201C201C201C2019001000000000002183107DC00DC00DC0090010000590069004A004A005F007300730064004000909297609600904600000000000000000000000000000000000202D4300000021060EA00000210
```

You then convert this to binary like so:
```
/opt/jdk-10.0.2/bin/java -jar SoftPPT-1.0.0.jar FETEXT FEBINARY
```

Then push this to each card:
```
sudo ../../tools/setPPT.sh 0 FEBINARY1
sudo ../../tools/setPPT.sh 1 FEBINARY1
```



---

### 评论 #14 — Hackintoshihope (2018-09-05T05:47:11Z)

@mdai843
Fascinating have you understood yet why we have to do it this way? I’ve read about many users with unmodified verisions of ubuntu could do this without these modifications.

Also concerning that under volt that is effectively double the efficiency then what I am currently getting. If that is correct 30mhs+ for 6 Vegas that just might be the best performance per watt I’ve seen. 

I will be loading up my test rig and see if I can replicate your results in a similar fashion. Exciting stuff. 

---

### 评论 #15 — mdai843 (2018-09-05T05:48:35Z)

I just tested this on my larger rig with 6 Vega FEs to make sure this actually scaled up and worked on risers. Using this same clocks as before but with real undervolts, I was able to drop my wattage by about 70 watts. Before I was pulling 915 watts from the wall, but now am pulling 845 watts from the wall with no hash rate drop since the clocks remained the same. I'm sure one can do much better but I'm convinced that this actually works. 

```
[2018-09-04 22:48:36] Stats GPU 0 - lyra2z: 5.296Mh/s (5.280Mh/s)
[2018-09-04 22:48:36] Stats GPU 1 - lyra2z: 5.288Mh/s (5.280Mh/s)
[2018-09-04 22:48:36] Stats GPU 2 - lyra2z: 5.296Mh/s (5.280Mh/s)
[2018-09-04 22:48:36] Stats GPU 3 - lyra2z: 5.296Mh/s (5.281Mh/s)
[2018-09-04 22:48:36] Stats GPU 4 - lyra2z: 5.262Mh/s (5.247Mh/s)
[2018-09-04 22:48:36] Stats GPU 5 - lyra2z: 5.296Mh/s (5.281Mh/s)
[2018-09-04 22:48:36] Stats Total - lyra2z: 31.734Mh/s (31.649Mh/s)
```

```
root@epsilon:~/VegaToolsNConfigs/config/PPTDIR# cat /sys/class/drm/card5/device/pp_od_clk_voltage 
OD_SCLK:
0:        852Mhz        800mV
1:        991Mhz        800mV
2:       1138Mhz        800mV
3:       1138Mhz        800mV
4:       1138Mhz        800mV
5:       1138Mhz        800mV
6:       1138Mhz        800mV
7:       1138Mhz        800mV
OD_MCLK:
0:        167Mhz        800mV
1:        500Mhz        800mV
2:        800Mhz        800mV
3:        500Mhz        800mV
OD_RANGE:
SCLK:     852MHz       2400MHz
MCLK:     167MHz       1500MHz
VDDC:     800mV        1250mV
```

```====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  5   48.0c   102.0W   1138Mhz  800Mhz   14.9%    manual    0%
  3   47.0c   92.0W    1138Mhz  800Mhz   13.73%   manual    0%
  1   46.0c   94.0W    1138Mhz  800Mhz   14.9%    manual    0%
  4   46.0c   92.0W    1138Mhz  800Mhz   15.69%   manual    0%
  2   44.0c   93.0W    1138Mhz  800Mhz   20.0%    manual    0%
  0   43.0c   96.0W    1138Mhz  800Mhz   13.73%   manual    0%
================================================================================
====================           End of ROCm SMI Log          ====================
```

---

### 评论 #16 — Hackintoshihope (2018-09-05T05:52:54Z)

@mdai843
If you could would you be able to detail what deviations if any you took from setting up your rigs with @evgeniyosipov original instructions? I understand you detailed how to actually push the modified tables but is that the only change you did with the setup? Used an otherwise fresh 16.04.5. (just making sure as I’vs been driven crazy troubleshooting this and if you have actually found the solution...) 

Any additional information will help.

---

### 评论 #17 — mdai843 (2018-09-05T06:02:23Z)

I didn't take any deviations from the OP for setting up the machine aside from how to set up the power play tables. His original instructions will suffice. The order I do things are:

1) Install OS
2) Update and upgrade everything via apt
3) Install latest ROCm 
4) Install latest 4.18.x kernel
5) Update kernel params and grub
6) Mining software setup and power play table config. 

Tekcomm's repos are offline as he removed all traces of himself. You can find some of his old stuff like tdxminer here: https://github.com/earlvanze/AMD-ROCm-Miner

---

### 评论 #18 — Hackintoshihope (2018-09-05T06:07:43Z)

Tekcomm left for some reason but he did not develop tdxminer. He modified it to work with RX 550 and RX 560. However regardless it seems you’ve done it I’ll report back on a fresh install. 

---

### 评论 #19 — mdai843 (2018-09-05T06:20:56Z)

Good luck, I spent more time on this than I care to admit. So I really hope this will help any one else struggling with undervolting vegas on linux. 

---

### 评论 #20 — Hackintoshihope (2018-09-05T07:58:46Z)

@mdai843 
IT WORKS! HAHA!

I did need to install java... but in essence it works as you say.

Although I would like to know what exactly you are doing to get your hex cleaned up? Is there an easy way to do this?

---

### 评论 #21 — mdai843 (2018-09-05T08:05:25Z)

That's awesome. Thanks for validating these steps. To clean it up, I just did it in vi with some search and replace. I'm sure you can write a little script to do some regex replacements. It's just dropping the commas, the new lines, the backslashes, and all the text before the actual hex code. 

As for why this works? Not sure yet. I suppose this will be one of those things that gets fixed over time. For now, we'll just have to do it this way. 

---

### 评论 #22 — Hackintoshihope (2018-09-05T20:56:22Z)

@mdai843 

`B6020801005C00E1060000EE2B00001B004800000080A90300F0490200640008000000000000000000000000000002015C004F02460294009E01BE0028017A008C00BC0100000000720200009000A8026D0143019701F0490200710202020000000000000800000000000000050007000300050000000000000001082003840320032003200320038403CA030101200301018403000860EA00000040190100018038010002DC4A010003905F01000400770100059091010006C0D40100070108D04C01000000800000000000001C83010001000000000000000088BC010002000000000000000088BC010003000000000000000088BC010004000000000000000088BC01000500000000010000009C250200060000000001000000BC730200070000000001000000000560EA00000040190100008038010000DC4A010000905F0100000008286E0000002CC9000001F80B0100028038010003905F010004F491010005D0B0010006C0D401000700086C39000000245E000001FC85000002ACBC00000334D0000004686E0100050897010006ECA30100070001683C01000001043C41000000000050C3000000000050C3000002000050C300000400000108009885000040B5000060EA000050C300000180BB000060EA0000940B010050C300000200E10000940B01004019010050C300000378FF0000401901008826010050C300000440190100803801008038010050C300000580380100DC4A0100DC4A010050C30000060077010000770100905F010050C300000790910100909101000077010050C300000118000000000000000BE4122413241332000A005403C201C201C201C201C201C20190010000000000020A3107DC00DC00DC0090010000590069004A004A005F007300730064004000909297609600904600000000000000000000000000000000000202D4300000021060EA00000210`

You will need to convert the above to binary just as you showed me.

Would you be able to test this HEX and report what hash rate you experience? It has three states that are modified. 5 6 7. To access these states and get performance measures from each one do something like this:  run each command each time the miner starts to get the correct state (/opt/rocm/bin/rocm-smi --setsclk 5 --setfan 205), (/opt/rocm/bin/rocm-smi --setsclk 6 --setfan 205), (/opt/rocm/bin/rocm-smi --setsclk 7 --setfan 205) without parenthesis of course.

Each state is as follows 1138 MHZ 800mv, 1407 MHZ 900mv, and 1607 MHZ 970mv (all with 500MHZ HBM2)

I am getting about a 12-20% hash rate drop at the same clocks as I did before without the undervolting.


---

### 评论 #23 — mdai843 (2018-09-06T02:49:21Z)

@Hackintoshihope my results below:

/opt/rocm/bin/rocm-smi --setsclk 5 --setfan 205 (376 watts from the wall and notice the voltage is 900mV even though we are fixed at 500 mem and 1134 core. For reference, the pp table in my example above does 1138/800 @ 800mv pulling ~300 from the wall. Don't know why, vagaries of working with AMD cards I suppose.)
```'
root@vega:~/VegaToolsNConfigs/tools# cat /sys/class/drm/card0/device/pp_od_clk_voltage 
OD_SCLK:
0:        852Mhz        800mV
1:        991Mhz        900mV
2:       1138Mhz        800mV
3:       1138Mhz        800mV
4:       1138Mhz        800mV
5:       1138Mhz        800mV
6:       1407Mhz        900mV
7:       1607Mhz        970mV
OD_MCLK:
0:        167Mhz        800mV
1:        500Mhz        800mV
2:        500Mhz        800mV
3:        500Mhz        800mV
OD_RANGE:
SCLK:     852MHz       2400MHz
MCLK:     167MHz       1500MHz
VDDC:     800mV        1250mV

GPU0
GFX Clocks and Power:
        500 MHz (MCLK)
        1134 MHz (SCLK)
        1269 MHz (PSTATE_SCLK)
        800 MHz (PSTATE_MCLK)
        900 mV (VDDGFX)
        122.0 W (average GPU)

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   49c     119.0W   1138Mhz  500Mhz   0.0%     manual    0%         0%       
  0   47c     123.0W   1138Mhz  500Mhz   0.0%     manual    0%         0%       
================================================================================
====================           End of ROCm SMI Log          ====================

[2018-09-05 19:47:40] Stats GPU 0 - lyra2z: 5.228Mh/s (5.227Mh/s)
[2018-09-05 19:47:40] Stats GPU 1 - lyra2z: 5.228Mh/s (5.228Mh/s)
[2018-09-05 19:47:40] Stats Total - lyra2z: 10.456Mh/s (10.455Mh/s)
```

---

### 评论 #24 — mdai843 (2018-09-06T02:52:27Z)

/opt/rocm/bin/rocm-smi --setsclk 6 --setfan 205 (unstable on one card and hangs, will report stats on other card. 330 watts from the wall including hung gpu)
```
GPU1
GFX Clocks and Power:
        500 MHz (MCLK)
        1352 MHz (SCLK)
        1269 MHz (PSTATE_SCLK)
        800 MHz (PSTATE_MCLK)
        900 mV (VDDGFX)
        139.0 W (average GPU)

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   52c     139.0W   1407Mhz  500Mhz   0.0%     manual    0%         0%
  0   39c     63.0W    1407Mhz  500Mhz   0.0%     manual    0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================

[2018-09-05 19:52:16] Stats GPU 0 - lyra2z: 0.000Mh/s (0.623Mh/s)  
[2018-09-05 19:52:16] Stats GPU 1 - lyra2z: 6.253Mh/s (6.232Mh/s)  
[2018-09-05 19:52:16] Stats Total - lyra2z: 6.253Mh/s (6.855Mh/s) 
```

---

### 评论 #25 — mdai843 (2018-09-06T02:57:15Z)

/opt/rocm/bin/rocm-smi --setsclk 7 --setfan 205 (both cards hang)
```
GPU0
GFX Clocks and Power:
        500 MHz (MCLK)
        1603 MHz (SCLK)
        1269 MHz (PSTATE_SCLK)
        800 MHz (PSTATE_MCLK)
        975 mV (VDDGFX)
        93.0 W (average GPU)

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   44c     81.0W    1607Mhz  500Mhz   0.0%     manual    0%         0%
  0   41c     94.0W    1607Mhz  500Mhz   0.0%     manual    0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```


---

### 评论 #26 — Hackintoshihope (2018-09-06T03:12:45Z)

@mdai843 

These settings are extremely experimental and being used on Vega 64 and Vega 56's Only ran for 10-15min. If I am familiar you are using a Vega FE? But your results do seem to mimic what I am getting. For the tests you have ran.

---

### 评论 #27 — 949f45ac (2018-09-11T17:14:07Z)

Should this work with RX 400 / 500 series cards as well?
I’ve tried a few things but generally had problems. So I am uncertain whether it is because I have not only Vega cards installed, or because this only works for Vega.

---

### 评论 #28 — akostadinov (2018-12-31T14:02:26Z)

setting `pp_od_clk_voltage` doesn't work for me with `rocm-dkms-2.0.89-1.x86_64` and gfx900 (vega fe) card.
```
# echo "s 5 1650 960"> /sys/class/drm/card0/device/pp_od_clk_voltage
-bash: echo: write error: Invalid argument
```

ops, I see in `dmesg` 
```
[13062.728914] amdgpu: [powerplay] OverDrive feature not enabled
```

How do I enable this?

Update, ok, I figured, I don't line kernel command lines. It can be enabled by adding a modprobe.conf file and rebuilding initrd `dracut -f`. Just make sure dracut-generic config is not enabled because modprobe files are ignored in such case. Btw a good resource is [arch wiki](https://wiki.archlinux.org/index.php/AMDGPU) (as usual).
```
# $ cat /etc/modprobe.d/00local.conf
# options amdgpu ppfeaturemask=0xffffffff
```

---

### 评论 #29 — jlgreathouse (2018-12-31T23:14:55Z)

Hi @akostadinov 

Yep, in order to use the OverDrive settings like `pp_od_clk_voltage`, you must enable OverDrive features for the driver. Note that, depending on [the default settings for ppfeaturemask](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L123), you may not need to set the `ppfeaturemask` to `0xffffffff`. You only need to make sure that you set the OverDrive bit. [In this case](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/include/amd_shared.h#L131) (ROCm 2.0) this requires that you OR 0x4000 into whatever the default mask it. The default has all other bits on in this case, so `0xffffffff` is correc.t I only note this because the default may change in future versions.

For instance, in [the 4.20 upstream driver](https://github.com/torvalds/linux/blob/v4.20/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L118), the default is `0xfffd3fff`.

Note also that, rather than writing directly to `/sys/class/drm/card0/device/pp_od_clk_voltage`, you can now use [rocm-smi](https://github.com/RadeonOpenCompute/ROC-smi/tree/roc-2.0.0) to set these values using the `--setslevel SCLKLEVEL SCLK SVOLT` and `--setmlevel MCLKLEVEL MCLK MVOLT` options.

Note also that, when defining the rules in your new DPM tables, you will need to follow some of the rules that I mention in these posts:

- [The frequency of DPM N cannot be higher than the frequency of DPM N+1, and it cannot be lower than the frequency of DPM N-1](https://github.com/RadeonOpenCompute/ROCm/issues/606#issuecomment-436784002)
- [Similarly, the voltage of DPM N cannot be higher than the voltage of DPM N+1, and it cannot be lower than the voltage of DPM N-1](https://github.com/RadeonOpenCompute/ROCm/issues/606#issuecomment-436819697)
- That said, you can change the frequency or voltage of N-1 (obeying the rules above, recursively) to lower N-1 and then lower N to reach configurations that would not be available by default. For instance, if DPM6 was 1300 MHz and DPM7 was 1400 MHz, you could first set DPM6 to 1200 then DPM7 to 1250.

Finally, you may be interested in [this discussion](https://github.com/RadeonOpenCompute/ROCm/issues/458#issuecomment-449775522) about changing the maximum power setting for your GPU and [this discussion](https://github.com/RadeonOpenCompute/ROCm/issues/564#issuecomment-428069668) on performance loss due to thermal throttling / fan speed choices.

I just tested the `rocm-smi` method of doing this on both the ROCm 2.0 DKMS driver, as well as the upstream 4.20 driver on Polaris 10 and Vega 10. I think that should simplify things for everyone, so I'm going to close up this issue. :)

---
