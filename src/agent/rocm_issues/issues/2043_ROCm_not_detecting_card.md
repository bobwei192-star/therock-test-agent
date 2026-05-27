# ROCm not detecting card

> **Issue #2043**
> **状态**: closed
> **创建时间**: 2023-04-13T23:39:20Z
> **更新时间**: 2023-04-14T19:43:56Z
> **关闭时间**: 2023-04-14T19:43:56Z
> **作者**: Dunedin87
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2043

## 描述

I was in the market to purchase a card, as I saw Pytorch offering install with rocm available, decided to get a 6950 XT. I re-installed pytorch with rocm with the following code.
`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2`
However
`torch.cuda.is_available()`
showed as False
I also ran, `sudo amdgpu-install --usecase=rocm`, but same result
I saw other people trying to troubleshoot run rocminfo, following was the output

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.33'not found (required by rocminfo)`

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34 not found (required by rocminfo)`

`rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version GLIBCXX_3.4.29 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version GLIBCXX_3.4.30 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version CXXABI_1.3.13 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.32 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

And this is where I first see probably cause of the problem?
I'm running Linux Mint 20, which is based on Ubuntu 20. Only way for me to upgrade to GLIB2.33 / 2.34 would be by upgrading to Linux Mint 21 (Ubuntu 22). Reading the AMD docs, it showed rocm5.4.2 is supported by Ubuntu 20

I'm not a computer scientists or an expert, is there an easy way to get rocm to run on Linux Mint 20? 


---

## 评论 (3 条)

### 评论 #1 — Spencer-Dawson (2023-04-14T07:00:07Z)

FYI I've stuck with ubuntu in part because it's officially supported(as is RHEL and SLES, but nothing else)

Some random things you could try.

1. Install build-essential or the mint equivalent because it includes a lot of C/C++ libraries beyond the system default.
2. I'm currently using `--usecase=hiplibsdk,hip,rocm,dkms` with my install flag instead of just -`-usecase=rocm`. You could try that, but I don't think it would help.
3. You could look at my installer script for ubuntu. It won't work for you as is, but if you can understand the flow it might help you understand the install process better https://gist.github.com/Spencer-Dawson/7fdb5dd09461b6cece8a99537f381e44

What version of glibc do you have anyway? `ldd --version` gives me `ldd (Ubuntu GLIBC 2.35-0ubuntu3.1) 2.35`

And what version of rocm do you have installed(I know you mention 5.4.2), but what does apt say `apt show rocm-libs -a` gives me `Version: 5.3.0.50300-63~22.04`

---

### 评论 #2 — Dunedin87 (2023-04-14T17:11:20Z)

Hey Spencer, thanks for looking into it. 

I have build-essential installed

`ldd --version` is `ldd (Ubuntu GLIBC 2.31-0ubuntu9.9) 2.31`

Thanks for providing the script, I went through it, essentially following the steps manually, since my system is Ubuntu 20.04, I following AMD's install guide
https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.2/page/How_to_Install_ROCm.html

`sudo apt-get update`

`wget https://repo.radeon.com/amdgpu-install/5.4.2/ubuntu/focal/amdgpu-install_5.4.50402-1_all.deb`
`sudo apt-get install ./amdgpu-install_5.4.50402-1_all.deb`

I did get the following error
`TN: Download is performed unsandboxed as root as file '/home/ds/Downloads/rocm/amdgpu-install_5.4.50402-1_all.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)`

I'm searching around the web on what that means and how to get past this for now.

Also, show rocm-libs has a suffix of 22.04, Since my system is 20.04, I think I need to somehow revert it to 20.04 system. My guess is that installing from the script at pytorch's site installed the 22.04 version and due to the error above, I'm not able to re-install with the 20.04 version.
`apt show rocm-libs -a` show
`Version: 5.4.3.50403-121~22.04`



---

### 评论 #3 — Dunedin87 (2023-04-14T19:43:36Z)

Update, it works now!

Here were the steps to resolve the issue:
The 13: Permission denied error above was bypassed by double clicking the .deb file instead of using `sudo apt-get install ./amdgpu...`
After which, I ran `sudo amdgpu-install --usecase=rocm` again.

`apt show rocm-libs -a` now shows
`Version: 5.4.2.50402-104~20.04`

Important thing is now it doesn't show 22.04, since my system is Ubuntu 20.04. My hunch is that the command on pytorch's site 
`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2` doesn't necessarily detect whether you need 20.04 or 22.04 version. 

Now torch.cuda.is_available() shows as True however it does give a warning
`/home/ds/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")`
But, loading data and model into device and doing a quick forward run seems to be working for now.

Thanks @Spencer-Dawson for your help and pushing me towards the right solution.


---
