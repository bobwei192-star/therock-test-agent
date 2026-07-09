# Incorrect VRAM / MMIO reads of RX 6900 XT in virtualized environment

- **Issue #:** 1711
- **State:** closed
- **Created:** 2022-03-19T07:47:57Z
- **Updated:** 2022-03-19T14:18:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1711

I've encountered  something funny when playing around with the virtualization support of ROCm on RX 6900 XT. My set up is to pass the RX 6900 XT to a Linux guest VM with vfio. I'm running vanilla Linux 5.15.0 and qemu 6.2.

The guest is able to recognize the GPU but it fails to load the PSP runtime database:

```
[    9.335351] amdgpu 0000:03:00.0: amdgpu: PSP runtime database doesn't exist
[   11.208301] [drm] Loading DMUB firmware via PSP: version=0x02010003
[   11.211139] [drm] use_doorbell being set to: [true]
[   11.211786] [drm] use_doorbell being set to: [true]
[   11.212374] [drm] use_doorbell being set to: [true]
[   11.212963] [drm] use_doorbell being set to: [true]
[   11.213735] [drm] Found VCN firmware Version ENC: 1.13 DEC: 2 VEP: 0 Revision: 20
[   11.214612] amdgpu 0000:03:00.0: amdgpu: Will use PSP to load VCN firmware
[   11.399185] [drm] reserve 0xa00000 from 0x83fe000000 for PSP TMR
[   11.516981] amdgpu 0000:03:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[   11.518130] amdgpu 0000:03:00.0: amdgpu: smu driver if version = 0x00000040, smu fw if version = 0x0000003d, smu fw version = 0x003a3f00 (58.63.0)
[   11.519613] amdgpu 0000:03:00.0: amdgpu: SMU driver if version not matched
[   11.520420] amdgpu 0000:03:00.0: amdgpu: use vbios provided pptable
[   11.593488] amdgpu 0000:03:00.0: amdgpu: SMU is initialized successfully!
[   11.594886] [drm] Display Core initialized with v3.2.149!
[   11.597609] [drm] DMUB hardware initialized: version=0x02010003
```

Then the kfd refuses to load again due to different versions of firmware on the card:

```
[   11.614269] kfd kfd: amdgpu: skipped device 1002:73bf, PCI rejects atomics 85<92
```

The exact same kernel initializes the GPU just fine on the host. The results are the same for vanilla kernels / qemu on Ubuntu 20.04. I looked at the source codes of the driver. It seems the checks are simply to read the values from VRAM / registers and to compare with the expected results.

The only logical explanation is that the guest VM somehow reads incorrect values from the GPU. It is quite unlikely to me since the initialization has gone this far.

Your helps and ideas are appreciated. 