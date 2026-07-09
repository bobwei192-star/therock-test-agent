# hsa_signal_wait_acquire() doesn't return on /opt/rocm/hsa/sample/vector_copy

- **Issue #:** 13
- **State:** closed
- **Created:** 2016-06-06T06:51:24Z
- **Updated:** 2018-10-25T00:35:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/13

cont. https://github.com/RadeonOpenCompute/hcc/issues/71

["verify-installation"](https://github.com/RadeonOpenCompute/ROCm#verify-installation) step doesn't succeed because hsa_signal_wait_acquire() doesn't return.

Environment is following:
- Ubuntu 14.04.4
- Core i7-3770K
- AMD Radeon R9 FuryX
- DDR3-1600 2GBx4

Steps to reproduce are following:
1. Clean-install ubuntu 14.04.4 ("Erase disk and install ubuntu")
2. Boot normally, and I got "low level graphic mode" (this is expected for FuryX, right?).
3. Enter console mode with "Ctrl+Alt+F1".
4. Install hcc; following https://github.com/RadeonOpenCompute/ROCm#add-the-rocm-apt-repository
5. reboot
6. Enter console mode again
7. export PATH=${PATH}:/opt/rocm/bin
8. cp -r /opt/rocm/hsa/sample/ ~/sample
9. cd ~/sample
10. make
11. ./vector_copy output following but doesn't finish.

```
Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is Fiji.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
Loading the code object succeeded.
Freeze the executable succeeded.
Extract the symbol from the executable succeeded.
Extracting the symbol from the executable succeeded.
Extracting the kernarg segment size from the executable succeeded.
Extracting the group segment size from the executable succeeded.
Extracting the private segment from the executable succeeded.
Creating a HSA signal succeeded.
Finding a fine grained memory region succeeded.
Allocating argument memory for input parameter succeeded.
Allocating argument memory for output parameter succeeded.
Finding a kernarg memory region succeeded.
Allocating kernel argument memory buffer succeeded.
Dispatching the kernel succeeded.
```

This seems [hsa_signal_wait_acquire()](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-1.1.0/sample/vector_copy.c#L409) doesn't return.

What's the problem and how can I fix this?

Note that I use Ivy Bridge CPU so ROCm doen't support the CPU according to @whchung .
Could you point me to the notice for the supported CPU on any wiki page or other documents etc?

Thanks.
