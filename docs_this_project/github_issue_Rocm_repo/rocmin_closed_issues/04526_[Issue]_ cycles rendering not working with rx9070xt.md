# [Issue]: cycles rendering not working with rx9070xt

- **Issue #:** 4526
- **State:** closed
- **Created:** 2025-03-25T00:17:32Z
- **Updated:** 2025-04-25T14:18:19Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4526

i made report in
https://projects.blender.org/blender/blender/issues/136143
but i guess problem in rocm

cycles rendering not working in blender with rx9070xt 

System Information
os:arch linux 6.13.8
mesa 25.0.2-2
rocm-hip-runtime 6.3.3-1
gnome 48
windowing system wayland

GPU
RX 9070 XT

CPU
AMD Ryzen 7 9700X 

Blender Version
4.4.0 from official site

Exact steps for others to reproduce the error
open scene with textured object and press rendering
terminal says

Memory access fault by GPU node-1 (Agent handle: 0x7bc2d9de9e00) on address 0x2c95e7ee8000. Reason: Page not present or supervisor privilege.
Failed to read GPU memory: Input/output error

attaching scene with i have problem (actually i have problem in all my scenes)
https://projects.blender.org/attachments/0f9a2ba3-af6b-4b32-8899-17c16135ee52
no matter its just hip or hip rt, when selected igpu rdna2 there is no problems

also i tested lasted RadeonProRender in blender 4.3
and its also freezes and crashed with 9070 but not with igpu rdna2
