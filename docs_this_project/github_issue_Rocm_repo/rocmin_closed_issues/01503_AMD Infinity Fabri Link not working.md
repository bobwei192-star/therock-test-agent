# AMD Infinity Fabri Link not working 

- **Issue #:** 1503
- **State:** closed
- **Created:** 2021-06-24T10:28:45Z
- **Updated:** 2021-06-24T14:57:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1503

Hi everybody, 

here is my problem:

I have 2 gpu MI100 in my server and they are seen by the system:

========================== Link Type between two GPUs ==========================
GPU0 GPU1
GPU0 0 PCIE
GPU1 PCIE 0

*******************************

Instead, If I connect them with through a bridge (AMD Infinity Fabri Link) then the system doesn't see them anymore at all.

The bridge is a 4 slots bridge, but I have only 2 MI100, so, is it possible that having a 4 slots bridge for only 2 MI100 then it does not work?

regards