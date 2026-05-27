# Vega FE not recognized by OpenCL calls

> **Issue #143**
> **状态**: closed
> **创建时间**: 2017-07-01T23:03:58Z
> **更新时间**: 2018-07-30T15:00:05Z
> **关闭时间**: 2017-07-02T01:38:38Z
> **作者**: jstefanop
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/143

## 描述

Hi, just got an Vega FE and trying to run some compute task on it. Installed 1.6 (ROCM OpenCL opencl-dev)and everything seems fine (Vega card is properly initialized on boot, and KFD shows device added properly), but OpenCL apps don't see the card. 

Also tried installing the 17.20 driver packages, and same thing there as well (Those drivers DO see the Polaris based cards though). Interestingly if I remove the polaris card and try to run clinfo on just the vega card it crashes. (I don't see clinfo installed with rocm). 

---

## 评论 (34 条)

### 评论 #1 — gstoner (2017-07-01T23:39:27Z)

You can not mix the 17.20 component with the ROCm driver.  Very bad things will happen.   

Let's focus on the ROCm stack, this is what I work on primarily. 

One thing was this system where you had AMDGPUpro drive on it,  did you purge the driver before installing ROCm driver.     What OS are you running as well? 

So does the system have two Cards in the ROCm 1.6,  Polaris and Vega10, in the system, what is the CPU in the system? 

I ended up writing new install instruction for ROCm 
https://rocm.github.io/ROCmInstall.html  they post install step tests 

Can you do this Post install verification

Verify you have the correct Kernel Post install

$ uname -r
4.9.0-kfd-compute-rocm-rel-1.6-77
Test the driver is installed correctly

cd /opt/rocm/hsa/sample
make
./vector_copy
Test if OpenCL is working based on default ROCm OpenCL include and library locations:

g++ -I /opt/rocm/opencl/include/ ./HelloWorld.cpp -o HelloWorld -L/opt/rocm/opencl/lib/x86_64 -lOpenCL
Run it:

./HelloWorld

One last thing can you try HIP Sample 

We also developed a new install FAQ 
https://rocm.github.io/install_issues.html 

On Polaris and Vega10  this morning Me and my team was running ROCm with MIOpen 1.0 which OpenCL based.  



---

### 评论 #2 — jstefanop (2017-07-01T23:47:51Z)

I was not mixing components, I just tried both 17.20 amdgpu pro drivers, then purged those drivers and installed the ROCM kernel. I was definitely in the right kernel (this is in Ubuntu 16.04.2 btw). CPU is Core i3 on Z97 Motherboard.

Interestingly the HSA folder is not present after the install. 

I guess I might need to just do a clean install and see how it goes. Would I need to do and bash exports for the OpenCL App to find the ROCM components properly? Seems like the paths are different than AMDGPU-pro...so any openCL app built for AMDGPU-Pro might not see the ROCm OpenCL components?

---

### 评论 #3 — gstoner (2017-07-02T00:01:15Z)

They are different paths path for OpenCL.   you need to at the shell  "export OPENCL_ROOT=/opt/rocm/opencl"


---

### 评论 #4 — jstefanop (2017-07-02T03:01:13Z)

Ok will double check tomorrow if that was the issue. 

---

### 评论 #5 — jstefanop (2017-07-02T19:38:47Z)

@gstoner That was not it...tried downloading the openCl helloworld example, and libraries cannot be found even after that export:

/usr/bin/ld: cannot find -lOpenCL
collect2: error: ld returned 1 exit status


Is that export all that is needed? I know in that past ive had to do LD_LIBRARY_PATH exports etc. 

---

### 评论 #6 — jstefanop (2017-07-02T23:52:14Z)

Still no way to get the ROCm stack to work with OpenCL...i see on the OPENGPU blog there is mentioning about this variable:

echo 'export LLVM_BIN=/opt/amdgpu-pro/bin' | sudo tee /etc/profile.d/amdgpu-pro.sh

Is there something equivalent for ROCm stack? It would be great if there is so much minute details to get this stack going that you guys make a script that checks against all dependencies, bash variables, libraries etc.

---

### 评论 #7 — gstoner (2017-07-03T00:07:59Z)


On Jul 2, 2017, at 6:52 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


Still no way to get the ROCm stack to work with OpenCL...i see on the OPENGPU blog there is mentioning about this variable:

echo 'export LLVM_BIN=/opt/amdgpu-pro/bin' | sudo tee /etc/profile.d/amdgpu-pro.sh

Is there something equivalent for ROCm stack? It would be great if there is so much minute details to get this stack going that you guys make a script that checks against all dependencies, bash variables, libraries etc.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-312524492>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaigYGd3-60rOOaaV4lfzWYAh3i8ks5sKC0ugaJpZM4OLcF9>.

There is some thing wrong with your system

This all you have to do.   We were running ROCm with OpenCL with MIOpen

Here’s a simple workflow to get you quickly up and running with OpenCL on ROCm –
Install the ROCm OpenCL implementation (assuming you already have the ‘rocm’ package installed):

sudo apt-get install rocm-opencl-dev


Set an environment variable that points to the installation directory for OpenCL:

export OPENCL_ROOT=/opt/rocm/opencl


For a sample OpenCL application, let’s use a simple vector-add example from the University of Bristol’s very nice “Hands On OpenCL” lectures.

git clone https://github.com/HandsOnOpenCL/Exercises-Solutions.git

cd Exercises-Solutions/Exercises/Exercise02/C

make \
  CCFLAGS="-I$OPENCL_ROOT/include/opencl1.2 -O3 -DDEVICE=CL_DEVICE_TYPE_DEFAULT" \
  LIBS="-L$OPENCL_ROOT/lib/x86_64 -lOpenCL -lm"

./vadd



---

### 评论 #8 — gstoner (2017-07-03T00:11:04Z)


What slot is your GPU in on that mother board  make sure it is x16 slot that is real x16 slot

Also I like you to install fresh copy of Ubuntu  and follow these step to install the os
ROCm GPU Server Driver Installation Guide for Linux
Introduction

The ROCm Platform brings a rich foundation to advanced computing by seamlessly integrating the CPU and GPU with the goal of solving real-world problems.

This support starts with AMD’s FIJI Family of dGPUs. ROCm 1.3 further extends support to include the Polaris Family of ASICs. With ROCm 1.6 we add Vega Family of products.

System Requirements

To use ROCm on your system you need the following:

  *   ROCm Capable CPU and GPU
     *   PCIe Gen 3 Enabled CPU with PCIe Platform Atomics
     *   ROCm enabled GPU’s
        *   Radeon Instinct Family MI25, MI8, MI6
        *   Radeon Vega Frontier Edition
  *   Supported Version of Linux with a specified GCC Compiler and ToolChain

Table 1. Native Linux Distribution Support in ROCm 1.6

Distribution    Kernel  GCC     GLIBC
x86_64
Fedora 24       4.9     5.40    2.23
Ubuntu 16.04    4.9     5.40    2.23
Pre Install Directions
Verify You Have ROCm Capable GPU Installed int the System

lspci | grep -i AMD


You will see list of AMD GPU’s
Verify You Have a Supported Version of Linux

uname - m && cat /etc/*release


You will see some thing like for Ubuntu

x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.2 LTS"


Verify version of GCC

gcc --version


You will see

gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609


Choose an Installation Method

Package manager Based Install A Package Manager Based Installation use your Linux Distro system’s package management service.
Ubuntu uses Debian and Fedora RPM Packages

  *   Ubuntu
  *   Fedora

Ubuntu Install
Add the Repo Server

For Debian based systems, like Ubuntu, configure the Debian ROCm repository as follows:

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'


The gpg key might change, so it may need to be updated when installing a new release. The current rocm.gpg.key is not avialable in a standard key ring distribution, but has the following sha1sum hash:

f0d739836a9094004b0a39058d046349aacc1178 rocm.gpg.key

Install or update ROCm

sudo apt-get update
sudo apt-get install rocm rocm-opencl-dev


Then, make the ROCm kernel your default kernel. If using grub2 as your bootloader, you can edit the GRUB_DEFAULT variable in the following file:

sudo nano /etc/default/grub


set the GRUB_Default Edit: GRUB_DEFAULT=”Advanced options for Ubuntu>Ubuntu, with Linux 4.9.0-kfd-compute-rocm-rel-1.6-77”

sudo update-grub


________________________________
Fedora Install

Use the dnf (yum) repository for installation of rpm packages. To configure a system to use the ROCm rpm directory create the file /etc/yum.repos.d/rocm.repo with the following contents:

[remote]

name=ROCm Repo

baseurl=http://repo.radeon.com/rocm/yum/rpm/

enabled=1

gpgcheck=0


Execute the following commands:

sudo dnf clean all
sudo dnf install rocm rocm-opencl-dev


Just like Ubuntu installs, the ROCm kernel must be the default kernel used at boot time.

Post Install Manual installation steps for Fedora to support HCC compiler

A fully functional Fedora installation requires a few manual steps to properly setup, including:

  *   Building compatible libc++ and libc++abi libraries for Fedora<https://github.com/RadeonOpenCompute/hcc/wiki#fedora>

Post install verification

Verify you have the correct Kernel Post install

$ uname -r
4.9.0-kfd-compute-rocm-rel-1.6-77


Test the driver is installed correctly

cd /opt/rocm/hsa/sample
make
./vector_copy


Test if OpenCL is working based on default ROCm OpenCL include and library locations:

g++ -I /opt/rocm/opencl/include/ ./HelloWorld.cpp -o HelloWorld -L/opt/rocm/opencl/lib/x86_64 -lOpenCL


Run it:

./HelloWorld


To Uninstall the a Package

  *   Ubuntu

sudo apt-get purge libhsakmt
sudo apt-get purge radeon-firmware
sudo apt-get purge $(dpkg -l | grep 'kfd\|rocm' | grep linux | grep -v libc | awk '{print $2}')


  *   Fedora

sudo dnf remove ROCm


List of ROCm Packages for Ubuntu and Fedora<https://rocm.github.io/ROCmLinuxpackages.html>

Installing development packages for cross compilation

It is often useful to develop and test on different systems. In this scenario, you may prefer to avoid installing the ROCm Kernel to your development system.

In this case, install the development subset of packages:

sudo apt-get update
sudo apt-get install rocm-dev





Greg
On Jul 2, 2017, at 6:52 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


Still no way to get the ROCm stack to work with OpenCL...i see on the OPENGPU blog there is mentioning about this variable:

echo 'export LLVM_BIN=/opt/amdgpu-pro/bin' | sudo tee /etc/profile.d/amdgpu-pro.sh

Is there something equivalent for ROCm stack? It would be great if there is so much minute details to get this stack going that you guys make a script that checks against all dependencies, bash variables, libraries etc.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-312524492>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaigYGd3-60rOOaaV4lfzWYAh3i8ks5sKC0ugaJpZM4OLcF9>.



---

### 评论 #9 — jstefanop (2017-07-03T16:07:36Z)

@gstoner Doing a complete fresh Ubuntu server install and well see how it goes. I just want to confirm that the ONLY environment variables needed by ROCm is the OPENCL_ROOT?

Also why the 16x PCIe lanes? We are building custom switchboard that will house 16+ gpus, and the switch can only feed 1x-4x lanes to each GPU (compute algorthms we are running dont require high intera GPU GPU or CPU GPU bandwidth). 



---

### 评论 #10 — gstoner (2017-07-03T17:46:54Z)

You can use smaller number of lanes but they need to be on the PCIe Gen 3 lanes with PCIe atomics support which usually is off the CPU PCIe Root I/O  Here is more info https://rocm.github.io/ROCmPCIeFeatures.html

You can have PLX off the roots.  How many cascading PLX are you looking at. 1 level deep or more.

Greg

On Jul 3, 2017, at 11:07 AM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> Doing a complete fresh Ubuntu server install and well see how it goes. I just want to confirm that the ONLY environment variables needed by ROCm is the OPENCL_ROOT?

Also why the 16x PCIe lanes? We are building custom switchboard that will house 16+ gpus, and the switch can only feed 1x-4x lanes to each GPU (compute algorthms we are running dont require high intera GPU GPU or CPU GPU bandwidth).

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-312684453>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuX2XlhxMGoQu6Wji-6Hrf3P8W-VZks5sKRHJgaJpZM4OLcF9>.



---

### 评论 #11 — jstefanop (2017-07-03T19:03:37Z)

Hmm we actually designed gen 2 switches to keep costs down since we don't need the extra bandwidth. Switch is one level deep. So will the rocm driver not work at all behind the switch for normal Opencl calls?

---

### 评论 #12 — jstefanop (2017-07-03T22:02:31Z)

@gstoner Ok after a clean install we finally got the vega card to work. Please see other two issues opened. Vega performance under ROCm is horribly slow, Polaris cards work at full speed (and vega works full speed under windows). 

---

### 评论 #13 — JustinTArthur (2017-07-06T19:42:46Z)

For anyone having similar problems, I would recommend running the simple [KFD Check Installation shell script](https://raw.githubusercontent.com/HSAFoundation/HSA-Drivers-Linux-AMD/master/kfd_check_installation.sh) using the same environment would be running the OpenCL script on. It discovers GPUs in the same way that the ROCm OpenCL libs do as far as I can tell.

---

### 评论 #14 — gstoner (2017-07-06T20:22:06Z)


@jstefanop  @JustinTArthur   Can you guys run Babelstream on OpenCL and HIP  https://github.com/UoB-HPC/BabelStream. also run Mixbench https://github.com/ekondis/mixbench  there is HIP and OpenCL version of the benchmarks as well.   

---

### 评论 #15 — jstefanop (2017-07-06T20:53:08Z)

Will do, do you have pre compiled windows binaries we can test on windows side for comparison? Don't currently have a windows build environment setup. 

---

### 评论 #16 — gstoner (2017-07-06T20:55:14Z)

Sorry I do not have precompiled binary I alway just build them.




On Jul 6, 2017, at 3:53 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


Will do, do you have pre compiled windows binaries we can test on windows side for comparison? Don't currently have a windows build environment setup.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-313516128>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duabb26GLimAaVML3j3jzD5SyID9_ks5sLUk0gaJpZM4OLcF9>.



---

### 评论 #17 — nevion (2017-07-06T21:03:22Z)

>>We are building custom switchboard that will house 16+ gpus, and the switch can only feed 1x-4x lanes to each GPU (compute algorthms we are running dont require high intera GPU GPU or CPU GPU bandwidth).

Cryptominers detected.  Hopefully this boom ups the ROCm game significantly - particularly performance.  @jstefanop Is your effort private or one of the public ones?

---

### 评论 #18 — gstoner (2017-07-06T21:44:10Z)

One thing for crypto miner developers,   if you want more control of the kernels, we give you access to GCN ISA in the compiler   Please read this https://rocm.github.io/GCN_asm_tutorial.html.   It is how we drove our Winograd solver to 90+ percent efficiency for 3x3 convolutions in MIOpen.  This put you in the power schedule the GPU and use all our instructions for your problem.    

Guys, as I said in a different thread, the ROCm compiler is little over a year old. It's fully open source based LLVM code generator and is not using the same closed source two stage compiler foundation used in our MS Windows Version of OpenCL,  note the Windows Compiler is a two stage Jit with an intermediate language then is finalized through our graphics shader compiler, tightly coupled to the driver.  ROCm Compiler can be updated independently of the base driver. 

The ROCm Compiler source is right here, it is a single compiler that generates Native GCN ISA, you can spill the code with the disassembler and see the ISA.   

- OpenCL Driver https://github.com/RadeonOpenCompute/ROCm-OpenCL-Driver
- LLVM core https://github.com/RadeonOpenCompute/llvm
- Intrinsics/Device libs https://github.com/RadeonOpenCompute/ROCm-Device-Libs

Up to know we have not run currency mining code on ROCm, we were heads down on MIOpen and Deep learning frameworks and building ROCm.  THere is some optimization we are already looking at. 

---

### 评论 #19 — JustinTArthur (2017-07-06T21:56:13Z)

Thanks, @gstoner. All great things. I'm excited about what ROCm means for the future of performance computing.

---

### 评论 #20 — nevion (2017-07-06T21:59:40Z)

@gstoner please don't interpret my comment as impatient criticism, I'm looking at the focus (or illumination) that the cryptoboom will give on performance as improving on the existing performance.  I wasn't throwing criticism around between the lines.  Thanks for the tip on the asm - please point me to the winograd solver kernel you mention as I'm sure I'll learn some lessons from it.  I hope to never have to use it and instead get good enough at coercing the compiler to get it to do what I want, but it's one more weapon in the arsenal.  On a related note, ~~are intrinsic functions in the queue?~~ whoops, I noticed that the last libs pack seems to have that.  Hm I'm still curious why you went to asm if you had intrinsics, or what delta/issues you noticed along the way.  I figure you may not have mapped all functionality to intrinsics too.

---

### 评论 #21 — gstoner (2017-07-06T22:13:15Z)

Guys, I not taking it as criticism, I just want to set the stage for where we at on ROCm,  we are all pushing very hard to make the best possible platform for GPU computing.    

I will tell you we are going to release 1.6.1,  we found one of the issues for Ryzen it is in this release.   

We also have some cool thing cooking to make developing on ROCm easier. 

---

### 评论 #22 — jstefanop (2017-07-06T22:31:57Z)

@gstoner I understand, but in the short term we are trying to figure out which stack to go for (especially since we will most likely go the Radeon Instinct route with Vega). Right now we see the drivers are more or less fully optimized for Vega on windows side, but we obviously cant run our systems on Windows. 

Polaris is more or less fully optimized on linux via the AMDGPU-Pro closed source OpenCL stack, which has comparable performance to the windows drivers. It seems like for Vega you guys went straight with the ROCm openCL components, so will there be a Vega optimized AMDGPU-Pro closed source OpenCL release, or is the OpenCL stack from here on out going to be ROCm based, and well just have to wait until this stack gets optimized for Vega and bugs fixed?

---

### 评论 #23 — gstoner (2017-07-06T22:51:55Z)

Here is magic decoder ring

Polaris, Tonga, Fiji,

  *   AMDGPUPro driver Windows and Linux use historical ORCA/KMD base stack for OpenGL and OpenCL
  *    Use the OpenCL LLVM to HSAIL based historical compiler on Shader Compiler

Vega10 - Forward

  *   MS Windows  PAL/KMD based Stack with Vulkan/OpenCL and DX Use the OpenCL LLVM to HSAIL based historical compiler on ShaderCompiler - Does not support Float16 Packed other features.
  *   AMDGPUpro  ROCm based stack new LC compiler   OpenCL runs on ROCr/KFD + LC compiler

ROCm

  *   Headless Optimized Driver Supports FIJI, Polaris, Vega10 and newer GPU’s   OpenCL runs on ROCr/KFD + LC compiler



On Jul 6, 2017, at 5:31 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> I understand, but in the short term we are trying to figure out which stack to go for (especially since we will most likely go the Radeon Instinct route with Vega). Right now we see the drivers are more or less fully optimized for Vega on windows side, but we obviously cant run our systems on Windows.

Polaris is more or less fully optimized on linux via the AMDGPU-Pro closed source OpenCL stack, which has comparable performance to the windows drivers. It seems like for Vega you guys went straight with the ROCm openCL components, so will there be a Vega optimized AMDGPU-Pro closed source OpenCL release, or is the OpenCL stack from here on out going to be ROCm based, and well just have to wait until this stack gets optimized for Vega and bugs fixed?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-313537130>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuXAn786dH5Ruq-TkGLmIam9xcm4_ks5sLWBegaJpZM4OLcF9>.



---

### 评论 #24 — jstefanop (2017-07-06T23:14:01Z)

Ok great thanks for clearing that up...so driver efforts on compute side going forward (for both ROCm and AMDGPU-Pro) will be focused on ROCr/KFD + LC compiler

---

### 评论 #25 — jstefanop (2017-07-06T23:19:12Z)

Posting benchmark results here until I have performed the tests on both stacks with both Polaris and Vega

Polaris + AMDGPU-Pro 17.10 = https://pastebin.com/E90aSqx6
Polaris + ROCm 1.6 = https://pastebin.com/n14UD7ve
Vega + ROCm 1.6 = https://pastebin.com/DzGTAtj8

---

### 评论 #26 — gstoner (2017-07-07T00:30:54Z)

Thank you for the numbers.  

---

### 评论 #27 — jstefanop (2017-07-07T03:09:54Z)

I updated the comment with all tests on both vega and polaris. As you can see Polaris + AMDGPU-Pro is at near saturation on the memory controller, with closer but a bit slower on the ROCm stack. 

Vega on the other hand is underperforming and not coming close to saturating HBM2 (polaris card actually beat it on mem bandwidth on some tests). The raw compute performance is about where it should be though, but there is obviously something going on with the memory. 

Vega also failed the alternating mix bench test with following error:
Memory access fault by GPU node-1 on address 0x500000000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)

---

### 评论 #28 — gstoner (2017-07-07T03:12:06Z)

Can I get the mem clock and system/cu clock of Vega10.
On Jul 6, 2017, at 10:09 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


I updated the comment with all tests on both vega and polaris. As you can see Polaris + AMDGPU-Pro is at near saturation on the memory controller, with closer but a bit slower on the ROCm stack.

Vega on the other hand is underperforming and not coming close to saturating HBM2 (polaris card actually beat it on mem bandwidth on some tests). The raw compute performance is about where it should be though, but there is obviously something going on with the memory.

Vega also failed the alternating mix bench test with following error:
Memory access fault by GPU node-1 on address 0x500000000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-313575740>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZcpcoV0tfhWg-1sI8Pr2L_Ib7keks5sLaGDgaJpZM4OLcF9>.



---

### 评论 #29 — jstefanop (2017-07-07T03:14:34Z)

Stock clocks for both i.e. 1600/945 on vega, and whatever the stock clock on a Ryzen 5 1400 is. 

---

### 评论 #30 — gstoner (2017-07-07T03:16:01Z)

Thank, so your running auto clock not forced clocks


On Jul 6, 2017, at 10:14 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


Stock clocks for both i.e. 1600/945 on vega, and whatever the stock clock on a Ryzen 5 1400 is.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/143#issuecomment-313576281>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubWoXqEqRvJCfRskUtULgAjOHWQkks5sLaKbgaJpZM4OLcF9>.



---

### 评论 #31 — triosphere (2018-07-30T13:30:21Z)

Hi Greg (or anyone else who cares to comment).  I was wondering if you could point me in a direction, or maybe recommend the most recent download link for ROCm on Linux?  I realize that some of the information I'm about to give you is not directly related to AMD development, but at the risk of offering up too little info as opposed to too much, I'll err on the side of verbosity.

My original intention was to experiment with XMR mining on my OS of choice, Debian.  My hardware is as follows:

Gigabyte GA-B250 FinTech mainboard
Pentium G4400T
8 GB of RAM
Approx. 80 GB HDD
Gigabyte Radeon Vega 64 GPUs

This board can reportedly accommodate 12 GPUs, but I'm only interested in 6 to start, with the possibility of adding more.

When I do a fresh install of Debian 9, I have a single external GPU connected to a PCIe 1x slot via riser and Debian sees it as a Vega video adapter.  I am using the onboard VGA connector for my actual monitor, because presumably I don't need to *see* the video output on my Vegas if I am just mining with them.

I've tried just about every OpenCL flavor in existence, but the farthest I've gotten is to see the OpenCL "platform" but without any devices attached.  Most of the solutions designed for Ubuntu compile and install on Debian.  But in the end when I run XMR-Stak or an equivalent, my Vega isn't detected.  CPU mining works.

I appreciate your info and have been reading numerous threads.  I definitely do not expect any lengthy response, but would be grateful for any suggestions for a Linux driver or GPU monitoring software you can offer, ideally for Debian but I am at a point where I may need to try a different OS.  I definitely do not want to capitulate and use Windows, even though at this stage of driver development I realize there is a significant difference in potential profit from mining.

I can also offer to do some testing with the above hardware if there is anything specific I can help out with.

Thanks.

---

### 评论 #32 — gstoner (2018-07-30T14:29:11Z)

@triosphere To test the system,  run single GPU in 6 slot it is a x16 lane first, they added in the GPUs'. 
Currently, only Vega10 class hardware could run on this hardware with ROCm driver on x1 slots but you have to shut off SDMA.    

Polaris and FIJI  GPU's currently have a Firmware requirement for PCIe Atomics to run, when you use x1 slot they drop to PCIe Gen2 when you use USB enabled RISERs which drop PCIe Atomics support  

One is is Debian right now is not officially supported with our DKMS enable driver.    With 1.9 ROCm it be easier to use upstream Linux kernel aka 4.18 or 4.19 so supporting Debian will be easier.   There is this layer called KCL that has to fixed, which we also asking for to the Linux team

---

### 评论 #33 — triosphere (2018-07-30T14:53:47Z)

Thanks a lot, Greg.  I also noticed you're a music gearhead.  Designed and built my own electric guitar, and thankfully we moved into a larger space with a basement room to hold all my gear.

I'll post any GPU successes.



---

### 评论 #34 — gstoner (2018-07-30T15:00:05Z)

@triosphere Yes love Guitars and tube amps.  Love to have a basement again,  I am in Texas, we hit limestone two feet underground. 

---
