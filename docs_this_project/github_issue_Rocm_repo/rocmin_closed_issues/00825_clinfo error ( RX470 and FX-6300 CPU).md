# clinfo error ( RX470 and FX-6300 CPU)

- **Issue #:** 825
- **State:** closed
- **Created:** 2019-06-20T06:13:59Z
- **Updated:** 2019-06-28T13:38:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/825

Hello there!
I have followed instructions on https://rocm.github.io/install.html to install the rocm on default Ubuntu 18.04.2 server to the letter. 

Everything installed well, but clinfo gives error, I guess it caused by that PCE-E thing because of very old CPU/mobo I have there. 

I then removed rocm and installed amdgpu-pro 19.20 drivers, it also installed very well, but same error on clinfo (ERROR: clGetPlatformIDs(-1001) ) ... 

I have working rocm on another machine (xeon  v3 and rx-470) ubuntu 18.04.2 desktop with no issues.  

I also had amdgpu-pro worked on same machine I have troubles now, but it was 16.04 I think, and not sure what version of amd drivers it was I think one+ year old.  

Any help would be very appreciated!