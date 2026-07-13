# Odd glitch on Ubuntu

- **Issue #:** 1692
- **State:** closed
- **Created:** 2022-02-25T02:53:00Z
- **Updated:** 2022-03-03T05:02:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1692

I am experiencing a very odd glitch. So far I've tested this with focal, xenial, and also jammy, where it happens on all 3 fresh installs.

When I try to run any program that takes advantage of rocm 4.3, the program just gets stuck.

I've left it overnight to see if it would resume but it did not.

But the most odd thing about it is that for some reason my gpu, (RX Vega 56) becomes extra "sensitive" I wanna say...

For example, while the program is stuck, just moving or clicking the mouse shoots the gpu usage to 100%, and as soon as I pkill python it doesn't do it anymore.

I've been tinkering with this for days and I have no idea why it's doing this.

Any help at all would be appreciated.