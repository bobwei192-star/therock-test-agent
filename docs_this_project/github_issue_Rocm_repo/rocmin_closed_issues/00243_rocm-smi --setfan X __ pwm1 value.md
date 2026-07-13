# rocm-smi --setfan X != pwm1 value

- **Issue #:** 243
- **State:** closed
- **Created:** 2017-11-04T19:05:40Z
- **Updated:** 2018-06-03T15:14:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/243

Can someone explain to me why --setfan and pwm1 value differ.
```
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
168
# rocm-smi -d 0 --setfan 170
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
181
# rocm-smi -d 0 --setfan 175
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
188
# rocm-smi -d 0 --setfan 180
# cat /sys/class/drm/card0/device/hwmon/hwmon0/pwm1
193
```
