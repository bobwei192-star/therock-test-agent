# [Feature Request]: Official Windows ONNX Runtime / ROCm support for Ryzen AI MAX+ 395 laptops (Radeon 8060S / gfx1151)

> **Issue #6294**
> **状态**: open
> **创建时间**: 2026-05-22T10:28:07Z
> **更新时间**: 2026-05-26T15:38:48Z
> **作者**: AIwork4me
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/6294

## 标签

- **Feature Request** (颜色: #fbca04)

## 负责人

- schung-amd

## 描述

### Problem Description

I am filing this as a customer feature request from the perspective of a Windows laptop user who purchased a Ryzen AI MAX+ 395 machine specifically for local AI inference and AI developer workloads.

My laptop is an **ASUS ProArt PX13 HN7306EA** with **AMD Ryzen AI MAX+ 395 w/ Radeon 8060S**. This is exactly the kind of premium AI PC product that many developers expect to use for local ONNX inference, computer vision, OCR, small model serving, and edge AI experimentation on Windows.

However, in practice, I currently do not have a usable official AMD GPU path for **ONNX Runtime GPU inference on Windows**. In my Windows environment, ONNX Runtime exposes only CPU/Azure providers:

```text
onnxruntime providers: ['AzureExecutionProvider', 'CPUExecutionProvider']
```

When I explicitly require ROCm/MIGraphX GPU execution in a real ONNX validation workload, it fails immediately:

```text
Requested ONNX provider 'rocm' is unavailable.
Available providers: AzureExecutionProvider, CPUExecutionProvider
```

This is not a model issue. The same workload runs correctly on CPU and validates against Paddle native CPU inference. The blocker is that there is no clear, official, supported Windows path for using the Radeon 8060S GPU through ROCm/MIGraphX/ONNX Runtime on a Ryzen AI MAX+ 395 laptop.

As a customer, this is a major gap. AMD is selling Ryzen AI MAX+ 395 laptops as high-end AI PC products, but Windows developers cannot easily use the integrated Radeon 8060S for one of the most common inference deployment APIs: **ONNX Runtime**.

Competing ecosystems have much clearer Windows laptop inference stories:

- NVIDIA users can use CUDA-backed ONNX Runtime / TensorRT workflows on many Windows laptops.
- Intel AI PC users can use OpenVINO on Windows.
- AMD Ryzen AI MAX+ 395 users currently have no similarly clear Windows ROCm/MIGraphX ONNX Runtime path.

This leaves customers who paid for AMD's flagship AI PC silicon forced back to CPU for ONNX inference.

There is already related demand and friction for this silicon family in #6157, where another Ryzen AI MAX+ 395 / Radeon 8060S user reports ROCm instability on Linux with gfx1151. My request here is specifically focused on the **Windows AI PC customer experience**: please provide an official, documented, stable Windows support path for ONNX Runtime GPU inference on Ryzen AI MAX+ 395 / Radeon 8060S laptops.

### Why Windows support matters

Many Ryzen AI MAX+ 395 laptops are purchased as Windows machines. The target customer is not only a Linux workstation user; it is also:

- an AI application developer building Windows desktop apps;
- an ISV validating ONNX models on consumer/prosumer AI PCs;
- a researcher or student using a laptop as their primary machine;
- a local inference user who expects the integrated Radeon GPU to accelerate models;
- an open-source developer trying to support AMD AI PC users without requiring a full Linux workstation setup.

For these users, saying \"use CPU\" or \"try an unsupported Linux workaround\" is not enough. The Windows experience matters because Windows is the default OS for many AIPC laptops.

ONNX Runtime is a key deployment layer for this audience. OCR, vision models, embeddings, document AI, audio models, and many edge AI workflows are commonly exported to ONNX. If ROCm/MIGraphX does not provide a usable Windows path here, AMD's best AI PC hardware becomes difficult to recommend for practical ONNX inference development.

### Local hardware/software configuration

Detected locally on my Windows machine:

```text
Laptop: ASUS ProArt PX13 HN7306EA
CPU: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
CPU cores/threads: 16 cores / 32 logical processors
GPU: AMD Radeon(TM) 8060S Graphics
GPU device ID: PCI\VEN_1002&DEV_1586&SUBSYS_17141043&REV_C1
GPU driver: 32.0.22032.6002, driver date 2025-12-15
Memory: 132,766,306,304 bytes (~128 GB)
OS: Microsoft Windows 11 Home China, Version 10.0.26200, 64-bit
BIOS: ASUS HN7306EA.307, 2026-01-26
```

Python / inference environment:

```text
uv: 0.11.16
Python: 3.10.20
onnxruntime: 1.20.1
onnxruntime providers: ['AzureExecutionProvider', 'CPUExecutionProvider']
paddlepaddle: 3.3.0 CPU
numpy: 2.2.6
opencv-python: 4.13.0
rocm-smi: not available on this Windows environment
WSL Linux distro: not installed on this machine at the time of testing
```

### Repro workload

I built a small PP-OCRv6 ONNX Runtime validation project to compare:

1. Paddle native CPU inference (`paddlepaddle==3.3.0`, CPU build)
2. ONNX Runtime CPU inference
3. ONNX Runtime GPU inference requiring ROCm/MIGraphX

The OCR model and pipeline are valid. Paddle CPU and ONNX Runtime CPU produce matching text output.

Command used for precision validation:

```powershell
uv run python scripts/verify_accuracy.py --include-paddle --include-gpu --gpu-provider rocm
```

Result summary:

```text
ort_cpu:    ran successfully on 8 images / 268 detected text lines
paddle_cpu: ran successfully on 8 images / 268 detected text lines
ort_gpu:    unavailable: Requested ONNX provider 'rocm' is unavailable.
            Available providers: AzureExecutionProvider, CPUExecutionProvider

ort_cpu vs paddle_cpu:
- text output: 268 / 268 lines matched
- all 8 test images passed
- max score drift: 2.567e-03
- max detection box drift: 3 px
```

This is important because it shows the model, preprocessing, postprocessing, and validation workload are healthy. The missing piece is the AMD GPU ONNX Runtime path on Windows for this Ryzen AI MAX+ 395 laptop.

Benchmark command:

```powershell
uv run python scripts/benchmark.py --include-paddle --include-gpu --gpu-provider rocm --iterations 3
```

Benchmark summary from this run:

```text
ort_cpu avg:     336.90 ms
paddle_cpu avg: 3757.62 ms
ort_gpu: unavailable, because no ROCm/MIGraphX provider is exposed
```

The CPU path is functional, but it is not what customers expect from a flagship AMD AI PC laptop with Radeon 8060S graphics and large unified memory.

### Expected behavior / requested Windows support

Please provide an official Windows support path for **Ryzen AI MAX+ 395 / Radeon 8060S / gfx1151-class AIPC products** that includes:

1. A clear ROCm / MIGraphX / ONNX Runtime support matrix entry for Ryzen AI MAX+ 395 and Radeon 8060S on Windows.
2. A supported ONNX Runtime GPU provider path on Windows, preferably through `MIGraphXExecutionProvider` or the appropriate AMD provider going forward.
3. Exact installation documentation for Windows users: AMD driver version, ROCm/MIGraphX runtime package if applicable, Python version, ONNX Runtime wheel source, and known limitations.
4. If native Windows ROCm support is not planned, please document the official WSL2 path for Ryzen AI MAX+ 395 laptops and provide validated steps.
5. A minimal Windows validation sample using a common ONNX model so customers can verify that the AMD GPU provider is active and not silently falling back to CPU.
6. A roadmap or ETA for Ryzen AI MAX+ 395 / Radeon 8060S / gfx1151 ONNX Runtime acceleration.

I would be happy to test nightly builds, preview wheels, WSL2 instructions, or diagnostic scripts on this laptop and report results.

### ROCm Version

No usable ROCm/MIGraphX ONNX Runtime provider path is available in my current Windows laptop environment. `rocm-smi` is not available, and ONNX Runtime exposes only:

```text
AzureExecutionProvider
CPUExecutionProvider
```

### ROCm Component

Windows support for ONNX Runtime / MIGraphX / ROCm on Ryzen AI MAX+ 395 AIPC laptops, Radeon 8060S, gfx1151-class integrated GPU.

### Closing note

Ryzen AI MAX+ 395 laptops are exactly the kind of devices many developers want to use for local AI on Windows. Please make AMD's own Windows AI PC experience first-class for ONNX Runtime GPU inference. Without this, developers and customers are left with powerful AMD hardware that cannot be used through one of the most important AI deployment stacks on the platform these laptops actually ship with.


---

## 评论 (2 条)

### 评论 #1 — Kinetic-Labs-GT (2026-05-22T13:53:24Z)

This issue is being categorized as a macro-level ecosystem feature request that cannot be resolved via a localized open-source code patch or Pull Request within this repository. 

### Architectural Overview

1. **Driver-Level Prerequisites:** Official support for ROCm/MIGraphX execution providers on Windows client platforms depends on proprietary WHQL driver enablement and kernel-level runtime libraries (`amdkcl`/`amdgpu`) engineered for the Windows display driver model (WDDM). User-space source modifications cannot bypass these fundamental operating system packaging dependencies.
2. **Upstream Distribution Dependencies:** Exposing a native `MIGraphXExecutionProvider` or specialized ROCm wheel for Windows requires formal integration pipelines with the upstream [ONNX Runtime repository](https://github.com/microsoft/onnxruntime). This includes establishing dedicated CI/CD build matrices, validating hardware intrinsics for the `gfx1151` microarchitecture, and publishing official binaries via NuGet or PyPI.
3. **Current Client Toolchain Guidance:** On Windows architectures featuring Ryzen AI Max silicon, client-side hardware acceleration for ONNX workloads is primarily engineered to interface with the `DirectMLExecutionProvider` via DirectX 12 compute queues, or the specialized AMD NPU driver stack using the ONNX Runtime QNN Execution Provider. 

### Recommended Action
To advocate for expanding native ROCm user-space framework packaging to Windows laptops, this feature tracking request should be redirected to standard product management avenues, such as the **AMD Community Forums** or formal corporate feedback channels, as it requires cross-organization runtime distribution and validation.

---

### 评论 #2 — schung-amd (2026-05-26T15:38:48Z)

Hi @AIwork4me, thanks for the input. I believe you should be able to leverage the Ryzen AI MAX+ 395 and similar processors with the Vitis AI EP; see https://onnxruntime.ai/docs/execution-providers/Vitis-AI-ExecutionProvider.html. I'll reach out internally to see if we have any ongoing efforts to enable the MIGraphX EP for ONNX on Windows for other AMD hardware. I have seen some mention of related work but am not sure of the status.

As for WSL, ideally the Linux instructions should work and the ROCm EP worked in the past pre-deprecation. However as you mention it is not well-documented whether the MIGraphX EP is supported in the same way. I'll take a look to see if this currently works and see if we can add some docs to that effect.

---
