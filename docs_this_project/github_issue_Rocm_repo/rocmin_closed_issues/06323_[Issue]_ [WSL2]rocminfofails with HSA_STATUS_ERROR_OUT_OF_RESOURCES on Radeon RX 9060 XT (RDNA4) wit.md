# [Issue]: [WSL2]rocminfofails with HSA_STATUS_ERROR_OUT_OF_RESOURCES on Radeon RX 9060 XT (RDNA4) with Windows 10 despite official OS support claim

- **Issue #:** 6323
- **State:** closed
- **Created:** 2026-06-02T14:43:12Z
- **Updated:** 2026-06-06T11:09:23Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6323

### Problem Description

System Environment

Windows version: Windows 10 Pro 22H2 (OS Build 19045.6456)

WSL version: WSL 2 (kernel 5.10.16.3-microsoft-standard-WSL2)

Linux distro (in WSL): Ubuntu 26.04 LTS (Resolute Raccoon) — also tested with Ubuntu 24.04 (Noble)

GPU: AMD Radeon RX 9060 XT (RDNA4, gfx1200)

AMD Windows driver tested:

Adrenalin 26.5.2 (standard game‑ready)

Adrenalin 26.2.2 (the version that introduced ROCDXG, specifically for WSL)

ROCm installation method: both via Ubuntu universe repo (rocm metapackage) and via AMD's official amdgpu-install script (--usecase=wsl,rocm --no-dkms)

Problem Description
rocminfo always fails with the following error regardless of which driver or installation method I use:

text
WSL environment detected.
hsa api call failure at: ./rocminfo.cc:1324
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
The GPU is not listed in the output. No other errors appear during installation.

Steps to Reproduce

Fresh Ubuntu 26.04 WSL2 environment (imported from official .wsl image).

Set up apt mirror (e.g., Aliyun) and sudo apt update.

Attempt A (Ubuntu repo): sudo apt install rocm → installs ROCm 7.1.0-0ubuntu6. rocminfo fails as above.

Attempt B (AMD official script):

bash
wget https://repo.radeon.com/amdgpu-install/7.2/ubuntu/noble/amdgpu-install_7.2.70200-1_all.deb
sudo apt install ./amdgpu-install_7.2.70200-1_all.deb
sudo amdgpu-install -y --usecase=wsl,rocm --no-dkms
After purging all previous ROCm packages, installation succeeds but rocminfo still fails with the same error.

Attempt C: Manually downloaded and installed hsa-runtime-rocr4wsl-amdgpu from AMD repo, then re‑ran amdgpu-install. No change.

Troubleshooting Done

User added to video and render groups.

wsl --shutdown performed after every change.

Windows drivers tested: 26.5.2 and 26.2.2 — same error persists.

Cleaned all rocm and amdgpu packages and apt sources (/etc/apt/sources.list.d/rocm.list etc.).

/dev/dxg exists.

Hyper‑V and virtualization (SVM) enabled in BIOS.

WSL kernel updated (wsl --update).

Confirmed by rocminfo that the runtime fails to allocate resources, preventing GPU detection.

Expected Behavior
rocminfo should detect the RX 9060 XT and list its properties.

Actual Behavior
rocminfo returns HSA_STATUS_ERROR_OUT_OF_RESOURCES and the GPU is not shown.

Additional Context

According to AMD's official system requirements for Windows, Windows 10 22H2 (GA) is listed as a supported OS.

The GPU is also listed as officially supported: AMD Radeon RX 9060 XT RDNA4 gfx1200 Runtime ✅ HIP SDK ✅

The amdgpu-install script I used (7.2) and the Adrenalin WSL drivers (26.2.2) were designed for Windows 11 and Ubuntu 24.04 (Noble) as the primary platform. The fact that Windows 10 22H2 is officially listed as supported but the new ROCDXG‑based drivers fail suggests a gap between the official system requirements table and the actual runtime compatibility of the WSL ROCm stack on Windows 10.

Hypothesis / Key Question
Could this be because the newer ROCDXG‑based driver stack (Adrenalin 26.x + amdgpu-install 7.x) is only fully validated on Windows 11, even though the system requirements page lists Windows 10 22H2? If so, is there any plan to restore functional WSL+ROCm support for Windows 10 22H2 with RDNA4 GPUs, or should users on Windows 10 simply be considered unsupported despite the official documentation?

Request
Please clarify the official support status:

Is Windows 10 22H2 still supported for WSL2 ROCm compute with RDNA4 GPUs (RX 9060 XT in particular)?

If yes, what specific driver + ROCm version combination is required to resolve HSA_STATUS_ERROR_OUT_OF_RESOURCES?

If no, please update the system requirements documentation to reflect that Windows 11 is the minimum required OS for WSL2+ROCm on RDNA4.
(Tips:All the text above was summarized and translated using DeepSeek. If you need any specific details or notice any discrepancies, please feel free to request them directly in this issue. However, please keep in mind that I'm not deeply familiar with the technical intricacies, so I would really appreciate it if you could provide basic instructions on how to gather the information you need.)

### Operating System

Windows 10 Pro 22H2 (OS Build 19045.6456)

### CPU

AMD Ryzen 5 5600G with Radeon Graphics

### GPU

AMD Radeon RX 9060 XT 16GB

### ROCm Version

ROCm 7.2.1

### ROCm Component

_No response_

### Steps to Reproduce

Steps

1. Launch WSL2 Ubuntu instance
2. Update package list and install basic tools
3. Set up Aliyun mirror (optional but recommended for speed)
4. Attempt A: Install ROCm from Ubuntu official repository
5. Add user to video/render groups and restart WSL
6. Run rocminfo(→ Observed error: HSA_STATUS_ERROR_OUT_OF_RESOURCES)
7. Attempt B: Install ROCm using AMD's official amdgpu-install script (ROCDXG method)

- First, completely purge previous ROCm packages
- Then install the script:

> `wget https://repo.radeon.com/amdgpu-install/7.2/ubuntu/noble/amdgpu-install_7.2.70200-1_all.deb
> sudo apt install ./amdgpu-install_7.2.70200-1_all.deb
> sudo amdgpu-install -y --usecase=wsl,rocm --no-dkms`

- Add user to groups and restart WSL again.
- Run rocminfo again → Same error persists.

8. Attempt C: Manually install hsa-runtime-rocr4wsl-amdgpu(Then re-run sudo amdgpu-install -y --usecase=wsl,rocm --no-dkms and rocminfo. But ... No change, same error.)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

WSL environment detected.
hsa api call failure at: ./rocminfo.cc:1324
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

### Additional Information

_No response_