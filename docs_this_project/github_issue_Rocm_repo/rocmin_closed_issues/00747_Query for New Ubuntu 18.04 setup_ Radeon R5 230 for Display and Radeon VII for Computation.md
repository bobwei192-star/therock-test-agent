# Query for New Ubuntu 18.04 setup: Radeon R5 230 for Display and Radeon VII for Computation

- **Issue #:** 747
- **State:** closed
- **Created:** 2019-03-20T04:27:59Z
- **Updated:** 2019-08-07T16:49:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/747

Hello,

I'm awaiting the Radeon VII for my new home-lab PC that was assembled a few days ago. I attempted installing ROCm without the Radeon VII while I have the R5 230 right now. The 1080p display lost its original 1920x1080 resolution and dropped to a low resolution right after reboot . The rocminfo and clinfo commands would also show up errors. I later found that the ROCm installation had also removed the monitor.xml file located at $HOME/.config. As I still don't have the Radeon VII yet and that ROCm might not support the low-end card, I did not try any more troubleshooting attempts and reinstalled Ubuntu.

My query is regarding the installation procedure after I later connect the Radeon VII. As I would still be using the R5 230 for display, is it possible that this resolution issue will occur again? Is it not possible to keep the R5 230 graphics unaffected from the ROCm installation once the Radeon VII is there? Should I connect the Radeon VII to the display when installing ROCm? What about when I connect the display back again to the R5 230 after the ROCm installation?

My lab configuration:

ASUS Strix B450F Motherboard
AMD Ryzen 2700X CPU
Sapphire AMD Radeon R5 230 2GB DDR3 Graphics Card (For Display)
Sapphire AMD Radeon VII 16 GB HBM2 (Not connected yet)
Corsair 2x16 GB 3200 Mhz DDR4 RAM
WD Blue 500 GB M2 SSD
WD NAS Red 4 TB HDD
Corsair TX Gold 850M PSU
Corsair Spec 1 Case
ASUS 22" VZ229H Monitor

Thank you.

