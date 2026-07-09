# Fedora: leftover 70-kfd udev rule from rocm-dkms breaks initrd

- **Issue #:** 1133
- **State:** closed
- **Created:** 2020-06-05T21:09:18Z
- **Updated:** 2021-02-15T14:14:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1133

since having installed rocm-dkms rocm-runtime and friends, updated kernels do not boot and freeze at ["switching to amdgpudrmfb from EFI VGA"](https://lh3.googleusercontent.com/1GvQif_j2chmjV-EMBsn7uxGM_duRk-eMom6xDLe8M-EYWE6DO043PyoFkdXSk5dQNl-JBi3u8jX4A9RYUg-D8aDEhcPXriV-WLgqiXW6CFQBEnOv0fRAahKnhQuurVXIJfxi6AEdEsy2pnP-amtvVQcPuZwkmHy2c4q0CQOzjdwQoP02ZdDLcwyzfJjDv6FV6a6D-JHBe4_Xdrkxpw7fhuJlRMV1_tZKWg1hg-RidTx5aFvjloRDnAh2Pq6LWj7wfy7NPnpEVW94LsutT_SX5gMZkD6Pgftp6UrebLkA8AF2CdYRlMyxmtXZHTETU7DMcUxzFY6YpQY-t09Ub2n3PDZxiueTgD7Y4UVlIx5IKpF_rgF4afFDN2GPXzbA8gutZV8JTIzY1ec4F2iD1Ntq9LXr0JFVNYycrBn0HfPA7LBboNs8U2WwtPL4eKGj61C_bD0uXjWzHZEhoR-wtrmoWydU6Eb_vrKxkOK7KPSHigJYbxvvYNbc5UQi_JqpYKwzEkQrQZXMHOjqkYapxJJLsM2is67x5hianMxKJKTcbzgvJAFxooWPswEZcU6PVJbcVnjgpefi6VCmqC-XVHWraddussHhjK3_NkjtljM2ZmERO7ox59Jp6gZP7kyDjrGL6gSulB8PKATOLWwwz4JtIfBxVlUXNFKVboswTk8l2P9jzl33p6_kng-38F8N1s=w2616-h1962-no)

I've since uninstalled all rocm-* packages but the issue persists and I don't know what did the packages touch that screwed up the system. I'm having to stay at 5.6.13-300.fc32.x86_64 since newer versions freeze