# ROCm fails to install from APT repository in 22.04

> **Issue #1713**
> **状态**: closed
> **创建时间**: 2022-03-24T05:27:25Z
> **更新时间**: 2024-05-20T16:53:57Z
> **关闭时间**: 2022-11-10T08:25:07Z
> **作者**: erkinalp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1713

## 描述

Ubuntu 22.04's feature freeze has already passed and the version in the APT repository is not installable due to missing dependencies (in APT-based distributions, feature freeze is also the minor version freeze).

Main issues being:

- python 3.8, whereas the earliest version available is 3.9
- libstdc++ and libgcc symbol version 5 but the earliest version available is 9

---

## 评论 (100 条)

### 评论 #1 — Bengt (2022-03-29T01:05:35Z)

Hi, @erkinalp!

Thanks for this bug report. I am glad that users are already testing ROCm in the Ubuntu pre-release version.

For more context, see also the other [issues about Ubuntu 22.04](https://github.com/RadeonOpenCompute/ROCm/issues?q=ubuntu+22.04).

As a workaround for Python 3.8 not being part of Ubuntu 22.04, one should soon be able to install Python 3.8 from the commonly-used deadsnakes PPA. However, it does not support Ubuntu 22.04 (Jammy Jellyfish), yet: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa

---

### 评论 #2 — xuhuisheng (2022-04-22T02:38:02Z)

So I move my test result to the issue.

because of gcc-11, I cannot install rocm-dev rocm-libs in ubuntu-22.04 docker image.

```
work@7cead9071756:/var/spool/apt-mirror/mirror$ sudo apt install -y rocm-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 openmp-extras : Depends: libstdc++-5-dev but it is not installable or
                          libstdc++-7-dev but it is not installable
                 Depends: libgcc-5-dev but it is not installable or
                          libgcc-7-dev but it is not installable
                 Recommends: gcc but it is not going to be installed
                 Recommends: g++ but it is not going to be installed
 rocm-gdb : Depends: libpython3.8 but it is not installable
 rocm-llvm : Depends: python but it is not installable
             Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
             Recommends: gcc but it is not going to be installed
             Recommends: g++ but it is not going to be installed
             Recommends: gcc-multilib but it is not going to be installed
             Recommends: g++-multilib but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

And I try to compile ROCm-5.1.1 in the ubuntu-22.04 docker image. boost-1.72.0, rocsolver had some compile errors.
The pytorch need to compile with python-3.10, and there seems to be some configuration errors, I am going on dig.

---

### 评论 #3 — Bengt (2022-04-23T00:39:54Z)

DeadSnakes PPA now has support for Ubuntu 22.04 "Jammy Jellyfish":

https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa?field.series_filter=jammy

So, to fix the issue of Python 3.8 not being installed, you can install it like so:

```bash
sudo add-apt-repository --yes ppa:deadsnakes/ppa && \
sudo apt-get update && \
sudo apt install --yes python3.8
```

---

### 评论 #4 — erkinalp (2022-04-23T04:09:31Z)

@Bengt Python 3.8 is not supported for the entire lifetime of 22.04.

---

### 评论 #5 — Bengt (2022-04-23T09:45:56Z)

True. I didn't mean to suggest that installing Python from the PPA should be the permanent solution for end users. I meant it as a workaround for people who want to debug the installation issues, like @xuhuisheng.

---

### 评论 #6 — xuhuisheng (2022-04-23T12:01:07Z)

Thank you @Bengt .
I have got that you want to show me a way to test pytorch on ubuntu-22.04 and pytorch-3.8.
But I think the major issue is gcc-11.

I had built a pytorch-1.11.0-py310.whl with a little patch of breadpad. but then I met a compile error when run mnist. It looks like miopen want to compile naive_conv.cpp for torchvision, And this kernel cannot compile properly on gcc-11.

---

### 评论 #7 — xuhuisheng (2022-04-24T09:00:51Z)

update: 2022-04-24

I had commetted out a lot of codes to pass the compile step on ubuntu-22.04.
The main part of work is skip `log_bench()` in rocSOLVER, skip include some header, likes `thread.h` in hip_runtime.h.

Now pytorch-1.11.0 and tensorflow_rocm-2.8.1 run properly with ROCm-5.1.1 on ubuntu-22.04.
Just some small samples, I only test mnist today.

I think it wont be a problem for ROCm team to support ubuntu-22.04, just wait for them a while.

I will stay on ubuntu-20.04 recently. Maybe next year, maybe ROCm-6.0 can add official support for ubuntu-22.04, then I can upgrade to the new LTS.

---

### 评论 #8 — Bengt (2022-04-24T19:58:44Z)

Hi, @xuhuisheng!

Yes, I meant installing Python from the PPA as a workaround, only. Maybe that has aided you in isolating the core issue of GCC-11.

Thanks for testing ROCm installation and compilation so thoroughly. I hope your information can help the @qROCmSupport team in their effort to make ROCm work under Ubuntu 22.04.

To my eyes, the next, most obvious target would be Ubuntu 22.04.1. This will be the first Linux kernel update which needs to be considered for building the lower-level libraries. However, only supporting the first point release of Ubuntu's LTS versions is not what I would like to consider solid support.

---

### 评论 #9 — erkinalp (2022-04-24T20:01:19Z)

Indeed, as @Bengt has always been saying, this should have been ready much earlier, with all the bugs ironed out by now.

---

### 评论 #10 — Laitaps (2022-04-25T12:47:17Z)

This makes it really hard to support AMD.  On my laptop with an RTX 3080, everything  just works.  My desktop with Radeon Vll, not so much.  I am very surprised.  If AMD does not take steps to improve support, they will never have parity with Nvidia in ML.  This was an opportunity  to build some goodwill and you blew it.

---

### 评论 #11 — L3P3 (2022-05-11T09:30:10Z)

@xuhuisheng could you please provide your changes as a fork so I may test it also?

---

### 评论 #12 — xuhuisheng (2022-05-13T00:28:54Z)

@L3P3 rocsolver had solved fmt issue. We can wait for the next version 5.2.

https://github.com/ROCmSoftwarePlatform/rocSOLVER/commit/2bbfb8976f6e4d667499c77e41a6433850063e88

---

### 评论 #13 — SciPyPanda (2022-06-11T06:54:11Z)

Is this issue still being solved? Any updates?

---

### 评论 #14 — xuhuisheng (2022-06-26T16:24:49Z)

@L3P3 
Since ROCm-5.2 didn't release on May.
I upload a document for patching ROCm-5.1.3 on ubuntu-22.04.

<https://github.com/xuhuisheng/rocm-build/tree/develop/ubuntu2204>

---

### 评论 #15 — L3P3 (2022-06-27T18:10:29Z)

@xuhuisheng sorry, I tried to follow your instructions but it is too hard to understand what I need to do.
Instructions are incomplete, not all steps explained. I hope they will release it officially soon. Thanks for help.

---

### 评论 #16 — L3P3 (2022-07-02T09:47:06Z)

ROCm was released. Is this issue closable then?

---

### 评论 #17 — SciPyPanda (2022-07-02T11:33:38Z)

Still erroring on old dependencies in my case.

```
sudo apt install rocm-dev5.2.0

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-gdb5.2.0 : Depends: libpython3.8 but it is not installable
 rocm-llvm5.2.0 : Depends: python but it is not installable
                  Depends: libstdc++-5-dev but it is not installable or
                           libstdc++-7-dev but it is not installable
                  Depends: libgcc-5-dev but it is not installable or
                           libgcc-7-dev but it is not installable
                  Recommends: gcc-multilib but it is not going to be installed
                  Recommends: g++-multilib but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

---

### 评论 #18 — xuhuisheng (2022-07-03T14:52:44Z)

The good news is the issues of roctracer and rocsolver had been solved.
<https://github.com/xuhuisheng/rocm-build/tree/master/ubuntu2204>

---

### 评论 #19 — arinc9 (2022-07-12T13:24:30Z)

> This makes it really hard to support AMD. On my laptop with an RTX 3080, everything just works. My desktop with Radeon Vll, not so much. I am very surprised. If AMD does not take steps to improve support, they will never have parity with Nvidia in ML. This was an opportunity to build some goodwill and you blew it.

@B0tBuilder I have a Radeon VII on my desktop too. Do you have multiple displays? I experience Gnome freezing for about 30 seconds when I turn off my second display. Waking up from suspend is also problematic. It takes about 30 seconds to wake up and the "Join Displays" option changes to "Single Display" and the primary display changes to the second display.

I assumed there might be something wrong with the GPU so I wanted to install the amdgpu driver but I see the same dependency issue as everyone else after running `amdgpu-install`.

---

### 评论 #20 — Laitaps (2022-07-12T13:37:07Z)

> > This makes it really hard to support AMD. On my laptop with an RTX 3080, everything just works. My desktop with Radeon Vll, not so much. I am very surprised. If AMD does not take steps to improve support, they will never have parity with Nvidia in ML. This was an opportunity to build some goodwill and you blew it.
> 
> @B0tBuilder I have a Radeon VII on my desktop too. Do you have multiple displays? I experience Gnome freezing for about 30 seconds when I turn off my second display. Waking up from suspend is also problematic. It takes about 30 seconds to wake up and the "Join Displays" option changes to "Single Display" and the primary display changes to the second display.
> 
> I assumed there might be something wrong with the GPU so I wanted to install the amdgpu driver but I see the same dependency issue as everyone else after running `amdgpu-install`.

I experience no such issue.

---

### 评论 #21 — mchaker (2022-07-18T12:48:33Z)

Attempting to follow the ROCm installation docs, even with accepting the proprietary EULA:

```shell
sudo amdgpu-install --usecase="dkms,workstation,rocm" --opencl=rocr,legacy --vulkan=amdvlk,pro --accept-eula --no-32
```

results in:

```shell
The following packages have unmet dependencies:
 rocm-llvm : Depends: python but it is not installable
             Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
             Recommends: gcc-multilib but it is not going to be installed
             Recommends: g++-multilib but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

---

### 评论 #22 — Rmalavally (2022-07-18T20:26:17Z)

Thank you for reaching out with your query. Please note that ROCm v5.2 does not support Ubuntu v22.04.

Support for Ubuntu v22.04 will be made available in a future release.

ROCm Documentation Team

---

### 评论 #23 — Laitaps (2022-07-18T20:42:29Z)

What future release and when?

---

### 评论 #24 — Rmalavally (2022-07-18T21:06:33Z)

As a best practice, we do not commit to fixes in specific releases. Please continue to review our release documentation on our new portal at https://docs.amd.com.

ROCm Documentation Team 

---

### 评论 #25 — Laitaps (2022-07-18T22:40:50Z)

It has been quite a while since 22.04 was released.  Does anyone find this situation acceptable?

---

### 评论 #26 — L3P3 (2022-07-19T11:12:28Z)

> It has been quite a while since 22.04 was released. Does anyone find this situation acceptable?

I agree that this is a very annoying way of communication. AMD guys can do better, I think. This is just bad organisation.

---

### 评论 #27 — ye-luo (2022-07-19T12:22:09Z)

> It has been quite a while since 22.04 was released. Does anyone find this situation acceptable?

It is acceptable for me. 18.04 and 20.04 are available for production which is more important than any feature from 22.04 in my use case. The message from AMD is clear that if production use is needed now, don't upgrade to 22.04. Users need to weigh their choices based on the need.

I believe AMD also would like to enable 22.04 support ASAP but there is likely issues to work through and it takes time. If the engineers behind the scenes are working day and night trying to resolve issues, keep adding pressure won't help. Keep in mind that NVIDIA reverted to using X.org from Wayland in the last minute. There can be a few technical hurdles for AMD as well in the 22.04 bring up. Regardless of how soon we hope the support can be enabled, the actual date is only after all the blocking issue being resolved.

---

### 评论 #28 — Laitaps (2022-07-19T12:53:07Z)

While I appreciate your perspective, your response is littered with statements you could have no way of knowing.  AMD should have been working on 22.04 for some months prior to its release.  Given no statements to the community to the effect, I find your remark that "...engineers behind the scenes are working day and night trying to resolve issues..." to be dubious at best.  As are your comments regarding Wayland.    

Many of us have dependencies on updated packages available in 22.04 or would like to take advantage of more modern variants for performance reasons.  In these cases, simply remaining on 18.04 or 20.04 is not an option or productive.  There are a number of workarounds, but that simply makes administration more difficult.

I would hope they are working on all the "blocking issues" because that is how software development works.  AMD should be engaging with the community and provide information.  If they are indeed "working day and night", I would like to hear that from them as opposed to assumptions by a third party.  They could have very easily simply made the decision to devote resources elsewhere.

While your comments sound reasonable and you make some good assumptions (e.g. Wayland) we don't really have any way of knowing until someone on their end decides to explain the situation.  With the coming generational shift in hardware, the lack of communication is likely to have a significant impact on purchasing decisions.



---

### 评论 #29 — Bengt (2022-07-19T15:28:48Z)

@ye-luo please note that there was a [discussion about starting development towards supporting 22.04 right after 21.10 released](https://github.com/RadeonOpenCompute/ROCm/issues/1590). Therefore, there is no excuse to not start sufficiently ahead of time to [provide launch-day support for this important release](https://github.com/RadeonOpenCompute/ROCm/issues/1761), other than business reasons. I think it is unfair to just assume that AMD was surprised by the Ubuntu 22.04 release, the demand for running the latest LTS release of a supported operating system, or the breaking changes like the dropped Python 2 package. In contrast to your assumptions, I feel like AMD is actually quite honest about what OSs they support, at what time, and for which reasons. That does not make the situation any less dire to users missing critical features, or this discussion less valuable. So let's please follow their lead and stick to the facts. Making false assumptions can only hinder progress.

---

### 评论 #30 — nwgat (2022-07-21T01:47:06Z)

> Attempting to follow the ROCm installation docs, even with accepting the proprietary EULA:
> 
> ```shell
> sudo amdgpu-install --usecase="dkms,workstation,rocm" --opencl=rocr,legacy --vulkan=amdvlk,pro --accept-eula --no-32
> ```
> 
> results in:
> 
> ```shell
> The following packages have unmet dependencies:
>  rocm-llvm : Depends: python but it is not installable
>              Depends: libstdc++-5-dev but it is not installable or
>                       libstdc++-7-dev but it is not installable
>              Depends: libgcc-5-dev but it is not installable or
>                       libgcc-7-dev but it is not installable
>              Recommends: gcc-multilib but it is not going to be installed
>              Recommends: g++-multilib but it is not going to be installed
> E: Unable to correct problems, you have held broken packages.
> ```

getting the same error here to, basiclly amdgpu unifed on ubuntu 22.02 is broken atm
https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-22-20

---

### 评论 #31 — SSean08 (2022-07-21T02:14:04Z)

Further tests indicates that other use-cases doesn't work due to the broken dependencies, but, I was able to install others such as OpenCL. I didn't directly followed the instructions of the installation docs because _amdgpu-install_ is needed to be invoked which in turn stops due to the non-working dependencies. I just simply specified the use-cases that I needed, for the meantime, I was lucky. Though, I'm not entirely sure if this will also work on other machines.

---

### 评论 #32 — zaxophone (2022-07-21T02:50:50Z)

> Further tests indicates that other use-cases doesn't work due to the broken dependencies, but, I was able to install others such as OpenCL. I didn't directly followed the instructions of the installation docs because _amdgpu-install_ is needed to be invoked which in turn stops due to the non-working dependencies. I just simply specified the use-cases that I needed, for the meantime, I was lucky. Though, I'm not entirely sure if this will also work on other machines.

What specifically did you do to get OpenCL working without amdgpu-install? I'm not able to get OpenCL working with my 6600 XT on Ubuntu 22.04 because rocm-llvm will not install. If there is a workaround I'd love to know how you got there.

---

### 评论 #33 — L3P3 (2022-07-21T07:54:05Z)

> What specifically did you do to get OpenCL working without amdgpu-install? I'm not able to get OpenCL working with my 6600 XT on Ubuntu 22.04 because rocm-llvm will not install. If there is a workaround I'd love to know how you got there.

I installed some opencl package via `apt install` from the same repo that offers `amdgpu-install`. I forgot the package name though, will look it up later. It worked, I ran folding@home on my 5500 XT on latest Ubuntu.

It was one of these: https://repo.radeon.com/amdgpu/latest/ubuntu/pool/proprietary/o

---

### 评论 #34 — dpospisil (2022-07-21T15:43:53Z)

I have figured out that on my box `amdgpu-install --opencl=rocr` fails with above deps errors. But, for some uknown reason `amdgpu-install --usecase=opencl` went through and left me with working OpenCL setup.

---

### 评论 #35 — AgenttiX (2022-07-21T21:30:55Z)

For me the command to get OpenCL working on Ubuntu 22.04 was `amdgpu-install --usecase=opencl --no-dkms`, [as discussed on Ask Ubuntu](https://askubuntu.com/questions/1406137/how-enable-opencl-on-amd-gpu-ubuntu-22-04-lts). It seems that this particular configuration doesn't try to install the packages that are broken on Ubuntu 22.04.

---

### 评论 #36 — jacodt (2022-07-23T10:12:10Z)

I managed to get ```rocm-llvm``` installed with a manual work around. 

I used apt to download the rocm-llvm deb file manually without installing, then decompressed and untarred the internal control file in the deb.
I then manually edited the control file dependencies to change the ```python``` dependency to ```python3``` and I added ```libstdc++-10-dev``` and ```libgcc-10-dev```. Then I rebuilt the rocm-llvm deb file with the new control file in place using ```ar```. I then installed ```libstdc++-10-dev``` and then used ```dpkg``` to install my new rocm-llvm deb file. 

After this install the normal ```amdgpu-install --usecase=rocm``` worked fine and ```rocminfo``` produced the expected results.

This also allowed me to install ```tensorflow-rocm``` which works with the gpu and the "Hello World" mnist example works fine.

(This obviouslly doesn't fix rocm-llvm and link it to the right libraries etc, but it does get it installed and move past the dependency check hurdle. You could probably do the same by just removing the deps all together in the control file. The fact that everything *seems* to work leads me to believe that the issue is mostly around the construction of the rocm-llvm deb file and not the binaries themselves)

---

### 评论 #37 — Bengt (2022-07-24T14:12:10Z)

Hi @jacodt! Thanks for providing the workaround you discovered. Unfortunately, I am not very versed in the tools you used, so I cannot reproduce your findings. Would you be able to provide executable instructions for people to follow your path?

---

### 评论 #38 — jacodt (2022-07-24T14:46:33Z)

> Hi @jacodt! Thanks for providing the workaround you discovered. Unfortunately, I am not very versed in the tools you used, so I cannot reproduce your findings. Would you be able to provide executable instructions for people to follow your path?

Create a directory you will be working in. Change into that directory.

Download the ```rocm-llvm``` deb file using:
`apt download rocm-llvm`

Then extract the deb file:
`ar x rocm-llvm_14.0.0.22204.50200-65_amd64.deb`

This will create a bunch of files in the directory. We now need to extract the data from ```control.tar.xz``` which was created.

`tar xf control.tar.xz`

This will create a ```control``` file in your working directory

Edit the control file with your favourite text editor, I use ```vim```

`vim control`

In the "Depends:" line, change ```python``` to ```python3```. Basically I edited the line to look like this:

`Depends: python3, libc6, libstdc++6|libstdc++8, libstdc++-5-dev|libstdc++-7-dev|libstdc++-10-dev, libgcc-5-dev|libgcc-7-dev|libgcc-10-dev, rocm-core`

Save the file and close editor
Now rebuild the `control.tar.xz` file (the `postinst` and `prerm` files should be there already):

`tar c postinst prerm control | xz -c > control.tar.xz`

Now rebuild the deb file. Please note that order of files is important, i.e. data.tar.xz should be last:
`ar rcs rocm-llvm_14.0.0.22204.50200-65_amd64.deb debian-binary control.tar.xz data.tar.xz`

Now install `libstdc++-10-dev' and 'libgcc-10-dev' (Not sure if this is needed, but because we added it to the dependencies we need to install it. I saw some posts that suggest that the llvm version bundled with rocm is compatible with this version, so I just did that):

`sudo apt-get install libstdc++-10-dev libgcc-10-dev`

Edit: We also (thanks to @sarriola below) need to now install rocm-core:
`sudo apt install rocm-core`

Now we install our newly packaged deb file:
`sudo dpkg -i rocm-llvm_14.0.0.22204.50200-65_amd64.deb`


At this stage rocm-llvm is installed and `amdgpu-install --usecase=rocm` works. Basically run the `amdgpu-install` command for your usecase. Since `rocm-llvm` is now installed, it no longer complains about dependencies.

Additional things I also did:
Earlier in this thread there was mention of the deadsnakes repo to install python3.8, I also did that to clear some other dependency. Also if your `/opt/rocm/bin/clinfo` is showing 0 devices make sure your user belong to the `render` and `video` groups:
`sudo usermod -a -G render $LOGNAME`
`sudo usermod -a -G video $LOGNAME`

Good luck. Took me ages to get this stupid thing working, but at least now `tensorflow-rocm` is working on my machine and I can continue my work. Also, since `opencl` works, you can get `plaidml` to work with `keras`.

I have also managed to recompile `pytorch` with the installed `rocm` and I got that working as well. 

All of this was done on my Ubuntu 22-04 machine which is running the standard `5.15.0-41-generic` kernel (had some dkms issues with the low-latency kernel so switched to generic). I am using a AMD RX 6800XT card.







---

### 评论 #39 — sarriola (2022-07-25T21:05:11Z)

Thanks @jacodt for your step-by-step instructions!

I had one issue when installing the newly packaged rocm-llvm  deb file because
of a rocm-core dependency.

> Now we install our newly packaged deb file:

> sudo dpkg -i rocm-llvm_14.0.0.22204.50200-65_amd64.deb
> dpkg: dependency problems prevent configuration of rocm-llvm:
>  rocm-llvm depends on rocm-core; however:
>   Package rocm-core is not installed.
> 

So, the fix was easy and I just tried installing rocm-core with:
> apt install rocm-core

Then I tried installing the rocm-llvm again and everything worked!

Thanks Again. Now I can take advantage of my integrated AMD Radeon graphics for a developmental version of Blender 3.3.





---

### 评论 #40 — qakcn (2022-08-04T12:41:35Z)

@jacodt Thanks a lot. Your solution saved me form suffering.

---

### 评论 #41 — novaspirit (2022-08-04T16:38:31Z)

@jacodt you solution works perfectly! i have followed the steps and created the deb files and uploaded everything to my git. feel free to use! [novaspirit/amdgpu-rocm-ubu22](https://novaspirit.github.io/amdgpu-rocm-ubu22/)

---

### 评论 #42 — smaga38 (2022-08-14T20:28:08Z)

@jacodt thank you good man
it helped me a lot

---

### 评论 #43 — LucasDaniOV (2022-08-14T23:19:36Z)

@jacodt thanks a lot for your time and help.
I'm curious how did you fix these dependencies? libstdc++-5-dev, libstdc++-7-dev, libgcc-5-dev, ibgcc-7-dev

With your solution the python dependency is fine, how did you take care of the other?

---

### 评论 #44 — qakcn (2022-08-15T09:39:49Z)

> @jacodt thanks a lot for your time and help. I'm curious how did you fix these dependencies? libstdc++-5-dev, libstdc++-7-dev, libgcc-5-dev, ibgcc-7-dev
> 
> With your solution the python dependency is fine, how did you take care of the other?

@LucasDaniOV You should check again. The modification of `Depends:` line in `control` file is not only changing `python3`, but also adding `|libstdc++-10-dev` and `|libgcc-10-dev`.

---

### 评论 #45 — LucasDaniOV (2022-08-15T10:07:15Z)

@qakcn You are right! thanks for telling me I completely missed it lol. It finally works :) Thank you @jacodt 

---

### 评论 #46 — vskode (2022-08-15T12:01:14Z)

Thanks a lot for the solution you have posted @jacodt . 
Unfortunately I still get a dependency error:
xserver-xorg-amdgpu-video-amdgpu : Depends: xorg-video-abi-24 but it is not installable

However, I am running 5.15.0-43-generic and not 5.15.0-41-generic because on the older version my wifi and bluetooth card aren't detected. But is that a likely source of the error? I thought anything within the 5.15 kernel versions should be backward-compatible. Anyway, if anyone has a suggestion how to fix that error, I'd love to hear it.

P.S. Just to check, the amdgpu-install file that has worked for all of you to install is the most recent one (amdgpu-install_22.20.50201-1_all.deb), correct?

Thank you so much

---

### 评论 #47 — jacodt (2022-08-15T12:59:28Z)

> Thanks a lot for the solution you have posted @jacodt . Unfortunately I still get a dependency error: xserver-xorg-amdgpu-video-amdgpu : Depends: xorg-video-abi-24 but it is not installable
> 
> However, I am running 5.15.0-43-generic and not 5.15.0-41-generic because on the older version my wifi and bluetooth card aren't detected. But is that a likely source of the error? I thought anything within the 5.15 kernel versions should be backward-compatible. Anyway, if anyone has a suggestion how to fix that error, I'd love to hear it.
> 
> P.S. Just to check, the amdgpu-install file that has worked for all of you to install is the most recent one (amdgpu-install_22.20.50201-1_all.deb), correct?
> 
> Thank you so much

Mmm... that is strange. I just checked and can't duplicate the problem. Specifically I downloaded the ```xserver-xorg-amdgpu-video-amdgpu``` file (using ```apt download```)

Then I typed ```dpkg -I xserver-xorg-amdgpu-video-amdgpu_1%3a22.0.0.50200-1438747~22.04_amd64.deb```
(note uppercase 'I', lowercase 'i' would install)

This showed that it depends on ```xorg-video-abi-25``` (not ```xorg-video-abi-24```)

Maybe try downloading the package manually (using apt download) and installing via dpkg (make sure to run apt update first)? 
Also, are you using xorg or wayland? Maybe that is also an issue (for what it is worth I am on wayland).

It is very unlikely that the issue is related to a kernel subversion number. I am on 5.15-0-46-generic at the moment and everything still working fine.

To your other point, I haven't yet used the latest install package. My writeup in the previous post was using the older package. I don't **think** that is the problem... as all the packages are still ultimately fetched from the AMD repo. 



---

### 评论 #48 — vskode (2022-08-15T15:16:55Z)

Thanks for your advice.
I got it to work - the install package actually was the reason it didn't work. Once I installed the new install package it told me that my rocm-cmake version was incorrect, so I purged my current installation and cloned this repo https://github.com/RadeonOpenCompute/rocm-cmake . That ended up doing the trick and it finally worked.
Sadly I found out afterwards, that there is no support for the integrated GPU's, like the gfx90c, which is what I'm using. 
Thanks a lot for the help anyway!

---

### 评论 #49 — wolfdraak (2022-08-15T18:35:31Z)

Notwithstanding the fact that on a clean install of Ubuntu 22.04 and 22.04.1 I get all the same above unmet errors (dependencies not met) when trying to install the latest drivers for a MSI Radeon RX 6650 XT card from AMD's site and following various iterations of amdgpu-install. **I also get:**
```
`sudo lshw -c video

  *-display                 
       description: VGA compatible controller
       product: Advanced Micro Devices, Inc. [AMD/ATI]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:0b:00.0
       logical name: /dev/fb0
       version: c1
       width: 64 bits
       **clock: 33MHz**
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom fb
       configuration: depth=32 driver=amdgpu latency=0 resolution=3840,2160
       resources: iomemory:7c0-7bf iomemory:7e0-7df irq:111 memory:7c00000000-7dffffffff memory:7e00000000-7e0fffffff ioport:f000(size=256) memory:fcc00000-fccfffff memory:fcd00000-fcd1ffff
redacted@redacted-PC:~$ lsmod | grep amd
edac_mce_amd           36864  0
amdgpu               9850880  22
iommu_v2               24576  1 amdgpu
gpu_sched              45056  1 amdgpu
drm_ttm_helper         16384  1 amdgpu
ttm                    86016  2 amdgpu,drm_ttm_helper
drm_kms_helper        311296  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
drm                   622592  15 gpu_sched,drm_kms_helper,amdgpu,drm_ttm_helper,ttm
`
```

Does the above indicate I have bigger issues with this card basically not being recognized at all by Ubuntu? Advice please!

---

### 评论 #50 — NoobOfDecades (2022-08-15T19:04:18Z)

Same issues. Following. AMD please improve support for Ubuntu 22.04.1

---

### 评论 #51 — nmcela (2022-08-16T16:24:07Z)

I knew I was going to destroy my computer if I ran the update and lo & behold, this time it was AMD that didn't disappoint me. :D This is absurd, is every regular Ubuntu + AMD user's computer now broken? 

I have a RX590 and I'm not using it for this OpenCL stuff. Just the regular usecase. Luckily @jacodt solution works, though also needs a `sudo apt install rocm-core` in the end [as detailed here](https://askubuntu.com/a/1422287/1562435) (edit: and apparently earlier in this thread too).

---

### 评论 #52 — robert2555 (2022-08-17T17:54:04Z)

Same here on Ubuntu 22.04.1 LTS
```
amdgpu-install --opencl=rocr --vulkan=pro
Hit:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:2 http://de.archive.ubuntu.com/ubuntu jammy InRelease                      
Hit:3 https://brave-browser-apt-release.s3.brave.com stable InRelease          
Hit:4 https://repo.steampowered.com/steam stable InRelease                     
Get:5 http://de.archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]     
Hit:6 http://repository.spotify.com stable InRelease                           
Hit:7 https://ppa.launchpadcontent.net/obsproject/obs-studio/ubuntu jammy InRelease
Get:8 http://de.archive.ubuntu.com/ubuntu jammy-backports InRelease [99,8 kB]  
Hit:9 https://repo.radeon.com/amdgpu/22.20/ubuntu jammy InRelease              
Get:10 http://de.archive.ubuntu.com/ubuntu jammy-updates/main amd64 DEP-11 Metadata [91,6 kB]
Get:11 http://de.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 DEP-11 Metadata [141 kB]
Get:12 http://de.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 DEP-11 Metadata [940 B]
Get:13 http://de.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 DEP-11 Metadata [12,5 kB]
Fetched 460 kB in 1s (653 kB/s)              
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package rocm-hip-runtime
E: Unable to locate package rocm-opencl-runtime
E: Unable to locate package vulkan-amdgpu-pro
E: Unable to locate package vulkan-amdgpu-pro:i386

```

---

### 评论 #53 — dpospisil (2022-08-18T07:36:53Z)

I have opened support ticket with AMD on 07/19. After full month of nonsense questions the support guy finally admited that there is an issue and according to his/her words contacted driver team yesterday. It is absolutely unbeliavable how bad is AMD doing.

---

### 评论 #54 — saadrahim (2022-08-18T15:07:24Z)

> I have opened support ticket with AMD on 07/19. After full month of nonsense questions the support guy finally admited that there is an issue and according to his/her words contacted driver team yesterday. It is absolutely unbeliavable how bad is AMD doing.

Is this the support ticket? Or did you raise it separately?

---

### 评论 #55 — M4ST3R0FD1S4ST3R (2022-09-03T16:37:01Z)

Any way this can be made to work on Pop!_OS 22.04?

---

### 评论 #56 — jacodt (2022-09-03T16:51:13Z)

> Any way this can be made to work on Pop!_OS 22.04?

In theory it should be possible if you are able to run a 5.15 kernel on Pop!_OS 22.04. You would also need to edit the **amdgpu-install** script once the installer from amd is loaded, since it is hardcoded to only detect ubundu and linuxmint as debian based. The you would likely also need to edit the deb file for rocm-llvm as highlighted in an earlier post.

But the kernel version is the most important. I have never managed to get it working on a non-supported kernel. Since theoretically Pop 22.04 is based off Ubuntu 22.04 the kernel **should** be fine, unless System76 is ahead of the game again.

---

### 评论 #57 — wolfdraak (2022-09-06T15:42:26Z)

How is AMD still failing linux users this hard months after the issue is known?

---

### 评论 #58 — M4ST3R0FD1S4ST3R (2022-09-07T15:35:56Z)

> > Any way this can be made to work on Pop!_OS 22.04?
> 
> In theory it should be possible if you are able to run a 5.15 kernel on Pop!_OS 22.04. You would also need to edit the **amdgpu-install** script once the installer from amd is loaded, since it is hardcoded to only detect ubundu and linuxmint as debian based. The you would likely also need to edit the deb file for rocm-llvm as highlighted in an earlier post.
> 
> But the kernel version is the most important. I have never managed to get it working on a non-supported kernel. Since theoretically Pop 22.04 is based off Ubuntu 22.04 the kernel **should** be fine, unless System76 is ahead of the game again.

Pop!_OS 22.05 runs kernel version 5.18, also couldn't find the sub-directory where the install script is located when unpacking the apt file.

---

### 评论 #59 — AbelVM (2022-09-10T10:35:45Z)

Hmmm... Nope, regardless the release notes, it's not installable/compatible with Ubuntu 22.4.x yet

![image](https://user-images.githubusercontent.com/9017165/189479493-c0aebe26-58e8-4839-9b90-79f054b7196d.png)


---

### 评论 #60 — colibris79 (2022-09-13T06:30:35Z)

@jacodt Thank you very much for describing the process. I've managed to install amdgpu with it in my Mint 21 (Ubuntu 22.04), Kernel 5.15.0-47 and  Ryzen 7 4700U PC. After the installation everything seems fine but rocm-llvm has been kept back because of the dependencies that caused the problem in the first place:
The following packages have unmet dependencies:
```
 rocm-llvm : Depends: python but it is not going to be installed
             Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
```
Is this to be expected and should be solved when the rocm package from the Radeon repositories is updated for Ubuntu 22.04? I've checked the .deb package created following your instructions and the control file has no longer mention of python and has libstdc++10 and libgcc10 (which they are installed).  I've tried purging the package and reinstalling but I still get the same message.
So why is rocm-llvm still looking for these packages after modifying the control file and successfully installing?

---

### 评论 #61 — Laitaps (2022-09-13T12:38:15Z)

> I knew I was going to destroy my computer if I ran the update and lo & behold, this time it was AMD that didn't disappoint me. :D This is absurd, is every regular Ubuntu + AMD user's computer now broken?
> 
> I have a RX590 and I'm not using it for this OpenCL stuff. Just the regular usecase. Luckily @jacodt solution works, though also needs a `sudo apt install rocm-core` in the end [as detailed here](https://askubuntu.com/a/1422287/1562435) (edit: and apparently earlier in this thread too).

Yes, it is rather absurd.  On top of that, this has been in discussion since before 22.04 was even released.

---

### 评论 #62 — Laitaps (2022-09-13T12:38:37Z)

AMD is doing its best to sell more NVIDIA hardware.

---

### 评论 #63 — michieal (2022-09-20T00:29:01Z)

Ya know... it's really difficult to get the driver working properly when half of the packages just outright fail.

`The following packages have unmet dependencies:
 rocm-gdb : Depends: libpython3.8 but it is not installable
 rocm-llvm : Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
E: Unable to correct problems, you have held broken packages.
`

And yeah, this is a common problem across the userbase. My real question here is this:
You have the ability to detect the version of Ubuntu being ran.. Why the F@*! didn't you make a 22.04 package that had updated requirements so that it would install?! And I swear to the gods of gaming, wine, and lacy things that if ya tell me that this is a "They won't mind..." situation, I'm done with AMD after decades of supporting them (since ~1994.)

Also, your user base should NOT be your testing base. FFS.

---

### 评论 #64 — Moerty (2022-09-22T20:57:14Z)

https://repo.radeon.com/amdgpu-install/22.20.3/ubuntu/jammy/

---

### 评论 #65 — ghost (2022-09-22T22:45:26Z)

> https://repo.radeon.com/amdgpu-install/22.20.3/ubuntu/jammy/

@Moerty is this a new update that is now working?

---

### 评论 #66 — colibris79 (2022-09-22T22:53:49Z)

> > https://repo.radeon.com/amdgpu-install/22.20.3/ubuntu/jammy/
> 
> @Moerty is this a new update that is now working?

Don't think so. That is the one I have installed and I still had to follow @jacodt method to install and it keeps rocm-llvm held back 

---

### 评论 #67 — ghost (2022-09-22T23:14:39Z)

@colibris79 

Thanks. I just did a fresh reinstall so i think I'll try jacodt method now (it wasn't working on my upgraded mint)

---

### 评论 #68 — colibris79 (2022-09-22T23:19:01Z)




> @colibris79
> 
> Thanks. I just did a fresh reinstall so i think I'll try jacodt method now (it wasn't working on my upgraded mint)

Same here with Mint21. You can install if you skip installing rocm, otherwise you need to follow jacodt's method

---

### 评论 #69 — ghost (2022-09-22T23:28:38Z)

@colibris79 my main desire is to get blender running.

Will that work without ROCM? jacodt's method isn't working for me, `Error: package rocm-llvm not found in APT cache!`

---

### 评论 #70 — colibris79 (2022-09-22T23:37:48Z)

Install amdgpu that will add the package. Then 
apt-get download rocm-llvm
Follow the instructions to modify the deb file and install



---

### 评论 #71 — ghost (2022-09-22T23:39:17Z)

@colibris79 you star! appreciate you :)

---

### 评论 #72 — peluca13 (2022-09-23T15:14:35Z)

i got a fresh kubuntu 22.04 installation and sucessfully performed jacodt's method to install the latest amd driver for my radeon rx 590. But the performance on my computer regarding games was even worst ... i got to rollback to the default drivers that cames with the os. Anyone with the same issue?

---

### 评论 #73 — jacodt (2022-09-23T16:27:59Z)

Potentially easier way to resolve the dependency issue on Ubuntu 22.04:

I built three dummy debian packages that does nothing other than provide a dependency for **libstdc++-7-dev**, **libgcc-7-dev** and **python**. They were built using **equivs-build**. You can install these with **dpkg** and then the amd install doesn't break and you don't need to edit the package from AMD. Just make sure that you have some kind of libstdc++ dev package installed (I used libstdc++-10-dev)

[https://github.com/jacodt/rocm_dummy_packages](https://github.com/jacodt/rocm_dummy_packages)



---

### 评论 #74 — liv09370 (2022-10-05T15:22:12Z)

apt-get download rocm-llvm
sudo dpkg --ignore-depends=libstdc++-5-dev --ignore-depends=libstdc++-7-dev --ignore-depends=libgcc-7-dev --ignore-depends=libgcc-5-dev --ignore-depends=python -i rocm-llvm_1*.deb

---

### 评论 #75 — colibris79 (2022-10-06T01:28:24Z)





> apt-get download rocm-llvm sudo dpkg --ignore-depends=libstdc++-5-dev --ignore-depends=libstdc++-7-dev --ignore-depends=libgcc-7-dev --ignore-depends=libgcc-5-dev --ignore-depends=python -i rocm-llvm_1*.deb

Tried it and I ended up with rocm-llvm as a broken package. Went back to jacodt's method, there the package shows as held back, but not broken

---

### 评论 #76 — chrysochos (2022-10-08T09:50:29Z)

Run the command  "amdgpu-uninstall"  and reboot the system.
In my case I run the command outside of the Desktop. I pressed Ctrl+Alt+F4 and I logged in as root. Then I run "amdgpu-uninstall" and "reboot".
 


---

### 评论 #77 — NatoBoram (2022-10-16T19:18:24Z)

So I bought a RX 6700 XT last week, and...

It's weird enough that, [in multi-display configurations, FreeSync will *not* be engaged (even if both FreeSync displays are identical)](https://www.amd.com/en/support/kb/faq/gpu-754#faq-Limitation-of-AMD-FreeSync-on-Linux);

It's weird enough that I have to modify `/usr/bin/amdgpu-install` to add `pop` in `os_release` since it doesn't check `ID_LIKE` in `/etc/os-release`;

It's weird enough that I have to modify `/usr/bin/amdgpu-install` to nuke `debian_build_package_list` because it looks for a package that doesn't exist;

But that I have to install [these dummy packages](https://github.com/jacodt/rocm_dummy_packages) to make it work in Ubuntu **L**ong **T**ime **S**upport when it's a known problem since literally 206 days is just plain offensive.

Also it still doesn't work.

```bash
The following packages have unmet dependencies:
 xserver-xorg-amdgpu-video-amdgpu : Depends: xorg-video-abi-24
E: Unable to correct problems, you have held broken packages.
```

```bash
Package xorg-video-abi-24 is a virtual package provided by:
  xserver-xorg-core 2:1.20.13-1ubuntu1~20.04.3 [Not candidate version]
  xserver-xorg-core 2:1.20.8-2ubuntu2 [Not candidate version]
```

Other steps I went through:

* Create a `/etc/apt/sources.list.d/ubuntu.list` file with outdated `source.list` entries.

```list
deb http://ca.archive.ubuntu.com/ubuntu focal           main restricted universe multiverse # Ubuntu
deb http://ca.archive.ubuntu.com/ubuntu focal-security  main restricted universe multiverse # Ubuntu
deb http://ca.archive.ubuntu.com/ubuntu focal-updates   main restricted universe multiverse # Ubuntu
deb http://ca.archive.ubuntu.com/ubuntu focal-proposed  main restricted universe multiverse # Ubuntu
deb http://ca.archive.ubuntu.com/ubuntu focal-backports main restricted universe multiverse # Ubuntu
deb http://archive.canonical.com/ubuntu focal           partner                             # Ubuntu
```

* Download and install `xserver-xorg-core_1.20.13-1ubuntu1~20.04.3_amd64.deb` from https://launchpad.net/~ubuntu-security/+archive/ubuntu/ppa/+build/24150343

And even after it went through...

```bash
ERROR (dkms apport): kernel package linux-headers-5.19.0-76051900-generic is not supported
Error! Bad return status for module build on kernel: 5.19.0-76051900-generic (amd64)
Consult /var/lib/dkms/amdgpu/5.16.9.22.20-1438746~20.04/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

It's literally easier to install Nvidia drivers :/

By that point, I had some outdated dependencies already installed, so I could remove the outdated `source.list` and just

```bash
amdgpu-install --uninstall
amdgpu-install --no-dkms
```

**Edit:** An auto-update borked my system. TL;DR: Don't use `amdgpu-install`, it'll bork your system, too.

---

### 评论 #78 — ToucheSir (2022-10-16T20:05:11Z)

Having also set up a 6700 XT recently, I found that (much like with Nvidia GPUs/CUDA) avoiding the installation script altogether and leaning on distro package management is the better solution. In other words, skip `amdgpu-install` entirely and follow the instructions under https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3/page/How_to_Install_ROCm.html#d23e2424 ("Using Package Manager on Ubuntu" if the anchor breaks in the future). Choosing the "Repositories with Latest Packages" variant of each command was sufficient, as was installing package variants without any versions in the name (e.g. `rocm-hip-sdk` instead of `rocm-hip-sdk5.3`).

The only benefit `amdgpu-install` adds is preset lists of packages for each "usecase", but you can just copy those from the script in the .deb if you can't find the packages you need some other way.

---

### 评论 #79 — Martinc4321 (2022-10-17T21:57:21Z)

Still no fix ? @Rmalavally 
Still getting an error on my Ubuntu 22.04 ... 
With running "amdgpu-install --usecase=rocm"
All friends have fun with stable diffusion,
while me cannot get drivers :/
```
The following packages have unmet dependencies:
 openmp-extras : Depends: libstdc++-5-dev but it is not installable or
                          libstdc++-7-dev but it is not installable
                 Depends: libgcc-5-dev but it is not installable or
                          libgcc-7-dev but it is not installable
 rocm-llvm : Depends: python but it is not installable
             Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
```


---

### 评论 #80 — Martinc4321 (2022-10-17T21:59:37Z)

@zhang2amd ?

---

### 评论 #81 — Martinc4321 (2022-10-17T22:10:06Z)

I removed --purge amdgpu-install +
After installing using manual/ guide to get latest version:
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3/page/How_to_Install_ROCm.html
I am getting this ...
```

amdgpu-install --usecase=rocm
Hit:1 http://sk.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://sk.archive.ubuntu.com/ubuntu jammy-updates InRelease                                                              
Hit:3 http://sk.archive.ubuntu.com/ubuntu jammy-backports InRelease                                                            
Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                               
Hit:5 https://apt.repos.intel.com/mkl all InRelease                                                                            
Hit:6 https://ppa.launchpadcontent.net/kisak/kisak-mesa/ubuntu jammy InRelease                                                 
Hit:7 https://ppa.launchpadcontent.net/oibaf/graphics-drivers/ubuntu jammy InRelease                     
Hit:8 https://repo.radeon.com/amdgpu/5.3/ubuntu focal InRelease       
Hit:9 https://repo.radeon.com/rocm/apt/5.3 focal InRelease
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
linux-headers-5.15.0-50-generic is already the newest version (5.15.0-50.56).
linux-headers-5.15.0-50-generic set to manually installed.
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dev : Depends: rocm-cmake (= 0.8.0.50300-63~20.04) but 5.0.0-1 is to be installed
            Depends: rocm-device-libs (= 1.0.0.50300-63~20.04) but 5.0.0-1 is to be installed
            Depends: rocm-utils (= 5.3.0.50300-63~20.04) but it is not going to be installed

```

---

### 评论 #82 — Rmalavally (2022-10-17T22:19:34Z)

Thank you for reaching out. Let me discuss this internally and get back to you. Appreciate your letting us know.

Regards,
ROCm Documentation Team

---

### 评论 #83 — Martinc4321 (2022-10-17T22:28:05Z)


![example](https://user-images.githubusercontent.com/43873903/196295293-f8f2635c-db46-4d27-af67-de0bc540f48e.png)
I tried to isntall older version of rocm using 
"sudo amdgpu-install --usecase=rocm --rocmrelease=4.5.0 --no-dkms"

Got this:```

sudo amdgpu-install --usecase=rocm --rocmrelease=4.5.0 --no-dkms
Hit:1 http://sk.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://sk.archive.ubuntu.com/ubuntu jammy-updates InRelease                                                                                                    
Hit:3 http://sk.archive.ubuntu.com/ubuntu jammy-backports InRelease                                                                                                  
Hit:4 https://ppa.launchpadcontent.net/kisak/kisak-mesa/ubuntu jammy InRelease                                                                                       
Hit:5 https://apt.repos.intel.com/mkl all InRelease                                                               
Hit:6 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                
Hit:7 https://ppa.launchpadcontent.net/oibaf/graphics-drivers/ubuntu jammy InRelease                                           
Hit:8 https://repo.radeon.com/amdgpu/5.3/ubuntu focal InRelease       
Hit:9 https://repo.radeon.com/rocm/apt/5.3 focal InRelease
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package rocm-dev4.5.0
E: Couldn't find any package by glob 'rocm-dev4.5.0'
E: Couldn't find any package by regex 'rocm-dev4.5.0'
```


---

### 评论 #84 — Martinc4321 (2022-10-17T22:29:00Z)

My gpu info:
```
sudo lshw -C display
  *-display                 
       description: VGA compatible controller
       product: Navi 10 [Radeon RX 5600 OEM/5600 XT / 5700/5700 XT]
       vendor: Advanced Micro Devices, Inc. [AMD/ATI]
       physical id: 0
       bus info: pci@0000:28:00.0
       logical name: /dev/fb0
       version: c4
       width: 64 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom fb
       configuration: depth=32 driver=amdgpu latency=0 resolution=2560,1080
       resources: irq:105 memory:d0000000-dfffffff memory:e0000000-e01fffff ioport:e000(size=256) memory:fcd00000-fcd7ffff memory:c0000-dffff

```

---

### 评论 #85 — Martinc4321 (2022-10-17T22:41:37Z)

Here is `rocminfo` output:
```
(base) conto@conto-MS-7B85:~$ rocminfo
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 3700X 8-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor 
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3600                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    16302516(0xf8c1b4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    16302516(0xf8c1b4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16302516(0xf8c1b4) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1010                            
  Uuid:                    GPU-XX                             
  Marketing Name:          AMD Radeon RX 5700                 
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
    L2:                      4096(0x1000) KB                    
  Chip ID:                 29471(0x731f)                      
  ASIC Revision:           2(0x2)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1750                               
  BDFID:                   10240                              
  Internal Node ID:        1                                  
  Compute Unit:            36                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    1280(0x500)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1010:xnack-  
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             

```

---

### 评论 #86 — xuhuisheng (2022-10-17T23:19:25Z)

@Martinc4321 
Unfortunately, gfx1010 is not on the list of ROCm offical support list.

And I test gfx1010 on ROCm-5.3.0 with `export HSA_OVERRIDE_GFX_VERSION=10.3.0` hack, but it broke on ROCm-5.3.0 this time.

---

### 评论 #87 — njzjz (2022-10-26T23:20:50Z)

> ```
> The following packages have unmet dependencies:
>  rocm-dev : Depends: rocm-cmake (= 0.8.0.50300-63~20.04) but 5.0.0-1 is to be installed
>             Depends: rocm-device-libs (= 1.0.0.50300-63~20.04) but 5.0.0-1 is to be installed
>             Depends: rocm-utils (= 5.3.0.50300-63~20.04) but it is not going to be installed
> ```

@Martinc4321 I got how to resolve this error. Add a `pin-priority` file to `/etc/apt/preferences.d` before executing `apt-get`:

```bash
printf 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | tee /etc/apt/preferences.d/rocm-pin-600 
```

---

### 评论 #88 — martadinata666 (2022-11-05T17:47:06Z)

I just following the guide, and it install correclty, i saw the apt log that many still using `focal` instead updating repo to `jammy`

`deb [arch=amd64] https://repo.radeon.com/amdgpu/5.3/ubuntu jammy main`

---

### 评论 #89 — erkinalp (2022-11-10T08:25:07Z)

Resolved in 5.3

---

### 评论 #90 — mchaker (2022-11-10T10:09:38Z)

Thank you so much Radeon/ROCm team!

![image](https://user-images.githubusercontent.com/10101544/201062759-3ef3ede8-9590-40e9-9e12-fcf54d43ece0.png)

---

### 评论 #91 — hostingnuggets (2022-11-11T19:53:36Z)

So is this also finally fixed inside the AMD GPU installer from AMD for Ubuntu 22.04 LTS?


---

### 评论 #92 — Martinc4321 (2022-11-22T13:12:07Z)

I can confirm. Finally i can use my hardware. And use i will.
Many thanks ;)

There was just One small error with python libs but i was able to solve it pretty quickly.
["ImportError: libamdhip64.so.5](https://github.com/RadeonOpenCompute/ROCm/issues/1753)

---

### 评论 #93 — Martinc4321 (2022-11-22T13:28:34Z)

> @Martinc4321 Unfortunately, gfx1010 is not on the list of ROCm offical support list.
> 
> And I test gfx1010 on ROCm-5.3.0 with `export HSA_OVERRIDE_GFX_VERSION=10.3.0` hack, but it broke on ROCm-5.3.0 this time.

As you sad now i can see message about unsupported device.
Export you mentioned enables it to not show given error but it will die on:
```
2022-11-22 14:22:53.461610: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.535615: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.535677: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.535991: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-11-22 14:22:53.536651: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.536716: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.536752: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.536858: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.536908: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.536946: I tensorflow/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-11-22 14:22:53.536969: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1616] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 7676 MB memory:  -> device: 0, name: AMD Radeon RX 5700, pci bus id: 0000:28:00.0
2022-11-22 14:22:53.746371: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:00.310785: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
Transforming target 0
Transforming target 1
Transforming target 2
Transforming target 3
2022-11-22 14:23:08.376620: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:08.714553: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
TF dataset transform done
Creating TF input data structure
2022-11-22 14:23:20.345216: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.345847: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.351685: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.358503: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.359383: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.378206: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.380787: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
2022-11-22 14:23:20.383370: I tensorflow/core/common_runtime/gpu_fusion_pass.cc:507] ROCm Fusion is enabled.
Memory access fault by GPU node-1 (Agent handle: 0x557dd7244580) on address 0x7fee70b23000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```

EDIT:
Different version seems to work
`export HSA_OVERRIDE_GFX_VERSION=10.0.0`

EDIT:
I found out it uses CPU with that env var. ...
So yeah it is not working as you said .

---

### 评论 #94 — Martinc4321 (2022-11-25T20:09:29Z)

OK, combination of Ubuntu 20.04 and rocm-5.2.0 on the official TensorFlow docker [image](https://blog.tensorflow.org/2018/08/amd-rocm-gpu-support-for-tensorflow.html) ([hub.docker](https://hub.docker.com/r/rocm/tensorflow/) using instruction in description)
Inside the docker image running
and  adding `export HSA_OVERRIDE_GFX_VERSION=10.3.0` 
and runing base stuff as "apt update", installing pip+packages(you use). 

It uses my GPU Navi 10 [Radeon RX 5600 OEM/5600 XT / 5700/5700 XT]!!! ( Checked by `radeontop`, that it is uses its resources.)
(sadly it is slower than using CPU outside docker ( But someone might make OS image from that docker and run it natively. ( I don't plan to do that.)))



---

### 评论 #95 — karim789 (2022-12-12T00:28:07Z)

doesnt work for Ubuntu 22.04.1 and installer amdgpu-install_22.20.50200-1_all.deb

> $ sudo LANG=C amdgpu-install
> Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
> Get:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]                                                                         
> Hit:5 http://archive.ubuntu.com/ubuntu jammy InRelease                                                                                      
> Hit:7 https://repo.radeon.com/amdgpu/22.20/ubuntu jammy InRelease                                         
> Hit:8 https://repo.radeon.com/rocm/apt/5.2 ubuntu InRelease
> Fetched 224 kB in 1s (371 kB/s)
> Reading package lists... Done
> Reading package lists... Done
> Building dependency tree... Done
> Reading state information... Done
> linux-headers-5.15.0-56-generic is already the newest version (5.15.0-56.62).
> linux-headers-5.15.0-56-generic set to manually installed.
> linux-modules-extra-5.15.0-56-generic is already the newest version (5.15.0-56.62).
> linux-modules-extra-5.15.0-56-generic set to manually installed.
> Some packages could not be installed. This may mean that you have
> requested an impossible situation or if you are using the unstable
> distribution that some required packages have not yet been created
> or been moved out of Incoming.
> The following information may help to resolve the situation:
> 
> The following packages have unmet dependencies:
>  rocm-llvm : Depends: python but it is not installable
>              Depends: libstdc++-5-dev but it is not installable or
>                       libstdc++-7-dev but it is not installable
>              Depends: libgcc-5-dev but it is not installable or
>                       libgcc-7-dev but it is not installable
>              Recommends: gcc-multilib but it is not going to be installed
>              Recommends: g++-multilib but it is not going to be installed
> E: Unable to correct problems, you have held broken packages



---

### 评论 #96 — xuhuisheng (2022-12-12T02:56:34Z)

@karim789 
Please try latest ROCm-5.4
<https://repo.radeon.com/amdgpu/5.4/ubuntu/>

---

### 评论 #97 — karim789 (2022-12-12T11:35:38Z)

> @karim789 Please try latest ROCm-5.4 https://repo.radeon.com/amdgpu/5.4/ubuntu/

The issue is rather that the link to the amdgpu installer on the AMD driver page points to an obsolete driver .deb file.

Anyway it appears that my R9 280X isn't supported by the amdgpu driver.
I wanted to try proprietary driver hoping it would fix the issue where I have no Atmos audio working below a screen refresh rate of 30hz, therefore no 24p which is annoying to watch movies.
Considering the issue comes with R9 280X or intel HD4600 and they share the same intel_hda_audio driver and that it works with a Nvidia card, then I probably it's this driver that has an issue.

---

### 评论 #98 — Apisteftos (2023-02-14T16:08:42Z)

I installed the latest version rocm-5.4.3 and is not compatible with my hardware gfx 8.3.0. I am using Ubuntu 22.04.1 LTS. I have `Radeon RX 480` with compatible VGA controller ` Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (rev c7)`. Hence, I uninstalled the `rocm-5.4.3` version and I am trying to install the `rocm-4.5.x` version.  While I trying to install this version under the command `amdgpu-install -y --usecase=rocm` throws me couple of dependencies packages. 

<pre>
The following packages have unmet dependencies:
 openmp-extras : Depends: libstdc++-5-dev but it is not installable or
                          libstdc++-7-dev but it is not installable
                          Depends: libgcc-5-dev but it is not installable or
                          libgcc-7-dev but it is not installable
 rocm-llvm : Depends: python but it is not installable
                    Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
                      Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
E: Unable to correct problems, you have held broken packages.
</pre>

Now, I came to this thread and reading all the above comments, tried to install these dependencies. I installed python 3.8 under the command: 

`sudo add-apt-repository ppa:deadsnakes/ppa`
 `sudo apt-get update`
`sudo apt-get install python3.8`

downloading the package: `sudo apt-get download rocm-llvm`  was just a brocken package. Opening the Synaptic Package Manager and going on search `rocm-llvm` , right click, mark for installation throws me a message:

<pre>
Package rocm-llvm has no available version, but exists in the database.
This typically means that the package was mentioned in a dependency and never uploaded, has been obsoleted or is not available with the contents of sources.list
</pre>

So it's not possible to install the rocm-4.5.x








---

### 评论 #99 — stackcverflow (2023-04-13T11:36:30Z)

For those who want to do it quickly,

Here's a summary of the procedure for Ubuntu v22.04 (Jammy)  from the ROCm documentation
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.3/page/How_to_Install_ROCm.html#d23e2091

## Installation
```bash
sudo apt-get update
wget https://repo.radeon.com/amdgpu-install/5.3/ubuntu/jammy/amdgpu-install_5.3.50300-1_all.deb
sudo apt-get install ./amdgpu-install_5.3.50300-1_all.deb

# Add repositories
echo 'deb [arch=amd64] https://repo.radeon.com/amdgpu/latest/ubuntu jammy main' | sudo tee /etc/apt/sources.list.d/amdgpu.list
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ jammy main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt-get update

# Install Kernel mode (That may already be installed using the above commands)
sudo apt install amdgpu-dkms

# Reboot
sudo reboot
```

---

## Verification after reboot
```bash
### Kernel mode check
dkms status
>>> Response : "amdgpu/5.18.13-1538762.22.04....."

### ROCm installation check
sudo /opt/rocm-5.4.3/bin/rocminfo
>>> Response : "ROCk module is loaded"
```
---
Note: It works for my old RX 480, so it should work if you have a newer processor.
>you can find the ROCm support GPU list here: https://github.com/ROCm/ROCm.github.io/blob/master/hardware.md)

---

### 评论 #100 — chriamue (2023-10-02T19:18:59Z)

> > ```
> > The following packages have unmet dependencies:
> >  rocm-dev : Depends: rocm-cmake (= 0.8.0.50300-63~20.04) but 5.0.0-1 is to be installed
> >             Depends: rocm-device-libs (= 1.0.0.50300-63~20.04) but 5.0.0-1 is to be installed
> >             Depends: rocm-utils (= 5.3.0.50300-63~20.04) but it is not going to be installed
> > ```
> 
> @Martinc4321 I got how to resolve this error. Add a `pin-priority` file to `/etc/apt/preferences.d` before executing `apt-get`:
> 
> ```shell
> printf 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | tee /etc/apt/preferences.d/rocm-pin-600 
> ```

Pin-Priority alone didn't help me but running `amdgpu-install` with `--rocmrelease=5.7.0` worked for me:

```sh
sudo amdgpu-install --usecase=dkms,graphics,rocm,hip,hiplibsdk --rocmrelease=5.7.0
```

---
