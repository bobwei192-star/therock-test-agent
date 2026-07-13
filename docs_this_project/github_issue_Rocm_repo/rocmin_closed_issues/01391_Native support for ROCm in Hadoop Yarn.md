# Native support for ROCm in Hadoop Yarn

- **Issue #:** 1391
- **State:** closed
- **Created:** 2021-02-22T10:38:19Z
- **Updated:** 2023-04-26T10:08:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/1391

Hi everybody,

In the Hadoop 3.x ecosystem there seems to be space for a native non-Nvidia GPU support, see:

https://issues.apache.org/jira/browse/YARN-10225
https://issues.apache.org/jira/browse/YARN-8891

From Hadoop 3.3.0 (still not released) it will be possible to create custom jars to support various devices, like new GPUs, something that for the moment is limited to Nvidia cards. I think that it would be great to have an official Hadoop plugin maintained by ROCm devs, that eventually may end up in Hadoop's main repo?

Hadoop users can still target ROCm GPUs via solutions like https://github.com/criteo/tf-yarn, but the Yarn scheduler will still be unware of GPUs as resources, so not really a fine grained solution. I'd be happy to help in case needed, this seems to be a very interesting project to reduce the monopoly from Nvidia :)

Thanks in advance!