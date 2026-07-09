# Installing CUDA Toolkit broke ROCm installation

- **Issue #:** 2106
- **State:** closed
- **Created:** 2023-05-03T23:08:16Z
- **Updated:** 2024-02-16T20:24:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/2106

Command rocminfo was working great until I installed the CUDA Toolkit 12.0
(The server blade has both AMD MI100 and NVIDIA V100 GPUs)
Now cuda works fine but I get the following error when running the command `rocminfo`
```
ktb@server:~ rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
ktb is member of video group
```

Any suggestions?