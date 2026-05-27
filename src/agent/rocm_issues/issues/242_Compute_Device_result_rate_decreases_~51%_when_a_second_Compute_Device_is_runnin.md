# Compute Device result rate decreases ~51% when a second Compute Device is running

> **Issue #242**
> **状态**: closed
> **创建时间**: 2017-11-03T01:37:01Z
> **更新时间**: 2018-02-18T03:55:56Z
> **关闭时间**: 2018-02-18T03:55:56Z
> **作者**: lsimplify
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/242

## 描述

My issue is that my performance (result rate) decreases once I run OpenCL code on a second GPU.
I start the program and ask it to run on Device 0. I start the program a second time and ask it to run on Device 1. **Device 1 starts and stays at half performance compared to it's performance when ran alone. Device 0's performance decreases ~105%.**

(I setup the program to use 2 CPU threads for each Compute Device, in case that makes any difference for you.)

My two compute devices each have their own x8 PCIe 3.0 directly to the processor. 
Compute Devices: RX580 4GB (Qty 2)

./rocm_agent_enumerator -t gpu
```
gfx000
gfx803

```
Headless Ubuntu 17.10, AMD Ryzen 5 1600X, 32GiB system ram
uname -r   `4.11.0-kfd-compute-rocm-rel-1.6-180`

lspci -v -d1002
```

24:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev e7) (prog-if 00 [VGA controller])
	Subsystem: XFX Pine Group Inc. Ellesmere [Radeon RX 470/480/570/580]
	Flags: bus master, fast devsel, latency 0, IRQ 323
	Memory at e0000000 (64-bit, prefetchable) [size=256M]
	Memory at f0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at e000 [size=256]
	Memory at fe900000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

24:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
	Subsystem: XFX Pine Group Inc. Device aaf0
	Flags: bus master, fast devsel, latency 0, IRQ 335
	Memory at fe960000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel

25:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480] (rev e7) (prog-if 00 [VGA controller])
	Subsystem: XFX Pine Group Inc. Ellesmere [Radeon RX 470/480/570/580]
	Flags: bus master, fast devsel, latency 0, IRQ 330
	Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Memory at d0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at d000 [size=256]
	Memory at fe800000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at fe840000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

25:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Device aaf0
	Subsystem: XFX Pine Group Inc. Device aaf0
	Flags: bus master, fast devsel, latency 0, IRQ 337
	Memory at fe860000 (64-bit, non-prefetchable) [size=16K]
	Capabilities: <access denied>
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
```

dmesg | grep -i IOMMU
```
[    1.059385] AMD-Vi: IOMMU performance counters supported
[    1.059588] iommu: Adding device 0000:00:01.0 to group 0
[    1.059651] iommu: Adding device 0000:00:01.3 to group 1
[    1.059714] iommu: Adding device 0000:00:02.0 to group 2
[    1.059782] iommu: Adding device 0000:00:03.0 to group 3
[    1.059846] iommu: Adding device 0000:00:03.1 to group 4
[    1.059911] iommu: Adding device 0000:00:03.2 to group 5
[    1.059973] iommu: Adding device 0000:00:04.0 to group 6
[    1.060038] iommu: Adding device 0000:00:07.0 to group 7
[    1.060053] iommu: Adding device 0000:00:07.1 to group 7
[    1.060116] iommu: Adding device 0000:00:08.0 to group 8
[    1.060130] iommu: Adding device 0000:00:08.1 to group 8
[    1.060192] iommu: Adding device 0000:00:14.0 to group 9
[    1.060206] iommu: Adding device 0000:00:14.3 to group 9
[    1.060284] iommu: Adding device 0000:00:18.0 to group 10
[    1.060298] iommu: Adding device 0000:00:18.1 to group 10
[    1.060311] iommu: Adding device 0000:00:18.2 to group 10
[    1.060325] iommu: Adding device 0000:00:18.3 to group 10
[    1.060337] iommu: Adding device 0000:00:18.4 to group 10
[    1.060350] iommu: Adding device 0000:00:18.5 to group 10
[    1.060362] iommu: Adding device 0000:00:18.6 to group 10
[    1.060374] iommu: Adding device 0000:00:18.7 to group 10
[    1.060447] iommu: Adding device 0000:03:00.0 to group 11
[    1.060467] iommu: Adding device 0000:03:00.1 to group 11
[    1.060487] iommu: Adding device 0000:03:00.2 to group 11
[    1.060499] iommu: Adding device 0000:04:00.0 to group 11
[    1.060510] iommu: Adding device 0000:04:01.0 to group 11
[    1.060522] iommu: Adding device 0000:04:02.0 to group 11
[    1.060534] iommu: Adding device 0000:04:03.0 to group 11
[    1.060545] iommu: Adding device 0000:04:04.0 to group 11
[    1.060557] iommu: Adding device 0000:04:08.0 to group 11
[    1.060575] iommu: Adding device 0000:1e:00.0 to group 11
[    1.060590] iommu: Adding device 0000:23:00.0 to group 11
[    1.060674] iommu: Adding device 0000:24:00.0 to group 12
[    1.060699] iommu: Using direct mapping for device 0000:24:00.0
[    1.060725] iommu: Adding device 0000:24:00.1 to group 12
[    1.060796] iommu: Adding device 0000:25:00.0 to group 13
[    1.060821] iommu: Using direct mapping for device 0000:25:00.0
[    1.060851] iommu: Adding device 0000:25:00.1 to group 13
[    1.060862] iommu: Adding device 0000:26:00.0 to group 7
[    1.060872] iommu: Adding device 0000:26:00.2 to group 7
[    1.060882] iommu: Adding device 0000:26:00.3 to group 7
[    1.060891] iommu: Adding device 0000:27:00.0 to group 8
[    1.060901] iommu: Adding device 0000:27:00.2 to group 8
[    1.060910] iommu: Adding device 0000:27:00.3 to group 8
[    1.061089] AMD-Vi: Found IOMMU at 0000:00:00.2 cap 0x40
[    1.062314] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)
[    1.383424] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
```


dmseg | grep kfd
Here are some boot messages:
```
[    1.229795] usb usb6: Manufacturer: Linux 4.11.0-kfd-compute-rocm-rel-1.6-180 xhci-hcd
[    1.425181] kfd kfd: Initialized module
[    2.265702] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[    2.265929] kfd kfd: Reserved 2 pages for cwsr.
[    2.265973] kfd kfd: added device 1002:67df
[    3.462612] kfd kfd: Allocated 3969056 bytes on gart for device 1002:67df
[    3.465282] kfd kfd: Reserved 2 pages for cwsr.
[    3.465786] kfd kfd: added device 1002:67df
```
and these messages appear when starting even a single Compute Device: 
```
[   84.025373] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025402] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025422] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025442] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025462] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[   84.025482] kfd2kgd: Failed to create BO on domain VRAM. ret -12
```

I continuously get additional messages when running both Compute Devices:
```
[48405.710824] Started evicting process of pasid 2
[48405.711497] Finished evicting process of pasid 2
[48405.712811] Finished restoring process of pasid 1
[48406.126508] Started restoring process of pasid 2
[48406.126862] Started evicting process of pasid 1
[48406.127546] Finished evicting process of pasid 1
[48406.128858] Finished restoring process of pasid 2
[51389.814655] Started evicting process of pasid 2
[51389.814657] process_evict_queues: 14 callbacks suppressed
[51389.814658] Evicting PASID 2 queues
[51389.814696] Evicting PASID 2 queues
[51389.814840] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.814918] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.814984] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815049] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815115] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815180] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815246] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815311] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815377] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815392] Finished evicting process of pasid 2
[51389.815443] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815509] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815574] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815640] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815705] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815771] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815837] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815902] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.815968] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816034] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816099] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816164] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816230] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816295] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816362] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816427] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816493] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816567] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816634] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51389.816700] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[51390.244946] Started restoring process of pasid 2
[51390.245612] Started evicting process of pasid 1
[51390.245612] Evicting PASID 1 queues
[51390.246302] Evicting PASID 1 queues
[51390.246320] Finished evicting process of pasid 1
[51390.247619] process_restore_queues: 12 callbacks suppressed
[51390.247619] Restoring PASID 2 queues
[51390.247623] Restoring PASID 2 queues
[51390.247626] Finished restoring process of pasid 2
[51390.660963] Started restoring process of pasid 1
[51390.661311] Started evicting process of pasid 2
[51390.661312] Evicting PASID 2 queues
[51390.661331] Evicting PASID 2 queues
[51390.661993] Finished evicting process of pasid 2
[51390.663301] Restoring PASID 1 queues
[51390.663305] Restoring PASID 1 queues
[51390.663307] Finished restoring process of pasid 1
```


---

## 评论 (10 条)

### 评论 #1 — preda (2017-11-03T09:38:04Z)

What do you mean by "device 0 performance decreases by 105%"? Could you give an example?


---

### 评论 #2 — lsimplify (2017-11-03T19:53:51Z)

>decreases by 105%

I think my 105% is wrong. I should have used:  `[ (theoretical - experimental) / theoretical ] · 100  = percent error`. I think the percent error equation is the best equation because the Device 0's performance, or result rate, should remain the same independent of what Device 1 is doing. Thus the percent error should be ~0%.

**What do the two variables equal?**
```
theoretical = result rate of Device 0 before Device 1 starts
experimental = result rate of Device 0 around 15 minutes after Device 1 starts
```

**An Example**
I'm running [xmr-stak-amd](https://github.com/fireice-uk/xmr-stak-amd) version `1.1.0-1.4.0`. The program's GitHub repository has the OpenCL source code.  The `xmr-stak-amd` is built with the `rocm-1.6.180` OpenCL files in `/opt/rocm/opencl...`

Each Device has a configuration directory `'rx580_a'` `'rx580_b'` to hold the `xmr-stak-amd` `config.txt` file. The `xmr-stak-amd` binary is symbolic linked into both configuration directories.

systemd unit files execute `xmr-stak-amd` in the Device's configuration directory as a non-privileged user. The unit turns the fans up.

Device 0 `config.txt` snippet:
```
"gpu_threads_conf" : [ 
 { "index" : 0, "intensity" : ???, "worksize" : ?, "affine_to_cpu" : false },
 { "index" : 0, "intensity" : ???, "worksize" : ?, "affine_to_cpu" : false },
],
```
Device 1 `config.txt` snippet:
```
"gpu_threads_conf" : [ 
 { "index" : 1, "intensity" : ???, "worksize" : ?, "affine_to_cpu" : false },
 { "index" : 1, "intensity" : ???, "worksize" : ?, "affine_to_cpu" : false },
],
```

**Data**

`xmr-stak-amd` is executed to run Device 0.
~ 15 minutes later:
Device 0
```
Thread ID	10s	60s	15m average (H/s)
0		479.3	468.1	471.5
1		479.3	468.5	471.5
Totals:		958.5	936.5	943.0
```

`xmr-stak-amd` is executed to run Device 1. (The first `xmr-stak-amd` is still running Device 0.)
~ 15 minutes later:
Device 0
```
Thread ID	10s	60s	15m average (H/s)
0		149.4	158.2	169.6
1		298.9	298.8	288.1
Totals:		448.3	457.0	457.8
```
Device 1
```
Thread ID	10s	60s	15m average (H/s)
0		241.0	242.8	234.2
1		240.9	242.8	231.9
Totals:		481.9	485.7	466.1
```

**Stat. Analysis**

Device 0's percent error: [ (943.0 - 457.8) / 943.0 ] · 100 = ~51%

**So Device 0's performance, or result rate, decreased ~51%, not 105%.**

**dmesg**
I found this in the `dmesg` log after I executed `xmr-stak-amd` on Device 1:
```
[   83.912995] (this message intentionally removed)
[11886.403327] Started evicting process of pasid 1
[11886.403329] Evicting PASID 1 queues
[11886.404030] Evicting PASID 1 queues
[11886.404428] Finished evicting process of pasid 1
[11886.404832] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.404971] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405091] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405234] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405368] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405493] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405617] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405732] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405831] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.405927] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406022] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406114] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406201] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406289] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406374] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406457] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.406829] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.407171] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.407500] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.407780] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.408059] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.408336] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.408617] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.408911] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.409217] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.409574] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.409921] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.410239] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.410546] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.410852] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[11886.809033] Started restoring process of pasid 1
[11886.809930] Started evicting process of pasid 2
[11886.809931] Evicting PASID 2 queues
[11886.810619] Evicting PASID 2 queues
[11886.810637] Finished evicting process of pasid 2
[11886.811987] Restoring PASID 1 queues
[11886.811992] Restoring PASID 1 queues
[11886.811997] Finished restoring process of pasid 1
[11887.225036] Started restoring process of pasid 2
[11887.225553] Started evicting process of pasid 1
[11887.225555] Evicting PASID 1 queues
[11887.225576] Evicting PASID 1 queues
[11887.225945] Finished evicting process of pasid 1
[11887.227289] Restoring PASID 2 queues
[11887.227294] Restoring PASID 2 queues
[11887.227298] Finished restoring process of pasid 2
[11887.641040] Started restoring process of pasid 1
[11887.641537] Started evicting process of pasid 2
[11887.641539] Evicting PASID 2 queues
[11887.642211] Evicting PASID 2 queues
[11887.642226] Finished evicting process of pasid 2
[11887.643577] Restoring PASID 1 queues
[11887.643583] Restoring PASID 1 queues
[11887.643587] Finished restoring process of pasid 1
[11888.057044] Started restoring process of pasid 2
[11888.057553] Started evicting process of pasid 1
[11888.057555] Evicting PASID 1 queues
[11888.057573] Evicting PASID 1 queues
[11888.058863] Finished evicting process of pasid 1
[11888.060211] Restoring PASID 2 queues
[11888.060217] Restoring PASID 2 queues
[11888.060220] Finished restoring process of pasid 2
[11888.473047] Started restoring process of pasid 1
[11888.473418] Started evicting process of pasid 2
[11888.474108] Finished evicting process of pasid 2
[11888.475467] Restoring PASID 1 queues
[11888.475473] Restoring PASID 1 queues
[11888.475478] Finished restoring process of pasid 1
[11888.889052] Started restoring process of pasid 2
[11888.889551] Started evicting process of pasid 1
[11888.889945] Finished evicting process of pasid 1
[11888.891301] Finished restoring process of pasid 2
[11889.305057] Started restoring process of pasid 1
[11889.305549] Started evicting process of pasid 2
...
```

---

### 评论 #3 — preda (2017-11-03T22:05:43Z)

One thing to verify is that GPU selection is working correctly. If you run just one instance, in turn on GPU-0 and GPU-1, do you see the correct GPU heating up/spinning up?

If this works as expected, when you run the two instances at the same time, do *both* GPUs heat-up/spin up?


---

### 评论 #4 — nevion (2017-11-04T03:19:47Z)

Hm..  I used to have a problem like this on OpenCL on fglrx ~ 3 years ago and have been wondering how multi-GPU would work since then.  Actually I think the only other guy who noticed it at the time was a cryptominer for litecoin or something.  I had the problem in a laptop with an m290x crossfire. 

Have no way of testing this as of now, but figured it was worth mentioning since some bits may have been shared since the AMD App SDK days.

---

### 评论 #5 — lsimplify (2017-11-04T07:12:34Z)

> If you run just one instance, in turn on GPU-0 and GPU-1, do you see the correct GPU heating up/spinning up?

When I start one instance, both GPUs go from ~38W to  ~85W. Soon after the instance signifies the OpenCL kernels are compiled, the wattage of the correct GPU increases a lot more than the other GPU. I tried this in turn for Device 0 and Device 1. 

In case you're wondering why I didn't use temperature: 
- The temperatures are comparatively closer. 
- One card has poor airflow. (My second card's backplate is like a few centimeters away from the first's fans.) 
- The cards heat each other.
- Temperature changes gradually. Wattage changes starkly.

> If this works as expected, when you run the two instances at the same time, do both GPUs heat-up/spin up?

Yes. Cooley, the wattages "oscillate". I wish I could graph this to see whether the oscillations match up to the frequency of the **dmesg** message `Finished restoring process of pasid 1`. I mean---I think one GPU runs at a time---this is what I think I'm seeing. **I'll try to GIF what I'm seeing tomorrow. (:**

I don't have access to wattage when using the standard kernel and tools, but I can tell you that the ~51% performance decrease did not happen with the kernel I used before!

```
$ cat /usr/local/bin/card 
rocm-smi -tP | grep GPU | sort; dmesg |tail -1
```
`$ watch -pn.1 /usr/local/bin/card`
```
Every 10.0s: /usr/local/bin/card

GPU[0]          : Average GPU Power:    107.158 W
GPU[0]          : Temperature: 53.0c
GPU[1]          : Average GPU Power:    90.72 W
GPU[1]          : Temperature: 49.0c
[ 6295.258769] Finished restoring process of pasid 2
```

---

### 评论 #6 — lsimplify (2017-11-04T07:46:26Z)

I'll post more examples involving `xmr-stak-amd` and [vector_copy](https://github.com/RadeonOpenCompute/ROCm#verify-installation) in ~36h. ...

_OK. Here are more examples:_
**Second Example** causes a subset of the messages found in [First Example](https://github.com/RadeonOpenCompute/ROCm/issues/242#issuecomment-341809682).
**Third Example** causes messages I have not seen before. 

I followed the "Verify installation" instructions on the [ROCm page](https://github.com/RadeonOpenCompute/ROCm#verify-installation). The `vector_copy` program that results is used in both following Examples.

Both Examples still have `xmr-stak-amd` using 2 CPU threads for each Compute Device.

**Second Example**
_The first `xmr-stak-amd` is still running Device 0. I stopped the `xmr-stak-amd` running Device 1._
**Note: The **dmesg** messages did not happen when I stopped both `xmr-stak-amd` running Device 0 and Device 1---not even when the following command line had `./vector_copy&` 754 times.** 

I executed `vector_copy` with this command line: `$ ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy&`

```
[1]   Done                    ./vector_copy
[2]   Done                    ./vector_copy
[3]   Done                    ./vector_copy
[4]   Done                    ./vector_copy
[5]   Done                    ./vector_copy
[6]   Done                    ./vector_copy
[7]   Done                    ./vector_copy
[8]   Done                    ./vector_copy
[9]   Done                    ./vector_copy
[10]   Done                    ./vector_copy
[11]   Done                    ./vector_copy
[12]   Done                    ./vector_copy
[13]   Done                    ./vector_copy
[14]   Done                    ./vector_copy
[15]   Done                    ./vector_copy
[16]   Done                    ./vector_copy
[17]   Done                    ./vector_copy
[18]   Done                    ./vector_copy
[19]   Done                    ./vector_copy
[20]   Done                    ./vector_copy
[21]   Done                    ./vector_copy
[22]   Done                    ./vector_copy
[23]   Done                    ./vector_copy
[24]   Done                    ./vector_copy
[25]   Done                    ./vector_copy
[26]   Done                    ./vector_copy
[27]   Done                    ./vector_copy
[28]   Done                    ./vector_copy
[29]   Done                    ./vector_copy
[30]   Done                    ./vector_copy
[31]   Done                    ./vector_copy
[32]   Done                    ./vector_copy
[33]   Done                    ./vector_copy
[34]   Done                    ./vector_copy
[35]   Done                    ./vector_copy
[36]   Done                    ./vector_copy
[37]   Segmentation fault      ./vector_copy
[38]   Done                    ./vector_copy
[39]   Done                    ./vector_copy
[40]   Done                    ./vector_copy
[41]-  Done                    ./vector_copy
[42]+  Done                    ./vector_copy
```

**dmesg** logs that resulted:
```
[15104.644183] Started evicting process of pasid 1
[15104.644190] Evicting PASID 1 queues
[15104.644229] Evicting PASID 1 queues
[15104.645758] Finished evicting process of pasid 1
[15105.066752] Started restoring process of pasid 1
[15105.071114] Started evicting process of pasid 28
[15105.071116] Evicting PASID 28 queues
[15105.071143] Evicting PASID 28 queues
[15105.071175] Finished evicting process of pasid 28
[15105.071236] Started evicting process of pasid 29
[15105.071238] Evicting PASID 29 queues
[15105.071261] Evicting PASID 29 queues
[15105.071292] Finished evicting process of pasid 29
[15105.071302] Started evicting process of pasid 30
[15105.071303] Evicting PASID 30 queues
[15105.071327] Evicting PASID 30 queues
[15105.071375] Finished evicting process of pasid 30
[15105.071384] Started evicting process of pasid 31
[15105.071396] Evicting PASID 31 queues
[15105.071460] Evicting PASID 31 queues
[15105.071544] Finished evicting process of pasid 31
[15105.071553] Started evicting process of pasid 32
[15105.071628] Finished evicting process of pasid 32
[15105.071637] Started evicting process of pasid 33
[15105.071716] Finished evicting process of pasid 33
[15105.071726] Started evicting process of pasid 34
[15105.071799] Finished evicting process of pasid 34
[15105.071836] Started evicting process of pasid 35
[15105.071887] Finished evicting process of pasid 35
[15105.071925] Started evicting process of pasid 36
[15105.071982] Finished evicting process of pasid 36
[15105.072024] Started evicting process of pasid 37
[15105.072077] Finished evicting process of pasid 37
[15105.072118] Started evicting process of pasid 38
[15105.072173] Finished evicting process of pasid 38
[15105.072215] Started evicting process of pasid 39
[15105.072274] Finished evicting process of pasid 39
[15105.072308] Started evicting process of pasid 40
[15105.072361] Finished evicting process of pasid 40
[15105.072394] Started evicting process of pasid 41
[15105.072449] Finished evicting process of pasid 41
[15105.072453] Started evicting process of pasid 42
[15105.072539] Finished evicting process of pasid 42
[15105.072557] Started evicting process of pasid 25
[15105.072622] Finished evicting process of pasid 25
[15105.072934] Started evicting process of pasid 43
[15105.072989] Finished evicting process of pasid 43
[15105.073284] Started evicting process of pasid 24
[15105.074962] Finished evicting process of pasid 24
[15105.076287] Restoring PASID 1 queues
[15105.076320] Restoring PASID 1 queues
[15105.076348] Finished restoring process of pasid 1
[15105.103951] Started evicting process of pasid 1
[15105.104662] Finished evicting process of pasid 1
[15105.482791] Started restoring process of pasid 24
[15105.482917] Started restoring process of pasid 43
[15105.482979] Restoring PASID 43 queues
[15105.482998] Restoring PASID 43 queues
[15105.483016] Finished restoring process of pasid 43
[15105.483017] Started restoring process of pasid 42
[15105.483073] Restoring PASID 42 queues
[15105.483103] Restoring PASID 42 queues
[15105.483167] Finished restoring process of pasid 42
[15105.483168] Started restoring process of pasid 41
[15105.483224] Restoring PASID 41 queues
[15105.483266] Restoring PASID 41 queues
[15105.483269] Restoring PASID 24 queues
[15105.483348] Finished restoring process of pasid 41
[15105.483350] Restoring PASID 24 queues
[15105.483449] Finished restoring process of pasid 24
[15105.483449] Started restoring process of pasid 40
[15105.483603] Finished restoring process of pasid 40
[15105.483604] Started restoring process of pasid 39
[15105.483763] Finished restoring process of pasid 39
[15105.483764] Started restoring process of pasid 38
[15105.483943] Finished restoring process of pasid 38
[15105.483944] Started restoring process of pasid 37
[15105.484125] Finished restoring process of pasid 37
[15105.484126] Started restoring process of pasid 36
[15105.484344] Finished restoring process of pasid 36
[15105.484344] Started restoring process of pasid 35
[15105.484539] Finished restoring process of pasid 35
[15105.484539] Started restoring process of pasid 34
[15105.484720] Finished restoring process of pasid 34
[15105.484721] Started restoring process of pasid 33
[15105.484911] Finished restoring process of pasid 33
[15105.484913] Started restoring process of pasid 32
[15105.485143] Finished restoring process of pasid 32
[15105.485144] Started restoring process of pasid 31
[15105.485381] Finished restoring process of pasid 31
[15105.485382] Started restoring process of pasid 30
[15105.485623] Finished restoring process of pasid 30
[15105.485624] Started restoring process of pasid 29
[15105.485856] Finished restoring process of pasid 29
[15105.485857] Started restoring process of pasid 28
[15105.486064] Finished restoring process of pasid 28
[15105.498781] Started evicting process of pasid 24
[15105.498901] Finished evicting process of pasid 24
[15105.499226] Started evicting process of pasid 42
[15105.499332] Finished evicting process of pasid 42
[15105.499658] Started evicting process of pasid 41
[15105.499764] Finished evicting process of pasid 41
[15105.500269] Started evicting process of pasid 39
[15105.500362] Finished evicting process of pasid 39
[15105.500516] Started evicting process of pasid 38
[15105.500593] Finished evicting process of pasid 38
[15105.500691] Started evicting process of pasid 37
[15105.500767] Finished evicting process of pasid 37
[15105.501517] Started evicting process of pasid 43
[15105.501599] Finished evicting process of pasid 43
[15105.501912] Started evicting process of pasid 40
[15105.501987] Finished evicting process of pasid 40
[15105.502306] Started evicting process of pasid 34
[15105.502369] Finished evicting process of pasid 34
[15105.502403] Started evicting process of pasid 35
[15105.502480] Finished evicting process of pasid 35
[15105.503250] Started evicting process of pasid 28
[15105.503316] Finished evicting process of pasid 28
[15105.508204] ------------[ cut here ]------------
[15105.508265] WARNING: CPU: 3 PID: 8894 at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu_object.c:1030 amdgpu_bo_gpu_offset+0xf5/0x160 [amdgpu]
[15105.508266] Modules linked in: nls_iso8859_1 dm_crypt edac_mce_amd edac_core kvm_amd snd_hda_codec_realtek snd_hda_codec_generic kvm snd_hda_codec_hdmi irqbypass snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep i2c_piix4 ccp snd_pcm snd_timer snd soundcore mac_hid i2c_designware_platform 8250_dw i2c_designware_core shpchp ib_iser rdma_cm iw_cm ib_cm ib_core configfs iscsi_tcp libiscsi_tcp libiscsi scsi_transport_iscsi ip_tables x_tables autofs4 btrfs raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear amdkfd amd_iommu_v2 crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc amdgpu mxm_wmi ttm aesni_intel drm_kms_helper syscopyarea igb aes_x86_64 crypto_simd glue_helper sysfillrect cryptd sysimgblt dca fb_sys_fops drm ptp
[15105.508319]  ahci pps_core libahci i2c_algo_bit gpio_amdpt wmi gpio_generic
[15105.508327] CPU: 3 PID: 8894 Comm: vector_copy Not tainted 4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[15105.508328] Hardware name: Micro-Star International Co., Ltd MS-7A32/X370 GAMING PRO CARBON (MS-7A32), BIOS 1.97 09/20/2017
[15105.508330] Call Trace:
[15105.508336]  dump_stack+0x63/0x90
[15105.508340]  __warn+0xcb/0xf0
[15105.508342]  warn_slowpath_null+0x1d/0x20
[15105.508395]  amdgpu_bo_gpu_offset+0xf5/0x160 [amdgpu]
[15105.508452]  amdgpu_vm_update_ptes+0x290/0x380 [amdgpu]
[15105.508507]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.508562]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.508617]  ? amdgpu_sync_fence+0x90/0x140 [amdgpu]
[15105.508671]  amdgpu_vm_frag_ptes+0x11b/0x130 [amdgpu]
[15105.508726]  ? amdgpu_sync_resv+0xc8/0x170 [amdgpu]
[15105.508781]  amdgpu_vm_bo_update_mapping+0x2e7/0x3c0 [amdgpu]
[15105.508836]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.508889]  amdgpu_vm_clear_freed+0x81/0x140 [amdgpu]
[15105.508949]  unmap_bo_from_gpuvm.isra.13+0x69/0xd0 [amdgpu]
[15105.509008]  amdgpu_amdkfd_gpuvm_unmap_memory_from_gpu+0x189/0x2c0 [amdgpu]
[15105.509020]  kfd_unmap_memory_from_gpu+0x31/0x60 [amdkfd]
[15105.509030]  kfd_ioctl_unmap_memory_from_gpu+0x12a/0x1c0 [amdkfd]
[15105.509040]  kfd_ioctl+0x241/0x3f0 [amdkfd]
[15105.509049]  ? kfd_unmap_memory_from_gpu+0x60/0x60 [amdkfd]
[15105.509052]  ? apparmor_mmap_file+0x18/0x20
[15105.509056]  do_vfs_ioctl+0x92/0x5a0
[15105.509058]  SyS_ioctl+0x79/0x90
[15105.509061]  entry_SYSCALL_64_fastpath+0x1e/0xad
[15105.509063] RIP: 0033:0x7f837fd4dea7
[15105.509064] RSP: 002b:00007ffda5eecba8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[15105.509067] RAX: ffffffffffffffda RBX: 0000558a3689fe80 RCX: 00007f837fd4dea7
[15105.509068] RDX: 00007ffda5eecc00 RSI: 00000000c0184b14 RDI: 0000000000000003
[15105.509069] RBP: 00007ffda5eecd20 R08: 00007f837fc3b2f0 R09: 0000000000001000
[15105.509071] R10: 0000000000004032 R11: 0000000000000246 R12: 0000000040084b0a
[15105.509072] R13: 0000000000000003 R14: 0000000000000000 R15: 0000000000000000
[15105.509074] ---[ end trace ac9cdb4ddfa8e912 ]---
[15105.509075] ------------[ cut here ]------------
[15105.509128] WARNING: CPU: 3 PID: 8894 at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu_object.c:1033 amdgpu_bo_gpu_offset+0x14f/0x160 [amdgpu]
[15105.509128] Modules linked in: nls_iso8859_1 dm_crypt edac_mce_amd edac_core kvm_amd snd_hda_codec_realtek snd_hda_codec_generic kvm snd_hda_codec_hdmi irqbypass snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep i2c_piix4 ccp snd_pcm snd_timer snd soundcore mac_hid i2c_designware_platform 8250_dw i2c_designware_core shpchp ib_iser rdma_cm iw_cm ib_cm ib_core configfs iscsi_tcp libiscsi_tcp libiscsi scsi_transport_iscsi ip_tables x_tables autofs4 btrfs raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear amdkfd amd_iommu_v2 crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc amdgpu mxm_wmi ttm aesni_intel drm_kms_helper syscopyarea igb aes_x86_64 crypto_simd glue_helper sysfillrect cryptd sysimgblt dca fb_sys_fops drm ptp
[15105.509173]  ahci pps_core libahci i2c_algo_bit gpio_amdpt wmi gpio_generic
[15105.509179] CPU: 3 PID: 8894 Comm: vector_copy Tainted: G        W       4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[15105.509180] Hardware name: Micro-Star International Co., Ltd MS-7A32/X370 GAMING PRO CARBON (MS-7A32), BIOS 1.97 09/20/2017
[15105.509181] Call Trace:
[15105.509184]  dump_stack+0x63/0x90
[15105.509186]  __warn+0xcb/0xf0
[15105.509188]  warn_slowpath_null+0x1d/0x20
[15105.509240]  amdgpu_bo_gpu_offset+0x14f/0x160 [amdgpu]
[15105.509293]  amdgpu_vm_update_ptes+0x290/0x380 [amdgpu]
[15105.509347]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.509400]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.509454]  ? amdgpu_sync_fence+0x90/0x140 [amdgpu]
[15105.509507]  amdgpu_vm_frag_ptes+0x11b/0x130 [amdgpu]
[15105.509561]  ? amdgpu_sync_resv+0xc8/0x170 [amdgpu]
[15105.509614]  amdgpu_vm_bo_update_mapping+0x2e7/0x3c0 [amdgpu]
[15105.509667]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.509721]  amdgpu_vm_clear_freed+0x81/0x140 [amdgpu]
[15105.509779]  unmap_bo_from_gpuvm.isra.13+0x69/0xd0 [amdgpu]
[15105.509837]  amdgpu_amdkfd_gpuvm_unmap_memory_from_gpu+0x189/0x2c0 [amdgpu]
[15105.509848]  kfd_unmap_memory_from_gpu+0x31/0x60 [amdkfd]
[15105.509858]  kfd_ioctl_unmap_memory_from_gpu+0x12a/0x1c0 [amdkfd]
[15105.509868]  kfd_ioctl+0x241/0x3f0 [amdkfd]
[15105.509877]  ? kfd_unmap_memory_from_gpu+0x60/0x60 [amdkfd]
[15105.509879]  ? apparmor_mmap_file+0x18/0x20
[15105.509882]  do_vfs_ioctl+0x92/0x5a0
[15105.509885]  SyS_ioctl+0x79/0x90
[15105.509887]  entry_SYSCALL_64_fastpath+0x1e/0xad
[15105.509888] RIP: 0033:0x7f837fd4dea7
[15105.509889] RSP: 002b:00007ffda5eecba8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[15105.509891] RAX: ffffffffffffffda RBX: 0000558a3689fe80 RCX: 00007f837fd4dea7
[15105.509893] RDX: 00007ffda5eecc00 RSI: 00000000c0184b14 RDI: 0000000000000003
[15105.509894] RBP: 00007ffda5eecd20 R08: 00007f837fc3b2f0 R09: 0000000000001000
[15105.509895] R10: 0000000000004032 R11: 0000000000000246 R12: 0000000040084b0a
[15105.509896] R13: 0000000000000003 R14: 0000000000000000 R15: 0000000000000000
[15105.509898] ---[ end trace ac9cdb4ddfa8e913 ]---
[15105.509914] ------------[ cut here ]------------
[15105.510199] kernel BUG at /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.6/kernel/drivers/gpu/drm/amd/amdgpu/gmc_v8_0.c:640!
[15105.510832] Started evicting process of pasid 36
[15105.510899] Finished evicting process of pasid 36
[15105.512118] Started evicting process of pasid 32
[15105.512178] Finished evicting process of pasid 32
[15105.513382] invalid opcode: 0000 [#1] SMP
[15105.514032] Modules linked in: nls_iso8859_1 dm_crypt edac_mce_amd edac_core kvm_amd snd_hda_codec_realtek snd_hda_codec_generic kvm snd_hda_codec_hdmi irqbypass snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep i2c_piix4 ccp snd_pcm snd_timer snd soundcore mac_hid i2c_designware_platform 8250_dw i2c_designware_core shpchp ib_iser rdma_cm iw_cm ib_cm ib_core configfs iscsi_tcp libiscsi_tcp libiscsi scsi_transport_iscsi ip_tables x_tables autofs4 btrfs raid10 raid456 async_raid6_recov async_memcpy async_pq async_xor async_tx xor raid6_pq libcrc32c raid1 raid0 multipath linear amdkfd amd_iommu_v2 crct10dif_pclmul crc32_pclmul ghash_clmulni_intel pcbc amdgpu mxm_wmi ttm aesni_intel drm_kms_helper syscopyarea igb aes_x86_64 crypto_simd glue_helper sysfillrect cryptd sysimgblt dca fb_sys_fops drm ptp
[15105.514790] Started restoring process of pasid 1
[15105.522077]  ahci pps_core libahci i2c_algo_bit gpio_amdpt wmi gpio_generic
[15105.523437] CPU: 3 PID: 8894 Comm: vector_copy Tainted: G        W       4.11.0-kfd-compute-rocm-rel-1.6-180 #1
[15105.525024] Hardware name: Micro-Star International Co., Ltd MS-7A32/X370 GAMING PRO CARBON (MS-7A32), BIOS 1.97 09/20/2017
[15105.526792] task: ffff942d4a8f4600 task.stack: ffffbc68cf530000
[15105.528752] RIP: 0010:gmc_v8_0_get_vm_pde+0x1d/0x20 [amdgpu]
[15105.530635] RSP: 0018:ffffbc68cf5339f8 EFLAGS: 00010286
[15105.534197] RAX: ffffff0000000fff RBX: ffffbc68cf533b40 RCX: ffffffffc08cb1c0
[15105.535949] RDX: 0000000000000007 RSI: fffffffffffff000 RDI: ffff942e4f9d0000
[15105.536739] RBP: ffffbc68cf5339f8 R08: 0000000000000001 R09: 0000000000009be3
[15105.538792] R10: 0000000000000000 R11: 0000000000009be3 R12: ffffbc68cf533b40
[15105.541588] R13: ffff942db69e1640 R14: ffffbc68cfc34400 R15: 0000000000a01000
[15105.543978] FS:  00007f83804d8780(0000) GS:ffff942e5e6c0000(0000) knlGS:0000000000000000
[15105.545988] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[15105.547959] CR2: 00007f837c9e06a0 CR3: 000000079eb63000 CR4: 00000000003406e0
[15105.550040] Call Trace:
[15105.551055]  amdgpu_vm_update_ptes+0x2a1/0x380 [amdgpu]
[15105.553308]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.555677]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.558016]  ? amdgpu_sync_fence+0x90/0x140 [amdgpu]
[15105.560473]  amdgpu_vm_frag_ptes+0x11b/0x130 [amdgpu]
[15105.562750]  ? amdgpu_sync_resv+0xc8/0x170 [amdgpu]
[15105.564085]  amdgpu_vm_bo_update_mapping+0x2e7/0x3c0 [amdgpu]
[15105.566504]  ? amdgpu_vm_alloc_levels.isra.16+0x320/0x320 [amdgpu]
[15105.569062]  amdgpu_vm_clear_freed+0x81/0x140 [amdgpu]
[15105.571565]  unmap_bo_from_gpuvm.isra.13+0x69/0xd0 [amdgpu]
[15105.574039]  amdgpu_amdkfd_gpuvm_unmap_memory_from_gpu+0x189/0x2c0 [amdgpu]
[15105.576270]  kfd_unmap_memory_from_gpu+0x31/0x60 [amdkfd]
[15105.578037]  kfd_ioctl_unmap_memory_from_gpu+0x12a/0x1c0 [amdkfd]
[15105.580931]  kfd_ioctl+0x241/0x3f0 [amdkfd]
[15105.583777]  ? kfd_unmap_memory_from_gpu+0x60/0x60 [amdkfd]
[15105.586677]  ? apparmor_mmap_file+0x18/0x20
[15105.589642]  do_vfs_ioctl+0x92/0x5a0
[15105.591297]  SyS_ioctl+0x79/0x90
[15105.593848]  entry_SYSCALL_64_fastpath+0x1e/0xad
[15105.596332] RIP: 0033:0x7f837fd4dea7
[15105.598783] RSP: 002b:00007ffda5eecba8 EFLAGS: 00000246 ORIG_RAX: 0000000000000010
[15105.601319] RAX: ffffffffffffffda RBX: 0000558a3689fe80 RCX: 00007f837fd4dea7
[15105.602909] RDX: 00007ffda5eecc00 RSI: 00000000c0184b14 RDI: 0000000000000003
[15105.605650] RBP: 00007ffda5eecd20 R08: 00007f837fc3b2f0 R09: 0000000000001000
[15105.608502] R10: 0000000000004032 R11: 0000000000000246 R12: 0000000040084b0a
[15105.611247] R13: 0000000000000003 R14: 0000000000000000 R15: 0000000000000000
[15105.613680] Code: 93 c0 e8 37 45 da ed 5b 31 c0 41 5c 5d c3 0f 1f 44 00 00 55 48 b8 ff 0f 00 00 00 ff ff ff 48 85 c6 48 89 e5 75 05 48 89 f0 5d c3 <0f> 0b 90 0f 1f 44 00 00 83 3d d4 7e 1b 00 02 74 14 55 48 8d b7 
[15105.617641] RIP: gmc_v8_0_get_vm_pde+0x1d/0x20 [amdgpu] RSP: ffffbc68cf5339f8
[15105.629049] ---[ end trace ac9cdb4ddfa8e914 ]---
[15105.930817] Started restoring process of pasid 32
[15105.934823] Started restoring process of pasid 36
[15105.937836] Started restoring process of pasid 28
[15105.942824] Started restoring process of pasid 35
[15105.946819] Started restoring process of pasid 34
[15105.948367] Finished restoring process of pasid 34
[15105.949459] Started restoring process of pasid 40
[15105.952501] Started restoring process of pasid 43
[15105.954865] Started restoring process of pasid 37
[15105.958819] Started restoring process of pasid 38
[15105.960404] Finished restoring process of pasid 38
[15105.961422] Started restoring process of pasid 39
[15105.966826] Started restoring process of pasid 41
[15105.970835] Started restoring process of pasid 42
[15106.170009] Finished restoring process of pasid 32
[15106.170675] Finished restoring process of pasid 36
[15106.171756] Finished restoring process of pasid 28
[15106.172793] Finished restoring process of pasid 35
[15106.173729] Finished restoring process of pasid 40
[15106.175153] Finished restoring process of pasid 37
[15106.176135] Finished restoring process of pasid 43
[15106.177160] Finished restoring process of pasid 42
[15106.178074] Finished restoring process of pasid 41
[15106.482713] Finished restoring process of pasid 39
[15107.285371] Finished restoring process of pasid 1
```
**End of Second Example**

**Start of Third Example**

_I stopped `xmr-stak-amd` on Device 0 and started `xmr-stak-amd` on Device 1._

Upon starting `xmr-stak-amd` on Device 1, I saw this in **dmesg**:
```
[18263.115703] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.117111] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.118797] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.120340] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.121655] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.123230] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.124640] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.125860] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.126231] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.127331] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.128146] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.128416] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.129242] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.130085] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.131054] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.132012] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.132877] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.133730] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.134570] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.135488] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.136291] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.137083] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.137872] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.138625] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.139433] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.140161] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.140875] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.141569] kfd2kgd: Failed to create BO on domain VRAM. ret -12
[18263.142151] kfd2kgd: Failed to create BO on domain VRAM. ret -12
```

I ran this `./vector_copy` command line: `$./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy& ./vector_copy&`

I checked **dmesg** and I saw an error message I have not seen before... 1000+ of them:
```
[18361.872850] Started restoring process of pasid 13
[18361.873844] kfd2kgd: amdgpu: failed to validate PT BOs
[18361.874793] Restore failed, try again after 100 ms
[18361.875770] Started restoring process of pasid 22
[18361.876742] kfd2kgd: amdgpu: failed to validate PT BOs
[18361.877685] Restore failed, try again after 100 ms
[18361.878638] Started restoring process of pasid 21
[18361.879581] kfd2kgd: amdgpu: failed to validate PT BOs
[18361.880549] Restore failed, try again after 100 ms
[18361.881501] Started restoring process of pasid 16
[18361.882124] kfd2kgd: amdgpu: failed to validate PT BOs
[18361.883132] Restore failed, try again after 100 ms
[18361.904851] Started restoring process of pasid 25
[18361.905867] kfd2kgd: amdgpu: failed to validate PT BOs
[18361.906823] Restore failed, try again after 100 ms
[18362.256860] Started restoring process of pasid 26
[18362.257875] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.258528] Restore failed, try again after 100 ms
[18362.259429] Started restoring process of pasid 15
[18362.260382] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.261366] Restore failed, try again after 100 ms
[18362.262347] Started restoring process of pasid 12
[18362.263284] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.264215] Restore failed, try again after 100 ms
[18362.265181] Started restoring process of pasid 17
[18362.266124] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.267054] Restore failed, try again after 100 ms
[18362.288861] Started restoring process of pasid 16
[18362.289867] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.290834] Restore failed, try again after 100 ms
[18362.291776] Started restoring process of pasid 21
[18362.292745] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.293690] Restore failed, try again after 100 ms
[18362.294644] Started restoring process of pasid 22
[18362.295617] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.296600] Restore failed, try again after 100 ms
[18362.297580] Started restoring process of pasid 13
[18362.298421] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.299211] Restore failed, try again after 100 ms
[18362.320860] Started restoring process of pasid 25
[18362.321861] kfd2kgd: amdgpu: failed to validate PT BOs
[18362.322800] Restore failed, try again after 100 ms
```
Minutes have passed... maybe 100 ...and these ^^^ messages are still coming. 

`ps` shows `vector_copy` 84 times. One is defunct. I read `top` and see four have ~100% CPU utilization.
`ps` shows `xmr-stak-amd` 1 time. I checked it's performance: zero results per second 
I asked systemd to stop `xmr-stak-amd` on Device 1 (it stops it manually with control signals). Now `xmr-stak-amd` is defunct.
I tried to manually start `xmr-stak-amd` on Device 0... and the output that signifies that it built the kernels doesn't even appear. 

---

### 评论 #7 — rhlug (2017-11-04T19:10:18Z)

I have 2 vega 56's both mining eth, I dont see any drop on 2nd GPU.   Both are in x16 slots ATM.

```
# rates
Screen #0
           Speed: (5s):40.03M (avg):39.87Mh/s | A:40000000000  R:0  HW:20  WU:40.993
           Speed: (5s):40.03M (avg):39.87Mh/s | A:40000000000  R:0  HW:20  WU:40.766
Screen #1
           Speed: (5s):40.87M (avg):39.88Mh/s | A:20000000000  R:0  HW:17  WU:41.761
           Speed: (5s):40.54M (avg):39.88Mh/s | A:20000000000  R:0  HW:17  WU:41.807

# cat /sys/class/drm/card*/device/pp_dpm_sclk | grep \*
1: 991Mhz *
1: 991Mhz *
# cat /sys/class/drm/card*/device/pp_dpm_mclk | grep \*
3: 1020Mhz *
3: 1020Mhz *
```

---

### 评论 #8 — lsimplify (2017-11-14T08:39:22Z)

I lowered the intensity a little and found a sweet spot. Also, I'm using xmr-stak instead of xmr-stak-amd, but I hadn't thought (or checked) if it fixes this oddity that my posts were regarding.

With the lower intensity, no longer does starting one cause the other's hashrate to decrease. **Anyone have a clue on the existence of this oddity?**

The cards up-time is 36 hours. 

The cards are overclocked in firmware __and__ with rocm-smi. I think it is remarkable that these two cards didn't have any compute errors (xmr-stak lists this information) or "<?VM.>.*.mem< ^access!fault<..FE x007820<<<" **dmesg** errors. That tool is so useful and I love the program's interface. Thank you! You are helping me run my cards mad. ;) but in a good way.

These numbers were copied from the webpage after an up-time of 36 hours when both were running:
GPU0 or (a)
Thread ID	10s	60s	15m	H/s
0		        1027.7	1029.8	1030.0
Totals:		1027.7	1029.8	1030.0
Highest:	        1036.6

GPU1 or (b)
Thread ID	10s	60s	15m	H/s
0		        1009.3	1008.0	1008.2
Totals:		1009.3	1008.0	1008.2
Highest:	        1011.7	

@rhlug Do you want to try increasing the intensity in the config for one ..or both cards and then running them and checking dmesg, etc. I'm wondering if setting "higher" intensities reproduces the same error messages.... or at least a slow down **on the other card** in general.

---

### 评论 #9 — rhlug (2017-11-14T22:43:24Z)

@rhlug Not really sure, havent been messing with vega on linux because I cant undervolt them easily.

When I did run xmr-stak-amd on ubuntu 16.04 with vega 56 (flashed to 64), I was getting 1300 h/s @ 2016/1600 intensities.

I dont have things setup to do any experiments right now.  Maybe for ROCm 1.7 I will.

---

### 评论 #10 — lsimplify (2018-02-18T03:55:56Z)

Even though I don't have an answer to why only one card was used at a time (I described this above), I'm closing this issue because this issue goes away when I decrease the intensity number like I stated in an above post.

---
