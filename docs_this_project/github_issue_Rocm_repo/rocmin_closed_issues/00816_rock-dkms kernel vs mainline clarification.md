# rock-dkms kernel vs mainline clarification

- **Issue #:** 816
- **State:** closed
- **Created:** 2019-06-08T21:00:59Z
- **Updated:** 2019-09-20T08:31:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/816

`README.md` lists the differences between upstream kernel driver and `rock-dkms` but I find it a bit vague. Any help would be appreciated.

"Includes the latest GPU firmware"/"Does not include most up-to-date firmware", what firmware are we talking about? Where is it located?

"Features and hardware support varies depending on kernel version" exactly what features? Could you give some examples?

"IPC and RDMA capabilities are not yet enabled" When is this needed? I guess RDMA is needed when doing distributed computing with multiple separate physical machines? What about IPC? I can't seem to understand how the kernel driver is involved here.