# [Issue]: no sane way to build without docker

- **Issue #:** 4904
- **State:** closed
- **Created:** 2025-06-09T14:35:27Z
- **Updated:** 2025-06-11T02:18:25Z
- **Labels:** AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4904

### Problem Description

```
» make -f ../ROCm-6.4.1/ROCm/tools/rocm-build/ROCm.mk all
OUT_DIR=
ROCM_INSTALL_PATH=
sudo mkdir -p -m 775 "" && \
sudo chown -R "1000:1000" "/opt"     #<-- DAMN IT AMD WHAT IS WRONG HERE?
[sudo] password for <user>:
sudo: a password is required
make: *** [../ROCm-6.4.1/ROCm/tools/rocm-build/ROCm.mk:269: /logs] Error 1
```

Why would any step except `make install` require root permissions? This is seriously fucked up. I think I am going to buy an NVIDIA card for AI play. It was a mistake to buy an AMD device. This is something nobody somewhat sane would want to touch  with a ten-foot pole. How can you hope that anyone will use this? I really hope for your that you will get it straight some day, so there is a bit competition in the AI hardware space. But if the rest of your software is, as the first few minutes promise, your hardware could be the best, but you still would not get adopted widely.
I guess your developers hate it and nobody, who does not get get payed, is willing to invest time into this. Please hire someone who is willing to fix the build and support this guy as good as you can. 

### How To Reproduce

Just follow the official instructions. Note that the makefile does not support `PREFIX`, and there is not other documented way to change the output directory. 

