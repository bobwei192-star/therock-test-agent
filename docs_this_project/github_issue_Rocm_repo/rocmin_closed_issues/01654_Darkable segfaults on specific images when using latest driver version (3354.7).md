# Darkable segfaults on specific images when using latest driver version (3354.7)

- **Issue #:** 1654
- **State:** closed
- **Created:** 2022-01-03T19:20:22Z
- **Updated:** 2025-11-20T01:57:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1654

I am using latest opencl-amd on arch which is providing driver version 3354.7

[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/7803629/clinfo.txt)
A typical darktable start without crashes, I also don't see anything in the opencl output when it crashes
[dt-opencl.txt](https://github.com/RadeonOpenCompute/ROCm/files/7803656/dt-opencl.txt)

Bug is described here also with sample images to download:
https://github.com/darktable-org/darktable/issues/10778

The stacktrace of the bug:
https://www.toptal.com/developers/hastebin/elagijalow.yaml

And some more stacktraces in:
https://github.com/darktable-org/darktable/issues/10082

When I disable opencl the bug does not appear so I am quite sure it's a driver issues. Others with NVidia cards can't reproduce this either.

Is there anything else I can provide?