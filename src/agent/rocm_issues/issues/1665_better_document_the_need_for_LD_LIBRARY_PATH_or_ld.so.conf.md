# better document the need for LD_LIBRARY_PATH or ld.so.conf

> **Issue #1665**
> **状态**: closed
> **创建时间**: 2022-02-03T08:45:12Z
> **更新时间**: 2024-10-29T14:17:09Z
> **关闭时间**: 2024-10-29T14:17:09Z
> **作者**: bgoglin
> **标签**: Under Investigation, Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1665

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Documentation** (颜色: #5319e7)

## 描述

Hello
We're using rsmilib in hwloc, and hwloc is used in MPI. Some MPI users are surprised to see rsmi-related link error at runtime (they don't even know MPI uses hwloc). The issue is that some platforms don't have the path of lib rsmi in LD_LIBRARY_PATH or ld.so.conf. That's easy to fix, but it's not something that end-user should do here, since they don't use rsmi directly. It's rather something to fix on the admin side, the one who installed MPI and/or hwloc.

I see in https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#post-install-actions-and-verification-process that "Users might set LD_LIBRARY_PATH to load the ROCm library version of choice." but I think this should be improved:
* change "might" into something stronger, maybe make it mandatory like competitors do
* talk about /etc/ld.so.conf being an easier alternative for admins
* say that RPM/DEB packages take care of adding the relevant files in /etc/ld.so.conf.d/rocm-foo.conf (I don't see it installed on platforms I have access to, but I see the code in your github repos).

Thanks
Brice


---

## 评论 (17 条)

### 评论 #1 — bgoglin (2022-02-03T08:53:45Z)

By the way, platforms I have access to didn't install /etc/ld.so.conf.d/x86_64-librocm_smi_lib.conf because ENABLE_LDCONFIG was OFF when building the rocm-smi-lib debian package, why don't you enable it?

---

### 评论 #2 — Maxzor (2022-02-03T09:01:35Z)

I believe that the correct way to do this is to install the library in a default path found in default ld.so.conf.d - no need for new entries, or even just a default lib directory such as plain /usr/lib.
And evolved installations such as the spack ones use RPATH.

---

### 评论 #3 — sofiageo (2022-02-16T10:45:20Z)

~~I've found that librocalution.so for ROCm 5.0.0 (Ubuntu release) is missing the RPATH rocm lib paths. So some software (e.g Pytorch, JuliaGPU) won't run if you don't set LD_LIBRARY_PATH as well.~~

edit: for some reason that was just temporary, and I have no idea what caused it. It works fine after a couple of days.

---

### 评论 #4 — Maxzor (2022-02-17T11:24:27Z)

The answer, in traditional Linux distributions, to the installation topic, is to have the libraries be installed in paths that are automatically found by the linker defaults.
This is not playing with rpath, nor LD_LIBRARY_PATH, nor even adding new entries to /etc/ld.so.conf.d.

We are having [extensive discussions](https://lists.debian.org/debian-ai/2022/02/msg00065.html) between ROCm and Debian developers to install the ROCm stack in such default locations, that will abide better by Linux distribution expectations.

---

### 评论 #5 — sofiageo (2022-02-19T11:22:36Z)

I'm still confused about the current situation. I'm trying to provide a package for users of Arch Linux that works, based on the Ubuntu release. I guess the only way at the moment is to ask them to manually set the LD_LIBRARY_PATH to every ROCm library path in `/opt/rocm` - if what gboglin says is correct (that the libraries are missing ENABLE_LDCONFIG). Adding the library paths in `ld.so.conf` doesn't seem to make a difference.

Feel free to link any article or blog post that will make me more educated on the subject. Thanks

---

### 评论 #6 — bgoglin (2022-02-19T11:49:36Z)

@sofiageo If you're building your own Arch packages, you should be enable to set ENABLE_LDCONFIG. I was talking about the Debian packages build by AMD, those don't have ENABLE_LDCONFIG.

---

### 评论 #7 — sofiageo (2022-02-19T11:57:51Z)

> @sofiageo If you're building your own Arch packages, you should be enable to set ENABLE_LDCONFIG. I was talking about the Debian packages build by AMD, those don't have ENABLE_LDCONFIG.

I'm not building the packages, I'm using the Ubuntu packages built by AMD. It's a quick way to provide ROCm binaries to people, I know there will probably be some other issues like P2P for devices not working, but for the most part this practice works. (ROCr OpenCL works / HIP works / etc). The package is `opencl-amd` and [opencl-amd-dev](https://aur.archlinux.org/packages/opencl-amd-dev) from AUR.

edit: I'll try to add every library separately to ld.so.conf and see if it makes any difference. Maybe the problem is I only add `/opt/rocm/lib` and `/opt/rocm/hip/lib` and that doesn't follow symlinks?

edit2: I think I understand what's going on. `ld.so.conf` works fine, but symlinks for all libraries are not present in `/opt/rocm/lib`, so you need to know which libraries need to be added to `ld.so.conf` files. Setting LD_LIBRARY_PATH overrides the [library search order](https://datacadamia.com/os/linux/so#search_path). If an application doesn't work without LD_LIBRARY_PATH it means that probably it is using wrong library paths from the RPATH of the executable, which is picked before the `ld.so.conf` files.

---

### 评论 #8 — klausbu (2023-02-18T14:34:22Z)

I have a related issue:

I want to overwrite the default library location of  rocThrust /opt/rocm-5.4.0/include/thrust  with the location of my custom version located at /opt/rocm-5.4.0/myspecialrocm/include/thrust/

The following approaches have no effect, the hipcc compiler keeps using the default version:

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm-5.4.0/myspecialrocm/include/thrust/  OR the hipcc parameter -I=/opt/rocm-5.4.0/myspecialrocm/include/thrust

How can I overwrite the default paths of selected libraries to be able to compile programs with my custom versions?

---

### 评论 #9 — spirosbond (2024-06-01T15:28:17Z)

If you are here because of the below error when running rocm-smi:
```
Unable to load the rocm_smi library.
Set LD_LIBRARY_PATH to the folder containing librocm_smi64.so.1
Please refer to https://github.com/RadeonOpenCompute/rocm_smi_lib for the installation guide.

```

I managed to fix it by:
1. Installing python 3.11. I had the issue with python 3.12
2. Updating the libgcc to its latest version. 

For point 2, if you are running conda/miniconda you might need to use the conda-forge channel since it has a later version:
`conda install -c conda-forge libstdcxx-ng`

After that, rocm-smi works as expected.

---

### 评论 #10 — ppanchad-amd (2024-07-03T19:25:13Z)

@bgoglin Is your issue resolved in the latest rocm 6.1.2. Thanks!

---

### 评论 #11 — bgoglin (2024-07-03T19:33:58Z)

@ppanchad-amd Can you point to some doc changes relevant to the issue?

---

### 评论 #12 — ppanchad-amd (2024-07-03T20:04:05Z)

@bgoglin Link you have in your original post is no longer accessible.

This is the current documentation for installing ROCm SMI: https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/install/install.html

Please confirm if this the document where you'd prefer your below changes to be made:
->change "might" into something stronger, maybe make it mandatory like competitors do
->talk about /etc/ld.so.conf being an easier alternative for admins
->say that RPM/DEB packages take care of adding the relevant files in /etc/ld.so.conf.d/rocm-foo.conf (I don't see it installed on platforms I have access to, but I see the code in your github repos).

---

### 评论 #13 — bgoglin (2024-07-06T07:14:00Z)

@ppanchad-amd Yes, looks like the place to apply such changes.

---

### 评论 #14 — ppanchad-amd (2024-07-08T14:20:51Z)

@bgoglin Created internal ticket to fix documentation. Thanks!

---

### 评论 #15 — sohaibnd (2024-10-24T22:22:02Z)

Hi @bgoglin, how exactly are you getting librocm_smi64.so? are your building it from source or installing ROCm using the instructions in the [docs](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html)? The most recent ROCm installation instructions already mention that users have to configure the dynamic linker using ldconfig ([source](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/post-install.html)).

---

### 评论 #16 — bgoglin (2024-10-25T06:01:21Z)

@sohaibnd Looks good to me then. I guess you may close this issue, thanks.

---

### 评论 #17 — sohaibnd (2024-10-29T14:15:30Z)

@bgoglin Great, please feel free to create another ticket if you find missing/lacking documentation for anything else!

---
