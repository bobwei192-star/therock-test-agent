# Need more efficiency with new architecture graphics card of rdna3

- **Issue #:** 2215
- **State:** closed
- **Created:** 2023-06-02T01:53:10Z
- **Updated:** 2024-08-01T15:20:48Z
- **Labels:** hardware:Radeon
- **URL:** https://github.com/ROCm/ROCm/issues/2215



Could ROCm please make use of the AI units that are already present in their rdna3 graphics card, especially after announcing that their 7x40 CPU has AI units? The current stable diffusion calculations feel like they were made without relying on the AI units, with the XTX graphics card having a fp32 computational power of 61.4t and image generation speed of more than twice that of the 2060 graphics card's 6.4t. They're not even on the same level. I would like to know when ROCm will improve the software calls to the hardware efficiency of the new architecture graphics cards, especially since the Radeon Pro W7900 graphics card has also been released.