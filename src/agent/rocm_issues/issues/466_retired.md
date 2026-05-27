# retired...

> **Issue #466**
> **状态**: closed
> **创建时间**: 2018-07-24T17:48:37Z
> **更新时间**: 2018-08-19T16:31:21Z
> **关闭时间**: 2018-08-19T16:31:21Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/466

## 描述

*(无描述)*

---

## 评论 (14 条)

### 评论 #1 — PNixx (2018-07-26T17:34:00Z)

Ubuntu 18.04.
```
amdgpu-pro-17.50-511655/amdgpu-install --headless --opencl=legacy
*****
Building for 4.18.0-rc5
Building for architecture x86_64
Building initial module for 4.18.0-rc5
ERROR (dkms apport): kernel package linux-headers-4.18.0-rc5 is not supported
Error! Bad return status for module build on kernel: 4.18.0-rc5 (x86_64)
```

---

### 评论 #2 — PNixx (2018-07-26T17:45:17Z)

Not working for me. I see log `/var/lib/dkms/amdgpu/17.50-511655/build/make.log`. Do you help me?
```
DKMS make.log for amdgpu-17.50-511655 for kernel 4.18.0-rc5 (x86_64)
Чт июл 26 20:43:29 MSK 2018
make: вход в каталог «/usr/src/linux-headers-4.18.0-rc5»
make[2]: *** Нет правила для сборки цели «/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdkcl/kcl_drm.o», требуемой для «/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdkcl/amdkcl.o».  Останов.
make[2]: *** Ожидание завершения заданий…
scripts/Makefile.build:581: recipe for target '/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdkcl' failed
make[1]: *** [/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdkcl] Error 2
make[1]: *** Ожидание завершения заданий…
make[2]: *** Нет правила для сборки цели «/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdgpu/amdgpu_drv.o», требуемой для «/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdgpu/amdgpu.o».  Останов.
make[2]: *** Ожидание завершения заданий…
scripts/Makefile.build:581: recipe for target '/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdgpu' failed
make[1]: *** [/var/lib/dkms/amdgpu/17.50-511655/build/amd/amdgpu] Error 2
Makefile:1529: recipe for target '_module_/var/lib/dkms/amdgpu/17.50-511655/build' failed
make: *** [_module_/var/lib/dkms/amdgpu/17.50-511655/build] Error 2
make: выход из каталога «/usr/src/linux-headers-4.18.0-rc5»
```

---

### 评论 #3 — PNixx (2018-07-26T17:53:09Z)

```
$ dmesg | grep BOOT
[    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.18.0-rc5 root=/dev/mapper/farm2--vg-root ro net.ifnames=0 biosdevname=0 quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram vt.handoff=1
[    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.18.0-rc5 root=/dev/mapper/farm2--vg-root ro net.ifnames=0 biosdevname=0 quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram vt.handoff=1
```
I run tdxminer, but I see:
```
             tdxminer version 0.2.2.2
  This is a beta release and may be unstable on some hardware.
[2018-07-26 20:51:10] Failed to list OpenCL platforms.
```

---

### 评论 #4 — ghost (2018-07-26T17:55:32Z)

Also since its not running live off the usb you may have issues.

On Fri, Jul 27, 2018 at 1:54 AM, Jason Kurtz <tekcommnv@gmail.com> wrote:

> lspci -v
> Please
> and
> clinfo
>
>
> On Fri, Jul 27, 2018 at 1:53 AM, Sergey Odintsov <notifications@github.com
> > wrote:
>
>> $ dmesg | grep BOOT
>> [    0.000000] Command line: BOOT_IMAGE=/vmlinuz-4.18.0-rc5 root=/dev/mapper/farm2--vg-root ro net.ifnames=0 biosdevname=0 quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram vt.handoff=1
>> [    0.000000] Kernel command line: BOOT_IMAGE=/vmlinuz-4.18.0-rc5 root=/dev/mapper/farm2--vg-root ro net.ifnames=0 biosdevname=0 quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off toram vt.handoff=1
>>
>> I run tdxminer, but I see:
>>
>>              tdxminer version 0.2.2.2
>>   This is a beta release and may be unstable on some hardware.
>> [2018-07-26 20:51:10] Failed to list OpenCL platforms.
>>
>> —
>> You are receiving this because you authored the thread.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/RadeonOpenCompute/ROCm/issues/466#issuecomment-408180730>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AWn0w8UHJT2lqzFiNDATUJ1eLDwwxJ67ks5uKgIJgaJpZM4VdLlV>
>> .
>>
>
>


---

### 评论 #5 — PNixx (2018-07-26T18:00:27Z)

```
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega [Radeon RX Vega] (rev c3) (prog-if 00 [VGA controller])
	Subsystem: Gigabyte Technology Co., Ltd Vega 10 XT [Radeon RX Vega 64]
	Flags: bus master, fast devsel, latency 0, IRQ 33
	Memory at c0000000 (64-bit, prefetchable) [size=256M]
	Memory at d0000000 (64-bit, prefetchable) [size=2M]
	I/O ports at e000 [size=256]
	Memory at fe500000 (32-bit, non-prefetchable) [size=512K]
	Expansion ROM at 000c0000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```
$ /opt/amdgpu-pro/bin/clinfo
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs

---

### 评论 #6 — PNixx (2018-07-26T19:15:47Z)

Last log:
```
close(6)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/tls/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/tls", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64-linux-gnu", {st_mode=S_IFDIR|0755, st_size=16384, ...}) = 0
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/tls/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/tls", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64-linux-gnu", {st_mode=S_IFDIR|0755, st_size=61440, ...}) = 0
openat(AT_FDCWD, "/lib/tls/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/tls/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/tls", 0x7ffc4086ade0)        = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64", 0x7ffc4086ade0)     = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib/x86_64", 0x7ffc4086ade0)     = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
openat(AT_FDCWD, "/usr/lib/tls/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/tls/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/tls/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/tls", 0x7ffc4086ade0)    = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib/x86_64", 0x7ffc4086ade0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/usr/lib", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
munmap(0x7fcc9e157000, 79431)           = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 6
fstat(6, {st_mode=S_IFREG|0644, st_size=79431, ...}) = 0
mmap(NULL, 79431, PROT_READ, MAP_PRIVATE, 6, 0) = 0x7fcc9e157000
close(6)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libamdoclsc64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libamdoclsc64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/libamdoclsc64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/libamdoclsc64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7fcc9e157000, 79431)           = 0
openat(AT_FDCWD, "./amdoclsc64", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "./libamdoclsc64.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
munmap(0x7fcc9860d000, 74831768)        = 0
close(4)                                = 0
getdents(3, /* 0 entries */, 32768)     = 0
close(3)                                = 0
futex(0x7fcc9d7994d8, FUTEX_WAKE_PRIVATE, 2147483647) = 0
futex(0x7fcc9d5921a0, FUTEX_WAKE_PRIVATE, 2147483647) = 0
write(2, "terminate called after throwing "..., 48) = 48
write(2, "cl::Error", 9)                = 9
write(2, "'\n", 2)                      = 2
write(2, "  what():  ", 11)             = 11
write(2, "clGetPlatformIDs", 16)        = 16
write(2, "\n", 1)                       = 1
rt_sigprocmask(SIG_UNBLOCK, [ABRT], NULL, 8) = 0
rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1], [], 8) = 0
getpid()                                = 1132
gettid()                                = 1132
tgkill(1132, 1132, SIGABRT)             = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
--- SIGABRT {si_signo=SIGABRT, si_code=SI_TKILL, si_pid=1132, si_uid=1000} ---
+++ killed by SIGABRT (core dumped) +++
```

---

### 评论 #7 — securitizones (2018-07-28T06:47:16Z)

Do you apply these patches to v3. If so how does it update the image on the v3 usb stick. Can you apply this to a standard 18.04 install. 

---

### 评论 #8 — securitizones (2018-07-28T08:23:48Z)

Hi doc. I still can't make it work. How can I apply these changes to a live V2 or v3 and reboot as the kernel is updated as its a live usb and does not retain any of the kernel updates. Please please help me , do I have to install to disk or do something else to install these kernels and reboot to keep the changes.

---

### 评论 #9 — Rocket31337 (2018-07-28T18:44:57Z)

I'm having issues with mine... Any tips?

root@miner4:~# rocm-smi 


====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   19.0c   5.0W     1663Mhz  167Mhz   36.86%   manual    4%       
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================

05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c3) (prog-if 00 [VGA controller])
        Subsystem: Device 1da2:e376
        Flags: bus master, fast devsel, latency 0, IRQ 135
        Memory at 2000000000 (64-bit, prefetchable) [size=8G]
        Memory at 2200000000 (64-bit, prefetchable) [size=2M]
        I/O ports at e000 [size=256]
        Memory at f7c00000 (32-bit, non-prefetchable) [size=512K]
        Expansion ROM at f7c80000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [64] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
        Capabilities: [150] Advanced Error Reporting
        Capabilities: [200] #15
        Capabilities: [270] #19
        Capabilities: [2a0] Access Control Services
        Capabilities: [2b0] Address Translation Service (ATS)
        Capabilities: [2c0] #13
        Capabilities: [2d0] #1b
        Capabilities: [320] Latency Tolerance Reporting
        Kernel driver in use: amdgpu
        Kernel modules: amdgpu

./clinfo 
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)



---

### 评论 #10 — PNixx (2018-07-29T11:45:05Z)

> Here is a installer to use if you install V5 or ubuntu 16.x & 18.x via the install to usb :)

This installer for linux-image-4.18.0-rc5 kernel?

---

### 评论 #11 — ghost (2018-07-31T21:23:15Z)

Added 550 support


---

### 评论 #12 — Hackintoshihope (2018-08-05T21:57:25Z)

Voltage and power consumption does not change with these patches. At the wall measured with a watt meter power consumption is stuck at 300W per card no matter the voltage setting. Did not know is this expected behavior or if Vega support is still in beta?

---

### 评论 #13 — emerzon (2018-08-18T08:58:57Z)

Can't get tdxminer to work.


>              tdxminer version 0.2.2.2
>   This is a beta release and may be unstable on some hardware.
> [2018-08-18 10:47:58] Failed to initialize device number 0.
> [2018-08-18 10:47:58] Failed to initialize device number 1.
> 

Using Ubuntu 18.04, kernel 4.18.0 and installer above.

> [    0.000000] Command line: BOOT_IMAGE=/@/boot/vmlinuz-4.18.0 root=UUID=98ecb148-fe2f-4706-a45c-43a947e7f9f5 ro rootflags=subvol=@ quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off intel_iommu=on iommu=pt vt.handoff=1
> [    0.000000] Kernel command line: BOOT_IMAGE=/@/boot/vmlinuz-4.18.0 root=UUID=98ecb148-fe2f-4706-a45c-43a947e7f9f5 ro rootflags=subvol=@ quiet splash amdgpu.ppfeaturemask=0xffffffff amdgpu.dc=1 amdgpu.hw_i2c=1 amdgpu.vm_fragment_size=9 amdgpu.dpm=1 amdgpu.audio=1 amdgpu.ngg=1 selinux=0 security=off audit=0 spectre_v2=off nopti pti=off intel_iommu=on iommu=pt vt.handoff=1

> ~$ clinfo -l
> Platform #0: Clover
>  +-- Device #0: Radeon RX Vega (VEGA10 / DRM 3.27.0 / 4.18.0, LLVM 6.0.0)
>  `-- Device #1: Radeon RX Vega (VEGA10 / DRM 3.27.0 / 4.18.0, LLVM 6.0.0)
> Platform #1: AMD Accelerated Parallel Processing
>  +-- Device #0: gfx900
>  `-- Device #1: gfx900

> $ rocm-smi
> 
> 
> ====================    ROCm System Management Interface    ====================
> ================================================================================
>  GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
>   1   39.0c   3.0W     852Mhz   167Mhz   11.76%   auto      0%       
>   0   36.0c   5.0W     852Mhz   167Mhz   30.98%   auto      0%       
> ================================================================================
> ====================           End of ROCm SMI Log          ====================

miner strace here:
https://pastebin.com/ai83MWTt


---

### 评论 #14 — emerzon (2018-08-18T11:17:24Z)

First I removed the clover icd, and then it was failing at build.

>            tdxminer version 0.2.2.2
>   This is a beta release and may be unstable on some hardware.
> failed to build program.
> [2018-08-18 13:12:35] Failed to initialize device number 0.
> failed to build program.
> [2018-08-18 13:12:35] Failed to initialize device number 1.

I reinstall amdpro with --opencl=pal,legacy

>   Driver Version                                  2639.3 (PAL,HSAIL)

However, it still fails at compilation.

I tried some other miners:
Claymore also fails in compilation:

> Cannot build OpenCL program for GPU 0
> Cannot build OpenCL program for GPU 1
> Command-line error: invalid option: --march=hsail64
> 
> 1 catastrophic error detected in this compilation.
> Compilation terminated.
> GPU #0: set -etha as 0 (ETH algo for fast cards)
> Command-line error: invalid option: --march=hsail64
> 

XMRig-AMD actually is able to compile, but no hashrate is actually seen:

>  * VERSIONS     XMRig/2.7.3-beta libuv/1.18.0 OpenCL/2.0 gcc/7.3.0
>  * CPU          AMD Ryzen 7 1800X Eight-Core Processor          x64 AES
>  * ALGO         cryptonight, donate=5%
>  * POOL #1      cryptonightv7.eu.nicehash.com:3363 variant 1
>  * COMMANDS     hashrate, pause, resume
> [2018-08-18 13:14:39] compiling code and initializing GPUs. This will take a while...
> [2018-08-18 13:14:39] #0, GPU #0 Radeon RX Vega, intensity: 896 (8/256), cu: 56
> [2018-08-18 13:14:40] GPU #0 compiling...
> [2018-08-18 13:14:48] GPU #0 compilation completed, elapsed time 8.89s
> [2018-08-18 13:14:48] #1, GPU #1 Radeon RX Vega, intensity: 768 (8/256), cu: 56
> [2018-08-18 13:14:49] use pool cryptonightv7.eu.nicehash.com:3363 172.65.195.168
> [2018-08-18 13:14:49] new job from cryptonightv7.eu.nicehash.com:3363 diff 100001 algo cn/1
> | THREAD | GPU | 10s H/s | 60s H/s | 15m H/s |
> |      0 |   0 |     n/a |     n/a |     n/a |
> |      1 |   1 |     n/a |     n/a |     n/a |
> [2018-08-18 13:14:52] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
> | THREAD | GPU | 10s H/s | 60s H/s | 15m H/s |
> |      0 |   0 |     n/a |     n/a |     n/a |
> |      1 |   1 |     n/a |     n/a |     n/a |
> [2018-08-18 13:15:00] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
> 

If I CTRL-C, I can see that GPU is actually still doing something, since it starts running hot:

> ====================    ROCm System Management Interface    ====================
> ================================================================================
>  GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
>   1   54.0c   121.0W   1622Mhz  800Mhz   40.78%   auto      0%       
>   0   55.0c   115.0W   1590Mhz  800Mhz   25.88%   auto      0%       
> ================================================================================
> ====================           End of ROCm SMI Log          ====================
> 




---
