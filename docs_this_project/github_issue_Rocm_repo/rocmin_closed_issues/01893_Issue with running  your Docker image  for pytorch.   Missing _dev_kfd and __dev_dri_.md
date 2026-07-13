# Issue with running  your Docker image  for pytorch.   Missing /dev/kfd and "/dev/dri"

- **Issue #:** 1893
- **State:** closed
- **Created:** 2023-01-18T18:18:17Z
- **Updated:** 2024-11-13T20:22:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1893

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
