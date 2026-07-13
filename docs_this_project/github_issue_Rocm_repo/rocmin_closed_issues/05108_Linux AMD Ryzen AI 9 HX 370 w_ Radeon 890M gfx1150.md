# Linux AMD Ryzen AI 9 HX 370 w/ Radeon 890M gfx1150

- **Issue #:** 5108
- **State:** closed
- **Created:** 2025-07-28T05:26:12Z
- **Updated:** 2026-01-26T15:01:29Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5108

Why is the gfx1150 not supported on Linux (kernel 6.14)?

After realizing that pytorch ROCm does not support this device, I thought I might "just" build it from source. But that just made me realize that there is no support in ANY of the AMD software libraries for this GPU!

In the newest version 6.4.2 there seems to be support for the gfx1151, but not for the gfx1150 (incl.  beta 7) .

When can we see this happening? Or, if not, why?

Thank you.