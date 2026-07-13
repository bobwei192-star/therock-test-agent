# Fiji card does not clock up with ROCm 1.4

- **Issue #:** 90
- **State:** closed
- **Created:** 2017-02-24T02:08:19Z
- **Updated:** 2018-10-16T01:50:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/90

No matter what I do, the Fiji card in question is stuck at 300 MHz core clock. Loading it with work, setting clocks or PowerPlay level all does not do anything.

Radeontop shows:
```
                                                       Graphics pipe  64.17% |                                                                           
```

But the clocks are stuck:
```
$ /opt/rocm/bin/rocm-smi -d 0 -a
===================   ROCm System Management Interface   ===================
============================================================================
GPU[0]          : GPU ID: 0x7300
============================================================================
============================================================================
GPU[0]          : Temperature: 36.0c
============================================================================
============================================================================
GPU[0]          : GPU Clock Level: 0 (300Mhz)
GPU[0]          : GPU Memory Clock Level: 0 (500Mhz)
============================================================================
============================================================================
GPU[0]          : Fan Level: 48 (18.82)%
============================================================================
============================================================================
GPU[0]          : Current PowerPlay Level: manual
============================================================================
============================================================================
GPU[0]          : Current OverDrive value: 0%
============================================================================
============================================================================
GPU[0]          : Minimum SCLK: 974MHz
GPU[0]          : Minimum MCLK: 0MHz
GPU[0]          : Activity threshold: 30%
GPU[0]          : Hysteresis Up: 0ms
GPU[0]          : Hysteresis Down: 5ms
============================================================================
============================================================================
GPU[0]          : Supported GPU clock frequencies on GPU0
GPU[0]          : 0: 300Mhz *
GPU[0]          : 1: 508Mhz 
GPU[0]          : 2: 717Mhz 
GPU[0]          : 3: 874Mhz 
GPU[0]          : 4: 911Mhz 
GPU[0]          : 5: 944Mhz 
GPU[0]          : 6: 974Mhz 
GPU[0]          : 7: 1000Mhz 
GPU[0]          : 
GPU[0]          : Supported GPU Memory clock frequencies on GPU0
GPU[0]          : 0: 500Mhz *
GPU[0]          : 
============================================================================
===================          End of ROCm SMI Log         ===================
```

Also:
```
$ /opt/rocm/bin/rocm-smi -d 0 --setsclk 7

===================   ROCm System Management Interface   ===================


===================   ROCm System Management Interface   ===================
GPU[0]          : Successfully set GPU Clock frequency to Level 7
===================          End of ROCm SMI Log         ===================
```
does nothing.

BTW funnily enough
```
 $ /opt/rocm/bin/rocm-smi -d 0 --setsclk 1000

===================   ROCm System Management Interface   ===================

===================   ROCm System Management Interface   ===================
GPU[0]          : Successfully set GPU Clock frequency to Level 1000
===================          End of ROCm SMI Log         ===================
```
is also supported while --setmlck only takes as argument the index of the memory frequency from the list (i.e. 0) not the memory clock value (500).