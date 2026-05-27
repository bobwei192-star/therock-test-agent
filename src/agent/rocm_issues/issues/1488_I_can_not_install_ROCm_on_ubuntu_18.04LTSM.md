# I can not install ROCm on ubuntu 18.04LTSM

> **Issue #1488**
> **状态**: closed
> **创建时间**: 2021-06-03T12:28:37Z
> **更新时间**: 2021-06-07T04:19:13Z
> **关闭时间**: 2021-06-06T07:52:48Z
> **作者**: BahramianArmin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1488

## 描述

I do this way :
sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt install rocm-dkms
      Reading package lists... Done
      Building dependency tree       
      Reading state information... Done
      Some packages could not be installed. This may mean that you have
      requested an impossible situation or if you are using the unstable
      distribution that some required packages have not yet been created
      or been moved out of Incoming.
      The following information may help to resolve the situation:
      
      The following packages have unmet dependencies:
       rocm-dkms : Depends: rocm-dev but it is not going to be installed
      E: Unable to correct problems, you have held broken packages.

how can i solved this problems?

---

## 评论 (14 条)

### 评论 #1 — xuhuisheng (2021-06-03T12:38:32Z)

should run 'sudo apt update' again

---

### 评论 #2 — ROCmSupport (2021-06-04T07:44:26Z)

Thanks @BahramianArmin for reaching out.
Before installing rocm (I mean after mapping repo), you need to give "sudo apt update".
So request you to follow like below.

_wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
sudo apt update
sudo apt install rocm-dkms_

Hope this helps.
If the issue is resolved for you, help us by closing this ticket.
Thank you very much.


---

### 评论 #3 — BahramianArmin (2021-06-04T08:18:07Z)

> should run 'sudo apt update' again

Thank for your attention to this issue 
I do your option but 
it dose not wrok again
same error...

---

### 评论 #4 — BahramianArmin (2021-06-04T08:20:27Z)

> Thanks @BahramianArmin for reaching out.
> Before installing rocm (I mean after mapping repo), you need to give "sudo apt update".
> So request you to follow like below.
> 
> _wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add - echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list sudo apt update sudo apt install rocm-dkms_
> 
> Hope this helps.
> If the issue is resolved for you, help us by closing this ticket.
> Thank you very much.

Thank for your  professional behavior 
I run all of thing you say an again i have a same problems:
I copy below the here entirely:

wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
[sudo] password for armin: 
OK
deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main
(base) ➜  ~ sudo apt update
Ign:1 cdrom://Kubuntu 18.04.5 LTS _Bionic Beaver_ - Release amd64 (20200806.1) bionic InRelease
Err:2 cdrom://Kubuntu 18.04.5 LTS _Bionic Beaver_ - Release amd64 (20200806.1) bionic Release
  Please use apt-cdrom to make this CD-ROM recognized by APT. apt-get update cannot be used to add new CD-ROMs
Hit:3 http://deb.anydesk.com all InRelease
Hit:4 http://archive.ubuntu.com/ubuntu bionic InRelease                                     
Hit:5 http://ppa.launchpad.net/gladky-anton/lammps/ubuntu bionic InRelease                  
Hit:6 http://packages.microsoft.com/repos/edge stable InRelease                             
Hit:7 http://archive.canonical.com/ubuntu bionic InRelease                                  
Get:8 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]                   
Hit:9 http://ppa.launchpad.net/linrunner/tlp/ubuntu bionic InRelease                        
Get:11 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                
Hit:12 http://deb.playonlinux.com bionic InRelease                                          
Get:13 http://packages.microsoft.com/repos/code stable InRelease [10.4 kB]                  
Hit:14 http://repository.spotify.com stable InRelease                                       
Hit:15 http://archive.canonical.com bionic InRelease                                        
Get:10 https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04 ./ InRelease [1,559 B]
Hit:16 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic InRelease                  
Get:17 https://mega.nz/linux/MEGAsync/xUbuntu_18.04 ./ InRelease [2,473 B]                  
Get:18 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                
Hit:19 https://repo.radeon.com/rocm/apt/debian ubuntu InRelease                             
Get:20 http://archive.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                 
Hit:21 https://download.docker.com/linux/ubuntu bionic InRelease                            
Hit:22 http://ppa.launchpad.net/malteworld/ppa/ubuntu bionic InRelease                      
Hit:23 http://dl.google.com/linux/chrome/deb stable InRelease                               
Ign:24 http://ppa.launchpad.net/me-davidsansome/clementine/ubuntu bionic InRelease          
Get:25 http://packages.microsoft.com/repos/code stable/main armhf Packages [31.6 kB]        
Err:10 https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04 ./ InRelease
  The following signatures were invalid: EXPKEYSIG DFA175A75104960E Emulators OBS Project <Emulators@build.opensuse.org>
Hit:26 http://ppa.launchpad.net/nm-l2tp/network-manager-l2tp/ubuntu bionic InRelease        
Get:27 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [2,097 kB]       
Hit:28 http://ppa.launchpad.net/oibaf/graphics-drivers/ubuntu bionic InRelease              
Get:29 http://packages.microsoft.com/repos/code stable/main amd64 Packages [30.8 kB]        
Get:30 http://packages.microsoft.com/repos/code stable/main arm64 Packages [31.8 kB]        
Hit:31 http://ppa.launchpad.net/openkim/latest/ubuntu bionic InRelease                      
Get:32 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [48.5 kB]
Hit:33 http://ppa.launchpad.net/otto-kesselgulasch/gimp/ubuntu bionic InRelease             
Hit:35 http://ppa.launchpad.net/teejee2008/ppa/ubuntu bionic InRelease                      
Get:36 http://security.ubuntu.com/ubuntu bionic-security/universe Translation-en [255 kB]   
Hit:37 http://ppa.launchpad.net/thopiekar/sierrabreeze/ubuntu bionic InRelease              
Get:38 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [60.3 kB]
Hit:39 http://ppa.launchpad.net/ubuntuhandbook1/audacity/ubuntu bionic InRelease            
Get:40 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]
Err:41 http://ppa.launchpad.net/me-davidsansome/clementine/ubuntu bionic Release            
  404  Not Found [IP: 91.189.95.85 80]
Get:42 http://archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages [1,298 kB]        
Ign:34 https://davidbailey00.fury.land/apt  InRelease                                       
Ign:43 https://davidbailey00.fury.land/apt  Release                                         
Ign:44 https://notion.davidbailey.codes/debs  Packages                          
Ign:44 https://davidbailey00.fury.land/apt  Packages                            
Ign:45 http://as-repository.openvpn.net/as/debian bionic InRelease                          
Err:47 http://as-repository.openvpn.net/as/debian bionic Release                            
  404  Not Found [IP: 10.10.34.35 80]
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                             
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                     
Get:49 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [294 kB]
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                                
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                                  
Get:50 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1,735 kB]   
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                                
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                                  
Get:44 https://davidbailey00.fury.land/apt  Packages [1,530 B]                              
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                             
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                   
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                    
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                      
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                                
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                      
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                             
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                   
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                    
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                      
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                      
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                        
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                             
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                     
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                                
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                        
Get:52 http://archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages [1,567 kB]    
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                                
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                                  
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                             
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                               
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                                
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                      
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                    
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                      
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                 
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                   
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                                
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                        
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                      
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                        
Get:53 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [289 kB]
Ign:46 https://notion.davidbailey.codes/debs  Translation-en_US                             
Ign:46 https://davidbailey00.fury.land/apt  Translation-en_US                               
Get:54 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 Packages [26.6 kB]  
Get:55 http://archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,468 B]
Get:56 http://archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [9,292 B]
Ign:48 https://notion.davidbailey.codes/debs  Translation-en                                
Ign:48 https://davidbailey00.fury.land/apt  Translation-en                                  
Ign:51 https://notion.davidbailey.codes/debs  Translation-fa                                
Ign:51 https://davidbailey00.fury.land/apt  Translation-fa                                  
Err:57 http://dl.winehq.org/wine-builds/ubuntu bionic InRelease                             
  Connection failed [IP: 151.101.14.217 80]
Reading package lists... Done
E: The repository 'cdrom://Kubuntu 18.04.5 LTS _Bionic Beaver_ - Release amd64 (20200806.1) bionic Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04 ./ InRelease: The following signatures were invalid: EXPKEYSIG DFA175A75104960E Emulators OBS Project <Emulators@build.opensuse.org>
W: Target Packages (stable/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Packages (stable/binary-all/Packages) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Translations (stable/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Translations (stable/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Translations (stable/i18n/Translation-fa) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11 (stable/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11 (stable/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons-small (stable/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons (stable/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons-hidpi (stable/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons-large (stable/dep11/icons-128x128.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target CNF (stable/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target CNF (stable/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
E: The repository 'http://ppa.launchpad.net/me-davidsansome/clementine/ubuntu bionic Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
E: The repository 'http://as-repository.openvpn.net/as/debian bionic Release' no longer has a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: Target Packages (stable/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Packages (stable/binary-all/Packages) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Translations (stable/i18n/Translation-en_US) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Translations (stable/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target Translations (stable/i18n/Translation-fa) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11 (stable/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11 (stable/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons-small (stable/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons (stable/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons-hidpi (stable/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target DEP-11-icons-large (stable/dep11/icons-128x128.tar) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target CNF (stable/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
W: Target CNF (stable/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1
(base) ➜  ~ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dkms : Depends: rocm-dev but it is not going to be installed
E: Unable to correct problems, you have held broken packages.




---

### 评论 #5 — BahramianArmin (2021-06-04T08:29:14Z)

my kernel version is : 
Linux 5.4.0-74-generic x86_64
Thanks for  your attentions


---

### 评论 #6 — ROCmSupport (2021-06-04T08:45:28Z)

Hi @BahramianArmin 
Thanks.
Looks like update did not go well.
I found from your log that you are trying it on "Kubuntu" OS.
The way you network is configured to the harddisc/system is also doubtful as its showing "connection failed" error.
**Can you please check your environment once.**

Connection failed [IP: 151.101.14.217 80]
Reading package lists... Done
E: The repository 'cdrom://Kubuntu 18.04.5 LTS Bionic Beaver - Release amd64 (20200806.1) bionic Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04 ./ InRelease: The following signatures were invalid: EXPKEYSIG DFA175A75104960E Emulators OBS Project Emulators@build.opensuse.org
W: Target Packages (stable/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list:59 and /etc/apt/sources.list.d/docker.list:1

---

### 评论 #7 — BahramianArmin (2021-06-04T09:19:45Z)

thanks a again:
i fix it all of them ....
and run the below sequence agaain:
  wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
  echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
  sudo apt update
  sudo apt install rocm-dkms

and this happend:
 wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
OK
deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main
(base) ➜  ~ sudo apt update
Hit:1 http://dl.google.com/linux/chrome/deb stable InRelease                                
Hit:2 http://deb.anydesk.com all InRelease                                                  
Hit:3 http://dl.winehq.org/wine-builds/ubuntu bionic InRelease                              
Hit:4 http://packages.microsoft.com/repos/edge stable InRelease                             
Hit:5 http://repository.spotify.com stable InRelease                                        
Hit:6 http://ppa.launchpad.net/linrunner/tlp/ubuntu bionic InRelease                        
Hit:7 http://archive.canonical.com/ubuntu bionic InRelease                                  
Hit:8 http://archive.ubuntu.com/ubuntu bionic InRelease                                     
Hit:9 http://packages.microsoft.com/repos/code stable InRelease                             
Hit:10 http://archive.canonical.com bionic InRelease                                        
Hit:11 http://archive.ubuntu.com/ubuntu bionic-updates InRelease                            
Get:12 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                
Hit:13 http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic InRelease                  
Get:14 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                
Get:15 https://mega.nz/linux/MEGAsync/xUbuntu_18.04 ./ InRelease [2,473 B]                  
Hit:16 https://repo.radeon.com/rocm/apt/debian ubuntu InRelease                             
Hit:17 http://ppa.launchpad.net/malteworld/ppa/ubuntu bionic InRelease                      
Get:18 http://archive.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                 
Hit:19 http://ppa.launchpad.net/nm-l2tp/network-manager-l2tp/ubuntu bionic InRelease        
Hit:20 http://ppa.launchpad.net/oibaf/graphics-drivers/ubuntu bionic InRelease 
Hit:21 http://ppa.launchpad.net/openkim/latest/ubuntu bionic InRelease         
Hit:22 http://ppa.launchpad.net/otto-kesselgulasch/gimp/ubuntu bionic InRelease
Hit:23 http://ppa.launchpad.net/teejee2008/ppa/ubuntu bionic InRelease         
Hit:24 http://ppa.launchpad.net/thopiekar/sierrabreeze/ubuntu bionic InRelease 
Hit:25 http://ppa.launchpad.net/ubuntuhandbook1/audacity/ubuntu bionic InRelease
Fetched 254 kB in 5s (48.7 kB/s)                   
Reading package lists... Done
Building dependency tree       
Reading state information... Done
3 packages can be upgraded. Run 'apt list --upgradable' to see them.
(base) ➜  ~ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 rocm-dkms : Depends: rocm-dev but it is not going to be installed
E: Unable to correct problems, you have held broken packages.

---

### 评论 #8 — ROCmSupport (2021-06-04T12:42:24Z)

Very strange to see that. Can you please the config details like OS and Asic etc.,.

I am able to install ROCm 4.2 on **Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-73-generic x86_64)** like below.

master@prj47-rack-43:/opt$ wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -
OK
master@prj47-rack-43:/opt$
master@prj47-rack-43:/opt$ echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list
deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ ubuntu main

master@prj47-rack-43:/opt$ sudo apt update
Hit:1 http://us.archive.ubuntu.com/ubuntu bionic InRelease
Get:2 http://us.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
Get:3 https://repo.radeon.com/rocm/apt/debian ubuntu InRelease [1,811 B]
Get:4 http://us.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]
Get:5 https://repo.radeon.com/rocm/apt/debian ubuntu/main amd64 Packages [18.3 kB]  u
Get:6 http://us.archive.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
Fetched 272 kB in 1s (280 kB/s)                               d
Reading package lists... Done
Building dependency tree
Reading state information... Done
76 packages can be upgraded. Run 'apt list --upgradable' to see them.

master@prj47-rack-43:/opt$ sudo apt install rocm-dkms
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  comgr dkms hip-base hip-doc hip-rocclr hip-samples hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libbabeltrace-ctf1 libbabeltrace1
  libdrm-dev libdw1 libelf-dev libfile-basedir-perl libfile-copy-recursive-perl libfile-listing-perl libfile-which-perl libhttp-date-perl
  libipc-system-simple-perl libpthread-stubs0-dev libpython3.8 libpython3.8-minimal libpython3.8-stdlib libtimedate-perl liburi-encode-perl libx11-dev
  libx11-doc libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu mesa-common-dev openmp-extras rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake
  rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs rocm-gdb rocm-opencl rocm-opencl-dev rocm-smi-lib rocm-utils rocminfo rocprofiler-dev roctracer-dev
  x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev zlib1g-dev
Suggested packages:
  menu libxcb-doc
The following NEW packages will be installed:
  comgr dkms hip-base hip-doc hip-rocclr hip-samples hsa-amd-aqlprofile hsa-rocr-dev hsakmt-roct hsakmt-roct-dev libbabeltrace-ctf1 libbabeltrace1
  libdrm-dev libdw1 libelf-dev libfile-basedir-perl libfile-copy-recursive-perl libfile-listing-perl libfile-which-perl libhttp-date-perl
  libipc-system-simple-perl libpthread-stubs0-dev libpython3.8 libpython3.8-minimal libpython3.8-stdlib libtimedate-perl liburi-encode-perl libx11-dev
  libx11-doc libxau-dev libxcb1-dev libxdmcp-dev llvm-amdgpu mesa-common-dev openmp-extras rock-dkms rock-dkms-firmware rocm-clang-ocl rocm-cmake
  rocm-dbgapi rocm-debug-agent rocm-dev rocm-device-libs rocm-dkms rocm-gdb rocm-opencl rocm-opencl-dev rocm-smi-lib rocm-utils rocminfo rocprofiler-dev
  roctracer-dev x11proto-core-dev x11proto-dev xorg-sgml-doctools xtrans-dev zlib1g-dev
0 upgraded, 57 newly installed, 0 to remove and 76 not upgraded.
Need to get 671 MB of archives.
After this operation, 775 MB of additional disk space will be used.
Do you want to continue? [Y/n] y


---

### 评论 #9 — BahramianArmin (2021-06-04T14:53:31Z)

I do all of thing that may important
But it still not work.... 

---

### 评论 #10 — BahramianArmin (2021-06-04T14:57:57Z)

Do you have any option why not install dependencies!?? 

---

### 评论 #11 — seesturm (2021-06-04T16:33:23Z)

Based on the messages it is hard to tell why apt does not attempt install of rocm-dev. Maybe you get more hints if you explicitly ask apt to install rocm-dev like so
`sudo apt install rocm-dkms rocm-dev`

---

### 评论 #12 — BahramianArmin (2021-06-06T07:50:01Z)

> Based on the messages it is hard to tell why apt does not attempt install of rocm-dev. Maybe you get more hints if you explicitly ask apt to install rocm-dev like so
> `sudo apt install rocm-dkms rocm-dev`

I do also this way But still not work!


---

### 评论 #13 — BahramianArmin (2021-06-06T07:52:48Z)

I do lots of things and finally I use 'aptitude' to install and it works!! :D 
Thanks a lot from every one for helping !

---

### 评论 #14 — ROCmSupport (2021-06-06T10:26:48Z)

Good to know that your issue is resolved.
I hope aptitude is the only packaging tool for ubuntu, anyway thanks for the closure.

---
