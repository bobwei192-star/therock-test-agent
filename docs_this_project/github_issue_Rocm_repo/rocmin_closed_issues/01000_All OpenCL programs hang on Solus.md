# All OpenCL programs hang on Solus

- **Issue #:** 1000
- **State:** closed
- **Created:** 2020-01-16T20:25:53Z
- **Updated:** 2023-12-14T08:12:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1000

I'm currently trying to package ROC 2.10.0 for Solus and I ran into an issue, I'm using a RX5700XT with an AMD A10-6700 and I'm running kernel 5.4.8.

At the moment I think ROCr-Runtime is working fine as rocminfo reports my GPU correctly, I'm having a problem with ROCm-OpenCL-Runtime though. As soon as a program tries to start OpenCL it hangs and use 100% of a CPU core. For instance, clinfo hangs without printing anything and Blender becomes irresponsive when I try to open the settings panel (that's when it looks for OpenCL devices) I need to CTRL-C clinfo and kill blender or they won't ever exit.

Here are the logs I see you've asked in other posts:
[lspci -v](https://pastebin.com/LcMtu0UV)
[rocminfo](https://pastebin.com/Rm9LTthF)
[groups](https://pastebin.com/PfQPnQ3a)

[strace clinfo](https://pastebin.com/4AgDB6tF)
[ldd clinfo](https://pastebin.com/7T47YDqG)

As you can see in Solus we don't use /opt so all binaries and libs are in /usr/bin/ and /usr/lib64, the binaries and libs created by rocm-opencl-runtime are located in /usr/bin/rocm-opencl and /usr/bin/rocm-opencl but since rocminfo runs fine and the strace shows clinfo can find everything it needs to I don't think it's a problem