# Which OpenGL version did ROCm support?

- **Issue #:** 235
- **State:** closed
- **Created:** 2017-10-25T03:19:32Z
- **Updated:** 2018-06-03T15:15:29Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/235

Now I have built ROCK-Kernel-Driver, ROCT-Thunk-Interface and ROCR-Runtime from branch roc-1.6.3 on my ubunu16.04-arm64 server which is running on Cavium Thunder X.
then I install mesa with 'sudo apt-get install mesa-common-dev mesa-utils',  checking with 'glxinfo | grep OpenGL' , output is as follows:

OpenGL vendor string: VMware, Inc.
OpenGL renderer string: Gallium 0.4 on llvmpipe (LLVM 4.0, 128 bits)
OpenGL core profile version string: 3.3 (Core Profile) Mesa 17.0.7
OpenGL core profile shading language version string: 3.30
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
OpenGL version string: 3.0 Mesa 17.0.7
OpenGL shading language version string: 1.30
OpenGL context flags: (none)
OpenGL extensions:
OpenGL ES profile version string: OpenGL ES 3.0 Mesa 17.0.7
OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00
OpenGL ES profile extensions

I wonder if ROCm kernel driver support more higher version of OpenGL?