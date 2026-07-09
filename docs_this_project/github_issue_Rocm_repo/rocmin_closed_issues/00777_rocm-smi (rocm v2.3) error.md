# rocm-smi (rocm v2.3) error

- **Issue #:** 777
- **State:** closed
- **Created:** 2019-04-19T01:18:08Z
- **Updated:** 2019-06-07T12:14:40Z
- **URL:** https://github.com/ROCm/ROCm/issues/777

Was working fine with ROCm v2.2, manually setting the power target to 300w also works fine.

> Traceback (most recent call last):
>   File "/opt/rocm/bin/rocm-smi", line 1910, in <module>
>     setPowerOverDrive(deviceList, args.setpoweroverdrive, args.autorespond)
>   File "/opt/rocm/bin/rocm-smi", line 1396, in setPowerOverDrive
>     power_cap_path = getFilePath(device, 'power1_cap')
>   File "/opt/rocm/bin/rocm-smi", line 130, in getFilePath
>     pathDict = valuePaths[key]
> KeyError: 'power1_cap'