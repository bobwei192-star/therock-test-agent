# [Documentation]: Add `partition` information to `amd-smi` documentation

- **Issue #:** 4476
- **State:** closed
- **Created:** 2025-03-10T19:38:10Z
- **Updated:** 2025-03-25T19:38:10Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/4476

### Description of errors

The latest version of [this page](https://rocm.docs.amd.com/projects/amdsmi/en/latest/how-to/amdsmi-cli-tool.html#get-started) (corresponding to ROCm 6.3.3) does not provide up-to-date information for `amd-smi`. Namely, this documentation is missing any information about the `partition` command added in ROCm 6.3.

Currently the docs list the following output of `amd-smi`:

```
~$ amd-smi
usage: amd-smi [-h]  ...

AMD System Management Interface | Version: 24.7.1.0 | ROCm version: 6.3.0 | Platform: Linux Baremetal

options:
  -h, --help          show this help message and exit

AMD-SMI Commands:
                      Descriptions:
    version           Display version information
    list              List GPU information
    static            Gets static information about the specified GPU
    firmware (ucode)  Gets firmware information about the specified GPU
    bad-pages         Gets bad page information about the specified GPU
    metric            Gets metric/performance information about the specified GPU
    process           Lists general process information running on the specified GPU
    event             Displays event information for the given GPU
    topology          Displays topology information of the devices
    set               Set options for devices
    reset             Reset options for devices
    monitor (dmon)    Monitor metrics for target devices
    xgmi              Displays xgmi information of the devices
```

although this should be the following (note the addition of `partition`):
```
:~$ amd-smi
usage: amd-smi [-h]  ...

AMD System Management Interface | Version: 24.7.1+8dc45db | ROCm version: 6.3.3 |
Platform: Linux Baremetal

options:
  -h, --help          show this help message and exit

AMD-SMI Commands:
                      Descriptions:
    version           Display version information
    list              List GPU information
    static            Gets static information about the specified GPU
    firmware (ucode)  Gets firmware information about the specified GPU
    bad-pages         Gets bad page information about the specified GPU
    metric            Gets metric/performance information about the specified GPU
    process           Lists general process information running on the specified GPU
    event             Displays event information for the given GPU
    topology          Displays topology information of the devices
    set               Set options for devices
    reset             Reset options for devices
    monitor (dmon)    Monitor metrics for target devices
    xgmi              Displays xgmi information of the devices
    partition         Displays partition information of the devices
```

Also, an entire subsection needs to be added for the output of `partition -h`. Something like:

## amd-smi partition
Displays partition information for specified devices.

```
~$ amd-smi partition -h
usage: amd-smi partition [-h] [-g GPU [GPU ...]] [-c] [-m] [-a] [--json | --csv]
                         [--file FILE] [--loglevel LEVEL]

If no GPU is specified, returns information for all GPUs on the system.                                
If no partition argument is provided, all partition information will be displayed.

partition arguments:
  -h, --help               show this help message and exit
  -g, --gpu GPU [GPU ...]  Select a GPU ID, BDF, or UUID from the possible choices:
                           ID: 0 | BDF: 0000:01:00.0 | UUID: b8ff74a0-0000-1000-80e0-078991ff9d4d
                           ID: 1 | BDF: 0000:41:00.0 | UUID: eaff74a0-0000-1000-80a6-9826c47efb9c
                           ID: 2 | BDF: 0000:81:00.0 | UUID: b8ff74a0-0000-1000-808a-f96f2664a354
                           ID: 3 | BDF: 0000:c1:00.0 | UUID: 1aff74a0-0000-1000-80a5-0edc8434308c
                             all | Selects all devices
  -c, --current            display the current partition information
  -m, --memory             display the current memory partition mode and capabilities
  -a, --accelerator        display accelerator partition information

Command Modifiers:
  --json                   Displays output in JSON format (human readable by default).
  --csv                    Displays output in CSV format (human readable by default).
  --file FILE              Saves output into a file on the provided path (stdout by default).
  --loglevel LEVEL         Set the logging level from the possible choices:
                           	DEBUG, INFO, WARNING, ERROR, CRITICAL

```



### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_