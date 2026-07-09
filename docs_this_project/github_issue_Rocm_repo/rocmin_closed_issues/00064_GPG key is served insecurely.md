# GPG key is served insecurely

- **Issue #:** 64
- **State:** closed
- **Created:** 2016-12-31T23:18:26Z
- **Updated:** 2017-12-17T19:05:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/64

The GPG key for the debian repository is served over an insecure connection (HTTP) and can be trivially changed using a man-in-the-middle attack.