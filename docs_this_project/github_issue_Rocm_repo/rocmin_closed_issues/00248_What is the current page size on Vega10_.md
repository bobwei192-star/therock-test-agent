# What is the current page size on Vega10?

- **Issue #:** 248
- **State:** closed
- **Created:** 2017-11-11T00:32:04Z
- **Updated:** 2018-06-03T15:13:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/248

I get this on my system:
$ dmesg | grep drm | grep fragment
[    1.568317] [drm] vm size is 262144 GB, block size is 9-bit,fragment size is 9-bit
[    2.670044] [drm] vm size is 262144 GB, block size is 9-bit,fragment size is 9-bit

I look in the code /drivers/gpu/drm/amd/amdgpu/gmc_v9_0.c:
```
	case CHIP_VEGA10:
		/* XXX Don't know how to get VRAM type yet. */
		adev->mc.vram_type = AMDGPU_VRAM_TYPE_HBM;
		/*
		 * To fulfill 4-level page support,
		 * vm size is 256TB (48bit), maximum size of Vega10,
		 * block size 512 (9bit)
		 */
		adev->vm_manager.vm_size = 1U << 18;
		adev->vm_manager.block_size = 9;
		adev->vm_manager.num_level = 3;
		amdgpu_vm_set_fragment_size(adev, 9);
		break;
	default:
		break;
	}

	DRM_INFO("vm size is %llu GB, block size is %u-bit,fragment size is %u-bit\n",
			adev->vm_manager.vm_size,
			adev->vm_manager.block_size,
			adev->vm_manager.fragment_size);
```

What does mean "block size 512 (9bit)" ? 
How does this relate to amdgpu.vm_fragment_size=9 in amdgpu to set 2M pages?
Or this comment incorrect?