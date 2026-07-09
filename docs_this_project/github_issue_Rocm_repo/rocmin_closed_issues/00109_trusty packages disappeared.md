# trusty packages disappeared

- **Issue #:** 109
- **State:** closed
- **Created:** 2017-05-02T08:35:34Z
- **Updated:** 2017-05-04T07:00:12Z
- **URL:** https://github.com/ROCm/ROCm/issues/109

Hi - 
I just noticed that the trusty packages disappeared. 

```
$ sudo aptitude update
#...
Ign http://packages.amd.com trusty/main Translation-en_US
Ign http://packages.amd.com trusty/main Translation-en
Err http://packages.amd.com trusty/main amd64 Packages
  404  Not Found
Fetched 72 B in 3s (22 B/s)  
W: Failed to fetch http://packages.amd.com/rocm/apt/debian/dists/trusty/main/binary-amd64/Packages: 404  Not Found
E: Some index files failed to download. They have been ignored, or old ones used instead.
E: Couldn't rebuild package cache
```
and indeed, I can see only xenial binaries (tagged 1.5 !!) on the server mentioned above. will trusty not be supported anymore for 1.5 and upwards?