# Status of non-amd64 arch support? (arm64, power9, etc.)

- **Issue #:** 1825
- **State:** closed
- **Created:** 2022-10-07T20:09:40Z
- **Updated:** 2024-05-09T16:28:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1825

I'm just trying to get OpenCL working on a power9 computer, I can't seem to find any information anywhere concerning what architectures are supported other than amd64. 

This guide seems to suggest that version 3.5 mostly worked on power9: https://systems.nic.uoregon.edu/internal-wiki/index.php?title=Rocm_on_power9

However building a somewhat-recent version like 5.1.3 fails, amongst other things including a message about  -DNO_WARN_X86_INRINSICS, so I'm guessing that somewhere along the way ROCm was changed to no longer be architecture-agnostic.