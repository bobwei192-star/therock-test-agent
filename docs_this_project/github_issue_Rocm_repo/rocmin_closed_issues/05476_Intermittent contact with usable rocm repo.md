# Intermittent contact with usable rocm repo

- **Issue #:** 5476
- **State:** closed
- **Created:** 2025-10-07T11:53:08Z
- **Updated:** 2025-10-14T14:53:11Z
- **Labels:** status: fix submitted
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5476

Hi,

Since last week I have been experiencing increasing difficulty using the ROCm repo at

https://repo.radeon.com/rocm/el9/latest/main

Occasionally, I can access this successfully but I am now repeatedly receiving download errors like the following:

`dnf --refresh --enablerepo=ROCm list rocm
AMD ROCm repository                                                                                               2.2 kB/s | 1.1 kB     00:00    
Errors during downloading metadata for repository 'ROCm':
  - Status code: 404 for https://repo.radeon.com/rocm/el9/latest/main/repodata/83977142cdd069243fe3e3bdd41cbff686dbe6c1dfccdf6496b5c25141baab49-primary.xml.gz (IP: 23.48.165.4)
  - Status code: 404 for https://repo.radeon.com/rocm/el9/latest/main/repodata/5e84f1ad7df04733eda63d4fe25ccf18a114570dbf58ea9117c482a0811a5ca5-filelists.xml.gz (IP: 23.48.165.4)
Error: Failed to download metadata for repo 'ROCm': Yum repo downloading error: Downloading error(s): repodata/83977142cdd069243fe3e3bdd41cbff686dbe6c1dfccdf6496b5c25141baab49-primary.xml.gz - Cannot download, all mirrors were already tried without success; repodata/5e84f1ad7df04733eda63d4fe25ccf18a114570dbf58ea9117c482a0811a5ca5-filelists.xml.gz - Cannot download, all mirrors were already tried without success
`
I believe the repos on at least the ip addresses 23.1.96.192, 23.48.165.4, 23.48.165.31, 2.19.248.134, 2.19.248.149 may be missing some files under repodata. This is making it very difficult to install the latest ROCm on the MI300X boxes we have in Cambridge.

Many thanks for your attention -

Best regards

Stuart
