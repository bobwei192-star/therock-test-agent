# ROCm 测试需求解析提示词优化方案

## 目录

1. [核心问题：8 种意图是否需要 8 套提示词？](#1-核心问题)
2. [推荐方案：1 主 + 3 变体](#2-推荐方案)
3. [意图聚类分析](#3-意图聚类分析)
4. [提示词模板设计](#4-提示词模板设计)
5. [意图路由实现](#5-意图路由实现)
6. [架构对比总结](#6-架构对比总结)
7. [扩展：新增 ENV_BUILD 意图](#7-扩展-新增-env_build-意图)
8. [方案合理性评估](#8-方案合理性评估)

---

## 1. 核心问题

在设计 ROCm 测试需求解析系统时，面临以下 8 种用户意图：

| 意图 | 描述 |
|------|------|
| GENERATE | 从零创建新测试用例 |
| APPEND | 在现有测试文件上追加新测试函数/场景 |
| UPDATE | 修复已有测试的错误或适配新版本 |
| REFACTOR | 优化代码结构，不改测试逻辑与断言目标 |
| EXECUTE_EXTERNAL | 下载/编译/运行第三方测试套件（如 igt-gpu-tools） |
| DIAGNOSE | 分析测试失败日志，定位根因 |
| COVERAGE | 分析现有测试集的等价类/边界值覆盖度 |
| PROBE | 探测当前 ROCm 环境能力，输出报告 |

**问题**：是否需要为每种意图编写独立的提示词或创建独立的子 Agent？

---

## 2. 推荐方案

**核心结论**：不需要 8 套提示词，也不需要 8 个子 Agent。推荐「1 个主提示词 + 3 个变体」方案。

| 方案 | 提示词数量 | 子 Agent 数量 | 维护成本 | 推荐度 |
|------|-----------|--------------|----------|--------|
| A. 8 套完整提示词 | 8 | 0~8 | 🔴 极高 | ❌ 不推荐 |
| B. 8 个子 Agent | 8 | 8 | 🔴 极高 | ❌ 不推荐 |
| C. 1 主 + 3 变体（推荐） | 4 | 1 | 🟢 低 | ✅ 推荐 |
| D. 1 个提示词 + 动态条件分支 | 1 | 1 | 🟡 中 | ⚠️ 可行但易混淆 |

---

## 3. 意图聚类分析

### 3.1 聚类逻辑

8 个意图可以按「工作模式」聚为三类：

```
┌─────────────────────────────────────────────────────────────┐
│                    测试生命周期                              │
├─────────────┬─────────────┬─────────────────────────────────┤
│   创建类     │   修改类     │           查询/诊断类            │
│  (写代码)    │  (改代码)    │         (只读/分析)             │
├─────────────┼─────────────┼─────────────────────────────────┤
│ • GENERATE  │ • UPDATE    │ • DIAGNOSE                      │
│ • APPEND    │ • REFACTOR  │ • COVERAGE                      │
│             │             │ • PROBE                         │
│             │             │ • EXECUTE_EXTERNAL              │
└─────────────┴─────────────┴─────────────────────────────────┘
```

### 3.2 聚类差异表

| 聚类 | 核心差异 | 输出要求 |
|------|----------|----------|
| 创建类 | 从零产出代码 | 必须输出完整测试规格 + AAAC + Fixture |
| 修改类 | 基于已有代码变更 | 必须包含「历史代码约束」章节 + 变更范围 |
| 查询/诊断类 | 不产出代码，只分析 | 简化模板，禁止输出代码生成相关章节 |

---

## 4. 提示词模板设计

### 4.1 模板 A：创建类（GENERATE + APPEND）

**复用度**：~90%

**设计理由**：两者都产出新代码，区别仅在于 APPEND 多一个「历史代码约束」章节。

```markdown
## 意图识别
意图: <GENERATE|APPEND>

## 测试规格输出
1. 测试目标: <一句话描述被测功能>
2. ROCm 组件: <命令/库名，如 rocm-smi/rocminfo/rocBLAS/kfd>
3. 测试点清单:
   - <测试点1>: <等价类:有效/无效/边界> | <AAAC简要>
   - <测试点2>: ...
4. 等价类划分:
   - 有效等价类: <正常输入/正常环境/正常输出场景>
   - 无效等价类: <命令缺失/无GPU/权限不足/异常参数>
   - 边界等价类: <数值边界/单多GPU边界/空输出边界>
5. AAAC 四阶段设计:
   - Arrange: <环境检查、数据准备、fixture 依赖初始化>
   - Act: <执行被测命令或调用被测函数的具体方式>
   - Assert: <验证返回码、输出关键词存在性、数值范围>
   - Cleanup: <副作用清理动作；只读操作写"无">
6. 断言策略:
   - 应断言: <返回码为0、数值在合理范围、输出包含关键词>
   - 禁断言: <精确字符串匹配、具体数值等于、输出长度固定>
   - 诊断要求: <assert 失败时必须输出 returncode、stderr[:500]、stdout[:500]>
7. 降级条件: <命令不在PATH时skip、无AMD GPU时skip、ROCm版本不兼容时skip>
8. Fixture 需求: <命令执行器fixture/临时文件fixture/无>
9. 历史代码约束（仅 APPEND 时必填）: <...>（GENERATE 时写"无"）
```

### 4.2 模板 B：修改类（UPDATE + REFACTOR）

**设计理由**：两者都不新增测试逻辑，只是修改现有代码。

```markdown
## 意图识别
意图: <UPDATE|REFACTOR>

## 测试规格输出
1. 测试目标: <一句话描述被测功能>
2. ROCm 组件: <命令/库名>
3. 测试点清单: <...>
4. 等价类划分: <...>
5. AAAC 四阶段设计: <...>
6. 断言策略: <...>
7. 降级条件: <...>
8. Fixture 需求: <...>
9. 历史代码约束（必填）:
   - 必须保留的函数: <...>
   - 禁止修改的断言目标: <...>
   - 允许调整的结构: <...>
   - UPDATE 额外: <错误根因分析>
   - REFACTOR 额外: <结构优化目标>
```

### 4.3 模板 C：查询/诊断类（DIAGNOSE + COVERAGE + PROBE）

**设计理由**：三者都是只读分析，不生成代码。

```markdown
## 意图识别
意图: <DIAGNOSE|COVERAGE|PROBE>

## 简化模板（禁止输出代码生成章节）
1. 分析目标: <一句话描述分析目标>
2. 输入数据: <日志/代码/环境信息>
3. 分析维度:
   - DIAGNOSE: <失败阶段→根因→修复建议>
   - COVERAGE: <等价类覆盖度→缺失点→补充建议>
   - PROBE: <环境能力项→探测结果→兼容性结论>
4. 输出格式: <结构化报告，不含代码块>
```

**关键约束**：明确禁止输出 AAAC、Fixture、代码模板等章节。

### 4.4 external_intent：外部执行类（EXECUTE_EXTERNAL）

**设计理由**：这是唯一涉及「下载/编译/运行第三方代码」的模式，工作流完全不同。

```markdown
## 意图识别
意图: EXECUTE_EXTERNAL

## 执行规格
1. 目标套件: <如 igt-gpu-tools>
2. 获取方式: <git clone/下载tar/包管理器>
3. 编译依赖: <...>
4. 运行方式: <...>
5. 结果提取: <...>
```

---

## 5. 意图路由实现

不需要 LLM 判断，规则匹配即可：

```python
def route_intent(raw_requirement: str) -> str:
    """意图路由：规则匹配 8 选 1"""
    text = raw_requirement.lower()
    
    # 修改类
    if any(k in text for k in ["修复", "报错", "失败", "error", "fix"]):
        return "UPDATE" if "重构" not in text else "REFACTOR"
    
    # 创建类（追加）
    if any(k in text for k in ["追加", "添加", "补充", "append", "add"]):
        return "APPEND"
    
    # 查询诊断类
    if any(k in text for k in ["诊断", "分析日志", "为什么失败", "diagnose"]):
        return "DIAGNOSE"
    if any(k in text for k in ["覆盖度", "覆盖率", "coverage"]):
        return "COVERAGE"
    if any(k in text for k in ["探测", "环境", "probe", "环境能力"]):
        return "PROBE"
    
    # 外部执行类
    if any(k in text for k in ["igt", "外部套件", "第三方", "external"]):
        return "EXECUTE_EXTERNAL"
    
    # 默认：创建新测试
    return "GENERATE"
```

### 5.1 推荐架构

```
用户输入
   │
   ▼
┌─────────────────────┐
│  轻量级意图分类器     │  ← 规则匹配（5 行代码）
│  (Intent Router)    │
└─────────────────────┘
   │
   ├── GENERATE/APPEND ──→ 加载 create_intent ──→ 主 Agent 执行
   ├── UPDATE/REFACTOR ──→ 加载 update_intent ──→ 主 Agent 执行
   ├── DIAGNOSE/COVERAGE/PROBE ──→ 加载 query_intent ──→ 主 Agent 执行
   └── EXECUTE_EXTERNAL ──→ 加载 external_intent ──→ 主 Agent 执行
```

---

## 6. 架构对比总结

| 维度 | 8 套提示词/8 个子 Agent | 1 主 + 5 意图模板（推荐） |
|------|------------------------|--------------------------|
| 提示词维护量 | 8 份 × 全量章节 | 5 份 × 差异化章节 |
| Agent 维护量 | 8 个独立配置 | 1 个统一配置 |
| 意图误判成本 | 高（Agent 间无法回退） | 低（只是换模板） |
| 新增意图扩展 | 需新增完整 Agent | 只需添加意图模板 |
| LLM 调用次数 | 2 次 | 2 次 |
| 上下文一致性 | 差（各 Agent 独立记忆） | 好（统一 Store 命名空间） |

---

## 7. 扩展：新增 ENV_BUILD 意图

### 7.1 需求场景

用户需要编译 Docker 镜像或测试环境镜像（例如为测试某个模型，提前编译 rocm+pytorch+llvm 成镜像）。

### 7.2 为什么需要新增意图

| 候选意图 | 不匹配原因 |
|----------|------------|
| EXECUTE_EXTERNAL | 产出测试报告，而非 Dockerfile |
| GENERATE | 产出 test_*.py，而非 Dockerfile |
| PROBE | 只读探测，而非写操作（编译、打包） |
| REFACTOR | 无历史镜像代码可供重构 |

**结论**：必须新增第 9 意图，命名为 `ENV_BUILD`（环境构建）。

### 7.3 架构设计：「1 Agent + 5 个意图模板 + 策略模式」

#### 方案对比与选型

| 维度 | 方案A：策略模式 | 方案B：条件边路由 |
|------|----------------|------------------|
| **架构复杂度** | 低（单一节点） | 中（条件分支） |
| **职责分离** | 策略内聚 | 节点分离 |
| **扩展性** | 高（新增策略即可） | 中（需修改条件边） |
| **代码可维护性** | 高（策略模式解耦） | 中（条件判断扩散） |
| **Graph 结构** | 简洁 | 复杂 |
| **推荐度** | ✅ 推荐 | ⚠️ 不推荐 |

**最终选择：方案A（策略模式）**

```
用户输入
   │
   ▼
┌─────────────────────────┐
│   Intent Router (9选1)  │
│   ENV_BUILD 关键词优先   │
└─────────────────────────┘
   │
   ├── 创建类 ──────→ create_intent
   ├── 修改类 ──────→ update_intent
   ├── 查询诊断类 ───→ query_intent
   ├── 外部执行类 ───→ external_intent
   └── 环境构建类 ───→ build_intent  ← 新增
                           │
                           ▼
                    ┌─────────────┐
                    │  统一 Agent  │
                    │ (同一模型/记忆)│
                    └─────────────┘
                           │
                           ▼
               ┌────────────────────────┐
               │      generator         │
               │ 输出: artifact_path     │
               │ (test_xxx.py 或 Dockerfile)│
               └────────────────────────┘
                           │
                           ▼
               ┌────────────────────────┐
               │    sandbox_executor    │
               │ 根据 intent 选择策略    │ ← 策略模式，无 if-else
               │ ├─ PytestStrategy      │
               │ ├─ DockerBuildStrategy │
               │ └─ ExternalRunStrategy │
               └────────────────────────┘
                           │
                           ▼
                          END
```

**策略模式优势**：
1. **开闭原则**：新增意图只需添加新策略，无需修改现有代码
2. **职责清晰**：每个策略专注于一种执行方式
3. **无 if-else 地狱**：通过多态替代条件判断
4. **测试友好**：策略可独立单元测试

### 7.4 build_intent：ENV_BUILD 规格设计

```markdown
## 意图识别
意图: ENV_BUILD

## 构建规格输出
1. 构建目标: <一句话，如"编译 ROCm 6.0 + PyTorch 2.3 + LLVM 17 的测试基础镜像">
2. 基础镜像: <如 rocm/dev-ubuntu-22.04:6.0>
3. ROCm 组件清单:
   - <组件1>: <版本/分支> | <安装方式: apt/源码编译/官方wheel>
4. 第三方依赖:
   - <PyTorch>: <版本> | <构建方式>
   - <LLVM>: <版本> | <构建方式>
5. 构建阶段设计:
   - Stage 1 (系统层): <apt update/install 基础工具>
   - Stage 2 (ROCm层): <安装/验证 ROCm 核心库>
   - Stage 3 (Python层): <pip install / 编译 PyTorch>
   - Stage 4 (验证层): <rocm-smi 探测、CUDA 可用性检查>
6. 缓存与体积优化:
   - 层缓存策略: <哪些指令合并以减少层数>
   - 清理动作: <apt clean / pip cache purge>
7. 运行时约束:
   - 设备挂载: </dev/kfd,/dev/dri>
   - 环境变量: <HSA_OVERRIDE_GFX_VERSION / PYTORCH_ROCM_ARCH>
8. 验证脚本:
   - 自检命令: <rocm-smi、python -c "import torch; print(torch.cuda.is_available())">
9. 输出物:
   - Dockerfile 片段或完整文件
   - build.sh（含 docker buildx 命令、标签策略）
```

### 7.5 Graph 适配方案：策略模式

**推荐实现：sandbox_executor 内部策略模式**

```python
from abc import ABC, abstractmethod
from typing import Any, Dict

# 策略接口
class ExecutionStrategy(ABC):
    @abstractmethod
    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        pass

# Pytest 测试执行策略
class PytestStrategy(ExecutionStrategy):
    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        # 执行 pytest test_xxx.py
        result = client.exec("pytest", artifact_path)
        return {"status": "success" if result.returncode == 0 else "failed",
                "output": result.stdout}

# Docker 构建策略
class DockerBuildStrategy(ExecutionStrategy):
    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        # 执行 docker build
        result = client.exec("docker", "build", "-f", artifact_path, ".")
        return {"status": "success" if result.returncode == 0 else "failed",
                "image_tag": extract_image_tag(result.stdout)}

# 外部套件执行策略
class ExternalRunStrategy(ExecutionStrategy):
    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        # 执行外部测试套件
        result = client.exec(artifact_path)
        return {"status": "success" if result.returncode == 0 else "failed",
                "report": result.stdout}

# 策略工厂
class StrategyFactory:
    _strategies = {
        "GENERATE": PytestStrategy(),
        "APPEND": PytestStrategy(),
        "UPDATE": PytestStrategy(),
        "REFACTOR": PytestStrategy(),
        "ENV_BUILD": DockerBuildStrategy(),
        "EXECUTE_EXTERNAL": ExternalRunStrategy(),
        # DIAGNOSE/COVERAGE/PROBE 不需要执行策略
    }
    
    @classmethod
    def get_strategy(cls, intent: str) -> ExecutionStrategy:
        return cls._strategies.get(intent, PytestStrategy())

# sandbox_executor 节点
def sandbox_executor(state: AgentState) -> Dict[str, Any]:
    intent = state.get("parsed_intent", "GENERATE")
    artifact_path = state.get("generated_artifact", "")
    
    if not artifact_path:
        return {"status": "failed", "errors": ["No artifact generated"]}
    
    # 使用策略模式执行
    strategy = StrategyFactory.get_strategy(intent)
    result = strategy.execute(artifact_path, state)
    
    return {"execution_result": result}
```

**策略模式优势**：
1. **开闭原则**：新增意图只需添加新策略类，无需修改 sandbox_executor
2. **无 if-else**：通过多态替代条件判断
3. **测试友好**：每个策略可独立单元测试
4. **职责分离**：策略只负责执行逻辑，sandbox_executor 只负责调度

### 7.6 意图路由规则扩展（9 选 1）

```python
def route_intent(raw_requirement: str) -> str:
    text = raw_requirement.lower()
    
    # 新增 ENV_BUILD 识别（优先级最高）
    env_keywords = [
        "docker", "镜像", "image", "编译环境", "build image",
        "rocm+pytorch", "llvm编译", "基础镜像", "dockerfile",
        "环境准备", "容器化", "镜像构建"
    ]
    if any(k in text for k in env_keywords):
        return "ENV_BUILD"
    
    # 原有 8 意图...
    # ...
    
    return "GENERATE"
```

### 7.7 记忆空间设计

```python
# 当前记忆命名空间
("user_id", "project_id", "plans")        # 测试计划
("user_id", "project_id", "generations")  # 测试代码

# 新增
("user_id", "project_id", "env_builds")   # 镜像构建历史
```

**好处**：支持跨命名空间召回（如"基于上次构建的镜像跑测试"）。

### 7.8 build_intent 设计总结

| 维度 | 设计决策 | 理由 |
|------|----------|------|
| 意图数量 | 9 个（新增 ENV_BUILD） | 语义边界清晰 |
| Agent 数量 | 仍 1 个 | 同一模型能力域 |
| 提示词模板 | 5 个（create_intent/update_intent/query_intent/external_intent/build_intent） | ENV_BUILD 独立模板 |
| Graph 节点 | 策略模式统一执行 | 保持单一 sandbox_executor，无分支 |
| 记忆命名空间 | 新增 env_builds | 与测试代码记忆隔离 |
| 沙盒行为 | 策略选择执行 | PytestStrategy/DockerBuildStrategy/ExternalRunStrategy |

---

## 8. 方案合理性评估

### 8.1 优点

| 维度 | 评估 |
|------|------|
| **架构简洁性** | ✅ 统一 Agent + 差异化模板，避免碎片化 |
| **可维护性** | ✅ 4-5 个模板 vs 8-9 个，降低维护成本 |
| **扩展性** | ✅ 新增意图只需判断聚类，无需重构整个系统 |
| **容错性** | ✅ 意图误判时只需换模板，不影响 Agent 切换 |
| **上下文一致性** | ✅ 统一记忆空间，支持跨意图关联 |
| **性能** | ✅ 规则路由避免额外 LLM 调用 |

### 8.2 潜在风险与缓解

| 风险 | 描述 | 缓解策略 |
|------|------|----------|
| 规则匹配不足 | 复杂意图可能漏判 | 预留轻量级 LLM 分类作为 fallback |
| 模板膨胀 | 条件章节过多导致模板复杂 | 模板中使用条件注释标记 |
| 沙盒复杂度 | ENV_BUILD 需要特殊处理 | 独立验证节点，保持 sandbox_executor 纯净 |

### 8.3 最终评价

**架构合理性**：⭐⭐⭐⭐⭐（5/5）

该方案在保持架构简洁性的同时，兼顾了扩展性和灵活性：
- 通过聚类减少了 50% 的模板维护量
- 统一 Agent 保证了上下文一致性
- ENV_BUILD 的设计保持了主图纯洁性
- 规则路由保证了低延迟

**实施建议**：
1. 先实现「1 Agent + 4 模板」核心架构
2. 验证稳定后再扩展 ENV_BUILD
3. 监控意图分类准确率，必要时引入轻量级 LLM 分类器作为增强