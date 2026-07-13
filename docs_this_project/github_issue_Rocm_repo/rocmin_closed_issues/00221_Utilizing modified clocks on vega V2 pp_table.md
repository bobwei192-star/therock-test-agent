# Utilizing modified clocks on vega V2 pp_table

- **Issue #:** 221
- **State:** closed
- **Created:** 2017-10-05T17:24:13Z
- **Updated:** 2018-05-12T18:44:27Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/221

I overwrote the pp_table with some custom clocks for my RX Vega 56 on states 5, 6 and 7.  So now I have the following:

$ cat /sys/class/drm/card0/device/pp_dpm_sclk
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1320Mhz 
6: 1325Mhz 
7: 1330Mhz 

When I start to utilize the GPU, the sclk never changes from state #0.  I get errors about it.

[  960.778779] amdgpu: [powerplay] Cannot find requested DCEFCLK!
[  961.172699] amdgpu: [powerplay] Cannot find requested DCEFCLK!
[ 1150.402251] amdgpu: [powerplay] Cannot find requested DCEFCLK!


