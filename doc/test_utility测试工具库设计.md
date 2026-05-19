# Test Utility 测试工具库设计

## 1. 背景

`Test Case Agent` 生成的是 **pytest 测试脚本（`test_*.py`）和 Shell 测试脚本（`test_*.sh`）**。这些脚本在执行时，需要一套可复用的、模块化的、可插拔的工具函数库——这就是 `test_utility` 的定位。

**它不是 Agent 的 Tool Use（Function Calling）**，而是生成的测试代码可以 `import` 或 `source` 的共享库。

### 设计原则

- **可插拔**：测试脚本通过 `import rocm_test_utils` 或 `source suites/lib.sh` 使用
- **独立可测**：每个工具函数可以单独单元测试
- **安全可控**：高风险操作（下载模型、安装包、Docker）需加 `dry_run` / `confirm` 保护
- **共享性**：Agent 的 Tool Use 层和测试脚本可以共享同一套底层实现

### 和 Agent Tool Use 的边界

| 维度 | Agent Tool Use | Test Utility |
|------|----------------|--------------|
| 调用者 | LLM Agent 推理循环 | pytest / shell 测试脚本 |
| 触发时机 | 生成代码之前/之后 | 测试执行期间 |
| 返回值消费方 | Agent 的 Memory/State | 测试断言 `assert` |
| 典型用途 | 搜索已有用例、生成脚本、校验语法、调用 AIDevOps | 查询 GPU、下载模型、运行 benchmark、解析日志 |

### 三层体系总览

本项目的工具分为三个层级：

| 层 | 调用者 | 定位 | 文档 |
|----|--------|------|------|
| **Agent Tool Use** | LLM 推理循环 | Agent 决策工具 | `Tool_use层设计.md` |
| **Test Utility** | pytest / shell 脚本 | 测试运行时的共享库 | 本文档 |
| **System Environment** | 操作系统 / Shell | 透明系统级工具（RTK、rocminfo 等） | `Tool_use层设计.md` 第 9 章 |

三层之间互不感知，各司其职。

---

## 2. 工具函数总览

### 2.1 环境查询类

| 函数名 | 中文描述 | 典型能力 |
|--------|----------|----------|
| `query_rocm_version` | 查询当前 ROCm 版本 | 读取 `/opt/rocm`、执行 `rocminfo`、`rocm-smi` |
| `query_gpu_info` | 查询 GPU 数量、名称、显存、可见设备 | `rocm-smi`、`rocminfo`、`torch.cuda` |
| `check_torch_cuda_available` | 检查 PyTorch ROCm/CUDA interface 是否可用 | `torch.cuda.is_available()` |
| `check_rocm_tools` | 检查 `rocminfo`、`rocm-smi`、`hipcc` 等工具是否存在 | shell command check |
| `check_docker_available` | 检查 Docker 是否安装、daemon 是否可用、当前用户是否有权限 | `docker info` |
| `check_network_access` | 检查 Hugging Face、GitHub、Artifactory 是否可达 | HTTP HEAD / ping |
| `check_disk_space` | 检查模型、数据集、Docker 镜像所需磁盘空间 | filesystem stat |
| `check_python_env` | 检查 Python、pip、venv、关键 package | Python import / pip list |
| `check_required_env_vars` | 检查 token 和运行变量是否存在 | `HF_TOKEN`、`ROCR_VISIBLE_DEVICES` 等 |

**在测试脚本中的典型用法**：

```python
from rocm_test_utils import query_gpu_info, check_disk_space

def test_gpu_available():
    info = query_gpu_info()
    assert info.device_count >= 1, "需要至少一张 GPU"
    assert "Navi" in info.device_names[0], "需要 Navi 架构 GPU"
```

### 2.2 资产下载类

| 函数名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `download_hf_model` | 从 Hugging Face 下载模型 | `repo_id`、`revision`、`files`、`local_dir` |
| `download_hf_dataset` | 从 Hugging Face 下载数据集 | `dataset_id`、`split`、`local_dir` |
| `download_artifactory_asset` | 从 AMD Artifactory 下载模型、数据集、wheel、zip/tar | `url`、`dest`、`extract` |
| `download_http_asset` | 下载普通 HTTP/HTTPS 文件 | `url`、`dest` |
| `verify_asset_checksum` | 校验下载文件完整性 | `path`、`checksum` |
| `extract_archive` | 解压 zip、tar、tar.gz、tgz | `archive_path`、`dest` |
| `link_cached_asset` | 将缓存模型或数据链接到 workload 目录 | `source`、`target` |

**在测试脚本中的典型用法**：

```python
from rocm_test_utils import download_hf_model, verify_asset_checksum

@pytest.fixture(scope="module")
def model():
    path = download_hf_model("Qwen/Qwen2.5-7B-Instruct-GGUF", local_dir="/tmp/models")
    verify_asset_checksum(path, checksum="sha256:...")
    return path
```

**实际来源示例**：

- `test_case/suites/text_generation/test_vllm.sh` 中有 Hugging Face 模型、ShareGPT 数据集和 Artifactory 模型下载。
- `test_case/suites/rocm/test_resnet_training.sh` 中有 ImageNet 数据集下载。
- `rocm-on-radeon/in-development/cpp_rocm_llm_inf/utils/environment_builder.py` 使用 `hf_hub_download` 和 `snapshot_download`。
- `rocm-on-radeon/model-scripts/pyt_migx_llm_inf/constants.py` 中有 Artifactory 模型映射。

### 2.3 仓库和源码类

| 函数名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `clone_repo` | clone GitHub、GitLab 或内部镜像仓库 | `url`、`branch`、`commit`、`dest` |
| `checkout_repo_ref` | 切换到指定分支、tag 或 commit | `repo_path`、`ref` |
| `update_repo` | 更新已存在仓库 | `repo_path`、`strategy` |
| `build_from_source` | 源码编译 workload 依赖 | `repo_path`、`build_system`、`flags` |
| `apply_source_patch` | 对外部源码做受控 patch | `repo_path`、`patch` |

**实际来源示例**：

- `test_case/suites/rocm/test_rocpydecode.sh` clone ROCm `rocPyDecode`。
- `test_case/suites/rocm/test_hipfort.sh` clone ROCm `hipfort`。
- `test_case/suites/rocm/test_rccl.sh` clone `rccl` 和 `rccl-tests`。
- `test_case/suites/rocm/test_resnet_training.sh` clone `tinygrad`。
- `rocm-on-radeon` 的 ComfyUI、vLLM、llama.cpp、LLaMA-Factory、torch_migraphx 场景需要 clone 或源码构建。

### 2.4 依赖安装类

| 函数名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `install_pip_requirements` | 安装 `requirements.txt` | `requirements_path`、`venv_path`、`extra_index_url` |
| `install_pip_package` | 安装单个 pip 包或 wheel | `package`、`version`、`index_url` |
| `install_system_packages` | 安装 apt/dnf 系统包 | `packages`、`manager` |
| `setup_python_venv` | 创建或复用 Python 虚拟环境 | `venv_path`、`python_version` |
| `install_rocm_package` | 安装 ROCm 组件包 | `package`、`version` |
| `install_llama_cpp_python_rocm` | 安装带 ROCm/HIP 编译参数的 llama-cpp-python | `cmake_args` |

**实际来源示例**：

- `rocm-on-radeon` 中存在大量 `requirements.txt`。
- `rocm-on-radeon/in-development/cpp_rocm_llm_inf/README.md` 描述 llama-cpp-python ROCm 构建。
- `test_case/suites/rocm/test_rocm_bandwidth_test.sh`、`test_bandwidth.sh`、`test_rsmitst.sh` 会安装 ROCm 测试包。
- `test_case/test_controller.py` 的 Docker 路径中会安装 `bc`、`psutil`、`requests`。

### 2.5 Docker 类

| 函数名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `check_docker_image` | 检查本地是否已有镜像 | `image`、`tag` |
| `docker_pull_image` | 拉取 Docker 镜像 | `image`、`tag`、`registry` |
| `docker_build_image` | 根据 Dockerfile 构建镜像 | `dockerfile`、`context`、`tag` |
| `docker_run_test_case` | 用 Docker 运行 `test_case` 用例 | `suite`、`test`、`image`、`devices`、`volumes` |
| `docker_run_workload` | 在容器里运行 `rocm-on-radeon` workload | `image`、`command`、`env` |
| `generate_docker_env_file` | 从环境配置生成 Docker env file | `source_env`、`output_path` |
| `cleanup_docker_artifacts` | 清理测试产生的容器、临时文件或权限问题 | `paths`、`containers` |

**实际来源示例**：

- `test_case/test_controller.py` 支持 `RUN_TYPE=dockerrun`、`DOCKER_IMAGE`、`DEVICE_NAME`、`VOLUME_PATH`、`MEMORY`、`GPUS`。
- `test_case/test_controller.py` 的 Docker 路径会挂载 workspace、`/etc/profile.d/`、`/mnt`，并透传设备。
- `rocm-on-radeon/semi-automated-scripts/vllm_rocm_llama3_inf/Dockerfile` 是 Docker 构建来源。
- `rocm-on-radeon/model-scripts/vllm_rocm_llm_inf/run.sh` 有 Docker 参数和镜像配置。

**安全注意**：Docker GPU 透传、host network、capability、security option 都是高风险动作，测试脚本中需要人工确认。

### 2.6 Workload 运行类

| 函数名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `run_test_case` | 通过 `test_controller.py` 执行单个测试用例 | `suite`、`test`、`dynamic_vars` |
| `run_test_suite` | 通过 `test_controller.py` 执行整个 suite | `suite`、`dynamic_vars` |
| `run_rocm_workload` | 直接运行 `rocm-on-radeon` workload 做开发验证 | `workload_id`、`args`、`env` |
| `run_model_inference` | 运行模型推理 workload | `model_name`、`precision`、`devices` |
| `run_model_training` | 运行模型训练 workload | `model_name`、`dataset`、`devices` |
| `run_vllm_benchmark` | 运行 vLLM throughput / latency benchmark | `model_name`、`num_prompts`、`devices` |
| `run_llama_cpp_benchmark` | 运行 llama.cpp / llama-bench 场景 | `model_name`、`ngl`、`threads` |
| `run_component_test` | 运行 ROCm 组件测试 | `component`、`args` |
| `run_performance_benchmark` | 运行性能基准 | `benchmark`、`args` |

**注意**：

- `run_rocm_workload` 是开发辅助工具，最终入库验证应尽量使用 `run_test_case`。
- `run_test_suite`、训练、大模型、多 GPU、overnight benchmark 都必须人工确认。

### 2.7 结果解析类

| 函数名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `parse_junit_result` | 解析 JUnit XML | `xml_path` |
| `parse_case_log` | 解析 `test_case` 日志 | `log_path` |
| `extract_result_block` | 提取 `BEGIN RESULTS` / `END RESULTS` 中的结果块 | `log_path` |
| `extract_inference_metrics` | 提取推理耗时、吞吐、latency、token 数 | `log_path`、`patterns` |
| `extract_training_metrics` | 提取训练耗时、loss、accuracy | `log_path` |
| `parse_rocm_info` | 解析 `rocminfo` 输出 | `text` |
| `parse_rocm_smi` | 解析 `rocm-smi` 输出 | `text` |

**在测试脚本中的典型用法**：

```python
from rocm_test_utils import extract_inference_metrics

def test_vllm_throughput():
    log = run_vllm_benchmark("Qwen/Qwen2.5-7B", num_prompts=100)
    metrics = extract_inference_metrics(log)
    assert metrics["throughput"] > 100  # tokens/s
    assert metrics["ttft"] < 200  # ms
```

**实际来源示例**：

- `test_case` 使用 JUnit XML 和 suite logs。
- `rocm-on-radeon` 多个脚本输出 `BEGIN RESULTS` / `END RESULTS`。
- vLLM 场景关注 throughput、latency、prompt 数、输出 token。
- LLM/MIGraphX 场景关注 inference time、input tokens、output tokens、TTFT。

---

## 3. 推荐接口草案

### 3.1 `query_gpu_info()`

```python
def query_gpu_info(
    backend: Literal["rocm", "cuda", "auto"] = "auto",
    devices: Optional[str] = None,
) -> GPUInfo:
    """查询 GPU 数量、名称、显存和当前可见设备。

    Args:
        backend: rocm / cuda / auto
        devices: 可选，例如 "0,1"

    Returns:
        GPUInfo 包含:
        - gpu_available: bool
        - device_count: int
        - devices: list[int]
        - device_names: list[str]
        - visible_env: str | None
        - skip_reason: str | None
    """
```

### 3.2 `download_hf_model()`

```python
def download_hf_model(
    repo_id: str,
    revision: Optional[str] = None,
    files: Optional[list[str]] = None,
    local_dir: Optional[str] = None,
    token_env: str = "HF_TOKEN",
    dry_run: bool = True,
) -> DownloadResult:
    """从 Hugging Face 下载模型文件。

    Args:
        repo_id: 模型仓库，例如 "Qwen/Qwen2.5-7B-Instruct-GGUF"
        revision: 分支、tag 或 commit
        files: 指定文件列表，可为空表示全部
        local_dir: 本地保存目录
        token_env: token 环境变量名，默认 HF_TOKEN
        dry_run: 是否只生成计划

    Returns:
        DownloadResult 包含:
        - status: "planned" | "downloaded" | "skipped" | "failed"
        - local_dir: str
        - downloaded_files: list[str]
        - requires_token: bool
        - estimated_size_gb: float
        - human_confirm_required: bool
    """
```

### 3.3 `download_artifactory_asset()`

```python
def download_artifactory_asset(
    url: str,
    dest: str,
    extract: bool = False,
    checksum: Optional[str] = None,
    dry_run: bool = True,
) -> DownloadResult:
    """从 AMD Artifactory 下载模型、数据集、wheel 或工具包。"""
```

### 3.4 `clone_repo()`

```python
def clone_repo(
    url: str,
    dest: str,
    branch: Optional[str] = None,
    commit: Optional[str] = None,
    depth: Optional[int] = None,
    recursive: bool = False,
    dry_run: bool = True,
) -> RepoResult:
    """拉取外部源码仓库。

    Returns:
        - status: str
        - repo_path: str
        - checked_out_ref: str
        - human_confirm_required: bool
    """
```

### 3.5 `install_pip_requirements()`

```python
def install_pip_requirements(
    requirements_path: str,
    venv_path: Optional[str] = None,
    python: Optional[str] = None,
    extra_index_url: Optional[str] = None,
    constraints: Optional[str] = None,
    dry_run: bool = True,
) -> InstallResult:
    """安装 workload 的 Python 依赖。

    Returns:
        - status: str
        - command_summary: str
        - log_path: str
        - human_confirm_required: bool
    """
```

### 3.6 `install_system_packages()`

```python
def install_system_packages(
    packages: list[str],
    manager: Literal["apt", "dnf"] = "apt",
    dry_run: bool = True,
) -> InstallResult:
    """安装系统包。"""
```

### 3.7 `docker_run_test_case()`

```python
def docker_run_test_case(
    suite: str,
    test: str,
    image: str,
    dynamic_vars: Optional[dict] = None,
    devices: Optional[list[str]] = None,
    volumes: Optional[list[str]] = None,
    memory: Optional[str] = None,
    gpus: Optional[str] = None,
    dry_run: bool = True,
) -> DockerResult:
    """使用 Docker 路径运行 test_case 测试用例。

    Returns:
        - status: str
        - docker_command_summary: str
        - junit_path: str
        - log_path: str
        - human_confirm_required: bool
    """
```

### 3.8 `run_test_case()`

```python
def run_test_case(
    suite: str,
    test: str,
    dynamic_vars: Optional[dict] = None,
    junit: bool = True,
    package: Optional[str] = None,
    verbose: bool = False,
    timeout_seconds: Optional[int] = None,
) -> RunResult:
    """通过 test_controller.py 运行单个测试用例。

    Returns:
        - status: str
        - exit_code: int
        - junit_path: str
        - log_path: str
        - stdout_path: str
        - stderr_path: str
    """
```

### 3.9 `parse_junit_result()`

```python
def parse_junit_result(xml_path: str) -> JUnitResult:
    """解析 JUnit XML，汇总测试结果。

    Returns:
        - total: int
        - passed: int
        - failed: int
        - skipped: int
        - errors: int
        - failed_cases: list[str]
    """
```

---

## 4. 项目和来源映射

### 4.1 来自 `test_case` 的能力

| 来源 | 可抽象工具函数 |
|------|----------------|
| `test_controller.py list` | 发现能力，此部分归 Agent Tool Use |
| `test_controller.py run` | `run_test_case`、`run_test_suite` |
| `RUN_TYPE=dockerrun` | `docker_run_test_case` |
| `-d KEY=VALUE` | 动态变量，`run_test_case.dynamic_vars` 参数 |
| `-j -p -v` | `parse_junit_result` |
| `suites/lib.sh` | Shell 测试公共函数，对应 Shell 版 utility |
| `suites/shunit2` | Shell 测试框架 |
| `suites/rocm/test_rocminfo*.sh` | `query_rocm_version`、`parse_rocm_info` |
| `suites/rocm/test_rocm_smi.sh` | `query_gpu_info`、`parse_rocm_smi` |
| `suites/text_generation/test_vllm.sh` | `download_hf_model`、`download_hf_dataset`、`run_vllm_benchmark` |
| `suites/rocm/test_resnet_training.sh` | `download_artifactory_asset`、`clone_repo`、`install_pip_package` |
| `utils/artifact_uploader.py` | 产物上传 |

### 4.2 来自 `rocm-on-radeon` 的能力

| 来源 | 可抽象工具函数 |
|------|----------------|
| `model-scripts/**/run.sh` | `run_rocm_workload` |
| `model-scripts/**/requirements.txt` | `install_pip_requirements` |
| `in-development/cpp_rocm_llm_inf/utils/environment_builder.py` | `download_hf_model`、`query_gpu_info` |
| `model-scripts/pyt_migx_llm_inf/constants.py` | `download_artifactory_asset` |
| `semi-automated-scripts/**/Dockerfile` | `docker_build_image` |
| vLLM workload | `run_vllm_benchmark`、`docker_run_workload` |
| llama.cpp workload | `install_llama_cpp_python_rocm`、`run_llama_cpp_benchmark` |
| 输出结果块 | `extract_result_block`、`extract_inference_metrics` |

---

## 5. 优先级建议

### P0：核心工具（测试脚本基础能力）

- `query_rocm_version`
- `query_gpu_info`
- `check_torch_cuda_available`
- `check_disk_space`
- `check_network_access`
- `parse_junit_result`
- `parse_case_log`
- `extract_result_block`
- `extract_inference_metrics`

### P1：资产和运行工具

- `download_hf_model`
- `download_hf_dataset`
- `download_artifactory_asset`
- `extract_archive`
- `run_test_case`
- `run_model_inference`
- `run_vllm_benchmark`

### P2：高级和风险工具

- `clone_repo`
- `build_from_source`
- `install_pip_requirements`
- `install_system_packages`
- `docker_pull_image`
- `docker_build_image`
- `docker_run_test_case`
- `docker_run_workload`
- `run_model_training`
- `run_performance_benchmark`

---

## 6. 项目结构建议

```
rocm_test_utils/
├── __init__.py              # 统一导出
├── env/
│   ├── __init__.py
│   ├── gpu.py               # query_gpu_info
│   ├── rocm.py              # query_rocm_version
│   ├── docker.py            # check_docker_available
│   └── network.py           # check_network_access
├── download/
│   ├── __init__.py
│   ├── huggingface.py       # download_hf_model / dataset
│   ├── artifactory.py       # download_artifactory_asset
│   └── http.py              # download_http_asset
├── repo/
│   ├── __init__.py
│   ├── clone.py             # clone_repo
│   └── build.py             # build_from_source
├── install/
│   ├── __init__.py
│   ├── pip.py               # install_pip_requirements
│   ├── system.py            # install_system_packages
│   └── venv.py              # setup_python_venv
├── run/
│   ├── __init__.py
│   ├── test_controller.py   # run_test_case
│   ├── vllm.py              # run_vllm_benchmark
│   └── workload.py          # run_rocm_workload
├── parse/
│   ├── __init__.py
│   ├── junit.py             # parse_junit_result
│   ├── log.py               # extract_result_block
│   └── metrics.py           # extract_inference_metrics
└── shell/
    └── lib.sh               # Shell 版公共函数 (对应 test_case/suites/lib.sh)
```
