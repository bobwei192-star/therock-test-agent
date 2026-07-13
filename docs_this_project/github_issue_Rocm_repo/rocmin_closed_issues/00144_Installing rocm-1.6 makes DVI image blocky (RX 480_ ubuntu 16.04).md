# Installing rocm-1.6 makes DVI image blocky (RX 480, ubuntu 16.04)

- **Issue #:** 144
- **State:** closed
- **Created:** 2017-07-03T11:15:03Z
- **Updated:** 2017-07-26T13:48:46Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/144

Hi. I have dual monitor configuration - old Symcaster 2443 (vga+dvi) and new aoc I2475PXQU (DP + others). If i connect any of those via DVI-DVI cable, I get "blocky" or "pixalized" image on that monitor (font is hard to read). The non DVI monitor is ok. But if I connect via HDMI-DVI cable (hdmi on card) it is ok (on both "HDMI->DVI" and "DP-DP").

This is visible already in booting process.

In the ROCm-1.5 it was working (still kernel 4.9)