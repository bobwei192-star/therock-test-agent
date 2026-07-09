# FR: allow fine-tuned voltage/frequency control

- **Issue #:** 512
- **State:** closed
- **Created:** 2018-08-23T23:37:38Z
- **Updated:** 2019-01-04T00:05:18Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/512

amdgpu-pro allows setting the frequency and voltage per power state by writing to 
/sys/class/drm/card0/device/pp_od_clk_voltage, e.g.:
echo "s 4 900 1050" > pp_od_clk_voltage
echo c > pp_od_clk_voltage
as described here:
https://www.reddit.com/r/Amd/comments/8weeln/you_can_undervolt_vegas_in_linux_now/

Could ROCm offer a similar functionality?
