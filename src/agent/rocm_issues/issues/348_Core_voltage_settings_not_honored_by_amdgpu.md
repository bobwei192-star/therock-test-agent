# Core voltage settings not honored by amdgpu

> **Issue #348**
> **状态**: closed
> **创建时间**: 2018-03-01T02:39:43Z
> **更新时间**: 2018-10-27T05:46:22Z
> **关闭时间**: 2018-06-03T14:38:50Z
> **作者**: Angel996
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/348

## 描述

Being able to downvolt GPUs in Linux is obviously crucial in mining. A simple hack of the polaris10_smc.c file found here achieves the task, it does work with latest versions of amdgpu (like 17.40):

https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/amd-linux/918649-underclocking-undervolting-the-rx-470-with-amdgpu-pro-success

The `polaris10_get_dependency_volt_by_clk` is responsible for setting core voltage. Strange though, the article is dated 2016, yet, up until now this has not been fixed. Core voltage table contained in GPU vbios works correctly in Windows, however in Linux it's ignored and core voltage is set at bootup at some fixed value (whose _value_ I was not even able to tell).

I am not that much of a programmer to do it myself (I'm also kinda afraid to burn my GPUs $1800 worth), but this should really be an easy job for someone who wrote amdgpu. Just wonder why it's never been done? Or maybe it can be set somewhere in the OS itself, in config files? In `/sys/class/hwmon/hwmon$i/device/pp_table` ? Can you please hint it?

p.s. Neither ohgodatool or rocm-smi can actually downvolt GPU core. Power table values change, but actual core voltage does not. Ohgodatool can downvolt vddci, but that's only about 5% power savings.

thanks )

---

## 评论 (41 条)

### 评论 #1 — ms178 (2018-03-01T21:04:42Z)

As this is possibly not a ROCm issue, I guess the correct channel for this bug report would be: https://bugzilla.kernel.org or maybe the amd-gfx mailing list, could you please file this as a bug over there?! Thanks!

---

### 评论 #2 — gstoner (2018-03-03T17:13:42Z)

This is correct, the issue is in the amdgpu driver which ROCm inherits,  We will track it here until it closes 

---

### 评论 #3 — rhlug (2018-03-08T23:49:55Z)

I've been testing pp_tables on each ROCm release.  

Pretty sure this isnt a ROCm issue, because I've manage to get it working.    Modified pp_tables work on kernel 4.4.0-112-generic, but not in 4.13.0-36-generic (hwe kernel), nor in 4.16.0-041600rc4-generic.  

I was using ROCm 1.7 before, and was able to modified clocks and core voltages with 4.4.0-112 kernel.  I just tested the 1.7.1 Beta 4, and it also works on 4.4.0-112, but not on 4.13 or 4.16 kernels I tried.

```
# uname -a
Linux localhost 4.4.0-112-generic #135-Ubuntu SMP Fri Jan 19 11:48:36 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

# cat /sys/class/drm/card*/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1084Mhz 
3: 1138Mhz 
4: 1200Mhz 
5: 1401Mhz 
6: 1536Mhz 
7: 1630Mhz 

# cat mining/ppt/ethash/0 > /sys/class/drm/card0/device/pp_table 

# cat /sys/class/drm/card*/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1017Mhz 
3: 1047Mhz 
4: 1097Mhz 
5: 1147Mhz 
6: 1197Mhz 
7: 1227Mhz 
```

here is what happens in 4.16 (same thing occurs in 4.13)

```
# uname -a
Linux localhost 4.16.0-041600rc4-generic #201803041930 SMP Mon Mar 5 00:32:34 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

# cat /sys/class/drm/card*/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1084Mhz 
3: 1138Mhz 
4: 1200Mhz 
5: 1401Mhz 
6: 1536Mhz 
7: 1630Mhz 

# cat mining/ppt/ethash/0 > /sys/class/drm/card0/device/pp_table

# cat /sys/class/drm/card*/device/pp_dpm_sclk
Killed

# tail -n 2 /var/log/syslog
Mar  8 17:14:24 rig23 kernel: [   70.310155] amdgpu: [powerplay] Failed to register high thermal interrupt!
Mar  8 17:14:24 rig23 kernel: [   70.310156] amdgpu: [powerplay] amdgpu: powerplay initialization failed
```

How it works in 4.4.0-112 and not in the hwe kernel or bleeding edge is beyond me.


---

### 评论 #4 — Angel996 (2018-03-09T01:39:25Z)

rhlug, thanks for your input. But you are referring to core clock, not core voltage. I can set both core and memory clocks fine. I run `4.4.0-112-generic #135-Ubuntu SMP Fri Jan 19 11:48:36 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux` which is latest generic kernel available, I believe.

---

### 评论 #5 — rhlug (2018-03-09T13:38:12Z)

@Angel996  you misread.  --> "was able to modified clocks and core voltages"


---

### 评论 #6 — rhlug (2018-03-09T13:42:16Z)

```
# ./mod_pptable.t 1
Modifying core-state-2 to 108400 (70A701)
Modifying core-state-3 to 113800 (88BC01)
Modifying core-state-4 to 120000 (C0D401)
Modifying core-state-5 to 128700 (BCF601)
Modifying core-state-6 to 129700 (A4FA01)
Modifying core-state-7 to 130700 (8CFE01)
Modifying mem-state-2 to 94500 (247101)
Modifying mem-state-3 to 102000 (708E01)
Modifying vcore-state-1 to 850 (5203)
Modifying vcore-state-2 to 850 (5203)
Modifying vcore-state-3 to 875 (6B03)
Modifying vcore-state-4 to 900 (8403)
Modifying vcore-state-5 to 900 (8403)
Modifying vcore-state-6 to 900 (8403)
Modifying vcore-state-7 to 900 (8403)
# Full Hex string of /sys/class/drm/card0/device/pp_table
B6 02 08 01 00 5C 00 E1 06 00 00 EE 2B 00 00 1B 00 48 00 00 00 80 A9 03  [48]
00 F0 49 02 00 32 00 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 01  [96]
5C 00 4F 02 46 02 94 00 9E 01 BE 00 28 01 7A 00 8C 00 BC 01 00 00 00 00  [144]
72 02 00 00 90 00 A8 02 6D 01 43 01 97 01 F0 49 02 00 71 02 02 02 00 00  [192]
00 00 00 00 08 00 00 00 00 00 00 00 05 00 07 00 03 00 05 00 00 00 00 00  [240]
00 00 01 08 20 03 52 03 52 03 6B 03 84 03 84 03 84 03 84 03 01 01 46 05  [288]
01 01 84 03 00 08 60 EA 00 00 00 40 19 01 00 01 80 38 01 00 02 DC 4A 01  [336]
00 03 90 5F 01 00 04 00 77 01 00 05 90 91 01 00 06 6C B0 01 00 07 01 08  [384]
D0 4C 01 00 00 00 80 00 00 00 00 00 00 1C 83 01 00 01 00 00 00 00 00 00  [432]
00 00 70 A7 01 00 02 00 00 00 00 00 00 00 00 88 BC 01 00 03 00 00 00 00  [480]
00 00 00 00 C0 D4 01 00 04 00 00 00 00 00 00 00 00 BC F6 01 00 05 00 00  [528]
00 00 01 00 00 00 A4 FA 01 00 06 00 00 00 00 01 00 00 00 8C FE 01 00 07  [576]
00 00 00 00 01 00 00 00 00 05 60 EA 00 00 00 40 19 01 00 00 80 38 01 00  [624]
00 DC 4A 01 00 00 90 5F 01 00 00 00 08 28 6E 00 00 00 2C C9 00 00 01 F8  [672]
0B 01 00 02 80 38 01 00 03 90 5F 01 00 04 F4 91 01 00 05 D0 B0 01 00 06  [720]
C0 D4 01 00 07 00 08 6C 39 00 00 00 24 5E 00 00 01 FC 85 00 00 02 AC BC  [768]
00 00 03 34 D0 00 00 04 68 6E 01 00 05 08 97 01 00 06 EC A3 01 00 07 00  [816]
01 68 3C 01 00 00 01 04 3C 41 00 00 00 00 00 50 C3 00 00 00 00 00 24 71  [864]
01 00 02 00 00 70 8E 01 00 04 00 00 01 08 00 98 85 00 00 40 B5 00 00 60  [912]
EA 00 00 50 C3 00 00 01 80 BB 00 00 60 EA 00 00 94 0B 01 00 50 C3 00 00  [960]
02 00 E1 00 00 94 0B 01 00 40 19 01 00 50 C3 00 00 03 78 FF 00 00 40 19  [1008]
01 00 88 26 01 00 50 C3 00 00 04 40 19 01 00 80 38 01 00 80 38 01 00 50  [1056]
C3 00 00 05 80 38 01 00 DC 4A 01 00 DC 4A 01 00 50 C3 00 00 06 00 77 01  [1104]
00 00 77 01 00 90 5F 01 00 50 C3 00 00 07 90 91 01 00 90 91 01 00 00 77  [1152]
01 00 50 C3 00 00 01 18 00 00 00 00 00 00 00 0B E4 12 60 09 60 09 4B 00  [1200]
0A 00 54 03 90 01 90 01 90 01 90 01 90 01 90 01 90 01 00 00 00 00 00 02  [1248]
04 31 07 DC 00 DC 00 DC 00 2C 01 00 00 59 00 69 00 4A 00 4A 00 5F 00 73  [1296]
00 73 00 64 00 40 00 90 92 97 60 96 00 90 55 00 00 00 00 00 00 00 00 00  [1344]
00 00 00 00 00 00 00 00 02 02 D4 30 00 00 02 10 60 EA 00 00 02 10 

Packed into 694 bytes and wrote to pp_table
```

---

### 评论 #7 — Angel996 (2018-03-09T19:26:12Z)

rhlug, powerplay table DOES get modified for core voltage, but core voltage is not physically changed on the GPU.

---

### 评论 #8 — rhlug (2018-03-10T23:38:20Z)

@Angel996  I'm not a home to confirm, but when I return I will test next week with various core voltages and measure TDP.   I do know my TDP for 2x vega was 409w mining eth @ nearly 40Mh/s each, and here is the rocm-smi

```
# /opt/rocm/bin/rocm-smi 

====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   53.0c   142.0W   1227Mhz  1023Mhz  54.9%    auto      0%       
  1   62.0c   128.0W   1227Mhz  1023Mhz  60.0%    auto      0%       
================================================================================
====================           End of ROCm SMI Log          ====================

```

I have display attached to GPU 0, so it pulls a bit more watts.  GPU 1 uses less power and runs hotter, so maybe just a shit ASIC.




---

### 评论 #9 — Angel996 (2018-03-11T16:28:51Z)

I have Polaris GPUs and the bug is probably in `polaris10_smc.c`. I believe, Vega powerplay routines are contained within `vega10_*.c` files. And, unfortunately, rocm-smi does not provide power reading for Polaris GPUs. Neither have I found a way to see current VDDC / VDDCi value. Could have been handy too. Here is my rocm-smi output (Claymore ETH miner running):

```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   65.0c   N/A      1100Mhz  2050Mhz  46.67%   auto      0%
  1   65.0c   N/A      1100Mhz  2000Mhz  46.67%   auto      0%
  2   63.0c   N/A      1100Mhz  2050Mhz  24.71%   auto      0%
  3   64.0c   N/A      1100Mhz  2040Mhz  40.0%    auto      0%
  4   64.0c   N/A      1080Mhz  2040Mhz  40.0%    auto      0%
================================================================================
====================           End of ROCm SMI Log          ====================

```

---

### 评论 #10 — 949f45ac (2018-03-12T14:26:07Z)

Supposedly improvements will arriving with kernel release 4.17.

https://lists.freedesktop.org/archives/dri-devel/2018-February/167138.html
>- Expose GPU voltage and power via hwmon
>- Initial wattman-like support

---

### 评论 #11 — rhlug (2018-03-20T15:02:16Z)

@949f45ac 

What works in 4.4.0-112, is not working in the nightly 4.16.0-994.201803200223.   So that is worrisome for 4.17.
```
# uname -a
Linux localhost 4.16.0-994-lowlatency #201803200223 SMP PREEMPT Tue Mar 20 02:28:15 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

# cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1084Mhz 
3: 1138Mhz 
4: 1200Mhz 
5: 1401Mhz 
6: 1536Mhz 
7: 1630Mhz 

# cat 0 > /sys/class/drm/card0/device/pp_table 

# cat /sys/class/drm/card0/device/pp_dpm_sclk
Killed

# tail -n 2 /var/log/syslog
Mar 20 09:58:29 localhost kernel: [  123.821132] amdgpu: [powerplay] Failed to register high thermal interrupt!
Mar 20 09:58:29 localhost kernel: [  123.821133] amdgpu: [powerplay] amdgpu: powerplay initialization failed
```




---

### 评论 #12 — rhlug (2018-03-20T15:52:13Z)

@Angel996  

I can confirm on Vega10 powerplay, the vcore modifications work on kernel 4.4.0-112 

You can see 522w @ stock, 482w w/ 990mv core, and 434w w/ 890mv core on GPU #0.   My other 5 Vegas were sitting idle while testing, hence the higher TDP.

```
pp_table -> stock
522w (6gpu, GPU0 mining ethash, ~34mh/s)

pp_table -> eth_vega64_pp_table_1227_890_1023
434w (6gpu, GPU0 mining ethash, ~39mh/s)

pp_table -> eth_vega64_pp_table_1227_990_1023
470w (6gpu, GPU0 mining ethash, ~39.5mh/s, 62c, 4720rpm)
```

Here is rocm-smi output, most notable is the fan speed to keep like temperature at same core and memory clocks.

```

@ 990mv
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   61.0c   173.0W   1227Mhz  1023Mhz  95.69%   auto      0%       

@ 890mv
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   62.0c   142.0W   1227Mhz  1023Mhz  47.84%   auto      0%       

```


---

### 评论 #13 — todxx (2018-03-21T11:37:16Z)

@rhlug The first error you're seeing is coming from vega10_register_thermal_interrupt in vega10_hwmgr.c.
After some digging, I have some vague ideas of what might be happening.

This function is part of the hwmgr initialization sequence.  When pp tables are written, the hwmgr is re-initialized.  This re-initialization is when this error is hit.  The interesting part is that this initialization sequence is the same as was performed when the card was first loaded, and it seems to have worked the first time.  So digging through what vega10_register_thermal_interrupt does and looking for anything that could be different between the first initialization and a second, I ended up finding this in the irq registration routine amdgpu_irq_add_id:
```
	if (adev->irq.client[client_id].sources[src_id] != NULL)
		return -EINVAL;

	if (source->num_types && !source->enabled_types) {
		atomic_t *types;

		types = kcalloc(source->num_types, sizeof(atomic_t),
				GFP_KERNEL);
		if (!types)
			return -ENOMEM;

		source->enabled_types = types;
	}

	adev->irq.client[client_id].sources[src_id] = source;
	return 0;
```

The first two lines are a check to see if the irq was already registered, and if there was the routine exits with an error.  The registration happens in the 2nd to last line.  As can easily be seen, unless something unregisters the irq, running this routine twice would cause it to fail on the second call.

After digging around some more, the only irq clean-up I found was during device shutdown, i.e. unloading all of amdgpu for the device.  So my best guess is that when the hwmgr is reinitialized, it is attempting to register an already registered irq, gets an error, and aborts.

A quick and dirty hack to test this theory would be to replace the three occurances of `return -EINVAL` in vega10_register_thermal_interrupt with `return 0`.  Then a failure to register one of the thermal interrupts will cause the routine to return without causing hwmgr to abort initialization, though you will run the risk of potentially running without thermal threshold interrupts active.  Currently it looks like the interrupts only trigger an over-temp warning to be printed, so you wont be losing much.



---

### 评论 #14 — rhlug (2018-03-21T16:57:34Z)

@todxx  Thanks. Looking at 4.4.0-112 ubuntu source, vega10_hwmgr.c is not part of it.  So its coming via rock dkms.   Whereas in 4.16.x its provided by the kernel itself.

It didnt look like there was any difference in that block of code you mention above.  I was comparing

-> ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c
-> torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c

Does changing out the pp_table execute amdgpu_irq_reset_work_func() because it appears that bit has changed between ROCK-Kernel-Driver and 4.16.x

```
-		amdgpu_gpu_reset(adev);
+		amdgpu_device_gpu_recover(adev, NULL, false);
```

There are alot of changes between amdgpu_gpu_reset() in ROCK-Kernel-Driver and amdgpu_device_gpu_recover() in kernel.




---

### 评论 #15 — Angel996 (2018-03-21T18:36:47Z)

Hmm. How about some `polaris10_smc.c` talk, people? :-) The problem we, RX400/500 series owners are having, is not contained within the `vega10_hwmgr.c` source file.

---

### 评论 #16 — rhlug (2018-03-21T21:09:09Z)

I have lots of polaris, but all mine are bios modified, making pp_tables unnecessary.   vega10 requires pp_tables due to locked bios. 

---

### 评论 #17 — cdarken (2018-03-21T21:11:28Z)

@rhlug The issue is that the driver ignores whatever you have set in bios for the voltages.

@Angel996 I am using a workaround like here: https://forum.ethereum.org/discussion/17192/undervolting-amd-rx-cards-on-linux
It's a bit brute force but it works fine.

---

### 评论 #18 — Angel996 (2018-03-21T21:29:01Z)

cdarken, only modifying kernel module works for me. Setting VDDC via power table using ohgodatool _succeeds_, but does not _work_. Also I'm looking for a way to at least read current VDDC. _/sys/class/drm/card0/device/pp_voltage_ does not work since there is no _pp_voltage_ file in that directory.

---

### 评论 #19 — cdarken (2018-03-21T21:35:30Z)

@Angel996 at first, when I just tried to set a certain state at a fixed voltage it didn't work, but I think the trick in that workaround is that you have to set the entire table of voltages to the one you want, so the driver can only set the one you want no matter what.

Edit: btw, the detail is that you have to use the kernel driver, not the amdgpu-pro driver

---

### 评论 #20 — rhlug (2018-03-21T22:53:19Z)

@cdarken  my 6x 470 rigs on linux pull around 830w TDP with mod bios, mining 28.7Mh/s+ ethash.   Maybe I can get lower, but it sure seems to me like the 900mv vcore are lowering TDP significantly.  Its been 15 months since I modded my polaris chips, but IIRC, my TDP was directly effected by the voltages I was setting at the time.




---

### 评论 #21 — todxx (2018-03-22T03:15:30Z)

@rhlug I don't think the previous versions of the kernel had "better" clean-up of the irq's.  I believe the main difference affecting this error is that the thermal interrupt registration was added in 4.15.  So the 1.7.x rock kernel doesn't have the vega10_register_thermal_interrupt function at all.

I'm not sure what would be the correct way to fix this issue.  The vega10_register_thermal_interrupt function is invoked via a func ptr from an instance of the pp_hwmgr_func struct.  However, that struct doesn't seem to have a corresponding unregister func ptr.  Also, I couldn't manage to find a reverse version of amdgpu_irq_add_id for removing irq registration, so I'm not sure how one would go about implementing the unregister function.  I think this will need the attention of the amdgpu team to get a non-hacky fix.

---

### 评论 #22 — cdarken (2018-03-22T07:30:43Z)

@rhlug did you modify other settings in the bios, like the TDP? I did that too and it had some impact, I was at just under 100W on the GPU, as shown by the rocm-smi utility. but now I'm running with VDDC at 820mV and core freq at 1100 and I'm under 80W, mostly around 77.

---

### 评论 #23 — Angel996 (2018-03-22T11:18:24Z)

cdarken, power limit can be modified using ohgodatool, it does work, but it's not really usable because cards get very unstable, frequencies jump a lot and hashrate drops significantly when a card hits its power limit. 

I'll try the entire table trick for voltages as per your suggestion, thanks!

---

### 评论 #24 — cdarken (2018-03-22T11:28:41Z)

out of curiosity, can you post your rocm-smi output with your current setup?

---

### 评论 #25 — rhlug (2018-03-23T16:31:31Z)

my rocm-smi doesnt report wattage, probably because I'm not using rocm, but amdgpu-pro 17.50 on all my rx470/570 stuff.

```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  0   54.0c   N/A      1146Mhz  2046Mhz  37.65%   auto      0%       
  1   60.0c   N/A      1143Mhz  2093Mhz  40.0%    auto      0%       
  2   56.0c   N/A      1144Mhz  2094Mhz  37.65%   auto      0%       
  3   60.0c   N/A      1111Mhz  2041Mhz  47.84%   auto      0%       
  4   56.0c   N/A      1145Mhz  2095Mhz  37.65%   auto      0%       
  5   59.0c   N/A      1142Mhz  2092Mhz  37.65%   auto      0%       
================================================================================
====================           End of ROCm SMI Log          ====================
```


 and yes I lowered all three of the powertunes

TDP = 85
TDC = 99
Max Power = 100


---

### 评论 #26 — Angel996 (2018-03-23T17:15:19Z)

There is no wattage report for Polaris family GPUs. Only for Vegas.

---

### 评论 #27 — cdarken (2018-03-23T17:23:23Z)

I'm using this branch of the rocm-smi tool: https://github.com/RadeonOpenCompute/ROC-smi/tree/krussell/fixes

And you can check manually your power, execute this:
```
sudo cat /sys/kernel/debug/dri/*/amdgpu_pm_info
```
Replace the star with the card index that you want to see. That file should exist no matter what driver version you're using, I believe. 

---

### 评论 #28 — Angel996 (2018-03-23T21:59:53Z)

Wow, I was gonna say "awesome". :)) It does work.

Is it possible to see current VDDC settings? The voltage, I mean. If they calculate power, the should know the voltage. Or is it supplied by the chip itself?

---

### 评论 #29 — cdarken (2018-03-23T23:23:58Z)

The voltages are not exposed through the sys interface, AFAIK.

---

### 评论 #30 — rhlug (2018-03-25T15:22:41Z)

Here are some 570s

```
# cat /sys/kernel/debug/dri/*/amdgpu_pm_info | grep -A6 GFX
GFX Clocks and Power:
	2046 MHz (MCLK)
	1146 MHz (SCLK)
	59.180 W (VDDC)
	12.125 W (VDDCI)
	77.205 W (max GPU)
	78.49 W (average GPU)
--
GFX Clocks and Power:
	2093 MHz (MCLK)
	1143 MHz (SCLK)
	60.201 W (VDDC)
	12.199 W (VDDCI)
	80.62 W (max GPU)
	79.144 W (average GPU)
--
GFX Clocks and Power:
	2094 MHz (MCLK)
	1144 MHz (SCLK)
	61.152 W (VDDC)
	12.201 W (VDDCI)
	79.90 W (max GPU)
	80.97 W (average GPU)
--
GFX Clocks and Power:
	2041 MHz (MCLK)
	1129 MHz (SCLK)
	63.199 W (VDDC)
	12.118 W (VDDCI)
	81.70 W (max GPU)
	82.61 W (average GPU)
--
GFX Clocks and Power:
	2095 MHz (MCLK)
	1145 MHz (SCLK)
	60.145 W (VDDC)
	12.202 W (VDDCI)
	79.160 W (max GPU)
	79.91 W (average GPU)
--
GFX Clocks and Power:
	2092 MHz (MCLK)
	1142 MHz (SCLK)
	60.192 W (VDDC)
	12.197 W (VDDCI)
	78.162 W (max GPU)
	79.133 W (average GPU)
```


---

### 评论 #31 — gstoner (2018-03-25T15:25:09Z)

I am talking to the AMDGPU and power management team about this.  

---

### 评论 #32 — gstoner (2018-03-25T15:27:14Z)

Vega10 they introduced the PSP and also changed the SMU firmware interfaces, they removed a number of the interface we had on GFX8.  We in negotiations with the team who develop VBIOS,  PPLIB and SMU firmware team where all this logic takes place. 

---

### 评论 #33 — cdarken (2018-03-25T17:45:21Z)

@rhlug would you share your bios for the 570s, please? I'm curious what you changed. thanks.

---

### 评论 #34 — Angel996 (2018-03-25T18:34:58Z)

The `cat /sys/kernel/debug/dri/*/amdgpu_pm_info` method works for all my Polaris cards, it's excellent. It would be cool to have VDDM power consumption and voltages, but apparently this is not possible.

---

### 评论 #35 — rhlug (2018-03-27T15:31:41Z)

@cdarken - not easily as they are all on a windows disk that I only use for flashing.  next time I break it out I can.  I have an RMA coming from MSI in the next week or two, so it shouldnt be long.


---

### 评论 #36 — rhlug (2018-03-28T16:10:02Z)

pp_tables are working on latest nightly... 41mh/s ethash on vega 56 (mesa clover opencl)

cant wait to compare this to a working amdgpu-pro 18.10.


---

### 评论 #37 — rhlug (2018-03-29T15:40:33Z)

>> I have an RMA coming from MSI in the next week or two, so it shouldnt be long.

maybe not... GRRRR

```
Dear customer,

Replacement is not available for your RMA. Would you accept below refund amount?

Radeon RX 470 GAMING X 4G    Refund price $178
```

Too bad I cant replace it for anywhere near $178 right now.

---

### 评论 #38 — Angel996 (2018-08-14T21:42:48Z)

I am really sorry, but has anyone been able to modify core voltage on Polaris cards w/o modifying the kernel module?

---

### 评论 #39 — Venemo (2018-10-26T09:03:38Z)

@gstoner It seems to me that this issue is still present in latest `amdgpu` when using Polaris. It will disrespect the voltages from video bios and automatically under-volt the video memory on my RX 570, which results in instability.

Can you please look into this a bit more?

Note that I didn't edit my video bios, just took a look at what values are in there, and compared it to the contents of `/sys/class/drm/card0/device/pp_od_clk_voltage` --- it turns out that the vbios suggests to set all memory voltages to 1000 mV (on all clock settings), while amdgpu decides to set them a couple of hundred mV lower. This, under heavy load, will make the graphics card unstable, and results in a GPU hang and the dreaded `ring gfx timeout` and similar messages.

If I manually edit `/sys/class/drm/card0/device/pp_od_clk_voltage` to increase the memory voltages, then the instability goes away.

---

### 评论 #40 — jlgreathouse (2018-10-26T19:36:11Z)

Do you have OverDrive enabled in your `ppfeaturemask`? I would assume so, since `pp_od_clk_voltage` [doesn't return anything without OverDrive enabled](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c#L4450).

As such, a few questions:
- If you're not running with OverDrive enabled (disable [bit 14 of the ppfeaturemask](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/include/amd_shared.h#L130)), does this instability still exist? I would like to try to figure out if this is a general problem or a potential problem on our OD path.
- Are you using a custom modified VBIOS or the default VBIOS that came on your GPU/
- Could you possibly send me your VBIOS ROM and the PPTable in use in this problematic case? You can get these by dumping (as root) `/sys/class/drm/card0/device/rom` and `/sys/class/drm/card0/device/pp_table` to files. Email --> Joseph dot Greathouse at amd
- Could you show me the values in `/sys/class/drm/card0/device/subsystem_device`, `/sys/class/drm/card0/device/subsystem_vendor`, and `/sys/class/drm/card0/device/vbios_version`

---

### 评论 #41 — Venemo (2018-10-27T05:41:44Z)

@jlgreathouse Thank you for looking into this.

* If I'm not running with OD enabled, yes, the instability still exists. Note that I'm not using OD to overclock, just using it for editing those voltages. Please take a look at [this bug report](https://bugs.freedesktop.org/show_bug.cgi?id=108493) where I describe in detail what my setup looks like and what happens exactly when the GPU hangs. **EDIT:** just to clarify, I tried running with `ppfeaturemask=0xffffffff` (enabling all pp features) and also tried not setting `ppfeaturemask` at all. The instability happens in both cases. But I haven't tried changing just that one bit.
* I haven't modified my VBIOS, however the card is second-hand so there is a slight chance it was modified (though the seller did not mention this). I used [this tool](https://github.com/wilvk/pbec) to see what voltages are set in VBIOS.
* I cannot access that `rom` file, because it tells me `Invalid argument`. So I was working with `/sys/kernel/debug/dri/0/amdgpu_vbios` ― aren't these supposed to be the same? In any case, I attached the content of `amdgpu_vbios` and the `pp_table` to the aforementioned bugreport on freedesktop.org
* Yeah, sure, here you go:

```
[root@timur-xps ~]# cat /sys/class/drm/card0/device/subsystem_device
0xe343
[root@timur-xps ~]# cat /sys/class/drm/card0/device/subsystem_vendor
0x1da2
[root@timur-xps ~]# cat /sys/class/drm/card0/device/vbios_version
113-D00034-S07
```

---
