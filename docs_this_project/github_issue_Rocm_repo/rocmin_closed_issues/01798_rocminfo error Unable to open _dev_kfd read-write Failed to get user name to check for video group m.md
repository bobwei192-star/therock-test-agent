# rocminfo error Unable to open /dev/kfd read-write Failed to get user name to check for video group membership

- **Issue #:** 1798
- **State:** closed
- **Created:** 2022-08-24T21:43:48Z
- **Updated:** 2025-09-10T00:19:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/1798

Hello everyone, I downloaded the docker image rocm5.2_ubuntu20.04_py3.7_pytorch_1.11.0_navi21 but I did not work for me. I am using a 6900xt as GPU and 5900x as CPU, do not know it is important but my system is Arch Linux, but it should not matter as I am running the ROCm in the container. The error occurs when I run the command:
`root@101acc334128:/var/lib/jenkins# /opt/rocm-5.2.0/bin/rocminfo`
Then the output:
`ROCk module is loaded`
`Unable to open /dev/kfd read-write: No such file or directory`
`Failed to get user name to check for video group membership`
