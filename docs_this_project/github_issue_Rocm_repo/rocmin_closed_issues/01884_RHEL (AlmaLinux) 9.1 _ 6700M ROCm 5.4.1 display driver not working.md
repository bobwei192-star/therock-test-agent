# RHEL (AlmaLinux) 9.1 + 6700M ROCm 5.4.1 display driver not working

- **Issue #:** 1884
- **State:** closed
- **Created:** 2023-01-06T11:51:03Z
- **Updated:** 2024-05-23T18:27:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/1884

I have a notebook with a AMD Ryzen™ 9 5900HX CPU + 6700M GPU and want to implement rocALUTION in a CFD software and port another GPU application from cuda to HPI using rocThrust.

I installed ROCm 5.4.1 using the installer script:

Step 1:

RHEL v9.1

To download and install the installer for RHEL v9.1 distribution, type the following command:

sudo yum install https://repo.radeon.com/amdgpu-install/5.4.1/rhel/9.1/amdgpu-install-5.4.50401-1.el9.noarch.rpm  

Step 2:

sudo amdgpu-install --usecase=dkms,graphics,opencl,hip,rocm,hiplibsdk 


When rebooting, the display resolution is different and I get a message screen telling me, that something went wrong and that I should contact the system administrator. The boot process stops at that point.

Booting an old kernel (RHEL (AlmaLinux) 9.0), uninstalling ROCm and rebooting fixes the RHEL (AlmaLinux) 9.1 boot issue so I assume it's the display driver that's not installed properly when installing ROCm. 

Is there a known fix for that?

What usecases are actually needed to develop rocALUTION based applications running on the GPU and applications using rocThrust running on the GPU? dkms,graphics,opencl,hip,rocm,hiplibsdk is certainly overkill but I wanted to make sure I don't miss something.