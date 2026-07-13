# Problems with Radeon VII in certain PCIe slot

- **Issue #:** 2156
- **State:** closed
- **Created:** 2023-05-21T15:26:09Z
- **Updated:** 2024-08-01T14:20:15Z
- **URL:** https://github.com/ROCm/ROCm/issues/2156

I have Radeon VII, Asus PRIME X570-P  board and AMD Ryzen 7 3700X.

When the GPU is in the first PCIe slot (x16, connected to CPU), everything works fine.

When the GPU is in the second PCIe slot (x4, connected to chipset), it does not work correctly. Stable diffusion fails with message "A tensor with all NaNs was produced in Unet".
It might be the same issue as https://github.com/RadeonOpenCompute/ROCm/issues/2055

I have minimized the pytorch reproducer to this:
```
import torch
device = torch.device("cuda" if (torch.cuda.is_available()) else "cpu")
data = torch.rand(3,3).float()
print('Initial Data nan', torch.any(torch.isnan(data)))
data = data.to(device)
print('Device Data nan', torch.any(torch.isnan(data)))
data = data.to("cpu")
print('CPU Data nan', torch.any(torch.isnan(data)))
```
It prints
```
Initial Data nan tensor(False)
Device Data nan tensor(True, device='cuda:0')
CPU Data nan tensor(False)
```

I haven't noticed any problems outside of pytorch, the rvs testsuite does not report  anything suspicious.

In the first PCIe slot the GPU works fine even with HSA_ENABLE_SDMA=0.

Tested on openSUSE Leap 15.4,  kernel 5.14.21-150400.24.60-default, amdgpu-dkms 1:6.0.5.50500-1581431,
the official torch-2.0.1+rocm5.4.2 (the same result with self-compiled torch against ROCm 5.5).

If I understand the documentation correctly, Radeon VII is supported, does not need  PCIe atomics and thus it should work
in any PCIe slot.

