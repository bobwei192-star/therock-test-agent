# sudo: amdgpu-uninstall: command not found

> **Issue #1914**
> **状态**: closed
> **创建时间**: 2023-03-03T12:47:46Z
> **更新时间**: 2024-06-27T13:21:15Z
> **关闭时间**: 2024-06-27T13:21:15Z
> **作者**: Enferlain
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1914

## 标签

- **Documentation** (颜色: #5319e7)

## 负责人

- MathiasMagnus

## 描述

Trying to get rocm working for something ai related, I'm on ubuntu 22.10, ran these commands 

> sudo apt-get update
> wget https://repo.radeon.com/amdgpu-install/5.4.3/ubuntu/jammy/amdgpu-install_5.4.50403-1_all.deb 
> sudo apt-get install ./amdgpu-install_5.4.50403-1_all.deb

At the end it puts "download is performed unsandboxed as root as file"

But when I check it says I have it installed 

![image](https://user-images.githubusercontent.com/15861396/222723770-d106d964-38b9-4f07-86e4-869e46c9670e.png)

I'm trying to remove it for troubleshooting with "sudo amdgpu-uninstall --rocmrelease=5.4.3" but it says "sudo: amdgpu-uninstall: command not found"

Why is that?


---

## 评论 (9 条)

### 评论 #1 — arch-user-france1 (2023-03-03T16:55:07Z)

Perhaps it's not in the `PATH` which is the variable the shell interpreter checks for binary files to run. Could you please try to run the command without `sudo`?
Please also show us your `$PATH` variable: `echo $PATH`.

You could try searching for the command in the folder `/opt`.

---

### 评论 #2 — alexschroeter (2023-03-03T17:05:08Z)

I usually don't install like this so I cannot check but in another issue, someone mentioned that it is actually. https://github.com/RadeonOpenCompute/ROCm/issues/1908#issuecomment-1435957473

`sudo amdgpu-install --uninstall`

---

### 评论 #3 — Enferlain (2023-03-04T11:47:14Z)

> Perhaps it's not in the `PATH` which is the variable the shell interpreter checks for binary files to run. Could you please try to run the command without `sudo`? Please also show us your `$PATH` variable: `echo $PATH`.
> 
> You could try searching for the command in the folder `/opt`.

![Screenshot from 2023-03-04 12-45-45](https://user-images.githubusercontent.com/15861396/222898432-47dd0bcc-ebe7-46d1-bafe-ccea175b5455.png)



> I usually don't install like this so I cannot check but in another issue, someone mentioned that it is actually. [#1908 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1908#issuecomment-1435957473)
> 
> `sudo amdgpu-install --uninstall`

This one works, prompts me to remove the 15gb of stuff, thanks!

---

### 评论 #4 — saadrahim (2023-05-25T02:59:44Z)

Reopening to ensure this is included in our documentation.

---

### 评论 #5 — saadrahim (2024-01-24T20:38:31Z)

@MathiasMagnus  is this still valid, can you assign to someone to check?

---

### 评论 #6 — kentrussell (2024-01-29T15:05:40Z)

Some of the release packages didn't include amdgpu-uninstall. The Packaging guys (e.g. @Mystro256) can check if it got legacied or whatever. But "amdgpu-install --uninstall" will always be present.

---

### 评论 #7 — MathiasMagnus (2024-02-06T14:11:50Z)

We [don't `wget` unsandboxed](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/amdgpu-install.html#installation) anymore in the docs, neither do we document the use of the removed utility and use [`amdgpu-install --uninstall`](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/amdgpu-install.html#uninstalling-rocm)

@Enferlain Do these address your concern?

---

### 评论 #8 — ppanchad-amd (2024-05-10T15:07:45Z)

Internal ticket has been created to update documentation. Thanks!

---

### 评论 #9 — harkgill-amd (2024-06-27T13:21:15Z)

Documentation [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/amdgpu-install.html#uninstalling-rocm) now points to the correct command "sudo amdgpu-install --uninstall". 

---
