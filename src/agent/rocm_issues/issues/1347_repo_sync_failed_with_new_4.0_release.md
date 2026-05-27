# repo sync failed with new 4.0 release

> **Issue #1347**
> **状态**: closed
> **创建时间**: 2020-12-19T20:58:26Z
> **更新时间**: 2020-12-23T05:57:50Z
> **关闭时间**: 2020-12-23T05:57:49Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1347

## 描述

Issue #1. 
Documentation still refers to 3.10.x. The version is static, therefore it appears to be forgotten whenever new release is launched. The newest source download therefore is always guessing game.
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code

Issue #2. 
this appears successful:
 ~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-4.0.x 

Once I did repo sync, it failed: 

repo sync
Traceback (most recent call last):
  File "/root/ROCm/.repo/repo/main.py", line 56, in <module>
    from subcmds.version import Version
  File "/root/ROCm/.repo/repo/subcmds/__init__.py", line 38, in <module>
    ['%s' % name])
  File "/root/ROCm/.repo/repo/subcmds/upload.py", line 27, in <module>
    from hooks import RepoHook
  File "/root/ROCm/.repo/repo/hooks.py", line 472
    file=sys.stderr)
        ^


---

## 评论 (6 条)

### 评论 #1 — Rmalavally (2020-12-20T00:31:58Z)

>Issue #1.
Documentation still refers to 3.10.x. The version is static, therefore it appears to be forgotten whenever new release is launched. The newest source download therefore is always guessing game.
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code

Thank you for the feedback. Please refresh the browser and review again. 

AMD ROCm Documentation Team

---

### 评论 #2 — gggh000 (2020-12-20T06:39:27Z)

I see it is updated to 4.0.x. However what is going to happen once for example 4.1 comes out? Same problem...??
Also I am still getting following error. see there are two issues mentioned in this:

repo has been initialized in /root
root@ubuntu-desktop:~# repo sync
Traceback (most recent call last):
  File "/root/.repo/repo/main.py", line 56, in <module>
    from subcmds.version import Version
  File "/root/.repo/repo/subcmds/__init__.py", line 38, in <module>
    ['%s' % name])
  File "/root/.repo/repo/subcmds/upload.py", line 27, in <module>
    from hooks import RepoHook
  File "/root/.repo/repo/hooks.py", line 472
    file=sys.stderr)


---

### 评论 #3 — ROCmSupport (2020-12-21T06:38:17Z)

Hi @gggh000 
I am not able to reproduce this. repo sync is perfect in my case.
I have Ubuntu 18.04.5 + Vega10(64CUs).

Can you please share some info related to OS and kernel.
And also please confirm whether repo sync is failing for other rocm versions also like 3.10 etc..
Thank you.

---

### 评论 #4 — gggh000 (2020-12-22T19:42:08Z)

here is the whole log with rocm4.0, I will try with 3.x or earlier version. However it was working.
(https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#getting-the-rocm-source-code)
root@vm-guest:~# cd
root@vm-guest:~# ls
root@vm-guest:~# mkdir -p ~/bin/
root@vm-guest:~# curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

Command 'curl' not found, but can be installed with:

apt install curl

root@vm-guest:~#
root@vm-guest:~# APT IN^Crl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
root@vm-guest:~# nohup apt install curl -y ; curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
nohup: ignoring input and appending output to 'nohup.out'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 39134  100 39134    0     0   212k      0 --:--:-- --:--:-- --:--:--  212k
root@vm-guest:~#
root@vm-guest:~# chmod a+x ~/bin/repo
root@vm-guest:~# mkdir -p ~/ROCm/
root@vm-guest:~# cd ~/ROCm/
root@vm-guest:~/ROCm#   git config --global user.email "you@example.com"
root@vm-guest:~/ROCm#   git config --global user.name "Your Name"
root@vm-guest:~/ROCm# ~/bin/repo init -u https://github.com/RadeonOpenCompute/ROCm.git -b roc-4.0.x

Your identity is: Your Name <you@example.com>
If you want to change this, please re-run 'repo init' with --config-name

Testing colorized output (for 'repo diff', 'repo status'):
  black    red      green    yellow   blue     magenta   cyan     white
  bold     dim      ul       reverse
Enable color display in this user account (y/N)? y

repo has been initialized in /root/ROCm
root@vm-guest:~/ROCm# repo sync

Command 'repo' not found, but can be installed with:

snap install git-repo  # version 1.12.37-3, or
apt  install repo

See 'snap info git-repo' for additional versions.

root@vm-guest:~/ROCm# apt install repo -y
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  python-kerberos
The following NEW packages will be installed:
  python-kerberos repo
0 upgraded, 2 newly installed, 0 to remove and 594 not upgraded.
Need to get 44.0 kB of archives.
After this operation, 129 kB of additional disk space will be used.
Get:1 http://ubuntu.osuosl.org/ubuntu bionic/universe amd64 python-kerberos amd64 1.1.14-1 [22.5 kB]
Get:2 http://ubuntu.osuosl.org/ubuntu bionic/universe amd64 repo all 1.12.37-3ubuntu1 [21.5 kB]
Fetched 44.0 kB in 0s (607 kB/s)
Selecting previously unselected package python-kerberos.
(Reading database ... 180088 files and directories currently installed.)
Preparing to unpack .../python-kerberos_1.1.14-1_amd64.deb ...
Unpacking python-kerberos (1.1.14-1) ...
Selecting previously unselected package repo.
Preparing to unpack .../repo_1.12.37-3ubuntu1_all.deb ...
Unpacking repo (1.12.37-3ubuntu1) ...
Setting up python-kerberos (1.1.14-1) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up repo (1.12.37-3ubuntu1) ...
root@vm-guest:~/ROCm# repo sync
Traceback (most recent call last):
  File "/root/ROCm/.repo/repo/main.py", line 56, in <module>
    from subcmds.version import Version
  File "/root/ROCm/.repo/repo/subcmds/__init__.py", line 38, in <module>
    ['%s' % name])
  File "/root/ROCm/.repo/repo/subcmds/upload.py", line 27, in <module>
    from hooks import RepoHook
  File "/root/ROCm/.repo/repo/hooks.py", line 472
    file=sys.stderr)
        ^
SyntaxError: invalid syntax
root@vm-guest:~/ROCm#


---

### 评论 #5 — gggh000 (2020-12-22T20:07:18Z)

I tried on different machine with slightly different ubuntu version and it works. I will sort out the difference. I think this can close now. 

---

### 评论 #6 — ROCmSupport (2020-12-23T05:57:49Z)

Thanks for the confirmation @gggh000 
Closing this now

---
