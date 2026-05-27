# MI250X (gfx90a) not available as cuda device on pytorch

> **Issue #1916**
> **状态**: closed
> **创建时间**: 2023-03-03T23:00:30Z
> **更新时间**: 2024-10-12T00:55:50Z
> **关闭时间**: 2024-07-09T19:41:49Z
> **作者**: nishshah0
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1916

## 描述

I have MI250X system
![image](https://user-images.githubusercontent.com/122632692/222849737-e039480b-3b6f-4e1b-8334-079d205eefab.png)
with rocm5.4 installed
![image](https://user-images.githubusercontent.com/122632692/222849933-d47b49d4-103d-4256-97ed-28c6b1dac4af.png)
I installed pytorch using following command
`pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/rocm**5.4**/`
notice 5.4 at the end. The installation completed successfully.

But when I use torch.cuda.is_available(), it return False
![image](https://user-images.githubusercontent.com/122632692/222850473-76f4c929-e15c-49bc-bd07-f2cfd6a2e5e6.png)

what am I missing?

---

## 评论 (5 条)

### 评论 #1 — TheCowboyHermit (2023-03-09T08:40:59Z)

I have the same problem on my 7900 XTX as well.

I think pip kept trying to install "torch-1.13.1-cp310-cp310-manylinux1_x86_64.whl" rather than something like "https://download.pytorch.org/whl/nightly/rocm5.4.2/torch-2.1.0.dev20230308%2Brocm5.4.2-cp310-cp310-linux_x86_64.whl"

It basically attempting to install non-rocm version of the package.

Upon downloading the package manually like [torch-2.1.0.dev20230308+rocm5.4.2-cp310-cp310-linux_x86_64.whl](https://download.pytorch.org/whl/nightly/rocm5.4.2/torch-2.1.0.dev20230308%2Brocm5.4.2-cp310-cp310-linux_x86_64.whl) and then running: `pip install torch-2.1.0.dev20230308+rocm5.4.2-cp310-cp310-linux_x86_64.whl` and then re-run the test:

```py
import torch
torch.cuda.is_available()
```

On my 7900 XTX, it works by returning true, so basically we were given a very bad instruction, because pip looks for the "general" version first rather than the version we're looking for in ROCM.

Side note, you'll need to download and install other packages listed [Here](https://download.pytorch.org/whl/nightly/)

---

### 评论 #2 — ppanchad-amd (2024-05-10T15:24:05Z)

@nishshah0 Do you still need assistance with this issue? If not, please close the ticket. Thanks!

---

### 评论 #3 — harkgill-amd (2024-07-09T19:41:49Z)

Hi @nishshah0, if you are still experiencing this issue after following the steps here, [Installing PyTorch on ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/3rd-party/pytorch-install.html), please re-open this ticket. Thanks!

---

### 评论 #4 — unclemusclez (2024-10-02T14:50:09Z)

Yes this problem still exists. I first noticed this with openwebui, i have two different AMD cards on two different Linux systems that are running two different version of PyTorch that work fine with diffusion. ~~it seems to be local to Whisper.~~ 

i thought i was in the whisper github.. this issues shows itself on both of my systems. Whisper checks for CUDA and fails, so it reverts to CPU. 

I am currently using pytorch 2.4.1 on WSL Linux 22.04 for my gfx1100 and pytorch 2.2.1, 2.4.1, and nightly builds 2.6.0.dev for the gfx906. i thought i was installing the wrong version of things, but it seems that this is an AMD issue. 

I Thought ` torch.cuda.is_available() = False` is expected with ROCm ... ~~i happen to be using both the identified problematic cards in this ticket, the gfx1100 and gfx906, for my two systems.~~ so it seems like its a wide range of GFX cards. 

---

### 评论 #5 — unclemusclez (2024-10-12T00:55:29Z)

always try `sudo usermod -a -G render,video $USER:$GROUP` for each user using the audio. it fixed my issue above

---
