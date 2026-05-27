# Unable to Install ROCm correctly

> **Issue #1118**
> **状态**: closed
> **创建时间**: 2020-05-26T05:42:49Z
> **更新时间**: 2020-05-29T11:05:57Z
> **关闭时间**: 2020-05-29T11:05:57Z
> **作者**: Rutvik-Trivedi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1118

## 描述

I want to set up my GPU for PyTorch in Ubuntu 20.04. I am completely new to the setting up stuff and have no experience with GPUs altogether, and faced a lot of problems while trying to configure based on the documentation given. I tried out the installation guide and I don't know what the problem is. I would request some help on setting up my system if it is supported for this at this point of time. This is the message I am getting which I have no idea what the error is. I tried searching for and got a lot of different solutions. I tried all without success. I think I am having a different problem altogether:

```
$ sudo /opt/rocm/bin/rocminfo
ROCk module is loaded
<USER> is member of video group
hsa api call failure at: /data/jenkins-workspace/compute-rocm-rel-3.3/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

```
If I run ```dmesg | grep amdgpu```, the following messages pop out:
```
$ dmesg | grep -i amdgpu
[   20.684577] [drm] amdgpu kernel modesetting enabled.
[   20.684578] [drm] amdgpu version: 5.4.8
[   20.846429] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 0: 0xa0000000 -> 0xafffffff
[   20.846430] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 2: 0xb0000000 -> 0xb01fffff
[   20.846431] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xb2200000 -> 0xb223ffff
[   20.846442] amdgpu 0000:01:00.0: enabling device (0400 -> 0403)
[   21.207900] amdgpu 0000:01:00.0: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[   21.207902] amdgpu 0000:01:00.0: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   21.208345] [drm] amdgpu: 4096M of VRAM memory ready
[   21.208347] [drm] amdgpu: 15886M of GTT memory ready.
[   21.780897] amdgpu: [powerplay] hwmgr_sw_init smu backed is iceland_smu
[   21.807264] amdgpu: [powerplay] can't get the mac of 5
[   21.813001] [drm] Initialized amdgpu 3.36.0 20150101 for 0000:01:00.0 on minor 1
[   30.905299] amdgpu: [powerplay] VI should always have 2 performance levels
[   53.602021] amdgpu: [powerplay] can't get the mac of 5
[   58.649120] amdgpu: [powerplay] VI should always have 2 performance levels
[   65.353858] amdgpu: [powerplay] can't get the mac of 5
[   70.649100] amdgpu: [powerplay] VI should always have 2 performance levels
[   95.544782] amdgpu: [powerplay] can't get the mac of 5
[  101.753588] amdgpu: [powerplay] VI should always have 2 performance levels
[  106.648326] amdgpu: [powerplay] can't get the mac of 5
[  112.765460] amdgpu: [powerplay] VI should always have 2 performance levels
[  120.756067] amdgpu: [powerplay] can't get the mac of 5
[  126.846593] amdgpu: [powerplay] VI should always have 2 performance levels
[  133.137531] amdgpu: [powerplay] can't get the mac of 5
[  150.617741] amdgpu: [powerplay] VI should always have 2 performance levels
[  169.125761] amdgpu: [powerplay] can't get the mac of 5
[  175.257388] amdgpu: [powerplay] VI should always have 2 performance levels
[  251.974242] amdgpu: [powerplay] can't get the mac of 5
[  258.188603] amdgpu: [powerplay] VI should always have 2 performance levels
[  311.937210] amdgpu: [powerplay] can't get the mac of 5
[  318.191991] amdgpu: [powerplay] VI should always have 2 performance levels
[  371.906937] amdgpu: [powerplay] can't get the mac of 5
[  378.070510] amdgpu: [powerplay] VI should always have 2 performance levels
[  425.235868] amdgpu: [powerplay] can't get the mac of 5
[  437.187879] amdgpu: [powerplay] VI should always have 2 performance levels
[  491.376021] amdgpu: [powerplay] can't get the mac of 5
[  497.531085] amdgpu: [powerplay] VI should always have 2 performance levels
[  551.347446] amdgpu: [powerplay] can't get the mac of 5
[  557.603576] amdgpu: [powerplay] VI should always have 2 performance levels
[  611.314621] amdgpu: [powerplay] can't get the mac of 5
[  617.569412] amdgpu: [powerplay] VI should always have 2 performance levels
[  671.287709] amdgpu: [powerplay] can't get the mac of 5
[  677.542727] amdgpu: [powerplay] VI should always have 2 performance levels
[  731.257183] amdgpu: [powerplay] can't get the mac of 5
[  737.513229] amdgpu: [powerplay] VI should always have 2 performance levels
[  791.224024] amdgpu: [powerplay] can't get the mac of 5
[  797.474598] amdgpu: [powerplay] VI should always have 2 performance levels
[  851.195397] amdgpu: [powerplay] can't get the mac of 5
[  857.448651] amdgpu: [powerplay] VI should always have 2 performance levels
[  910.828453] amdgpu: [powerplay] can't get the mac of 5
[  917.082055] amdgpu: [powerplay] VI should always have 2 performance levels
[  970.792947] amdgpu: [powerplay] can't get the mac of 5
[  977.047408] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1030.754488] amdgpu: [powerplay] can't get the mac of 5
[ 1037.003079] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1090.697060] amdgpu: [powerplay] can't get the mac of 5
[ 1096.952295] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1150.662098] amdgpu: [powerplay] can't get the mac of 5
[ 1156.914045] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1210.894362] amdgpu: [powerplay] can't get the mac of 5
[ 1217.158649] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1270.920491] amdgpu: [powerplay] can't get the mac of 5
[ 1277.178895] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1331.286646] amdgpu: [powerplay] can't get the mac of 5
[ 1337.565865] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1391.341482] amdgpu: [powerplay] can't get the mac of 5
[ 1397.583605] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1451.312376] amdgpu: [powerplay] can't get the mac of 5
[ 1457.567534] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1511.263030] amdgpu: [powerplay] can't get the mac of 5
[ 1517.516637] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1571.242848] amdgpu: [powerplay] can't get the mac of 5
[ 1577.329802] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1631.483699] amdgpu: [powerplay] can't get the mac of 5
[ 1637.746527] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1691.518836] amdgpu: [powerplay] can't get the mac of 5
[ 1697.692964] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1751.451320] amdgpu: [powerplay] can't get the mac of 5
[ 1757.706466] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1811.353647] amdgpu: [powerplay] can't get the mac of 5
[ 1817.472449] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1871.369316] amdgpu: [powerplay] can't get the mac of 5
[ 1877.648275] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1931.464593] amdgpu: [powerplay] can't get the mac of 5
[ 1937.687503] amdgpu: [powerplay] VI should always have 2 performance levels
[ 1991.454568] amdgpu: [powerplay] can't get the mac of 5
[ 1997.702968] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2051.486059] amdgpu: [powerplay] can't get the mac of 5
[ 2057.729291] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2111.280446] amdgpu: [powerplay] can't get the mac of 5
[ 2117.534785] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2171.263886] amdgpu: [powerplay] can't get the mac of 5
[ 2177.502770] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2231.233034] amdgpu: [powerplay] can't get the mac of 5
[ 2237.385390] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2291.482254] amdgpu: [powerplay] can't get the mac of 5
[ 2297.500040] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2351.475631] amdgpu: [powerplay] can't get the mac of 5
[ 2357.702646] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2411.354909] amdgpu: [powerplay] can't get the mac of 5
[ 2417.598879] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2471.280060] amdgpu: [powerplay] can't get the mac of 5
[ 2477.531919] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2531.254168] amdgpu: [powerplay] can't get the mac of 5
[ 2537.509068] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2538.522494] amdgpu: [powerplay] can't get the mac of 5
[ 2544.785944] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2591.273045] amdgpu: [powerplay] can't get the mac of 5
[ 2597.528109] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2651.272477] amdgpu: [powerplay] can't get the mac of 5
[ 2657.227449] amdgpu: [powerplay] VI should always have 2 performance levels
[ 2711.433852] amdgpu: [powerplay] can't get the mac of 5
[ 2717.696429] amdgpu: [powerplay] VI should always have 2 performance levels

```
I didn't encounter anyone getting this type of message. So, I am confused as to what this means. 
My system configurations are:
  
  

![Screenshot from 2020-05-26 11-10-24](https://user-images.githubusercontent.com/38552168/82864180-9fbee580-9f41-11ea-9e03-1031cd421748.png)
  
 
I tried the guide provided here at #1112 but without any luck.  
Please guide me through the required steps if the system is compatible.

---

## 评论 (1 条)

### 评论 #1 — rkothako (2020-05-27T14:05:48Z)

Hi @Rutvik-Trivedi,
Looks like the GPU might not support ROCm. Please check this https://github.com/RadeonOpenCompute/ROCm/wiki#Hardware-and-Software-Support

And also, ROCm 3.3 does not have official support of Ubuntu 20.04.


---
