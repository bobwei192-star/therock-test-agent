# URL returned error: 404 Not Found

- **Issue #:** 699
- **State:** closed
- **Created:** 2019-02-06T13:01:55Z
- **Updated:** 2019-02-06T13:42:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/699

I tried to clone the sourcecode as you describe on your github page and become a 404 Not Found:

Get https://gerrit.googlesource.com/git-repo/clone.bundle
Get https://gerrit.googlesource.com/git-repo
Get https://github.com/RadeonOpenCompute/ROCm.git
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (22) The requested URL returned error: 404 Not Found
Server does not provide clone.bundle; ignoring.
fatal: Couldn't find remote ref refs/heads/roc-2.1.0
fatal: Couldn't find remote ref refs/heads/roc-2.1.0
fatal: cannot obtain manifest https://github.com/RadeonOpenCompute/ROCm.git
error: in `sync`: [Errno 2] No such file or directory: '/home/erocm/ROCm/.repo/manifests/.git/HEAD'
error: manifest missing or unreadable -- please run init
