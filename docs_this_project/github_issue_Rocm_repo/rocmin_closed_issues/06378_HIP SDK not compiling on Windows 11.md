# HIP SDK not compiling on Windows 11

- **Issue #:** 6378
- **State:** closed
- **Created:** 2026-06-23T19:24:56Z
- **Updated:** 2026-06-29T13:14:33Z
- **Labels:** status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6378

After requesting support from AMD's website, I was reffered to come here and opening an issue

After installing the HIP SDK For Windows, and adding libraries' directories to PATH, VSCode (I do not have VS22) has not found the files, which had to be fixed by copying the AMD\ROCm\ folder, and placing next to the C++ code files in File Explorer.

Then, after setting properties of the workspace, the libraries and binaries were found by VSCode, after which there were an error that came up when compiling, not allowing the code (test code I copied from the HIP-Examples repository, link below) to run. The errors shown by VSCode seemed to not be the issue, but files in the installation from the SDK, saying that the device (an RX 9070 that I have bought for HIP) was not supported, but the same card works well when tested under load, and AMD:Adrenalin shows no problems. I could not find the exact source of the fault, as I have no other hardware that can run HIP, and I could not find HIP (or ROCm) documentation online for Windows.

Repository link : https://github.com/ROCm/HIP-Examples/blob/master/vectorAdd/vectoradd_hip.cpp

Error message : 

<img width="2079" height="211" alt="Image" src="https://github.com/user-attachments/assets/acfd0c64-d846-4f2e-8de5-7613461da5c8" />