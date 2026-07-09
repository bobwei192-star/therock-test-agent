# miss tag on hcc when repo sync roc-3.3.0 to roc-3.1.0

- **Issue #:** 1078
- **State:** closed
- **Created:** 2020-04-08T03:04:53Z
- **Updated:** 2021-03-17T08:03:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1078

I meet a error , when I run repo sync 
#error: in `sync`: revision refs/tags/rocm-3.3.0 in hcc not found

root@k8snode:~/rocm3# ~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-3.3.0
.repo/manifests/: discarding 1 commits

If you want to change this, please re-run 'repo init' with --config-name

Testing colorized output (for 'repo diff', 'repo status'):
  black    red      green    yellow   blue     magenta   cyan     white 
  bold     dim      ul       reverse 
Enable color display in this user account (y/N)? 

repo has been initialized in /home/motech/rocm3

root@k8snode:~/rocm3# ~/bin/repo sync
error: in `sync`: revision refs/tags/rocm-3.3.0 in hcc not found
