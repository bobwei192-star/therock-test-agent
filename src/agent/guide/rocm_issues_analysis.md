# ROCm Issues 集合分析与总结

## 数据概览

- **数据来源**: https://github.com/ROCm/ROCm/issues
- **总Issue数量**: 3129 条
- **开放中**: 228 条 | **已关闭**: 2901 条
- **采集时间**: 2026-05-27
- **时间跨度**: 2016年 (ROCm 1.0) ~ 至今

### 高频标签统计
| 标签 | 数量 | 说明 |
|------|------|------|
| Under Investigation | 452 | 调查中 |
| status: triage | 227 | 待分类 |
| Documentation | 178 | 文档问题 |
| Feature Request | 146 | 功能请求 |
| Verified Issue | 103 | 已验证问题 |
| Compiler Functional Bug | 12 | 编译器功能Bug |
| Bug_Functional_Issue | 24 | 功能性问题 |

---

## 一、按芯片分类

### 1.1 旗舰/数据中心 GPU

| 芯片系列 | 典型型号 | ISA标识 | 相关Issue |
|----------|----------|---------|-----------|
| **Vega 10** | Radeon VII, MI50 | gfx900/gfx906 | #1124, #1149, #1196 (性能回归), #1098 (代码生成Bug) |
| **Vega 20** | Radeon Instinct MI50/MI60 | gfx906 | #1062 (MI50不工作) |
| **Arcturus** | MI100 | gfx908 | 新架构适配问题 |
| **Aldebaran** | MI250X | gfx90a | 11条标记 |
| **Aqua Vanjaram** | MI300X | gfx942 | 32条标记 |

### 1.2 消费者 GPU

| 芯片系列 | 典型型号 | ISA标识 | 主要问题 |
|----------|----------|---------|----------|
| **Hawaii** | S9150, R9 290X/390X | gfx701 | #1006 (ROCm 3.0 后支持中断), #1159 (PyTorch不支持) |
| **Polaris** | RX 470/480/580 | gfx803 | #1008 (clinfo卡死), #1073 (TF buggy), #1165 (TF segfault) |
| **Vega** | Vega 56/64 | gfx900 | #1149 (P-state卡住), #1106 (Blender渲染) |
| **Navi 10 (RDNA1)** | RX 5700/5700XT | gfx1010 | #1061, #1003, #1079, #1194 (长期无官方支持) |
| **Navi 21/22 (RDNA2)** | RX 6800/6900XT | gfx1030 | #1180 (用户强烈要求支持, ROCm 5.0 才开始) |
| **Navi 31/32 (RDNA3)** | RX 7900XT/7900XTX | gfx1100 | 63条+38条标记，较新一代支持延迟 |

### 1.3 APU / 移动端

| 芯片系列 | 典型型号 | ISA标识 | 主要问题 |
|----------|----------|---------|-----------|
| **Carrizo** | A10/A12 APU | gfx801 | #106 (BIOS/CRAT表配置需求) |
| **Bristol Ridge** | A-series APU | gfx801 | #106评论区 (部分笔记本可工作) |
| **Raven Ridge** | Ryzen 2500U | gfx902 | #1034 (clinfo segfault), #1176 (rocminfo内核segfault) |
| **Renoir** | Ryzen 4000系列APU | gfx909 | #1101 (支持计划问题) |

---

## 二、按问题现象分类

### 2.1 安装/部署问题（最高频）

| 子类别 | 典型现象 | 代表Issue |
|--------|----------|-----------|
| 自动升级破坏 | 系统更新时ROCm自动升级导致安装损坏 | #1198 |
| APT源问题 | 仓库签名无效/404/源不可达 | #1009, #1058, #1169, #1186 |
| 依赖缺失 | 包缺少依赖声明 | #1167, #1129, #1130, #1131 |
| 路径错误 | /opt/rocm 符号链接、ldconfig路径 | #1156, #1157 |
| 版本化包冲突 | 版本化与非版本化包冲突 | #1134, #1160 |

### 2.2 驱动/运行时错误

| 子类别 | 典型现象 | 代表Issue |
|--------|----------|-----------|
| HSA资源耗尽 | `HSA_STATUS_ERROR_OUT_OF_RESOURCES` | #1047, #1080, #1088 |
| /dev/kfd不可用 | `Cannot allocate memory` / `Failed to get user name` | #1109, #1148, #1174, #1185 |
| hsa_api_call_failure | 安装后调用失败 | #1064, #1070, #1104 |
| PCIe原子操作 | `PCI rejects atomics` 导致设备不可用 | #1047 评论区 |
| GPU初始化失败 | amdgpu_device_ip_init failed | #1038, #1079 |

### 2.3 编译器/代码生成Bug

| 子类别 | 典型现象 | 代表Issue |
|--------|----------|-----------|
| 严重代码生成错误 | 生成错误ISA导致计算结果错误 | #1098 (OMOD调度Bug) |
| VGPR分配问题 | 寄存器使用过多导致Occupancy下降 | #1002, #1124, #1196 |
| 优化选项错误 | -cl-fast-relaxed-math相关 | #1098 |
| flat vs ds原子操作 | 局部内存使用了flat操作而非ds操作 | #1181 |
| 版本间回归 | 3.3正常 → 3.5/3.7异常 | #1097, #1032 |

### 2.4 性能回归

| 子类别 | 典型现象 | 代表Issue |
|--------|----------|-----------|
| 版本间退化 | ROCm 3.3→3.5有5%退化 | #1124 |
| 编译器回归 | comgr变更导致VGPR增加 | #1196 (3.3→3.7持续到5.0) |
| 特定场景退化 | gpuOwl、HPC应用受影响 | #1124, #1196 |
| 内存带宽退化 | HBM1使用超过2GB时带宽减半 | #102 |

### 2.5 应用兼容性

| 应用领域 | 典型应用 | 代表Issue |
|----------|----------|-----------|
| 深度学习 | TensorFlow, PyTorch | #1073, #1159, #1014 |
| 3D渲染 | Blender Cycles | #1030, #1106 |
| 视频后期 | Davinci Resolve | #1030 |
| 分布式计算 | gpuOwl, Folding@Home | #1020, #1081 |
| 基准测试 | Luxmark, clpeak | #1145 |
| 科学计算 | Keras, OpenMPI | #1042, #1017 |

### 2.6 OS兼容性

- **Ubuntu**: 16.04/18.04/19.10/20.04/22.04/24.04 (最广泛)
- **Debian**: #1125
- **RHEL/CentOS/SLES**: #1071, #1084
- **Arch Linux**: #117, #1149
- **Solus**: #1000
- **Fedora**: #1133
- **Kali**: #1060
- **ClearLinux**: #1197
- **非Linux**: FreeBSD (#105), ARM64 (#1052)

### 2.7 工具问题

| 工具 | 典型现象 | 代表Issue |
|------|----------|-----------|
| clinfo | 卡死/Segfault/无输出 | #1007, #1008, #1034, #1040, #1063, #1117 |
| rocminfo | HSA error/依赖缺失 | #1063, #1129, #1174, #1176 |
| rocm-smi | 设置时钟/配置文件失败 | #1051, #1089, #1144 |
| rocprof | OpenCL支持 | #1100 |

### 2.8 硬件支持与文档

| 类别 | 典型现象 | 代表Issue |
|------|----------|-----------|
| 新架构支持延迟 | Navi/RDNA2用户长期等待 | #1061, #1180 |
| 老旧硬件废弃 | gfx7/gfx8 被官方移除 | #1073, #1159, #1198 (Vega56被弃) |
| 不支持GUI应用 | 官方文档声明(后修改) | #1106 评论区 |
| 文档错误 | 安装指南误导、编程指南混乱 | #1127, #1135, #1136 |

---

## 三、按驱动/软件层次分类

### 3.1 Kernel Driver (amdgpu-dkms/ROCk)
- GPU初始化、PCIe原子操作、IOMMUv2配置
- SMU/BTC固件通信问题
- P-state电源管理
- 内核版本兼容性 (4.x → 5.x → 6.x)

### 3.2 HSA Runtime (ROCR-Runtime)
- HSA_STATUS_ERROR_OUT_OF_RESOURCES
- /dev/kfd 访问失败
- 多GPU设备管理
- 内存池分配

### 3.3 HIP Runtime (HIP/ROCclr)
- hipErrorNoDevice (#1159)
- hipErrorNoBinaryForGpu
- CUDA兼容层转换问题
- HIP_VISIBLE_DEVICES (#1170)

### 3.4 OpenCL Runtime
- clinfo 工具问题
- Image支持
- clGetPlatformIDs/clGetDeviceIDs错误
- SVM能力报告

### 3.5 编译器 (LLVM/COMGR/lightning compiler)
- VGPR分配问题
- 调度优化问题
- flat vs ds 指令选择
- OMOD支持
- 版本间回归

### 3.6 上层库 (MIOpen/rocBLAS/rocRAND)
- 深度学习框架依赖
- 特定架构汇编内核缺失 (RDNA)
- Winograd卷积支持

### 3.7 工具与基础设施
- ROCm-SMI (系统管理)
- rocprof (性能分析)
- rocminfo (设备信息)
- 安装脚本和包管理

---

## 四、按用途/使用场景分类

| 场景 | 用途 | 关键组件 | 突出问题 |
|------|------|----------|----------|
| **AI训练/推理** | TensorFlow, PyTorch, ONNX | ROCm → MIOpen, rocBLAS | GPU支持列表不明确，新硬件支持慢 |
| **HPC/科学计算** | 自定义kernel, OpenMP | OpenCL/HIP Runtime, LLVM | 编译器回归和VGPR分配导致性能不稳定 |
| **3D渲染** | Blender, Davinci Resolve | OpenCL Runtime | GUI应用兼容性差，渲染结果错误 |
| **加密/挖矿** | Ethminer, 自定义算法 | OpenCL | 代码生成正确性要求高 |
| **分布式计算** | gpuOwl, Folding@Home | OpenCL | 性能回归问题敏感 |
| **系统管理** | GPU监控、调频 | rocm-smi | 时钟设置不可靠 |

---

## 五、对 Test Case Agent 的价值分析

### 5.1 作为测试场景知识库的三大核心价值

#### 价值一：提供真实、丰富的测试场景模板

这个 issue 集合直接来源于真实用户的使用反馈，覆盖了 ROCm 生态几乎所有的组件和使用方式。每个 issue 都是一个天然的 **测试场景原型**，包含：

- **触发条件**: 用户的操作环境（OS版本、Kernel版本、GPU型号）
- **预期行为**: 用户期望的功能/workflow
- **实际行为**: 具体的错误信息、日志输出
- **复现步骤**: 用户描述的触发方式
- **诊断信息**: 日志输出、dmesg、配置状态

**对 Agent 的启示**: 可以作为生成测试用例的输入材料，Agent 可以从 issue 描述中提取：
- 测试前置条件（环境配置、依赖版本）
- 测试步骤（安装 → 配置 → 运行）
- 验证断言（rocminfo 正常输出、clinfo 识别设备、无 segfault）

#### 价值二：建立问题分类体系，指导测试覆盖优先级

从 issue 分类可以看出，测试需要覆盖以下层次：

```
安装/卸载 → 包依赖 → 驱动加载 → HSA初始化 → HIP/OpenCL运行时 → 编译器 → 上层框架
```

每个层次都有对应的失败模式，可以帮助 Agent 设计分层测试策略：

| 测试层次 | 验证目标 | 可从Issue推导的测试用例 |
|----------|----------|------------------------|
| L0: 环境检查 | Kernel版本、PCIe原子操作、IOMMU | 检查 `/dev/kfd` 可读写，检查 AtomOps |
| L1: 安装 | 包依赖完整性、路径正确性 | 检查 /opt/rocm 符号链接、ldconfig |
| L2: 驱动加载 | GPU识别、HSA初始化 | rocminfo 输出解析 |
| L3: OpenCL Runtime | ICD加载、设备枚举 | clinfo 输出解析、OpenCL kernel运行 |
| L4: HIP Runtime | 设备发现、kernel编译执行 | hip-samples 示例运行 |
| L5: 编译器 | ISA生成正确性、性能一致性 | 编译简单kernel检查ISA |
| L6: 框架 | TF/PyTorch基础运算 | 导入框架、执行基本操作 |

#### 价值三：提供回归测试的关键检查点

多个 issue 演示了版本升级引入回归的问题：

- **#1124, #1196**: ROCm 3.3 → 3.5 编译器回归导致 ~5% 性能退化
- **#1098**: LLVM commit 555d8f4e 引入严重代码生成 Bug
- **#1030**: ROCm 3.1 完全破坏 Blender/Davinci Resolve
- **#1079**: ROCm 3.3 破坏 Navi 内核模式支持

这些历史回归案例可以作为 Agent 设计 **回归测试套件** 的依据，确保：
- 关键应用（Blender、TF、PyTorch）在新版本上正常工作
- GPU 频率管理（P-state）不会异常
- 编译器输出的一致性检查

### 5.2 具体可提炼的测试维度

#### A. 操作系统 + 内核版本矩阵

基于 issue 的高频出现模式：
```
Ubuntu 18.04 + Kernel 4.15 / 5.3+
Ubuntu 20.04 + Kernel 5.4+
Ubuntu 22.04 + Kernel 5.15+
Debian Bullseye / Bookworm
RHEL 7.x / 8.x / 9.x
```

#### B. GPU 芯片矩阵

```
gfx701 (Hawaii)    - 老旧、部分弃用
gfx803 (Polaris)   - 消费级、逐步弃用
gfx900/gfx906 (Vega) - 主力计算卡（也被部分弃用）
gfx908 (MI100)     - 数据中心
gfx90a (MI200)     - 数据中心
gfx942 (MI300)     - 最新数据中心
gfx1010 (Navi10)   - RDNA1 消费级
gfx1030 (Navi21)   - RDNA2 消费级（ROCm 5.0+支持）
gfx1100 (Navi31)   - RDNA3 消费级（早期支持）
```

#### C. 关键工具体验检查

| 工具 | 正常期望 | 异常信号 |
|------|----------|----------|
| `rocminfo` | 列出所有GPU, 显示ISA和内存 | HSA_STATUS_ERROR, segfault |
| `clinfo` | 列出OpenCL平台和设备 | 卡死、无输出、clGetDeviceIDs(-1) |
| `rocm-smi` | 显示GPU状态、可设置频率 | 时钟设置无效、GPU卡在异常P-state |
| `hipcc` | 编译HIP代码 | hipErrorNoBinaryForGpu |
| `python -c "import torch; torch.cuda.is_available()"` | True | False / RuntimeError |

### 5.3 对 Agent 架构设计的指导

1. **分层验证策略**: Agent 应生成从底层到上层的逐层验证脚本，按照 L0→L6 层次递进
2. **环境感知**: 测试用例需包含环境检测前置步骤（GPU型号、Kernel版本、OS版本）
3. **错误模式匹配**: 可以将高频错误模式（如 HSA_STATUS_ERROR_OUT_OF_RESOURCES）编码为已知问题库，用于智能诊断
4. **版本感知回归**: 记录已知的性能基线和bug修复版本，对新版本自动触发回归检查
5. **多维度覆盖**: 生成测试用例时兼顾：OS × Kernel × GPU × ROCm版本 × 框架版本的交叉组合

### 5.4 注意事项

- 本文档中描述的 issue 主要集中在 ROCm 早期版本（1.0 ~ 5.0），但反映的问题模式具有普遍性
- 部分 issue 中 GPU 已经被官方弃用（如 gfx7/gfx8），但仍可作为测试 "降级场景" 的参考
- ROCm 6.0+ 的新 issue 在 stats.json 中也占了相当比例，说明新架构（RDNA3, MI300）仍有持续的新问题出现
- 建议 Agent 优先覆盖 stats.json 中高频标记对应的硬件-版本组合

---

**文档创建时间**: 2026-05-27  
**数据来源**: `/home/zs/TestCaseAgent/src/agent/rocm_issues/issues/` (3129条issue)
