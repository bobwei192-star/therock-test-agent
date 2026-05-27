# How to install RDC client on the management console

> **Issue #1425**
> **状态**: closed
> **创建时间**: 2021-03-24T12:58:09Z
> **更新时间**: 2024-02-08T03:52:47Z
> **关闭时间**: 2024-02-08T03:52:47Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1425

## 描述

This isn't clear to me by reading the PDF guide. I can install the RDC daemon on the compute nodes, but I'm stuck there.


---

## 评论 (16 条)

### 评论 #1 — ROCmSupport (2021-03-24T13:02:22Z)

Hi @valeriob01 
Thanks for reaching out.
Can you please share the exact steps you followed and the pdf guide/doc you used.
Thank you.

---

### 评论 #2 — valeriob01 (2021-03-24T13:06:52Z)

> Hi @valeriob01
> Thanks for reaching out.
> Can you please share the exact steps you followed and the pdf guide/doc you used.
> Thank you.

I follow the steps in the latest version 4.1 , just `apt install rdc`


---

### 评论 #3 — valeriob01 (2021-03-24T13:10:24Z)

> > Hi @valeriob01
> > Thanks for reaching out.
> > Can you please share the exact steps you followed and the pdf guide/doc you used.
> > Thank you.
> 
> I follow the steps in the latest version 4.1 , just `apt install rdc`

BTW, the installation shows a warning:
`useradd: Warning: missing or non-executable shell '/bin/nologin'`

I have `/bin/false` which substitutes it on Ubuntu.

---

### 评论 #4 — ROCmSupport (2021-03-25T11:12:37Z)

Thanks @valeriob01 
I am able to reproduce this warning.
Other than that, I am able to install rdc well.

---

### 评论 #5 — valeriob01 (2021-03-25T11:27:19Z)

How do you install it? I cannot find rdc daemon after installation.


---

### 评论 #6 — valeriob01 (2021-03-25T11:29:10Z)

My original question was how to install rdc client on the management console, however this becomes second class question now, lets first install the daemon correctly.


---

### 评论 #7 — ROCmSupport (2021-03-25T12:03:47Z)

sudo apt install rdc --> installs rdc under /opt/rocm
/opt/rocm/rdc/bin will have both rdcd(daemon) and rdci(client interface).


---

### 评论 #8 — valeriob01 (2021-03-25T12:31:37Z)

> sudo apt install rdc --> installs rdc under /opt/rocm
> /opt/rocm/rdc/bin will have both rdcd(daemon) and rdci(client interfact).

Ok that's done, and generated the certs. In which directories shall I copy the certs?


---

### 评论 #9 — ROCmSupport (2021-03-25T12:41:41Z)

Request you to follow the rdc docs for all of the information.

---

### 评论 #10 — valeriob01 (2021-03-25T17:09:02Z)

> Request you to follow the rdc docs for all of the information.

Some modifications are necessary:

1. System: Ubuntu 20.04
2. Still need to build gRPC from source;
2. gRPC branch 1.28.1 is not found in the repository;
3. Compiled and installed gRPC;
4. `rdci stats` fails with error: `ERROR RdcLibraryLoader.cc(43): Fail to open librdc_client.so: libgrpc.so.9: cannot open shared object file: No such file or directory`



---

### 评论 #11 — ROCmSupport (2021-03-26T02:23:14Z)

Once you install rdc as apt install rdc, you will find /opt/rocm/rdc.
In that, you can see grpc also as a folder, so no need to compile/install explicitly.
If some library loading problem is there, recommend to export explicitly something like 
_export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm-4.1.0/rdc/lib/:/opt/rocm-4.1.0/rdc/grpc/lib/:/opt/rocm-4.1.0/rdc/grpc/lib64:/opt/rocm-4.1.0/rocm_smi/lib/_


---

### 评论 #12 — valeriob01 (2021-03-26T09:29:51Z)

> Once you install rdc as apt install rdc, you will find /opt/rocm/rdc.
> In that, you can see grpc also as a folder, so no need to compile/install explicitly.
> If some library loading problem is there, recommend to export explicitly something like
> _export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm-4.1.0/rdc/lib/:/opt/rocm-4.1.0/rdc/grpc/lib/:/opt/rocm-4.1.0/rdc/grpc/lib64:/opt/rocm-4.1.0/rocm_smi/lib/_

better but still:

`rdci stats --host localhost:50051 -s 2442 -g 1`
failed to connect to all addresses. Error code:14
rdci Error: RDC Client error


---

### 评论 #13 — ROCmSupport (2021-05-07T12:47:59Z)

Hi @valeriob01 
Can you please confirm whether issue is still observed and also more information is really helpful to understand the problem better.
Thank you.

---

### 评论 #14 — valeriob01 (2021-05-07T12:58:45Z)

Yes, still present. Sorry I gave up using rdc for the moment and am using a different software to monitor gpus, however the error code should be clear to you as you programmed it :-)


---

### 评论 #15 — abhimeda (2024-01-22T22:42:57Z)

@valeriob01 is this issue still persisting on the latest version of ROCm? If not can we close this ticket?

---

### 评论 #16 — nartmada (2024-02-08T03:52:47Z)

Closing this ticket as no response from @valeriob01.  Please re-open if you still observe the issue.  Thanks.

---
