# When do the rocm 5.5.0 release? 

> **Issue #2038**
> **状态**: closed
> **创建时间**: 2023-04-13T01:00:33Z
> **更新时间**: 2023-05-10T16:59:24Z
> **关闭时间**: 2023-05-10T16:59:24Z
> **作者**: PennyFranklin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2038

## 描述

I can't wait to use my 7900xtx to run stable diffusion under rocm, rather than directml on win11, which is a bad experience. 

---

## 评论 (43 条)

### 评论 #1 — KylinC (2023-04-13T06:55:53Z)

I can't wait, too

---

### 评论 #2 — M330570912 (2023-04-13T15:18:02Z)

我也等不及了

---

### 评论 #3 — PennyFranklin (2023-04-13T16:35:25Z)

> 我也等不及了

刚刚忒特看到了，w7900专业卡有了，ROCm支持近在眼前

---

### 评论 #4 — Roachomg (2023-04-14T01:10:14Z)

争取5.6上windows
waiting 'Rocm for windows' on version 5.6

---

### 评论 #5 — xuhuisheng (2023-04-14T01:31:48Z)

> 争取5.6上windows waiting 'Rocm for windows' on version 5.6

I am afraid ROCm-5.6 already enter internal test steps, and there is no sign to show windows official supporting.

---

### 评论 #6 — Roachomg (2023-04-14T01:45:06Z)




> > 争取5.6上windows waiting 'Rocm for windows' on version 5.6
> 
> I am afraid ROCm-5.6 already enter internal test steps, and there is no sign to show windows official supporting.

Acknowledged,thanks for reply!

---

### 评论 #7 — PennyFranklin (2023-04-14T01:53:29Z)

> > 争取5.6上windows waiting 'Rocm for windows' on version 5.6
> 
> I am afraid ROCm-5.6 already enter internal test steps, and there is no sign to show windows official supporting.

Pro w7900卡发布了，和7900xtx一个核心，那按道理来说我这个7900xtx很快就能适配ROCm了吧

---

### 评论 #8 — xuhuisheng (2023-04-14T02:39:31Z)

> > > 争取5.6上windows waiting 'Rocm for windows' on version 5.6
> > 
> > 
> > I am afraid ROCm-5.6 already enter internal test steps, and there is no sign to show windows official supporting.
> 
> Pro w7900卡发布了，和7900xtx一个核心，那按道理来说我这个7900xtx很快就能适配ROCm了吧

首先ROCm-5.5大概率能支持gfx11 - 7xxx系列。参考miopen对应ROCm-5.5的issue <https://github.com/ROCmSoftwarePlatform/MIOpen/pull/1925>

但是ROCm-5.5已经测试了4个月了，还没发布。之前也有ROCm-4.4只做内部发布，最终没有公开发布的例子，所以不敢说ROCm-5.5会不会公开发布出来。

主要是现在ROCm-5.6都进测试阶段了，也有可能一个月后ROCm-5.6直接发布出来了。到时候ROCm-5.6倒是肯定能支持gfx11。

---

### 评论 #9 — KylinC (2023-04-14T08:33:10Z)

只能用来打游戏了，大概

---

### 评论 #10 — Enferlain (2023-04-14T13:24:08Z)

rocm for windows soon copium

---

### 评论 #11 — trougnouf (2023-04-14T15:21:59Z)

I couldn't care less about Windows but 7900 XTX ROCm support (5.5.0 release) is very much looked forward to.

---

### 评论 #12 — Enferlain (2023-04-14T15:29:09Z)

1 guy on linux vs millions on windows omegalol

---

### 评论 #13 — trougnouf (2023-04-14T15:31:17Z)

> 1 guy on linux vs millions on windows omegalol

Playing with stable diffusion maybe, but not many people are doing actual ML development on Windows.

---

### 评论 #14 — wszgrcy (2023-04-14T16:09:11Z)

https://gist.github.com/In-line/c1225f05d5164a4be9b39de68e99ee2b 
but amd delete image. the torrent now no speed .......

---

### 评论 #15 — PennyFranklin (2023-04-14T16:38:55Z)

> > > > 争取5.6上windows waiting 'Rocm for windows' on version 5.6
> > > 
> > > 
> > > I am afraid ROCm-5.6 already enter internal test steps, and there is no sign to show windows official supporting.
> > 
> > Pro w7900卡发布了，和7900xtx一个核心，那按道理来说我这个7900xtx很快就能适配ROCm了吧
> 
> 首先ROCm-5.5大概率能支持gfx11 - 7xxx系列。参考miopen对应ROCm-5.5的issue <https://github.com/ROCmSoftwarePlatform/MIOpen/pull/1925>
> 
> 但是ROCm-5.5已经测试了4个月了，还没发布。之前也有ROCm-4.4只做内部发布，最终没有公开发布的例子，所以不敢说ROCm-5.5会不会公开发布出来。
> 
> 主要是现在ROCm-5.6都进测试阶段了，也有可能一个月后ROCm-5.6直接发布出来了。到时候ROCm-5.6倒是肯定能支持gfx11。

刚刚看B站直播有up主说AMD官宣win上ROCm了，既然上那肯定是一家人整整齐齐了，我已经不急了

---

### 评论 #16 — sirus20x6 (2023-04-16T11:16:23Z)

I'm also in need of 7000 support on linux. This release is months behind schedule.

---

### 评论 #17 — aoolmay (2023-04-18T10:47:10Z)

Rocm for the last two generations seems to be including, working but unofficial, gaming cards support with the release of workstation analogs.
AMD has only just announced W7800 and W7900 workstation cards. Press release mentions second half of year, still a couple months away.

Can't wait myself, but not buying into 7900 too early, might even wait for 7950 altoghether.

---

### 评论 #18 — PiotrKlimczak (2023-04-21T17:57:25Z)

There is already 5.5rc5 in the wild as docker container. Got it working fully with PyTorch on my 7900xt. 

---

### 评论 #19 — sirus20x6 (2023-04-21T18:29:52Z)

> There is already 5.5rc5 in the wild as docker container. Got it working fully with PyTorch on my 7900xt.

but have you gotten it to work outside of docker?

---

### 评论 #20 — PiotrKlimczak (2023-04-21T18:41:37Z)

Nope, so it is limited. As you need to pull sources to docker and run it there. 
Got for example stable diffusion working and quite few other examples. 
Did also simple performance checks and perf is similar to rtx 3090, but this is very limited test.
Also tbc I am not PyTorch nor python expert. Commercially I work with java but exploring slowly ai as there are plans to use it commercially at some point. So for me it is all experimental and learning at home before using commercially in a year or two. 

---

### 评论 #21 — PiotrKlimczak (2023-04-22T09:00:31Z)

Interesting. TBC I am running Linux. 
Afaik docker gives no performance penalty as it runs directly on host kernel with no hardware emulation.
The only difference with docker vs host is that docker runs its own libs on top of standard kernel and does that with its own isolated ip stack and usually cpu/ram quotas. 

---

### 评论 #22 — PiotrKlimczak (2023-04-23T15:54:15Z)

Regadless, got it working natively on Ubuntu 20.
Reason for that was that Docker umages from rocm repo were also Ubuntu 20.

1. Install ubuntu 20.04
2. Install AMDGPU PRO driver from AMD website
3. Restart ubuntu to pick up new driver
4. Install Anaconda from the net
5. $ conda create -n anaconda38 python=3.8
6. $ conda activate anaconda38
7. $ export HIP_VISIBLE_DEVICES=0
8. $ export PYTORCH_ROCM_ARCH="gfx1100"
9. pull "rocm/composable_kernel:ck_ub20.04_rocm5.5_rc5" docker image and start it (unfortunately not avaialble anymore as they keep deleting them)
10. Copy /opt/rocm* from docker image to your local /opt
11. Install PyTorch 2.0.0 as per https://github.com/pytorch/pytorch#from-source to youor conda 

Above is was inspired by https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions/9591





---

### 评论 #23 — PiotrKlimczak (2023-04-23T20:57:15Z)

Works also on Ubuntu 22 with conda but required quite few hacks so don't recommend trying until official build available.

---

### 评论 #24 — PennyFranklin (2023-04-24T00:57:15Z)

> Works also on Ubuntu 22 with conda but required quite few hacks so don't recommend trying until official build available.

thanks a lot, and actually I use ubuntu 22, so I'll wait or even wait for the Windows  release 

---

### 评论 #25 — sirus20x6 (2023-04-27T00:24:29Z)

I check back 3 times a day to see if I can use the gpu I paid $1,000 for. still the answer is no.

---

### 评论 #26 — PennyFranklin (2023-04-27T00:37:21Z)

i paid for almost 1300 dollars : ( GPU's price was very crazy at China months ago. and enen so i can't enjoy the functions after a long time wait... i consider i would buy NVIDIA card for the next time 

---

### 评论 #27 — countradooku (2023-04-28T10:31:00Z)

https://github.com/RadeonOpenCompute/ROCm/pull/2094

no windows suport nice nice very nice.

---

### 评论 #28 — countradooku (2023-05-02T06:16:26Z)

We don't even have Rx 7900xtx support ik this release. Cool

---

### 评论 #29 — sucaiji (2023-05-02T06:44:41Z)

Amd, fuck you! I've been waiting for almost half a year, why doesn't version 5.5 still support 7900XT/7900XTX?

---

### 评论 #30 — countradooku (2023-05-02T06:49:18Z)

@sucaiji and they deleted some days ago docs for windows with no explanation 

---

### 评论 #31 — cguentherTUChemnitz (2023-05-02T07:55:29Z)

> When do the rocm 5.5.0 release?

The answer is:
4 hours ago: https://github.com/RadeonOpenCompute/ROCm/releases/tag/rocm-5.5.0

---

### 评论 #32 — PiotrKlimczak (2023-05-02T07:59:01Z)

Let's wait for official community builds. I am pretty sure 7900 cards will work as they were in latest rc builds even if not explicitly mentioned in release notes. I mean why wouldn't they. Also they do mention some gfx11 changes which would be for 7900 cards too. 

---

### 评论 #33 — Lukanite (2023-05-02T16:27:58Z)

8.3it/s on 512x512 SD 1.5, native install on Ubuntu 22.04 with a 7900 XTX. An improvement over 5.4.3 for sure, but I feel like there's still a lot of untapped potential to go.

---

### 评论 #34 — aoolmay (2023-05-02T17:31:25Z)

@GeneralAwareness That's laughable indeed. This kind of messaging from community had me wasted 100s of hours when i was begining my journey years ago. This is just short of encouraging prematurely buying cards that are not fit for purpose and being forced to run some degraded performance software.

---

### 评论 #35 — saadrahim (2023-05-02T18:01:29Z)

ROCm 5.5.0 was released yesterday. I am closing this thread as a result. 

These forums have not been actively moderated in the past. Please watch your language. We are trying to keep a welcoming environment for everyone. I do not want to have to take any action against participants but may do so in the future.

As you may be aware, AMD has source code for Windows available in the many public repositories that constitute ROCm. However, full ROCm functionality has not been announced on Windows yet. Please await a public announcement with the understanding that no timeline is available now.  Only the HIP runtime is bundled with the drivers on Windows at present.

In addition, the milestones publicly shared in this repository are not final. Features may be transferred to a different milestone at any time.


---

### 评论 #36 — PennyFranklin (2023-05-03T14:39:24Z)

> ROCm 5.5.0 was released yesterday. I am closing this thread as a result. 
> 
> These forums have not been actively moderated in the past. Please watch your language. We are trying to keep a welcoming environment for everyone. I do not want to have to take any action against participants but may do so in the future.
> 
> As you may be aware, AMD has source code for Windows available in the many public repositories that constitute ROCm. However, full ROCm functionality has not been announced on Windows yet. Please await a public announcement with the understanding that no timeline is available now.  Only the HIP runtime is bundled with the drivers on Windows at present.
> 
> In addition, the milestones publicly shared in this repository are not final. Features may be transferred to a different milestone at any time.
> 

but I tried and couldn't  update rocm in the ubuntu22.04.2 by 'sudo  apt upgrade' code or 'sudo apt install rocm-dev' code 

---

### 评论 #37 — PennyFranklin (2023-05-03T16:25:05Z)

and I'm not sure whether should I change my current drive to amdgpu-pro drive to get this work 

---

### 评论 #38 — sirus20x6 (2023-05-03T20:18:07Z)

> > ROCm 5.5.0 was released yesterday. I am closing this thread as a result.
> > These forums have not been actively moderated in the past. Please watch your language. We are trying to keep a welcoming environment for everyone. I do not want to have to take any action against participants but may do so in the future.
> > As you may be aware, AMD has source code for Windows available in the many public repositories that constitute ROCm. However, full ROCm functionality has not been announced on Windows yet. Please await a public announcement with the understanding that no timeline is available now.  Only the HIP runtime is bundled with the drivers on Windows at present.
> > In addition, the milestones publicly shared in this repository are not final. Features may be transferred to a different milestone at any time.
> 
> but I tried and couldn't update rocm in the ubuntu22.04.2 by 'sudo apt upgrade' code or 'sudo apt install rocm-dev' code

Just because ROCM 5.5 is released doesn't mean that ubuntu is going to pick up the package and put it in apt any time soon. Your best bet is to try compiling from source, in other words this git repository.

---

### 评论 #39 — PennyFranklin (2023-05-04T00:39:23Z)

emmm，so how about open the terminal under the 'opt' file and key the code 'git clone....... (rocm)'? 

---

### 评论 #40 — xuhuisheng (2023-05-04T02:23:06Z)

@PennyFranklin 
You can follow the offical installation document.
<https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.5/page/Introduction_to_ROCm_Installation_Guide_for_Linux.html>

---

### 评论 #41 — PiotrKlimczak (2023-05-04T06:46:40Z)

Or just pull docker image https://hub.docker.com/r/rocm/composable_kernel/tags and copy it from there. 
Getting it working on Ubuntu 22 requires few lib hacks but it works. On Ubuntu 20 it just works since docker image is the same. 

---

### 评论 #42 — selroc (2023-05-04T06:59:09Z)

> > > ROCm 5.5.0 was released yesterday. I am closing this thread as a result.
> > > These forums have not been actively moderated in the past. Please watch your language. We are trying to keep a welcoming environment for everyone. I do not want to have to take any action against participants but may do so in the future.
> > > As you may be aware, AMD has source code for Windows available in the many public repositories that constitute ROCm. However, full ROCm functionality has not been announced on Windows yet. Please await a public announcement with the understanding that no timeline is available now.  Only the HIP runtime is bundled with the drivers on Windows at present.
> > > In addition, the milestones publicly shared in this repository are not final. Features may be transferred to a different milestone at any time.
> > 
> > 
> > but I tried and couldn't update rocm in the ubuntu22.04.2 by 'sudo apt upgrade' code or 'sudo apt install rocm-dev' code
> 
> Just because ROCM 5.5 is released doesn't mean that ubuntu is going to pick up the package and put it in apt any time soon. Your best bet is to try compiling from source, in other words this git repository.

This is not necessary to compile from source. You just have to change a line in /etc/apt/sources.list.d/rocm.list file, and you will pick the version you want.


---

### 评论 #43 — PennyFranklin (2023-05-04T09:54:26Z)

> @PennyFranklin 
> You can follow the offical installation document.
> <https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.5/page/Introduction_to_ROCm_Installation_Guide_for_Linux.html>

but I followed the documentation to install and turned into an  error in terminal as follow : 

penny@neko:~$ sudo apt update
[sudo] password for penny: 
E: Malformed entry 1 in list file /etc/apt/sources.list.d/rocm.list (URI parse)
E: The list of sources could not be read.
penny@neko:~$ 

code in the file like this : 

deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] <Release-2 specific rocm baseurl> jammy main
 
after that I can't do almost everything in ubuntu, even can't fix it by using dpkg in advanced opinion, in the end I had to reinstall the whole system,  for twice. 

---
