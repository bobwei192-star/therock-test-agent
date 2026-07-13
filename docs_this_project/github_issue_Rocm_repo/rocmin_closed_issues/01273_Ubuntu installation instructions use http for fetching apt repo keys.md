# Ubuntu installation instructions use http for fetching apt repo keys

- **Issue #:** 1273
- **State:** closed
- **Created:** 2020-10-31T23:18:32Z
- **Updated:** 2020-12-11T05:29:41Z
- **URL:** https://github.com/ROCm/ROCm/issues/1273

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#installing-a-rocm-package-from-a-debian-repository

uses http, instead of https in the install instruction for fetching apt repo keys.

This is unsecure.

Please use https. From my test the server already serves files on https, so just update of the documentation (links and example how to use it), should be updated and it should work.

