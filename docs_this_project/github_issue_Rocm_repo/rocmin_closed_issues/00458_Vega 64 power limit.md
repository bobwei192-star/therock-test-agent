# Vega 64 power limit

- **Issue #:** 458
- **State:** closed
- **Created:** 2018-07-15T12:09:43Z
- **Updated:** 2018-12-24T22:49:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/458

Hi, 
In ROCm-SMI a OC function was implemented. There is possibility to change clock profile for GPU and memory ( does not work) and OC the highest GPU profile by setting --setoverdrive %. But in my case almost non of this does not matter because there is power limit of 220W. 
Is there any way to pass this 220W? Any extra power limit extension?

Recently I flashed my card with Vega 64 LC edition bios. There is a limit to 264W but still, I cannot use the full capability of the card and I am the stack to 1560MHz. This card is working flawlessly at 1770Mhz @365W so I am losing a lot of computing power. 
GPU voltage control would also be a very nice feature.