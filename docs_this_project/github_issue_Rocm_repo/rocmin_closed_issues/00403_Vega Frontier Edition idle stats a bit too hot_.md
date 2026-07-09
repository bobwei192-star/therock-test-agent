# Vega Frontier Edition idle stats a bit too hot?

- **Issue #:** 403
- **State:** closed
- **Created:** 2018-05-06T03:32:31Z
- **Updated:** 2018-10-09T21:08:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/403

Hi all,

I've been checking rocm-smi on the heat/voltage/clock/fan speeds while the card is idle, and from what I see it seems to default at having the clock at max which sets the average temperature to a whopping 79.0c
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   79.0c   31.0W    1528Mhz  945Mhz   18.82%   auto      0%       
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```
I'm in Vancouver and it is getting a bit warmer granted, but it seems a little too hot to me... :)

When I run this manually:
```
rocm-smi --setperflevel low
```
I get much better temperatures and average power readouts:
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD
  1   36.0c   3.0W     852Mhz   167Mhz   12.94%   low       0%       
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A      
================================================================================
====================           End of ROCm SMI Log          ====================
```
Do I need to do anything special for it to go into this lower profile without doing this manually every time? I use this card as purely a compute device, the display is handled by a Quadro k2000 so nothing should be taxing it that I know of, no GUI/X11 is being displayed out of it.

Cheers!