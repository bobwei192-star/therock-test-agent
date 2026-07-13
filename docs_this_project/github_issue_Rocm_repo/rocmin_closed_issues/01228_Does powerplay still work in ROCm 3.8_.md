# Does powerplay still work in ROCm 3.8?

- **Issue #:** 1228
- **State:** closed
- **Created:** 2020-09-22T09:21:04Z
- **Updated:** 2020-12-14T06:18:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1228

Before it was possible to undervolt or otherwise tweak the voltage/frequency with powerplay, e.g. by writing to 
/sys/class/drm/card0/device/pp_od_clk_voltage

(to enable PP one had to boot with amdgpu.ppfeaturemask=0xffffffff or similar)

Did ROCm 3.8 change the way PP works? is it still possible to tweak voltage/frequency -- in a different way / how?
