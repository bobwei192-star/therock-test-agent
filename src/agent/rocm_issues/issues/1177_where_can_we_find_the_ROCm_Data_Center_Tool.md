# where can we find the ROCm Data Center Tool ?

> **Issue #1177**
> **状态**: closed
> **创建时间**: 2020-07-10T03:19:22Z
> **更新时间**: 2020-12-16T11:51:56Z
> **关闭时间**: 2020-12-16T11:51:56Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1177

## 描述

Last commit removed the guide......

---

## 评论 (10 条)

### 评论 #1 — selroc (2020-07-30T04:47:52Z)

20 days passed and no response. Why AMD publish things if they want to keep them secret?


---

### 评论 #2 — rahulmula (2020-07-30T06:02:11Z)

RDC(ROCm data center)Tool is available in the ROCm package from ROCM3.6

You can install using below instructions:

#Install grpc:

Note: CMake 3.15 or greater is required to build grpc.
$ sudo apt-get install -y automake make g++ unzip libcap-dev doxygen
$ sudo apt-get install -y build-essential autoconf libtool pkg-config
$ sudo apt-get install -y libgflags-dev libgtest-dev
$ sudo apt-get install -y clang-5.0 libc++-dev curl
$  git clone -b v1.28.1 https://github.com/grpc/grpc
$ cd grpc
$ git submodule update --init
$ mkdir -p cmake/build
$ cd cmake/build
By default (without using the CMAKE_INSTALL_PREFIX option), the following will install
to /usr/local lib, include and bin directories
$ cmake -DgRPC_INSTALL=ON -DBUILD_SHARED_LIBS=ON <-DCMAKE_INSTALL_PREFIX=<install dir>> ../..
$ make
$ sudo make install
$ sudo ldconfig

#Install RDC

If ROCm3.6 or more is installed try below command:
sudo apt-get install rdc

for authentication, setup below certificates:
To generate the keys and certificates using scripts, make the following calls:
cd /opt/rocm-<version>/rdc/authentication/

$ 01gen_root_cert.sh
provide answers to posed questions

$ 02gen_ssl_artifacts.sh
provide answers to posed questions

At this point, the keys and certificates are in the newly-created "CA/artifacts" directory. This directory must be deleted if you need to rerun the scripts.

To install the keys and certificates, cd into the artifacts directory and run the install.sh script as root, specifying the install location. By default, RDC expects this to be in /etc/rdc:

$ cd CA/artifacts
$ sudo install_<client|server>.sh /etc/rdc

/etc/rdc must be copied to all client and server machines that are expected to communicate with one another.



---

### 评论 #3 — selroc (2020-07-30T06:08:56Z)

Thank you very much, can we have the PDF guide too?


---

### 评论 #4 — selroc (2020-07-30T06:09:47Z)

btw, when ROCm 3.6 will be out?


---

### 评论 #5 — rahulmula (2020-07-30T06:22:48Z)

i dont have any pdf, you will see install instructions in readme soon. Rocm3.6 is already out

---

### 评论 #6 — selroc (2020-07-30T06:35:11Z)

> i dont have any pdf, you will see install instructions in readme soon. Rocm3.6 is already out

Repository for 3.6 not found.
http://repo.radeon.com/rocm/apt/



---

### 评论 #7 — rahulmula (2020-07-30T07:52:35Z)

> > i dont have any pdf, you will see install instructions in readme soon. Rocm3.6 is already out
> 
> Repository for 3.6 not found.
> http://repo.radeon.com/rocm/apt/

rocm3.6 is not a public release, for rdc to available need to wait till 3.7 (may be u can expect 3.7 in Aug 2nd week)

---

### 评论 #8 — selroc (2020-08-01T17:48:26Z)

Which network port RDC uses to communicate ?


---

### 评论 #9 — valeriob01 (2020-08-21T01:56:47Z)

Reiterating the question: Which network port RDC uses to communicate ?

---

### 评论 #10 — ROCmSupport (2020-12-16T11:51:56Z)

Hi All,
RDC released from 3.7 and please check the docs for all of the information.
Thank you.

---
