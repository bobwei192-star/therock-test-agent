# rocminfo error Unable to open /dev/kfd read-write Failed to get user name to check for video group membership

> **Issue #1798**
> **状态**: closed
> **创建时间**: 2022-08-24T21:43:48Z
> **更新时间**: 2025-09-10T00:19:53Z
> **关闭时间**: 2024-07-17T13:51:30Z
> **作者**: EduMio
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1798

## 描述

Hello everyone, I downloaded the docker image rocm5.2_ubuntu20.04_py3.7_pytorch_1.11.0_navi21 but I did not work for me. I am using a 6900xt as GPU and 5900x as CPU, do not know it is important but my system is Arch Linux, but it should not matter as I am running the ROCm in the container. The error occurs when I run the command:
`root@101acc334128:/var/lib/jenkins# /opt/rocm-5.2.0/bin/rocminfo`
Then the output:
`ROCk module is loaded`
`Unable to open /dev/kfd read-write: No such file or directory`
`Failed to get user name to check for video group membership`


---

## 评论 (12 条)

### 评论 #1 — SturtKoh (2022-09-05T22:36:01Z)

does your login account is added to video group?
$sudo usermod -a -G video $LOGNAME
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.5/page/How_to_Install_ROCm.html

---

### 评论 #2 — Rmalavally (2022-09-06T01:13:28Z)

@SturtKoh, please refer to the latest ROCm documentation at https://docs.amd.com. 

Let us know if you cannot find the information you need. 

ROCm Documentation Team

---

### 评论 #3 — SturtKoh (2023-06-05T06:55:35Z)

> 

yeap, but I wonder that it was a right guide...

---

### 评论 #4 — tom-papatheodore (2023-09-14T14:06:59Z)

I ran into this issue when using the `--containall` option to Apptainer, but I was able to resolve it with the additional option `--bind=/dev/kfd,/dev/dri`:

```
$ apptainer run --containall --bind=/dev/kfd,/dev/dri tensorflow_latest.sif
```

The `--containall` option tells Apptainer not to bring in anything from the host environment; no environment variables, bind mounts, etc.

The `--bind=/dev/kfd,/dev/dri` option says, "but I *would* like these specific directories bind mounted". These are used by the GPU driver to collect information about the available GPUs.

However, the error can be generated for multiple reasons, but I wanted to share my specific situation in case it's helpful for someone.


---

### 评论 #5 — matteobrv (2023-12-10T21:27:43Z)

> Hello everyone, I downloaded the docker image rocm5.2_ubuntu20.04_py3.7_pytorch_1.11.0_navi21 but I did not work for me. I am using a 6900xt as GPU and 5900x as CPU, do not know it is important but my system is Arch Linux, but it should not matter as I am running the ROCm in the container. The error occurs when I run the command: `root@101acc334128:/var/lib/jenkins# /opt/rocm-5.2.0/bin/rocminfo` Then the output: `ROCk module is loaded` `Unable to open /dev/kfd read-write: No such file or directory` `Failed to get user name to check for video group membership`

I'm on Linux Mint 21.2 (kernel: 6.2.0-33-generic) and was facing the same issue with an RX6850M XT GPU. The solution is to explicitly grant the ROCm container access to the necessary device files using the `--device` flag. In this case, you'll need to specify both `--device /dev/kfd` and `--device /dev/dri`. For a detailed explanation of why this is necessary, refer to the [Accessing GPUs in containers](https://rocm.docs.amd.com/en/latest/deploy/docker.html#accessing-gpus-in-containers) section of the official documentation.

---

### 评论 #6 — srinivamd (2023-12-10T22:47:06Z)

One solution to avoid this issue that I use is by updating the amdgpu udev rules.
For `render` group systems, ex. Ubuntu, use this for `cat /etc/udev/rules.d/70-amdgpu.rules ` to allow read, write by all users.
```
KERNEL=="kfd", GROUP="render", MODE="0666" 
SUBSYSTEM=="drm", MODE="0666"
```
Replace `render` with `video` above to use the `video` group.

Then, regenerate dev files using `udevadm` by running:
```
sudo udevadm control --reload
sudo udevadm trigger
```
Check the permissions of `/dev/kfd`, i.e. `ls -l /dev/kfd` should show `666` with `rw` for all.

Check with your system administrator as appropriate as above requires `sudo` privileges.

---

### 评论 #7 — nasawyer7 (2024-01-08T08:31:19Z)

for me, /dev/kfd just does not exist at all

---

### 评论 #8 — ppanchad-amd (2024-06-18T16:13:00Z)

@EduMio Have you resolved your issue? If so, please close the ticket. Thanks!

---

### 评论 #9 — harkgill-amd (2024-07-17T13:51:30Z)

Hi @EduMio, please try the following:

1. Follow the steps outlined at [Using a Docker image with PyTorch installed](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party/pytorch-install.html) under [Installing PyTorch for ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party/pytorch-install.html). Launching the docker container with the `--device=/dev/kfd` flag specified should resolve your issue.

2. Try the fix @srinivamd highlighted above.

If you are still experiencing this issue after trying both solutions, please re-open this ticket. Thanks!

---

### 评论 #10 — dobo290 (2024-11-30T15:50:02Z)

Im in fedora 41 and after this major update, all of this doesn't work.
I'm using podman with either jellyfin in decoding and Ollama with rocm for LLMs.
All the containers do show access to the files /dev/dri and kfd, rocm-smi is not showing a gpu in any container and radeontop says no permission to get access in any way. I tried  adding groups like dram, icr, kfd with udev rules, I checked the gpu drivers and selinux, I even tried going for chown 777/666 and using sys module in Podman, security opt and many other things, I can't get it back.
The error appeared after updating from 40 to 41.
Before that, everything ran out of the box. I just had to add the devices to my docker-compose file and it was set.

---

### 评论 #11 — harkgill-amd (2024-12-02T15:03:12Z)

Hi @dobo290, could you please create a new issue with the exact error message and steps to reproduce? If there is a regression in Fedora 41, it would be better to investigate it on a new thread for more visibility.

---

### 评论 #12 — dray89 (2025-09-10T00:19:53Z)

anyone solved this yet? I have gone through these instructions and am also missing kvd and dri


---
