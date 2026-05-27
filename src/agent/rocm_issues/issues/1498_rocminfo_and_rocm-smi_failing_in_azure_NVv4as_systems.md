# rocminfo and rocm-smi failing in azure NVv4as systems 

> **Issue #1498**
> **状态**: closed
> **创建时间**: 2021-06-22T11:51:25Z
> **更新时间**: 2024-03-27T05:55:28Z
> **关闭时间**: 2021-06-23T09:15:28Z
> **作者**: Abhishek262
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1498

## 描述

Hey

I've installed ROCm pn the system, however running basic ROCm commands give me errors as shown below.

System details : 
Ubuntu 18.04 LTS
kernel : 5.4
Azure size : Standard NV4as_v4 (4 vcpus, 14 GiB memory)


azureuser@mi25:/proc$ rocminfo
ROCk module is NOT loaded, possibly no GPU devices
azureuser@mi25:/proc$ rocm-smi
ERROR:root:Driver not initialized (amdgpu not found in modules)

The Output of lshw is as shown below

![image](https://user-images.githubusercontent.com/21343683/122918760-17498900-d37d-11eb-9a95-cce9a94bfea7.png)

The Output of lspci is below

![image](https://user-images.githubusercontent.com/21343683/122918919-465ffa80-d37d-11eb-9f96-72ef56952f4b.png)

I'm not sure what's going wrong, I'm fairly sure I've followed the installation steps accurately and have tried reinstalling it as well.



---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-06-23T08:13:53Z)

Hi @Abhishek262 
Thanks for reaching out.
Let me check this for you.

---

### 评论 #2 — ROCmSupport (2021-06-23T09:15:28Z)

Hi @Abhishek262 
**ROCm is not officially supporting Azure environment right now.**
And more over, NVv4as systems support Windows OS right now, you can check this @ https://docs.microsoft.com/en-us/azure/virtual-machines/nvv4-series

Hope this helps.
Thank you.

---

### 评论 #3 — muhammad-asn (2024-03-27T05:46:10Z)

Will the RoCM support the Azure Standard_NG32ads_V620_v1  type (AMD V620)?

@ROCmSupport 

The VM specification
```
PRETTY_NAME="Ubuntu 22.04.4 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

Kernel version 
```
root@azure-vm:/home/azureadmin# uname -a
Linux azure-vm 5.15.0-1058-azure #66-Ubuntu SMP Fri Feb 16 00:40:24 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

---
