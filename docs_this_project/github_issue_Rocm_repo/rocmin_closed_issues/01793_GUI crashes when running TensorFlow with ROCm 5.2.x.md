# GUI crashes when running TensorFlow with ROCm 5.2.x

- **Issue #:** 1793
- **State:** closed
- **Created:** 2022-08-20T11:23:29Z
- **Updated:** 2024-03-16T03:10:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/1793

I want to perform training on my local computer using `tensorflow-rocm`, but currently it only works if I do it in a non-graphical view or stay at the login screen, while I SSH into the computer. This really defeats the purpose of training locally, as I then need my laptop to access and use TensorFlow on the desktop computer.

I suspect it might have something to do with video memory. When using `radeontop` it starts to consume all memory (shows it uses more than what is available)  when ever the smallest TensorFlow problem is started. This appears to be okay when in non-graphical mode, but using the GUI (Gnome 42) it freezes the GUI and crashes, and sends me back to the login screen (it logs me out). It also crashes the execution of the TensorFlow model/code, thus leaving me with nothing.

I have a Radeon VII installed with Ubuntu 22.04.1 LTS

[gui_dmesg.log](https://github.com/RadeonOpenCompute/ROCm/files/9386954/gui_dmesg.log)
[rocminfo.log](https://github.com/RadeonOpenCompute/ROCm/files/9386957/rocminfo.log)

Here is a simple example that fails to run in GUI mode, but runs without flaws and quickly in non-graphical mode.
[simple_example.zip](https://github.com/RadeonOpenCompute/ROCm/files/9386970/simple_example.zip)