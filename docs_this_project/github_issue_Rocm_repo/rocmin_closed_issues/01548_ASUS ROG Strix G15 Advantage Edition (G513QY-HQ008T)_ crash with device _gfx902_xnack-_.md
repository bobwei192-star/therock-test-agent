# ASUS ROG Strix G15 Advantage Edition (G513QY-HQ008T), crash with device 'gfx902:xnack-'

- **Issue #:** 1548
- **State:** closed
- **Created:** 2021-08-06T15:51:55Z
- **Updated:** 2021-08-11T09:50:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/1548

        Hi
        I'm doing some basic OpenCL programming and things are working fine
        with my 'main PC' with an 'AMD Radeon PRO WX 7100 8GB PCIe 3.0'.

        clGetDeviceIDs() reports one device of CL_DEVICE_TYPE_GPU for
        the platform and clGetDeviceInfo() reports 'gfx803' as CL_DEVICE_NAME.

        A few days ago I bought the mentioned notebook but things did not
        work as expected. This notebook has an AMD Ryzen 9 5900HX CPU and an
        AMD Radeon RX 6800M GPU.

        Now clGetDeviceIDs() reports two devices of CL_DEVICE_TYPE_GPU for
        the platform and clGetDeviceInfo() shows 'gfx1031' and 'gfx902:xnack-'
        for CL_DEVICE_NAME.

        With my OpenCL programm I can use device 'gfx1031' but when trying
        to use device 'gfx902:xnack-' I get 'random errors'.

        Comparable problems also occur with clinfo. The symptoms are:

        When run the first time after power up of the PC the programs
        run up to some point and then stop with this error:

        Memory access fault by GPU node-2 (Agent handle: 0x5652e8860350) on address (nil). Reason: Unknown.

        In this case dmesg is showing things like these:

[  199.015019] amdgpu 0000:07:00.0: amdgpu: [gfxhub0] no-retry page fault (src_id:0 ring:173 vmid:8 pasid:32772, for process clinfo pid 1382 thread clinfo pid 1382)
[  199.015026] amdgpu 0000:07:00.0: amdgpu:   in page starting at address 0x0000000000000000 from IH client 0x1b (UTCL2)
[  199.015035] amdgpu 0000:07:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840A51
[  199.015036] amdgpu 0000:07:00.0: amdgpu:      Faulty UTCL2 client ID: CPC (0x5)
[  199.015037] amdgpu 0000:07:00.0: amdgpu:      MORE_FAULTS: 0x1
[  199.015038] amdgpu 0000:07:00.0: amdgpu:      WALKER_ERROR: 0x0
[  199.015038] amdgpu 0000:07:00.0: amdgpu:      PERMISSION_FAULTS: 0x5
[  199.015039] amdgpu 0000:07:00.0: amdgpu:      MAPPING_ERROR: 0x0
[  199.015039] amdgpu 0000:07:00.0: amdgpu:      RW: 0x1

        When rerun the programs do NOT stop but seem to be in a busy loop
        with top showing about 100% CPU for the process. I do not see dmesg
        messages in this case.

        In my OpenCL program the last activity before the crash is just
        before I call clCreateContext().
        For clinfo the last messages printed on the screen before the crash
        are these:

...
  Device Name                                     gfx902:xnack-
  Device Vendor                                   Advanced Micro Devices, Inc.
...
...
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
*** crash***

        BTW, I first noticed this problem with my Arch Linux and ROCm 4.3
        (and also 4.2) which I installed from the AUR.

        In order to make sure that the problem was not introduced by some
        error in the Arch installation I set up a fresh UBUNTU 20.04.02
        and installed the latest ROCm according to instructions from here:

        https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#supported-operating-systems

        After some minor correction for LD_LIBRARY_PATH I could/can run
        clinfo and my program also on UBUNTU 20.04.02 but the crash I see
        still is there. So the problem should not be with the Arch installation.

        Would anybody have a clue what might be the problem here or what
        could we do to narrow down the problem?

        BTW rocminfo does run without problems in any case.