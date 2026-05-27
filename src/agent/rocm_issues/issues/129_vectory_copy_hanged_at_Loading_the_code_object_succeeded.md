# vectory_copy hanged at Loading the code object succeeded

> **Issue #129**
> **状态**: closed
> **创建时间**: 2017-06-16T09:32:50Z
> **更新时间**: 2017-07-02T17:43:05Z
> **关闭时间**: 2017-07-02T17:43:05Z
> **作者**: zhaojunfan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/129

## 描述

Linux 16.04.02, AMD W9100 graphic card, ROCm 1.5.
I follow the README.md. try to install the ROCm on my PC.

. wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
2. sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
3. sudo apt-get update
4. sudo apt-get install rocm
5. sudo reboot now

Then I Verify installation.
To verify that the ROCm stack completed successfully you can execute to HSA
vectory_copy sample application (we do recommend that you copy it to a
separate folder and invoke make therein):

```shell
cd /opt/rocm/hsa/sample
make
./vector_copy

But I do not get all the test pass. Trying to run the vector_copy hsa sample hangs at Loading the code object succeeded. 
the output just like followings:

Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx701.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
....

Who can help me solve the problem?Thanks!!!

---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-06-16T10:20:58Z)

Are you on a PCIe Gen3 x16 slot that has  PCIe Atomic support

On Jun 16, 2017, at 4:32 AM, zhaojunfan <notifications@github.com<mailto:notifications@github.com>> wrote:


Linux 16.04.02, AMD W9100 graphic card, ROCm 1.5.
I follow the README.md. try to install the ROCm on my PC.

. wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
2. sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
3. sudo apt-get update
4. sudo apt-get install rocm
5. sudo reboot now

Then I Verify installation.
To verify that the ROCm stack completed successfully you can execute to HSA
vectory_copy sample application (we do recommend that you copy it to a
separate folder and invoke make therein):

cd /opt/rocm/hsa/sample
make
./vector_copy

But I do not get all the test pass. Trying to run the vector_copy hsa sample hangs at Loading the code object succeeded.
the output just like followings:

Initializing the hsa runtime succeeded.
Checking finalizer 1.0 extension support succeeded.
Generating function table for finalizer succeeded.
Getting a gpu agent succeeded.
Querying the agent name succeeded.
The agent name is gfx701.
Querying the agent maximum queue size succeeded.
The maximum queue size is 131072.
Creating the queue succeeded.
"Obtaining machine model" succeeded.
"Getting agent profile" succeeded.
Create the program succeeded.
Adding the brig module to the program succeeded.
Query the agents isa succeeded.
Finalizing the program succeeded.
Destroying the program succeeded.
Create the executable succeeded.
....

Who can help me solve the problem?Thanks!!!

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/129>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuWF98mRi9tXDA5b4uk-6TD4punhLks5sEkvDgaJpZM4N8PPg>.



---

### 评论 #2 — gstoner (2017-07-02T17:43:05Z)

 1.6 rolled out this week https://rocm.github.io/ROCmInstall.html  Note Hawaii support is still experimental. 

---
