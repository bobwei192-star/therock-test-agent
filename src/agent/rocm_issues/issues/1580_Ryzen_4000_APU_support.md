# Ryzen 4000 APU support

> **Issue #1580**
> **状态**: closed
> **创建时间**: 2021-09-26T14:48:48Z
> **更新时间**: 2022-06-14T02:19:24Z
> **关闭时间**: 2021-10-11T07:55:38Z
> **作者**: Etaash-mathamsetty
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1580

## 描述

If I read correctly ryzen 4000 APUs are not supported. Are there any plans to support them in the future and if not, what opencl ICD should I use? (mesa doesn't work btw)

---

## 评论 (13 条)

### 评论 #1 — ROCmSupport (2021-09-27T11:05:38Z)

Thanks @Etaash-mathamsetty for reaching out.
I certainly understood the problem.
I will check with BU team and share some update on this soon.
Thank you.

---

### 评论 #2 — Etaash-mathamsetty (2021-10-06T00:26:00Z)

> Thanks @Etaash-mathamsetty for reaching out. I certainly understood the problem. I will check with BU team and share some update on this soon. Thank you.

Any update?

---

### 评论 #3 — ROCmSupport (2021-10-06T01:49:27Z)

Hi @Etaash-mathamsetty 
Got update that we are not supporting Ryzen 4000 APUs for now with ROCm.
I can not comment about future plans. Request you to follow our documentation for updates.
Thank you.

---

### 评论 #4 — Etaash-mathamsetty (2021-10-08T01:18:32Z)

Does anybody know what I opencl icd I should use then???

---

### 评论 #5 — a-repko (2021-10-08T23:31:30Z)

Hi @Etaash-mathamsetty , I have a more-or-less good experience with extracted OpenCL from AMDGPU-PRO 20.40 in Gentoo Linux. An installation script can be downloaded here:
[https://gist.github.com/kytulendu/3351b5d0b4f947e19df36b1ea3c95cbe/1a921fc0b51ed29af494723c4486388ad3ac43d0](https://gist.github.com/kytulendu/3351b5d0b4f947e19df36b1ea3c95cbe/1a921fc0b51ed29af494723c4486388ad3ac43d0)
I suggest you to uninstall rocm-opencl-runtime component before (but it may work anyway). Newer versions of that driver (20.45 etc) contain an integrated ROCm component in order to support RDNA 2 (Navi 2, or RX 6000 series), so its probably better to stay at 20.40 to avoid collisions and problems (except if you have that discrete graphics as well).

I only noticed one problem: If I had an X-console running in parallel, then running OpenCL in a text console killed the X-server. So you should perhaps go either all-text or all-graphics.

Now, one comment about kernels: You need at least 5.8, which also gives a correct number of CU in rocminfo. Newer kernels (tried up to 5.11) give nonsensical +20 CU, but it doesn't appear to impact functionality.

That said, I managed to run certain OpenCL tasks with ROCm as well (tried in text-only mode; it is a bit slower then amdpro, except if your code is optimized with assembly):
- kernel 5.8.18 + ROCm 4.2: First I needed to run `clinfo`, which caused a GPU reset (i.e., screen flickering); then I was able to run `mfakto` program, but not `gpuowl`
- [faint memories] kernel 5.11 + ROCm 4.1 was probably able to run `gpuowl`, while spitting a lot of warning messages
- see also #883, #1101
- haven't tried 4.3 or 4.3.1

By the way, Ryzen 2000 APU series (Raven Ridge) is well supported in terms of OpenCL from ROCm 3.10 onwards.

---

### 评论 #6 — ROCmSupport (2021-10-11T07:55:38Z)

I am closing this now as there is no official support of Ryzen 4000 APUs for now with ROCm now.
Feel feel to open a new issue, for any, for quick resolutions.
Thank you.

---

### 评论 #7 — Etaash-mathamsetty (2021-10-12T22:03:31Z)

> Hi @Etaash-mathamsetty , I have a more-or-less good experience with extracted OpenCL from AMDGPU-PRO 20.40 in Gentoo Linux. An installation script can be downloaded here: https://gist.github.com/kytulendu/3351b5d0b4f947e19df36b1ea3c95cbe/1a921fc0b51ed29af494723c4486388ad3ac43d0 I suggest you to uninstall rocm-opencl-runtime component before (but it may work anyway). Newer versions of that driver (20.45 etc) contain an integrated ROCm component in order to support RDNA 2 (Navi 2, or RX 6000 series), so its probably better to stay at 20.40 to avoid collisions and problems (except if you have that discrete graphics as well).
> 
> I only noticed one problem: If I had an X-console running in parallel, then running OpenCL in a text console killed the X-server. So you should perhaps go either all-text or all-graphics.
> 
> Now, one comment about kernels: You need at least 5.8, which also gives a correct number of CU in rocminfo. Newer kernels (tried up to 5.11) give nonsensical +20 CU, but it doesn't appear to impact functionality.
> 
> That said, I managed to run certain OpenCL tasks with ROCm as well (tried in text-only mode; it is a bit slower then amdpro, except if your code is optimized with assembly):
> 
> * kernel 5.8.18 + ROCm 4.2: First I needed to run `clinfo`, which caused a GPU reset (i.e., screen flickering); then I was able to run `mfakto` program, but not `gpuowl`
> * [faint memories] kernel 5.11 + ROCm 4.1 was probably able to run `gpuowl`, while spitting a lot of warning messages
> * see also [Ryzen APU can not run ROCm? ( clinfo segmentation fault core dumped) #883](https://github.com/RadeonOpenCompute/ROCm/issues/883), [Is there a support plan for Renoir apu ? #1101](https://github.com/RadeonOpenCompute/ROCm/issues/1101)
> * haven't tried 4.3 or 4.3.1
> 
> By the way, Ryzen 2000 APU series (Raven Ridge) is well supported in terms of OpenCL from ROCm 3.10 onwards.

I run into vram issues with that, and it usually ends up freezing linux and forcing me to do a forced shutdown.
and 20.40 dosen't support ubuntu 21.04 or my 5.14 kernel
rocm-dkms dosen't install on my 5.14 kernel and ended up bricking my linux install
anything other than amd works fine (pocl works, mesa kinda works(I need image support))

---

### 评论 #8 — Etaash-mathamsetty (2021-11-04T00:42:52Z)

I switched to arch
and this script kills arch
every single time

---

### 评论 #9 — a-repko (2021-11-06T00:48:19Z)

OK, I suppose that it is well understood that one should be careful when running a random installation script from the web (more so if it isn't from a well respected source). In fact, I first ran this script (in Gentoo Linux) manually line-by-line to be sure what's going on. So I see that it is better to provide a step-by-step manual installation here instead of a script. In any case I'm not forcing anybody to do it - I'm just giving the procedure which enabled me to get working OpenCL on APU Renoir (4650G, 4750G) and also Cezanne (5700G); this "PAL" OpenCL is also a faster alternative to ROCm for some workloads on R9 Nano (Fiji, gfx803), Vega 56/64 and Radeon VII. I tested it with kernels 5.8 (Renoir) and 5.10 (Cezanne), so I don't know if it works with the newer ones. By the way, with regard to ROCm OpenCL on Renoir - it seems that it works somewhere sometimes (Cezanne is even worse) - it apparently depends also on the motherboard/BIOS - one program may work in one configuration, but not the other, and vice versa (my experience listed above actually involved different motherboards).

So here is the extraction and installation of PAL OpenCL (I removed Vulkan, it proved to be unnecessary):
1. download AMDGPU-PRO 20.40 and extract it to some temporary directory
<pre>wget --referer https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-20-40 https://drivers.amd.com/drivers/linux/amdgpu-pro-20.40-1147286-ubuntu-20.04.tar.xz
tar xJf amdgpu-pro-20.40-1147286-ubuntu-20.04.tar.xz</pre>
2. prepare directories `/opt/amdgpu` and `/opt/amdgpu-pro` - i.e., if they are present, uninstall corresponding packages or take care not to replace existing files by the ones listed below; if they are not present, create them (including the needed subdirectories). In the steps below, I recommend to create a separate (temporary) directory tree for /opt and /etc, which can be saved and employed for repeated installs of this OpenCL
3. extract files from *.deb archives by means of
<pre>ar x package.deb
tar xJvf data.tar.xz</pre>
namely:
- extract `libdrm_amdgpu.so.1.0.0` from `libdrm-amdgpu-amdgpu1_2.4.100-1147286_amd64.deb`, then rename and place it to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm_amdpro.so.1.0.0`
- extract `libdrm_amdgpu.so.1.0.0` from `libdrm-amdgpu-amdgpu1_2.4.100-1147286_i386.deb`, then rename and place it to `/opt/amdgpu-pro/lib/i386-linux-gnu/libdrm_amdpro.so.1.0.0`
- extract `amdgpu.ids` from `libdrm-amdgpu-common_1.0.0-1147286_all.deb`, and place it to `/opt/amdgpu/share/libdrm/`
- extract `libamd_comgr.so.1.7.0` from `opencl-amdgpu-pro-comgr_20.40-1147286_amd64.deb`, and place it to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/`
- extract `libamdocl64.so` from `opencl-amdgpu-pro-icd_20.40-1147286_amd64.deb`, and place it to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/`
- extract `libamdocl-orca64.so` and `libamdocl12cl64.so` from `opencl-orca-amdgpu-pro-icd_20.40-1147286_amd64.deb`, and place them to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/`
- extract `libamdocl-orca32.so` and `libamdocl12cl32.so` from `opencl-orca-amdgpu-pro-icd_20.40-1147286_i386.deb`, and place them to `/opt/amdgpu-pro/lib/i386-linux-gnu/`
4. create files with simple text contents:
- `/etc/OpenCL/vendors/amdocl64.icd` containing `libamdocl64.so` (this file can be present from rocm-opencl-runtime, in which case you can simply keep it)
- `/etc/OpenCL/vendors/amdocl-orca64.icd` containing `libamdocl-orca64.so`
- `/etc/OpenCL/vendors/amdocl-orca32.icd` containing `libamdocl-orca32.so`
- `/etc/ld.so.conf.d/zz_amdgpu-pro_x86_64.conf` containing
<pre># AMDGPU-PRO OpenCL support
/opt/amdgpu-pro/lib/x86_64-linux-gnu</pre>
- `/etc/ld.so.conf.d/zz_amdgpu-pro_x86.conf` containing
<pre># AMDGPU-PRO OpenCL support
/opt/amdgpu-pro/lib/i386-linux-gnu</pre>
5. create symbolic links and modify the binaries to use "amdpro" instead of "amdgpu":
- in `/opt/amdgpu-pro/lib/i386-linux-gnu/`:
<pre>ln -s libdrm_amdpro.so.1.0.0 libdrm_amdpro.so.1
sed -i "s|libdrm_amdgpu|libdrm_amdpro|g" libamdocl-orca32.so</pre>
- in `/opt/amdgpu-pro/lib/x86_64-linux-gnu`:
<pre>ln -s libdrm_amdpro.so.1.0.0 libdrm_amdpro.so.1
ln -s libamd_comgr.so.1.7.0 libamd_comgr.so
sed -i "s|libdrm_amdgpu|libdrm_amdpro|g" libamdocl-orca64.so</pre>
6. now if you didn't copy the files above to the real directories `/etc` and `/opt`, do it now, and then run
`ldconfig`


---

### 评论 #10 — Etaash-mathamsetty (2021-11-14T03:50:13Z)

> OK, I suppose that it is well understood that one should be careful when running a random installation script from the web (more so if it isn't from a well respected source). In fact, I first ran this script (in Gentoo Linux) manually line-by-line to be sure what's going on. So I see that it is better to provide a step-by-step manual installation here instead of a script. In any case I'm not forcing anybody to do it - I'm just giving the procedure which enabled me to get working OpenCL on APU Renoir (4650G, 4750G) and also Cezanne (5700G); this "PAL" OpenCL is also a faster alternative to ROCm for some workloads on R9 Nano (Fiji, gfx803), Vega 56/64 and Radeon VII. I tested it with kernels 5.8 (Renoir) and 5.10 (Cezanne), so I don't know if it works with the newer ones. By the way, with regard to ROCm OpenCL on Renoir - it seems that it works somewhere sometimes (Cezanne is even worse) - it apparently depends also on the motherboard/BIOS - one program may work in one configuration, but not the other, and vice versa (my experience listed above actually involved different motherboards).
> 
> So here is the extraction and installation of PAL OpenCL (I removed Vulkan, it proved to be unnecessary):
> 
> 1. download AMDGPU-PRO 20.40 and extract it to some temporary directory
> 
> wget --referer https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-20-40 https://drivers.amd.com/drivers/linux/amdgpu-pro-20.40-1147286-ubuntu-20.04.tar.xz
> tar xJf amdgpu-pro-20.40-1147286-ubuntu-20.04.tar.xz
> 1. prepare directories `/opt/amdgpu` and `/opt/amdgpu-pro` - i.e., if they are present, uninstall corresponding packages or take care not to replace existing files by the ones listed below; if they are not present, create them (including the needed subdirectories). In the steps below, I recommend to create a separate (temporary) directory tree for /opt and /etc, which can be saved and employed for repeated installs of this OpenCL
> 2. extract files from *.deb archives by means of
> 
> ar x package.deb
> tar xJvf data.tar.xz
> namely:
> 
> * extract `libdrm_amdgpu.so.1.0.0` from `libdrm-amdgpu-amdgpu1_2.4.100-1147286_amd64.deb`, then rename and place it to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm_amdpro.so.1.0.0`
> * extract `libdrm_amdgpu.so.1.0.0` from `libdrm-amdgpu-amdgpu1_2.4.100-1147286_i386.deb`, then rename and place it to `/opt/amdgpu-pro/lib/i386-linux-gnu/libdrm_amdpro.so.1.0.0`
> * extract `amdgpu.ids` from `libdrm-amdgpu-common_1.0.0-1147286_all.deb`, and place it to `/opt/amdgpu/share/libdrm/`
> * extract `libamd_comgr.so.1.7.0` from `opencl-amdgpu-pro-comgr_20.40-1147286_amd64.deb`, and place it to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/`
> * extract `libamdocl64.so` from `opencl-amdgpu-pro-icd_20.40-1147286_amd64.deb`, and place it to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/`
> * extract `libamdocl-orca64.so` and `libamdocl12cl64.so` from `opencl-orca-amdgpu-pro-icd_20.40-1147286_amd64.deb`, and place them to `/opt/amdgpu-pro/lib/x86_64-linux-gnu/`
> * extract `libamdocl-orca32.so` and `libamdocl12cl32.so` from `opencl-orca-amdgpu-pro-icd_20.40-1147286_i386.deb`, and place them to `/opt/amdgpu-pro/lib/i386-linux-gnu/`
> 
> 1. create files with simple text contents:
> 
> * `/etc/OpenCL/vendors/amdocl64.icd` containing `libamdocl64.so` (this file can be present from rocm-opencl-runtime, in which case you can simply keep it)
> * `/etc/OpenCL/vendors/amdocl-orca64.icd` containing `libamdocl-orca64.so`
> * `/etc/OpenCL/vendors/amdocl-orca32.icd` containing `libamdocl-orca32.so`
> * `/etc/ld.so.conf.d/zz_amdgpu-pro_x86_64.conf` containing
> 
> # AMDGPU-PRO OpenCL support
> /opt/amdgpu-pro/lib/x86_64-linux-gnu
> * `/etc/ld.so.conf.d/zz_amdgpu-pro_x86.conf` containing
> 
> # AMDGPU-PRO OpenCL support
> /opt/amdgpu-pro/lib/i386-linux-gnu
> 1. create symbolic links and modify the binaries to use "amdpro" instead of "amdgpu":
> 
> * in `/opt/amdgpu-pro/lib/i386-linux-gnu/`:
> 
> ln -s libdrm_amdpro.so.1.0.0 libdrm_amdpro.so.1
> sed -i "s|libdrm_amdgpu|libdrm_amdpro|g" libamdocl-orca32.so
> * in `/opt/amdgpu-pro/lib/x86_64-linux-gnu`:
> 
> ln -s libdrm_amdpro.so.1.0.0 libdrm_amdpro.so.1
> ln -s libamd_comgr.so.1.7.0 libamd_comgr.so
> sed -i "s|libdrm_amdgpu|libdrm_amdpro|g" libamdocl-orca64.so
> 1. now if you didn't copy the files above to the real directories `/etc` and `/opt`, do it now, and then run
>    `ldconfig`

that's exactly what I suspected, the amdgpu-pro vulkan causes arch linux to fail. But even if I read over the script there was no way to realize that. 
Anyway, the way I did it was using the 20.40 version from the aur. (thank you arch linux for keeping old versions)
Then I disabled updates for opencl-amd

---

### 评论 #11 — Etaash-mathamsetty (2022-06-05T22:01:47Z)

this now works using opencl-amd 22.10.3 on the AUR, I only have 512 MB of vram though, any for ROCM to use my system ram? (I cannot expand my vram size since my laptop's bios is retarded)

---

### 评论 #12 — crackleware (2022-06-14T01:18:40Z)

@Etaash-mathamsetty maybe you can upgrade your BIOS? i had to do that to increase VRAM on my ThinkCentre system with AMD Ryzen 5 PRO 4650GE with Radeon Graphics. then i selected 2G in BIOS settings for VRAM and i currently see 1983M VRAM in `radeontop`.

---

### 评论 #13 — Etaash-mathamsetty (2022-06-14T02:19:24Z)

> @Etaash-mathamsetty maybe you can upgrade your BIOS? i had to do that to increase VRAM on my ThinkCentre system with AMD Ryzen 5 PRO 4650GE with Radeon Graphics. then i selected 2G in BIOS settings for VRAM and i currently see 1983M VRAM in `radeontop`.

I am already running the latest bios lol

---
