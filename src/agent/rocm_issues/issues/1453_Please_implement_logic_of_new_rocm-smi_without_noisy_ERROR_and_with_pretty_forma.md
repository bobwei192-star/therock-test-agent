# Please implement logic of new rocm-smi without noisy "ERROR" and with pretty formatted messages.

> **Issue #1453**
> **状态**: closed
> **创建时间**: 2021-04-14T09:18:37Z
> **更新时间**: 2023-01-23T05:41:30Z
> **关闭时间**: 2023-01-23T05:41:30Z
> **作者**: perestoronin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1453

## 描述

```
/opt/rocm/bin/rocm-smi -a | wgetpaste
ERROR: GPU[0] 		: fclk clock is unsupported
ERROR: GPU[0] 		: fclk frequency is unsupported
ERROR: 2 GPU[0]: % memory use: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.	
ERROR: 9 GPU[0]: od volt: The called function has not been implemented in this system for this device type	
ERROR: 2 GPU[0]: ras: RSMI_STATUS_NOT_SUPPORTED: This function is not supported in the current environment.	
ERROR: 9 GPU[0]: od volt: The called function has not been implemented in this system for this device type	
ERROR: 9 GPU[0]: od volt: The called function has not been implemented in this system for this device type	
ERROR: 9 GPU[0]: od volt: The called function has not been implemented in this system for this device type	
ERROR: 9 GPU[0]: od volt: The called function has not been implemented in this system for this device type	
WARNING:  		 One or more commands failed
```
Please implement logic of rocm-smi without noisy "ERROR" and with pretty formatted messages.

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-04-19T09:11:50Z)

Thanks @perestoronin for reaching us out.
I will assign to developer and getback with an update asap.
Thank you.

---
