# rocminfo HSA_STATUS_ERROR_OUT_OF_RESOURCES

> **Issue #1080**
> **状态**: closed
> **创建时间**: 2020-04-12T00:56:03Z
> **更新时间**: 2021-03-17T07:45:54Z
> **关闭时间**: 2021-03-17T07:45:54Z
> **作者**: MatPoliquin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1080

## 描述

Ubuntu 19.10
Kernel 5.3.0-46-generic
rocm-dkms 3.3.0-19
RX 580
E5 2680v2

When I run **rocminfo**, I get this error
ROCk module is loaded
xeon is member of video group
`hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
`


But if I run it as **root**, it works as intended
`sudo /opt/rocm/bin/rocminfo`

This problem started with the latest rocm

EDIT:
I got it to work by installing rocm 3.1 first and then upgrading to 3.3

---

## 评论 (19 条)

### 评论 #1 — jackyin68 (2020-04-16T01:28:00Z)

this can not be solved?

---

### 评论 #2 — hrittich (2020-04-17T14:00:11Z)

This issue might be related to #1070 and #1064.

---

### 评论 #3 — jankaltoun (2020-04-25T15:38:01Z)

I had the same problem. Add yourself to both `video` and `render` groups and restart your computer so that the changes take effect.

---

### 评论 #4 — rggs (2020-04-25T18:07:36Z)

> I had the same problem. Add yourself to both `video` and `render` groups and restart your computer so that the changes take effect.

It seems that for me, there is no render group?
`usermod: group 'render' does not exist`
Is there a some extra set up I need to do? I'm on Ubuntu 18.04.4 LTS.

---

### 评论 #5 — jankaltoun (2020-04-25T18:23:30Z)

I'm on Ubuntu 20.04 but I'm not sure whether that has anything to do with it.
I basically had to (or at least I believe so) grant myself access to `/dev/kfd`.

In my case it looks like this:

`crw-rw---- 1 root render 236, 0 dub 25 17:34 /dev/kfd`

---

### 评论 #6 — pty819 (2020-04-25T19:00:10Z)

> I had the same problem. Add yourself to both `video` and `render` groups and restart your computer so that the changes take effect.

thank you！

---

### 评论 #7 — hrittich (2020-04-29T08:38:54Z)

@rsbball11 On 18.04 there is no render group. The device `/dev/kfd` is owned by the `video` group

    crw-rw-rw- 1 root video 239, 0 Apr 29  2020 /dev/kfd

---

### 评论 #8 — rodgasp (2020-05-05T05:34:50Z)

> I'm on Ubuntu 20.04 but I'm not sure whether that has anything to do with it.
> I basically had to (or at least I believe so) grant myself access to `/dev/kfd`.
> 
> In my case it looks like this:
> 
> `crw-rw---- 1 root render 236, 0 dub 25 17:34 /dev/kfd`

Hello @jankaltoun , can u please help me? I'm on 20.04 too, and just can't make it right..
I've a Rx580, and my outups are:

xphreak@xphreak:~$ groups
xphreak adm cdrom sudo dip video plugdev render lpadmin lxd sambashare

xphreak@xphreak:~$ ls -la /dev/kfd
crw-rw---- 1 root render 238, 0 mai  5 02:29 /dev/kfd

phreak@xphreak:~$ sudo /opt/rocm/bin/rocminfo 
ROCk module is loaded
xphreak is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
xphreak@xphreak:~$ 



---

### 评论 #9 — jankaltoun (2020-05-05T09:28:53Z)

@rodgasp good news is, that it must work 😄. I have the same GPU.
Maybe a sill question, but... Did you try restarting your machine? Group changes do not get applied immediately.

---

### 评论 #10 — MatPoliquin (2020-05-05T10:09:03Z)

I got it to work by installing rocm 3.1 first and then upgrading to 3.3

---

### 评论 #11 — rodgasp (2020-05-05T13:12:44Z)

> @rodgasp good news is, that it must work 😄. I have the same GPU.
> Maybe a sill question, but... Did you try restarting your machine? Group changes do not get applied immediately.

That's great, thanks for answer! So, I'm on this mission right now, installing a fresh 18.04 on the machine, I found some details that could be the problem, please tell me if you know something about it:

- On https://github.com/RadeonOpenCompute/ROCm/issues/722 , I understand that after installing ROCm without any issues dmesg | grep kfd returns the following:

[    5.737933] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[output omitted]

I tried to install the ./amdgpu-pro-install drivers, but since I was on 20.04, it wasn't possible, what takes me on the new instalation, of 18.04.. 

On the reference post:

 "I read here https://www.amd.com/en/support/kb/release-notes/amdgpu-installation that the --opencl=rocm flag must be used when installing the drivers. I'll do this and get back to you.

./amdgpu-pro-install -y --opencl=rocm 

EDIT: Using the flag made no difference this support chipset still gives the same "call returned 4104" error and rejects atomics. But It is likely due to the CPU which I didn't bother to check not being supported... Looking for some Intel Xeon E5 v3's as I type this." 

@jankaltoun Do you know if I need a specific processor to deal with Pci Atomics, to get Rocm working? I'm using a btc250pro mother board, with 12 Rx580 conected trough Pci Risers, can you tell me if that should work? What hardware setup do you use? 

Thanks again!

---

### 评论 #12 — x09zeref (2020-05-05T15:32:52Z)

**>** @rodgasp good news is, that it must work smile. I have the same GPU.
> Maybe a sill question, but... Did you try restarting your machine? Group changes do not get applied immediately.

-man..i trying follow your step to add user to render groups but after reboot, i got error when run /opt/rocm/opencl/bin/x86_64/clinfo

`Segmentation fault (core dumped)`

-on hashcat when doing benchmark, got this error 
`Cannot find an OpenCL ICD loader library`
Any solution?

ubuntu 20.04 LTS
Kernal : 5.4.0-29-generic
GPU : RX480


---

### 评论 #13 — jankaltoun (2020-05-05T15:35:02Z)

@x09zeref I'm afraid that this is beyond my current knowledge of this topic :(.

---

### 评论 #14 — x09zeref (2020-05-05T15:37:24Z)

> @x09zeref I'm afraid that this is above my current knowledge of this topic :(.

thanks for replay man.. worked well on ubuntu 18.04, but still issue with openCL on 20.04.. so hoping ROCm will release update for latest kernal in future..

---

### 评论 #15 — jhonny-oliveira (2020-05-05T22:02:29Z)

> I got it to work by installing rocm 3.1 first and then upgrading to 3.3

Where did you get 3.1? Here I can only find 3.3: http://repo.radeon.com/rocm/apt/debian.

---

### 评论 #16 — Rmalavally (2020-05-05T22:26:18Z)

You have to traverse one repo above debian to access links to all ROCm releases. 
Debian points to the latest release.

Try https://repo.radeon.com/rocm/apt/3.1/ 

---

### 评论 #17 — jhonny-oliveira (2020-05-06T06:55:01Z)

> You have to traverse one repo above debian to access links to all ROCm releases.
> Debian points to the latest release.
> 
> Try https://repo.radeon.com/rocm/apt/3.1/

Thanks!

---

### 评论 #18 — faust3 (2020-10-03T16:53:31Z)

For me it did not work as root.
But I got a similar message with Ubuntu 20.04 and Ryzen2400g.
When I set the option amdgpu cwsr_enable=0, I was at least able to execute rocminfo.

---

### 评论 #19 — ROCmSupport (2021-03-17T07:45:54Z)

Thank you all for the responses.
I understood that issue is resolved already.
For the best experience, request you to try with the latest ROCm 4.0.
Thank you.

---
