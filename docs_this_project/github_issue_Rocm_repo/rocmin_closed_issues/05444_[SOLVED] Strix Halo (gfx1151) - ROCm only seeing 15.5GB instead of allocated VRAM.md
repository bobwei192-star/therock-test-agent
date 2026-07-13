# [SOLVED] Strix Halo (gfx1151) - ROCm only seeing 15.5GB instead of allocated VRAM

- **Issue #:** 5444
- **State:** closed
- **Created:** 2025-09-29T14:18:30Z
- **Updated:** 2026-04-27T06:56:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/5444

### Problem Description
Strix Halo systems (gfx1151) with large VRAM allocations are limited to only ~15.5GB visible memory in the ROCm/HIP runtime, despite the kernel correctly seeing the full allocation. This is affecting all users with Ryzen AI MAX+ processors trying to use the unified memory architecture for LLM workloads.

### Affected Configuration
- **Hardware:** AMD Ryzen AI MAX+ (Strix Halo) with Radeon 8060S (gfx1151)
- **Memory:** Any system with >16GB VRAM allocated (tested with 96GB allocation)
- **ROCm versions:** Affects 6.4.1 through 7.0 RC
- **Symptom:** ROCm applications can only allocate ~15.5GB despite larger VRAM allocation

### Reproduction
On any affected system with kernel ≤6.15:
```bash
# Check kernel sees full VRAM (example: 96GB)
$ cat /sys/class/drm/card*/device/mem_info_vram_total
103079215104  # 96GB in bytes

# But ROCm only sees 15.5GB
$ rocminfo | grep -A3 "Pool" | grep Size
Size:    16651264(0x3e2000) KB  # Only 15.5GB!

# HIP applications fail to allocate beyond 15.5GB
$ hipMemGetInfo  # Returns ~15.5GB total
```

### Solution
**Upgrade to kernel 6.16.9 or later.** This is a kernel-level fix, not a ROCm issue.

```bash
# Ubuntu/Debian users can use mainline kernel:
sudo add-apt-repository ppa:cappelikan/ppa
sudo apt update && sudo apt install mainline
sudo mainline --install 6.16.9
sudo update-initramfs -c -k 6.16.9-061609-generic
sudo reboot

# Fedora users:
# Install kernel 6.16.9 from rawhide or testing repos
```

### Verification After Fix
```bash
# After kernel 6.16.9:
$ uname -r
6.16.9-061609-generic

# NO kernel parameters needed!
$ cat /proc/cmdline
root=UUID=72998fb2-b0eb-4676-97c9-31ac53b5e2a5 ro quiet splash rd.luks.options=tpm2-device=auto
# Note: No amdgpu.gttsize, no ttm.pages_limit, no amd_iommu=off

$ rocminfo | grep "Size:" | grep "100663296"
      Size:                    100663296(0x6000000) KB   # 96GB visible!

# Ollama now uses full memory
$ OLLAMA_GPU_MEMORY=96GB ollama run llama3.3:70b  # Works!
```

### Technical Details
The kernel 6.16.x series appears to include fixes for:
- Unified memory architecture (UMA) handling for APUs  
- HSA memory pool detection on gfx1151
- Proper VRAM aperture mapping for Strix Halo

### Testing Configuration
- **System:** HP ZBook Ultra G1a with Ryzen AI MAX+ PRO 395
- **VRAM allocation:** 96GB (not yet tested with other allocations)
- **ROCm version:** 6.4.1 (ROCm 7.0 not yet tested)
- **Kernel tested:** 6.16.9-061609-generic on Ubuntu 24.04.1 LTS

### Expected Impact
This fix enables:
- Running 70B+ parameter models that require >15GB VRAM
- Full utilization of Strix Halo's unified memory architecture
- No performance penalties from GTT workarounds
- Native ROCm performance without hacks

### Related Discussions
- Performance issues (separate): #4748
- Community workarounds: https://strixhalo-homelab.d7.wtf/
- Framework forum: https://community.frame.work/t/amd-strix-halo-ryzen-ai-max-395-gpu-llm-performance-tests/72521

### Notes
- Kernel 6.15.x and earlier: Issue persists
- Kernel 6.16.9+: Issue resolved
- ROCm 6.4.1 works perfectly with the new kernel (7.0 not required)
- No GTT expansion parameters needed

### Community Testing Needed
Please test and report back with:
- Different VRAM allocations (32GB, 64GB, 128GB)
- Different Strix Halo systems (Framework, GMKtec, ASUS, etc.)
- ROCm 7.0 compatibility
- Other distributions (Fedora, Arch, etc.)

This fix should theoretically work for all configurations, but more testing will help confirm.

---
*System verified working: HP ZBook Ultra G1a, 128GB RAM (96GB VRAM), Ubuntu 24.04.1, ROCm 6.4.1*