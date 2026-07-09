# error messages: kfd2kgd: Failed to map bo to gpuvm; kfd2kgd: amdgpu_vm_bo_update failed

- **Issue #:** 791
- **State:** closed
- **Created:** 2019-05-08T19:25:56Z
- **Updated:** 2019-10-05T08:15:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/791

Hi,

i'm developing a multi GPU program that uses MPI parallelization. The setup I'm using is as follows:
Mainboard: X10SRA-F
GPU: 2 x Radeon Pro Duo, i.e. 4 ASICS
OS: ubuntu 18.04.2 LTS, kernel 4.15.0-48-generic, ROCm 2.4

When using about 10.7 GB per GPU in a run where two MPI ranks use 2 GPUs each, the following errors start showing up in dmesg after the program has been running for a while. Also the performance of the program starts to drop when the error messages start showing up.

message 1:
[  374.528056] amdgpu 0000:0a:00.0: bo 000000008621f4e3 va 0x0001907700-0x0001907805 conflict with 0x0001907700-0x0001907802
[  374.528937] kfd2kgd: Failed to map VA 0x1907700000 in vm. ret -22                                                                                                                       
[  374.529847] kfd2kgd: Failed to map bo to gpuvm
[  374.530783] Failed to map to gpu 0/4

message 2:
[  375.487864] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[  375.487871] kfd2kgd: amdgpu_vm_bo_update failed
[  375.488963] kfd2kgd: validate_invalid_user_pages: update PTE failed

Both messages show up many times and they are printed in red!

Is that a problem with ROCm or with my code? The error does not show up when using one GPU per MPI rank only. For smaller data sets the and 2 GPUs per MPI rank the problem does not show up. The code does not produce out of bound memory access, I believe.

Greetings