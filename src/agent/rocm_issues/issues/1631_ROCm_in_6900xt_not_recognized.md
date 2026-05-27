# ROCm in 6900xt not recognized

> **Issue #1631**
> **状态**: closed
> **创建时间**: 2021-11-29T18:31:47Z
> **更新时间**: 2022-02-02T12:34:01Z
> **关闭时间**: 2021-11-30T06:32:50Z
> **作者**: EduMio
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1631

## 描述

Hello. I am trying to run my pytorch model with the ROCm with my 6900xt. I installed the ROCm 4.5 correctly, it works perfectly with tensorflow. So I moved on and downloaded with docker pull rocm/pytorch:latest, but it wont recognize my GPU. The command I am using is `sudo docker run -it -v $HOME:/data --privileged --rm --device=/dev/kfd --device=/dev/dri --group-add video rocm/pytorch:latest` it gives me the following error:
![image](https://user-images.githubusercontent.com/55565758/143923202-05496d18-7a5a-48cb-9bfe-34946c0bd3fb.png)


---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-11-30T06:32:50Z)

Hi @EduMio 
Thanks for reaching out.
Navi series of cards are not officially supported right now with ROCm 4.5 and so some things do not work definitely. We can not comment/work on this issue until its supported officially.
Please stay tuned for more updates through our documentation. Thank you.

---

### 评论 #2 — Djip007 (2021-12-12T14:37:02Z)

container rocm/pytorch:latest is build with rocm 4.3.1... not 4.5... may be wy can try to rebuild pytorch with rocm 4.5.x

---

### 评论 #3 — EduMio (2021-12-13T03:03:56Z)

I wish I could, but in the official page (
https://hub.docker.com/r/rocm/pytorch/tags) I did not find a 4.5.x version
of it. I tried with the rocm/pytorch:latest but to no avail. I guess we
just have to wait for the 4.5.x version.

On Sun, Dec 12, 2021 at 11:37 AM Djip007 ***@***.***> wrote:

> container rocm/pytorch:latest is build with rocm 4.3.1... not 4.5... may
> be try to rebuild pytorch with rocm 4.5.x
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1631#issuecomment-991909667>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANH53PUB4224WYD4XN3RXSLUQSXRTANCNFSM5I72CBYA>
> .
>


---

### 评论 #4 — Djip007 (2021-12-17T19:02:53Z)

yesterday: rocm4.5.2_ubuntu18.04_py3.8_pytorch_1.10.0
=> pytorch + rocm4.5.2... did'nt test... but good news no?

---

### 评论 #5 — EduMio (2021-12-17T20:27:31Z)

That is good news for sure, I am going to test that on my VM and see how it
goes. Thank you for sharing the info!

On Fri, Dec 17, 2021 at 4:03 PM Djip007 ***@***.***> wrote:

> yesterday: rocm4.5.2_ubuntu18.04_py3.8_pytorch_1.10.0
> => pytorch + rocm4.5.2... did'nt test... but good news no?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1631#issuecomment-996965290>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANH53PSRY2K5O7JR35OFYHDUROCORANCNFSM5I72CBYA>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


---

### 评论 #6 — Djip007 (2022-02-01T16:14:06Z)

Au cas ou (et pas du tout testé...) je suis tombé la dessus:
https://download.pytorch.org/whl/nightly/rocm4.5.2/torch_nightly.html

ca voudrait dire que il y a plus que les versions qui sont mis sur la page d'accueil de pytorch.. https://pytorch.org/get-started/locally/


---

### 评论 #7 — EduMio (2022-02-02T12:34:01Z)

Thank you very much! I am going to try it in some weeks and might post some
testing feedbacks in my machine


On Tue, Feb 1, 2022 at 1:14 PM Djip007 ***@***.***> wrote:

> Au cas ou (et pas du tout testé...) je suis tombé la dessus:
> https://download.pytorch.org/whl/nightly/rocm4.5.2/torch_nightly.html
>
> ca voudrait dire que il y a plus que les versions qui sont mis sur la page
> d'accueil de pytorch.. https://pytorch.org/get-started/locally/
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1631#issuecomment-1027017985>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANH53PVVNRHKQN2AL5GGPADUZABFRANCNFSM5I72CBYA>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


---
