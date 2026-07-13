# ROCm doesn't support intel_iommu=on without iommu=pt

- **Issue #:** 597
- **State:** closed
- **Created:** 2018-11-02T01:34:30Z
- **Updated:** 2023-12-12T21:51:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/597

Are there any technical reasons for not supporting regular Intel IOMMU usage without passthrough-only mode? I don't see this problem/limitation documented anywhere.

Using an X99 chipset with IOMMU with full DMAR/interrupt-remapping/x2apic features, ROCm will only give protection faults, unless SWIOTLB is used instead of the IOMMU for any OpenCL-based apps. 

Anything that doesn't use ROCm works correctly in this situation.