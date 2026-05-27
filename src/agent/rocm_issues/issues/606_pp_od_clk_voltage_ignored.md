# pp_od_clk_voltage ignored?

> **Issue #606**
> **状态**: closed
> **创建时间**: 2018-11-07T08:16:08Z
> **更新时间**: 2019-01-03T23:56:04Z
> **关闭时间**: 2019-01-03T23:56:04Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/606

## 描述

ROCm 1.9.1, Ubuntu 18.10, Vega64.

I enable PP with
GRUB_CMDLINE_LINUX_DEFAULT="amdgpu.ppfeaturemask=0xffffffff"

The "pp_od_clk_voltage" control file can be read correctly:

cat /sys/class/drm/card1/device/pp_od_clk_voltage 
OD_SCLK:
0:        852Mhz        800mV
1:        991Mhz        900mV
2:       1084Mhz        950mV
3:       1138Mhz       1000mV
4:       1200Mhz       1050mV
5:       1401Mhz       1100mV
6:       1536Mhz       1150mV
7:       1630Mhz       1200mV
OD_MCLK:
0:        167Mhz        800mV
1:        500Mhz        800mV
2:        800Mhz        950mV
3:        945Mhz       1050mV
OD_RANGE:
SCLK:     852MHz       2400MHz
MCLK:     167MHz       1500MHz
VDDC:     800mV        1200mV

I fix the power state to "5" with rocm-smi --setsclk 5,
next I edit the pp_od_clk_voltage for state 5:
echo "s 5 860 850" > pp_od_clk_voltage
echo c > pp_od_clk_voltage

No errors are reported, either on "echo" or in dmesg, but the change to the table has no effect on the GPU: it does not change the power use, the performance, or the voltage reported by "sensors".

So it seems that edits to pp_od_clk_voltage are ignored.. ?


---

## 评论 (16 条)

### 评论 #1 — rumatadest (2018-11-07T08:26:28Z)

Try set 
echo "manual" > /sys/class/drm/card0/device/power_dpm_force_performance_level

---

### 评论 #2 — preda (2018-11-07T08:40:41Z)

/sys/class/drm/card0/device/power_dpm_force_performance_level is already "manual". It seems it is such set by rocm-smi --setsclk 5.

---

### 评论 #3 — rumatadest (2018-11-07T09:22:09Z)

hm..
what is 860? looks like it's too low for 5 state.
my string is 
echo "s 5 1490 850" > /sys/class/drm/card0/device/pp_od_clk_voltage
echo "c"> /sys/class/drm/card0/device/pp_od_clk_voltage


---

### 评论 #4 — preda (2018-11-07T11:11:29Z)

in "s 5 860 850", 860 is frequency. Why would it be too low? The overall range is SCLK: 852MHz 2400MHz, and no error relative to range is reported on write.


---

### 评论 #5 — jlgreathouse (2018-11-07T19:54:35Z)

Try writing `1` into `/sys/class/drm/card0/device/pp_sclk_od` to turn on your custom OverDrive tables.

---

### 评论 #6 — preda (2018-11-07T20:48:16Z)

@jlgreathouse I tried writing 1 to /sys/class/drm/card0/device/pp_sclk_od , but it didn't help. I'm a bit confused by the behavior I see, it seems the GPU actual state is disconnected from what is reported in pp_*, or at least I couldn't figure out the relation.


---

### 评论 #7 — jlgreathouse (2018-11-07T21:29:31Z)

Ah, sorry. Writing `1` does basically the same thing as writing `c` into `/sys/class/drm/card0/device/pp_od_clk_voltage`. It causes the in-memory tables to be uploaded to the card so that it starts using them. My internal scripts weren't doing that, so my "solution" above really wouldn't affect your problem.

You're right, what's being reported out of a read from `pp_od_clk_voltage` is the OverDrive PowerPlay table *as it stands within the driver*. However, that table may or may not have been loaded into the hardware/firmware yet.

I believe I can recreate the problem you're running into, and the root cause is that you can't set the frequency for DPM state N to a value that is less than a DPM state <N.

So for instance, you're trying to set DPM5 to 860 MHz,  However, DPM4 in your table is 1200 MHz. As such, I would wager that when you try to force yourself into DPM5 it will automatically keep DPM5's frequency at a minimum of 1200 MHz (despite what the in-kernel table says). This is a function of our on-chip firmware, as tables that don't meet this these frequency requirements could cause our control algorithms to fail. (e.g. imagine the firmware wants to reduce power usage, so it goes to a lower DPM state... but then frequency/power goes up. Yuck.)

In addition, you should use rocm-smi to force your target DPM state *after* passing in the 'confirmation' into `pp_od_clk_voltrage`. Updating the firmware DPM table will un-force DPM settings so you'll likely end up automatically back in DPM 6 or 7 (of jumping between them at the firmware's discretion).

---

### 评论 #8 — preda (2018-11-07T21:49:25Z)

To start with, I don't understand exactly what voltage is reported by "sensors" for the GPU, and what is the relation of that voltage to the GPU tables:

Below are two Vega64 GPUs, with similar load, both with "rocm-smi --setsclk 5", both reporting the same tables pp_od_clk_voltage, and yet: one has vddgfx 0.95, the other has vddgfx 0.93, and none of these voltages correspond to what is in pp_od_clk_voltage (either proc or mem).

amdgpu-pci-6700
Adapter: PCI adapter
vddgfx:       +0.95 V  
fan1:        2396 RPM
temp1:        +78.0 C  (crit = +89.0 C, hyst = -273.1 C)
power1:      151.00 W  (cap = 200.00 W)

amdgpu-pci-6a00
Adapter: PCI adapter
vddgfx:       +0.93 V  
fan1:        2259 RPM
temp1:        +74.0 C  (crit = +89.0 C, hyst = -273.1 C)
power1:      156.00 W  (cap = 200.00 W)

cat /sys/class/drm/card1/device/pp_od_clk_voltage 
OD_SCLK:
0:        852Mhz        800mV
1:        991Mhz        900mV
2:       1084Mhz        950mV
3:       1138Mhz       1000mV
4:       1200Mhz       1050mV
5:       1401Mhz       1100mV
6:       1536Mhz       1150mV
7:       1630Mhz       1200mV
OD_MCLK:
0:        167Mhz        800mV
1:        500Mhz        800mV
2:        800Mhz        950mV
3:        945Mhz       1050mV
OD_RANGE:
SCLK:     852MHz       2400MHz
MCLK:     167MHz       1500MHz
VDDC:     800mV        1200mV


---

### 评论 #9 — preda (2018-11-07T21:54:34Z)

What I tried to achieve was to lower the vddgfx voltage of the first GPU from 0.95 to 0.93 to match the second GPU. No matter how much I tried I couldn't get a meaningful outcome from pp_od_clk_voltage.


---

### 评论 #10 — jlgreathouse (2018-11-07T23:45:40Z)

Well now the question is changing.

`sensors` is part of the `lm-sensors` package, which is not built or supported by AMD. That said, it's reading voltage from /sys/class/hwmon/hwmon1/in0_input (or hwmonN, depending on the GPU). You can see this by running `strace sensors`. The [source code for amdgpu](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c#L1360) shows that the value in this sysfs file is gathered from [amdgpu_hwmon_show_vddgfx()](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c#L1127).

This will [query the on-chip firmware](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/powerplay/hwmgr/vega10_hwmgr.c#L3719) to read the voltage being supplied by the board's voltage regulators.

So what you're seeing is that, even with the same DPM tables, your two GPUs are running at slightly different voltages. One is actually running a bit lower than the 950 mV of DPM2. I would strongly wager that this is a function of the [Adaptive Voltage and Frequency Scaling](https://www.slideshare.net/AMD/isscc) mechanism that is [available on Vega 10 GPUs](https://radeon.com/_downloads/vega-whitepaper-11.6.17.pdf). [This feature](https://image.slidesharecdn.com/pressdeckcarrizoissccnoembargodate-150508131953-lva1-app6892/95/isscc-carrizo-9-638.jpg?cb=1431091251) will automatically calibrate to your GPU, and it will apply voltage offsets to particular DPM states if this particular chip does not need that voltage to hit the target frequency. This saves power on your GPU. As such, it appears that one of your GPUs is slightly more efficient at 1084 MHz, since it needs a lower voltage.

Towards your question: you could try the commands I showed in my previous posts to write an updated DPM table. Note that much like I mentioned with clock limits (DPM N clock can't be lower than DPM N-1 clock, and it can't be higher than DPM N+1 clock) the same is true for voltages. So if you're trying to get SCLK DPM 2 to 850 mV (say), this will fail in your current tables, because DPM 1 requires 900 mV. As such, the firmware will (I believe) set your SCLK DPM 2 voltage to 900 mV. This may not be shown when you try to read the table back out, because you're reading the table you attempted to send into the firmware, not what the firmware actually accepted.

---

### 评论 #11 — preda (2018-11-08T18:02:29Z)

@jlgreathouse thank you for the pointers and the information. The situation seems to be more complex then what meets the eye, maybe in time some specification of the intended behavior of pp_od_clk_voltage will emerge. In particular, my two Vega64 are running at 1401MHz state "5" (not 1084MHz) on 0.95/0.93V, which is a faraway departure from the table.

After more experimentation, it does seem to me that you were right: a write to "pp_sclk_od" is needed in order to force a read of the table. (Just writing a "c" (commit) to pp_od_clk_voltage does not activate the table).

What is the interaction of the memory voltage with the sclk voltage -- is vddgfx the max() of the two voltages?


---

### 评论 #12 — jlgreathouse (2018-11-08T19:12:30Z)

I don't believe you should need to write to `pp_sclk_od`. That was a mistake on my part because the scripts I was using (internal dev branch of rocm-smi) wasn't (at the time) writing the proper commit message. I went back and started manually writing the commit message and things were working as I expected. This was on a Fiji, since that's the only system I had on hand that was running an upstream kernel, and I was out of the office (and thus unable to configure a custom system to match your "not officially supported by AMD at this time" setup).

If I remember correctly, Polaris GPUs more aggressively build their internal DPM tables by characterizing the chip during boot. However, the default OD tables (which is what you're reading when you read that file) are the pessimistic estimates burned into the VBIOS. Your GPUs might be better than these pessimistic estimates.

There are multiple voltages in play on our GPUs, including the voltage supplied to the core graphics logic, the voltage for video encode/decode hardware, voltages to run the video output, and voltage supplied to the memory chips. I believe the voltage being displayed is for the core graphics logic. However, running the memory system at particular frequencies will also require that logic (which interfaces to the memory through memory controllers in the graphics logic) to run at a particular frequency. As such, yes, I believe the actual supplied voltage will be the maximum of the two requested voltages (one for SCLK and one for MCLK).

The intended behavior of pp_od_clk_voltage is [documented in the kernel driver source code](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c#L469).

---

### 评论 #13 — preda (2018-11-08T21:49:58Z)

After writing this table:
echo s 0 852 800
echo s 1 1000 850
echo s 2 1100 880
echo s 3 1200 890
echo s 4 1300 900
echo s 5 1401 920
echo s 6 1405 925
echo s 7 1410 930
echo c
to pp_od_clk_voltage,

I see this unusual value in pp_sclk_od (it was reporting 0 initially).
/sys/class/drm/card1/device# cat pp_sclk_od        
26335

(I always read the same value 26335 from pp_sclk_od, after an update to pp_od_clk_voltage)

---

### 评论 #14 — jlgreathouse (2018-11-09T00:57:08Z)

Walking through what's happening here:
- That file is defined by [this chunk](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c#L942) of the amdgpu source code. In particular, the function `amdgpu_get_pp_sclk_od()` will be called when you read the file.
- `amdgpu_get_pp_sclk_od()` and what it will cause to be printed to the file are shown [here](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c#L747). Note that `value`, what will eventually be printed to the screen is a `uint32_t` unsigned value. It's set by `amdgpu_dpm_get_sclk_od()`.
- `amdgpu_dpm_get_sclk_od()` is a generic function (through a macro) [defined here](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_dpm.h#L314). Basically, it calls `get_sclk_od()` for your device, and different device generations will define this function differently.
- Your Polaris 10 GPU uses the SMU7 code, so the function pointer is [set here](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c#L5046). This will call `smu7_get_sclk_od()`.
- `smu7_get_sclk_od()` is [defined here](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.c#L4513). It reads the frequency contained in the current DPM table's highest state and compares it to the "golden" value that's set by the VBIOS. You'll also note that it returns a signed integer, though the `value` types being worked on [are unsigned](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/powerplay/hwmgr/smu7_hwmgr.h#L90).

In the end, what is being displayed is based on the following function:
```c
        /* uint32_t sclk_table->dpm_levels[sclk_table->count - 1].value is current DPM7
            uint32_t golden_sclk_table->dpm_levels[golden_sclk_table->count - 1].value is default DPM7 */
	value = (sclk_table->dpm_levels[sclk_table->count - 1].value -
			golden_sclk_table->dpm_levels[golden_sclk_table->count - 1].value) *
			100 /
			golden_sclk_table->dpm_levels[golden_sclk_table->count - 1].value;
```

The problem you're running into is because the values are unsigned, but ` (sclk_table->dpm_levels[sclk_table->count - 1].value - golden_sclk_table->dpm_levels[golden_sclk_table->count - 1].value)` is a negative number in your case. When you set your maximum frequency to 1410 MHz, but the default is 1630 MHz, that value should be negative. But all of the values in this chunk of code are unsigned. The subtraction that results in a "negative" number ends up being a huge unsigned value divided by a slightly less huge unsigned value. This test app demonstrates the problem:

```c
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

uint32_t dpm_value = 141000;
uint32_t golden_value = 163000;

static int smu7_get_sclk_od()
{
    int value;
    value = (dpm_value - golden_value) * 100 / golden_value;
    printf("Value after subtract: %u\n", (dpm_value - golden_value));
    printf("Value after multiply: %u\n", (dpm_value - golden_value) * 100);
    printf("Value after divide: %u\n", ((dpm_value - golden_value) * 100) / golden_value);
    return value;
}

#define amdgpu_dpm_get_sclk_od() smu7_get_sclk_od()

int main()
{
    uint32_t value = 0;
    value = amdgpu_dpm_get_sclk_od();
    printf("Final value returned to sysfs: %d\n", value);
}
```
```
$ ./a.out
Value after subtract: 4294945296
Value after multiply: 4292767296
Value after divide: 26335
Final value returned to sysfs: 26335
```

Basically, `pp_sclk_od` is normally supposed to hold a percentage that tells you how much faster your maximum frequency is over the normal "maximum" frequency. Writing to the file is supposed to be a quick and easy way to boost your maximum frequency by a fixed percentage without needing to rewrite the DPM tables.  It looks like we aren't really handling the "manually writing the DPM tables to underclock" situation well. I'll try to get a patch into amdgpu to fix this. Thanks for the report.

---

### 评论 #15 — jlgreathouse (2018-11-20T03:24:41Z)

Hi @preda 

[This patch](https://cgit.freedesktop.org/~agd5f/linux/commit/?h=amd-staging-drm-next&id=29bf84e646c45b3370b640d44c0ce454ecb845c3) should fix the problem you reported.

---

### 评论 #16 — preda (2019-01-03T23:55:54Z)

Thank you @jlgreathouse for the nice debug and fix! I'm going to close this issue for now.

As an idea, maybe somebody from the team concerned with power management, powerplay (amdgpu?) would like to do a test for how to achieve *undervolting*, and maybe publish somewhere an example or best-practice for undervolting.


---
