# ROCm installation fails on Debian buster/sid

> **Issue #631**
> **状态**: closed
> **创建时间**: 2018-12-08T23:11:47Z
> **更新时间**: 2021-07-19T13:37:46Z
> **关闭时间**: 2021-01-07T10:35:02Z
> **作者**: RBKreckel
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/631

## 描述

On Debian/testing, apt install rocm-dkms fails with
Error! Bad return status for module build on kernel: 4.18.0-3-amd64 (amd64)
Consult /var/lib/dkms/amdgpu/1.9-307/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10

I attach the file
[make.log](https://github.com/RadeonOpenCompute/ROCm/files/2660115/make.log)


---

## 评论 (15 条)

### 评论 #1 — valeriob01 (2018-12-09T14:26:23Z)

ROCm works in Debian buster with kernel 4.19.0-rc7

---

### 评论 #2 — valeriob01 (2018-12-11T18:34:48Z)

Works also with kernel 4.19.5

---

### 评论 #3 — jlgreathouse (2018-12-11T19:40:41Z)

ROCm is not officially supported on Debian. However, as @valeriob01 notes, you should be able to [use the upstream kernel](https://github.com/RadeonOpenCompute/ROCm/tree/roc-1.9.1#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels). To do that, do not install the `rocm-dkms` module. Instead, install just the `rocm-dev` module and follow the directions in that link to set up your udev rules.

---

### 评论 #4 — valeriob01 (2018-12-12T08:36:56Z)

> ROCm is not officially supported on Debian. However, as @valeriob01 notes, you should be able to [use the upstream kernel](https://github.com/RadeonOpenCompute/ROCm/tree/roc-1.9.1#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels). To do that, do not install the `rocm-dkms` module. Instead, install just the `rocm-dev` module and follow the directions in that link to set up your udev rules.

I have followed the standard procedure: installed rocm-dkms and libnuma-dev.


---

### 评论 #5 — kochd (2018-12-12T08:59:38Z)

I think i was getting the same error (cant check right now).
Could anybody clarify:
<pre>
/var/lib/dkms/amdgpu/1.9-307/build/amd/amdgpu/amdgpu_drv.c:769:2: error: implicit declaration of function ‘vga_switcheroo_set_dynamic_switch’; did you mean ‘vga_switcheroo_process_delayed_switch’? [-Werror=implicit-function-declaration]
  vga_switcheroo_set_dynamic_switch(pdev, VGA_SWITCHEROO_OFF);
  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  vga_switcheroo_process_delayed_switch
</pre>

---

### 评论 #6 — jlgreathouse (2018-12-12T16:59:31Z)

@valeriob01 That's somewhat surprising. I guess what might be happening is that your `rock-dkms` installation silently fails but all of the other packages work correctly. At that point, the upstream `amdgpu` and `amdkfd` drivers will still be installed, and all your user-level software will work with them.

I would wager if you run `dkms status`, you will find that the `amdgpu/1.9-307` package will not be listed as "installed".

@kochd Yes, that error is because you are trying to use a kernel newer than 4.15, which our `rock-dkms` package does not support. If you are running a newer kernel ([as noted above](https://github.com/RadeonOpenCompute/ROCm/issues/631#issuecomment-446334686)) you can likely skip this step. You will lose some of our features that have not been upstreamed yet, but our user-level ROCm software should work.

---

### 评论 #7 — valeriob01 (2018-12-12T18:02:40Z)

> @valeriob01 That's somewhat surprising. I guess what might be happening is that your `rock-dkms` installation silently fails but all of the other packages work correctly. At that point, the upstream `amdgpu` and `amdkfd` drivers will still be installed, and all your user-level software will work with them.
> 
> I would wager if you run `dkms status`, you will find that the `amdgpu/1.9-307` package will not be listed as "installed".
> 

dkms status  shows 

amdgpu/1.9-307: added

So what to do at this point ?


---

### 评论 #8 — jlgreathouse (2018-12-12T18:05:04Z)

@valeriob01 That means the DKMS driver provided by `rock-dkms` was added, but the build failed and it was not installed. As such, you are using your upstream 4.19 driver. That's what I expected. I don't think that's a problem, since you've said ROCm user-level tools are working for you. Things like this are one of the main reasons we worked to upstream our driver. :)

That said, there are some features that have not been upstreamed yet. If you want those features, you may need to either wait until our `rock-dkms` module supports newer kernels, or you may need to downgrade your kernel to 4.15.

---

### 评论 #9 — valeriob01 (2018-12-12T18:40:16Z)

The program run fine, maybe the performance is inferior.


---

### 评论 #10 — RBKreckel (2018-12-13T21:58:31Z)

> ROCm is not officially supported on Debian. However, as @valeriob01 notes, you should be able to [use the upstream kernel](https://github.com/RadeonOpenCompute/ROCm/tree/roc-1.9.1#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels). To do that, do not install the `rocm-dkms` module. Instead, install just the `rocm-dev` module and follow the directions in that link to set up your udev rules.

Ah, indeed, that works. Thanks a lot!

(Next thing on my agenda: Try to find out why GEGL still doesn't enable image support.)

---

### 评论 #11 — Infro (2019-02-01T00:42:30Z)

I tried modifying the DKMS code for Debian buster 4.19, but when starting X I get an error message of AMDGPU Flip failed.  Changes at https://github.com/Infro/ROCK-Kernel-Driver/commit/864174b9ead77cbb596baa422a175fa8525b76ae

My changes are just hacks to get try and get things to work, and doubt if I've covered all the bases, but hope that someone more knowledgeable might look at it, as there were very few changes I had to do to get it to compile...  If anyone else wants to try with my changes and are hoping for better, I'd be willing to help, but at your own risk.

---

### 评论 #12 — minzak (2019-03-24T18:39:17Z)

Yes, debian with kernel 4.19.x (latest **strech-updates**) with latest ROCm 2.0.1 not work if i install with  rocm-dkms.
But after install with **rocm-dkms** - all is works!
And not forget to modified **os-release** file to ubuntu before run `update-initramfs -u`

Works rocminfo and etc.

But after reboot - not work, just reboot after several seconds after boot, and it is also in recover mode.
It is latest screen before reboot.
![Untitled](https://user-images.githubusercontent.com/12154217/54884006-545c0380-4e74-11e9-9807-ac7fad082bb7.png)

If not use rocm-dkms - works after reboot.
But what different in this 2 way?


---

### 评论 #13 — ROCmSupport (2021-01-07T10:35:02Z)

Thank you all for the verification and confirming that issue is no more observed.
I am closing this now.
Request to open a new issue, if any, in future.
Thank you.

---

### 评论 #14 — JLT032 (2021-04-26T06:30:56Z)

the reason rocm does not install on Debian 10/Buster is a dependency on libpython3.8. I manually installed python3.8 but apt does not check /usr/local/lib to find the dependency exists there already for libpython3.8

---

### 评论 #15 — blattms (2021-07-19T13:36:45Z)

@commandline-be Had the same problem when trying to install rocm-dev as described in the [installation nodes ](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#using-debian-based-rocm-with-upstream-kernel-drivers) You have to choose version rocm-dev in version 3.7 on Debian buster (for all later versions rocm-gdb has the dependecy on libpython3.8) You can do that by requiring a specific version in /etc/apt/sources.list.d/rocm.list:
```
deb [arch=amd64] http://repo.radeon.com/rocm/apt/3.7 xenial main
```

It probably also works to not install rocm-dev but all packages that it depends on except rocm-gdb for later versions. Have not really checked that.

---
