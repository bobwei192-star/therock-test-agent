# Core voltage settings not honored by amdgpu

- **Issue #:** 348
- **State:** closed
- **Created:** 2018-03-01T02:39:43Z
- **Updated:** 2018-10-27T05:46:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/348

Being able to downvolt GPUs in Linux is obviously crucial in mining. A simple hack of the polaris10_smc.c file found here achieves the task, it does work with latest versions of amdgpu (like 17.40):

https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/amd-linux/918649-underclocking-undervolting-the-rx-470-with-amdgpu-pro-success

The `polaris10_get_dependency_volt_by_clk` is responsible for setting core voltage. Strange though, the article is dated 2016, yet, up until now this has not been fixed. Core voltage table contained in GPU vbios works correctly in Windows, however in Linux it's ignored and core voltage is set at bootup at some fixed value (whose _value_ I was not even able to tell).

I am not that much of a programmer to do it myself (I'm also kinda afraid to burn my GPUs $1800 worth), but this should really be an easy job for someone who wrote amdgpu. Just wonder why it's never been done? Or maybe it can be set somewhere in the OS itself, in config files? In `/sys/class/hwmon/hwmon$i/device/pp_table` ? Can you please hint it?

p.s. Neither ohgodatool or rocm-smi can actually downvolt GPU core. Power table values change, but actual core voltage does not. Ohgodatool can downvolt vddci, but that's only about 5% power savings.

thanks )