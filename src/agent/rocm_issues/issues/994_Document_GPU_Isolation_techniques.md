# Document GPU Isolation techniques

> **Issue #994**
> **状态**: closed
> **创建时间**: 2020-01-06T09:12:48Z
> **更新时间**: 2023-10-27T16:12:05Z
> **关闭时间**: 2023-10-27T16:12:05Z
> **作者**: abuccts
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/994

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- Maetveis

## 描述

Hi, I'm wondering the correct usage of `ROCR_VISIBLE_DEVICES`, and seeking for a method to isolate AMD GPUs for Docker (like [nvidia-container-runtime](https://github.com/NVIDIA/nvidia-container-runtime) can hide unmounted devices in `nvidia-smi`).

---

According to some search results, there're two environment variables for GPU isolation in ROCm:
* `HIP_VISIBLE_DEVICES` in HIP application (above ROC runtime) level
* `ROCR_VISIBLE_DEVICES` in ROC runtime (above ROC kernel driver) level

In my understanding, `HIP_VISIBLE_DEVICES` equals to `CUDA_VISIBLE_DEVICES` in NVIDIA, but `ROCR_VISIBLE_DEVICES` seems to be different from `NVIDIA_VISIBLE_DEVICES`.

Assume there're 4 GPU cards on a node:

* For NVIDIA:

    ```sh
    docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=2,3 ...
    ```
    will mount 2,3 cards into container and their ids are 0,1 inside container.
    
    Application can use `CUDA_VISIBLE_DEVICES=1` to choose the host card 3 inside container, `NVIDIA_VISIBLE_DEVICES` will be ignored by application, whose value is still `2,3`.

* For ROCm:

    ```sh
    docker run --device=/dev/kfd --device=/dev/dri/card2 --device=/dev/dri/card3 --group-add video ... (and related renderD* dev)
    ```
    will mount 2,3 cards into container, but all cards are visible in `rocm-smi` (*is this right?*).
    
    To choose the host card 3 inside container, application should use `HIP_VISIBLE_DEVICES=1` or `ROCR_VISIBLE_DEVICE=1`, while `ROCR_VISIBLE_DEVICE` won't be ignored in container.

Insofar as the above container case is concerned, `ROCR_VISIBLE_DEVICES` is more like a duplicate of `HIP_VISIBLE_DEVICES`, unlike `NVIDIA_VISIBLE_DEVICES` which isolates GPUs on the host.

---

BTW, is there any container runtime that ROCm provides to achieve the same functions like NVIDIA container runtime (e.g. ability to use `ROCR_VISIBLE_DEVICES` to isolate GPUs for container)?

---

## 评论 (17 条)

### 评论 #1 — sunway513 (2020-01-08T22:39:17Z)

Hi @abuccts , the following instructions might help:
Pass selected GPU driver interfaces (/dev/dri/render#) to Docker container. e.g. use the following docker run command option to select the first GPU:
`sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --group-add video`
You'll see four interfaces for your 4 GPU system:
`$ ls /dev/dri/render*`
`/dev/dri/renderD128 /dev/dri/renderD129 /dev/dri/renderD130 /dev/dri/renderD131`
Pass the additional devices interfaces if you want to expose more GPUs to the docker container at launch. 

---

### 评论 #2 — abuccts (2020-01-10T08:17:54Z)

Hi @sunway513, thanks for your response.

I knew that using `--device` flags works for ROCm as I described, like for nvidia gpus
```sh
docker run --device=/dev/nvidiactl --device=/dev/nvidia-uvm --device=/dev/nvidia0 ...
```
but nvidia-container-runtime also provides a capability to use `NVIDIA_VISIBLE_DEVICES` to achieve it
```sh
docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 ...
```

Both commands work on host, but __the second one__ is useful in Kubernetes. ROCm Docker only works with __the first one__.

There is a [device plugin](https://github.com/RadeonOpenCompute/k8s-device-plugin/) to use AMD GPUs in k8s, but it is not enough for scheduler extender.
An interface like `ROCR_VISIBLE_DEVICES` for AMD GPU isolation would be better, like NVIDIA [device plugin](https://github.com/NVIDIA/k8s-device-plugin) passes `NVIDIA_VISIBLE_DEVICES` to nvidia-container-runtime to use GPUs in k8s.

---

### 评论 #3 — sunway513 (2020-01-10T16:21:32Z)

Thanks @abuccts for elaboration. 
cc @y2kenny for AMD K8s support.

---

### 评论 #4 — y2kenny (2020-01-13T21:21:08Z)

@abuccts It's unclear to me why a custom container runtime is needed to pass in an environment variable.  According to [Docker run documentation](https://docs.docker.com/engine/reference/commandline/run/), -e is a standard flag.  What prevents you from `sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri/renderD128 --group-add video -e ROCR_VISIBLE_DEVICES=0`?

---

### 评论 #5 — abuccts (2020-01-15T11:43:09Z)

**In short, Kubernetes prevents me to use `--device` flag in Docker, and device plugin is not enough for GPU device in some scenarios.**

My goal is not to pass an env only, but to let `-e ROCR_VISIBLE_DEVICES=0` do what `--device=/dev/kfd --device=/dev/dri/renderD128 --group-add video` do (through a custom container runtime).
Just like for NVIDIA runtime, `-e NVIDIA_VISIBLE_DEVICES=0` will do the same as `--device=/dev/nvidiactl --device=/dev/nvidia-uvm --device=/dev/nvidia0`.

---

Let me explain it more clearly.

Here're the steps to use AMD GPUs in k8s:
1. specify resource `amd.com/gpu: 1` in pod spec
2. default scheduler schedule gpu and send allocate rpc request to device plugin
3. device plugin get the allocate request, **prepare DeviceSpec through plugin api** for corresponding gpus ([`Allocate` function](https://github.com/RadeonOpenCompute/k8s-device-plugin/blob/661b5788a9362cfc05e7f82a1293caee9a2b6997/cmd/k8s-device-plugin/main.go#L165-L198)), and return allocate response which **includes device spec for container**
4. kubelet get response and **pass the device config to container runtime**

Here're the steps to use NVIDIA GPUs in k8s:
1. specify resource `nvidia.com/gpu: 1` in pod spec
2. default scheduler schedule gpu and send allocate rpc request to device plugin
3. device plugin get the allocate request, **set `NVIDIA_VISIBLE_DEVICES` Env through plugin api** for corresponding gpus ([`Allocate` function](https://github.com/NVIDIA/k8s-device-plugin/blob/9f5f6a228bb044753c0680c4eed40d794c780ca3/server.go#L192-L213)), and return allocate response which **includes an env for container**
4. kubelet get response and **pass the env to container runtime, nvidia-container-runtime will add a pre-hook to add device spec if this env exists**

So the second implementation has a more modular design: k8s device plugin or `docker run` just set an env `NVIDIA_VISIBLE_DEVICES`, container runtime is responsible for checking the env and add devices spec in container.

Here's my scenario to use GPUs in k8s:
*In a large scale cluster, GPU topology is important for training. Kubernetes default scheduler only counts gpu resources and ignore their topology, so I use a **scheduler extender** for topology-aware gpu scheduling.*
* For NVIDIA GPUs, the scheduler interface is clear: custom scheduler just sets `NVIDIA_VISIBLE_DEVICES` env for scheduling result, which equals to step 1~3 in default scheduler.
* For AMD GPUs, it's not easy to achieve this: either to modify device plugin in step 3, or add a similar container runtime to accept an env like nvidia-container-runtime in step 4.

@y2kenny Hope this makes you understand my root problem, pls let me know if there's still something unclear to you.

This is more like a container runtime feature request for amd gpu, since I didn't find any useful solution through search. Or do you have any suggestions for the above scenario?

---

### 评论 #6 — y2kenny (2020-01-15T19:32:07Z)

@abuccts Ah ok, so this is not really a `docker run` question but how to get the environment variable into the k8s environment.  I think there's already a pull request for this on the device plugin side.  I just need to review and merge that.

---

### 评论 #7 — abuccts (2020-01-16T02:46:45Z)

Maybe you mean [this PR](https://github.com/RadeonOpenCompute/k8s-device-plugin/pull/5/files). It passes both `DeviceSpec` and `Envs` to plugin api, instead of just passing `Envs` and injecting device spec in runtime.

You can take a look at nvidia device plugin's [Allocate](https://github.com/NVIDIA/k8s-device-plugin/blob/9f5f6a228bb044753c0680c4eed40d794c780ca3/server.go#L192-L213), the code can explain easier. It works with a [container runtime](https://github.com/NVIDIA/nvidia-container-runtime) which reads the env and adds device spec in runtime (pre-start hook).

---

### 评论 #8 — y2kenny (2020-01-16T05:15:02Z)

Yup, that's the PR.  I am hesitating on the PR because I am thinking the respective runtime should be made container aware instead of me hacking in the environment variables like this.  I also need to figure out how 3 of our env vars (HIP_VISIBLE_DEVICES, ROCR_VISIBLE_DEVICES, GPU_DEVICE_ORDINAL) sort their GPUs.  The PR do it by sorting the PCI address, but I am not sure that's correct.  @sunway513, do you know folks' github handle from the HIP team, ROCr team and OpenCL team?  Can you add them here to comment on this?

---

### 评论 #9 — sunway513 (2020-01-16T05:24:12Z)

cc @gargrahul @skeelyamd @kentrussell for comments...
From my experiences, ROCR_VISIBLE_DEVICES isolates GPU resources pretty well.

---

### 评论 #10 — gargrahul (2020-01-16T19:16:53Z)

@sunway513 Yes I agree though in my opinion with HIP/VDI (not using ROCr on Windows) coming up, it would be recommended to continue using HIP_VISIBLE_DEVICES. 

---

### 评论 #11 — y2kenny (2020-01-17T03:04:02Z)

@gargrahul How does HIP sort the devices?  i.e.  how do you tell which device in the machine is 1 and which is 2?

---

### 评论 #12 — illwieckz (2021-12-04T22:05:38Z)

I verified `GPU_DEVICE_ORDINAL` now works with ROCm, see https://github.com/RadeonOpenCompute/ROCm/issues/1624#issuecomment-986099377 but a `ROCR_VISIBLE_DEVICE` would still be better, see #1624 for use case were `GPU_DEVICE_ORDINAL` is not enough: You can't blacklist a device in ROCm and keep it enabled in Orca because they both read the same environment vairable.

@ROCmSupport do you think it would be doable to implement `ROCR_VISIBLE_DEVICE`?

---

### 评论 #13 — skeelyamd (2021-12-07T01:16:44Z)

I think there has been some confusion in this thread as ROCR_VISIBLE_DEVICES was never intended to be equivalent to NVIDIA_VISIBLE_DEVICES.  ROCR_VISIBLE_DEVICES is intended to function as CUDA_VISIBLE_DEVICES does but at the ROCr level (HIP is not the lowest level user interface in ROCm).  It is not intended to be a container specific thing.

HIP_VISIBLE_DEVICES only applies to the HIP runtime and not to any other language runtime or library built atop ROCr.  Notably use of HIP_VISIBLE_DEVICES still allows ROCr to initialize all devices and for other (non-HIP) languages and libraries to use all devices, such as AOMP and UCX.

GPU_DEVICE_ORDINAL is also different from NVIDIA_VISIBLE_DEVICES.  GPU_DEVICE_ORDINAL is an older env var that applies device selection at what is now the ROCclr level, a middleware component that sits between ROCr and HIP / OpenCL and so impacts both HIP and OpenCL, but only HIP and OpenCL.

---

### 评论 #14 — saadrahim (2023-03-14T16:03:06Z)

Documentation team: Please document these concerns in https://advanced-micro-devices-demo--1940.com.readthedocs.build/projects/alpha/en/1940/how_to/docker_gpu_isolation.html. Change the title of the document to gpu_isolation_techniques. Link to individual pages for each type of isolation technique. 

- ROCr env vars
- HIP env vars
- ROCclr env vars
- docker based isolation
- GPU passthrough (Virtualization)
- comparison between techniques
- What is available on Windows?


---

### 评论 #15 — Maetveis (2023-03-20T09:02:29Z)

I've changed this issue to track the documentation effort for GPU isolation. If I understand it correctly the earlier discussion contained a request for a container runtime for rocm, I've expanded a bit on this feature request in: https://github.com/RadeonOpenCompute/ROCm/discussions/1836#discussioncomment-5365557. For the device plugin, you could [file an issue on its repository](https://github.com/RadeonOpenCompute/k8s-device-plugin/issues). 


---

### 评论 #16 — saadrahim (2023-06-01T15:45:45Z)

https://rocm.docs.amd.com/en/develop/understand/gpu_isolation.html

Please take a look at our documentation available and let us know if this meets your needs.

---

### 评论 #17 — samjwu (2023-10-27T16:12:05Z)

GPU Isolation techniques as of ROCm 5.7.1: https://rocm.docs.amd.com/en/docs-5.7.1/understand/gpu_isolation.html

---
