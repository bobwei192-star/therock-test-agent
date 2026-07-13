# Programs with ROCm drivers don't exit sucessfully

- **Issue #:** 857
- **State:** closed
- **Created:** 2019-08-05T01:04:29Z
- **Updated:** 2020-04-20T11:42:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/857

dkms status: amdgpu, 2.6-22, 4.15.0-55-generic, x86_64
gpu: 2 Vega 56, gfx900
cpu: AMD 1700 with X370

Hi, so every time I execute a program with rocm drivers, be HIP with tensorflow or OpenCL with Luxcore, the program doesn't exit successfully as if it is waiting in an infinite loop, but not consuming resources of the GPU (half of the GPU taches are on and it makes a scary coil whine and the watts consumed are like it is idling). It stops doing this after executing another program(and starts doing it again when it finishes), rebooting the computer, or executing a program and stop the execution of the program from terminal so it doesn't exit.

I have no idea how to debug GPUs so some help would be appreciated. This has been a recurrent problem with past ROCm releases and it occurs with the display GPU and the extra one, this doesn't occur with AMDGPU-pro OpenCL drivers.
