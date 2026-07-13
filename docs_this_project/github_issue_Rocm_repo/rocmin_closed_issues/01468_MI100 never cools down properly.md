# MI100 never cools down properly

- **Issue #:** 1468
- **State:** closed
- **Created:** 2021-05-11T12:58:38Z
- **Updated:** 2022-03-07T03:37:39Z
- **URL:** https://github.com/ROCm/ROCm/issues/1468

* RHEL 8.3
* [Installed ROCM 4.1 via these instructions](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel)
* Machine is an HPE server with two Epyc CPUs.  An identitical system contains an NVIDIA A100 with no issues (all temperatures low).

Just after boot, the MI100 GPU has these temperatures:

```
amdgpu-pci-2900
Adapter: PCI adapter
vddgfx:       +0.62 V
fan1:           0 RPM  (min =    0 RPM, max = 3850 RPM)
edge:         +53.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
junction:     +59.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
mem:          +55.0°C  (crit = +94.0°C, hyst = -273.1°C)
                       (emerg = +99.0°C)
power1:       49.00 W  (cap = 290.00 W)
```

If I then run an OpenCL program that hammers memory (in my case, summing 4GiB of floats 10000 times), the temperature grows significantly, and for `mem` it even hits the limit, leading to this message in dmesg:

```
amdgpu 0000:29:00.0: WARN: GPU thermal throttling temperature reached, expect performance decrease. HBM.
```

That's perhaps fine by itself, and maybe the MI100 needs more airflow than we're giving it, but the weird thing is that the idle temperature then gets stuck about 10C higher than at boot:

```
amdgpu-pci-2900
Adapter: PCI adapter
vddgfx:       +0.63 V
fan1:           0 RPM  (min =    0 RPM, max = 3850 RPM)
edge:         +66.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
junction:     +71.0°C  (crit = +100.0°C, hyst = -273.1°C)
                       (emerg = +105.0°C)
mem:          +68.0°C  (crit = +94.0°C, hyst = -273.1°C)
                       (emerg = +99.0°C)
power1:       54.00 W  (cap = 290.00 W)
```

This of course also means that it overheats much faster in subsequent executions.  It remains hot until we reboot the machine, which makes little sense to me.  Is this normal?  Should the critical temperature for the memory be increased?