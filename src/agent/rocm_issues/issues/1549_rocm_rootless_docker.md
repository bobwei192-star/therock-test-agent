# rocm rootless docker

> **Issue #1549**
> **状态**: closed
> **创建时间**: 2021-08-06T17:10:16Z
> **更新时间**: 2024-03-03T13:05:24Z
> **关闭时间**: 2024-01-20T03:00:50Z
> **作者**: den-run-ai
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1549

## 描述

Do you support running rootless docker with rocm/tensorflow and rocm/pytorch AMD images on AMD GPUs?
If yes, what are the required modifications to run in the rootless docker mode?

---

## 评论 (13 条)

### 评论 #1 — ROCmSupport (2021-08-09T05:36:13Z)

Thanks @denfromufa for reaching out.
I certainly understood the problem and will get back to you asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-08-11T07:38:14Z)

I am keeping this point in a discussion forum and will share an update soon.
Thank you.

---

### 评论 #3 — Djip007 (2021-12-11T19:05:44Z)

for rootless usage you can use podman :
```
> podman run --rm  -it  --device=/dev/kfd   --device=/dev/dri  --ipc=host  rocm/rocm-terminal
```
on fedora it work
don't know for docker.

---

### 评论 #4 — ROCmSupport (2021-12-14T13:09:18Z)

ROCm supports rootless dockers.
We need to configure rootless docker environment in a machine to verify it.
configuring rootless docker environment is not specific to ROCm, its common for all.
So I feel its not an issue actually.

---

### 评论 #5 — paklui (2021-12-17T21:00:19Z)

I think there are 2 options (subgid and a extra option to docker run, see below) that we can use to make rootless docker work that the details for the changes are described below.

To describe the changes, we first describe in the typical (non-rootless) docker host environment. When a user needs to access to our GPU, the user would need to be in the ‘video’ group in order to access the /dev/kfd device.

```
debug@node1:~$ ls -al /dev/kfd
crw-rw---- 1 root video 237, 0 Aug 10 13:55 /dev/kfd
```

Now, in the rootless docker environment, the container user needs to access /dev/kfd as well. 

The issue is that rootless docker does not use or allow passing the existing group of /dev/kfd in host, this is the reason why we need to do the following changes.

Due to the change in the group in the rootless docker environment, we need to make a modification to map the video group to a new group in the rootless docker. It is done by adding a new entry in /etc/setgid, for the user to allow access to /dev/kfd in the container. It is confirmed by the rootless docker developer Akihiro Suda that we needed this workaround due to the gid requirement for /dev/kfd.

You can do the following to map the video group (in my case, that's group number 44) on host to the new group in the rootless docker. This step requires admin to modify the /etc/setgid file on host, to allow the additional mapping of the group for the user to access the GPU in rootless docker.

```
debug@node1:~$ getent group video
video:x:44:root,debug

root@node1:~$ vim /etc/setgid
debug:44:1
debug:6194848:65536
```

Please note, the order of the new entry matters. The new entry needs to be BEFORE the existing entry in /etc/setgid.

Once the above change has been made, you can use “docker run **--group-add daemon**” (instead of “--group-add video” in the "rootful" docker scenario) to access the GPU, due to the change of group to ‘daemon’ group made by rootless docker. 

Another method is to use the "**docker run --user 0:1**" flag to allow the user to have the gid=1 when running the root docker. Either (--group-add daemon, or --user 0:1) is needed.

```
debug@node1:~$ vim ./docker-launch.sh
#!/bin/bash
docker run -it --rm --dns 8.8.8.8 --privileged \
  -v /home:/home \
  --cap-add=SYS_PTRACE --device=/dev/dri --device=/dev/kfd --device=/dev/mem \
  --group-add daemon \
  --security-opt seccomp=unconfined --network host \
  --name=tensorflow-training-${USER} \
  rocm/tensorflow:rocm4.2-tf2.5-dev

cd ~/benchmarks/scripts/tf_cnn_benchmarks
python3 tf_cnn_benchmarks.py --model=resnet50 --batch_size=128 --print_training_accuracy=True --variable_update=parameter_server --local_parameter_device=gpu --num_gpus=1

root@node1:/# id
uid=0(root) gid=0(root) groups=0(root),1(daemon)

root@node1:/# ls -al /dev/kfd
crw-rw---- 1 nobody daemon 237, 0 Aug 10 20:55 /dev/kfd
``` 

Then you should be able to access the GPU with this change inside the rootless docker. I checked with Akihiro Suda of Moby (dockerd) in the past, this should acceptable in most cases. 

---

### 评论 #6 — bioinfornatics (2023-04-11T07:09:29Z)

Dear team,

Thanks @paklui for your explanation. I have the same problem with `buildah`


# on the host

```bash
$ ls -al /dev/kfd
crw-rw-rw-. 1 root render 235, 0  9 avril 21:35 /dev/kfd
$  getent group video
video:x:39:
$  getent group render
render:x:105:
```

Note: the local user is not part of these groups

I have not yet created the `/etc/setgid`


# buildah

```bash
$  buildah_options="  --cap-add=SYS_PTRACE --group-add=105 --group-add=39 --security-opt seccomp=unconfined --network host  --device=/dev/kfd:rw --device=/dev/dri:rw --ipc=host "
$ devel_container="$(buildah from  ${buildah_options[*]} fedora:37)"
$ buildah run "${devel_container}" /bin/bash 
# ls /dev/kfd 
ls: cannot access '/dev/kfd': Permission denied
# dnf install -y rocminfo && rocminfo
…
ROCk module is loaded
Unable to open /dev/kfd read-write: Permission denied
root is not member of "video" group, the default DRM access group. Users must be a member of the "video" group or another DRM access group in order for ROCm applications to run successfully.
```

Thanks for your help

Best regards






---

### 评论 #7 — abhimeda (2024-01-02T15:50:20Z)

Is this still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #8 — nartmada (2024-01-20T02:02:24Z)

Hi @den-run-ai, do you still need this ticket to be opened?  ROCmSupport has commented ROCm does support rootless dockers and paklui has provided the instruction to configure such environment.  Thanks.

---

### 评论 #9 — den-run-ai (2024-01-20T03:00:48Z)

I believe this issue was resolved, thank you AMD team!

---

### 评论 #10 — bioinfornatics (2024-01-21T10:33:16Z)

The problem it is still present

```
$ buildah_options="  --cap-add=SYS_PTRACE --group-add=105 --group-add=39 --security-opt seccomp=unconfined --network host  --device=/dev/kfd:rw --device=/dev/dri:rw --ipc=host "

$ devel_container="$(buildah from  ${buildah_options[*]} fedora:39)"
Resolved "fedora" as an alias (/etc/containers/registries.conf.d/000-shortnames.conf)
Trying to pull registry.fedoraproject.org/fedora:39...
Getting image source signatures
Copying blob 718a00fe3212 done   | 
Copying config 368a084ba1 done   | 
Writing manifest to image destination

$ buildah run "${devel_container}" /bin/bash 

[root@04ff0f3d3aa3 /]# ls /dev/kfd 
ls: cannot access '/dev/kfd': Permission denied

[root@04ff0f3d3aa3 /]# dnf install -y rocminfo && rocminfo
Fedora 39 - x86_64                                                                                                                                                                                            6.5 MB/s |  89 MB     00:13    
Fedora 39 openh264 (From Cisco) - x86_64                                                                                                                                                                      2.2 kB/s | 2.5 kB     00:01    
Fedora 39 - x86_64 - Updates                                                                                                                                                                                  6.0 MB/s |  29 MB     00:04    
Dependencies resolved.
==============================================================================================================================================================================================================================================
 Package                                                  Architecture                                       Version                                                                Repository                                           Size
==============================================================================================================================================================================================================================================
Installing:
 rocminfo                                                 x86_64                                             5.7.0-1.fc39                                                           updates                                              37 k
Installing dependencies:
 hsakmt                                                   x86_64                                             1.0.6-34.rocm5.7.0.fc39                                                updates                                              73 k
 hwdata                                                   noarch                                             0.378-1.fc39                                                           updates                                             1.6 M
 kmod                                                     x86_64                                             30-6.fc39                                                              fedora                                              120 k
 libdrm                                                   x86_64                                             2.4.120-1.fc39                                                         updates                                             157 k
 libpciaccess                                             x86_64                                             0.16-9.fc39                                                            fedora                                               26 k
 numactl-libs                                             x86_64                                             2.0.16-3.fc39                                                          fedora                                               30 k
 rocm-runtime                                             x86_64                                             5.7.1-1.fc39                                                           updates                                             495 k

Transaction Summary
==============================================================================================================================================================================================================================================
Install  8 Packages

Total download size: 2.5 M
Installed size: 12 M
Downloading Packages:
(1/8): libpciaccess-0.16-9.fc39.x86_64.rpm                                                                                                                                                                    727 kB/s |  26 kB     00:00    
(2/8): numactl-libs-2.0.16-3.fc39.x86_64.rpm                                                                                                                                                                  668 kB/s |  30 kB     00:00    
(3/8): kmod-30-6.fc39.x86_64.rpm                                                                                                                                                                              1.1 MB/s | 120 kB     00:00    
(4/8): hsakmt-1.0.6-34.rocm5.7.0.fc39.x86_64.rpm                                                                                                                                                              1.0 MB/s |  73 kB     00:00    
(5/8): libdrm-2.4.120-1.fc39.x86_64.rpm                                                                                                                                                                       997 kB/s | 157 kB     00:00    
(6/8): rocm-runtime-5.7.1-1.fc39.x86_64.rpm                                                                                                                                                                   2.0 MB/s | 495 kB     00:00    
(7/8): rocminfo-5.7.0-1.fc39.x86_64.rpm                                                                                                                                                                       434 kB/s |  37 kB     00:00    
(8/8): hwdata-0.378-1.fc39.noarch.rpm                                                                                                                                                                         4.4 MB/s | 1.6 MB     00:00    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                                                                         2.1 MB/s | 2.5 MB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                                                                                                      1/1 
  Installing       : hwdata-0.378-1.fc39.noarch                                                                                                                                                                                           1/8 
  Installing       : libpciaccess-0.16-9.fc39.x86_64                                                                                                                                                                                      2/8 
  Installing       : libdrm-2.4.120-1.fc39.x86_64                                                                                                                                                                                         3/8 
  Installing       : numactl-libs-2.0.16-3.fc39.x86_64                                                                                                                                                                                    4/8 
  Installing       : hsakmt-1.0.6-34.rocm5.7.0.fc39.x86_64                                                                                                                                                                                5/8 
  Installing       : rocm-runtime-5.7.1-1.fc39.x86_64                                                                                                                                                                                     6/8 
  Installing       : kmod-30-6.fc39.x86_64                                                                                                                                                                                                7/8 
  Installing       : rocminfo-5.7.0-1.fc39.x86_64                                                                                                                                                                                         8/8 
  Running scriptlet: rocminfo-5.7.0-1.fc39.x86_64                                                                                                                                                                                         8/8 
  Verifying        : kmod-30-6.fc39.x86_64                                                                                                                                                                                                1/8 
  Verifying        : libpciaccess-0.16-9.fc39.x86_64                                                                                                                                                                                      2/8 
  Verifying        : numactl-libs-2.0.16-3.fc39.x86_64                                                                                                                                                                                    3/8 
  Verifying        : hsakmt-1.0.6-34.rocm5.7.0.fc39.x86_64                                                                                                                                                                                4/8 
  Verifying        : hwdata-0.378-1.fc39.noarch                                                                                                                                                                                           5/8 
  Verifying        : libdrm-2.4.120-1.fc39.x86_64                                                                                                                                                                                         6/8 
  Verifying        : rocm-runtime-5.7.1-1.fc39.x86_64                                                                                                                                                                                     7/8 
  Verifying        : rocminfo-5.7.0-1.fc39.x86_64                                                                                                                                                                                         8/8 

Installed:
  hsakmt-1.0.6-34.rocm5.7.0.fc39.x86_64    hwdata-0.378-1.fc39.noarch    kmod-30-6.fc39.x86_64    libdrm-2.4.120-1.fc39.x86_64    libpciaccess-0.16-9.fc39.x86_64    numactl-libs-2.0.16-3.fc39.x86_64    rocm-runtime-5.7.1-1.fc39.x86_64   
  rocminfo-5.7.0-1.fc39.x86_64            

Complete!
ROCk module is loaded
Unable to open /dev/kfd read-write: Permission denied
root is not member of "video" group, the default DRM access group. Users must be a member of the "video" group or another DRM access group in order for ROCm applications to run successfully.
```


---

### 评论 #11 — nartmada (2024-01-21T14:23:59Z)

Hi @bioinfornatics, can you please file a new ticket for buildah?  Thank you.

---

### 评论 #12 — serhii-nakon (2024-02-05T00:29:11Z)

@bioinfornatics @den-run-ai 
I found solution that works for me
1. Need find group IDs for render and video -  for me it 44 and 105
2. Edit /etc/subgid like here (if you will set here custom values please recalculate it properly, count of all IDs should be 65536) 
```
serhy:100000:44
serhy:44:1
serhy:100045:60
serhy:105:1
serhy:100106:65429
```
3. Run docker with parameter `privileged: true` (in my case in docker-compose.yaml) if I correctly understand it will share all devices that available to your user inside container
4. Inside container your will need create or edit existing group to get `render` and `video` groups with IDs `106` and `45` - by some reason docker add 1 as offset.
5. Next one add `render` and `video` to your user and to root user too - when I use `privileged: true` it need to do also for root user
6. It should works!!! (At least i complete MNIST test from PyTorch examples)

---

### 评论 #13 — Abdull (2024-03-03T13:05:23Z)

@paklui, are you sure the file is named `/etc/setgid`? Do you instead mean `/etc/subgid`?

---
