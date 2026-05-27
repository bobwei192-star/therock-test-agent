# linux kernel notice

> **Issue #1307**
> **状态**: closed
> **创建时间**: 2020-11-27T02:32:10Z
> **更新时间**: 2021-03-15T06:29:27Z
> **关闭时间**: 2020-12-11T04:35:15Z
> **作者**: clzstc123
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1307

## 描述

ubuntu 20.04
linux-image-5.4.0-54-generic        rocm-dkms,it's work
linux-image-5.4.0-57-generic        rocm-dkms,it does't work

---

## 评论 (21 条)

### 评论 #1 — ROCmSupport (2020-11-27T12:46:16Z)

Hi @clzstc123 
Thanks for reaching out.
ROCm is working with 5.4.0-42 and 5.4.0-54 kernels. Not sure about 5.4.0-56, need to check.
Whats the output you are getting?
Request you to share more details for better understanding of the problem.

---

### 评论 #2 — ddobreff (2020-11-30T13:54:17Z)

```
diff --git a/amd/amdgpu/amdgpu_bios.c b/amd/amdgpu/amdgpu_bios.c
index 8d76b9e..88e5af3 100644
--- a/amd/amdgpu/amdgpu_bios.c
+++ b/amd/amdgpu/amdgpu_bios.c
@@ -192,30 +192,35 @@ static bool amdgpu_read_bios_from_rom(struct amdgpu_device *adev)

 static bool amdgpu_read_platform_bios(struct amdgpu_device *adev)
 {
-       uint8_t __iomem *bios;
-       size_t size;
+        phys_addr_t rom = adev->pdev->rom;
+        size_t romlen = adev->pdev->romlen;
+        void __iomem *bios;

-       adev->bios = NULL;
+        adev->bios = NULL;

-       bios = pci_platform_rom(adev->pdev, &size);
-       if (!bios) {
-               return false;
-       }
+        if (!rom || romlen == 0)
+                return false;

-       adev->bios = kzalloc(size, GFP_KERNEL);
-       if (adev->bios == NULL)
-               return false;
+        adev->bios = kzalloc(romlen, GFP_KERNEL);
+        if (!adev->bios)
+                return false;

-       memcpy_fromio(adev->bios, bios, size);
+        bios = ioremap(rom, romlen);
+        if (!bios)
+                goto free_bios;

-       if (!check_atom_bios(adev->bios, size)) {
-               kfree(adev->bios);
-               return false;
-       }
+        memcpy_fromio(adev->bios, bios, romlen);
+        iounmap(bios);

-       adev->bios_size = size;
+        if (!check_atom_bios(adev->bios, romlen))
+                goto free_bios;

-       return true;
+        adev->bios_size = romlen;
+
+        return true;
+free_bios:
+        kfree(adev->bios);
+        return false;
 }

 #ifdef CONFIG_ACPI

```
This should fix the compile error for 5.4.0-56+

---

### 评论 #3 — ROCmSupport (2020-12-01T10:07:48Z)

Thanks @ddobreff for the workaround.
Hi @clzstc123, can you please give a try as above and update.
Thank you.

---

### 评论 #4 — ye-luo (2020-12-01T23:49:36Z)

encountered 5.4.0-56 issue when trying to install 3.10. @ROCmSupport could you test the fix on your ubuntu machine where the packages are made and roll out 3.10.1 to get this issue fixed?

---

### 评论 #5 — ROCmSupport (2020-12-02T04:40:15Z)

Hi @clzstc123 and @ye-luo 
I, myself, saw this issue, I mean able to reproduce this problem locally with 5.4.0-56. I am working with Kernel team for the fix.
I will update once the fix is available.

---

### 评论 #6 — Dantali0n (2020-12-02T07:42:00Z)

Here is the dkms crash dump [rock-dkms-firmware.0.txt](https://github.com/RadeonOpenCompute/ROCm/files/5627656/rock-dkms-firmware.0.txt)


---

### 评论 #7 — ROCmSupport (2020-12-02T08:42:01Z)

Yes @Dantali0n
I found the same crash and our kernel team is working on it.
Thank you.

---

### 评论 #8 — clzstc123 (2020-12-03T15:34:18Z)

> Hi @clzstc123 and @ye-luo 
> I, myself, saw this issue, I mean able to reproduce this problem locally with 5.4.0-56. I am working with Kernel team for the fix.
> I will update once the fix is available.

sadly, ubuntu update to 5.4.0-57.
![IMG_20201203_232631.jpg](https://user-images.githubusercontent.com/5130377/101051068-06dbe780-35c0-11eb-8f32-34d7e57a9299.jpg)
try to install rocm3.10 
it's log of install

---

### 评论 #9 — darsnack (2020-12-03T23:38:35Z)

Just leaving a note that this same issue cropped up with 4.15.0-126 on Ubuntu 18.04 LTS. The diff above worked to fix it though.

---

### 评论 #10 — ROCmSupport (2020-12-04T05:36:45Z)

Thanks @darsnack for trying a new kernel for time-being.

---

### 评论 #11 — ROCmSupport (2020-12-04T05:37:03Z)

Hi All,
Until the fix is available, we recommend to install ROCm on 5.4.0-54 kernel or hwe kernels.
Thank you.

---

### 评论 #12 — ROCmSupport (2020-12-11T04:35:15Z)

Hi All,
Fix for 5.4.0-56 is ready and pushed too. Updated Documentation accordingly.
Request to try the new packages.

**_Note: AMD ROCm v3.10 fails to install on Ubuntu kernel v5.4.0-56. To resolve the installation issue, new packages for 'rock-dkms' and 'rock-dkms-firmware' are created and replaced. It is recommended to perform a clean and fresh installation with the new packages._**

Thank you.

---

### 评论 #13 — josarv (2020-12-15T01:34:03Z)

@ROCmSupport  So let me get this straight, is it fixed now? Will installing it on a fresh Ubuntu w/ kernel v5.4.0-56 result in failure or not? Where do we get the new packages?

---

### 评论 #14 — ROCmSupport (2020-12-15T04:10:25Z)

Hi @josarv 
The kernel packages which have fix, are kept in the same 3.10 repo location.
You can uninstall any existing ROCm and do a fresh & clean install of 3.10 and it works now.

---

### 评论 #15 — josarv (2020-12-15T04:15:44Z)

@ROCmSupport  I am sorry for the spam, but it still is not perfectly clear to me (i need sleep). I have performed a clean fresh Ubuntu 20.04 installation (ships with 5.4.0-56) without anything else driver related. Will following [these](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html) instructions here, result in a failure, or am I good to go and install as per usual following the link? 

edit: (My confusion stems from not knowing which repo you're referring to, the package repository hosting the downloadable, or the git repo?)

---

### 评论 #16 — ROCmSupport (2020-12-15T04:25:18Z)

Hi @josarv 
Yon can use the same repo as we have not changed the repo.
We have kept packages with fix into the same repo, I mean we replaced old kernel packages with new set of packages in the same space and so same instructions should work perfect.
Thank you.

---

### 评论 #17 — heuripedes (2021-02-28T11:27:10Z)

> Hi All,
> Until the fix is available, we recommend to install ROCm on 5.4.0-54 kernel or hwe kernels.
> Thank you.

20.04's hwe is 5.8 which doesn't work either 

---

### 评论 #18 — ROCmSupport (2021-03-01T06:06:20Z)

Hi @heuripedes 
Request you to wait for ROCm 4.1.
Thanks.

---

### 评论 #19 — ChrisAi89 (2021-03-12T15:53:08Z)

> Hi @heuripedes
> Request you to wait for ROCm 4.1.
> Thanks.

Is there already an approximate date of release? I try to get my Radeon RX570 to work on a 5.8.0-44 kernel with ROCM 4.0, but for already well described reasons this task remains unaccomplished. Using older kernels with ROCM 3.5 caused unforeseen system instability and I really do not want to switch, for several reasons, the brand of my GPU.

---

### 评论 #20 — ROCmSupport (2021-03-15T06:23:04Z)

Hi @ChrisAi89 
It will be released anytime in this month. Please stay tuned.
Thank you.

---

### 评论 #21 — xuhuisheng (2021-03-15T06:29:27Z)

@ChrisAi89 
If you can downgrade linux kernel to 5.4.0, rocm-dkms from ROCm-4.0 can install successfully.

But since RX570, aka gfx803, had been removed from offcial support. It will be some issues when you use it on ROCm-4.0. Please refer here : https://github.com/xuhuisheng/rocm-build/tree/develop/gfx803



---
