# [Feature]: RISC-V and multi-arch friendly ROCm

- **Issue #:** 5629
- **State:** closed
- **Created:** 2025-11-05T06:05:09Z
- **Updated:** 2026-01-21T19:14:17Z
- **Labels:** Feature Request, status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5629

### Suggestion Description

RISC-V is now the open ISA standard overseen by ISO/IEC JTC1 and AMD cards are the open source best for AI and graphics.

Since the availability of RDNA3 open-source graphics driver, [RISC-V's quick adoption](https://riscv.org/blog/amds-fastest-gaming-gpu-now-works-with-risc-v-cpus-amd-radeon-rx-7900-xtx-open-source-linux-drivers-available/) marks that RISC-V-Radeon graphics experience now aligns with other ISAs. 

Modern commercial RISC-V CPUs equipped with PCIe 4.0+ have been long expecting a new chapter for multi-arch friendly ROCm for first-class AI experience.

Now with the devoted efforts from ISRC of ISCAS, the latest AMD ROCm 6.4.2 has been ported to multiple commercial RISC-V platforms, including UR-DP1000 (8-core desktop) and SG2044 (64-core server).

Upstreaming this work benefits RISC-V developers to use the prestigious AMD experience with the off-the-shelf and most likely future RISC-V products seamlessly.

For ROCm, ISCAS removes x86 hardcodes and refactor into a fully multi-arch friendly fashion.

Engineering results:

* Tested AMD cards include RX7900XT/XTX (20/24GB VRAM), W7900pro (48GB VRAM), MI200(64GB)

* Tested RISC-V platforms include UR-DP1000 (Milk-V Titan board, Rongda M-ATX and EVB) and SG2044
* Performance with some existing models:

![Image](https://github.com/user-attachments/assets/1e7b0280-1191-4e96-ab5a-ec3f1e3e56d3)

Ecosystem catch-ups:

* Fedora 42 has already shipped with this downstream ROCm RISC-V port and developers are thrilled to use these advancements.
* ISCAS has tested also on Debian and OpenEuler

Maintenance and on-goings:

* UltraRISC donates necessary boards to ISCAS to CI/CD future ROCm versions on supported RISC-V platforms and fix regressions
* ISCAS would jointly work with hardware providers to resolve bugs in RISC-V realm and keep RISC-V code in ROCm multi-arch clean

Co-signers for this upstreaming request: 

* Research Institutes and Universities: ISCAS, Shanghai Jiaotong University;

* Chip vendors: UltraRISC;

* Operating systems: Fedora; 

* Solutions: Milk-V;

We are looking forward to the ROCm community's opinions.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_