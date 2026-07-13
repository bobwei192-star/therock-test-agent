# rocm dkms on arch

- **Issue #:** 294
- **State:** closed
- **Created:** 2018-01-02T00:55:14Z
- **Updated:** 2021-01-05T10:02:03Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/294

Dear ROCm Team.

I am trying creating a aur PKG on arch for ROCm. As your work is really great, the arch community should benefit from it. For a good start i took the dkms package you are providing for ubuntu.
http://repo.radeon.com/rocm/apt/debian/pool/main/r/rocm-utils/rocm-utils_1.7.60_amd64.deb

As i understood the dependecies are small it should be doable easy? All includes files are in the package allready, no crossdeps so far. 

So i extracted the sources and brought em /usr/share and /usr/src. 

dkms add -m rock -v 1.7.60

worked and dkms is linking the dkms conf and sources right. 
Stupid as i am the next i tried just build it, which obviously failed :) - (dkms autoinstall)

the dmks buildlog is here https://pastebin.com/UuNRsEXQ
It looks like some vars arent defined. Where is it done in your package so i can adjust it for arch.

Maybe one of the more expirienced ones here can point me into the right direction?

Cheers
derdigge

PS: sorry for my bad english
