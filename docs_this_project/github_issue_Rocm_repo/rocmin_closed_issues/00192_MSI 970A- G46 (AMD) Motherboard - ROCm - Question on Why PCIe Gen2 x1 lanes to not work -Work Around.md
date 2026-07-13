# MSI 970A- G46 (AMD) Motherboard - ROCm - Question on Why PCIe Gen2 x1 lanes to not work -Work Around Found

- **Issue #:** 192
- **State:** closed
- **Created:** 2017-09-01T18:32:27Z
- **Updated:** 2017-10-17T14:01:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/192

Hello.

I am trying to use ROCm platform with amdgpu-pro-17.30.465504 drivers on my mining rig with 4 AMD GPUs (RX 470/480/570, mixed), motherboard MSI 970A- G46 (AMD), as remedy for lowered hashrate when mining with ETHash algorithm (the DAG issue). 

ROCm does seem to solve this issue (by adding `amdgpu.vm_fragment_size=9` to grub), however, my rig does not boot with 4 GPUs as usual, it only boots with 3 GPUs. I tried moving GPUs around the slots, it seems the problem is not the GPU count, but a certain PCIE 1x slot that causes ROCm to fail, but I'm not sure about this. After removing the 4th GPU the system gets all unstable and I have to reboot it several times (also using nomodeset option) to get it back to working state. If I choose previous kernel (4.4.0-62-generic) in grub menu, motherboard boots fine with 4 GPUs and works as intended.

The error msg I see in boot log with ROCm kernel and 4 GPUs looks something like this:

`AMD-Vi: Completion-Wait loop timed out` (lots of these messages)
`AMD-Vi: Event logged [IOTLB_INV_TIMEOUT] device=06:00.0 address=0x00000000798e0840` (these messages repeating for a while, then motherboard hangs dead exactly at this msg)

PCIE device #6 is actually the 4th GPU I am trying to add to that 1x slot.

Tried both BIOS and UEFI mode. All GPUs have vbios modded. I have 3 rigs with identical motherboards, and they all have this same issue. Tried moving GPUs around, same problem.