# pp_od_clk_voltage ignored?

- **Issue #:** 606
- **State:** closed
- **Created:** 2018-11-07T08:16:08Z
- **Updated:** 2019-01-03T23:56:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/606

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
