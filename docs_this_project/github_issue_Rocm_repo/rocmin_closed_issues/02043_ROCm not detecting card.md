# ROCm not detecting card

- **Issue #:** 2043
- **State:** closed
- **Created:** 2023-04-13T23:39:20Z
- **Updated:** 2023-04-14T19:43:56Z
- **URL:** https://github.com/ROCm/ROCm/issues/2043

I was in the market to purchase a card, as I saw Pytorch offering install with rocm available, decided to get a 6950 XT. I re-installed pytorch with rocm with the following code.
`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2`
However
`torch.cuda.is_available()`
showed as False
I also ran, `sudo amdgpu-install --usecase=rocm`, but same result
I saw other people trying to troubleshoot run rocminfo, following was the output

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.33'not found (required by rocminfo)`

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34 not found (required by rocminfo)`

`rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version GLIBCXX_3.4.29 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version GLIBCXX_3.4.30 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version CXXABI_1.3.13 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.32 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

`rocminfo: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34 not found (required by /opt/rocm-5.4.3/bin/../lib/libhsa-runtime64.so.1)`

And this is where I first see probably cause of the problem?
I'm running Linux Mint 20, which is based on Ubuntu 20. Only way for me to upgrade to GLIB2.33 / 2.34 would be by upgrading to Linux Mint 21 (Ubuntu 22). Reading the AMD docs, it showed rocm5.4.2 is supported by Ubuntu 20

I'm not a computer scientists or an expert, is there an easy way to get rocm to run on Linux Mint 20? 
