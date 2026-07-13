# modprobe: ERROR: could not insert 'amdkfd': Exec format error

- **Issue #:** 671
- **State:** closed
- **Created:** 2019-01-15T05:32:08Z
- **Updated:** 2019-01-16T02:25:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/671

Install fresh Ubuntu 18.04.1 Workstation.
System:
R5 2600X
RX Vega 64
X470 ASUS board
kernel 4.15.0-43-generic #46-Ubuntu SMP
GCC 7.3.0


Follow instructions on ROCm page.

Reboot.

No amdkfd loaded. Load it manually...

> sudo modprobe  amdkfd
_modprobe: ERROR: could not insert 'amdkfd': Exec format error_

I am actually getting this on above machine and another with same specs but an RX470 instead of a Vega 64.

I have upgraded kernel to 4.18: romc-dkms install says kernel 4.18 HEADERS(!) not supported.
I have upgraded kernel to 4.19: romc-dkms install says kernel 4.19 not supported.
I have upgraded kernel to 4.20: romc-dkms install says kernel 4.20 not supported.

Using amdkfd driver from Ubuntu's 4.18 kernel series the HIP sampels run, but for example hipCaffe fails most of it's unit tests.

I haven't got much hair left... has anyone else seen this, and manage to make the damned thing install?