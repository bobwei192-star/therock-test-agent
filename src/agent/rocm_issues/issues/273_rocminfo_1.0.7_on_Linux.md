# rocminfo 1.0.7 on Linux 

> **Issue #273**
> **状态**: closed
> **创建时间**: 2017-12-20T00:49:31Z
> **更新时间**: 2018-07-31T15:48:02Z
> **关闭时间**: 2018-06-03T15:04:42Z
> **作者**: reanimastudios
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/273

## 描述

Just running the executable gives me this:

mdriftmeyer@horus:/opt/rocm/bin$ ./rocminfo 
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
mdriftmeyer@horus:/opt/rocm/bin$

Is this something to expect?

---

## 评论 (11 条)

### 评论 #1 — gstoner (2017-12-20T01:39:33Z)

Can you check your username is in gpu Unix permissions group

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Reanimality Studios <notifications@github.com>
Sent: Tuesday, December 19, 2017 6:49:33 PM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: [RadeonOpenCompute/ROCm] rocminfo 1.0.7 on Linux (#273)


Just running the executable gives me this:

mdriftmeyer@horus:/opt/rocm/bin$ ./rocminfo
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
mdriftmeyer@horus:/opt/rocm/bin$

Is this something to expect?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/273>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubFEt_Xn1yE71HflzBY1dDVsLErsks5tCFmdgaJpZM4RHwXI>.


---

### 评论 #2 — gstoner (2017-12-20T03:35:19Z)

sudo usermod -a -G video <username>   Here is the command 

---

### 评论 #3 — reanimastudios (2017-12-20T03:55:29Z)

mdriftmeyer@horus:~$ groups
mdriftmeyer cdrom floppy sudo audio dip video plugdev netdev bluetooth lpadmin scanner

btw: your command $ sudo usermod -a -G on Debian spits this to console:

mdriftmeyer@horus:~$ sudo usermod -a -G video
[sudo] password for mdriftmeyer: 
Usage: usermod [options] LOGIN

Options:
  -c, --comment COMMENT         new value of the GECOS field
  -d, --home HOME_DIR           new home directory for the user account
  -e, --expiredate EXPIRE_DATE  set account expiration date to EXPIRE_DATE
  -f, --inactive INACTIVE       set password inactive after expiration
                                to INACTIVE
  -g, --gid GROUP               force use GROUP as new primary group
  -G, --groups GROUPS           new list of supplementary GROUPS
  -a, --append                  append the user to the supplemental GROUPS
                                mentioned by the -G option without removing
                                him/her from other groups
  -h, --help                    display this help message and exit
  -l, --login NEW_LOGIN         new value of the login name
  -L, --lock                    lock the user account
  -m, --move-home               move contents of the home directory to the
                                new location (use only with -d)
  -o, --non-unique              allow using duplicate (non-unique) UID
  -p, --password PASSWORD       use encrypted password for the new password
  -R, --root CHROOT_DIR         directory to chroot into
  -s, --shell SHELL             new login shell for the user account
  -u, --uid UID                 new UID for the user account
  -U, --unlock                  unlock the user account
  -v, --add-subuids FIRST-LAST  add range of subordinate uids
  -V, --del-subuids FIRST-LAST  remove range of subordinate uids
  -w, --add-subgids FIRST-LAST  add range of subordinate gids
  -W, --del-subgids FIRST-LAST  remove range of subordinate gids
  -Z, --selinux-user SEUSER     new SELinux user mapping for the user accoun



---

### 评论 #4 — gstoner (2017-12-20T03:59:46Z)

Sorry need the full command   <username> is your username you use for login.

sudo usermod -a -G video <username>




---

### 评论 #5 — gstoner (2017-12-20T04:03:50Z)

Sorry, it looks like when using  "<" username ">" without the quotes github was not displaying it. 

---

### 评论 #6 — reanimastudios (2017-12-20T04:10:00Z)

mdriftmeyer@horus:/opt/rocm/bin$ sudo usermod -a -G video mdriftmeyer
mdriftmeyer@horus:/opt/rocm/bin$ groups
mdriftmeyer cdrom floppy sudo audio dip video plugdev netdev bluetooth lpadmin scanner
mdriftmeyer@horus:/opt/rocm/bin$ ./rocminfo 
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
mdriftmeyer@horus:/opt/rocm/bin$

---

### 评论 #7 — nickbuller (2017-12-20T09:37:56Z)

You need to logout and log back in.

---

### 评论 #8 — gstoner (2018-03-02T23:10:23Z)

@reanimastudios Can you try the beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2  It supports 4.13 Linux kernel 

---

### 评论 #9 — repletetop (2018-07-31T06:20:56Z)

I have save problem

---

### 评论 #10 — repletetop (2018-07-31T06:21:30Z)

Linux desktop 4.15.0-29-generic #31~16.04.1-Ubuntu SMP Wed Jul 18 08:54:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux


---

### 评论 #11 — jlgreathouse (2018-07-31T15:48:02Z)

Hello @repletetop 

Please submit a separate ticket about this, rather than piggybacking on an old, closed ticket. rocminfo failing in this way indicates that you may not have a successfully working ROCm installation.

In that ticket, please include the following:

- Your OS version
- Your Linux kernel version
- The model number of your CPU
- Your motherboard model, if possible
- The type of GPU(s) you are trying to use. Ideally, if you could indicate which PCIe slots they are installed in your motherboard, this may help us debug your problem
- The output of the following commands:
```
groups
```
```
lsmod | grep amdgpu
```
```
lsmod | grep amdkfd
```

```
lspci | grep VGA
```
```
mkdir ~/temp_lspci
cd ~/temp_lspci
wget https://mirrors.edge.kernel.org/pub/software/utils/pciutils/pciutils-3.6.1.tar.xz
tar -xf pciutils-3.6.1.tar.xz
cd pciutils-3.6.1
make -j `nproc`
sudo ./lspci -t
```
```
cd ~/temp_lspci/pciutils-3.6.1
sudo ./lspci -vv
```

Thank you.

---
