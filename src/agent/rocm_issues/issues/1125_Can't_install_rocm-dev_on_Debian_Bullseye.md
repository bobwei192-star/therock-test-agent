# Can't install rocm-dev on Debian Bullseye

> **Issue #1125**
> **状态**: closed
> **创建时间**: 2020-06-03T03:26:16Z
> **更新时间**: 2023-02-01T19:31:26Z
> **关闭时间**: 2021-02-16T06:36:39Z
> **作者**: sebastianlacuesta
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1125

## 描述

Trying to install rocm-dev on Debian Bullseye (Testing) fails due to unmet dependencies.
```
$ sudo apt install rocm-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 llvm-amdgpu : Depends: libstdc++-5-dev but it is not installable or
                        libstdc++-7-dev but it is not installable
               Depends: libgcc-5-dev but it is not installable or
                        libgcc-7-dev but it is not installable
E: Unable to correct problems, you have held broken packages.
```
Neither libstdc++-5-dev, libstdc++-7-dev, libgcc-5-dev nor libgcc-7-dev are available for Bullseye anymore

---

## 评论 (36 条)

### 评论 #1 — UbuntuStrike (2020-06-14T15:23:56Z)

Yes, same here.

---

### 评论 #2 — rcgoodfellow (2020-07-11T21:31:27Z)

And since these are closed source binaries that cannot be re-built for current systems, this, in effect makes all of ROCm lose a principle benefit of open source, being able to port to the system you need to run on.

---

### 评论 #3 — sebastianlacuesta (2020-07-16T00:11:05Z)

Things are becoming worse. Now we have this:
```
$ sudo apt install rocm-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 libhsa-runtime64-1 : Depends: libhsakmt1 (>= 2.9.0) but it is not installable
 llvm-amdgpu : Depends: libstdc++-5-dev but it is not installable or
                        libstdc++-7-dev but it is not installable
               Depends: libgcc-5-dev but it is not installable or
                        libgcc-7-dev but it is not installable
E: Unable to correct problems, you have held broken packages.
```
Any chance to solve this?

---

### 评论 #4 — hexi03 (2020-07-16T12:12:29Z)

You can try to connect the repository for the stable version and take these packages from there, but for me, it breaks the system (conflict). Hope this fixes quickly.

---

### 评论 #5 — sebastianlacuesta (2020-08-24T13:19:25Z)

> You can try to connect the repository for the stable version and take these packages from there, but for me, it breaks the system (conflict). Hope this fixes quickly.

For me it breaks the system too. And with version 3.7.0, besides having to manually build package from source in https://salsa.debian.org/rocm-team/roct-thunk-interface, still no luck with those gcc dependencies.

---

### 评论 #6 — baryluk (2020-08-25T03:12:03Z)

I can confirm this is an issue with 3.7. However, you should remember that only Ubuntu 16.04 LTS xenial is supported, and it does provide `libstdc++-5`. Similarly Ubuntu 18.04 LTS bionic is supported and it provides `libstdc++-7-dev`.   Also Ubuntu 20.04 LTS focal provides `libstdc++-7-dev`.

I downloaded the `llvm-amdgpu3.7.0_11.0.dev_amd64.deb` manually and modified its dependencies (to include `libstdc++-10-dev` and `libgcc-10-dev`) and repackaged it back into deb file and installed using `dpkg -i` without failure.

After that I tested few binaries in `/opt/rocm-3.7.0/llvm/bin/` and they all work without issue.

Then I was able to install hip-rocclr3.7.0

This also made `/opt/rocm-3.7.0/hip/bin/hipconfig` happy (after adding manually a `/opt/rocm -> /opt/com-3.7.0` symlink).

And I did manage to compile and run many sample examples.


So it looks like fixable overall.


---

### 评论 #7 — baryluk (2020-09-22T20:14:47Z)

Still issue in ROCm 3.8.



---

### 评论 #8 — baryluk (2020-09-22T20:43:00Z)

For anybody struggling with working around this, here is a repackaged unsigned deb with dependencies for libstdc++-10-dev and libgcc-10-dev added.

```                                                                               
wget http://repo.radeon.com/rocm/apt/debian/pool/main/l/llvm-amdgpu3.8.0/llvm-amdgpu3.8.0_11.0.dev_amd64.deb                                                                                      
mkdir tmp
dpkg-deb -R llvm-amdgpu3.8.0_11.0.dev_amd64.deb tmpllvm-amdgpu
sed -E -i -e 's/libstdc\+\+-7-dev,/libstdc++-7-dev|libstdc++-10-dev,/' -e 's/libgcc-7-dev$/libgcc-7-dev|libgcc-10-dev/' tmpllvm-amdgpu/DEBIAN/control 
dpkg-deb -b tmpllvm-amdgpu llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
sudo dpkg -i llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
rm -rf tmpllvm-amdgpu
```


https://www.functor.xyz/rocm/llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb  (506MB)

```
9d8e9c711eaa367ef6f054eb3f7c373b8b81ae5a6980d5403f46ec287a72ac01  llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
```


---

### 评论 #9 — norbusan (2020-09-22T22:55:58Z)

@baryluk you need to change the version number also in the `DEBIAN/control` file, not only the file name. Actually, the file name is irrelevant and only for informative purposes. Furthermore, it is better to use `+` instead of `~` since the `~` sorts before the rest, meaning that `apt update` would try to reinstall the broken version.

I have set up a apt repository to get the package. The release files are signed with [my GPG key](https://www.preining.info/preining-norbert.asc). Here is the apt sources line:
```
deb https://www.preining.info/debian buster rocm
```
This package can be installed on buster and above (for the time being).

---

### 评论 #10 — baryluk (2020-09-22T22:59:18Z)

@norbusan I know the filename is irrelevant. But the version is also irrelevant. As long as you don't remove and install the package using `apt` it is going to work.


---

### 评论 #11 — norbusan (2020-09-22T23:42:56Z)

@baryluk yes, that is correct. And since AMD is not shipping minor updates and only major version jumps, the installed version of yours will work the same way.

---

### 评论 #12 — piodag (2020-09-23T20:52:16Z)

> For anybody struggling with working around this, here is a repackaged unsigned deb with dependencies for libstdc++-10-dev and libgcc-10-dev added.
> 
> ```
> wget http://repo.radeon.com/rocm/apt/debian/pool/main/l/llvm-amdgpu3.8.0/llvm-amdgpu3.8.0_11.0.dev_amd64.deb                                                                                      
> mkdir tmp
> dpkg-deb -R llvm-amdgpu3.8.0_11.0.dev_amd64.deb tmpllvm-amdgpu
> sed -E -i -e 's/libstdc\+\+-7-dev,/libstdc++-7-dev|libstdc++-10-dev,/' -e 's/libgcc-7-dev$/libgcc-7-dev|libgcc-10-dev/' tmpllvm-amdgpu/DEBIAN/control 
> dpkg-deb -b tmpllvm-amdgpu llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> sudo dpkg -i llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> rm -rf tmpllvm-amdgpu
> ```
> 
> https://www.functor.xyz/rocm/llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb (506MB)
> 
> ```
> 9d8e9c711eaa367ef6f054eb3f7c373b8b81ae5a6980d5403f46ec287a72ac01  llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> ```

Done. Thanks.

But my tensorflow-rocm is not recognised. I use it inside RStudio. Do I have to install rocm-libs too? Instructions are a bit clumsy. Is it normal to have more than 10GB for that library?

Regards


---

### 评论 #13 — baryluk (2020-09-23T22:23:40Z)

@gfwp You need to install `rocm-lib3.8.0` and `rccl3.8.0`  (or without version is you use unversioned ones). Then do `pip3 install tensorflow-rocm`, or something like that. Then in RStudio you probably need to do `install.packages("tensorflow")`. You need to make sure you have correct library paths (i.e. by setting `LD_LIBRARY_PATH` and `ROCM_PATH`) before you start. I do that manually like this: `LD_LIBRARY_PATH=/opt/rocm-3.8.0/lib ROCM_PATH=/opt/rocm-3.8.0`

I don't use RStudio, but I managed to make it work in Python, and R (just to test it).

Honestly your issue probably is for different issue, not related to this bug.


---

### 评论 #14 — piodag (2020-09-24T05:51:30Z)

> @gfwp You need to install `rocm-lib3.8.0` and `rccl3.8.0` (or without version is you use unversioned ones). Then do `pip3 install tensorflow-rocm`, or something like that. Then in RStudio you probably need to do `install.packages("tensorflow")`. You need to make sure you have correct library paths (i.e. by setting `LD_LIBRARY_PATH` and `ROCM_PATH`) before you start. I do that manually like this: `LD_LIBRARY_PATH=/opt/rocm-3.8.0/lib ROCM_PATH=/opt/rocm-3.8.0`
> 
> I don't use RStudio, but I managed to make it work in Python, and R (just to test it).
> 
> Honestly your issue probably is for different issue, not related to this bug.

Thanks a lot

---

### 评论 #15 — tai (2020-10-30T16:29:44Z)

Just FYI, it's easier to workaround the issue if you just install dummy package using equivs: https://wiki.debian.org/Packaging/HackingDependencies

Just create empty package that provides libstdc++-7-dev and libgcc-7-dev.

That said, ROCm should fix its dependency in DEBIAN/control so it references "libstdc++-dev" and "gcc", instead of version-specific "libstdc++-\<VER\>-dev" and "libgcc-\<VER\>-dev" package.

---

### 评论 #16 — baryluk (2020-11-02T06:36:45Z)

@tai Thanks. That is a neat trick.

https://www.functor.xyz/rocm/fake-old-libgcc_99_all.deb  should do the trick and work with both rocm 3.8 and 3.9. The equivs source in in the same directory there on the server if you want to check it out.

After downloading, go to directory you downloaded it to, and do `sudo dpkg -i fake-old-libgcc_99_all.deb`, then continue with normal ROCm installation just like for Ubuntu using normal install guide.


---

### 评论 #17 — radhekrishanji (2020-12-02T18:46:01Z)

> For anybody struggling with working around this, here is a repackaged unsigned deb with dependencies for libstdc++-10-dev and libgcc-10-dev added.
> 
> ```
> wget http://repo.radeon.com/rocm/apt/debian/pool/main/l/llvm-amdgpu3.8.0/llvm-amdgpu3.8.0_11.0.dev_amd64.deb                                                                                      
> mkdir tmp
> dpkg-deb -R llvm-amdgpu3.8.0_11.0.dev_amd64.deb tmpllvm-amdgpu
> sed -E -i -e 's/libstdc\+\+-7-dev,/libstdc++-7-dev|libstdc++-10-dev,/' -e 's/libgcc-7-dev$/libgcc-7-dev|libgcc-10-dev/' tmpllvm-amdgpu/DEBIAN/control 
> dpkg-deb -b tmpllvm-amdgpu llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> sudo dpkg -i llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> rm -rf tmpllvm-amdgpu
> ```
> 
> https://www.functor.xyz/rocm/llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb (506MB)
> 
> ```
> 9d8e9c711eaa367ef6f054eb3f7c373b8b81ae5a6980d5403f46ec287a72ac01  llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> ```

please provide step by step guide. i am unable to understand that what to do with that downloaded file. and how to install it. then after which commands should i use. my amd gpu is not working in hashcat and all other applications. i have tried all methods. but same error. please help me. 

---

### 评论 #18 — sebastianlacuesta (2020-12-02T19:18:18Z)

> > For anybody struggling with working around this, here is a repackaged unsigned deb with dependencies for libstdc++-10-dev and libgcc-10-dev added.
> > ```
> > wget http://repo.radeon.com/rocm/apt/debian/pool/main/l/llvm-amdgpu3.8.0/llvm-amdgpu3.8.0_11.0.dev_amd64.deb                                                                                      
> > mkdir tmp
> > dpkg-deb -R llvm-amdgpu3.8.0_11.0.dev_amd64.deb tmpllvm-amdgpu
> > sed -E -i -e 's/libstdc\+\+-7-dev,/libstdc++-7-dev|libstdc++-10-dev,/' -e 's/libgcc-7-dev$/libgcc-7-dev|libgcc-10-dev/' tmpllvm-amdgpu/DEBIAN/control 
> > dpkg-deb -b tmpllvm-amdgpu llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> > sudo dpkg -i llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> > rm -rf tmpllvm-amdgpu
> > ```
> > 
> > 
> > https://www.functor.xyz/rocm/llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb (506MB)
> > ```
> > 9d8e9c711eaa367ef6f054eb3f7c373b8b81ae5a6980d5403f46ec287a72ac01  llvm-amdgpu3.8.0_11.1.dev~fix1_amd64.deb
> > ```
> 
> please provide step by step guide. i am unable to understand that what to do with that downloaded file. and how to install it. then after which commands should i use. my amd gpu is not working in hashcat and all other applications. i have tried all methods. but same error. please help me.

Better go with @baryluk solution. Just install https://www.functor.xyz/rocm/fake-old-libgcc_99_all.deb. Then ensure you have libstdc++-10-dev and libgcc-10-dev installed. Finally just install rocm-dev from repo.
You can install this file with: `sudo dpkg -i fake-old-libgcc_99_all.deb`. For rocm-dev, you can follow the instructions in [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu](url), but if you are using debian, instead of `sudo apt install rocm-dkms && sudo reboot` at step 3, you better use `sudo apt install rocm-dev` (no reboot needed in this case). This works if you are using debian testing and have most up to date kernel by having linux-image-amd64 linux-headers-amd64 packages installed and update to testing or unstable.

Hope it helps. 

---

### 评论 #19 — UKDOP (2021-02-03T10:03:52Z)

Hi sebastianlacuesta and others,

I have just signed in and want to thank you all !
This has solved my issue of installing rocm-libs in Debian 11 
It is vital for upgrading HQplayer Embedded newer version with cuda offload.

Ii

---

### 评论 #20 — ROCmSupport (2021-02-16T06:36:39Z)

Thanks all for your ideas and suggestions.
As we are not supporting Debian officially, we can not share official info on this.
Request to try with the above tricks and suggestions to overcome installation problems.
Thank you.

---

### 评论 #21 — baryluk (2021-02-16T09:13:37Z)

@ROCmSupport This is still a bug in the ROCm packages, and should be fixed in ROCm packages, as they are simply incorrect.

---

### 评论 #22 — ROCmSupport (2021-02-16T11:39:16Z)

Hi @baryluk 
We are not able to reproduce this issue with our supported OSes.
For ex: Ubuntu has libstdc++ packages and will be installed automatically.

---

### 评论 #23 — mickyhong (2021-02-22T17:28:08Z)

Big thanks to  baryluk and sebastianlacuesta again !
I now also successfully installed rocm-dkms under Debian 11 after solving kernel header file not found issue.


---

### 评论 #24 — Dev380 (2021-04-26T13:59:44Z)

Hi, I have this issue too, the fakegcc worked for me but there's still one broken dependency: libython3.8. I checked and  my python version is 3.9  and for some reason it can't install the older version. Does anyone know how to create a fakepython.deb file or something like that?

---

### 评论 #25 — baryluk (2021-04-27T16:16:12Z)

@Dev380 This bug is about the `libstdc++` and `libgcc-dev`. Open a new bug about libpython3.8. Or actually look at the existing issue about this: https://github.com/RadeonOpenCompute/ROCm/issues/1236

---

### 评论 #26 — karlxmar (2021-08-11T20:14:34Z)

> @tai Thanks. That is a neat trick.
> 
> https://www.functor.xyz/rocm/fake-old-libgcc_99_all.deb should do the trick and work with both rocm 3.8 and 3.9. The equivs source in in the same directory there on the server if you want to check it out.
> 
> After downloading, go to directory you downloaded it to, and do `sudo dpkg -i fake-old-libgcc_99_all.deb`, then continue with normal ROCm installation just like for Ubuntu using normal install guide.

Clever fix! = ) I got a bit further with the fakegcc but not all the way. Hopefully Im stuck at something "easy"...

Im running Bulleye with 5.10.0-8-amd64. Im looking to install rocm to run hashcat on a RX570 board. Running apt install rocm-dkms I get stuck at the following (when rock-dkms is being configured)

> Loading new amdgpu-4.3-52 DKMS files...
> Building for 5.10.0-8-amd64
> Building for architecture amd64
> Building initial module for 5.10.0-8-amd64
> Error! Bad return status for module build on kernel: 5.10.0-8-amd64 (amd64)
> Consult /var/lib/dkms/amdgpu/4.3-52/build/make.log for more information.

Looking through the mentioned log I find at the end
> /var/lib/dkms/amdgpu/4.3-52/build/Makefile:26: "Local GCC version 100202 does not match kernel compiler GCC version 100201"
> /var/lib/dkms/amdgpu/4.3-52/build/Makefile:27: "This may cause unexpected and hard-to-isolate compiler-related issues"
>   MODPOST /var/lib/dkms/amdgpu/4.3-52/build/Module.symvers
> ERROR: modpost: "migrate_vma_finalize" [/var/lib/dkms/amdgpu/4.3-52/build/amd/amdgpu/amdgpu.ko] undefined!
> ERROR: modpost: "migrate_vma_pages" [/var/lib/dkms/amdgpu/4.3-52/build/amd/amdgpu/amdgpu.ko] undefined!
> ERROR: modpost: "migrate_vma_setup" [/var/lib/dkms/amdgpu/4.3-52/build/amd/amdgpu/amdgpu.ko] undefined!
> ERROR: modpost: "devm_request_free_mem_region" [/var/lib/dkms/amdgpu/4.3-52/build/amd/amdgpu/amdgpu.ko] undefined!

There is no file /var/lib/dkms/amdgpu/4.3-52/build/amd/amdgpu/amdgpu.ko

Any ideas or hints? Thanks a bunch!

---

### 评论 #27 — martinpaljak (2021-08-24T05:15:56Z)

Upgraded to Bullseye, removed all packages without source (incl the fake gcc tricky) and after making sure the kernel matches the compiler, rock-dkms gives
```
  CC [M]  /var/lib/dkms/amdgpu/4.3-52/build/amd/amdgpu/amdgpu_device.o
gcc: fatal error: cannot specify ‘-o’ with ‘-c’, ‘-S’ or ‘-E’ with multiple files
```

Wondering if it would be easier to have something with docker for the ubuntu userspace once the kernel parts are hacked together to compile-load with Bullseye?

---

### 评论 #28 — sebastianlacuesta (2021-08-24T18:29:37Z)

Not using right now, but taking a look once in a while just to see how this goes. I tested `clinfo` with `rocm-dev` install and kernel in experimental 5.13 and it works. README.md points that  `IPC and RDMA capabilities are not yet enabled`, so if you don't need this, maybe can try it without `rocm-dkms`. I confirmed that kernel 5.10 doesn't support what rocm 4.3 userspace needs. Best of luck.

---

### 评论 #29 — satmandu (2021-09-08T16:02:36Z)

@martinpaljak Did you find a solution for that dkms build?

I'm seeing the same issue with the current release of the amdgpu-dkms driver on Ubuntu 21.10 installs:
```
  CC [M]  /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/scheduler/sched_main.o
gcc: fatal error: cannot specify ‘-o’ with ‘-c’, ‘-S’ or ‘-E’ with multiple files
```

My guess is that this is something that broke the amd dkms setup with bullseye/impish. (But using `CC=gcc-10` also doesn't fix the issue.)

---

### 评论 #30 — martinpaljak (2021-09-08T17:55:17Z)

@satmandu I have a custom kernel with some parts of enabled manually, using rocm-opencl clinfo shows the GPU as a device, at least. Hashcat does not see it, but I think that might be a simpler path than dealing with dkms. 

---

### 评论 #31 — xmixahlx (2021-09-21T02:41:45Z)

rocm deb packages are designed for Ubuntu Focal, so either grab the necessary packages from Ubuntu and install them, or create custom packages that provide the dependencies for your distro.

---

### 评论 #32 — sebastianlacuesta (2021-09-21T16:25:11Z)

Are .dsc, orig.tar.gz and diff.gz files avaiable for these packages? Or sources with proper debian directory so everyone can change locally and support other debian derived distros unofficially?

---

### 评论 #33 — xmixahlx (2021-09-22T22:02:54Z)

You can create your own dummy packages for libgcc-7-dev and libpython3.8, then manually link (dummy) libpython3.8 to libpython3.9 for rocm-gdb dependencies.

create two files "fake-libpython3.8" and "fake-libgcc-7-dev" (contents below)
install equivs
run equivs-build $file
install resulting deb files
configure rocm deb repository
install desired rocm packages

"fake-libgcc-7-dev" contents:

```
Section: misc
Priority: optional
Standards-Version: 3.9.2

Package: fake-libgcc-7-dev
Version: 1.0
Provides: libgcc-7-dev, libstdc++-7-dev
Architecture: all
Description: Fake libgcc7-dev package to satisfy dependencies
 Fake libgcc7-dev package to satisfy dependencies
```

"fake-libpython3.8" contents:

```
Section: misc
Priority: optional
Standards-Version: 3.9.2

Package: fake-libpython3.8
Version: 1.0
Depends: libpython3.9
Provides: libpython3.8, libpython3.8-minimal, libpython3.8-stdlib
Architecture: all
Description: Fake libpython3.8 package to satisfy dependencies
 Fake libpython3.8 package to satisfy dependencies

## MANUAL INSTALL
#sudo ln -s /usr/lib/x86_64-linux-gnu/libpython3.9.so /usr/lib/x86_64-linux-gnu/libpython3.8.so
#sudo ln -s /usr/lib/x86_64-linux-gnu/libpython3.9.so /usr/lib/x86_64-linux-gnu/libpython3.8.so.1
#sudo ln -s /usr/lib/x86_64-linux-gnu/libpython3.9.so /usr/lib/x86_64-linux-gnu/libpython3.8.so.1.0
```

---

### 评论 #34 — mralusw (2023-01-16T07:00:41Z)

@xmixahlx another thing is that it tries to pull `rocm-llvm`, but I already have llvm-15 from
```
deb http://apt.llvm.org/focal/ llvm-toolchain-focal-15 main
```

I'll try to fake that too

---

### 评论 #35 — SLAYER-CODE (2023-02-01T16:24:09Z)

Same problem when installing amdgpu-dkms on degraded kernel version 'x86_64 Linux 5.10.0-21-amd64' Parrot Electro ara 5.1 operating system

     │   LD [M]  /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.o
       │ /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/Makefile:26: "Local GCC version 100202 does not match kern
       │ el compiler GCC version 100201"
       │ /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/Makefile:27: "This may cause unexpected and hard-to-isolat
       │ e compiler-related issues"
       │   MODPOST /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/Module.symvers
       │ ERROR: modpost: "migrate_vma_finalize" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.
       │ ko] undefined!
       │ ERROR: modpost: "migrate_vma_pages" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.ko]
       │  undefined!
       │ ERROR: modpost: "migrate_vma_setup" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.ko]
       │  undefined!
       │ ERROR: modpost: "devm_request_free_mem_region" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu
       │ /amdgpu.ko] undefined!


---

### 评论 #36 — baryluk (2023-02-01T19:31:26Z)

> Same problem when installing amdgpu-dkms on degraded kernel version 'x86_64 Linux 5.10.0-21-amd64' Parrot Electro ara 5.1 operating system
> 
> ```
>  │   LD [M]  /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.o
>    │ /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/Makefile:26: "Local GCC version 100202 does not match kern
>    │ el compiler GCC version 100201"
>    │ /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/Makefile:27: "This may cause unexpected and hard-to-isolat
>    │ e compiler-related issues"
>    │   MODPOST /var/lib/dkms/amdgpu/5.11.19.98-1290604/build/Module.symvers
>    │ ERROR: modpost: "migrate_vma_finalize" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.
>    │ ko] undefined!
>    │ ERROR: modpost: "migrate_vma_pages" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.ko]
>    │  undefined!
>    │ ERROR: modpost: "migrate_vma_setup" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu/amdgpu.ko]
>    │  undefined!
>    │ ERROR: modpost: "devm_request_free_mem_region" [/var/lib/dkms/amdgpu/5.11.19.98-1290604/build/amd/amdgpu
>    │ /amdgpu.ko] undefined!
> ```

Please open a separate bug. As your issue has nothing to do with this issue.

---
