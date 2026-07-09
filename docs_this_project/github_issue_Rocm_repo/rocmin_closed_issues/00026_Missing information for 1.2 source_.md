# Missing information for 1.2 source?

- **Issue #:** 26
- **State:** closed
- **Created:** 2016-08-25T10:59:13Z
- **Updated:** 2017-01-03T19:17:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/26

Using the given command to download the RoCM 1.2 source does not work:

$ repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-1.2.0

curl: (22) The requested URL returned error: 404 Not Found
Server does not provide clone.bundle; ignoring.
fatal: Couldn't find remote ref refs/heads/roc-1.2.0
Unexpected end of command stream
