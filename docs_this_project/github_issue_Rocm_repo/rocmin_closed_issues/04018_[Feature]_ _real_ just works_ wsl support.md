# [Feature]: "real" just works™ wsl support

- **Issue #:** 4018
- **State:** closed
- **Created:** 2024-11-08T05:53:46Z
- **Updated:** 2024-11-08T20:00:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/4018

### Suggestion Description

I've followed [this guide](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html), to install rocm in wsl. I've validated the install via "rocminfo" and the pytorch example.

I then installed ollama, unfortunately it didn't detect/ use the GPU via rocm. I then read the source to find out how [AMD GPU detection in ollama](https://github.com/ollama/ollama/blob/main/discover%2Famd_linux.go) works. I contemplated if I should raise an issue against ollama to make sure it also works under wsl, however I know this code works flawlessly on a bare-metal Linux installation so I don't really think ollama is at fault here.

After that I tried to install [invoke](https://github.com/invoke-ai/InvokeAI). The default installation didn't detect the GPU again so I used the workaround for pytorch from the docs to replace the relevant file in which then detected the GPU but also crashed due to some error.

In short this is really bad UX. I should follow the install guide and then just be able to run any rocm compatible application no tinkering required.

**Why don't you just install the "native" Windows version?**
I would like to administer these services remotely and administering Linux via ssh is way easier. I would also like to run some additional services which only have a Linux version.

**So why don't you just use a bare metal Linux install?**
I would, however this machine is also used as a shared console like gaming PC, so for broad game compatibility it has to run windows.

### Operating System

Windows 11 + WSL Ubuntu 22.04

### GPU

RX 7900xt

### ROCm Component

_No response_