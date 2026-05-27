# OpenCL: decreasing performance due to thermal throttling

> **Issue #564**
> **状态**: closed
> **创建时间**: 2018-09-30T21:16:28Z
> **更新时间**: 2018-10-11T16:34:07Z
> **关闭时间**: 2018-10-11T16:34:07Z
> **作者**: Moading
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/564

## 描述

Hi,
I have an up to date ubuntu 16.04.5 LTS running Rocm 1.9.
Hardware: Supermicro X10SRA-F, Xeon E5-2680V3, 3 x Radeon Pro Duo (polaris, gfx803). All GPUs are recognized.

I am running an OpenCL program that uses all 6 GPUs, the program is repeatedly executing a few kernels (without device side enqueue). At first, the performance of the program is good. After about 190 seconds, the performance starts to drop and never recovers. The only thing I noticed are messages in the output of dmesg that begin before the performance starts to drop.

The attached output of dmesg conatins messages like these:
[  483.147199] kfd kfd: Interrupt ring overflow, dropping interrupt 0
[  488.160470] enqueue_ih_ring_entry: 102777 callbacks suppressed
These messages worry me, because they are printed in red :)

The performance starts to drop at uptime 672 seconds.

What could cause these error messages? Should I look for a bug in my OpenCL kernels?

[dmesg.zip](https://github.com/RadeonOpenCompute/ROCm/files/2431980/dmesg.zip)


---

## 评论 (4 条)

### 评论 #1 — fxkamd (2018-10-01T13:30:44Z)

The inturrupt ring messages from KFD are usually harmless. But they indicated that your program is generating lots of signals to the host and KFD is having trouble keeping up.

That doesn't explain why your program's performance is dropping at 672 seconds. It's impossible to say without knowing more about how your program works. It could also be something in the OpenCL runtime, and I'm no expert for that.

Generally speaking, degrading performance over time could be caused by a resource leak. E.g. memory leaks can lead to address space and memory fragmentation and drag down the memory manager performance. Leaking queues could exceed the number of HW queues available and cause queues to be oversubscribed. Leaking event slots could make detection or signaled events slower. Etc.

---

### 评论 #2 — Moading (2018-10-02T08:00:29Z)

I think this is a thermal problem. After setting the fan speed to 100% via rocm-smi, the performance is constant. Now the question is why does the driver not increase fan speed further? All fans were set to automatic control.

Two GPUs are installed next to each other so that one card sucks in hot air from the back side of the other card.

---

### 评论 #3 — jlgreathouse (2018-10-09T05:56:24Z)

Hi @Moading 

Your question, "why does the driver not increase fan speed further" can yield a pretty long answer. I'll start with the quickest summary I can come up with, then discuss it in more detail and try to give you some workarounds.

### Summary
AMD must trade off performance with overall user experience. There is a limit to the amount of fan noise that users will generally find permissible for desktop and workstation cards, since those are often placed in computers sitting on desks, in offices, cubicles, etc. By default, these cards have a maximum acoustically acceptable fan speed and will throttle down performance if they get too hot to prevent too much fan noise.

### Details
AMD sells cards in a number of different domains. This includes our "Radeon"-branded consumer cards, "Radeon Pro"-branded workstation cards, and "Radeon Instinct"-branded server cards. The former two are actively cooled with fans or with water-cooling loops, while the latter do not come with fans. The latter are meant to be cooled using the case-fans in a server chassis. The server itself (likely through a [BMC](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface#Baseboard_management_controller)) controls the fans in response to various environmental and administrative inputs. These are usually installed in server rooms, and the fans can be quite loud (but can move a lot of air to allow for adequate cooling of high-powered parts).

For the consumer and workstation parts, let's focus on air cooling. In this case, the fans on the card can be controlled through a mix of the GPU's firmware and drivers. Fast fans allow for better cooling, but are noisier. Applications that burn a lot of GPU power can cause the chip's temperature to rise, and the fans should increase their speed to prevent the chip from reaching dangerous temperatures.

However, as you've seen, the firmware in our chips may not necessarily increase the fan speed to its absolute maximum in the face of high temperatures. Rather, after the fan speeds reach a certain point, the temperature may continue to rise if you continue to put work into the system. At some point, to prevent the chip from becoming hotter, the firmware will instead throttle the frequency of the chip to help it cool off. This can cause your application to slow down.

Your question is a good one. Why doesn't the firmware on these GPUs just ramp the fans up as fast as they will go to prevent any performance loss? I mentioned above that fans can be loud, and that's actually a major part of my answer to your question. "Radeon" and "Radeon Pro" GPUs are often installed in desktops or workstations that sit next to people, rather than in an isolated server room. Therefore, ramping up fan speed can be seen as a bad thing. If you'll look at a few recent GPU reviews (e.g. [1](https://www.anandtech.com/show/11278/amd-radeon-rx-580-rx-570-review/16), [2](https://techreport.com/review/31754/amd-radeon-rx-580-and-radeon-rx-570-graphics-cards-reviewed/6), [3](https://www.tomshardware.com/reviews/amd-radeon-rx-570-4gb,5028-17.html)), you'll see that fan noise while under load is one of the major things used to "grade" the quality of a GPU.

As such, there are incentives to get the best performance _within a reasonable amount of fan noise_ in these markets. Because of this, our drivers and firmware (and the OEMs who program settings into the VBIOS when they make a product) must make some tradeoffs when deciding the default settings for sustained fan speed vs. performance. You're running into this tradeoff pretty directly. :)

### Potential Solutions
I don't think that every company is going to be able to automatically answer meet every user's desire 100% of the time. I have no doubt that there are users who would hate to have their fans start screaming as soon as their chip starts to warm up. Based on your question, I'd guess you would rather maintain performance regardless of the noise. Rather than try to guess this, I think a better policy is to give some mechanisms to users to allow them to change things towards their needs.

Let me therefore try to describe some methods to fix the thermal throttling problems you're seeing.

#### Manually Maxing Fan Speeds
The most straightforward answer, which you've obviously taken advantage of, is to use a tool like `rocm-smi` to manually set the GPU's fan speed to its maximum. This will prevent as much thermal throttling as possible (though you may still run into some throttling in your applications due to power limits, etc.). 

We specifically allow user control over fans through tools like `rocm-smi` so that they can make their own performance-vs-noise tradeoffs, rather than relying on the default tradeoffs we made for the general case.

#### Feedback-Directed Manual Control
Rather than always keeping the fans at maximum, you could also use a tool like `rocm-smi` to monitor the temperature of your GPU and manually ramp the fan speed in reaction to rises in temperature. This is more advanced than simply setting the fans to 100%, but it shouldn't be too hard to implement in a simple shell script. This could be repeatedly run in the background using something like an [mcron](https://www.gnu.org/software/mcron/) job, or you could just launch off the shell script in the background with some sleep calls in it.

Note that you also don't need to use `rocm-smi`, as you could directly monitor temperature by watching the file `/sys/class/hwmon/hwmon#/temp1_input`, where "#" can be replaced with the number of the GPU you want to monitor. Similarly, fan speed can be controlled by writing `1` into `/sys/class/hwmon/hwmon#/pwm1_enable` and [writing a fan speed value](https://github.com/RadeonOpenCompute/ROC-smi/blob/roc-1.9.x/rocm_smi.py#L886) into `/sys/class/hwmon/hwmon#/pwm1`. (Write `2` into the `pwm1_enable` file to set things back to 'automatic' mode.

In the end, this would allow you to write your own control loop instead of using the one provided by AMD, if you wanted to get complex enough. :)

#### Custom Drivers
I haven't spoken much about the architecture of the fan control loop in our GPU software and hardware stack. Almost everything I've described so far has assumed you are using a standard ROCm software installation. However, one of the benefits of an open source software stack is that you can make modifications to the software to suit your needs. :)

As such, one potential thing you could do to alleviate your problem is to make some minor modifications to the ROCK kernel drivers to set your fans to run more aggressively. **Note** that making such modifications will take you outside of AMD's "officially supported" zone. **Note especially** that making incorrect modifications to the power or thermal control logic runs the risk of _damaging your hardware_, so such tasks should only be taken up by experts who are OK with the possible risks.

That said, in your original question you asked why AMD's drivers don't increase the fan speeds further. To be clear, the fan speeds on your GPU are actually under the control of on-chip firmware. This firmware monitors various temperatures across the GPU and tries to meet various targets. This includes setting the fan speeds to try to keep the GPU under a particular set-point temperature and to prevent the GPU from going over a maximum temperature. It will also try to limit the fans to some maximum speed(s). This is also the firmware that will lower clock frequency if temperature (or power usage, or a number of other factors) gets too high.

The defaults for all of these various targets (set-point temperature, maximum fan speed, etc.) are contained in the PowerPlay tables (pptables) that are part of the VBIOS which ships on your GPU. These values are set by the OEM device manufacturer, since different cards can have different cooling solutions, fans, clock frequencies, etc. As such, it's not like we have a single "maximum fan speed" or single "target temperature" per ASIC. That said, some of these firmware values are modified by (or initialized by) _the driver_. You can thus try to modify some of them by making a custom `amdgpu` driver.

##### gfx8 Example
@Moading, your GPU is a Radeon Pro Duo Polaris. This gfx803 GPU uses our "smu7" code. If you are using the drivers included in ROCm 1.9.1, you will find this code in `/usr/src/amdgpu-1.9-224/amd/amdgpu/powerplay/`. In particular, if you look at `/usr/src/amdgpu-1.9-224/amd/amdgpu/powerplay/smu7_thermal.c`, you will the following around line 158 in the function `smu7_fan_ctrl_start_smc_fan_control()`:
```c
if (PP_CAP(PHM_PlatformCaps_FanSpeedInTableIsRPM))
        hwmgr->hwmgr_func->set_max_fan_rpm_output(hwmgr,
                        hwmgr->thermal_controller.
                        advanceFanControlParameters.usMaxFanRPM);
...
if (!result && hwmgr->thermal_controller.
                advanceFanControlParameters.ucTargetTemperature)
        result = smum_send_msg_to_smc_with_parameter(hwmgr,
                        PPSMC_MSG_SetFanTemperatureTarget,
                        hwmgr->thermal_controller.
                        advanceFanControlParameters.ucTargetTemperature);
````

The former (assming your particular device does have the `FanSpeedInTableIsRPM` hardware capability, which I believe Polaris does) tells the firmware that the maximum fan speed it is aiming for is `advancedFanControlParameters.usMaxFanRPM`. This value comes from the pptable in the VBIOS (read back from the SMU, see `process_pptables_v1_0.c` if you care). However, you could inspect this and set it to whatever you want. For instance -- if you find that your GPU currently maxes its fan at 50%, and if `/sys/class/hwmon/hwmon#/fan1_input` shows that its speed is roughly 2000 RPM at that time, then you could modify your driver to call `set_max_fan_rpm_output(hwmgr, 4000)` to give the firmware permission to take the fan all the way up to the fan's maximum RPM. Note that you should be careful you do not set this *too* high, because the firmware may think that there is plenty of fan speed headroom left while the chip is slowly baking itself. :)  So don't set this more than the RPMs you see when you manually lock the fan to 100% (using e.g. `rocm-smi`).

In addition, you may want to change the value being sent to the SMU in the `PPSMC_MSG_SetFanTemperatureTarget` message. For example, your GPU may start to thermal throttle when it hits a temperature like 90C. If the SMU's fan is trying to target 85C, the fan may not ramp up fast enough to keep the chip from touching 90C. At that point, you will still thermally throttle. As such, you may want to lower the fan's temperature target (though this may raise the default fan speed even when the chip is idling).
You could add a kernel printout (using e.g. `pr_warning()` on a test build of your driver) to see what the default setpoint is on your card, if you desire.

After making these changes, you can rebuild and reinstall your driver with the following set of commands (on ROCm 1.9.1):
```
sudo dkms remove amdgpu/1.9-224 --all
sudo dkms add amdgpu/1.9-224
sudo dkms build amdgpu/1.9-224
sudo dkms install amdgpu/1.9-224
sudo reboot
```

Note that before rebooting, you should ensure that the `dkms build` command succeeds. This command rebuilds the driver and may fail if you make a coding mistake.

##### gfx9 Example
Newer GPUs, such as Vega 10, have a slightly different firmware interface in the driver. In this case, you would want to look at `/usr/src/amdgpu-1.9-224/amd/amdgpu/powerplay/vega10_thermal.c` in the function `vega10_thermal_setup_fan_table()`.

```c
table->FanMaximumRpm = (uint16_t)hwmgr->thermal_controller.
                advanceFanControlParameters.usMaxFanRPM;
table->FanThrottlingRpm = hwmgr->thermal_controller.
                advanceFanControlParameters.usFanRPMMaxLimit;
table->FanAcousticLimitRpm = (uint16_t)(hwmgr->thermal_controller.
                advanceFanControlParameters.ulMinFanSCLKAcousticLimit);
table->FanTargetTemperature = hwmgr->thermal_controller.
                advanceFanControlParameters.usTMax;
```

You'll see that we have the "fan target temperature" as we saw above, though the way of setting it is slightly different. However, we have multiple RPM limits:
- `FanMaximumRpm`: The Maximum RPM that the fan is allowed to spin at
- `FanThrottlingRpm`: The RPM to spin the fan at when your GPU is thermally throttling (this will likely be below `FanMaximumRpm` by default)
- `FanAcousticLimitRpm`: The maximum fan RPM to use in normal operating mode. This points back to the tradeoff between acoustics (noise) and performance.

If you happend to set `FanThrottlingRpm` and `FanAcousticLimitRpm` to the default value of `FanMaximumRpm`, then you could override the difference between the three that's put in by default. **Note**: please don't set the throttling RPM lower than the acoustic RPM limit. If you're in thermal throttling mode, you really don't want to _slow your fans down more_. This is dangerous and completely unsupported.

Again, you may need to move the `FanTargetTemperature` lower than the default to give the fans plenty of time to ramp up. :)

You can use the same dkms remove/add/build/install steps shown above to rebuild and install this new custom `amdgpu` build.

---

### 评论 #4 — Moading (2018-10-11T16:34:02Z)

Hi @jlgreathouse,

thank you for this detailed reply. I will use manual fan speed control.

Greetings!

---
