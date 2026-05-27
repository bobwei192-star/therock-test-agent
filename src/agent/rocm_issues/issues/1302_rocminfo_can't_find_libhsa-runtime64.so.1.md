# rocminfo can't find libhsa-runtime64.so.1

> **Issue #1302**
> **状态**: closed
> **创建时间**: 2020-11-23T17:58:14Z
> **更新时间**: 2021-05-03T13:59:13Z
> **关闭时间**: 2020-11-25T10:07:26Z
> **作者**: AveNoF
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1302

## 描述

$rocminfo
>rocminfo: error while loading shared libraries: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory


$/opt/rocm/opencl/bin/clinfo
dlerror: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory
dlerror: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory
ERROR: clGetPlatformIDs(-1001)

$/opt/rocm/bin/rocminfo
/opt/rocm/bin/rocminfo: error while loading shared libraries: libhsa-runtime64.so.1: cannot open shared object file: No such file or directory

lib-hsa-runtime64.so.1 is already exist /opt/rocm/hsa-amd-aqlprofile/ but can't use.

---

## 评论 (11 条)

### 评论 #1 — baryluk (2020-11-23T22:07:39Z)

This is probably a duplicate of this issue:

https://github.com/RadeonOpenCompute/ROCm/issues/1129

Please provide info about your distro, distro version, kernel version, which ROCm version you installed, what is your CPU, GPU, and do you use upstream kernel amdgpu, or the one from ROCm (`rock-dkms` `rocm-dkms`).

`dpkg -l | egrep -i "roc[mkr]|hip|clinfo|opencl"` output would be useful.



---

### 评论 #2 — ROCmSupport (2020-11-24T07:13:07Z)

Hi @AveNoF 
Thanks for reaching out.
Can you please help us with steps you followed to reproduce the problem along with the answers for @baryluk's comment.

---

### 评论 #3 — AveNoF (2020-11-24T08:40:33Z)

Kernel and distro is 5.4.0-54-generic Ubuntu-18.04.1 

and CPU:Ryzen5 1400

GPU:RX580 and RX470(2GPUs)

ROCmVer is 3.9.0.30900-17

and I installed rocm from rocm-dkms,rocm-dev

~$ dpkg -l | egrep -i "roc[mkr]|hip|clinfo|opencl"

ii  clinfo                                                      2.2.18.03.26-1                                   amd64        Query OpenCL system information
ii  comgr                                                       1.9.0.194-rocm-rel-3.9-17-0fa438b                amd64        Library to provide support functions
ii  hip-base                                                    3.9.20412-6d111f85                               amd64        HIP: Heterogenous-computing Interface for Portability [BASE]
ii  hip-doc                                                     3.9.20412-6d111f85                               amd64        HIP: Heterogenous-computing Interface for Portability [DOCUMENTATION]
ii  hip-rocclr                                                  3.9.20412-6d111f85                               amd64        HIP: Heterogenous-computing Interface for Portability [ROCClr]
ii  hip-samples                                                 3.9.20412-6d111f85                               amd64        HIP: Heterogenous-computing Interface for Portability [SAMPLES]
ii  hsa-rocr-dev                                                1.2.30900.0-rocm-rel-3.9-17-75f9b74a             amd64        AMD Heterogeneous System Architecture HSA - Linux HSA Runtime for Boltzmann (ROCm) platforms
ii  libresid-builder0c2a                                        2.1.1-15ubuntu1                                  amd64        SID chip emulation class based on resid
ii  miopengemm                                                  1.1.6.647-rocm-rel-3.8-30-b51a125                amd64        A tool for generating OpenCL matrix multiplication (GEMM) kernels
ii  ocl-icd-libopencl1:amd64                                    2.2.11-1ubuntu1                                  amd64        Generic OpenCL ICD Loader
ii  ocl-icd-libopencl1:i386                                     2.2.11-1ubuntu1                                  i386         Generic OpenCL ICD Loader
ii  ocl-icd-opencl-dev:amd64                                    2.2.11-1ubuntu1                                  amd64        OpenCL development files
ii  opencl-c-headers                                            2.2~2018.02.21-gb5c3680-1                        all          OpenCL (Open Computing Language) C header files
ii  rccl                                                        2.10.0-112-g250d820-rocm-rel-3.5-30              amd64        Optimized primitives for collective multi-GPU communication
ii  rock-dkms                                                   1:3.9-17                                         all          amdgpu driver in DKMS format.
ii  rock-dkms-firmware                                          1:3.9-17                                         all          firmware blobs used by amdgpu driver in DKMS format
ii  rocm-clang-ocl                                              0.5.0.64-rocm-rel-3.9-17-50fb51a                 amd64        OpenCL compilation with clang compiler.
ii  rocm-cmake                                                  0.3.0.153-rocm-rel-3.9-17-1d1caa5                amd64        rocm-cmake built using CMake
ii  rocm-dbgapi                                                 0.36.0-rocm-rel-3.9-17                           amd64        Library to provide AMD GPU debugger API
ii  rocm-dev                                                    3.9.0.30900-17                                   amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-device-libs                                            1.0.0.637-rocm-rel-3.9-17-db8c0c3                amd64        Radeon Open Compute - device libraries
ii  rocm-dkms                                                   3.9.0.30900-17                                   amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-gdb                                                    9.2-rocm-rel-3.9-17                              amd64        ROCgdb
ii  rocm-opencl                                                 3.6Beta-14-g0c40e05-rocm-rel-3.9-17              amd64        OpenCL: Open Computing Language on ROCclr
ii  rocm-opencl-dev                                             3.6Beta-14-g0c40e05-rocm-rel-3.9-17              amd64        OpenCL: Open Computing Language on ROCclr
ii  rocm-smi                                                    1.0.0-206-rocm-rel-3.9-17-ge39c0e2               amd64        System Management Interface for ROCm
ii  rocm-smi-lib64                                              2.7.0.5-rocm-rel-3.9-17-8f9f943                  amd64        AMD System Management libraries
ii  rocm-utils                                                  3.9.0.30900-17                                   amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocminfo                                                    1.30900.0                                        amd64        Radeon Open Compute (ROCm) Runtime rocminfo tool
ii  whiptail                                                    0.52.20-1ubuntu1                                 amd64        Displays user-friendly dialog boxes from shell scripts






libhsa-runtime64.so.1 is already exist in /opt/rocm/hsa-amd-aqlprofile/lib
but rocminfo say it is missing.


---

### 评论 #4 — AveNoF (2020-11-24T08:48:13Z)

I don't know how this error reproduce.but when  i updated  rocm 3.8 to 3.9,this error has happened.
and Tensorflow-rocm had error too with this message here is out put.

pip3 install tensorflow-rocm==2.2.0

Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow

ImportError: libhipsparse.so.0: cannot open shared object file: No such file or directory


---

### 评论 #5 — ROCmSupport (2020-11-24T09:08:56Z)

Hi @AveNoF
Looks like un-installation of 3.8 did not go well in your machine.
As ROCm upgrade is NOT supported, recommend to do clean un-installation of old ROCm and install new ROCm.

Can you please try uninstall ROCm completely once again and make sure that all packages are removed before you install 3.9.
Recommend to check sudo dpkg -l | grep hsa . Replace hsa with hip, llvm, rocm, rock and make sure that all packages are removed. Recommend to do the same for all other additional packages also if you installed anything explicitly.

Once you make sure that its clean, now try to install ROCm 3.9.
I hope this helps.

---

### 评论 #6 — ROCmSupport (2020-11-24T09:10:06Z)

TF error is due to missing hipsparse library which is a different issue, we can handle it separately.
Meanwhile recommend to install rocm 3.9 well and then we can see all rest of issues later.

---

### 评论 #7 — AveNoF (2020-11-24T15:54:25Z)

for uninstall all old rocm software i typed  sudo apt-get purge hsa* hip* llvm* rocm*
when my ubuntu-desktop had broken and I reinstalled ubuntu.
How should i have uninstall all old packages?

and now another problem has happen.

that errors was same as https://github.com/RadeonOpenCompute/ROCm/issues/1161
and  https://github.com/RadeonOpenCompute/ROCm/issues/1164

and now there is a error of hip that similer to https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/1106
but little different from mine.
tensorflow-rocm

&python3
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> hello = tf.constant('Hello World!')
2020-11-25 00:30:46.848606: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libamdhip64.so
/src/external/hip-on-vdi/rocclr/hip_code_object.cpp:120: guarantee(false && "hipErrorNoBinaryForGpu: Coudn't find binary for current devices!")
中止 (コアダンプ)


I wonder why such a core dump has happen.

$ pip3 list
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
absl-py (0.11.0)
apturl (0.5.2)
asn1crypto (0.24.0)
astunparse (1.6.3)
Brlapi (0.6.6)
cachetools (4.1.1)
certifi (2020.11.8)
chardet (3.0.4)
command-not-found (0.3)
cryptography (2.1.4)
cupshelpers (1.0)
defer (1.0.6)
distro-info (0.18ubuntu0.18.04.1)
gast (0.3.3)
google-auth (1.23.0)
google-auth-oauthlib (0.4.2)
google-pasta (0.2.0)
grpcio (1.33.2)
Guake (3.0.5)
h5py (2.10.0)
httplib2 (0.9.2)
idna (2.10)
importlib-metadata (3.1.0)
Keras-Preprocessing (1.1.2)
keyring (10.6.0)
keyrings.alt (3.0)
language-selector (0.1)
launchpadlib (1.10.6)
lazr.restfulclient (0.13.5)
lazr.uri (1.0.3)
louis (3.5.0)
macaroonbakery (1.1.3)
Mako (1.0.7)
Markdown (3.3.3)
MarkupSafe (1.0)
netifaces (0.10.4)
numpy (1.18.5)
oauth (1.0.1)
oauthlib (3.1.0)
olefile (0.45.1)
opt-einsum (3.3.0)
pbr (3.1.1)
pexpect (4.2.1)
Pillow (5.1.0)
pip (9.0.1)
protobuf (3.14.0)
pyasn1 (0.4.8)
pyasn1-modules (0.2.8)
pycairo (1.16.2)
pycrypto (2.6.1)
pycups (1.9.73)
pygobject (3.26.1)
pymacaroons (0.13.0)
PyNaCl (1.1.2)
pyRFC3339 (1.0)
python-apt (1.6.5+ubuntu0.3)
python-dateutil (2.6.1)
python-debian (0.1.32)
pytz (2018.3)
pyxdg (0.25)
PyYAML (3.12)
reportlab (3.4.0)
requests (2.25.0)
requests-oauthlib (1.3.0)
requests-unixsocket (0.1.5)
rsa (4.6)
scipy (1.4.1)
SecretStorage (2.3.1)
setuptools (50.3.2)
simplejson (3.13.2)
six (1.15.0)
system-service (0.3)
systemd-python (234)
tensorboard (2.4.0)
tensorboard-plugin-wit (1.7.0)
tensorflow-estimator (2.3.0)
tensorflow-rocm (2.3.2)
termcolor (1.1.0)
ubuntu-drivers-common (0.0.0)
ufw (0.36)
unattended-upgrades (0.1)
urllib3 (1.26.2)
usb-creator (0.3.3)
wadllib (1.3.2)
Werkzeug (1.0.1)
wheel (0.35.1)
wrapt (1.12.1)
xkit (0.0.0)
zipp (3.4.0)
zope.interface (4.3.2)


---

### 评论 #8 — baryluk (2020-11-24T18:53:12Z)

@AveNoF 

> for uninstall all old rocm software i typed `sudo apt-get purge hsa* hip* llvm* rocm*`
> when my ubuntu-desktop had broken and I reinstalled ubuntu.


doing sudo purge with llvm* was a bad idea. llvm is probably required by your standard graphics drivers and other important system components. Don't do such things blindly. Is sometimes might or might not work.


My recommendation would be to remove it using `sudo apt purge -V comgr*`. Then once that is done (it will remove the majority of rocm stuff probably), see for the remaining packages in the output of: `dpkg -l | gawk '$2 ~ /\yroc[mkrt]|\yhip|\yhsa\y/ { print $2; }'`


---

### 评论 #9 — ROCmSupport (2020-11-25T07:34:05Z)

Hi @AveNoF 

Recommend to uninstall ROCm as per below steps.
1. sudo apt autoremove rocm-opencl
2. Now check sudo dpkg -l | grep hsa. Replace hsa with hip, llvm, rocm, rock.
Remove all visible ROCm packages as sudo apt pugre <pkg> and make sure that all packages are removed. 
Recommend to do the same for all other additional packages also if you installed anything explicitly.

Once you make sure that its clean, now try to install ROCm 3.9.
I hope this helps.

---

### 评论 #10 — ROCmSupport (2020-11-26T05:58:27Z)

Thanks @AveNoF for closing this. Hope this issue is resolved for you.
Thank you.

---

### 评论 #11 — SakiiCode (2021-05-03T13:59:13Z)

For future reference, I had the same problem after several dirty up/downgrades. Managed to fix it with
```
sudo apt remove comgr hsa-rocr-dev rocm-opencl
sudo apt install rocm-opencl
```

---
