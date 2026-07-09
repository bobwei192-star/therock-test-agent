# openSUSE Tumbleweed + linux 5.0.8 small issue

- **Issue #:** 780
- **State:** closed
- **Created:** 2019-04-23T12:22:53Z
- **Updated:** 2023-12-18T18:55:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/780

Hello Folks,
I tried rpms of the rehl on openSUSE Tumbleweed with kernel 5.0.8 and RX 590.

There is this little issue about "pciutils-libs" dependency
opensuse has "pciutils". I ignored that and with yast installed "rocm-dkms" from yum repo.
So far no problem. 
/opt/rocm/bin/rocminfo
and
/opt/rocm/opencl/bin/x86_64/clinfo
both works

Kernel modules seems ok:
michael:/home/kemal # dmesg | grep kfd
[    5.456206] kfd kfd: Allocated 3969056 bytes on gart
[    5.456349] kfd kfd: added device 1002:67df
michael:/home/kemal # dkms status
amdgpu, 19.10-785424: added
amdgpu, 2.3-14.el7: added
 
I also compiled "hipBusBandwidth"  and executed it successfully.

In that sense, I believe making rocm rpms fully compatible with openSUSE Tumbleweed
will require very little work.
I hope you can find time to do this favor to us suse users.

Thanks for your time.
All the best...

Kemal

