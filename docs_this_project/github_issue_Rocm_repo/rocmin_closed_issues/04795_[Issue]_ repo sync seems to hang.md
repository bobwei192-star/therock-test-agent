# [Issue]: repo sync seems to hang

- **Issue #:** 4795
- **State:** closed
- **Created:** 2025-05-23T12:15:51Z
- **Updated:** 2025-05-24T16:03:47Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/4795

### Problem Description

Hi,

I try to get a checkout, but something seems to be wrong. After 4 hours I am still at 0%

OS:
NAME="Debian GNU/Linux"
VERSION="13 (trixie)"

» echo $ROCM_VERSION
6.4.1

### Operating System

Debian/SID

### CPU

AMD Ryzen Threadripper 2970WX

### GPU

7900 XTX

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

```
» ../repo --time --trace --color=always sync -j 1
: git --version
: /usr/bin/python3 /home/yolo/machine-learning/rocm/ROCm/.repo/repo/main.py --repo-dir=/home-nvme/oberon/machine-learning/rocm/ROCm/.repo --wrapper-version=2.54 --wrapper-path=/home/yolo/machine-learning/rocm/repo -- --time --trace --color=always sync -j 1
Fetching:  0% (0/65) 0:00 | ..working..Host key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU
+--[ED25519 256]--+
|                 |
|     .           |
|      o          |
|     o o o  .    |
|     .B S oo     |
|     =+^ =...    |
|    oo#o@.o.     |
|    E+.&.=o      |
|    ooo.X=.      |
+----[SHA256]-----+
Fetching:  0% (0/65) 4:35:32 | 1 job | 4:35:31 AMDMIGraphX @ AMDMIGraphX
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_