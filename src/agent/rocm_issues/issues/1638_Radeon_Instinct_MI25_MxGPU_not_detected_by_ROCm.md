# Radeon Instinct MI25 MxGPU not detected by ROCm

> **Issue #1638**
> **状态**: closed
> **创建时间**: 2021-12-14T09:55:29Z
> **更新时间**: 2024-02-01T04:04:11Z
> **关闭时间**: 2024-02-01T04:04:11Z
> **作者**: LeonSpark
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1638

## 描述

### Problem:
neither `/opt/rocm-4.5.0/bin/rocminfo` nor` /opt/rocm-4.5.0/opencl/bin/clinfo` detect my MI25 GPU
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/7710394/clinfo.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/7710391/rocminfo.txt)

### Environment

- Azure VM SKU: Standard NV16as v4
- Linux Distribution Information:
    ```
    uname -m && cat /etc/os-release
    x86_64
    NAME="CentOS Linux"
    VERSION="7 (Core)"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="7"
    PRETTY_NAME="CentOS Linux 7 (Core)"
    ANSI_COLOR="0;31"
    CPE_NAME="cpe:/o:centos:centos:7"
    HOME_URL="https://www.centos.org/"
    BUG_REPORT_URL="https://bugs.centos.org/"
    
    CENTOS_MANTISBT_PROJECT="CentOS-7"
    CENTOS_MANTISBT_PROJECT_VERSION="7"
    REDHAT_SUPPORT_PRODUCT="centos"
    REDHAT_SUPPORT_PRODUCT_VERSION="7"
    ```

- Kernel Information
   ``` 
   uname -srmv
   Linux 3.10.0-1160.31.1.el7.x86_64 #1 SMP Thu Jun 10 13:32:12 UTC 2021 x86_64
   ```
- GPU
  ```
   sudo lshw -class display
    *-display
         description: VGA compatible controller
         product: Hyper-V virtual VGA
         vendor: Microsoft Corporation
         physical id: 8
         bus info: pci@0000:00:08.0
         version: 00
         width: 32 bits
         clock: 33MHz
         capabilities: vga_controller bus_master rom
         configuration: driver=hyperv_fb latency=0
         resources: irq:11 memory:f8000000-fbffffff
    *-display
         description: VGA compatible controller
         product: Vega 10 [Radeon Instinct MI25 MxGPU]
         vendor: Advanced Micro Devices, Inc. [AMD/ATI]
         physical id: 1
         bus info: pci@a26d:00:00.0
         version: 00
         width: 64 bits
         clock: 33MHz
         capabilities: pciexpress msi msix vga_controller cap_list
         configuration: driver=amdgpu latency=0
         resources: iomemory:f0-ef iomemory:f0-ef irq:0 memory:fe0000000-fefffffff memory:ff0000000-ff01fffff memory:40880000-408fffff
  ```

- Amd kernel driver is loaded
  ```
  sudo lspci  -nnk
  0000:00:08.0 VGA compatible controller [0300]: Microsoft Corporation Hyper-V virtual VGA [1414:5353]
          Kernel driver in use: hyperv_fb
          Kernel modules: hyperv_fb
  00c4:00:02.0 Ethernet controller [0200]: Mellanox Technologies MT27710 Family [ConnectX-4 Lx Virtual Function] [15b3:1016] (rev 80)
          Subsystem: Mellanox Technologies Device [15b3:0190]
          Kernel driver in use: mlx5_core
          Kernel modules: mlx5_core
  a26d:00:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 [Radeon Instinct MI25 MxGPU] [1002:686c]
          Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:0c35]
          Kernel driver in use: amdgpu
          Kernel modules: amdgpu
  ```

  @ROCmSupport I follow the ROCm installation guide for 4.5 but it turns out MI25 GPU is not detected by ROCm. I'm experimenting on Azure VM with AMD MI25 GPU, different from other threads, this VM has another Hyper-V compatible VGA and there is no official driver provided by Microsoft on Linux platforms. Could you please help to point out where I was wrong, thanks a lot!

---

## 评论 (8 条)

### 评论 #1 — ROCmSupport (2021-12-20T11:06:36Z)

Thanks @LeonSpark for reaching out.
I certainly understood the problem.
I have tried MI25 on Ubuntu 20.04.3 and I am NOT able to reproduce the issue.
Can you please check once again on the same machine by uninstalling and installing rocm.
Request to share **dmesg** output also.


---

### 评论 #2 — LeonSpark (2021-12-24T08:20:03Z)

Thanks @ROCmSupport  for the reply!
I have retried on Ubuntu 20.04.3
Installation script attached as below:
```bash
sudo apt-get update
sudo apt-get install wget gnupg2
sudo usermod -a -G video $LOGNAME
sudo usermod -a -G render $LOGNAME
sudo apt-get update
wget https://repo.radeon.com/amdgpu-install/21.40.2/ubuntu/focal/amdgpu-install_21.40.2.40502-1_all.deb
sudo apt-get install ./amdgpu-install_21.40.2.40502-1_all.deb
sudo apt-get update
sudo amdgpu-install --usecase=rocm
sudo reboot
```
This time, both `rocminfo` and  `clinfo` don't output the expected results
```
/opt/rocm-4.5.2/bin/rocminfo
ROCk module is NOT loaded, possibly no GPU devices

/opt/rocm-4.5.2/opencl/bin/clinfo
Number of platforms:                             1
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.2 AMD-APP (3361.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback
  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               0
```
**dmesg** output is attached for your reference, many thanks.
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/7773386/dmesg.txt)



---

### 评论 #3 — LeonSpark (2021-12-24T08:30:22Z)

One more thing, after restarting the amdgpu driver is not loaded.  I'm sure the `dkms` is installed.

sudo amdgpu-install --usecase=dkms
```
Reading package lists... Done
Building dependency tree
Reading state information... Done
linux-headers-5.11.0-1022-azure is already the newest version (5.11.0-1022.23~20.04.1).
linux-modules-extra-5.11.0-1022-azure is already the newest version (5.11.0-1022.23~20.04.1).
amdgpu-dkms is already the newest version (1:5.11.32.40502-1350682).
0 upgraded, 0 newly installed, 0 to remove and 16 not upgraded.
```
sudo lshw -class display
```
 *-display
       description: VGA compatible controller
       product: Hyper-V virtual VGA
       vendor: Microsoft Corporation
       physical id: 8
       bus info: pci@0000:00:08.0
       version: 00
       width: 32 bits
       clock: 33MHz
       capabilities: vga_controller bus_master rom
       configuration: driver=hyperv_fb latency=0
       resources: irq:11 memory:f8000000-fbffffff memory:c0000-dffff
  *-display UNCLAIMED
       description: VGA compatible controller
       product: Vega 10 [Radeon Instinct MI25 MxGPU]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 1
       bus info: pci@af8c:00:00.0
       version: 00
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi msix vga_controller cap_list
       configuration: latency=0
       resources: iomemory:f0-ef iomemory:f0-ef memory:fe0000000-fefffffff memory:ff0000000-ff01fffff memory:40080000-400fffff
``` 
The video device is UNCLAIMED

---

### 评论 #4 — suijth (2022-01-03T14:53:54Z)

facing the exact same issue.
Azure Machine: NV4as_v4
OS: Ubuntu 18.04 

---

### 评论 #5 — LeonSpark (2022-01-06T04:36:23Z)

> Thanks @ROCmSupport for the reply! I have retried on Ubuntu 20.04.3 Installation script attached as below:
> 
> ```shell
> sudo apt-get update
> sudo apt-get install wget gnupg2
> sudo usermod -a -G video $LOGNAME
> sudo usermod -a -G render $LOGNAME
> sudo apt-get update
> wget https://repo.radeon.com/amdgpu-install/21.40.2/ubuntu/focal/amdgpu-install_21.40.2.40502-1_all.deb
> sudo apt-get install ./amdgpu-install_21.40.2.40502-1_all.deb
> sudo apt-get update
> sudo amdgpu-install --usecase=rocm
> sudo reboot
> ```
> 
> This time, both `rocminfo` and `clinfo` don't output the expected results
> 
> ```
> /opt/rocm-4.5.2/bin/rocminfo
> ROCk module is NOT loaded, possibly no GPU devices
> 
> /opt/rocm-4.5.2/opencl/bin/clinfo
> Number of platforms:                             1
>   Platform Profile:                              FULL_PROFILE
>   Platform Version:                              OpenCL 2.2 AMD-APP (3361.0)
>   Platform Name:                                 AMD Accelerated Parallel Processing
>   Platform Vendor:                               Advanced Micro Devices, Inc.
>   Platform Extensions:                           cl_khr_icd cl_amd_event_callback
>   Platform Name:                                 AMD Accelerated Parallel Processing
> Number of devices:                               0
> ```
> 
> **dmesg** output is attached for your reference, many thanks. [dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/7773386/dmesg.txt)

@ROCmSupport  Could someone help to take a look at dmesg output? thanks!


---

### 评论 #6 — ROCmSupport (2022-01-25T09:52:40Z)

Hi @LeonSpark 
I have gone through the dmesg and found that its CPU soft lockup.
**watchdog: BUG: soft lockup - CPU#2 stuck for 40s! [swapper/0:1]**
As per my experience, this is not a common issue. This issue is specific to your config only.
Now not seen in my configs and anywhere else. I do not think its due to ROCm.
I too have seen this kind of problem once/twice in one of the specific machines long back(an year ago) and the issue is gone automatically after some days. 

---

### 评论 #7 — ROCmSupport (2022-05-09T04:39:03Z)

Hi @LeonSpark 
I hope this issue is fixed now, recommend to check with the latest ROCm 5.1 and update. Thank you.

---

### 评论 #8 — nartmada (2024-02-01T04:04:11Z)

Closing the ticket as it has become stale.  @LeonSpark, please open another ticket for any new issue.  Thanks.

---
