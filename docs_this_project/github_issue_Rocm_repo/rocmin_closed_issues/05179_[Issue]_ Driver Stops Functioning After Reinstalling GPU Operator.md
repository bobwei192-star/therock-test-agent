# [Issue]: Driver Stops Functioning After Reinstalling GPU Operator

- **Issue #:** 5179
- **State:** closed
- **Created:** 2025-06-06T22:48:48Z
- **Updated:** 2025-10-03T17:09:29Z
- **Labels:** Question
- **Assignees:** yansun1996
- **URL:** https://github.com/ROCm/ROCm/issues/5179

### Problem Description

After installing AMD GPU operator v1.3.0 via helm -> uninstall it via helm-> reinstall it via helm again. The driver stops functioning. The metrics exporter pod reported coredump 
```shell
$:~# kubectl logs -n amd-operator  amd-gpu-metrics-exporter-bv869
exporter 2025/06/03 23:55:53 rocpclient.go:66: exec error :signal: aborted (core dumped)
exporter 2025/06/03 23:56:08 rocpclient.go:66: exec error :signal: aborted (core dumped)
exporter 2025/06/03 23:56:23 rocpclient.go:66: exec error :signal: aborted (core dumped)
```
Running `rocm-smi` command within the metrics exporter container hangs without any outputs:
```shell
$:~# kubectl exec -it -n amd-operator amd-gpu-metrics-exporter-bv869 -- /bin/bash
Defaulted container "metrics-exporter-container" out of: metrics-exporter-container, driver-init (init)
[root@amd-gpu-metrics-exporter-bv869 ~]# rocm-smi
(hangs)
```
This issue can only be fixed after a node reboot. 

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

Intel Xeon Processor (Icelake)

### GPU

AMD Instinct MI210 

### ROCm Version

ROCm 6.4

### ROCm Component

_No response_

### Steps to Reproduce

1. Prepare an env without pre-installed amd drivers.
2. Install amd gpu operator v1.3.0 via helm: with deviceconfig settings: `spec.driver.enable=true`, `spec.driver.version="6.4"` with proper private image registry. Use default values for everything else.
3. Uninstall amd gpu operator via helm
4. Repeat step 2 without rebooting the node

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_