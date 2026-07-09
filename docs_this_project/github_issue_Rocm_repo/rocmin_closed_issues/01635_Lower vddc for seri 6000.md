# Lower vddc for seri 6000

- **Issue #:** 1635
- **State:** closed
- **Created:** 2021-12-10T18:09:12Z
- **Updated:** 2022-01-28T11:43:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1635

Hi team,
I have a problem when use voltoffset for 6600xt.
I set VDDC_OFFSET: -150 (or -200 or -400) but when I cat file `/sys/class/drm/card1device/hwmon/hwmon*/in0_input` seem it stable min at 737(mV).
Could i set lower vddc for my gpu.
Thanks 