# Document GPU Isolation techniques

- **Issue #:** 994
- **State:** closed
- **Created:** 2020-01-06T09:12:48Z
- **Updated:** 2023-10-27T16:12:05Z
- **Labels:** Documentation
- **Assignees:** Maetveis
- **URL:** https://github.com/ROCm/ROCm/issues/994

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