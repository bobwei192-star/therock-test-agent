# Navi10(I know its not officially supported...again) not reaching highest memory state when overclocked.

- **Issue #:** 1247
- **State:** closed
- **Created:** 2020-09-28T08:36:13Z
- **Updated:** 2020-12-03T12:13:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/1247

Hello, since 3.8.0 was released, when you use pp_od_clk_voltage and overclock memory above stock(875) it results in this:
 cat pp_dpm_mclk
```
0: 100Mhz
1: 500Mhz
2: 625Mhz *
3: 900Mhz
```
Only way to bypass limitation is to use manual performance state but for my line of work it's unstable. Using ROCm 3.5.1 has no such issue.
Reproduce by using:
```
echo "s 1 1460" > pp_od_clk_voltage
echo "m 1 900" > pp_od_clk_voltage
echo "vc 2 1460 800" > pp_od_clk_voltage
echo c > pp_od_clk_voltage
```
I was about to submit this to amd official gitlab issues but yet again, I have no idea which commit breaks it or series.
