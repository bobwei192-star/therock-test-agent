# [Issue]: Ubuntu 22.04 machine fails to boot after following rocm installation instructions

- **Issue #:** 2948
- **State:** closed
- **Created:** 2024-03-06T15:34:51Z
- **Updated:** 2024-08-30T07:53:23Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/2948

### Problem Description

I followed the instructions described in https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html

Everything seemed to install without issue. I got a note about some secure boot authorization that would take place on the next reboot to enable AMD's third-party drivers, and set up a password for that. After shutting down, the next time the machine started, I only saw a black screen. I thought that this might be related to the graphics card driver update, so I tried all the different HDMI and displayport ports on the GPU and motherboard, but none of them worked.

After that, I powered down the machine and tried rebooting again, to see if anything different would happen. Now, one of the HDMI ports on the GPU does produce an image to the screen, but it just splashes the motherboard vendor logo briefly before reverting to a black screen with a blinking white cursor in the top left. Subsequent reboots have the same effect.

I'd like to include detailed info about my OS and GPU, but I can't successfully boot the machine any more to run those commands. I know its running ubuntu 22.04, with an intel 12700K CPU and a Radeon VII GPU, but I don't know anything more specific than that.

Can anyone help me figure out what to do to recover from this borked installation? 

### Operating System

Ubuntu 22.04

### CPU

intel 12700k

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_