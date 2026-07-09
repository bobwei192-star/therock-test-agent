# AMD Vega Frontier causes system hang/boot failure in thunderbolt 3 breakout box with ROCm driver.

- **Issue #:** 613
- **State:** closed
- **Created:** 2018-11-16T01:06:44Z
- **Updated:** 2023-12-08T17:46:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/613

First off, some configuration:

System: Apple iMac (2017).
CPU: i7 7700
Internal GPU: Radeon Pro 580
OS: Ubuntu 18.04.1
ROCm Version: 1.9.1

Thunderbolt Breakout: HP Omen Accelerator (Thunderbolt 3)
eGPU: Vega Frontier (Air Cooled)

Having gotten further than before, I still cannot get this configuration (which should be supported, to work).

I have verified that:

 - ROCm 1.9.1 is installed and working. With the eGPU disconnected, ROCm works and shows the internal graphics card (albeit as a 480 rather than a 580 in clinfo).
 - The TB3 enclosure works. With power disconnected to the GFX card, the TB3 enclosure is detected in Ubuntu. Other features (e.g. USB hub) work, direct access is enabled and the box is authorised.
 - The card/setup work fine under Mac OS - which detects the eGPU perfectly.

I'm experiencing 2 scenarios - if I boot ubuntu then hot plug the eGPU, I get an instant system lockup - to the point where the mouse cursor doesn't move.

If I boot with the eGPU connected, the boot process hangs at "A start job is running for Detect the available GPUs and deal with any system changes). There is a timer on this message, which at the point of writing says 3 hours 30 minutes / no limit - so I think it's safe to say it's hung indefinitely.

Any ideas on this? Happy to do any debugging/changes necessary.