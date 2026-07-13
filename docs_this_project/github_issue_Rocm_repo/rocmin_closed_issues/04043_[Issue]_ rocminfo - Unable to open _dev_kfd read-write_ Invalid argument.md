# [Issue]: rocminfo - Unable to open /dev/kfd read-write: Invalid argument

- **Issue #:** 4043
- **State:** closed
- **Created:** 2024-11-20T13:10:21Z
- **Updated:** 2025-09-18T11:07:55Z
- **Labels:** Under Investigation, AMD Instinct MI300X, ROCm 5.7.0, ROCm 6.2.1
- **URL:** https://github.com/ROCm/ROCm/issues/4043

### Problem Description

`rocminfo` produces the output:

```
root:~# rocminfo
ROCk module version 6.7.0 is loaded
Unable to open /dev/kfd read-write: Invalid argument
root is member of nogroup group
```

As a consequence, libraries like Pytorch does seem not detect and use ROCm.

### Operating System

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 9474F 48-Core Processor

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.2.1, ROCm 5.7.0

### ROCm Component

rocminfo

### Steps to Reproduce

I installed ROCm 6.2.1 (also happens for ROCm 5.7.0) inside a Ubuntu 22.0.4 Docker container that runs on a host machine with a MI300X GPU. I then added `root` to `render`, `video`, and `nogroup` groups:

```sh
root:~# groups root
root : root video nogroup render
```

The GPU seems to be present:

```
root:/workspace/rocm# rocm-smi --showallinfo

============================ ROCm System Management Interface ============================
============================== Version of System Component ===============================
Driver version: 6.7.0
==========================================================================================
=========================================== ID ===========================================
GPU[0]		: Device Name: 		AMD Instinct MI300X OAM
GPU[0]		: Device ID: 		0x74a1
GPU[0]		: Device Rev: 		0x00
GPU[0]		: Subsystem ID: 	0x74a1
GPU[0]		: GUID: 		8554
...
root:~# rocm_agent_enumerator
gfx000
gfx942
```

However, when I run `rocmsmi` I get this output:

```
root:~# rocminfo
ROCk module version 6.7.0 is loaded
Unable to open /dev/kfd read-write: Invalid argument
root is member of nogroup group
```
In general, it seems like I can't access `/dev/kfd`, even though I'm in the groups:
```
root:~# cat /dev/kfd
Unable to open /dev/kfd read-write: Invalid argument
root:~# /dev/kfd
-bash: /dev/kfd: Permission denied
root:~# ls -l /dev/kfd
crw-rw-rw- 1 nobody nogroup 511, 0 Nov 15 17:12 /dev/kfd
```

Am I missing something?

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
root:~# /opt/rocm/bin/rocminfo --support
ROCk module version 6.7.0 is loaded
Unable to open /dev/kfd read-write: Invalid argument
root is member of nogroup group
```

### Additional Information

_No response_