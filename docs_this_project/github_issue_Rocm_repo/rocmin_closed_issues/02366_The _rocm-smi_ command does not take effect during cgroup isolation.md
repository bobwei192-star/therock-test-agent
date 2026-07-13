# The ‘rocm-smi’ command does not take effect during cgroup isolation

- **Issue #:** 2366
- **State:** closed
- **Created:** 2023-08-04T02:33:30Z
- **Updated:** 2024-03-02T03:41:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/2366

Hello, may I ask for your advice? I have encountered a problem. I have two GPUs with AMD. When I use the ‘rocm-smi’ command in a container that has applied for cgroup isolation of one GPU, it still displays two GPUs. Is this because the ‘rocm-smi’  command does not support cgroup isolation at the bottom level