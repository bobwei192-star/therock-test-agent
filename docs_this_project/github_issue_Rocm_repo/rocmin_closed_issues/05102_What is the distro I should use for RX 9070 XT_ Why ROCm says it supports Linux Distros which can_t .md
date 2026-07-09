# What is the distro I should use for RX 9070 XT? Why ROCm says it supports Linux Distros which can't even recognize RX 9070 XT due to outdated Kernel and Mesa?

- **Issue #:** 5102
- **State:** closed
- **Created:** 2025-07-25T12:20:32Z
- **Updated:** 2025-08-08T10:20:05Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5102

Hi,

I've been using Windows for the most part and I have tried hopping on to Linux after buying AMD GPU.

I wanted to try doing some AI experimenting with RX 9070 XT. I installed supported Ubuntu version, followed the guide on ROCm 6.4.1 and it didn't really work for me. Ubuntu 24.04.02 with 6.8 Kernel didn't recognize the GPU.

I've tried some other distros and landed on Arch Linux. Being bleeding edge with newer Kernel at least it recognizes the GPU. I tried installing ROCm from pacman repository and it also didn't work for me. Basically one of the packages for Python itself constantly failed to install. ROCm packages installed but no idea if they work.

To be honest I wanted to try out Fedora the most due to it being more recent than Ubuntu, and more secure by default than Arch. But then I learned Fedora 42 doesn't support 6.4.1 yet, and likely this version will be available with Fedora 43.

At this point I honestly have no idea what to do to use this GPU for AI. What distro should I try and what guide to follow. After following the official ROCm guide I've been pretty much stuck with chat GPT. And I am pretty disappointed in it since it has been pretty much 5 months since I have bought the GPU. All the stable recommended distros don't seem to support ROCm 6.4.1 or have outdated kernel for RX 9070 XT which means I am forced to use bleeding edge. I have worked with RTX 2060 before and it took some tinkering but it worked on Windows in the end.

There is only one video I have found where somebody has made it work on OpenSUSE and I am wondering if I should switch my distro completely to Tumbleweed just because of this video: https://youtu.be/yCCoQ72DBpM?si=-lJKNVMzD6fnZtt3