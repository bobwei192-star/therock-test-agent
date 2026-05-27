# Pytorch and AMD GPU

> **Issue #1570**
> **状态**: closed
> **创建时间**: 2021-09-10T14:25:06Z
> **更新时间**: 2021-09-13T05:24:00Z
> **关闭时间**: 2021-09-13T05:24:00Z
> **作者**: Flock1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1570

## 描述

Hi,

I am using RX 6700 on my Ubuntu machine and have installed ROCm as well. When I install Pytorch for ROCma nd import it, I get the following:
```
"hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"
Aborted (core dumped)
```
Why am I getting this?

---

## 评论 (42 条)

### 评论 #1 — aoolmay (2021-09-10T14:53:31Z)

There is no support yet, there's a lot of promises with ever further timeline for it though.

What you can do in the meantime is use PlaidML over OpenCL provided by ROCm. It's using old Keras which is not great and lacking features, but it might get you by for a while.

---

### 评论 #2 — Flock1 (2021-09-10T17:18:14Z)

Hi,

Thanks for the reply. I tried PlaidML but when I enter the setup, I only see my CPU. The GPU isn't showing up


---

### 评论 #3 — aoolmay (2021-09-10T17:27:31Z)

It only shows up if you accept 'experimental device support' prompt.
If it doesn't show, check you clinfo and rocminfo, something might go wrong on ROCm install.

---

### 评论 #4 — Flock1 (2021-09-10T17:32:28Z)

When I run `clinfo`, I get `gfx1031` as the name of the device. I din't get any error when I run `clinfo` or `rocminfo`



---

### 评论 #5 — aoolmay (2021-09-10T17:35:59Z)

You must've missed the experimental device support prompt, it defaults to no and because of that didn't show OpenCL enabled GPU.

---

### 评论 #6 — Flock1 (2021-09-10T17:36:46Z)

No. it didn't show up. Only the CPU showed up. 

---

### 评论 #7 — aoolmay (2021-09-10T17:44:24Z)

Maybe it's something to do with current ROCm version? I'm still on 4.2 and it works on different machines with different AMD GPUs with no problems.

---

### 评论 #8 — Flock1 (2021-09-10T17:46:52Z)

I am using 4.3

---

### 评论 #9 — aoolmay (2021-09-10T17:50:50Z)

Now that i think about i might have the 4.3 installed on one of machines and gave me some problems with Plaid.
You can do that by changing default repository in "software&updates->other software" to "https://repo.radeon.com/rocm/apt/4.2/". Remember to uninstall 4.3 version first.

---

### 评论 #10 — Flock1 (2021-09-10T17:57:40Z)

So [here](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu), how do I ensure I install 4.2 instead of 4.3?

---

### 评论 #11 — aoolmay (2021-09-10T18:05:27Z)

Ok, step by step.
1. Uninstall 4.3 with "sudo apt autoremove rocm-opencl rocm-dkms rocm-dev rocm-utils && sudo reboot"
2. After the reboot you have to go into "software&updates" system application, in the tab "other software" you will find the default address for rocm repository "https://repo.radeon.com/rocm/apt/debian/", change it to "https://repo.radeon.com/rocm/apt/4.2/"
3. Update your package manager with new repository with "sudo apt update"
4. Install ROCm version 4.2 with "sudo apt install rocm-dkms && sudo reboot"
5. If version 4.2 works properly you will find your GPU in the plaid-setup.

---

### 评论 #12 — Flock1 (2021-09-10T18:28:01Z)

Thank you very much. Let me try that. 

---

### 评论 #13 — Flock1 (2021-09-10T18:39:29Z)

I'm not able to install 4.2. Getting this error:
```
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

---

### 评论 #14 — aoolmay (2021-09-10T18:48:10Z)

Sorry about leading you to a problem. Try "sudo dpkg --configure -a", if this won't work i'd just reinstall Ubuntu, it takes just as much time as troubleshooting.

---

### 评论 #15 — Flock1 (2021-09-10T18:48:11Z)

Also, after `sudo apt update` in step 3, I get the following:
`N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'https://repo.radeon.com/rocm/apt/4.2 ubuntu InRelease' doesn't support architecture 'i386'
`

---

### 评论 #16 — aoolmay (2021-09-10T18:48:53Z)

These are fine, it's just warnings with no consequence.

---

### 评论 #17 — Flock1 (2021-09-10T18:51:39Z)

Step 4 gives me this:
```
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

---

### 评论 #18 — aoolmay (2021-09-10T18:53:38Z)

Did you change repository path before, when i first sugested installing 4.2?

---

### 评论 #19 — Flock1 (2021-09-10T18:54:42Z)

No. When you provided me with the steps, that's when I changed it

---

### 评论 #20 — aoolmay (2021-09-10T18:56:55Z)

Then again, it's a package manager problem and time consuming to diagnose and fix, epsecially if you're not familiar with Ubuntu. Can you afford time to just reinstall Ubuntu?

---

### 评论 #21 — Flock1 (2021-09-10T18:59:15Z)

Yeah. I can reinstall it. But what's the solution though? Can you give me some idea? I have worked with Ubuntu for some time now. 

---

### 评论 #22 — aoolmay (2021-09-10T19:04:25Z)

Yes, follow standard installation procedure https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
After step 2 "Add the ROCm apt repository" change default address for rocm repository "https://repo.radeon.com/rocm/apt/debian/" to "https://repo.radeon.com/rocm/apt/4.2/".
Update "sudo apt update" and proceed with installation as normal.
Install PlaidML and you should see your GPU in the list.

---

### 评论 #23 — Flock1 (2021-09-10T19:33:29Z)

is 4.2 compatible with RX 6700? I want to be sure before I reinstall the OS

---

### 评论 #24 — aoolmay (2021-09-10T19:37:56Z)

I'm using ROCm 4.2 with PlaidML on machines with WX5100, WX7100 and RX6800. Make sure to use the officially supported kernel version, i vaguely remember that caused some problems.

---

### 评论 #25 — Flock1 (2021-09-10T19:38:58Z)

Ah. Let me reinstall the OS then. 

---

### 评论 #26 — Flock1 (2021-09-10T20:03:05Z)

So now that I'm doing a fresh installation, how do I proceed? I don't see the option in "software and updates"

---

### 评论 #27 — aoolmay (2021-09-10T20:07:40Z)

I'm using Xubuntu, i don't exactly know what your flavor of Ubuntu allows, quick search suggest you may have a thing called "software updater" in the vanilla?
![2021-09-10_22-07](https://user-images.githubusercontent.com/87392079/132911586-75053559-3f50-4cd3-bf2f-52f66077d1ba.png)


---

### 评论 #28 — Flock1 (2021-09-10T20:16:47Z)

So here's what I did:
1) Installed new OS
2) Followed the initial steps on the website
3) Instead of using the mentioned key, I got the key for 4.2
4) Then, I opened the software and update and I changed the link as you mentioned. 
5) Then, I installed using the apt command to install rocm. 

I still got the error. 

---

### 评论 #29 — aoolmay (2021-09-10T20:24:45Z)

https://github.com/RadeonOpenCompute/ROCm/tree/roc-4.2.x#Supported-Operating-Systems
Kernel and Ubuntu version is correct?
I'm puzzled, this solution works for me and i reinstalled one of the system just two weeks ago.

---

### 评论 #30 — Flock1 (2021-09-10T20:25:47Z)

It installs fine when I install 4.3. Something is wrong with 4.2

---

### 评论 #31 — aoolmay (2021-09-10T20:28:16Z)

I'm not aware if there were any changes to 4.2. I remember using PlaidML with 4.0 before, you could try 4.0 or 4.1.

---

### 评论 #32 — Flock1 (2021-09-10T20:44:28Z)

Let's see

---

### 评论 #33 — Flock1 (2021-09-10T21:01:39Z)

I am following this to install the ROCm. This works for me
https://www.youtube.com/watch?v=efKjfBkjPlM

---

### 评论 #34 — aoolmay (2021-09-10T21:10:25Z)

This guy shows steps you should be doing from ROCm installation manual and this is always for current version, which now is 4.3.
The problem you're having is that 4.3 doesn't work with PlaidML and 4.2 and earlier do. You have to figure out how to succesfully install 4.2 or earlier.
For me simply changing the repository directory always worked. I can't help you further, out of time.

---

### 评论 #35 — Flock1 (2021-09-10T21:31:43Z)

So in the above video, can you tell me what should I use version 4.2 so that it installs? 

---

### 评论 #36 — briansp2020 (2021-09-10T23:17:43Z)

You can follow the installation guide at https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html

To pick a specific version, instead of 
>echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list

Use specific version you want

>echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/4.2/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list

Other than that, all the instructions should be the same. I don't have Ubuntu on my PC any more. So, I can't try it to verify it myself.



---

### 评论 #37 — Flock1 (2021-09-11T00:35:56Z)

I tried that. I get this error

> Step 4 gives me this:
> 
> ```
> Errors were encountered while processing:
>  rock-dkms
>  rocm-dkms
> E: Sub-process /usr/bin/dpkg returned an error code (1)
> ```



---

### 评论 #38 — Flock1 (2021-09-11T01:26:37Z)

So guys, an update. I did fresh installation and I was bale to set AMD GPU in plaid setup. 

---

### 评论 #39 — Flock1 (2021-09-11T02:07:02Z)

When I ran `plaidbench keras mobilenet`, I got this:
```
plaidbench keras mobilenet
Running 1024 examples with mobilenet, batch size 1, on backend plaid
INFO:plaidml:Opening device "opencl_amd_gfx1031.0"
Compiling network... Warming up... Running...
Example finished, elapsed: 5.100s (compile), 2.723s (execution)

-----------------------------------------------------------------------------------------
Network Name         Inference Latency         Time / FPS          
-----------------------------------------------------------------------------------------
mobilenet            2.66 ms                   1.21 ms / 829.15 fps
Correctness: PASS, max_error: 7.314303729799576e-06, max_abs_error: 6.407499313354492e-07, fail_ratio: 0.0
```
So is my GPU working?

---

### 评论 #40 — aoolmay (2021-09-11T07:04:17Z)

Yes, good job. Can you confirm which ROCm version works with PlaidML for you?

---

### 评论 #41 — Flock1 (2021-09-11T13:07:16Z)

I think I found a solution. I needed to set `LD_LIBRARY_PATH` variable to `/opt/rocm-<versoin>/bin`

So I am using ROCm  4.3 with PlaidML 0.7

---

### 评论 #42 — ROCmSupport (2021-09-13T05:24:00Z)

Hi @Flock1 
Thanks for reaching out.
RX 6700 is not an officially supported card. Please look at supported hardware section @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Thank you.

---
