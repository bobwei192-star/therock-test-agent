# Issue with running  your Docker image  for pytorch.   Missing /dev/kfd and "/dev/dri"

> **Issue #1893**
> **状态**: closed
> **创建时间**: 2023-01-18T18:18:17Z
> **更新时间**: 2024-11-13T20:22:43Z
> **关闭时间**: 2024-07-03T19:45:23Z
> **作者**: raymondbernard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1893

## 描述

#Issue with running the default Docker image run for pytorch.  
# Missing /dev/kfd and "/dev/dri"


# example  found at https://www.amd.com/en/technologies/infinity-hub/pytorch

docker run --device=/dev/kfd --device=/dev/dri --group-add video --shm-size=4g --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host -it --rm -v <local_dir>:<container_dir> amdih/pytorch:[rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0](https://hub.docker.com/layers/rocm/pytorch/rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0/images/sha256-b075da4b74e9349e3fd9e38695c5800f391f1aec414f80d3846f67e21c70c0ce?context=explore)0


# Error received 

Digest: sha256:b075da4b74e9349e3fd9e38695c5800f391f1aec414f80d3846f67e21c70c0ce
Status: Downloaded newer image for amdih/pytorch:rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0
docker: Error response from daemon: error gathering device information while adding custom device "/dev/kfd": no such file or directory.

(.venv) C:\Users\RayBe\OneDrive\Documents\pytorch>docker run  --device=/dev/dri --group-add video --shm-size=4g --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host --rm -v C:\Users\RayBe\OneDrive\Documents\pytorch:/data/mnist amdih/pytorch:rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0
docker: Error response from daemon: error gathering device information while adding custom device "/dev/dri": no such file or directory.


# ran the Docker run command without listing the missing devices.  

(.venv) C:\Users\RayBe\OneDrive\Documents\pytorch>docker run -it --group-add video --shm-size=4g --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --ipc=host --rm -v C:\Users\RayBe\OneDrive\Documents\pytorch:/data/mnist amdih/pytorch:rocm5.0_ubuntu18.04_py3.7_pytorch_1.10.0




#   Missing /dev/kfd and /dev/dri!!! 
root@d7197a0a618a:/var/lib/jenkins# cd /dev
root@d7197a0a618a:/dev# dir
console  core  fd  full  mqueue  null  ptmx  pts  random  shm  stderr  stdin  stdout  tty  urandom  zero


# tested some basic functions 
root@d7197a0a618a:/var/lib/jenkins# python
Python 3.7.11 (default, Jul 27 2021, 14:32:16)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> x = torch.rand(5, 3)
>>> print(x)
tensor([[0.8026, 0.6577, 0.4702],
        [0.6649, 0.2105, 0.5955],
        [0.7936, 0.8153, 0.1621],
        [0.2718, 0.2482, 0.4927],
        [0.6228, 0.7599, 0.6008]])


---

## 评论 (6 条)

### 评论 #1 — brewfalconenterprises (2023-02-09T18:34:08Z)

Same error here. Without importing kfd and dri, PyTorch is not recognizing my GPU. All kinds of issues with ROCm on my RX6600XT.


---

### 评论 #2 — Cyp9715 (2023-02-11T23:53:37Z)

I have the same problem. Does anyone know the solution to the problem?

---

### 评论 #3 — alexschroeter (2023-02-16T20:14:54Z)

It looks like you are trying to do this on a Windows system, which doesn't have /dev/kfd and as far as I know Windows doesn't support running an AMD GPU inside a docker container.
So the message '"/dev/kfd": no such file or directory' makes sense since it doesn't exist on your system.

A better test if it works would also be:
```
root@d93ddb159808:/var/lib/jenkins# python
Python 3.7.11 (default, Jul 27 2021, 14:32:16)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.cuda.device_count()
2
```

If you run this in the container instance without the device, you see that it says false and the reason you could run your example is, that it just used the CPU for the calculation.

According to pytorch homepage, there are no working packages for windows and I don't know if WSL2 works for AMD.

---

### 评论 #4 — ppanchad-amd (2024-05-09T19:55:30Z)

@raymondbernard Has your issue been resolved? If so, please close the ticket. Thanks!

---

### 评论 #5 — harkgill-amd (2024-07-03T19:45:23Z)

Hi @raymondbernard, as @alexschroeter mentioned, the issue you are encountering is because the `docker run` command is meant for Linux OS's where /dev/kfd and /dev/dri exist. For Windows, only the HIP SDK is supported but you can run PyTorch on WSL2 following the instructions below.

1. [Install Radeon software for WSL with ROCm](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html)
2. [Install PyTorch for Radeon GPUs on WSL](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-pytorch.html)

If you encounter any issues with the installation on WSL, please open a new issue. Thanks!

---

### 评论 #6 — mohammed-Emad (2024-11-13T20:22:42Z)

for ubuntu users!
Try this..
```sudo apt install comgr rocminfo hsa-rocr rccl```


---
