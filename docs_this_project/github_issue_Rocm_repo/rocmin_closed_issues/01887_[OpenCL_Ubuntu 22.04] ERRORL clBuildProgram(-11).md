# [OpenCL/Ubuntu 22.04] ERRORL clBuildProgram(-11)

- **Issue #:** 1887
- **State:** closed
- **Created:** 2023-01-07T10:15:26Z
- **Updated:** 2023-01-09T17:33:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1887

Hi,
 
I want to use rocM/OpenCL with my following setup:

- AMD CPU 5950
- GPU 7900 XTX
- Ubuntu 22.04.1 LTS
- rocm-5.4.1
 
So I installed the recommend amdgpu-install package, excuted 'amdgpu-install --opencl=rocr', rebooted and tried to compile run a simple OpenCL program - but it did a SIGSEGV.

The clinfo output shows me that it cannot build a program: 
....
**ERROR: clBuildProgram(-11)**
 
The log in my home directory ($HOME/.cache/pocl/kcache/HC/NCOMMENGDMGEMFMJPBGNJKKHLHLCCIGAOFJGH/build.log) shows: **'error: unknown target CPU 'generic''**

 
I am stuck right now. Is this this a known bug, or can I fix this?
Any ideas are welcome!

----

❯ sudo dmesg | grep amdgpu
[    1.728194] [drm] amdgpu kernel modesetting enabled.
[    1.728195] [drm] amdgpu version: 5.18.13
[    1.728249] amdgpu: Ignoring ACPI CRAT on non-APU system
[    1.728254] amdgpu: Virtual CRAT table created for CPU
[    1.728267] amdgpu: Topology: Add CPU node
[    1.735618] amdgpu: PeerDirect support was initialized successfully
[    1.735733] amdgpu 0000:0d:00.0: vgaarb: deactivate vga console
[    1.735773] amdgpu 0000:0d:00.0: enabling device (0006 -> 0007)
[    1.738052] amdgpu 0000:0d:00.0: amdgpu: Fetched VBIOS from VFCT
[    1.738054] amdgpu: ATOM BIOS: 113-D7020100-102
[    1.738058] amdgpu 0000:0d:00.0: [drm:jpeg_v4_0_early_init [amdgpu]] JPEG decode is enabled in VM mode
[    1.738159] amdgpu 0000:0d:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[    1.738196] amdgpu 0000:0d:00.0: amdgpu: VRAM: 24560M 0x0000008000000000 - 0x00000085FEFFFFFF (24560M used)
[    1.738197] amdgpu 0000:0d:00.0: amdgpu: GART: 512M 0x0000000000000000 - 0x000000001FFFFFFF
[    1.738219] [drm] amdgpu: 24560M of VRAM memory ready
[    1.738220] [drm] amdgpu: 64364M of GTT memory ready.
[    1.739146] amdgpu 0000:0d:00.0: amdgpu: CP RS64 enable
[    1.739466] amdgpu 0000:0d:00.0: amdgpu: Will use PSP to load VCN firmware
[    2.025395] amdgpu 0000:0d:00.0: amdgpu: RAP: optional rap ta ucode is not available
[    2.025397] amdgpu 0000:0d:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
[    2.025445] amdgpu 0000:0d:00.0: amdgpu: smu driver if version = 0x00000030, smu fw if version = 0x00000034, smu fw program = 0, smu fw version = 0x004e4700 (78.71.0)
[    2.025448] amdgpu 0000:0d:00.0: amdgpu: SMU driver if version not matched
[    2.189465] amdgpu 0000:0d:00.0: amdgpu: SMU is initialized successfully!
[    2.502703] amdgpu 0000:0d:00.0: [drm:jpeg_v4_0_hw_init [amdgpu]] JPEG decode initialized successfully.
[    2.504415] kfd kfd: amdgpu: Allocated 3969056 bytes on gart
[    2.504508] amdgpu: sdma_bitmap: fff0
[    2.594623] amdgpu: HMM registered 24560MB device memory
[    2.594770] amdgpu: SRAT table not found
[    2.594771] amdgpu: Virtual CRAT table created for GPU
[    2.595292] amdgpu: Topology: Add dGPU node [0x744c:0x1002]
[    2.595297] kfd kfd: amdgpu: added device 1002:744c
[    2.595312] amdgpu 0000:0d:00.0: amdgpu: SE 6, SH per SE 2, CU per SH 8, active_cu_number 96
[    2.595375] amdgpu 0000:0d:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
[    2.595377] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
[    2.595377] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
[    2.595378] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
[    2.595378] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
[    2.595379] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
[    2.595379] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
[    2.595380] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
[    2.595381] amdgpu 0000:0d:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
[    2.595381] amdgpu 0000:0d:00.0: amdgpu: ring sdma0 uses VM inv eng 11 on hub 0
[    2.595382] amdgpu 0000:0d:00.0: amdgpu: ring sdma1 uses VM inv eng 12 on hub 0
[    2.595382] amdgpu 0000:0d:00.0: amdgpu: ring vcn_unified_0 uses VM inv eng 0 on hub 1
[    2.595383] amdgpu 0000:0d:00.0: amdgpu: ring vcn_unified_1 uses VM inv eng 1 on hub 1
[    2.595384] amdgpu 0000:0d:00.0: amdgpu: ring jpeg_dec uses VM inv eng 4 on hub 1
[    2.595384] amdgpu 0000:0d:00.0: amdgpu: ring mes_kiq_3.1.0 uses VM inv eng 13 on hub 0
[    2.602278] amdgpu 0000:0d:00.0: amdgpu: Using BACO for runtime pm
[    2.602575] [drm] Initialized amdgpu 3.49.0 20150101 for 0000:0d:00.0 on minor 0
[    2.610114] fbcon: amdgpudrmfb (fb0) is primary device
[    2.790455] amdgpu 0000:0d:00.0: [drm] fb0: amdgpudrmfb frame buffer device
[    3.391353] snd_hda_intel 0000:0d:00.1: bound 0000:0d:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
