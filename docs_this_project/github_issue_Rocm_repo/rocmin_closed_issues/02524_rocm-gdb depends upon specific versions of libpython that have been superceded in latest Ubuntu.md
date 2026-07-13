# rocm-gdb depends upon specific versions of libpython that have been superceded in latest Ubuntu

- **Issue #:** 2524
- **State:** closed
- **Created:** 2023-10-04T18:03:59Z
- **Updated:** 2024-11-27T15:29:20Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2524

In short, while starting debugging efforts for some code I am working on

``` 
jlandman@SCS-L-JLANDMAN:~$ ssh -X scruffy
Linux scruffy 6.1.0-10-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.38-1 (2023-07-14) x86_64
+---------------------------------------------------------------------+
|                                                                     |
|  ____                   __  __        scruffy.scalability.org       |
| / ___|  ___ _ __ _   _ / _|/ _|_   _                                |
| \___ \ / __| '__| | | | |_| |_| | | | 16 core threadripper +        |
|  ___) | (__| |  | |_| |  _|  _| |_| | AMD MI50 GPU         +        |
| |____/ \___|_|   \__,_|_| |_|  \__, | AMD 6600XT RDNA2 GPU          |
|                                 |___/                               |
|                                                                     |
+---------------------------------------------------------------------+

Last login: Wed Oct  4 13:46:15 2023 from 192.168.5.125
joe@scruffy:~$ sudo -s

root@scruffy:/home/joe# apt-get install  rocm-gdb
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-gdb : Depends: libpython3.10 but it is not installable or
                     libpython3.8 but it is not installable
E: Unable to correct problems, you have held broken packages.

root@scruffy:/home/joe# dpkg -l | grep libpython3 | grep Shared
ii  libpython3.11:amd64                     3.11.2-6                            amd64        Shared Python runtime library (version 3.11)

```

It seems that the requirement for libpython3.x should be for `.x >= 8`