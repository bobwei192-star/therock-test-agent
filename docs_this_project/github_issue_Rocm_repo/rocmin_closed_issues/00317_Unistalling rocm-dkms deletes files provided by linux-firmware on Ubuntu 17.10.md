# Unistalling rocm-dkms deletes files provided by linux-firmware on Ubuntu 17.10

- **Issue #:** 317
- **State:** closed
- **Created:** 2018-01-30T17:32:51Z
- **Updated:** 2018-06-03T14:46:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/317

Steps to reproduce on ubuntu 17.10 

1. Ensure that you have ssh access to your machine otherwise you will be locked out later on.
2. Add the rocm ppa to your repository
3. Remove rocm and reinstall linux-firmware:
`apt remove rocm-opencl rocm-dkms`
`apt install --reinstall linux-firmware`
4. Verify that /var/lib/firmware/amdgpu is populated
`ls /lib/firmware/amdgpu/`
5. Install rocm and reboot: 
`apt install rocm-opencl rocm-dkms`
`reboot`
4. Remove rocm and reboot
`apt remove rocm-opencl rocm-dkms`
`apt autoremove -y`
`reboot`
5. Log in onto your machine using ssh.
6. Have a look at /var/lib/firmware/amdgpu: it's gone!
`ls /lib/firmware/amdgpu/`
7. Recover:
`apt install --reinstall linux-firmware`
`reboot`

