# rocminfo leads to OOP

- **Issue #:** 876
- **State:** closed
- **Created:** 2019-08-26T20:18:26Z
- **Updated:** 2023-08-05T18:26:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/876

Hi,
Using rocm-dev from debian/ubuntu official repository (thus, with mainline debian buster kernel) leads to OOP while trying to get rocminfo. if i try to run it again, the process simply get's "stuck" (the same applies to clinfo, etc...) 

System is debian buster, with all packages up-to-date, on a RX560, seen by lspci as

`01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X] (rev e5)`

lspci -vvv:

```
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X] (rev e5) (prog-if 00 [VGA controller])
	Subsystem: Sapphire Technology Limited Baffin [Radeon RX 460/560D / Pro 450/455/460/555/555X/560/560X]
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 31
	NUMA node: 0
	Region 0: Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at d0000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at fe900000 (32-bit, non-prefetchable) [size=256K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```


uname -a:
`Linux munch 4.19.0-5-amd64 #1 SMP Debian 4.19.37-5+deb10u2 (2019-08-08) x86_64 GNU/Linux`

dkms status:
```
amdgpu, 2.7-22, 4.19.0-5-amd64, amd64: installed
openrazer-driver, 2.6.0, 4.19.0-5-amd64, x86_64: installed
```

lsmod | grep amdgpu:

```
amdgpu               4284416  21
amdttm                114688  1 amdgpu
amd_sched              32768  1 amdgpu
amdkcl                 32768  3 amd_sched,amdttm,amdgpu
i2c_algo_bit           16384  1 amdgpu
drm_kms_helper        200704  1 amdgpu
drm                   483328  10 drm_kms_helper,amd_sched,amdttm,amdgpu,amdkcl
```

Dmesg as an attachment
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/3542758/dmesg.txt)


Could you please help me to solve this?
TIA
