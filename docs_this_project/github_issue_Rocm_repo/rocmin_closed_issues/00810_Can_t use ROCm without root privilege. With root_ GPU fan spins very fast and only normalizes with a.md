# Can't use ROCm without root privilege. With root, GPU fan spins very fast and only normalizes with a complete shutdown

- **Issue #:** 810
- **State:** closed
- **Created:** 2019-06-04T01:09:05Z
- **Updated:** 2019-06-05T02:04:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/810

Applications run as normal user cannot detect `amdocl64` and make use of my GPU. Running them as root allows them to use the GPU, but introduces a problem with the GPU fan. It starts spinning unusually fast and do not stop until a reboot is performed.

[See this issue](https://github.com/hashcat/hashcat/issues/2050). I am running Ubuntu 18.04.2 with an AMD RX 560 4GB graphics device.

My user is part of the **video** group. I have followed [these instructions](https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository) precisely.