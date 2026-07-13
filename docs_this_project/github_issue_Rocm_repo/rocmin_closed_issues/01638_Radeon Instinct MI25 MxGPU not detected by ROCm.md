# Radeon Instinct MI25 MxGPU not detected by ROCm

- **Issue #:** 1638
- **State:** closed
- **Created:** 2021-12-14T09:55:29Z
- **Updated:** 2024-02-01T04:04:11Z
- **URL:** https://github.com/ROCm/ROCm/issues/1638

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