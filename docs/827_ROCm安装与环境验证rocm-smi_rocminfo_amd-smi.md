# ROCm 安装与环境验证（rocminfo / rocm-smi）

## 学习目标

- 掌握 ROCm 平台的完整安装流程（包括原生安装、DKMS 驱动安装、离线安装）
- 学会使用 rocminfo 和 rocm-smi 验证 GPU 环境并解读输出
- 理解 ROCm 安装后的关键配置文件、环境变量和设备节点
- 能够编写自动化安装和环境验证脚本
- 掌握 Docker 容器中 ROCm 透传的配置方法
- 理解 HSA、amdgpu、amdkfd 在内核态和用户态的分工

## 知识详解

### 一、ROCm 平台架构概览

ROCm（Radeon Open Compute）是 AMD 的开源 GPU 计算平台，其架构分为内核态驱动层、用户态运行时层、库层和工具层四个层次。

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ROCm 软件栈分层架构                               │
│                                                                     │
│  数据来源：ROCm Documentation                                       │
│  https://rocm.docs.amd.com/projects/install-on-linux/en/latest/     │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                     应用层 (Applications)                     │ │
│  │  PyTorch / TensorFlow / HIP 程序 / 自定义计算应用              │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │                     库层 (Libraries)                          │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │ │
│  │  │ rocBLAS  │ │ rocFFT   │ │ MIOpen   │ │ rocPRIM/Thrust   │ │ │
│  │  │ (BLAS)   │ │ (FFT)    │ │ (DNN)    │ │ (Parallel Prims) │ │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘ │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │ │
│  │  │ RCCL     │ │ rocSOLVER│ │ rocSPARSE│ │ hipSPARSE/hipBLAS│ │ │
│  │  │ (Collect)│ │ (Solver) │ │ (Sparse) │ │ (HIP 接口封装)   │ │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘ │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │                   运行时层 (Runtimes)                          │ │
│  │  ┌──────────────────────┐ ┌──────────────────────────────┐    │ │
│  │  │  HIP Runtime         │ │  ROCclr (Common Language     │    │ │
│  │  │  libamdhip64.so      │ │  Runtime - 设备抽象层)       │    │ │
│  │  └──────────────────────┘ └──────────────────────────────┘    │ │
│  │  ┌──────────────────────┐ ┌──────────────────────────────┐    │ │
│  │  │  rocTracer           │ │  hsa-runtime64 (HSA Runtime) │    │ │
│  │  │  (追踪/Profiling)    │ │  libhsa-runtime64.so         │    │ │
│  │  └──────────────────────┘ └──────────────────────────────┘    │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │                  内核态驱动层 (Kernel Drivers)                 │ │
│  │  ┌──────────────────────┐ ┌──────────────────────────────┐    │ │
│  │  │  amdgpu.ko           │ │  amdkfd.ko                   │    │ │
│  │  │  (图形/计算引擎驱动)  │ │  (HSA 内核驱动 - KFD)        │    │ │
│  │  │  管理 GPU 硬件资源     │ │  管理计算队列/用户模式调度   │    │ │
│  │  └──────────────────────┘ └──────────────────────────────┘    │ │
│  │  ┌──────────────────────────────────────────────────────────┐ │ │
│  │  │  DRM 子系统 (Direct Rendering Manager)                    │ │ │
│  │  │  /dev/dri/card*  /dev/dri/renderD*  /dev/kfd             │ │ │
│  │  └──────────────────────────────────────────────────────────┘ │ │
│  │  ┌──────────────────────────────────────────────────────────┐ │ │
│  │  │  GPU 固件 (Firmware)                                     │ │ │
│  │  │  /lib/firmware/amdgpu/*.bin                              │ │ │
│  │  └──────────────────────────────────────────────────────────┘ │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │                     硬件层 (Hardware)                         │ │
│  │  AMD GPU: gfx906(Vega20) / gfx1030(RDNA2) / gfx1100(RDNA3)   │ │
│  │  AMD GPU: gfx908(Arcturus) / gfx90a(Aldebaran) / gfx942(MI300)│ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 1.1 HSA（异构系统架构）概述

ROCm 建立在 HSA（Heterogeneous System Architecture）标准之上。HSA 定义了 CPU 和 GPU 等异构处理器之间统一内存访问、任务调度和同步的模型。

```
┌─────────────────────────────────────────────────────────────────────┐
│                  HSA 核心概念                                        │
│                                                                     │
│  数据来源：HSA Foundation 规范                                      │
│  https://rocm.docs.amd.com/en/latest/conceptual/hsa.html            │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  hUMA (Heterogeneous Unified Memory Access)                   │ │
│  │  ───────────────────────────────────────────────────────────  │ │
│  │  CPU 和 GPU 共享统一虚拟地址空间，指针在两者间可直接传递。     │ │
│  │  GPU 可通过页错误(Page Fault)按需迁移内存页面。                │ │
│  │  在支持 ATS/PRI 的平台上，CPU 和 GPU 共享页表。                │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │  AQL (Architected Queuing Language)                           │ │
│  │  ───────────────────────────────────────────────────────────  │ │
│  │  用户态可直接向 GPU 硬件队列提交命令包(AQL packets)，          │ │
│  │  无需内核介入每次提交。大幅降低命令提交延迟。                   │ │
│  ├───────────────────────────────────────────────────────────────┤ │
│  │  Signals (信号同步)                                           │ │
│  │  ───────────────────────────────────────────────────────────  │ │
│  │  HSA 信号是平台级同步原语，GPU 可以在信号值满足条件时         │ │
│  │  被唤醒，用于内核间依赖和完成通知。                            │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 1.2 amdgpu 与 amdkfd 驱动分工

```
┌─────────────────────────────────────────────────────────────────────┐
│              内核驱动模块职责划分                                    │
│                                                                     │
│  数据来源：Linux 内核源码                                            │
│  drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c                            │
│  drivers/gpu/drm/amd/amdkfd/kfd_module.c                            │
│                                                                     │
│  amdgpu.ko 职责:                                                    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  • GPU 硬件初始化、寄存器操作、时钟管理(DPM)                  │ │
│  │  • 显存(VRAM)分配与管理（TTM/GEM 内存管理器）                 │ │
│  │  • 图形/计算 ring buffer 管理                                 │ │
│  │  • 中断处理、GPU 恢复(reset)                                  │ │
│  │  • PM4 微引擎(ME/CP)控制                                      │ │
│  │  • GPU VM 页表管理（AMDGPU VM）                               │ │
│  │  • 门铃(Doorbell)机制                                         │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  amdkfd.ko 职责:                                                    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  • HSA 设备枚举和 ACPI 拓扑管理（KFD Topology）               │ │
│  │  • 计算队列创建/销毁/调度（用户态队列，AQL 协议）             │ │
│  │  • GPU 进程隔离和地址空间管理                                  │ │
│  │  • GPU 计算调度器(KFD Scheduler)                               │ │
│  │  • 事件通知和中断转发                                         │ │
│  │  • /dev/kfd 字符设备的用户态接口                              │ │
│  │  • CRIU 支持(Checkpoint/Restore)                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  两者通过 amdgpu_amdkfd 接口协作:                                    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  amdkfd 调用 amdgpu 提供的函数指针表                          │ │
│  │  (struct kgd2kfd_calls) 进行硬件操作                           │ │
│  │  amdgpu 调用 amdkfd 提供的函数指针表                          │ │
│  │  (struct kfd2kgd_calls) 通知计算设备事件                      │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 二、ROCm 安装组件结构

```
┌─────────────────────────────────────────────────────────────────────┐
│              ROCm 安装组件结构                                       │
│                                                                     │
│  /opt/rocm/                                                         │
│  ├── bin/                                                            │
│  │   ├── hipcc (HIP 编译器前端)                                      │
│  │   ├── rocminfo (GPU 信息工具)                                     │
│  │   ├── rocm-smi (GPU 管理工具)                                     │
│  │   ├── rocprof (性能剖析工具)                                      │
│  │   ├── rocgdb (GPU 调试工具)                                      │
│  │   ├── amd-smi (新一代 GPU 管理工具)                               │
│  │   ├── hipconfig (HIP 配置查询)                                    │
│  │   └── rocm-bandwidth-test (带宽测试)                              │
│  ├── lib/                                                            │
│  │   ├── libamdhip64.so (HIP Runtime)                                │
│  │   ├── librocblas.so (rocBLAS)                                    │
│  │   ├── librocfft.so (rocFFT)                                      │
│  │   ├── libMIOpen.so (MIOpen)                                      │
│  │   ├── librccl.so (RCCL - 集合通信库)                              │
│  │   ├── libroctx64.so (ROCm Tools Extension)                       │
│  │   ├── libroctracer64.so (ROCTracer)                              │
│  │   ├── libhsa-runtime64.so (HSA Runtime)                          │
│  │   └── libamd_comgr.so (Code Object Manager - 编译器后端集成)      │
│  ├── include/                                                        │
│  │   ├── hip/ (HIP API 头文件)                                       │
│  │   ├── rocblas/ (rocBLAS API)                                     │
│  │   └── miopen/ (MIOpen API)                                       │
│  ├── share/                                                          │
│  │   ├── rocm/  (配置文档)                                           │
│  │   └── miopen/ (MIOpen 数据库文件)                                 │
│  ├── .info/                                                          │
│  │   └── version (ROCm 版本号)                                       │
│  └── llvm/                                                           │
│      └── bin/ (ROCm LLVM 编译工具链)                                 │
│                                                                     │
│  内核模块 (amdgpu + amdkfd):                                         │
│  /lib/modules/$(uname -r)/updates/dkms/                              │
│  /lib/modules/$(uname -r)/kernel/drivers/gpu/drm/amd/                │
│                                                                     │
│  固件文件:                                                            │
│  /lib/firmware/amdgpu/                                               │
│  ├── gc_11_0_0_mes.bin                                               │
│  ├── sdma_6_0_0.bin                                                  │
│  ├── psp_13_0_0.bin                                                  │
│  └── ... (与 GPU ASIC 对应的固件文件)                                │
│                                                                     │
│  数据来源：ROCm 安装文档                                             │
│  https://rocm.docs.amd.com/projects/install-on-linux/                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 三、ROCm 支持的操作系统与硬件兼容性矩阵

> 数据来源：ROCm 官方兼容性页面
> https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html

```
┌─────────────────────────────────────────────────────────────────────┐
│        ROCm 版本与操作系统/硬件兼容性矩阵                            │
│                                                                     │
│  ┌──────────┬────────────────────────────────────────────────────┐ │
│  │ ROCm 版本 │ 支持的操作系统                │ 最低内核版本      │ │
│  ├──────────┼────────────────────────────────────────────────────┤ │
│  │ ROCm 6.2 │ Ubuntu 22.04.5/24.04          │ 5.15 (HWE)        │ │
│  │          │ RHEL 8.10/9.4                  │ 4.18.0-553 (RHEL)│ │
│  │          │ SLES 15 SP5/SP6               │ 5.14.21 (SLES)    │ │
│  ├──────────┼────────────────────────────────────────────────────┤ │
│  │ ROCm 6.1 │ Ubuntu 22.04.4/24.04          │ 5.15              │ │
│  │          │ RHEL 8.9/9.3                  │ 4.18.0-513        │ │
│  ├──────────┼────────────────────────────────────────────────────┤ │
│  │ ROCm 6.0 │ Ubuntu 22.04.3/22.04.4        │ 5.15              │ │
│  │          │ RHEL 8.9/9.3                  │ 4.18.0-513        │ │
│  └──────────┴────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │ 支持的 GPU 及对应的 gfx 目标                                  │   │
│  │ ──────────────────────────────────────────────────────────── │   │
│  │ gfx906 (Vega 20)        : Radeon VII, MI50/MI60              │   │
│  │ gfx908 (Arcturus)       : MI100                              │   │
│  │ gfx90a (Aldebaran)      : MI200 系列 (MI250/MI210/MI250X)   │   │
│  │ gfx942                  : MI300 系列 (MI300X/MI300A)         │   │
│  │ gfx1030 (Navi21)        : RX 6900 XT, RX 6800 等            │   │
│  │ gfx1031 (Navi22)        : RX 6700 XT                        │   │
│  │ gfx1032 (Navi23)        : RX 6600 系列                      │   │
│  │ gfx1100 (Navi31)        : RX 7900 XTX/XT                   │   │
│  │ gfx1101 (Navi32)        : RX 7800 XT                       │   │
│  │ gfx1102 (Navi33)        : RX 7600 系列                      │   │
│  │ gfx1150 (Phoenix)       : Ryzen 7040 APU (集成显卡)         │   │
│  │ gfx1151 (Hawk Point)    : Ryzen 8040 APU (集成显卡)          │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  注意：ROCm 6.0+ 对 RDNA3 (gfx11xx) 支持为正式支持                  │
│  RDNA2 (gfx103x) 为正式支持                                         │
│  Vega 架构 (gfx906) 自 ROCm 5.6+ 为"社区支持"级别                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 四、ROCm 安装流程详解

#### 4.1 安装前系统准备

安装 ROCm 之前需要确保系统满足以下条件：

```
┌─────────────────────────────────────────────────────────────────────┐
│                 安装前检查清单                                       │
│                                                                     │
│  数据来源：ROCm Install on Linux                                    │
│  https://rocm.docs.amd.com/projects/install-on-linux/en/latest/     │
│  install/preinstall.html                                            │
│                                                                     │
│  必要条件:                                                          │
│  □ 支持的 Linux 发行版（Ubuntu 22.04/24.04, RHEL 8/9, SLES 15）    │
│  □ 内核版本满足要求（Ubuntu: ≥5.15）                                │
│  □ GPU 硬件在 ROCm 支持列表中                                      │
│  □ amdgpu 驱动已安装（内核自带或 DKMS）                            │
│  □ 已安装必要的固件包 (linux-firmware 或 amdgpu-firmware)           │
│  □ 系统已更新到最新状态                                              │
│                                                                     │
│  可选条件（推荐）:                                                   │
│  □ 禁用 IOMMU 或配置为 passthrough 模式（某些平台需要）            │
│  □ 安装 numactl 用于 NUMA 感知优化                                 │
│  □ 配置 HugePages（2MB 或 1GB）                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**详细检查命令：**

```bash
#!/bin/bash
# preinstall_check.sh - ROCm 安装前系统检查

echo "=============================================="
echo " ROCm 安装前系统检查"
echo "=============================================="

# 1. 检查发行版
echo ""
echo "--- 1. 操作系统信息 ---"
echo "发行版: $(lsb_release -d 2>/dev/null | cut -f2)"
echo "版本号: $(lsb_release -rs 2>/dev/null)"
echo "架构: $(uname -m)"

# 2. 检查内核版本
echo ""
echo "--- 2. 内核版本 ---"
KERNEL_VER=$(uname -r)
echo "内核版本: $KERNEL_VER"
KERNEL_MAJOR=$(echo $KERNEL_VER | cut -d. -f1)
KERNEL_MINOR=$(echo $KERNEL_VER | cut -d. -f2)
if [ "$KERNEL_MAJOR" -ge 6 ] || { [ "$KERNEL_MAJOR" -eq 5 ] && [ "$KERNEL_MINOR" -ge 15 ]; }; then
    echo "✅ 内核版本满足要求 (≥5.15)"
else
    echo "⚠ 内核版本可能不满足要求，需 ≥5.15"
fi

# 3. 检查 GPU 硬件
echo ""
echo "--- 3. GPU 硬件检测 ---"
GPU_INFO=$(lspci -nn | grep -iE 'VGA|3D|Display' | grep -iE 'AMD|ATI|Advanced Micro')
if [ -n "$GPU_INFO" ]; then
    echo "发现 AMD GPU:"
    echo "$GPU_INFO"
else
    echo "❌ 未检测到 AMD GPU"
    exit 1
fi

# 4. 检查现有 amdgpu 驱动状态
echo ""
echo "--- 4. amdgpu 驱动状态 ---"
if lsmod | grep -q amdgpu; then
    echo "✅ amdgpu 驱动已加载"
    modinfo amdgpu 2>/dev/null | grep -E "^version|^filename"
else
    echo "⚠ amdgpu 驱动未加载，安装 ROCm 时会自动安装"
fi

# 5. 检查固件版本
echo ""
echo "--- 5. GPU 固件状态 ---"
GPU_ASIC_DIR="/lib/firmware/amdgpu"
if [ -d "$GPU_ASIC_DIR" ]; then
    echo "固件目录: $GPU_ASIC_DIR"
    FIRMWARE_COUNT=$(ls "$GPU_ASIC_DIR"/*.bin 2>/dev/null | wc -l)
    echo "固件文件数: $FIRMWARE_COUNT"
else
    echo "⚠ 未找到固件目录，需要安装 linux-firmware"
fi

# 6. 检查内存和 swap
echo ""
echo "--- 6. 系统内存 ---"
free -h
echo ""
echo "--- 7. 磁盘空间 ---"
df -h /opt /tmp 2>/dev/null

# 7. 检查关键内核参数
echo ""
echo "--- 8. 内核启动参数 ---"
cat /proc/cmdline 2>/dev/null
echo ""
echo "检查 IOMMU 是否启用:"
dmesg 2>/dev/null | grep -i iommu | head -5 || echo "  无法读取 dmesg，请以 sudo 运行"

echo ""
echo "=============================================="
echo " 检查完成"
echo "=============================================="
```

#### 4.2 完整安装流程（Ubuntu 24.04 示例）

```bash
#!/bin/bash
# install_rocm_ubuntu24.sh - 完整 ROCm 安装脚本

set -e

ROCm_VERSION=${1:-6.2.4}
UBUNTU_CODENAME=$(lsb_release -cs 2>/dev/null || echo "noble")

echo "=============================================="
echo " ROCm ${ROCm_VERSION} 安装脚本"
echo " 目标系统: Ubuntu ${UBUNTU_CODENAME}"
echo "=============================================="

# 1. 系统更新
echo ""
echo "【1/10】系统更新"
sudo apt-get update
sudo apt-get upgrade -y

# 2. 安装基础依赖
echo ""
echo "【2/10】安装基础依赖"
sudo apt-get install -y \
    wget gnupg2 software-properties-common \
    build-essential cmake git \
    python3 python3-pip python3-venv \
    numactl pciutils

# 3. 确保固件是最新版本
echo ""
echo "【3/10】更新 GPU 固件"
sudo apt-get install -y linux-firmware
# 检查关键固件是否存在 (以 RDNA3 Navi31 gfx1100 为例)
FIRMWARE_FILES=(
    "gc_11_0_0_mes.bin"
    "gc_11_0_0_mes1.bin"
    "psp_13_0_0_toc.bin"
    "sdma_6_0_0.bin"
    "vcn_4_0_0.bin"
)
echo "  检查关键固件文件:"
for fw in "${FIRMWARE_FILES[@]}"; do
    if [ -f "/lib/firmware/amdgpu/$fw" ]; then
        echo "    ✅ $fw"
    else
        echo "    ⚠ $fw 未找到"
    fi
done

# 4. 添加 ROCm 仓库密钥
echo ""
echo "【4/10】添加 ROCm 仓库 GPG 密钥"
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | \
    sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/rocm.gpg

# 5. 添加 ROCm APT 仓库
echo ""
echo "【5/10】配置 ROCm APT 仓库"
echo "deb [arch=amd64] https://repo.radeon.com/rocm/apt/${ROCm_VERSION} ${UBUNTU_CODENAME} main" | \
    sudo tee /etc/apt/sources.list.d/rocm.list
echo "deb [arch=amd64] https://repo.radeon.com/amdgpu/${ROCm_VERSION}/ubuntu ${UBUNTU_CODENAME} main" | \
    sudo tee /etc/apt/sources.list.d/amdgpu.list

sudo apt-get update

# 6. 安装 ROCm 核心包
echo ""
echo "【6/10】安装 ROCm 核心组件"
sudo apt-get install -y \
    rocm-hip-sdk \
    rocm-hip-libraries \
    rocm-device-libs \
    rocm-core \
    rocm-smi-lib \
    rocm-cmake \
    rocm-language-runtime \
    rocm-clang-ocl \
    rocm-opencl-sdk \
    rocm-ml-sdk

# 7. 安装内核驱动（如需要）
echo ""
echo "【7/10】安装内核驱动"
sudo apt-get install -y amdgpu-dkms rocm-dkms 2>/dev/null || {
    echo "  ⚠ amdgpu-dkms 可能已由内核自带，检查驱动状态"
    sudo modprobe amdgpu 2>/dev/null || true
    sudo modprobe amdkfd 2>/dev/null || true
}

# 8. 添加用户到必要组
echo ""
echo "【8/10】配置用户权限"
sudo usermod -a -G render,video $USER
echo "  当前用户 $USER 已添加到 render 和 video 组"

# 9. 配置 udev 规则
echo ""
echo "【9/10】配置 udev 规则"
sudo tee /etc/udev/rules.d/70-amdgpu.rules > /dev/null << 'UDEVEOF'
KERNEL=="kfd", GROUP="render", MODE="0660"
KERNEL=="renderD*", GROUP="render", MODE="0660"
KERNEL=="card*", GROUP="video", MODE="0660"
UDEVEOF
sudo udevadm control --reload-rules
sudo udevadm trigger

# 10. 配置环境变量
echo ""
echo "【10/10】配置环境变量"
BASHRC_FILE="$HOME/.bashrc"
if ! grep -q "ROCM_PATH" "$BASHRC_FILE"; then
    cat >> "$BASHRC_FILE" << 'EOF'

# ROCm Environment Variables
export ROCM_PATH=/opt/rocm
export HIP_PATH=/opt/rocm
export HIP_PLATFORM=amd
export PATH=$ROCM_PATH/bin:$PATH
export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH
EOF
    echo "  ✅ 环境变量已添加到 $BASHRC_FILE"
else
    echo "  环境变量已存在，跳过"
fi

echo ""
echo "=============================================="
echo " ROCm ${ROCm_VERSION} 安装完成"
echo "=============================================="
echo ""
echo "后续步骤:"
echo "  1. 重新启动系统: sudo reboot"
echo "  2. 重启后验证:"
echo "     source ~/.bashrc"
echo "     rocminfo"
echo "     rocm-smi"
echo "     /opt/rocm/bin/hipcc --version"
echo ""
```

#### 4.3 RHEL/Rocky Linux 安装流程

```bash
#!/bin/bash
# install_rocm_rhel9.sh - RHEL 9 / Rocky Linux 9 安装脚本

set -e

ROCm_VERSION=${1:-6.2.4}
RHEL_VERSION=$(rpm -E %rhel 2>/dev/null || echo "9")

echo "=============================================="
echo " ROCm ${ROCm_VERSION} RHEL ${RHEL_VERSION} 安装"
echo "=============================================="

# 1. 安装 EPEL 和基础依赖
echo ""
echo "【1】安装 EPEL 和依赖"
sudo dnf install -y epel-release
sudo dnf config-manager --set-enabled crb 2>/dev/null || \
    sudo dnf config-manager --set-enabled powertools 2>/dev/null || true
sudo dnf install -y \
    kernel-devel kernel-headers \
    dkms gcc gcc-c++ make cmake \
    wget git numactl-libs pciutils

# 2. 添加 ROCm 仓库
echo ""
echo "【2】添加 ROCm 仓库"
sudo tee /etc/yum.repos.d/rocm.repo > /dev/null << REPOEOF
[ROCm-${ROCm_VERSION}]
name=ROCm ${ROCm_VERSION}
baseurl=https://repo.radeon.com/rocm/rhel/${ROCm_VERSION}/main
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
REPOEOF

# 3. 安装 ROCm
echo ""
echo "【3】安装 ROCm 包"
sudo dnf install -y \
    rocm-hip-sdk \
    rocm-hip-libraries \
    rocm-device-libs \
    rocm-core \
    rocm-smi-lib

# 4. 内核驱动
echo ""
echo "【4】安装内核驱动"
sudo dnf install -y amdgpu-dkms rocm-dkms 2>/dev/null || true

# 5. 权限和 udev
echo ""
echo "【5】配置权限"
sudo usermod -a -G render,video $USER
sudo tee /etc/udev/rules.d/70-amdgpu.rules > /dev/null << 'UDEVEOF'
KERNEL=="kfd", GROUP="render", MODE="0660"
KERNEL=="renderD*", GROUP="render", MODE="0660"
KERNEL=="card*", GROUP="video", MODE="0660"
UDEVEOF
sudo udevadm control --reload-rules

echo ""
echo "=== 安装完成，请重新启动系统 ==="
```

#### 4.4 从源码编译 ROCm（高级）

> 数据来源：ROCm 官方构建指南
> https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/build-from-source.html

```bash
#!/bin/bash
# build_rocm_from_source.sh - 从源码编译 ROCm 组件
# 注意：完整编译可能需要数小时，需要大量磁盘空间(≥100GB)
# 以下为关键组件的编译示例

set -e

ROCM_ROOT="$HOME/ROCm-source"
mkdir -p "$ROCM_ROOT"
cd "$ROCM_ROOT"

# 编译 ROCclr (Common Language Runtime)
echo "=== 编译 ROCclr ==="
git clone --depth 1 https://github.com/ROCm/ROCclr.git
mkdir -p ROCclr/build && cd ROCclr/build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install
cd "$ROCM_ROOT"

# 编译 HIP
echo "=== 编译 HIP ==="
git clone --depth 1 https://github.com/ROCm/HIP.git
mkdir -p HIP/build && cd HIP/build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install
cd "$ROCM_ROOT"

# 编译 rocBLAS
echo "=== 编译 rocBLAS ==="
git clone --depth 1 https://github.com/ROCm/rocBLAS.git
mkdir -p rocBLAS/build && cd rocBLAS/build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=Release \
    -DAMDGPU_TARGETS=gfx1100
make -j$(nproc)
sudo make install

echo "=== 编译完成 ==="
```

### 五、rocminfo 详解

> 数据来源：ROCm rocminfo 文档
> https://rocm.docs.amd.com/projects/rocminfo/en/latest/

#### 5.1 rocminfo 源码位置与原理

rocminfo 工具的源码位于 [ROCm/rocminfo](https://github.com/ROCm/rocminfo) 仓库。其核心工作原理是：

1. 调用 HSA Runtime API (`hsa_init()`, `hsa_iterate_agents()`) 枚举系统中所有 HSA agent（包括 CPU 和 GPU）
2. 对每个 GPU agent 查询其属性（`hsa_agent_get_info()`）
3. 查询每个 agent 关联的内存池（`hsa_amd_agent_iterate_memory_pools()`）
4. 查询 ISA 信息（`hsa_agent_iterate_isas()`）
5. 格式化输出所有信息

```
┌─────────────────────────────────────────────────────────────────────┐
│            rocminfo 数据获取流程                                     │
│                                                                     │
│  rocminfo 二进制                                                    │
│     │                                                               │
│     ├─ hsa_init()                                                   │
│     │    └─ 初始化 HSA Runtime，加载 libhsa-runtime64.so            │
│     │                                                               │
│     ├─ hsa_iterate_agents()                                         │
│     │    └─ 回调函数遍历所有 Agent                                   │
│     │       ├─ Agent 0: CPU (Kaveri/Ryzen/EPYC)                    │
│     │       ├─ Agent 1: GPU 0 (如 gfx1100)                         │
│     │       └─ Agent N: GPU N                                      │
│     │                                                               │
│     ├─ hsa_agent_get_info() [每个 GPU Agent]                        │
│     │    ├─ HSA_AGENT_INFO_NAME          → "AMD Radeon RX 7900 XTX" │
│     │    ├─ HSA_AGENT_INFO_VENDOR_NAME   → "AMD"                   │
│     │    ├─ HSA_AGENT_INFO_CACHE_SIZE    → L1/L2/L3 缓存大小        │
│     │    ├─ HSA_AGENT_INFO_WAVEFRONT_SIZE → 32/64 (wavefront 大小)  │
│     │    └─ HSA_AMD_AGENT_INFO_CHIP_ID   → 芯片 ID                  │
│     │                                                               │
│     ├─ hsa_amd_agent_iterate_memory_pools()                         │
│     │    ├─ Pool: VRAM (GPU 本地显存)                               │
│     │    ├─ Pool: GTT (通过 PCIe 的系统内存)                         │
│     │    └─ Pool: System (CPU 侧系统内存)                            │
│     │                                                               │
│     └─ hsa_agent_iterate_isas()                                     │
│          └─ 列出支持的 ISA (如 amdgcn-amd-amdhsa--gfx1100)          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 5.2 rocminfo 完整输出示例及注释

以下是一个典型的 `rocminfo` 输出（基于 AMD Radeon RX 7900 XTX, gfx1100, ROCm 6.2），带逐段注释：

```

================================================================================
ROCk module (ROCm Kernel Driver) is loaded     ← KFD 驱动已加载
================================================================================
HSA System Attributes
================================================================================
Runtime Version:         1.14                    ← HSA Runtime 版本
Runtime Ext Version:     1.6
System Timestamp Freq.:  1000.000000MHz          ← 系统时间戳频率
Sig. Max Wait Duration:  18446744073709551616    ← 信号最大等待 (2^64-1)
Machine Model:           LARGE                   ← 大内存模型 (64位地址空间)
System Endianness:       LITTLE                   ← 小端字节序
Mwaitx:                  DISABLED

================================================================================
HSA Agents
================================================================================

*******                  ← 注意：星号数量指示硬件 NUMA 拓扑层级
Agent 1                  ← Agent 0 通常是 CPU，这里从 Agent 1 开始

  Name:                    AMD Radeon RX 7900 XTX   ← GPU 名称
  UID:                     GPU-XX                    ← 唯一标识符
  Marketing Name:          AMD Radeon RX 7900 XTX    ← 市场名称
  Vendor Name:             AMD                       ← 供应商
  Feature:                 KERNEL_DISPATCH           ← 支持内核分发
  Profile:                 FULL_PROFILE               ← 完整功能
  Float Round Mode:        NEAR                      ← 浮点舍入模式
  Max Queue Number:        128                       ← 最大队列数
  Queue Min Size:          64                        ← 队列最小大小
  Queue Max Size:          131072                    ← 队列最大大小
  Queue Type:              MULTI                     ← 多队列类型

  Node:                    1                         ← NUMA 节点编号
  Device Type:             GPU                       ← 设备类型
  Cache Info:
    L1:                      32KB                    ← L1 缓存 (每 CU)
    L2:                      6144KB                  ← L2 缓存 (共享)
    L3:                      98304KB                 ← L3/Infinity Cache
  Chip ID:                 7448                      ← GPU 芯片 ID (十进制)
  ASIC Revision:           0                         ← 芯片版本
  Cacheline Size:          64                        ← 缓存行大小
  Max Clock Freq. (MHz):   3200                      ← 最大核心频率
  BDFID:                   768                       ← PCIe BDF (Bus/Device/Function)
  Internal Node ID:        1
  Compute Unit:            96                        ← 计算单元数 (CU)
  SIMDs per CU:            2                         ← 每 CU 的 SIMD 数
  Shader Engines:          6                         ← 着色器引擎数
  Shader Arrs. per Eng.:   2                         ← 每引擎着色器阵列数
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE                     ← 不支持一致主机访问
  Max Workgroup Size:      1024                      ← 最大工作组大小
  Max Waves per CU:        32                        ← 每 CU 最大 Wave 数
  Max fbarriers/Workgrp:   32                        ← 最大栅栏数
  Packet Processor uCode:: 1040                      ← PM4 微码版本
  SDMA engine uCode::      87                        ← SDMA 微码版本
  IOMMU Support::          None                      ← IOMMU 支持状态
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    25153536(23.988GB)    ← VRAM 总大小
      Allocatable:             TRUE                  ← 可分配
      Alloc Granule:           4KB                   ← 分配粒度
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE                  ← 非全部 agent 可访问
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25153536(23.988GB)
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0.0001GB)           ← 本地组内存 (LDS)
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1100       ← ISA 名称
      Machine Models:          HSA_MACHINE_MODEL_LARGE          ← 支持的机器模型
      Profiles:                HSA_PROFILE_FULL                 ← 完整配置
      Default Rounding Mode:   NEAR                             ← 默认舍入
      Fast f16:                TRUE                             ← 快速半精度支持
      Workgroup Max Size:      1024                             ← 工作组最大尺寸
      Workgroup Max Size per Dimension:
        x                        1024
        y                        1024
        z                        1024
      Max Grid Size:           4294967295
      Max number of fbarriers per Workgroup: 32
```

#### 5.3 rocminfo 输出层级结构

```
┌─────────────────────────────────────────────────────────────────────┐
│  输出层级        说明                    关键字段                     │
│  ─────────────────────────────────────────────────────────────      │
│  System          ROCm 系统信息         版本号 / 系统属性             │
│  ├── Agent 0     CPU Agent             名称 / 核心 / 缓存            │
│  ├── Agent 1     GPU Agent 0           计算单元 / 显存               │
│  │   ├── Pool    VRAM/GTT/系统内存池   大小 / 可访问性               │
│  │   ├── ISA     支持的 ISA             gfx1100 (RDNA3)             │
│  │   └── Cache   GPU 缓存层次           L1 / L2 / L3 大小           │
│  └── Agent N     GPU Agent N           (多 GPU 系统)                │
│                                                                     │
│  ISA 命名规则：amdgcn-amd-amdhsa--gfxXXXX                           │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ amdgcn      = AMD GPU 架构标识                               │   │
│  │ amd         = 供应商标识                                     │   │
│  │ amdhsa      = AMD HSA ABI (应用程序二进制接口)               │   │
│  │ gfxXXXX     = 具体 GPU 目标架构 (如 gfx1100 = RDNA3 Navi31)  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 5.4 rocminfo 编程接口（C 语言示例）

```c
/*
 * rocminfo_custom.c - 使用 HSA API 获取 GPU 信息
 *
 * 编译：hipcc -o rocminfo_custom rocminfo_custom.c -lhsa-runtime64
 *
 * 数据来源：HSA Runtime API 文档
 * https://rocm.docs.amd.com/projects/HSA-Runtime/
 */

#include <hsa.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define CHECK_HSA(err, msg) \
    do { \
        if (err != HSA_STATUS_SUCCESS) { \
            const char *err_str; \
            hsa_status_string(err, &err_str); \
            fprintf(stderr, "%s: %s\n", msg, err_str); \
            exit(1); \
        } \
    } while (0)

static hsa_status_t agent_callback(hsa_agent_t agent, void *data)
{
    char name[64];
    hsa_device_type_t dev_type;
    uint32_t cu_count;
    uint16_t vendor_id;
    uint32_t cache_size[4];
    uint32_t wavefront_size;

    hsa_agent_get_info(agent, HSA_AGENT_INFO_NAME, name);
    hsa_agent_get_info(agent, HSA_AGENT_INFO_DEVICE, &dev_type);

    if (dev_type == HSA_DEVICE_TYPE_CPU) {
        printf("\n=== Agent: %s (CPU) ===\n", name);
        hsa_agent_get_info(agent, HSA_AGENT_INFO_CACHE_SIZE, cache_size);
        printf("  L1 Cache: %u bytes\n", cache_size[0]);
        return HSA_STATUS_SUCCESS;
    }

    if (dev_type != HSA_DEVICE_TYPE_GPU)
        return HSA_STATUS_SUCCESS;

    printf("\n=== Agent: %s (GPU) ===\n", name);

    hsa_agent_get_info(agent, HSA_AGENT_INFO_VENDOR_ID, &vendor_id);
    printf("  Vendor ID: 0x%04x\n", vendor_id);

    hsa_agent_get_info(agent, HSA_AGENT_INFO_WAVEFRONT_SIZE, &wavefront_size);
    printf("  Wavefront Size: %u\n", wavefront_size);

    hsa_agent_get_info(agent, (hsa_agent_info_t)HSA_AMD_AGENT_INFO_COMPUTE_UNIT_COUNT, &cu_count);
    printf("  Compute Units: %u\n", cu_count);

    hsa_agent_get_info(agent, HSA_AGENT_INFO_CACHE_SIZE, cache_size);
    printf("  L1: %u KB, L2: %u KB, L3: %u KB, L4: %u KB\n",
           cache_size[0]/1024, cache_size[1]/1024, cache_size[2]/1024, cache_size[3]/1024);

    uint32_t node;
    hsa_agent_get_info(agent, HSA_AGENT_INFO_NODE, &node);
    printf("  NUMA Node: %u\n", node);

    hsa_amd_memory_pool_t pool_list[16];
    hsa_amd_agent_iterate_memory_pools(agent, NULL, NULL);
    hsa_status_t pool_status;
    int pool_idx = 0;

    printf("\n  Memory Pools:\n");
    while (1) {
        pool_status = hsa_amd_agent_iterate_memory_pools(agent, &pool_list[pool_idx], NULL);
        if (pool_status != HSA_STATUS_SUCCESS) break;

        hsa_amd_memory_pool_t pool = pool_list[pool_idx];
        size_t pool_size;
        hsa_amd_memory_pool_get_info(pool, HSA_AMD_MEMORY_POOL_INFO_SIZE, &pool_size);

        hsa_amd_segment_t segment;
        hsa_amd_memory_pool_get_info(pool, HSA_AMD_MEMORY_POOL_INFO_SEGMENT, &segment);

        const char *seg_name;
        switch (segment) {
            case HSA_AMD_SEGMENT_GLOBAL:   seg_name = "GLOBAL"; break;
            case HSA_AMD_SEGMENT_GROUP:    seg_name = "GROUP(LDS)"; break;
            case HSA_AMD_SEGMENT_PRIVATE:  seg_name = "PRIVATE"; break;
            default:                       seg_name = "UNKNOWN"; break;
        }

        printf("    Pool %d: %s, Size: %.2f GB\n", pool_idx, seg_name,
               (double)pool_size / (1024.0 * 1024.0 * 1024.0));
        pool_idx++;
    }

    return HSA_STATUS_SUCCESS;
}

int main(void)
{
    hsa_status_t status;

    status = hsa_init();
    CHECK_HSA(status, "hsa_init failed");

    printf("HSA System Info\n");
    printf("================\n");

    uint16_t version_major, version_minor;
    hsa_system_get_info(HSA_SYSTEM_INFO_VERSION_MAJOR, &version_major);
    hsa_system_get_info(HSA_SYSTEM_INFO_VERSION_MINOR, &version_minor);
    printf("HSA Runtime Version: %u.%u\n", version_major, version_minor);

    status = hsa_iterate_agents(agent_callback, NULL);
    CHECK_HSA(status, "hsa_iterate_agents failed");

    status = hsa_shut_down();
    CHECK_HSA(status, "hsa_shut_down failed");

    return 0;
}
```

### 六、rocm-smi 完整用法

> 数据来源：rocm-smi 官方文档
> https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/

#### 6.1 rocm-smi 架构原理

rocm-smi（ROCm System Management Interface）通过 `librocm_smi64.so` 库与 `amdgpu` 内核驱动通信，读取 sysfs、debugfs 接口和通过 ioctl 调用来获取 GPU 状态和控制 GPU 行为。

```
┌─────────────────────────────────────────────────────────────────────┐
│                rocm-smi 数据流                                       │
│                                                                     │
│  rocm-smi CLI                                                       │
│     │                                                               │
│     ├─ librocm_smi64.so (用户态库)                                  │
│     │    ├─ PCIe 配置空间读取 (lspci 风格)                           │
│     │    ├─ /sys/class/drm/cardX/device/* (sysfs)                    │
│     │    │    ├─ pp_dpm_sclk       (GPU 核心频率档位)               │
│     │    │    ├─ pp_dpm_mclk       (显存频率档位)                   │
│     │    │    ├─ pp_od_clk_voltage (超频控制)                       │
│     │    │    ├─ hwmon/hwmonX/temp1_input (温度)                    │
│     │    │    ├─ hwmon/hwmonX/power1_average (平均功耗)             │
│     │    │    ├─ mem_info_vram_total (VRAM 总量)                    │
│     │    │    └─ mem_info_vis_vram_total (可见 VRAM 总量)           │
│     │    └─ /sys/class/kfd/kfd/topology/nodes/X/* (KFD 拓扑)       │
│     │                                                                 │
│     └─ 底层通信：ioctl(fd, DRM_IOCTL_AMDGPU_*, ...)                  │
│                                                                     │
│  数据来源：                                                          │
│  drivers/gpu/drm/amd/pm/amdgpu_pm.c (电源管理 sysfs)                │
│  drivers/gpu/drm/amd/amdgpu/amdgpu_kms.c (KMS sysfs)               │
│  https://github.com/ROCm/rocm_smi_lib                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 6.2 rocm-smi 命令参考

```bash
#!/bin/bash
# rocm_smi_guide.sh - rocm-smi 完整使用指南

echo "=============================================="
echo " rocm-smi 使用指南"
echo "=============================================="

# 1. 基本信息
echo ""
echo "【1】基本 GPU 信息"
rocm-smi --showproductname
# 输出示例:
# ======================== ROCm System Management Interface ========================
# ========================= Product Info ============================================
# GPU[0]        : Card Series:   AMD Radeon RX 7900 XTX
# GPU[0]        : Card Model:    0x7448
# GPU[0]        : Card Vendor:   Advanced Micro Devices, Inc. [AMD/ATI]
# GPU[0]        : Card SKU:      GFX1100

# 2. 温度
echo ""
echo "【2】GPU 温度"
rocm-smi --showtemp
# 输出:
# ======================== ROCm System Management Interface ========================
# ========================= Temperature Info =======================================
# GPU[0]        : Temperature (edge): 45.0 C
# GPU[0]        : Temperature (junction): 48.0 C
# GPU[0]        : Temperature (mem): 52.0 C

# 3. 频率
echo ""
echo "【3】GPU 频率"
rocm-smi --showclocks
# 输出:
# ======================== ROCm System Management Interface ========================
# ============================== Clock Info ========================================
# GPU[0]        : mclk: 0.100 GHz
# GPU[0]        : sclk: 0.100 GHz

# 4. 功耗
echo ""
echo "【4】GPU 功耗"
rocm-smi --showpower
# 输出:
# ======================== ROCm System Management Interface ========================
# ========================= Power Info =============================================
# GPU[0]        : Average Power: 15.0 W
# GPU[0]        : Current Socket Power: 15.0 W
# GPU[0]        : Power Limit: 355.0  W

# 5. 显存使用
echo ""
echo "【5】显存使用"
rocm-smi --showmeminfo vram
# 输出:
# ======================== ROCm System Management Interface ========================
# ======================== Memory Usage (VRAM) =====================================
# GPU[0]        : VRAM Total: 24560 MB
# GPU[0]        : VRAM Used:  1234  MB

# 6. GPU 利用率
echo ""
echo "【6】GPU 利用率"
rocm-smi --showuse
# 输出:
# ======================== ROCm System Management Interface ========================
# =========================== GPU Use Info =========================================
# GPU[0]        : GPU use (%): 0

# 7. 拓扑
echo ""
echo "【7】GPU 拓扑 (PCIe/NUMA 关系)"
rocm-smi --showtopo
# 输出:
# ======================== ROCm System Management Interface ========================
# =========================== Topology Info ========================================
#   GPU[0]  :  PCIe Link Speed: 16.0 GT/s
#   GPU[0]  :  PCIe Link Width: 16

# 8. 全部信息
echo ""
echo "【8】全部信息 (JSON 格式)"
rocm-smi --showallinfo --json 2>/dev/null | python3 -m json.tool | head -80

# 9. 持续监控 (CSV 输出)
echo ""
echo "【9】持续监控 (CSV, 2 秒间隔, 10 次采样)"
rocm-smi --csv -i 2 -n 10 --showuse --showpower --showtemp --showclocks 2>/dev/null

# 10. 频率控制
echo ""
echo "【10】频率控制"
echo "  查看可用 SCLK 档位:"
rocm-smi --showclocks
echo ""
echo "  设置 SCLK 到档位 3:"
rocm-smi --setsclk 3 2>/dev/null && echo "  ✅ SCLK set to level 3"
echo "  重置 SCLK 到默认:"
rocm-smi --resetclocks 2>/dev/null && echo "  ✅ Clocks reset to default"

# 11. 功耗上限设置
echo ""
echo "【11】功耗上限设置"
echo "  设置功耗上限为 300W:"
rocm-smi --setpoweroverdrive 300 2>/dev/null && echo "  ✅ Power limit set to 300W"

# 12. 风扇控制
echo ""
echo "【12】风扇控制"
echo "  查看风扇转速:"
rocm-smi --showfan
echo ""
echo "  设置风扇转速为 50%:"
rocm-smi --setfan 50 2>/dev/null && echo "  ✅ Fan speed set to 50%"

# 13. 固件版本
echo ""
echo "【13】固件版本"
rocm-smi --showfwinfo

# 14. 电压
echo ""
echo "【14】电压信息"
rocm-smi --showvoltage

# 15. ECC 错误计数 (仅 MI 系列数据中心 GPU)
echo ""
echo "【15】ECC 错误计数"
rocm-smi --show-ecc-count 2>/dev/null && echo "  ✅" || echo "  (不支持或非 ECC GPU)"

# 16. 性能等级
echo ""
echo "【16】性能等级"
rocm-smi --showperflevel

echo ""
echo "=============================================="
echo " rocm-smi 使用指南 结束"
echo "=============================================="
```

#### 6.3 rocm-smi --showallinfo 完整字段解析

`rocm-smi --showallinfo` 是最全面的信息输出，以下为其字段分类：

```
┌─────────────────────────────────────────────────────────────────────┐
│          rocm-smi --showallinfo 字段分类                             │
│                                                                     │
│  一、GPU 标识信息                                                    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ GPU ID / GUID                GPU 序号和全局唯一标识符         │ │
│  │ Device ID / Revision ID      硬件设备 ID 和版本               │ │
│  │ Marketing Name               市场名称                          │ │
│  │ Vendor Name                  供应商名称                        │ │
│  │ PCIe BDF                     总线/设备/功能编号                │ │
│  │ Subsystem ID / Vendor ID     子系统标识                        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  二、频率与时钟                                                      │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Current SCLK/MCLK            当前核心/显存频率                 │ │
│  │ Min/Max SCLK/MCLK            最小/最大频率限制                 │ │
│  │ Supported SCLK/MCLK levels   支持的频率档位列表                │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  三、功耗与温度                                                      │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Current Socket Power          当前 GPU 插槽功率                │ │
│  │ Average Socket Power          平均功耗                          │ │
│  │ Power Limit / Power Cap       功耗限制/上限                    │ │
│  │ Temperature Edge              边缘温度                          │ │
│  │ Temperature Junction          结温 (热点)                       │ │
│  │ Temperature Memory            显存温度                          │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  四、内存                                                            │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ VRAM Total Memory             总显存容量                        │ │
│  │ VRAM Total Used Memory        已用显存                          │ │
│  │ Visible VRAM Total Memory     可见显存(通过 BAR 映射)           │ │
│  │ GTT Total Memory              GTT 内存总量                      │ │
│  │ GTT Used Memory               GTT 已用内存                      │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  五、利用率                                                          │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ GPU use (%)                   GPU 核心利用率                   │ │
│  │ GFX Activity (%)              GFX 引擎活动率                   │ │
│  │ MEM Activity (%)              内存活动率                        │ │
│  │ PCIe Bandwidth                当前 PCIe 带宽                    │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  六、固件信息                                                        │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ VBIOS Version                 显卡 BIOS 版本                   │ │
│  │ VCN FW Version                视频编解码固件版本                │ │
│  │ SDMA FW Version               SDMA 固件版本                    │ │
│  │ PSP FW Version                平台安全处理器版本                │ │
│  │ ME FW Version                 微引擎固件版本                    │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 6.4 rocm-smi Python 库编程

rocm-smi 提供了 Python 绑定 `rocm-smi-lib`，可以直接在 Python 脚本中查询 GPU 数据。

```python
#!/usr/bin/env python3
"""
rocm_smi_python.py - 使用 ROCm SMI Python 绑定进行 GPU 监控

需要安装：pip install rocm-smi-lib

数据来源：https://github.com/ROCm/rocm_smi_lib
"""

try:
    from rocm_smi import rocm_smi_lib as rsmi
except ImportError:
    print("请先安装 rocm-smi-lib: pip install rocm-smi-lib")
    import sys
    sys.exit(1)

import json
import time
import sys


def main():
    rsmi.initializeRsmi()

    device_count = rsmi.numMonitorDevices()
    print(f"检测到 {device_count} 个 GPU\n")

    devices = list(range(device_count))

    print("=" * 60)
    print("GPU 基本信息")
    print("=" * 60)

    for dev in devices:
        print(f"\n--- GPU {dev} ---")

        dev_id = rsmi.getDeviceId(dev)
        print(f"  Device ID: {dev_id}")

        name = rsmi.getDeviceName(dev)
        print(f"  Name: {name}")

        vbios = rsmi.getDeviceVbios(dev)
        print(f"  VBIOS: {vbios}")

        print(f"\n  温度:")
        try:
            temp = rsmi.getDeviceTemperature(dev, 0)  # 0 = edge
            print(f"    Edge: {temp / 1000:.1f} °C")
        except Exception as e:
            print(f"    Edge: N/A ({e})")

        try:
            temp_j = rsmi.getDeviceTemperature(dev, 1)  # 1 = junction
            print(f"    Junction: {temp_j / 1000:.1f} °C")
        except Exception:
            pass

        try:
            temp_m = rsmi.getDeviceTemperature(dev, 3)  # 3 = memory
            print(f"    Memory: {temp_m / 1000:.1f} °C")
        except Exception:
            pass

        print(f"\n  功耗:")
        try:
            power = rsmi.getDeviceAveragePower(dev)
            print(f"    Average Power: {power / 1e6:.1f} W")
        except Exception as e:
            print(f"    Average Power: N/A")

        try:
            power_cap = rsmi.getDevicePowerCap(dev)
            print(f"    Power Cap: {power_cap / 1e6:.1f} W")
        except Exception:
            pass

        print(f"\n  频率:")
        try:
            sclk = rsmi.getDeviceCurrentSclk(dev)
            print(f"    SCLK: {sclk / 1e6:.0f} MHz")
        except Exception:
            pass
        try:
            mclk = rsmi.getDeviceCurrentMclk(dev)
            print(f"    MCLK: {mclk / 1e6:.0f} MHz")
        except Exception:
            pass

        print(f"\n  内存:")
        try:
            vram_total = rsmi.getDeviceTotalVram(dev)
            vram_used = rsmi.getDeviceUsedVram(dev)
            print(f"    VRAM Total: {vram_total / (1024**3):.1f} GiB")
            print(f"    VRAM Used:  {vram_used / (1024**3):.1f} GiB")
        except Exception:
            pass

        print(f"\n  利用率:")
        try:
            gpu_use = rsmi.getDeviceGpuUse(dev)
            print(f"    GPU Utilization: {gpu_use}%")
        except Exception:
            pass

    print("\n" + "=" * 60)
    print("实时监控 (按 Ctrl+C 退出)")
    print("=" * 60)

    try:
        while True:
            for dev in devices:
                power = rsmi.getDeviceAveragePower(dev)
                gpu_use = rsmi.getDeviceGpuUse(dev)
                temp = rsmi.getDeviceTemperature(dev, 0)
                vram_used = rsmi.getDeviceUsedVram(dev)

                print(
                    f"GPU {dev} | "
                    f"利用率: {gpu_use:3}% | "
                    f"功耗: {power/1e6:6.1f}W | "
                    f"温度: {temp/1000:4.1f}°C | "
                    f"VRAM: {vram_used/(1024**3):.1f}GiB"
                )
            print("\033[F" * device_count, end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n" * (device_count + 1))
        print("监控已停止")

    rsmi.shutdownRsmi()


if __name__ == "__main__":
    main()
```

### 七、amd-smi —— 新一代 GPU 管理工具

ROCm 6.1+ 引入了 `amd-smi` 作为 `rocm-smi` 的现代化替代，提供更丰富的监控选项和更易读的输出格式。

```
┌─────────────────────────────────────────────────────────────────────┐
│              amd-smi 与 rocm-smi 对比                                │
│                                                                     │
│  数据来源：AMD 官方 amd-smi 文档                                    │
│  https://rocm.docs.amd.com/projects/amdsmi/en/latest/               │
│                                                                     │
│  ┌──────────────┬─────────────────────┬─────────────────────────┐   │
│  │ 特性         │ rocm-smi            │ amd-smi                  │   │
│  ├──────────────┼─────────────────────┼─────────────────────────┤   │
│  │ 输出格式     │ 固定文本            │ 文本/JSON/YAML/表格      │   │
│  │ 实时监控     │ --csv 轮询          │ monitor 子命令 (TUI)     │   │
│  │ GPU 拓扑     │ --showtopo          │ topology 子命令 (图形)   │   │
│  │ 进程信息     │ --showpids          │ process 子命令 (详细)    │   │
│  │ 事件监控     │ 不支持              │ event 子命令             │   │
│  │ 固件管理     │ --showfwinfo        │ firmware 子命令           │   │
│  │ 定时任务     │ --csv 间隔          │ set --schedule            │   │
│  │ 后端库       │ librocm_smi64.so    │ libamd_smi.so            │   │
│  └──────────────┴─────────────────────┴─────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

```bash
#!/bin/bash
# amd_smi_guide.sh - amd-smi 使用指南

echo "=============================================="
echo " amd-smi 使用指南（ROCm 6.1+）"
echo "=============================================="

# 1. 基本信息
echo ""
echo "【1】列出所有 GPU"
amd-smi list
# 输出示例:
# =========================================== AMD SMI ===========================================
# =========================================== GPU LIST ===========================================
#   GPU   DEVICE  BUS_ID   NAME                TEMP   POWER   USAGE   VRAM%   CLOCK
#     0    7448    0000:03:00.0  Radeon RX 7900 XTX  45.0   15.0W    0%     5%     100 MHz

# 2. 静态信息
echo ""
echo "【2】GPU 静态信息"
amd-smi static --gpu 0

# 3. 实时监控 (TUI 模式)
echo ""
echo "【3】实时监控TUI (按q退出)"
amd-smi monitor --gpu 0

# 4. 进程信息
echo ""
echo "【4】GPU 上运行的进程"
amd-smi process --gpu 0

# 5. 拓扑信息
echo ""
echo "【5】GPU 拓扑"
amd-smi topology

# 6. 事件日志
echo ""
echo "【6】GPU 事件日志"
amd-smi event --gpu 0 2>/dev/null || echo "  (事件监控功能需要 amdgpu 事件支持)"

# 7. JSON 格式输出
echo ""
echo "【7】JSON 格式输出"
amd-smi static --gpu 0 --json 2>/dev/null | python3 -m json.tool 2>/dev/null | head -40

echo ""
echo "=============================================="
echo " amd-smi 使用指南 结束"
echo "=============================================="
```

### 八、实践操作

#### 8.1 环境验证脚本（增强版）

```bash
#!/bin/bash
# validate_rocm_env.sh - ROCm 环境全面验证脚本
#
# 数据来源：基于 ROCm 官方安装验证指南
# https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/post-install.html
#

echo "=============================================="
echo " ROCm 环境全面验证脚本"
echo " 时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo " 主机: $(hostname)"
echo "=============================================="

PASS=0; FAIL=0; WARN=0

check_pass() { echo "  ✅ $1"; PASS=$((PASS+1)); }
check_fail() { echo "  ❌ $1"; FAIL=$((FAIL+1)); }
check_warn() { echo "  ⚠️  $1"; WARN=$((WARN+1)); }

# =============================================
# 1. 安装位置检查
# =============================================
echo ""
echo "--- 1. 安装位置检查 ---"
[ -d "/opt/rocm" ] && check_pass "/opt/rocm 目录存在" || check_fail "/opt/rocm 目录不存在"
[ -f "/opt/rocm/.info/version" ] && {
    ROCM_VER=$(cat /opt/rocm/.info/version 2>/dev/null)
    check_pass "/opt/rocm/.info/version 存在 (版本: $ROCM_VER)"
} || check_warn "/opt/rocm/.info/version 不存在"
[ -f "/opt/rocm/bin/hipcc" ] && check_pass "hipcc 存在" || check_fail "hipcc 不存在"
[ -f "/opt/rocm/bin/rocminfo" ] && check_pass "rocminfo 存在" || check_fail "rocminfo 不存在"
[ -f "/opt/rocm/bin/rocm-smi" ] && check_pass "rocm-smi 存在" || check_fail "rocm-smi 不存在"
[ -f "/opt/rocm/bin/amd-smi" ] && check_pass "amd-smi 存在" || check_warn "amd-smi 不存在 (ROCm 6.1+ 提供)"
[ -f "/opt/rocm/bin/clang-offload-bundler" ] && check_pass "ROCm LLVM 工具链存在" || check_warn "ROCm LLVM 工具链未安装"

# =============================================
# 2. 内核驱动检查
# =============================================
echo ""
echo "--- 2. 内核驱动检查 ---"

# 检查 amdgpu 驱动
if lsmod | grep -q amdgpu; then
    check_pass "amdgpu 驱动已加载"
    AMDGPU_VER=$(modinfo -F version amdgpu 2>/dev/null || echo "未知")
    echo "         版本: $AMDGPU_VER"
else
    check_fail "amdgpu 驱动未加载"
fi

# 检查 amdkfd 驱动
if lsmod | grep -q amdkfd; then
    check_pass "amdkfd 驱动已加载"
else
    check_warn "amdkfd 驱动未加载（可能使用 ROCm 内核驱动或 DKMS 模块）"
fi

# 检查 DKMS 状态
if command -v dkms &>/dev/null; then
    dkms status 2>/dev/null | grep -i amdgpu | while read line; do
        echo "         DKMS: $line"
    done
fi

# 检查 DRM 设备节点
[ -c /dev/dri/card0 ] && check_pass "/dev/dri/card0 存在" || check_warn "/dev/dri/card0 不存在"
[ -c /dev/dri/renderD128 ] && check_pass "/dev/dri/renderD128 存在" || check_warn "/dev/dri/renderD128 不存在"
[ -c /dev/kfd ] && check_pass "/dev/kfd 存在" || check_fail "/dev/kfd 不存在"

# 检查设备权限
echo ""
echo "--- 2.1 DRM 设备权限 ---"
for dev in /dev/dri/card* /dev/dri/renderD* /dev/kfd; do
    if [ -e "$dev" ]; then
        PERMS=$(stat -c "%a %G" "$dev" 2>/dev/null)
        echo "         $(basename $dev): $PERMS"
    fi
done

# =============================================
# 3. GPU 硬件检查（通过 rocminfo）
# =============================================
echo ""
echo "--- 3. GPU 硬件检查 ---"

if [ -x /opt/rocm/bin/rocminfo ]; then
    GPU_COUNT=$(/opt/rocm/bin/rocminfo 2>/dev/null | grep -c "Marketing Name" || echo 0)
    if [ "$GPU_COUNT" -gt 0 ]; then
        check_pass "检测到 $GPU_COUNT 个 GPU 设备"
        /opt/rocm/bin/rocminfo 2>/dev/null | grep "Marketing Name" | while read -r line; do
            echo "         $line"
        done
    else
        check_fail "未检测到 GPU（用户可能不在 render/video 组）"
    fi

    # CU 数量
    CU_COUNT=$(/opt/rocm/bin/rocminfo 2>/dev/null | grep "Compute Unit:" | head -1 | awk '{print $NF}')
    [ -n "$CU_COUNT" ] && check_pass "计算单元 (CU): $CU_COUNT" || check_warn "无法获取计算单元数"

    # Wavefront 大小
    WF_SIZE=$(/opt/rocm/bin/rocminfo 2>/dev/null | grep "Wavefront Size:" | head -1 | awk '{print $NF}')
    [ -n "$WF_SIZE" ] && echo "         Wavefront 大小: $WF_SIZE"

    # ISA 信息
    ISA_INFO=$(/opt/rocm/bin/rocminfo 2>/dev/null | grep "Name:" | grep "amdgcn" | head -1)
    [ -n "$ISA_INFO" ] && echo "         ISA: $ISA_INFO"
else
    check_warn "rocminfo 不可执行，跳过 GPU 硬件检查"
fi

# =============================================
# 4. GPU 温度、功耗、频率检查（通过 rocm-smi）
# =============================================
echo ""
echo "--- 4. GPU 运行状态 ---"

if [ -x /opt/rocm/bin/rocm-smi ]; then
    # 温度
    TEMP_OUTPUT=$(/opt/rocm/bin/rocm-smi --showtemp 2>/dev/null)
    if echo "$TEMP_OUTPUT" | grep -q "Temperature"; then
        check_pass "GPU 温度可读取"
        echo "$TEMP_OUTPUT" | grep "Temperature" | while read -r line; do
            echo "         $line"
        done
    else
        check_warn "无法读取 GPU 温度"
    fi

    # 功耗
    POWER_OUTPUT=$(/opt/rocm/bin/rocm-smi --showpower 2>/dev/null)
    if echo "$POWER_OUTPUT" | grep -q "Power"; then
        check_pass "GPU 功耗可读取"
        echo "$POWER_OUTPUT" | grep "Power" | while read -r line; do
            echo "         $line"
        done
    else
        check_warn "无法读取 GPU 功耗"
    fi

    # 显存
    VRAM_OUTPUT=$(/opt/rocm/bin/rocm-smi --showmeminfo vram 2>/dev/null)
    if echo "$VRAM_OUTPUT" | grep -q "VRAM"; then
        check_pass "GPU 显存信息可读取"
        echo "$VRAM_OUTPUT" | grep "VRAM" | while read -r line; do
            echo "         $line"
        done
    fi
else
    check_warn "rocm-smi 不可执行"
fi

# =============================================
# 5. 库文件检查
# =============================================
echo ""
echo "--- 5. 关键运行时库检查 ---"

LIBS=(
    "libamdhip64.so"
    "librocblas.so"
    "librocfft.so"
    "libMIOpen.so"
    "librccl.so"
    "libroctx64.so"
    "libhsa-runtime64.so"
    "libamd_comgr.so"
    "librocprofiler64.so"
    "libroctracer64.so"
)

for lib in "${LIBS[@]}"; do
    if [ -f "/opt/rocm/lib/$lib" ]; then
        check_pass "$lib 存在"
    else
        check_warn "$lib 不存在"
    fi
done

# =============================================
# 6. 环境变量检查
# =============================================
echo ""
echo "--- 6. 环境变量检查 ---"

echo "$PATH" | grep -q "/opt/rocm/bin" && \
    check_pass "PATH 包含 /opt/rocm/bin" || \
    check_warn "PATH 未配置 ROCm bin 路径"

echo "${LD_LIBRARY_PATH:-}" | grep -q "/opt/rocm/lib" && \
    check_pass "LD_LIBRARY_PATH 包含 /opt/rocm/lib" || \
    check_warn "LD_LIBRARY_PATH 未配置 ROCm lib 路径"

[ -n "${ROCM_PATH:-}" ] && check_pass "ROCM_PATH 已设置: $ROCM_PATH" || \
    check_warn "ROCM_PATH 环境变量未设置"

[ -n "${HIP_PATH:-}" ] && check_pass "HIP_PATH 已设置: $HIP_PATH" || \
    check_warn "HIP_PATH 环境变量未设置"

echo "${HIP_PLATFORM:-}" | grep -q "amd" && \
    check_pass "HIP_PLATFORM=amd" || \
    check_warn "HIP_PLATFORM 未设置为 amd"

# =============================================
# 7. 功能测试（HIP 编译运行）
# =============================================
echo ""
echo "--- 7. HIP 编译运行测试 ---"

cat > /tmp/rocm_validate_test.cpp << 'CPPEOF'
#include <hip/hip_runtime.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>

#define CHECK_HIP(cmd) \
    do { \
        hipError_t err = cmd; \
        if (err != hipSuccess) { \
            std::cerr << "HIP Error: " << hipGetErrorString(err) \
                      << " at " << __FILE__ << ":" << __LINE__ << std::endl; \
            std::exit(1); \
        } \
    } while(0)

__global__ void vector_add(const float *a, const float *b, float *c, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        c[idx] = a[idx] + b[idx];
    }
}

int main() {
    int device_count;
    CHECK_HIP(hipGetDeviceCount(&device_count));
    std::cout << "GPU count: " << device_count << std::endl;

    for (int i = 0; i < device_count; i++) {
        hipDeviceProp_t prop;
        CHECK_HIP(hipGetDeviceProperties(&prop, i));
        std::cout << "GPU " << i << ": " << prop.name
                  << " (" << prop.totalGlobalMem/(1024*1024*1024) << " GB VRAM)"
                  << " [" << prop.multiProcessorCount << " CUs]"
                  << " [Max Clock: " << prop.clockRate/1000 << " MHz]"
                  << " [Memory Clock: " << prop.memoryClockRate/1000 << " MHz]"
                  << " [Memory Bus: " << prop.memoryBusWidth << " bits]"
                  << std::endl;
    }

    const int N = 1 << 24;
    const size_t bytes = N * sizeof(float);

    float *h_a = new float[N];
    float *h_b = new float[N];
    float *h_c = new float[N];

    for (int i = 0; i < N; i++) {
        h_a[i] = (float)i;
        h_b[i] = (float)(N - i);
    }

    float *d_a, *d_b, *d_c;
    CHECK_HIP(hipMalloc(&d_a, bytes));
    CHECK_HIP(hipMalloc(&d_b, bytes));
    CHECK_HIP(hipMalloc(&d_c, bytes));

    CHECK_HIP(hipMemcpy(d_a, h_a, bytes, hipMemcpyHostToDevice));
    CHECK_HIP(hipMemcpy(d_b, h_b, bytes, hipMemcpyHostToDevice));

    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    vector_add<<<blocks, threads>>>(d_a, d_b, d_c, N);
    CHECK_HIP(hipGetLastError());

    CHECK_HIP(hipMemcpy(h_c, d_c, bytes, hipMemcpyDeviceToHost));

    CHECK_HIP(hipDeviceSynchronize());

    bool correct = true;
    for (int i = 0; i < N; i++) {
        if (fabsf(h_c[i] - (float)N) > 1e-3f) {
            correct = false;
            std::cerr << "Mismatch at " << i << ": " << h_c[i] << " != " << N << std::endl;
            break;
        }
    }

    if (correct) {
        std::cout << "✅ Vector add test PASSED (N=" << N << ")" << std::endl;
    } else {
        std::cerr << "❌ Vector add test FAILED" << std::endl;
    }

    CHECK_HIP(hipFree(d_a));
    CHECK_HIP(hipFree(d_b));
    CHECK_HIP(hipFree(d_c));

    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return correct ? 0 : 1;
}
CPPEOF

if [ -f /opt/rocm/bin/hipcc ]; then
    /opt/rocm/bin/hipcc -o /tmp/rocm_validate_test /tmp/rocm_validate_test.cpp 2>/tmp/rocm_compile_err.log
    if [ $? -eq 0 ]; then
        check_pass "HIP 编译成功"
        /tmp/rocm_validate_test 2>&1
        if [ $? -eq 0 ]; then
            check_pass "HIP 计算验证通过"
        else
            check_fail "HIP 计算验证失败"
        fi
    else
        check_fail "HIP 编译失败"
        echo "编译错误日志:"
        cat /tmp/rocm_compile_err.log | head -20
    fi
else
    check_fail "hipcc 不可用，无法进行功能测试"
fi

# =============================================
# 8. 带宽测试（可选）
# =============================================
echo ""
echo "--- 8. GPU 带宽测试 ---"

if [ -f /opt/rocm/bin/rocm-bandwidth-test ]; then
    echo "运行 rocm-bandwidth-test（Device-to-Device 带宽）"
    /opt/rocm/bin/rocm-bandwidth-test 2>&1 | head -20
    if [ $? -eq 0 ]; then
        check_pass "GPU 带宽测试完成"
    else
        check_warn "GPU 带宽测试遇到问题"
    fi
else
    check_warn "rocm-bandwidth-test 未安装（安装 rocm-bandwidth-test 包）"
fi

# =============================================
# 9. sysfs 信息汇总
# =============================================
echo ""
echo "--- 9. sysfs GPU 信息 ---"

# 获取第一个 AMD GPU
GPU_PATH=$(find /sys/class/drm -name "card*" -exec sh -c 'cat "$0/device/vendor" 2>/dev/null | grep -q "0x1002" && echo "$0"' {} \; | head -1)

if [ -n "$GPU_PATH" ]; then
    echo "         GPU sysfs 路径: $GPU_PATH"

    # GPU 型号
    DEVICE_ID=$(cat "$GPU_PATH/device/device" 2>/dev/null)
    SUBSYS_ID=$(cat "$GPU_PATH/device/subsystem_device" 2>/dev/null)
    echo "         Device ID: $DEVICE_ID, Subsystem: $SUBSYS_ID"

    # 显存信息
    if [ -f "$GPU_PATH/device/mem_info_vram_total" ]; then
        VRAM_TOTAL=$(cat "$GPU_PATH/device/mem_info_vram_total")
        echo "         VRAM Total: $((VRAM_TOTAL / (1024*1024))) MB"
    fi

    # Link Speed
    LINK_SPEED=$(cat "$GPU_PATH/device/current_link_speed" 2>/dev/null)
    LINK_WIDTH=$(cat "$GPU_PATH/device/current_link_width" 2>/dev/null)
    if [ -n "$LINK_SPEED" ] && [ -n "$LINK_WIDTH" ]; then
        echo "         PCIe Link: $LINK_SPEED x$LINK_WIDTH"
    fi

    # NUMA Node
    NUMA_NODE=$(cat "$GPU_PATH/device/numa_node" 2>/dev/null)
    [ -n "$NUMA_NODE" ] && echo "         NUMA Node: $NUMA_NODE"
else
    check_warn "未在 sysfs 中找到 AMD GPU"
fi

# =============================================
# 总结
# =============================================
echo ""
echo "=============================================="
echo " 验证总结"
echo "=============================================="
echo "  通过: $PASS"
echo "  失败: $FAIL"
echo "  警告: $WARN"
echo "=============================================="

if [ $FAIL -gt 0 ]; then
    echo ""
    echo "❌ 发现 $FAIL 个关键问题，请检查:"
    echo "   1. 是否已安装 ROCm 并重启系统？"
    echo "   2. 用户是否在 render 和 video 组中？(groups 命令检查)"
    echo "   3. /dev/kfd 和 /dev/dri/renderD* 权限是否正确？"
    echo "   4. amdgpu 和 amdkfd 驱动是否正常加载？"
    exit 1
elif [ $WARN -gt 0 ]; then
    echo ""
    echo "⚠️  发现 $WARN 个警告，功能可能受限"
    echo "   建议检查上述警告项"
    exit 0
else
    echo ""
    echo "✅ ROCm 环境完全正常！所有检查通过。"
fi
```

#### 8.2 Docker 容器中 ROCm 透传配置

在容器化环境中使用 ROCm 需要将必要的设备节点和库映射到容器内。

```bash
#!/bin/bash
# rocm_docker_setup.sh - Docker 中 ROCm GPU 透传配置

echo "=============================================="
echo " Docker ROCm GPU 透传配置"
echo "=============================================="

# 1. 安装 Docker (如未安装)
echo ""
echo "【1】检查 Docker 安装"
docker --version 2>/dev/null && echo "  ✅ Docker 已安装" || {
    echo "  ⚠️  Docker 未安装，请先安装 Docker"
}

# 2. 安装 nvidia-container-toolkit 等效 - 对于 ROCm，直接使用设备映射即可
echo ""
echo "【2】ROCm 容器透传原理"
echo "  ROCm 容器化不使用特殊运行时，直接映射设备节点即可:"
echo "  ┌──────────────────────────────────────────────────┐"
echo "  │ 需要映射的设备:                                  │"
echo "  │   --device=/dev/kfd                              │"
echo "  │   --device=/dev/dri                              │"
echo "  │                                                  │"
echo "  │ 需要映射的组权限:                                │"
echo "  │   --group-add video                              │"
echo "  │   --group-add render                             │"
echo "  │                                                  │"
echo "  │ 可选(性能相关):                                  │"
echo "  │   --security-opt seccomp=unconfined              │"
echo "  │   --ipc=host                                     │"
echo "  │   --cap-add SYS_PTRACE                           │"
echo "  │   -v /opt/rocm:/opt/rocm                         │"
echo "  └──────────────────────────────────────────────────┘"
echo ""
echo "数据来源: https://rocm.docs.amd.com/en/latest/how-to/docker.html"

# 3. 拉取 ROCm Docker 镜像
echo ""
echo "【3】拉取 ROCm 官方 Docker 镜像"
echo "  AMD 官方提供预构建的 ROCm Docker 镜像:"
echo ""
echo "  Ubuntu 24.04 + ROCm 6.2 (完整版):"
echo "    docker pull rocm/rocm-terminal:latest"
echo ""
echo "  Ubuntu 22.04 + ROCm 6.2 (精简版):"
echo "    docker pull rocm/dev-ubuntu-22.04:6.2-complete"
echo ""
echo "  仅运行时 (Runtime only):"
echo "    docker pull rocm/rocm-terminal:latest"

# 4. 运行 ROCm 容器
echo ""
echo "【4】启动 ROCm 容器的完整命令"
cat << 'DOCKERRUN'
# 基本运行命令
docker run -it \
    --name rocm-test \
    --device=/dev/kfd \
    --device=/dev/dri \
    --group-add video \
    --group-add render \
    --security-opt seccomp=unconfined \
    --ipc=host \
    --cap-add SYS_PTRACE \
    -v /opt/rocm:/opt/rocm:ro \
    -e ROCM_PATH=/opt/rocm \
    rocm/rocm-terminal:latest \
    /bin/bash

# 容器内验证
# rocminfo
# rocm-smi
# hipcc --version
DOCKERRUN

# 5. Docker Compose 配置
echo ""
echo "【5】Docker Compose 配置示例"
cat << 'COMPOSEEOF'
# docker-compose.yml
version: '3.8'

services:
  rocm-dev:
    image: rocm/rocm-terminal:latest
    container_name: rocm-dev-container
    devices:
      - /dev/kfd
      - /dev/dri
    group_add:
      - video
      - render
    security_opt:
      - seccomp:unconfined
    ipc: host
    cap_add:
      - SYS_PTRACE
    volumes:
      - /opt/rocm:/opt/rocm:ro
      - ./workspace:/workspace
    environment:
      - ROCM_PATH=/opt/rocm
      - HSA_OVERRIDE_GFX_VERSION=11.0.0
    working_dir: /workspace
    command: /bin/bash

COMPOSEEOF

# 6. Dockerfile 示例
echo ""
echo "【6】自定义 ROCm Dockerfile"
cat << 'DOCKERFILEEOF'
# Dockerfile - 自定义 ROCm 开发环境
FROM rocm/dev-ubuntu-22.04:6.2-complete

ENV DEBIAN_FRONTEND=noninteractive
ENV ROCM_PATH=/opt/rocm
ENV PATH=$ROCM_PATH/bin:$PATH
ENV LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    git \
    cmake \
    build-essential \
    vim \
    htop \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    torch \
    numpy \
    pytest

WORKDIR /workspace

CMD ["/bin/bash"]
DOCKERFILEEOF

echo ""
echo "=============================================="
echo " Docker ROCm 配置指南 结束"
echo "=============================================="
```

#### 8.3 ROCm 设备拓扑与 NUMA 分析

```bash
#!/bin/bash
# rocm_topo_numa.sh - GPU 拓扑与 NUMA 绑定分析

echo "=============================================="
echo " GPU 拓扑与 NUMA 分析"
echo "=============================================="

# 1. PCIe 拓扑
echo ""
echo "【1】PCIe 设备拓扑"
lspci -tvvv 2>/dev/null | grep -A5 -i amd || \
    lspci | grep -iE "VGA|3D|Display" | grep -i amd

# 2. GPU PCIe 详细信息
echo ""
echo "【2】GPU PCIe 链路详情"
for dev in /sys/bus/pci/devices/*/; do
    VENDOR=$(cat "$dev/vendor" 2>/dev/null)
    if [ "$VENDOR" = "0x1002" ]; then
        DEV_ID=$(cat "$dev/device" 2>/dev/null)
        LINK_SPEED=$(cat "$dev/current_link_speed" 2>/dev/null)
        LINK_WIDTH=$(cat "$dev/current_link_width" 2>/dev/null)
        NUMA=$(cat "$dev/numa_node" 2>/dev/null)
        BDF=$(basename "$dev")
        echo "  GPU: $BDF  Device: $DEV_ID  PCIe: ${LINK_SPEED:-N/A} x${LINK_WIDTH:-N/A}  NUMA: ${NUMA:-N/A}"
    fi
done

# 3. CPU NUMA 拓扑
echo ""
echo "【3】CPU NUMA 拓扑"
numactl --hardware 2>/dev/null || echo "  numactl 未安装"

# 4. KFD 拓扑信息
echo ""
echo "【4】KFD 拓扑节点 (GPU NUMA 关系)"
if [ -d /sys/class/kfd/kfd/topology/nodes/ ]; then
    for node in /sys/class/kfd/kfd/topology/nodes/*/; do
        NODE_ID=$(basename "$node")
        NAME=$(cat "$node/name" 2>/dev/null)
        TYPE=$(cat "$node/properties" 2>/dev/null | grep "cpu_core_id_base\|gpu_id\|simd_count")
        echo "  Node $NODE_ID: $NAME"
        echo "    $TYPE"
    done
else
    echo "  KFD 拓扑不可用 (amdkfd 驱动可能未加载)"
fi

# 5. NUMA 感知的 HIP 程序示例
cat << 'CPPEOF' > /tmp/hip_numa_test.cpp

#include <hip/hip_runtime.h>
#include <iostream>
#include <sched.h>
#include <numa.h>

int main() {
    int count;
    hipGetDeviceCount(&count);
    std::cout << "GPU count: " << count << std::endl;

    for (int i = 0; i < count; i++) {
        hipDeviceProp_t prop;
        hipGetDeviceProperties(&prop, i);

        hipDeviceAttribute_t numa_attr =
            (hipDeviceAttribute_t)0x8007;  // hipDeviceAttributeNumaNode
        int numa_node = -1;
        hipDeviceGetAttribute(&numa_node, numa_attr, i);

        std::cout << "GPU " << i << ": " << prop.name
                  << " | NUMA Node: " << numa_node << std::endl;

        int can_access_host = 0;
        hipDeviceGetAttribute(&can_access_host,
            hipDeviceAttributeCanAccessHostRegisteredMem, i);
        std::cout << "  Can Access Host Registered Memory: "
                  << (can_access_host ? "Yes" : "No") << std::endl;
    }

    std::cout << "\nCPU NUMA info:\n";
    if (numa_available() >= 0) {
        int max_node = numa_max_node();
        std::cout << "  Max NUMA node: " << max_node << std::endl;
        for (int n = 0; n <= max_node; n++) {
            long long free_size;
            long long node_size = numa_node_size64(n, &free_size);
            std::cout << "  Node " << n << ": "
                      << node_size / (1024*1024) << " MB total, "
                      << free_size / (1024*1024) << " MB free" << std::endl;
        }
    }

    return 0;
}
CPPEOF

echo ""
echo "【5】编译 NUMA 感知测试程序"
/opt/rocm/bin/hipcc -o /tmp/hip_numa_test /tmp/hip_numa_test.cpp -lnuma 2>/dev/null && {
    echo "  ✅ 编译成功"
    echo "  运行: /tmp/hip_numa_test"
} || {
    echo "  ⚠️  编译失败 (可能需要安装 libnuma-dev)"
}

echo ""
echo "=============================================="
echo " GPU 拓扑与 NUMA 分析 结束"
echo "=============================================="
```

### 九、ROCm 环境变量完整参考

> 数据来源：ROCm 环境变量文档
> https://rocm.docs.amd.com/en/latest/conceptual/environment-variables.html

```
┌─────────────────────────────────────────────────────────────────────┐
│            ROCm 关键环境变量完整参考                                 │
│                                                                     │
│  一、路径类环境变量                                                  │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ ROCM_PATH        ROCm 安装根路径                       /opt/rocm│ │
│  │ HIP_PATH         HIP 安装路径                          /opt/rocm│ │
│  │ HIP_PLATFORM     HIP 平台选择                    amd / nvidia   │ │
│  │ DEVICE_LIB_PATH  设备库路径                     $ROCM_PATH/amdgcn│ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  二、运行时控制变量                                                  │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ HSA_ENABLE_SDMA        启用 SDMA 引擎             0/1 (默认1)  │ │
│  │ HSA_ENABLE_INTERRUPT   启用 GPU 中断              0/1 (默认1)  │ │
│  │ GPU_MAX_HW_QUEUES      最大硬件队列数              1-128       │ │
│  │ AMD_DEBUG              调试模式开关             位掩码          │ │
│  │ ROCR_VISIBLE_DEVICES   可见 GPU 列表             "0,1,2" 格式  │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  三、性能/调试变量                                                   │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ HSA_OVERRIDE_GFX_VERSION   覆盖 GPU 目标架构  "11.0.0"         │ │
│  │ HIP_VISIBLE_DEVICES        HIP 可见设备      "0,1" 格式      │ │
│  │ AMD_LOG_LEVEL              日志级别           0-3 (0=静默)    │ │
│  │ AMD_OCL_WAIT_COMMAND       等待命令完成      0/1              │ │
│  │ GPU_FORCE_64BIT_PTR       强制 64 位指针    0/1              │ │
│  │ ROCPROFILER_LOG            Profiler 日志     1               │ │
│  │ HSA_TOOLS_LIB              Tools 库路径      用于 rocprof     │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  四、MIOpen 专用变量                                                 │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ MIOPEN_FIND_MODE          查找模式           Normal/Fast/Hybrid│ │
│  │ MIOPEN_DEBUG_FIND_ONLY_SOLVER 调试求解器    1                  │ │
│  │ MIOPEN_LOG_LEVEL          日志级别           0-3              │ │
│  │ MIOPEN_CONVOLUTION_PREC_SEARCH 精度搜索     1                 │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 十、常见安装问题排查指南

> 数据来源：ROCm 故障排除文档
> https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/troubleshoot.html

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| hipGetDeviceCount 返回 0 | 用户不在 render/video 组 | `sudo usermod -aG render,video $USER`，然后重新登录 |
| rocminfo 无法运行 | PATH 未配置 | `export PATH=/opt/rocm/bin:$PATH` |
| /dev/kfd 不存在 | amdkfd 驱动未加载 | `sudo modprobe amdkfd` |
| 库未找到 | LD_LIBRARY_PATH 未配置 | `export LD_LIBRARY_PATH=/opt/rocm/lib:$LD_LIBRARY_PATH` |
| Permission denied | /dev/dri/renderD* 权限 | 添加 udev 规则或手动设置权限 |
| 安装失败(依赖) | 系统版本不匹配 | 检查 ROCm 支持的 OS 版本 |
| ROCm 检测不到 GPU | GPU 固件版本过旧 | 更新 linux-firmware |
| amdgpu 驱动加载失败 | 内核版本不匹配 | 安装匹配的 dkms 驱动或升级内核 |
| "Composable Kernel" 编译失败 | 磁盘空间不足 | ROCm 6.x 需要约 30GB 以上 `/opt` 空间 |
| hipcc 编译失败 | LLVM 工具链未完整安装 | 安装 rocm-llvm 包 |
| GPU 内存分配失败 | VRAM 已耗尽或 GPU 处于错误状态 | 重启或重置 GPU (`sudo cat /sys/kernel/debug/dri/N/amdgpu_gpu_recover`) |
| 内核模块签名验证失败 | UEFI Secure Boot 启用 | 导入 MOK 密钥或禁用 Secure Boot |

#### 10.1 案例：调试 "rocminfo 无 GPU" 问题

```
┌─────────────────────────────────────────────────────────────────────┐
│     案例分析：rocminfo 输出中没有 GPU                                │
│                                                                     │
│  数据来源：freedesktop.org amdgpu issue tracker                     │
│  https://gitlab.freedesktop.org/drm/amd/-/issues                    │
│                                                                     │
│  问题描述:                                                          │
│    Ubuntu 24.04 上正确安装了 ROCm 6.2，但 rocminfo 输出中只有       │
│    CPU Agent，没有 GPU Agent。                                      │
│                                                                     │
│  诊断步骤:                                                          │
│    1. groups -> 确认用户在 render/video 组中                        │
│       ❌ 发现 $USER 不在 render 组                                   │
│                                                                     │
│    2. ls -la /dev/kfd -> 检查 KFD 设备                              │
│       ✅ /dev/kfd 存在，权限 crw-rw---- 1 root render                │
│                                                                     │
│    3. ls -la /dev/dri/renderD* -> 检查 render 节点                   │
│       ❌ 权限为 crw-rw---- 1 root video，render 组无权限              │
│                                                                     │
│    4. dmesg | grep amdgpu -> 检查驱动加载                           │
│       ✅ amdgpu 驱动正常初始化                                       │
│                                                                     │
│    5. dmesg | grep kfd -> 检查 KFD 初始化                           │
│       ✅ "kfd: amdgpu: Allocated 3969056 bytes on gart"              │
│                                                                     │
│  根本原因:                                                          │
│    用户不在 render 组，且 /dev/dri/renderD128 的组所有权为          │
│    video 而非 render。                                              │
│                                                                     │
│  解决方案:                                                          │
│    sudo usermod -aG render,video $USER                              │
│    sudo tee /etc/udev/rules.d/70-amdgpu.rules << EOF                 │
│    KERNEL=="kfd", GROUP="render", MODE="0660"                       │
│    KERNEL=="renderD*", GROUP="render", MODE="0660"                  │
│    KERNEL=="card*", GROUP="video", MODE="0660"                      │
│    EOF                                                              │
│    sudo udevadm control --reload-rules                              │
│    sudo udevadm trigger                                             │
│    然后重新登录或重启。                                              │
│                                                                     │
│  验证:                                                              │
│    groups -> 应包含 render 和 video                                  │
│    rocminfo -> 应显示 GPU Agent                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 10.2 案例：DKMS 驱动编译失败

```
┌─────────────────────────────────────────────────────────────────────┐
│     案例分析：DKMS 内核驱动编译失败                                  │
│                                                                     │
│  问题描述:                                                          │
│    安装 amdgpu-dkms 时遇到编译错误，内核模块无法加载。              │
│                                                                     │
│  诊断:                                                              │
│    1. dkms status -> 查看模块状态                                    │
│       显示 amdgpu/6.2.x: added (但未 built)                         │
│                                                                     │
│    2. sudo dkms build amdgpu/6.2.x -> 尝试手动构建                   │
│       错误: kernel-devel 不匹配                                      │
│                                                                     │
│    3. uname -r 与已安装的 kernel-devel 版本对比                      │
│       ❌ 不匹配：运行内核 6.8.0-45, kernel-devel 6.8.0-40            │
│                                                                     │
│  解决方案:                                                          │
│    sudo apt update && sudo apt upgrade -y  # 更新到一致的内核版本    │
│    sudo apt install linux-headers-$(uname -r)  # 安装匹配的头文件    │
│    sudo dkms remove amdgpu/6.2.x --all                              │
│    sudo dkms install amdgpu/6.2.x                                   │
│    sudo modprobe amdgpu                                             │
│                                                                     │
│  教训:                                                              │
│    安装 DKMS 驱动前必须确保 kernel、kernel-devel/headers 版本一致   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 十一、ROCm 版本查看与切换

```bash
#!/bin/bash
# rocm_version_management.sh - ROCm 版本管理

echo "=============================================="
echo " ROCm 版本管理"
echo "=============================================="

# 1. 查看当前 ROCm 版本
echo ""
echo "【1】当前安装的 ROCm 版本"
if [ -f /opt/rocm/.info/version ]; then
    echo "  /opt/rocm/.info/version: $(cat /opt/rocm/.info/version)"
fi
if [ -f /opt/rocm/share/doc/rocm-version ]; then
    echo "  rocm-version 文件: $(cat /opt/rocm/share/doc/rocm-version)"
fi

# 2. 查看各组件版本
echo ""
echo "【2】各组件版本"
echo "  hipcc:"
/opt/rocm/bin/hipcc --version 2>/dev/null | head -1

echo "  ROCm LLVM (clang):"
/opt/rocm/llvm/bin/clang --version 2>/dev/null | head -1

echo "  rocminfo (HSA Runtime):"
/opt/rocm/bin/rocminfo 2>/dev/null | grep -E "Runtime Version|ROCk module" | head -3

# 3. 多版本安装架构
echo ""
echo "【3】多版本 ROCm 并存方案"

cat << 'MULTIARCH'
  推荐多版本的目录结构:

  /opt/rocm-6.0.2/       (ROCm 6.0.2)
  /opt/rocm-6.1.3/       (ROCm 6.1.3)
  /opt/rocm-6.2.4/       (ROCm 6.2.4 - 当前活跃)
  /opt/rocm -> /opt/rocm-6.2.4/   (符号链接指向当前版本)

  切换命令:
    sudo rm -f /opt/rocm
    sudo ln -sf /opt/rocm-6.0.2 /opt/rocm
    export ROCM_PATH=/opt/rocm

  数据来源：ROCm 安装文档多版本管理章节
  https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-multi-version.html
MULTIARCH

# 4. 版本切换脚本
echo ""
echo "【4】ROCm 版本切换脚本"
cat << 'SWITCHSCRIPT' > /tmp/switch_rocm.sh
#!/bin/bash
# switch_rocm.sh - ROCm 版本切换工具

VERSION=${1:-}
if [ -z "$VERSION" ]; then
    echo "用法: $0 <rocm_version>"
    echo "例如: $0 6.2.4"
    echo ""
    echo "已安装的 ROCm 版本:"
    ls -d /opt/rocm-* 2>/dev/null | sed 's|/opt/rocm-||' | sed 's|^|  |'
    exit 1
fi

TARGET="/opt/rocm-${VERSION}"
if [ ! -d "$TARGET" ]; then
    echo "错误: $TARGET 不存在"
    echo "请确认版本号并检查 /opt/ 目录"
    exit 1
fi

echo "切换到 ROCm $VERSION..."
sudo rm -f /opt/rocm
sudo ln -sf "$TARGET" /opt/rocm

echo "当前指向: $(readlink -f /opt/rocm)"
echo ""
echo "请在 shell 中执行:"
echo "  export ROCM_PATH=/opt/rocm"
echo "  export PATH=\$ROCM_PATH/bin:\$PATH"
echo "  export LD_LIBRARY_PATH=\$ROCM_PATH/lib:\$LD_LIBRARY_PATH"
echo ""
echo "验证: /opt/rocm/bin/hipcc --version"
SWITCHSCRIPT

chmod +x /tmp/switch_rocm.sh
echo "  脚本已生成: /tmp/switch_rocm.sh"

# 5. dpkg/rpm 包查询
echo ""
echo "【5】已安装的 ROCm 包列表"
if command -v dpkg &>/dev/null; then
    dpkg -l | grep -i rocm | awk '{print $2, $3}' | column -t
elif command -v rpm &>/dev/null; then
    rpm -qa | grep -i rocm
fi
```

### 十二、ROCm 带宽测试工具

`rocm-bandwidth-test` 用于测量 GPU 内部和 GPU 之间的数据传输带宽。

```bash
#!/bin/bash
# bandwidth_test_guide.sh - ROCm 带宽测试指南

echo "=============================================="
echo " ROCm 带宽测试指南"
echo "=============================================="

# 安装
echo "【安装】rocm-bandwidth-test"
echo "  sudo apt install rocm-bandwidth-test"
echo ""

# 测试类型
echo "【测试类型】"
echo "  1. Device-to-Device (D2D):     GPU 内部显存拷贝"
echo "  2. Host-to-Device (H2D):       CPU→GPU 拷贝"
echo "  3. Device-to-Host (D2H):       GPU→CPU 拷贝"
echo "  4. Bidirectional:              双向同时拷贝"
echo ""

# 运行示例
echo "【运行示例】"
echo "  # D2D 单向拷贝测试"
echo "  rocm-bandwidth-test"
echo ""
echo "  # 指定设备"
echo "  rocm-bandwidth-test --device 0"
echo ""
echo "  # 双向测试"
echo "  rocm-bandwidth-test --bidirectional"
echo ""
echo "  # 矩阵模式 (多 GPU)"
echo "  rocm-bandwidth-test --matrix"

# 期望带宽参考值
cat << 'BWREF'
【参考带宽值】（基于 PCIe 4.0 x16，RDNA3 GPU）

  传输方向        期望带宽 (单向)
  ─────────────────────────────────
  D2D (VRAM内)    ~800-1200 GB/s   (取决于 GPU 显存带宽)
  H2D (可固定)    ~25-28 GB/s      (PCIe 4.0 x16 理论 31.5 GB/s)
  D2H (可固定)    ~25-28 GB/s
  P2P (GPU间)     ~25-50 GB/s      (取决于 XGMI/PCIe 互联)

  数据来源：rocm-bandwidth-test 输出，AMD 官方性能文档
BWREF
```

### 十三、sysfs/debugfs 底层调试接口

除了 rocm-smi 工具外，可以直接通过 sysfs 和 debugfs 获取 GPU 底层信息。

```bash
#!/bin/bash
# low_level_gpu_info.sh - 通过 sysfs/debugfs 获取 GPU 底层信息

echo "=============================================="
echo " GPU sysfs/debugfs 底层信息"
echo " 数据来源：Linux 内核 amdgpu 驱动源码"
echo " drivers/gpu/drm/amd/pm/amdgpu_pm.c"
echo "=============================================="

# 找到 AMD GPU 的 sysfs 路径
for CARD in /sys/class/drm/card*; do
    VENDOR=$(cat "$CARD/device/vendor" 2>/dev/null)
    if [ "$VENDOR" = "0x1002" ]; then
        echo ""
        echo "=== GPU: $(basename $CARD) ==="
        DEV_PATH="$CARD/device"
        HW_PATH="$DEV_PATH/hwmon/hwmon*"

        # 设备 ID
        echo "Device ID: $(cat $DEV_PATH/device 2>/dev/null)"
        echo "Revision: $(cat $DEV_PATH/revision 2>/dev/null)"

        # 电源管理 (DPM)
        echo ""
        echo "--- 频率档位 (DPM) ---"
        for f in $DEV_PATH/pp_dpm_sclk $DEV_PATH/pp_dpm_mclk $DEV_PATH/pp_dpm_fclk; do
            if [ -f "$f" ]; then
                echo "$(basename $f):"
                cat "$f" 2>/dev/null | head -10
            fi
        done

        # OD (OverDrive) 参数
        if [ -f "$DEV_PATH/pp_od_clk_voltage" ]; then
            echo ""
            echo "--- OverDrive 参数 ---"
            cat "$DEV_PATH/pp_od_clk_voltage" 2>/dev/null | head -20
        fi

        # 电源状态
        if [ -f "$DEV_PATH/power_state" ]; then
            echo ""
            echo "--- 电源状态 ---"
            cat "$DEV_PATH/power_state" 2>/dev/null
        fi

        # 显存信息
        echo ""
        echo "--- 内存信息 ---"
        for f in $DEV_PATH/mem_info_vram_total $DEV_PATH/mem_info_vis_vram_total \
                 $DEV_PATH/mem_info_vram_used $DEV_PATH/mem_info_gtt_total \
                 $DEV_PATH/mem_info_gtt_used $DEV_PATH/mem_info_vis_vram_used; do
            if [ -f "$f" ]; then
                VAL=$(cat "$f" 2>/dev/null)
                case "$(basename $f)" in
                    mem_info_vram_total) echo "VRAM Total: $((VAL / 1048576)) MB";;
                    mem_info_vis_vram_total) echo "Visible VRAM Total: $((VAL / 1048576)) MB";;
                    mem_info_vram_used) echo "VRAM Used: $((VAL / 1048576)) MB";;
                    mem_info_vis_vram_used) echo "Visible VRAM Used: $((VAL / 1048576)) MB";;
                    mem_info_gtt_total) echo "GTT Total: $((VAL / 1048576)) MB";;
                    mem_info_gtt_used) echo "GTT Used: $((VAL / 1048576)) MB";;
                esac
            fi
        done

        # HWMon 温度/功耗/频率
        echo ""
        echo "--- 硬件监控 (hwmon) ---"
        for hwmon in $DEV_PATH/hwmon/hwmon*; do
            if [ -d "$hwmon" ]; then
                echo "hwmon: $(basename $hwmon)"

                # 温度
                for f in temp1_input temp2_input temp3_input; do
                    [ -f "$hwmon/$f" ] && echo "  $(echo $f | sed 's/_input//'): $(( $(cat $hwmon/$f) / 1000 ))°C"
                done

                # 功耗
                [ -f "$hwmon/power1_average" ] && echo "  Power Avg: $(( $(cat $hwmon/power1_average) / 1000000 )) W"
                [ -f "$hwmon/power1_cap" ] && echo "  Power Cap: $(( $(cat $hwmon/power1_cap) / 1000000 )) W"

                # 频率
                [ -f "$hwmon/freq1_input" ] && echo "  SCLK: $(( $(cat $hwmon/freq1_input) / 1000000 )) MHz"
                [ -f "$hwmon/freq2_input" ] && echo "  MCLK: $(( $(cat $hwmon/freq2_input) / 1000000 )) MHz"

                # 风扇
                [ -f "$hwmon/fan1_input" ] && echo "  Fan: $(cat $hwmon/fan1_input) RPM"
                [ -f "$hwmon/pwm1" ] && echo "  PWM: $(cat $hwmon/pwm1)"
            fi
        done

        # 电源能力
        echo ""
        echo "--- 电源能力 ---"
        [ -f "$DEV_PATH/power_dpm_force_performance_level" ] && \
            echo "Performance Level: $(cat $DEV_PATH/power_dpm_force_performance_level)"
        [ -f "$DEV_PATH/pp_power_profile_mode" ] && \
            echo "Power Profile: $(cat $DEV_PATH/pp_power_profile_mode | head -5)"

        break
    fi
done

# debugfs 信息（需要 root 权限）
echo ""
echo "--- debugfs 信息 (需要 root) ---"
sudo sh -c '
if mount | grep -q debugfs; then
    DEBUGFS=$(mount | grep debugfs | awk "{print \$3}" | head -1)
    DRM_DEBUG="$DEBUGFS/dri"
    if [ -d "$DRM_DEBUG" ]; then
        echo "可用的 debugfs 节点:"
        ls "$DRM_DEBUG" 2>/dev/null | grep amdgpu | head -10
    fi
else
    echo "  debugfs 未挂载，请运行: sudo mount -t debugfs none /sys/kernel/debug"
fi
' 2>/dev/null || echo "  (需要 root 权限查看 debugfs)"
```

### 十四、ROCm GPU 固件管理

```bash
#!/bin/bash
# gpu_firmware_check.sh - GPU 固件检查脚本

echo "=============================================="
echo " AMD GPU 固件检查"
echo "=============================================="

# 固件加载日志
echo ""
echo "【1】固件加载日志 (dmesg)"
dmesg 2>/dev/null | grep -i "amdgpu.*firmware\|amdgpu.*ucode\|amdgpu.*fw" | tail -20 || \
    sudo dmesg | grep -i "amdgpu.*firmware\|amdgpu.*ucode\|amdgpu.*fw" | tail -20

# 已加载的固件
echo ""
echo "【2】当前加载的固件"
ls -la /lib/firmware/amdgpu/ 2>/dev/null | head -20 || echo "  固件目录不存在"

# 各代 GPU 所需核心固件
cat << 'FWINFO'
【关键固件文件说明】

  固件前缀        用途                      涉及的 IP 块
  ──────────────────────────────────────────────────────
  gc_*            图形核心 (Graphics Core)    Shader/CU 控制
  sdma_*          SDMA 引擎                  异步 DMA
  psp_*           平台安全处理器               启动/安全
  smu_*           系统管理单元                 电源/频率
  vcn_*           视频编解码引擎               VCN 编解码
  mes_*           微引擎调度器                 用户态队列调度
  dcn_*           显示控制器 (仅消费级 GPU)    Display/DCN

  数据来源：amdgpu 驱动源码
  drivers/gpu/drm/amd/amdgpu/amdgpu_ucode.c
FWINFO

# 固件版本查询
echo ""
echo "【3】固件版本查询"
for gpu_card in /sys/class/drm/card*/device; do
    VENDOR=$(cat "$gpu_card/vendor" 2>/dev/null)
    if [ "$VENDOR" = "0x1002" ]; then
        echo "GPU: $(cat $gpu_card/device 2>/dev/null)"

        sudo cat /sys/kernel/debug/dri/*/amdgpu_firmware_info 2>/dev/null | head -30 || \
            echo "  (需要 root 权限查看 debugfs 固件信息)"
        break
    fi
done
```

### 十五、自动化环境健康检查脚本（生产环境）

```bash
#!/bin/bash
# rocm_health_check.sh - 生产环境 ROCm 健康检查
# 适用于数据中心定期巡检，可集成到监控系统

set -o pipefail

HOSTNAME=$(hostname)
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
REPORT_FILE="/tmp/rocm_health_${HOSTNAME}_$(date +%Y%m%d_%H%M%S).log"

exec > >(tee "$REPORT_FILE") 2>&1

echo "=============================================="
echo " ROCm 环境健康检查报告"
echo " 主机: $HOSTNAME"
echo " 时间: $TIMESTAMP"
echo "=============================================="

HEALTHY=true

# 1. 驱动状态
echo ""
echo "=== 1. 驱动状态 ==="
for mod in amdgpu amdkfd; do
    if lsmod | grep -q "^$mod "; then
        echo "  ✅ $mod 已加载"
    else
        echo "  ❌ $mod 未加载"
        HEALTHY=false
    fi
done

# 2. 设备节点
echo ""
echo "=== 2. 设备节点 ==="
for dev in /dev/kfd /dev/dri/renderD128; do
    if [ -c "$dev" ]; then
        echo "  ✅ $dev 存在"
    else
        echo "  ❌ $dev 不存在"
        HEALTHY=false
    fi
done

# 3. GPU 可见性
echo ""
echo "=== 3. GPU 检测 ==="
GPU_COUNT=$(/opt/rocm/bin/rocminfo 2>/dev/null | grep -c "Marketing Name" || echo 0)
if [ "$GPU_COUNT" -gt 0 ]; then
    echo "  ✅ 检测到 $GPU_COUNT 个 GPU"
    /opt/rocm/bin/rocminfo 2>/dev/null | grep "Marketing Name"
else
    echo "  ❌ 未检测到 GPU"
    HEALTHY=false
fi

# 4. 温度检查
echo ""
echo "=== 4. 温度检查 ==="
if [ -x /opt/rocm/bin/rocm-smi ]; then
    TEMP_OUTPUT=$(/opt/rocm/bin/rocm-smi --showtemp 2>/dev/null)
    TEMP_MAX=$(echo "$TEMP_OUTPUT" | grep -oP '\d+\.\d+ C' | sed 's/ C//' | sort -rn | head -1)
    if [ -n "$TEMP_MAX" ]; then
        TEMP_INT=${TEMP_MAX%.*}
        echo "  最高温度: $TEMP_MAX °C"
        if [ "$TEMP_INT" -gt 85 ]; then
            echo "  ⚠️  温度超过 85°C，需要关注"
        else
            echo "  ✅ 温度正常"
        fi
    fi
fi

# 5. 功耗检查
echo ""
echo "=== 5. 功耗检查 ==="
if [ -x /opt/rocm/bin/rocm-smi ]; then
    /opt/rocm/bin/rocm-smi --showpower 2>/dev/null | grep -E "Power|GPU"
fi

# 6. 显存检查
echo ""
echo "=== 6. 显存使用 ==="
if [ -x /opt/rocm/bin/rocm-smi ]; then
    /opt/rocm/bin/rocm-smi --showmeminfo vram 2>/dev/null
fi

# 7. ECC 错误检查 (数据中心 GPU)
echo ""
echo "=== 7. ECC 状态 ==="
if [ -x /opt/rocm/bin/rocm-smi ]; then
    ECC_COUNT=$(/opt/rocm/bin/rocm-smi --show-ecc-count 2>/dev/null | grep -oP '\d+' | head -1 || echo "")
    if [ -n "$ECC_COUNT" ] && [ "$ECC_COUNT" != "0" ]; then
        echo "  ⚠️  检测到 $ECC_COUNT 个 ECC 错误"
        HEALTHY=false
    else
        echo "  ✅ 无 ECC 错误（或不支持 ECC）"
    fi
fi

# 8. PCIe 链路检查
echo ""
echo "=== 8. PCIe 链路 ==="
for dev in /sys/bus/pci/devices/*/; do
    VENDOR=$(cat "$dev/vendor" 2>/dev/null)
    if [ "$VENDOR" = "0x1002" ]; then
        SPEED=$(cat "$dev/current_link_speed" 2>/dev/null)
        WIDTH=$(cat "$dev/current_link_width" 2>/dev/null)
        echo "  GPU $(basename $dev): PCIe $SPEED x$WIDTH"
    fi
done

# 9. 汇总
echo ""
echo "=============================================="
echo " 健康检查汇总"
echo "=============================================="
if $HEALTHY; then
    echo "  ✅ 所有检查通过"
else
    echo "  ❌ 发现问题，请查看上述检查项"
fi
echo " 报告文件: $REPORT_FILE"
echo "=============================================="
```

### 十六、相关链接

- **ROCm 安装文档**: https://rocm.docs.amd.com/projects/install-on-linux/
- **rocminfo 文档**: https://rocm.docs.amd.com/projects/rocminfo/
- **rocm-smi 文档**: https://rocm.docs.amd.com/projects/rocm_smi_lib/
- **ROCm 版本列表**: https://repo.radeon.com/rocm/
- **AMD GPU 固件仓库**: https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/amdgpu
- **ROCm Docker 镜像**: https://hub.docker.com/r/rocm/rocm-terminal
- **Linux 内核 amdgpu 驱动源码**: https://github.com/torvalds/linux/tree/master/drivers/gpu/drm/amd
- **AMD 官方 GPU 规格**: https://www.amd.com/en/products/specifications/graphics.html
- **HSA Runtime API 文档**: https://rocm.docs.amd.com/projects/HSA-Runtime/
- **GPUOpen 官方**: https://gpuopen.com/
- **Phoronix 测试套件 (GPU 测试)**: https://www.phoronix-test-suite.com/
- **ROCm 兼容性矩阵**: https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html
- **ROCm 环境变量文档**: https://rocm.docs.amd.com/en/latest/conceptual/environment-variables.html
- **ROCm 多版本安装**: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-multi-version.html
- **freedesktop.org AMDGPU Bug Tracker**: https://gitlab.freedesktop.org/drm/amd/-/issues
- **ROCm 故障排除**: https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/troubleshoot.html
- **AMD amd-smi 文档**: https://rocm.docs.amd.com/projects/amdsmi/
- **ROCm 带宽测试**: https://github.com/ROCm/rocm_bandwidth_test

## 今日小结

1. **ROCm 平台架构**：ROCm 分为内核驱动层（amdgpu + amdkfd）、运行时层（HSA Runtime + HIP Runtime）、库层（rocBLAS/rocFFT/MIOpen 等）和工具层（rocminfo/rocm-smi/rocprof 等）四层架构。HSA 提供了 CPU/GPU 统一地址空间和用户态队列调度的基础设施。

2. **内核驱动分工**：amdgpu.ko 负责 GPU 硬件初始化、显存管理、ring buffer 和中断处理；amdkfd.ko 负责计算队列创建/调度、GPU 进程隔离和 /dev/kfd 接口。两者通过 kgd2kfd_calls/kfd2kgd_calls 接口协作。

3. **ROCm 安装**：核心步骤包括添加 ROCm 仓库、安装用户空间组件、安装/配置内核驱动（amdgpu-dkms）、添加用户到 render/video 组、配置 udev 规则、设置环境变量。容器化部署通过映射 /dev/kfd 和 /dev/dri 设备节点实现 GPU 透传。

4. **rocminfo**：基于 HSA API 枚举 Agent 并查询属性（CU 数、缓存、内存池、ISA）。输出显示 GPU 名称、计算单元数（CU）、内存池大小（VRAM/GTT/System）、支持的 ISA（如 gfx1100）等核心信息。

5. **rocm-smi**：通过 sysfs（pp_dpm_sclk, hwmon, mem_info_* 等）和 ioctl 采集 GPU 温度、功耗、频率、显存使用、利用率、PCIe 拓扑等监控数据，并支持频率控制和功耗上限设置。

6. **amd-smi**（ROCm 6.1+）是 rocm-smi 的现代替代，提供 TUI 实时监控、JSON 输出、进程管理和事件监控等高级功能。

7. **环境验证**：完整验证应覆盖安装位置、驱动加载、设备节点权限、GPU 可见性、HIP 编译运行、温度和功耗读取等关键环节。常见问题包括用户组未配置、udev 规则缺失、内核版本不匹配和固件版本过旧。

8. **底层调试**：可通过 sysfs（/sys/class/drm/card*/device/*）和 debugfs（/sys/kernel/debug/dri/*/amdgpu_*）直接获取 GPU 底层状态信息，用于深度排错。

## 扩展思考

1. **HSA 用户态队列 vs 传统内核驱动提交**：amdkfd 的 AQL（Architected Queuing Language）用户态队列允许应用直接向 GPU 硬件环形缓冲区写入命令包，避免了每次提交时的内核态/用户态切换开销。请思考：在什么场景下这种设计能带来显著的性能优势？在 ROCm 6.x 中，门铃（Doorbell）机制是如何实现用户态通知 GPU 队列有新任务的？

2. **多 GPU 场景下的 NUMA 亲和性**：当一台服务器有 8 块 MI300X GPU 时，部分 GPU 挂载在 CPU Socket 0，部分在 CPU Socket 1。如果一个 HIP 程序在不考虑 NUMA 亲和性的情况下运行，会带来多大的性能损失？如何通过 `numactl` 和 `ROCR_VISIBLE_DEVICES` 环境变量实现最优的 GPU-CPU 绑定？

3. **Docker 中 ROCm 的安全隔离**：当容器直接映射 /dev/kfd 和 /dev/dri 时，所有容器共享同一 GPU 硬件。相比 NVIDIA 的 MIG（多实例 GPU）或 AMD 的 GPU 分区（Partitioning），这种方案在安全隔离和资源分配上有什么不足？ROCm 目前如何通过 SR-IOV 或 MES（Micro Engine Scheduler）实现更细粒度的 GPU 资源隔离？

4. **GPU 固件更新的影响**：`linux-firmware` 包中的 amdgpu 固件文件更新（如 `gc_11_0_0_mes.bin` 从旧版本升级到新版本）可能引入新的 MES 调度器特性。请探究 MES（Micro Engine Scheduler）固件在 ROCm 用户态调度中的作用，以及固件版本不匹配可能导致的问题现象。

5. **rocminfo 输出中 Pool 类型的含义**：rocminfo 输出中常看到多个内存池（GLOBAL FINE GRAINED、GLOBAL COARSE GRAINED、GROUP 等）。请深入研究 HSA 内存模型中 FINE GRAINED 和 COARSE GRAINED 的区别，以及它们对 GPU 原子操作和 CPU-GPU 一致性性能的影响。

---

## 补充资料一：高级环境配置

### 1.1 多版本 ROCm 并存

```bash
#!/bin/bash
# rocm_multiversion.sh

echo "=== ROCm 多版本并存 ==="

# 安装不同版本到不同路径
echo "【1】安装 ROCm 6.0 到 /opt/rocm-6.0.2"
echo "  可通过修改 APT sources list 的版本号来安装特定版本"
echo ""
echo "  # 安装 ROCm 6.0.2"
echo "  echo \"deb [arch=amd64] https://repo.radeon.com/rocm/apt/6.0.2 noble main\" | sudo tee /etc/apt/sources.list.d/rocm-6.0.list"
echo "  sudo apt update"
echo "  sudo apt install -y rocm-hip-sdk"
echo ""

echo "【2】安装 ROCm 6.2 到 /opt/rocm-6.2.4"
echo "  使用另一个 sources 文件:"
echo "  echo \"deb [arch=amd64] https://repo.radeon.com/rocm/apt/6.2.4 noble main\" | sudo tee /etc/apt/sources.list.d/rocm-6.2.list"

# 切换脚本
cat > /tmp/switch_rocm_multi.sh << 'SWITCH'
#!/bin/bash
VERSION=${1:-6.2.4}
TARGET="/opt/rocm-${VERSION}"

if [ ! -d "$TARGET" ]; then
    echo "ROCm $VERSION 未找到: $TARGET"
    echo "可用的版本:"
    ls -d /opt/rocm-* 2>/dev/null | sed 's|/opt/rocm-||'
    exit 1
fi

sudo rm -f /opt/rocm
sudo ln -sf "$TARGET" /opt/rocm
echo "已切换到 ROCm $VERSION: /opt/rocm -> $TARGET"

export ROCM_PATH=/opt/rocm
export PATH=$ROCM_PATH/bin:$PATH
export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH

echo ""
echo "环境变量已更新（当前 shell）"
echo "请运行以下命令使其永久生效："
echo "  echo 'source /opt/rocm-${VERSION}/.info/version 参考脚本' >> ~/.bashrc"
SWITCH

chmod +x /tmp/switch_rocm_multi.sh

echo ""
echo "切换脚本已创建: /tmp/switch_rocm_multi.sh"
echo "使用方法: /tmp/switch_rocm_multi.sh 6.0.2"
echo "          /tmp/switch_rocm_multi.sh 6.2.4"
```

### 1.2 GPU 权限和组配置

```bash
#!/bin/bash
# rocm_permissions.sh

echo "=== ROCm 权限配置 ==="

# 1. 检查当前用户组
echo "【1】当前用户组"
groups

# 2. 添加必要组
echo ""
echo "【2】添加用户到组"
sudo usermod -a -G video $USER
sudo usermod -a -G render $USER
sudo usermod -a -G kfd $USER 2>/dev/null || true

# 3. 检查设备权限
echo ""
echo "【3】设备权限"
ls -la /dev/dri/renderD* /dev/kfd 2>/dev/null

# 4. 配置 udev 规则
echo ""
echo "【4】创建 udev 规则"
sudo tee /etc/udev/rules.d/70-amdgpu.rules << 'EOF'
KERNEL=="kfd", GROUP="render", MODE="0660"
KERNEL=="renderD*", GROUP="render", MODE="0660"
KERNEL=="card*", GROUP="video", MODE="0660"
EOF

sudo udevadm control --reload-rules
sudo udevadm trigger

echo ""
echo "权限配置完成，请重新登录或重启以使组更改生效"
echo "验证命令: groups"
```

### 1.3 性能最大化配置

```bash
#!/bin/bash
# rocm_performance_tuning.sh

echo "=== ROCm 性能调优 ==="

# 1. 检查并设置计算模式
echo "【1】计算模式"
FLAGS=$(cat /sys/class/kfd/kfd/topology/nodes/*/properties 2>/dev/null | grep "compute_partition")
echo "当前: $FLAGS"

# 2. 可用 GPU 内存
echo ""
echo "【2】GPU 内存"
cat /sys/class/kfd/kfd/topology/nodes/*/mem_banks/*/properties 2>/dev/null | grep "size"

# 3. NUMA 配置
echo ""
echo "【3】NUMA 配置"
for node in /sys/bus/pci/devices/*/numa_node; do
    [ -f "$node" ] && echo "$(dirname $node): NUMA node $(cat $node)"
done | grep amd

# 4. PCIe 链路速度
echo ""
echo "【4】PCIe 链路"
lspci -vvv 2>/dev/null | grep -A 10 "VGA.*AMD" | grep "LnkSta:"

# 5. CPU 配置
echo ""
echo "【5】NUMA 绑定测试"
numactl --hardware 2>/dev/null | head -15

# 6. 大页配置
echo ""
echo "【6】HugePage 配置"
echo "当前 HugePage 状态:"
cat /proc/meminfo | grep -i huge
echo ""
echo "设置 2MB 大页 (需要 root):"
echo "  echo 2048 | sudo tee /proc/sys/vm/nr_hugepages"
echo ""
echo "设置 1GB 大页 (推荐 ML 工作负载):"
echo "  echo 4 | sudo tee /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages"
```

### 1.4 常见安装问题排查速查表

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| hipGetDeviceCount 返回 0 | 用户不在 render/video 组 | `sudo usermod -aG render,video $USER` |
| rocminfo 无法运行 | PATH 未配置 | `export PATH=/opt/rocm/bin:$PATH` |
| /dev/kfd 不存在 | amdkfd 驱动未加载 | `sudo modprobe amdkfd` |
| 库未找到 | LD_LIBRARY_PATH 未配置 | `export LD_LIBRARY_PATH=/opt/rocm/lib` |
| Permission denied | /dev/dri/renderD* 权限 | 添加 udev 规则 |
| 安装失败(依赖) | 系统版本不匹配 | 检查 ROCm 支持的 OS 版本 |
| GPU 固件加载失败 | linux-firmware 太旧 | `sudo apt update && sudo apt install linux-firmware` |
| HIP 程序 OOM | VRAM 不足 | 检查 rocm-smi --showmeminfo，可能需要释放显存 |
| "amdgpu: failed to initialize" | 内核参数冲突 | 检查 `cat /proc/cmdline`，尝试添加 `amdgpu.runpm=0` |
| 编译时 "cannot find -lrocblas" | 库链接路径未配置 | `export LIBRARY_PATH=/opt/rocm/lib:$LIBRARY_PATH` |
