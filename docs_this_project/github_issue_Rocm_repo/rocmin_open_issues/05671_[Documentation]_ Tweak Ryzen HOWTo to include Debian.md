# [Documentation]: Tweak Ryzen HOWTo to include Debian

- **Issue #:** 5671
- **State:** open
- **Created:** 2025-11-17T05:53:04Z
- **Updated:** 2025-12-11T15:17:19Z
- **Labels:** status: triage
- **Assignees:** tcgu-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5671

### Description of errors

Just walking through the online docs to see how they line up with my own best practice on Debian 13 for the Strix Halo. 

I noticed the [Linux HOWTO page](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/install/installryz/native_linux/install-ryzen.html#prepare-the-system) opens with 

`sudo apt update && sudo apt-get install linux-oem-24.04c`

Since this page is Ubuntu-only, it might be good to switch to the tabbed OS approach to broaden procedures for the other ROCm supported distibutions.  Debian 13 already ships the default kernel with the [MES kernel fixes](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1118658). 

The Debian 13 Trixie equivalent is

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/7.1/ubuntu/noble/amdgpu-install_7.1.70100-1_all.deb
sudo apt install ./amdgpu-install_7.1.70100-1_all.deb
sudo amdgpu-install -y --usecase=rocm
sudo mokutil --import /var/lib/dkms/mok.pub  # Add DKMS MOK key, enter a password for prompt on reboot w/ Secure Boot
sudo dpkg-reconfigure amdgpu-dkms  #Rebuild initramfs with signed modules
sudo usermod -a -G render,video $LOGNAME
sudo reboot   # Reboot enroll MOK key to pass Secure Boot
```



### Attach any links, screenshots, or additional evidence you think will be helpful.

The following convienently allows all the memory to be used by the GPU for AI workloads on all amdgpu versions (including future distribution kernels that use just `ttm`), works around the [MES hang](https://github.com/ROCm/ROCm/issues/5590).   It uses standard grub drop-in configuration to avoid any unecessary prompts at the next distribution upgrade and does not require creating a venv or running update-initramfs to apply the memory configuration.

`sudo vi /etc/default/grub.d/amdgpu.cfg`
```
# /etc/default/grub.d/amdgpu.cfg
GRUB_CMDLINE_LINUX="${GRUB_CMDLINE_LINUX:+$GRUB_CMDLINE_LINUX }ttm.pages_limit=32768000 ttm.page_pool_size=32768000 amdttm.pages_limit=32768000 amdttm.page_pool_size=32768000 amdgpu.cwsr_enable=0"

```
`update-grub`

Boot times are fast, and free memory is maximized with swap disabled in a headless configuration

```
sudo systemd-analyze
Startup finished in 4.395s (kernel) + 1.705s (userspace) = 6.101s 
graphical.target reached after 1.705s in userspace.

sudo free 
               total        used        free      shared  buff/cache   available
Mem:       131171464     1246480   130706828        1636      138376   129924984
Swap:              0           0           0

sudo amd-smi 
+------------------------------------------------------------------------------+
| AMD-SMI 26.1.0+5df6c765      amdgpu version: 6.16.6   ROCm version: 7.1.0    |
| VBIOS version: 00107962                                                      |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:c2:00.0    AMD Radeon Graphics | N/A        N/A   0             N/A/0 W |
|   0       0     N/A             N/A | N/A        N/A              161/512 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+

sudo cat /sys/kernel/debug/dri/128/amdgpu_firmware_info | grep MES
MES_KIQ feature version: 6, firmware version: 0x0000006f
MES feature version: 1, firmware version: 0x00000080

sudo modinfo amdgpu | head -n 3
filename:       /lib/modules/6.12.57+deb13-amd64/updates/dkms/amdgpu.ko.xz
version:        6.16.6
license:        GPL and additional rights

sudo dmesg | grep amdgpu | grep memory
[    3.543771] amdgpu 0000:c2:00.0: amdgpu: amdgpu: 512M of VRAM memory ready
[    3.543773] amdgpu 0000:c2:00.0: amdgpu: amdgpu: 128000M of GTT memory ready.
```


