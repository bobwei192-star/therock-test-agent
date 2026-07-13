# PCIe atomics on Asus ROG Zenith Extreme -- Threadripper

- **Issue #:** 451
- **State:** closed
- **Created:** 2018-07-07T02:12:37Z
- **Updated:** 2018-10-09T14:06:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/451

Hi again.

I can't seem to get PCIe atomics to tell me they are working on my new threadripper setup.  Here's the output from rocm/opecl/bin/clinfo

    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0

It isn't throwing any errors with kfd like it did the older drivers, but I'm thinking maybe that's because a change in the drivers?

Aaany-who.  I think I've gone through the motherboard's options with a fine tooth comb at this point and am not sure what else I can do ... so here I am :)  SVM, IOMMU, IOMMU-IVRS, PCIe-ARI enabled ...

Currently downloading tek's rocm-rippa 2 thing ... to see if I've somehow missed a kernel parameter or am missing some special sauce.


Other than that the drivers load and work just fine.  Though I'm seeing pretty much identical performance numbers (ethereum) as I did on my previous setup which was using 4x slots.... which I'm guessing is the atomics failing to do their magic.