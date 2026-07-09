# RDNA2 GPUs/iGPUs are not being enumerated with ROCm on Windows + Adrenalin 26.1.1

- **Issue #:** 5871
- **State:** closed
- **Created:** 2026-01-21T01:28:37Z
- **Updated:** 2026-04-04T13:21:52Z
- **Labels:** Windows, application:pytorch, status: triage, status: fix submitted
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5871

Update:
Update: Tested with ROCm 7.2 - Issue persists
I've installed the latest AMD Software: Adrenalin Edition 26.1.1 (released January 21, 2026) with the AI Bundle, which includes ROCm 7.2.
Results:

✅ Model still loads successfully to GPU
❌ Same crash on text generation - Python process terminates silently
❌ Same Event Viewer error:

Faulting module: amdhip64_7.dll
Exception code: 0xc0000005 (Access Violation)
System specs:

Driver: Adrenalin 26.1.1 (released today)
PyTorch: 2.9.0+rocmsdk20251116 (from AI Bundle)
ROCm: 7.2
GPU: AMD Radeon RX 7900 XTX
CPU: AMD Ryzen 9 9950X
OS: Windows 11 Build 10.0.26200

The bug has now been confirmed across ROCm 7.1.1 and 7.2 with both driver versions 25.20.01.17 and 26.1.1.

Log Name:      Application
Source:        Application Error
Date:          1/21/2026 8:01:56 PM
Event ID:      1000
Task Category: Application Crashing Events
Level:         Error
Keywords:      
User:          AORUSX870E\bruce
Computer:      AorusX870E
Description:
Faulting application name: python.exe, version: 3.12.10150.1013, time stamp: 0x67f515a7
Faulting module name: amdhip64_7.dll, version: 10.0.3581.0, time stamp: 0x69198ccb
Exception code: 0xc0000005
Fault offset: 0x00000000002ab8ba
Faulting process id: 0x3560
Faulting application start time: 0x1DC8B3A7B7F1C4E
Faulting application path: C:\Users\bruce\AppData\Local\Programs\Python\Python312\python.exe
Faulting module path: D:\text-generation-webui\venv\Lib\site-packages\_rocm_sdk_core\bin\amdhip64_7.dll
Report Id: 48a78f7a-9a69-48ac-91f8-af963f486ac6
Faulting package full name: 
Faulting package-relative application ID: 
Event Xml:
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Application Error" Guid="{a0e9b465-b939-57d7-b27d-95d8e925ff57}" />
    <EventID>1000</EventID>
    <Version>0</Version>
    <Level>2</Level>
    <Task>100</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8000000000000000</Keywords>
    <TimeCreated SystemTime="2026-01-22T01:01:56.1806364Z" />
    <EventRecordID>5007</EventRecordID>
    <Correlation />
    <Execution ProcessID="8404" ThreadID="19116" />
    <Channel>Application</Channel>
    <Computer>AorusX870E</Computer>
    <Security UserID="S-1-5-21-97673550-4160431826-3737378671-1001" />
  </System>
  <EventData>
    <Data Name="AppName">python.exe</Data>
    <Data Name="AppVersion">3.12.10150.1013</Data>
    <Data Name="AppTimeStamp">67f515a7</Data>
    <Data Name="ModuleName">amdhip64_7.dll</Data>
    <Data Name="ModuleVersion">10.0.3581.0</Data>
    <Data Name="ModuleTimeStamp">69198ccb</Data>
    <Data Name="ExceptionCode">c0000005</Data>
    <Data Name="FaultingOffset">00000000002ab8ba</Data>
    <Data Name="ProcessId">0x3560</Data>
    <Data Name="ProcessCreationTime">0x1dc8b3a7b7f1c4e</Data>
    <Data Name="AppPath">C:\Users\bruce\AppData\Local\Programs\Python\Python312\python.exe</Data>
    <Data Name="ModulePath">D:\text-generation-webui\venv\Lib\site-packages\_rocm_sdk_core\bin\amdhip64_7.dll</Data>
    <Data Name="IntegratorReportId">48a78f7a-9a69-48ac-91f8-af963f486ac6</Data>
    <Data Name="PackageFullName">
    </Data>
    <Data Name="PackageRelativeAppId">
    </Data>
  </EventData>
</Event>

### Problem Description

Sharing my experience getting oobabooga running on AMD 7900 XTX with Windows. Got very close but hit an AMD bug. Documenting for others.

AMD Radeon RX 7900 XTX + Windows 11 + ROCm 7.1.1: Model Loads Successfully, Crashes on Text Generation

TL;DR: Model loads to GPU perfectly, crashes immediately on first generation attempt. Root cause: HIP runtime bug in amdhip64_7.dll. Awaiting AMD fix.
Hardware/Software Configuration

GPU: AMD Radeon RX 7900 XTX (24GB VRAM)
OS: Windows 11
Driver: AMD Software PyTorch Edition 25.20.01.17 (driver store version 32.0.22001.17002)
Python: 3.12.10
PyTorch: 2.9.0+rocmsdk20251116 (ROCm 7.1.1)
oobabooga: Latest main branch (January 2026)

Installation Steps & Reproduction
1. Install Python 3.12

Download from python.org
During install, check "Add Python to PATH" and "Disable path length limit"

2. Clone oobabooga
cmdcd D:\
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
3. Create virtual environment
cmdpython -m venv venv
venv\Scripts\activate.bat
4. Install oobabooga base requirements
cmdpip install -r requirements\full\requirements.txt
5. Install ROCm SDK + PyTorch (in the activated venv)
cmdpip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/rocm_sdk_core-0.1.dev0-py3-none-win_amd64.whl

pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/rocm_sdk_devel-0.1.dev0-py3-none-win_amd64.whl

pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/rocm_sdk_libraries_custom-0.1.dev0-py3-none-win_amd64.whl

pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/rocm-0.1.dev0.tar.gz

pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torch-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl

pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchaudio-2.9.0+rocmsdk20251116-cp312-cp312-win_amd64.whl

pip install --no-cache-dir https://repo.radeon.com/rocm/windows/rocm-rel-7.1.1/torchvision-0.24.0+rocmsdk20251116-cp312-cp312-win_amd64.whl
6. Verify PyTorch sees GPU
cmdpython -c "import torch; print(torch.cuda.is_available())"
python -c "import torch; print(torch.cuda.get_device_name(0))"
Expected output: True and AMD Radeon RX 7900 XTX
7. Start oobabooga
cmdpython server.py
8. Reproduce the crash

Open browser to http://127.0.0.1:7860/
Go to Model tab
In "Download model or LoRA", enter: mistralai/Mistral-7B-Instruct-v0.2
Click Download (wait for completion, ~15GB)
Select the model from dropdown
Model loader: Transformers
attn-implementation: eager (or sdpa, both crash)
Click Load → ✅ Succeeds ("Successfully loaded" message appears)
Go to Chat tab
Type any message (e.g., "Hello")
Click Generate → ❌ Python crashes silently
Check Windows Event Viewer for amdhip64_7.dll crash

What Works ✅

PyTorch correctly detects 7900 XTX
Model downloads successfully
Model loads to GPU successfully (completes in ~22 seconds)
Shows "Successfully loaded" message

What Fails ❌

Text generation crashes immediately on first GPU compute
Python process terminates with no console error
Windows Event Viewer shows amdhip64_7.dll access violation

### Root Cause
**Windows Event Viewer shows:**
```
Faulting module: amdhip64_7.dll (version 10.0.3581.0)
Exception code: 0xc0000005 (Access Violation)
Fault offset: 0x00000000002ab8ba
Module path: D:\text-generation-webui\venv\Lib\site-packages\_rocm_sdk_core\bin\amdhip64_7.dll

This is AMD's HIP runtime library crashing during the first GPU compute operation.
Attempted Fixes That Don't Help

❌ Disabling Windows TDR (registry edits to TdrDelay, TdrLevel)
❌ Changing attention implementation (eager vs sdpa)
❌ Environment variables (HSA_OVERRIDE_GFX_VERSION, HSA_ENABLE_SDMA=0, AMD_DIRECT_DISPATCH=0)
❌ Different models or quantization levels
❌ Lowering truncation length

Status
This appears to be a known bug in ROCm 7.1.1 for Windows with RDNA3 GPUs (similar crashes reported in llama.cpp GitHub issues #17429).
The good news: We're extremely close - model loading works perfectly. This should be fixed in the next AMD driver/ROCm release.
Workarounds:

Wait for AMD driver update (25.30.x or ROCm 7.2+)
Dual-boot Linux - ROCm works perfectly on Linux
CPU-only mode - Set CUDA_VISIBLE_DEVICES=-1 (slow but functional)

For AMD/ROCm Team
If you need additional diagnostics (core dumps, debug logs, etc.) from a Windows 11 + 7900 XTX setup, happy to provide them.



### Operating System

window 11 OS Version: 10.0.26200

### CPU

CPU: AMD Ryzen 9 9950X 16-Core Processor

### GPU

AMD Radeon(TM) Graphics AMD Radeon RX 7900 XTX

### ROCm Version

ROCm: 7.1.52802-561cc400e1 PyTorch: 2.9.0+rocmsdk20251116

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_