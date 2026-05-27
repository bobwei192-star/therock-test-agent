# Linux Kernel Issue In 4.9: Booting into AMD ROCm Kernel - IRQ trap at vector 07 - Fixed in 1.6.1

> **Issue #162**
> **状态**: closed
> **创建时间**: 2017-07-16T20:57:18Z
> **更新时间**: 2017-07-25T19:36:44Z
> **关闭时间**: 2017-07-25T19:36:43Z
> **作者**: abgulati
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/162

## 描述

Hi!

I'm running Fedora 24 on a Ryzen 1700 + Gigabyte AB350 Gaming 3 board and on trying to boot into Fedora with ROCm kernel at boot time, the OS does not load, instead failing with a large recurring bunch of "IRQ trap at Vector 07" messages. Now having tried to install Ubuntu on this system this message isn't new to me as like many others with Gigabyte AM4 boards, I am unable to install Ubuntu 16.04 or 17.04, instead I see the recurring "IRQ trap at vector 07" messages. I believe some have mitigated this issue by recompiling the kernel for Ubuntu with AMD pinctrl disabled or other such workarounds. I am not familiar with recompiling kernels but will gladly learn and do whatever I can to assist in resolving this issue, given the appropriate guidance. I am technically proficient and qualified, just new to the Linux world!

If there is any further information I can provide please do let me know. I am eager to work on resolving the issue.

Regards!

---

## 评论 (8 条)

### 评论 #1 — gstoner (2017-07-16T22:25:21Z)

The team is going ROCm 1.6.1 release with patch for the Linux Kernel issue 

---

### 评论 #2 — abgulati (2017-07-17T03:34:38Z)

Okay Mr. Gregory that's perfect. Any way I can get involved? I would love to!

---

### 评论 #3 — jlgreathouse (2017-07-17T22:21:58Z)

Hi @abheekg13 

While you wait for a point-release of ROCm, the following steps may help you work around this problem. I have also included links to why these changes help, in case you want to know what's going on.

First and foremost, you will need to get your installation mechanism to boot (e.g. your Ubuntu 16.04.2 live image). One way to do this:

- When you are about to boot into the live disk, highlight "Install Ubuntu" and press 'e' on your keyboard
- Go down to the line that starts with `linux /casper/vmlinuz.efi` and replace `quiet splash` at the end with `acpi=off`
- Press F10 on your keyboard to continue booting.
([Why you do this](https://www.phoronix.com/forums/forum/linux-graphics-x-org-drivers/amd-linux/935547-amd-ryzen-on-linux/page4) -- [See this also](https://ubuntuforums.org/showthread.php?t=2354925&page=2&p=13627704#post13627704))

After you're in the Ubuntu installer, you should be able to install your OS like normal (though this may take longer than normal, since you only have one CPU core working at the moment).

Once you have installed Ubuntu, reboot the system. You will once again have to edit the GRUB boot command line to include `acpi=off` in order to boot into the OS.

- Hold down the shift key (or press escape during boot) to get to a GRUB menu
- Highlight "Ubuntu" and press 'e' on your keyboard.
- Go to the line that starts with `linux /boot/vmlinuz-4.8.0-58-generic.efi.signed` and change `quiet splash` to `acpi=off`.
- Press F10 on your keyboard to continue booting.

1. Update your base installation
1. [Download and install ROCm](https://github.com/RadeonOpenCompute/ROCm)
1. [Download the source code to this ROCm version's kernel (ROCK)](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/roc-1.6.0)
1. [Fixing the driver that causes this problem](https://patchwork.ozlabs.org/patch/766231/)
   1. You should use [this patch](https://github.com/RadeonOpenCompute/ROCm/files/1153719/fix_amd_irq.zip), rather than the version in the ozlabs.org link above; this message's patch is diffed based of the ROCK version of this file.
1. [Building this fixed kernel and installing it](https://kernelnewbies.org/KernelBuild)

```
# 1. Update base installation
sudo apt-get update
sudo apt-get -y upgrade

# 2. Download and install ROCm
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt-get update
sudo apt-get -y install rocm

# 3. Download the ROCK 1.6.0 source
sudo apt-get -y install git build-essential patch
git clone --depth=1 -b roc-1.6.x https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver.git
cd ROCK-Kernel-Driver

# 4. Fix the driver that causes this problem
wget https://github.com/RadeonOpenCompute/ROCm/files/1153719/fix_amd_irq.zip
unzip fix_amd_irq.zip
patch -Np1 -F1 --ignore-whitespace < ./fix_amd_irq.patch

# 5. Build and install the fixed kernel
sudo apt-get -y install libncurses5-dev gcc make git exuberant-ctags bc libssl-dev
make rock-rel_defconfig
make
sudo make modules_install install
sudo sed -i 's/GRUB_DEFAULT=0/GRUB_DEFAULT="1>3"/' /etc/default/grub
sudo update-grub2
```

At this point, you should reboot your system. You should be in a ROCm installation (`uname -r` should show `4.9.0-kfd+`) and have all the cores on your Ryzen processor working (e.g. `nproc` will return 16).

Note that the command in step 5 that builds the kernel is done with a single thread (since ACPI is off). This may take a while. However, once you're done, you should be able to boot normally, with all cores enabled, and ROCm 1.6 working.

---

### 评论 #4 — gstoner (2017-07-18T00:41:00Z)

@abheekg13  There are lot things to do.  I build out project list of stuff we need to do.  

---

### 评论 #5 — abgulati (2017-07-18T01:00:01Z)

Hello @jlgreathouse !

Thank you so very much for that detailed response, not only will this get me started with ROCm, but more importantly will give me the opportunity to learn and clear up a lot of "How to" questions in my head! I will follow the instructions in your post and report back as to my progress.

Thank you once again, Mr. Joseph!

---

### 评论 #6 — abgulati (2017-07-18T01:03:19Z)

Hello @gstoner I apologize if this is silly question, but where could I look at the list? I love AMD's open source approach WRT the machine learning platform and would love to contribute anyway I can.

---

### 评论 #7 — ratbuddy (2017-07-21T10:49:26Z)

Any time frame on the 1.6.1 release? Waiting for this fix :)

---

### 评论 #8 — gstoner (2017-07-25T19:36:43Z)

1.6.1  was released today 

---
