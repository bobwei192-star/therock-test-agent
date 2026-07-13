# Debian repository slow to access from Europe

- **Issue #:** 51
- **State:** closed
- **Created:** 2016-11-27T15:33:06Z
- **Updated:** 2017-07-02T17:15:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/51

Download speeds in Europe are 100 KB/s. I've mentioned this to Greg already. The issue is most like a mis-configuration of TCP stack parameters. Basically, the servers are allowing too few packets in flight and don't work well with high-latency networks. There's no need to add additional European servers or set up a CDN.