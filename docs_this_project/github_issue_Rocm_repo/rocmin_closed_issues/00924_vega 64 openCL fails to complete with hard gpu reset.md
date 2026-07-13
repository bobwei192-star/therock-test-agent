# vega 64 openCL fails to complete with hard gpu reset

- **Issue #:** 924
- **State:** closed
- **Created:** 2019-10-27T20:47:37Z
- **Updated:** 2023-12-18T16:29:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/924

I've been trying to run one of the opencl programs and the gpu will run at full tilt and never complete. If I kill the application, my vega 64 will do a hard reset. 

```
Oct 27 13:03:41 michaelpollind systemd[1]: NetworkManager-dispatcher.service: Succeeded.
Oct 27 13:03:35 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00bf7000
Oct 27 13:03:34 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00df0900
Oct 27 13:03:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00bf0900
Oct 27 13:03:32 michaelpollind systemd[1]: Started Session 12 of user michaelpollind.
Oct 27 13:03:32 michaelpollind systemd-logind[1178]: New session 12 of user michaelpollind.
Oct 27 13:03:32 michaelpollind login[17107]: pam_unix(login:session): session opened for user michaelpollind by LOGIN(uid=0)
Oct 27 13:03:32 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x009f0900
Oct 27 13:03:31 michaelpollind dhclient[1551]: bound to 192.168.0.21 -- renewal in 1465 seconds.
Oct 27 13:03:31 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x007f0900
Oct 27 13:03:31 michaelpollind nm-dispatcher[17168]: req:1 'dhcp4-change' [enp25s0]: start running ordered scripts...
Oct 27 13:03:31 michaelpollind nm-dispatcher[17168]: req:1 'dhcp4-change' [enp25s0]: new request (1 scripts)
Oct 27 13:03:31 michaelpollind systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 27 13:03:31 michaelpollind dbus-daemon[1200]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Oct 27 13:03:31 michaelpollind systemd[1]: Starting Network Manager Script Dispatcher Service...
Oct 27 13:03:31 michaelpollind dbus-daemon[1200]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.18' (uid=0 pid=1202 comm="/usr/sbin/NetworkManager --no-daemon ")
Oct 27 13:03:31 michaelpollind avahi-daemon[1179]: Registering new address record for 192.168.0.21 on enp25s0.IPv4.
Oct 27 13:03:31 michaelpollind avahi-daemon[1179]: New relevant interface enp25s0.IPv4 for mDNS.
Oct 27 13:03:31 michaelpollind avahi-daemon[1179]: Joining mDNS multicast group on interface enp25s0.IPv4 with address 192.168.0.21.
Oct 27 13:03:31 michaelpollind avahi-daemon[1179]: Interface enp25s0.IPv4 no longer relevant for mDNS.
Oct 27 13:03:31 michaelpollind avahi-daemon[1179]: Leaving mDNS multicast group on interface enp25s0.IPv4 with address 192.168.0.20.
Oct 27 13:03:31 michaelpollind avahi-daemon[1179]: Withdrawing address record for 192.168.0.20 on enp25s0.
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0): state changed unknown -> bound
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0):   nameserver '209.18.47.61'
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0):   nameserver '209.18.47.62'
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0):   lease time 3600
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0):   gateway 192.168.0.1
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0):   plen 24 (255.255.255.0)
Oct 27 13:03:31 michaelpollind NetworkManager[1202]: <info>  [1572206611.2228] dhcp4 (enp25s0):   address 192.168.0.21
Oct 27 13:03:31 michaelpollind dhclient[1551]: DHCPACK of 192.168.0.21 from 192.168.0.1 (xid=0xf7a0754e)
Oct 27 13:03:30 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x005f0900
Oct 27 13:03:30 michaelpollind dhclient[1551]: DHCPREQUEST for 192.168.0.21 on enp25s0 to 255.255.255.255 port 67 (xid=0x4e75a0f7)
Oct 27 13:03:30 michaelpollind dhclient[1551]: DHCPOFFER of 192.168.0.21 from 192.168.0.1
Oct 27 13:03:30 michaelpollind dhclient[1551]: DHCPDISCOVER on enp25s0 to 255.255.255.255 port 67 interval 3 (xid=0xf7a0754e)
Oct 27 13:03:30 michaelpollind NetworkManager[1202]: <info>  [1572206610.2080] dhcp4 (enp25s0): state changed expire -> unknown
Oct 27 13:03:30 michaelpollind NetworkManager[1202]: <info>  [1572206610.2051] device (enp25s0): DHCPv4: 480 seconds grace period started
Oct 27 13:03:30 michaelpollind NetworkManager[1202]: <info>  [1572206610.2051] dhcp4 (enp25s0): state changed bound -> expire
Oct 27 13:03:30 michaelpollind dhclient[1551]: DHCPNAK from 192.168.0.1 (xid=0x44e8cb74)
Oct 27 13:03:30 michaelpollind dhclient[1551]: DHCPREQUEST for 192.168.0.20 on enp25s0 to 192.168.0.1 port 67 (xid=0x74cbe844)
Oct 27 13:03:29 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x003f0900
Oct 27 13:03:28 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: HDMI ATI/AMD: no speaker allocation for ELD
Oct 27 13:03:28 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00df7000
Oct 27 13:03:27 michaelpollind dhclient[1551]: DHCPREQUEST for 192.168.0.20 on enp25s0 to 192.168.0.1 port 67 (xid=0x74cbe844)
Oct 27 13:03:27 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00df0900
Oct 27 13:03:26 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: HDMI ATI/AMD: no speaker allocation for ELD
Oct 27 13:03:26 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00bf7000
Oct 27 13:03:25 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00bf0900
Oct 27 13:03:24 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: HDMI ATI/AMD: no speaker allocation for ELD
Oct 27 13:03:24 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x009f7000
Oct 27 13:03:23 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x009f0900
Oct 27 13:03:22 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: HDMI ATI/AMD: no speaker allocation for ELD
Oct 27 13:03:22 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x007f7000
Oct 27 13:03:21 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x007f0900
Oct 27 13:03:20 michaelpollind systemd[1]: Started Getty on tty2.
Oct 27 13:03:20 michaelpollind systemd[1]: Stopped Getty on tty2.
Oct 27 13:03:20 michaelpollind systemd[1]: getty@tty2.service: Scheduled restart job, restart counter is at 1.
Oct 27 13:03:20 michaelpollind systemd[1]: getty@tty2.service: Service has no hold-off time (RestartSec=0), scheduling restart.
Oct 27 13:03:20 michaelpollind systemd[1]: getty@tty2.service: Succeeded.
Oct 27 13:03:20 michaelpollind systemd[1]: getty@tty2.service: Main process exited, code=killed, status=2/INT
Oct 27 13:03:20 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: HDMI ATI/AMD: no speaker allocation for ELD
Oct 27 13:03:20 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x005f7000
Oct 27 13:03:19 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x005f0900
Oct 27 13:03:18 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: HDMI ATI/AMD: no speaker allocation for ELD
Oct 27 13:03:18 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x003f7000
Oct 27 13:03:17 michaelpollind login[17065]: FAILED LOGIN (1) on '/dev/tty2' FOR 'UNKNOWN', Authentication failure
Oct 27 13:03:17 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x003f0900
Oct 27 13:03:16 michaelpollind kernel: snd_hda_codec_hdmi hdaudioC0D0: Unable to sync register 0x2f0d00. -11
Oct 27 13:03:16 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00270d01
Oct 27 13:03:15 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00d78901
Oct 27 13:03:14 michaelpollind login[17065]: pam_unix(login:auth): authentication failure; logname=LOGIN uid=0 euid=0 tty=/dev/tty2 ruser= rhost=
Oct 27 13:03:14 michaelpollind login[17065]: pam_unix(login:auth): check pass; user unknown
Oct 27 13:03:14 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00d77200
Oct 27 13:03:13 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00b78901
Oct 27 13:03:12 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00b77200
Oct 27 13:03:11 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00978901
Oct 27 13:03:10 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00977200
Oct 27 13:03:09 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00778901
Oct 27 13:03:08 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00777200
Oct 27 13:03:07 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00578901
Oct 27 13:03:06 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00577200
Oct 27 13:03:05 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00378901
Oct 27 13:03:04 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00377200
Oct 27 13:03:03 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00d70740
Oct 27 13:03:02 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00b70740
Oct 27 13:03:01 michaelpollind systemd[1]: Started Getty on tty5.
Oct 27 13:03:01 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00970740
Oct 27 13:03:00 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00770740
Oct 27 13:02:59 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00570740
Oct 27 13:02:58 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00370740
Oct 27 13:02:56 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:55 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:55 michaelpollind systemd[1]: Started Getty on tty3.
Oct 27 13:02:54 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:53 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:52 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:52 michaelpollind systemd[1]: Started Getty on tty2.
Oct 27 13:02:51 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:50 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:49 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:48 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:47 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:46 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:45 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:44 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:43 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:42 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:41 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:41 michaelpollind vnstatd[1392]: Info: Database write possible again.
Oct 27 13:02:41 michaelpollind vnstatd[1392]: Error: Unable to write database, continuing with cached data.
Oct 27 13:02:41 michaelpollind vnstatd[1392]: Error: Unable to create database backup "/var/lib/vnstat/.wlp29s0".
Oct 27 13:02:41 michaelpollind vnstatd[1392]: Info: Database write possible again.
Oct 27 13:02:41 michaelpollind vnstatd[1392]: Error: Unable to write database, continuing with cached data.
Oct 27 13:02:41 michaelpollind vnstatd[1392]: Error: Unable to create database backup "/var/lib/vnstat/.enp25s0".
Oct 27 13:02:40 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:40 michaelpollind kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Oct 27 13:02:40 michaelpollind kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Oct 27 13:02:40 michaelpollind kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Oct 27 13:02:40 michaelpollind kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Oct 27 13:02:39 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:38 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x001f0500
Oct 27 13:02:37 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, resetting bus: last cmd=0x00170500
Oct 27 13:02:36 michaelpollind kernel: snd_hda_intel 0000:21:00.1: No response from codec, disabling MSI: last cmd=0x00170500
Oct 27 13:02:35 michaelpollind kernel: snd_hda_intel 0000:21:00.1: azx_get_response timeout, switching to polling mode: last cmd=0x00170500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:33 michaelpollind kernel: snd_hda_intel 0000:21:00.1: spurious response 0x0:0x0, last cmd=0x1f0500
Oct 27 13:02:31 michaelpollind kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Oct 27 13:02:31 michaelpollind kernel: [drm:amdgpu_cs_ioctl [amdgpu]] *ERROR* Failed to initialize parser -125!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: GPU reset(1) succeeded!
Oct 27 13:02:31 michaelpollind kernel: [drm] Skip scheduling IBs!
Oct 27 13:02:31 michaelpollind kernel: [drm] recover vram bo from shadow done
Oct 27 13:02:31 michaelpollind kernel: [drm] recover vram bo from shadow start
Oct 27 13:02:31 michaelpollind kernel: [drm] SRAM ECC is not present.
Oct 27 13:02:31 michaelpollind kernel: [drm] ECC is not present.
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring vce2 uses VM inv eng 11 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring vce1 uses VM inv eng 10 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring vce0 uses VM inv eng 9 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring uvd_0 uses VM inv eng 6 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring page1 uses VM inv eng 5 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring sdma1 uses VM inv eng 4 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring page0 uses VM inv eng 1 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring sdma0 uses VM inv eng 0 on hub 1
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: ring gfx uses VM inv eng 0 on hub 0
Oct 27 13:02:31 michaelpollind kernel: [drm] VCE initialized successfully.
Oct 27 13:02:31 michaelpollind kernel: [drm] UVD and UVD ENC initialized successfully.
Oct 27 13:02:31 michaelpollind kernel: [drm] SADs count is: -2, don't need to read it
Oct 27 13:02:31 michaelpollind kernel: [drm] reserve 0x400000 from 0xf401000000 for PSP TMR
Oct 27 13:02:31 michaelpollind kernel: ---[ end trace 45389c1f905012b1 ]---
Oct 27 13:02:31 michaelpollind kernel: R13: 00007f16c7de9c80 R14: 0000000000000028 R15: 0000000000000000
Oct 27 13:02:31 michaelpollind kernel: R10: 0000000000000000 R11: 0000000000000246 R12: 00007f16c7de9cd0
Oct 27 13:02:31 michaelpollind kernel: RBP: 00007f16c7de9ccc R08: 0000000000000000 R09: 0000000000000000
Oct 27 13:02:31 michaelpollind kernel: RDX: 0000000000000000 RSI: 0000000000000080 RDI: 00007f16c7de9cd0
Oct 27 13:02:31 michaelpollind kernel: RAX: fffffffffffffe00 RBX: 00007f16c7de9ca8 RCX: 00007f18cbef83bb
Oct 27 13:02:31 michaelpollind kernel: RSP: 002b:00007f1849ffad80 EFLAGS: 00000246 ORIG_RAX: 00000000000000ca
Oct 27 13:02:31 michaelpollind kernel: Code: Bad RIP value.
Oct 27 13:02:31 michaelpollind kernel: RIP: 0033:0x7f18cbef83bb
Oct 27 13:02:31 michaelpollind kernel:  entry_SYSCALL_64_after_hwframe+0x44/0xa9
Oct 27 13:02:31 michaelpollind kernel:  do_syscall_64+0x10f/0x130
Oct 27 13:02:31 michaelpollind kernel:  exit_to_usermode_loop+0xbf/0x160
Oct 27 13:02:31 michaelpollind kernel:  ? __x64_sys_futex+0x144/0x180
Oct 27 13:02:31 michaelpollind kernel:  ? do_futex+0x10f/0x1e0
Oct 27 13:02:31 michaelpollind kernel:  do_signal+0x34/0x280
Oct 27 13:02:31 michaelpollind kernel:  get_signal+0x165/0x880
Oct 27 13:02:31 michaelpollind kernel:  do_group_exit+0x47/0xb0
Oct 27 13:02:31 michaelpollind kernel:  ? __unqueue_futex+0x2d/0x40
Oct 27 13:02:31 michaelpollind kernel:  do_exit+0x2e9/0xaf0
Oct 27 13:02:31 michaelpollind kernel:  task_work_run+0x8f/0xb0
Oct 27 13:02:31 michaelpollind kernel:  ____fput+0xe/0x10
Oct 27 13:02:31 michaelpollind kernel:  __fput+0xcc/0x260
Oct 27 13:02:31 michaelpollind kernel:  drm_release+0xa5/0xe0 [drm]
Oct 27 13:02:31 michaelpollind kernel:  drm_file_free.part.0+0x1d8/0x290 [drm]
Oct 27 13:02:31 michaelpollind kernel:  amdgpu_driver_postclose_kms+0x18e/0x260 [amdgpu]
Oct 27 13:02:31 michaelpollind kernel:  amdgpu_vm_fini+0x5b/0x3b0 [amdgpu]
Oct 27 13:02:31 michaelpollind kernel:  drm_sched_entity_destroy+0x20/0x30 [gpu_sched]
Oct 27 13:02:31 michaelpollind kernel:  drm_sched_entity_fini+0x4b/0x1c0 [gpu_sched]
Oct 27 13:02:31 michaelpollind kernel: Call Trace:
Oct 27 13:02:31 michaelpollind kernel: CR2: 00003fe8dc34e240 CR3: 0000000bd06b0000 CR4: 00000000003406e0
Oct 27 13:02:31 michaelpollind kernel: CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Oct 27 13:02:31 michaelpollind kernel: FS:  00007f1849ffb700(0000) GS:ffff9b56aed00000(0000) knlGS:0000000000000000
Oct 27 13:02:31 michaelpollind kernel: R13: ffff9b5697d20000 R14: ffff9b5550a04800 R15: 0000000000000000
Oct 27 13:02:31 michaelpollind kernel: R10: 0000062fadf8e700 R11: 0000062fadf8e700 R12: ffff9b5698188000
Oct 27 13:02:31 michaelpollind kernel: RBP: ffffb8e088bcfb10 R08: 0000000000000065 R09: 0000062fadf8e700
Oct 27 13:02:31 michaelpollind kernel: RDX: ffff9b5697d298f8 RSI: ffff9b5550a048b8 RDI: ffff9b5698188000
Oct 27 13:02:31 michaelpollind kernel: RAX: 0000000000000004 RBX: ffff9b5698b7eba0 RCX: ffff9b5690e08000
Oct 27 13:02:31 michaelpollind kernel: RSP: 0018:ffffb8e088bcfb00 EFLAGS: 00010202
Oct 27 13:02:31 michaelpollind kernel: Code: 4c 89 e7 e8 62 ed 00 00 48 8d 7b 18 e8 99 44 9d 00 be 40 00 00 00 4c 89 e7 e8 2c ef 00 00 48 85 c0 74 10 31 c0 5b 41 5c 5d c3 <0f> 0b b8 f0 ff ff ff eb f2 0f 0b eb ee 0f 1f 00 0f 1f 44 00 00 55
Oct 27 13:02:31 michaelpollind kernel: RIP: 0010:kthread_park+0x70/0x80
Oct 27 13:02:31 michaelpollind kernel: Hardware name: Micro-Star International Co., Ltd. MS-7A34/B350 TOMAHAWK (MS-7A34), BIOS 1.K0 11/01/2018
Oct 27 13:02:31 michaelpollind kernel: CPU: 12 PID: 16680 Comm: vadd Not tainted 5.3.7-050307-generic #201910180652
Oct 27 13:02:31 michaelpollind kernel:  drm i2c_piix4 r8169 ahci realtek libahci wmi gpio_amdpt gpio_generic
Oct 27 13:02:31 michaelpollind kernel: Modules linked in: xt_MASQUERADE nf_conntrack_netlink nfnetlink xfrm_user xfrm_algo iptable_nat xt_addrtype iptable_filter bpfilter xt_conntrack nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 libcrc32c br_netfilter bridge stp llc vmw_vsock_vmci_transport vsock vmw_vmci ccm overlay binfmt_misc snd_hda_codec_realtek snd_hda_codec_generic ledtrig_audio snd_hda_codec_hdmi snd_hda_intel snd_hda_codec snd_hda_core snd_hwdep ath9k snd_pcm joydev snd_seq_midi edac_mce_amd input_leds ath9k_common snd_seq_midi_event kvm_amd kvm ath9k_hw snd_rawmidi irqbypass snd_seq crct10dif_pclmul crc32_pclmul ghash_clmulni_intel ath snd_seq_device snd_timer mac80211 aesni_intel cfg80211 aes_x86_64 snd libarc4 crypto_simd cryptd soundcore ccp glue_helper k10temp mac_hid wmi_bmof sch_fq_codel vmwgfx hwmon_vid parport_pc ppdev lp parport ip_tables x_tables autofs4 wacom hid_generic usbhid hid amdgpu amd_iommu_v2 gpu_sched i2c_algo_bit ttm drm_kms_helper syscopyarea sysfillrect sysimgblt fb_sys_fops
Oct 27 13:02:31 michaelpollind kernel: WARNING: CPU: 12 PID: 16680 at kernel/kthread.c:510 kthread_park+0x70/0x80
Oct 27 13:02:31 michaelpollind kernel: [drm] PSP is resuming...
Oct 27 13:02:31 michaelpollind kernel: [drm] VRAM is lost due to GPU reset!
Oct 27 13:02:31 michaelpollind kernel: [drm] PCIE GART of 512M enabled (table at 0x000000F400900000).
Oct 27 13:02:31 michaelpollind kernel: amdgpu 0000:21:00.0: GPU reset succeeded, trying to resume
Oct 27 13:02:30 michaelpollind kernel: amdgpu 0000:21:00.0: GPU BACO reset
Oct 27 13:02:30 michaelpollind kernel: amdgpu 0000:21:00.0: GPU reset begin!
Oct 27 13:02:30 michaelpollind kernel: The cp might be in an unrecoverable state due to an unsuccessful queues preemption
Oct 27 13:02:30 michaelpollind kernel: qcm fence wait loop timeout expired
Oct 27 13:01:02 michaelpollind systemd[1]: systemd-hostnamed.service: Succeeded.
Oct 27 13:00:32 michaelpollind systemd[1]: Started Hostname Service.
Oct 27 13:00:32 michaelpollind dbus-daemon[1200]: [system] Successfully activated service 'org.freedesktop.hostname1'
Oct 27 13:00:32 michaelpollind systemd[1]: Starting Hostname Service...
Oct 27 13:00:32 michaelpollind dbus-daemon[1200]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.160' (uid=1000 pid=7566 comm="/opt/sublime_text/sublime_text /home/michaelpollin")
Oct 27 13:00:32 michaelpollind systemd[3042]: Started Virtual filesystem service - Apple File Conduit monitor.
Oct 27 13:00:32 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Successfully activated service 'org.gtk.vfs.AfcVolumeMonitor'
Oct 27 13:00:32 michaelpollind gvfs-afc-volume-monitor[16420]: Volume monitor alive
Oct 27 13:00:32 michaelpollind systemd[3042]: Starting Virtual filesystem service - Apple File Conduit monitor...
Oct 27 13:00:32 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Activating via systemd: service name='org.gtk.vfs.AfcVolumeMonitor' unit='gvfs-afc-volume-monitor.service' requested by ':1.76' (uid=1000 pid=7566 comm="/opt/sublime_text/sublime_text /home/michaelpollin")
Oct 27 13:00:32 michaelpollind systemd[3042]: Started Virtual filesystem service - digital camera monitor.
Oct 27 13:00:32 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Successfully activated service 'org.gtk.vfs.GPhoto2VolumeMonitor'
Oct 27 13:00:31 michaelpollind systemd[3042]: Starting Virtual filesystem service - digital camera monitor...
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Activating via systemd: service name='org.gtk.vfs.GPhoto2VolumeMonitor' unit='gvfs-gphoto2-volume-monitor.service' requested by ':1.76' (uid=1000 pid=7566 comm="/opt/sublime_text/sublime_text /home/michaelpollin")
Oct 27 13:00:31 michaelpollind systemd[3042]: Started Virtual filesystem service - GNOME Online Accounts monitor.
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Successfully activated service 'org.gtk.vfs.GoaVolumeMonitor'
Oct 27 13:00:31 michaelpollind systemd[3042]: Starting Virtual filesystem service - GNOME Online Accounts monitor...
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Activating via systemd: service name='org.gtk.vfs.GoaVolumeMonitor' unit='gvfs-goa-volume-monitor.service' requested by ':1.76' (uid=1000 pid=7566 comm="/opt/sublime_text/sublime_text /home/michaelpollin")
Oct 27 13:00:31 michaelpollind systemd[3042]: Started Virtual filesystem service - Media Transfer Protocol monitor.
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Successfully activated service 'org.gtk.vfs.MTPVolumeMonitor'
Oct 27 13:00:31 michaelpollind systemd[3042]: Starting Virtual filesystem service - Media Transfer Protocol monitor...
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Activating via systemd: service name='org.gtk.vfs.MTPVolumeMonitor' unit='gvfs-mtp-volume-monitor.service' requested by ':1.76' (uid=1000 pid=7566 comm="/opt/sublime_text/sublime_text /home/michaelpollin")
Oct 27 13:00:31 michaelpollind systemd[3042]: Started Virtual filesystem service - disk device monitor.
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Successfully activated service 'org.gtk.vfs.UDisks2VolumeMonitor'
Oct 27 13:00:31 michaelpollind systemd[3042]: Starting Virtual filesystem service - disk device monitor...
Oct 27 13:00:31 michaelpollind dbus-daemon[3127]: [session uid=1000 pid=3127] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.76' (uid=1000 pid=7566 comm="/opt/sublime_text/sublime_text /home/michaelpollin")
Oct 27 12:57:41 michaelpollind vnstatd[1392]: Info: Database write possible again.
Oct 27 12:57:41 michaelpollind vnstatd[1392]: Error: Unable to write database, continuing with cached data.
Oct 27 12:57:41 michaelpollind vnstatd[1392]: Error: Unable to create database backup "/var/lib/vnstat/.wlp29s0".
Oct 27 12:57:41 michaelpollind vnstatd[1392]: Info: Database write possible again.
Oct 27 12:57:41 michaelpollind vnstatd[1392]: Error: Unable to write database, continuing with cached data.
Oct 27 12:57:41 michaelpollind vnstatd[1392]: Error: Unable to create database backup "/var/lib/vnstat/.enp25s0".
Oct 27 12:52:41 michaelpollind vnstatd[1392]: Info: Database write possible again.
Oct 27 12:52:41 michaelpollind vnstatd[1392]: Error: Unable to write database, continuing with cached data.
Oct 27 12:52:41 michaelpollind vnstatd[1392]: Error: Unable to create database backup "/var/lib/vnstat/.wlp29s0".
Oct 27 12:52:41 michaelpollind vnstatd[1392]: Info: Database write possible again.
Oct 27 12:52:41 michaelpollind vnstatd[1392]: Error: Unable to write database, continuing with cached data.
Oct 27 12:52:41 michaelpollind vnstatd[1392]: Error: Unable to create database backup "/var/lib/vnstat/.enp25s0".
Oct 27 12:48:08 michaelpollind systemd[1]: NetworkManager-dispatcher.service: Succeeded.
Oct 27 12:47:58 michaelpollind dhclient[1550]: bound to 192.168.0.31 -- renewal in 1603 seconds.
Oct 27 12:47:58 michaelpollind nm-dispatcher[14980]: req:1 'dhcp4-change' [wlp29s0]: start running ordered scripts...
Oct 27 12:47:58 michaelpollind nm-dispatcher[14980]: req:1 'dhcp4-change' [wlp29s0]: new request (1 scripts)
Oct 27 12:47:58 michaelpollind systemd[1]: Started Network Manager Script Dispatcher Service.
Oct 27 12:47:58 michaelpollind dbus-daemon[1200]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
Oct 27 12:47:58 michaelpollind systemd[1]: Starting Network Manager Script Dispatcher Service...
```

rocminfo
```
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 2700 Eight-Core Processor
  Marketing Name:          AMD Ryzen 7 2700 Eight-Core Processor
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   0                                  
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    49302284(0x2f04b0c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    49302284(0x2f04b0c) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Marketing Name:          Vega 10 XT [Radeon RX Vega 64]     
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26751(0x687f)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1630                               
  BDFID:                   8448                               
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    8372224(0x7fc000) KB               
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Acessible by all:        FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***  
```

clinfo
```
Number of platforms:                             2
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 1.1 Mesa 19.3.0-devel (git-728a975 2019-10-26 disco-oibaf-ppa)
  Platform Name:                                 Clover
  Platform Vendor:                               Mesa
  Platform Extensions:                           cl_khr_icd
  Platform Profile:                              FULL_PROFILE
  Platform Version:                              OpenCL 2.1 AMD-APP (2982.0)
  Platform Name:                                 AMD Accelerated Parallel Processing
  Platform Vendor:                               Advanced Micro Devices, Inc.
  Platform Extensions:                           cl_khr_icd cl_amd_event_callback cl_amd_offline_devices 


  Platform Name:                                 Clover
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Max compute units:                             64
  Max work items dimensions:                     3
    Max work items[0]:                           256
    Max work items[1]:                           256
    Max work items[2]:                           256
  Max work group size:                           256
  Preferred vector width char:                   16
  Preferred vector width short:                  8
  Preferred vector width int:                    4
  Preferred vector width long:                   2
  Preferred vector width float:                  4
  Preferred vector width double:                 2
  Native vector width char:                      16
  Native vector width short:                     8
  Native vector width int:                       4
  Native vector width long:                      2
  Native vector width float:                     4
  Native vector width double:                    2
  Max clock frequency:                           1630Mhz
  Address bits:                                  64
  Max memory allocation:                         6871947673
  Image support:                                 No
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              32768
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     No
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               No
    Round to +ve and infinity:                   No
    IEEE754-2008 fused multiply-add:             No
  Cache type:                                    None
  Cache line size:                               0
  Cache size:                                    0
  Global memory size:                            8589934592
  Constant buffer size:                          2147483647
  Max number of constant args:                   16
  Local memory type:                             Scratchpad
  Local memory size:                             32768
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    0
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:                                
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:                              
    Out-of-Order:                                No
    Profiling :                                  Yes
  Platform ID:                                   0x7f2e3bb812e0
  Name:                                          Radeon RX Vega (VEGA10, DRM 3.33.0, 5.3.7-050307-generic, LLVM 9.0.0)
  Vendor:                                        AMD
  Device OpenCL C version:                       OpenCL C 1.1 
  Driver version:                                19.3.0-devel
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 1.1 Mesa 19.3.0-devel (git-728a975 2019-10-26 disco-oibaf-ppa)
  Extensions:                                    cl_khr_byte_addressable_store cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_fp64 cl_khr_fp16


  Platform Name:                                 AMD Accelerated Parallel Processing
Number of devices:                               1
  Device Type:                                   CL_DEVICE_TYPE_GPU
  Vendor ID:                                     1002h
  Board name:                                    Vega 10 XT [Radeon RX Vega 64]
  Device Topology:                               PCI[ B#33, D#0, F#0 ]
  Max compute units:                             64
  Max work items dimensions:                     3
    Max work items[0]:                           1024
    Max work items[1]:                           1024
    Max work items[2]:                           1024
  Max work group size:                           256
  Preferred vector width char:                   4
  Preferred vector width short:                  2
  Preferred vector width int:                    1
  Preferred vector width long:                   1
  Preferred vector width float:                  1
  Preferred vector width double:                 1
  Native vector width char:                      4
  Native vector width short:                     2
  Native vector width int:                       1
  Native vector width long:                      1
  Native vector width float:                     1
  Native vector width double:                    1
  Max clock frequency:                           1630Mhz
  Address bits:                                  64
  Max memory allocation:                         7287183769
  Image support:                                 Yes
  Max number of images read arguments:           128
  Max number of images write arguments:          8
  Max image 2D width:                            16384
  Max image 2D height:                           16384
  Max image 3D width:                            2048
  Max image 3D height:                           2048
  Max image 3D depth:                            2048
  Max samplers within kernel:                    26751
  Max size of kernel argument:                   1024
  Alignment (bits) of base address:              1024
  Minimum alignment (bytes) for any datatype:    128
  Single precision floating point capability
    Denorms:                                     Yes
    Quiet NaNs:                                  Yes
    Round to nearest even:                       Yes
    Round to zero:                               Yes
    Round to +ve and infinity:                   Yes
    IEEE754-2008 fused multiply-add:             Yes
  Cache type:                                    Read/Write
  Cache line size:                               64
  Cache size:                                    16384
  Global memory size:                            8573157376
  Constant buffer size:                          7287183769
  Max number of constant args:                   8
  Local memory type:                             Scratchpad
  Local memory size:                             65536
  Max pipe arguments:                            16
  Max pipe active reservations:                  16
  Max pipe packet size:                          2992216473
  Max global variable size:                      7287183769
  Max global variable preferred total size:      8573157376
  Max read/write image args:                     64
  Max on device events:                          1024
  Queue on device max size:                      8388608
  Max on device queues:                          1
  Queue on device preferred size:                262144
  SVM capabilities:                              
    Coarse grain buffer:                         Yes
    Fine grain buffer:                           Yes
    Fine grain system:                           No
    Atomics:                                     No
  Preferred platform atomic alignment:           0
  Preferred global atomic alignment:             0
  Preferred local atomic alignment:              0
  Kernel Preferred work group size multiple:     64
  Error correction support:                      0
  Unified memory for Host and Device:            0
  Profiling timer resolution:                    1
  Device endianess:                              Little
  Available:                                     Yes
  Compiler available:                            Yes
  Execution capabilities:                                
    Execute OpenCL kernels:                      Yes
    Execute native function:                     No
  Queue on Host properties:                              
    Out-of-Order:                                No
    Profiling :                                  Yes
  Queue on Device properties:                            
    Out-of-Order:                                Yes
    Profiling :                                  Yes
  Platform ID:                                   0x7f2e2c7c0d30
  Name:                                          gfx900
  Vendor:                                        Advanced Micro Devices, Inc.
  Device OpenCL C version:                       OpenCL C 2.0 
  Driver version:                                2982.0 (HSA1.1,LC)
  Profile:                                       FULL_PROFILE
  Version:                                       OpenCL 2.0 
  Extensions:                                    cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 
```


```
//------------------------------------------------------------------------------
//
// Name:       vadd.c
//
// Purpose:    Elementwise addition of two vectors (c = a + b)
//
// HISTORY:    Written by Tim Mattson, December 2009
//             Updated by Tom Deakin and Simon McIntosh-Smith, October 2012
//             Updated by Tom Deakin, July 2013
//             Updated by Tom Deakin, October 2014
//
//------------------------------------------------------------------------------


#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#ifdef __APPLE__
#include <OpenCL/opencl.h>
#include <unistd.h>
#else
#include <CL/cl.h>
#endif

#include "err_code.h"

//pick up device type from compiler command line or from
//the default type
#ifndef DEVICE
#define DEVICE CL_DEVICE_TYPE_DEFAULT
#endif


extern double wtime();       // returns time since some fixed past point (wtime.c)
extern int output_device_info(cl_device_id );


//------------------------------------------------------------------------------

#define TOL    (0.001)   // tolerance used in floating point comparisons
#define LENGTH (1024)    // length of vectors a, b, and c

//------------------------------------------------------------------------------
//
// kernel:  vadd
//
// Purpose: Compute the elementwise sum c = a+b
//
// input: a and b float vectors of length count
//
// output: c float vector of length count holding the sum a + b
//

const char *KernelSource = "\n" \
"__kernel void vadd(                                                 \n" \
"   __global float* a,                                                  \n" \
"   __global float* b,                                                  \n" \
"   __global float* c,                                                  \n" \
"   const unsigned int count)                                           \n" \
"{                                                                      \n" \
"   int i = get_global_id(0);                                           \n" \
"   if(i < count)                                                       \n" \
"       c[i] = a[i] + b[i];                                             \n" \
"}                                                                      \n" \
"\n";

//------------------------------------------------------------------------------


int main(int argc, char** argv)
{
    int          err;               // error code returned from OpenCL calls

    float*       h_a = (float*) calloc(LENGTH, sizeof(float));       // a vector
    float*       h_b = (float*) calloc(LENGTH, sizeof(float));       // b vector
    float*       h_c = (float*) calloc(LENGTH, sizeof(float));       // c vector (a+b) returned from the compute device

    unsigned int correct;           // number of correct results

    size_t global;                  // global domain size

    cl_device_id     device_id;     // compute device id
    cl_context       context;       // compute context
    cl_command_queue commands;      // compute command queue
    cl_program       program;       // compute program
    cl_kernel        ko_vadd;       // compute kernel

    cl_mem d_a;                     // device memory used for the input  a vector
    cl_mem d_b;                     // device memory used for the input  b vector
    cl_mem d_c;                     // device memory used for the output c vector

    // Fill vectors a and b with random float values
    int i = 0;
    int count = LENGTH;
    for(i = 0; i < count; i++){
        h_a[i] = rand() / (float)RAND_MAX;
        h_b[i] = rand() / (float)RAND_MAX;
    }

    // Set up platform and GPU device

    cl_uint numPlatforms;

    // Find number of platforms
    err = clGetPlatformIDs(0, NULL, &numPlatforms);
    checkError(err, "Finding platforms");
    if (numPlatforms == 0)
    {
        printf("Found 0 platforms!\n");
        return EXIT_FAILURE;
    }

    // Get all platforms
    cl_platform_id Platform[numPlatforms];
    err = clGetPlatformIDs(numPlatforms, Platform, NULL);
    checkError(err, "Getting platforms");

    // Secure a GPU
    for (i = 0; i < numPlatforms; i++)
    {
        err = clGetDeviceIDs(Platform[i], DEVICE, 1, &device_id, NULL);
        if (err == CL_SUCCESS)
        {
            break;
        }
    }

    if (device_id == NULL)
        checkError(err, "Finding a device");

    err = output_device_info(device_id);
    checkError(err, "Printing device output");

    // Create a compute context
    context = clCreateContext(0, 1, &device_id, NULL, NULL, &err);
    checkError(err, "Creating context");

    // Create a command queue
    commands = clCreateCommandQueue(context, device_id, 0, &err);
    checkError(err, "Creating command queue");

    // Create the compute program from the source buffer
    program = clCreateProgramWithSource(context, 1, (const char **) & KernelSource, NULL, &err);
    checkError(err, "Creating program");

    // Build the program
    err = clBuildProgram(program, 0, NULL, NULL, NULL, NULL);
    if (err != CL_SUCCESS)
    {
        size_t len;
        char buffer[2048];

        printf("Error: Failed to build program executable!\n%s\n", err_code(err));
        clGetProgramBuildInfo(program, device_id, CL_PROGRAM_BUILD_LOG, sizeof(buffer), buffer, &len);
        printf("%s\n", buffer);
        return EXIT_FAILURE;
    }

    // Create the compute kernel from the program
    ko_vadd = clCreateKernel(program, "vadd", &err);
    checkError(err, "Creating kernel");

    // Create the input (a, b) and output (c) arrays in device memory
    d_a  = clCreateBuffer(context,  CL_MEM_READ_ONLY,  sizeof(float) * count, NULL, &err);
    checkError(err, "Creating buffer d_a");

    d_b  = clCreateBuffer(context,  CL_MEM_READ_ONLY,  sizeof(float) * count, NULL, &err);
    checkError(err, "Creating buffer d_b");

    d_c  = clCreateBuffer(context,  CL_MEM_WRITE_ONLY, sizeof(float) * count, NULL, &err);
    checkError(err, "Creating buffer d_c");

    // Write a and b vectors into compute device memory
    err = clEnqueueWriteBuffer(commands, d_a, CL_TRUE, 0, sizeof(float) * count, h_a, 0, NULL, NULL);
    checkError(err, "Copying h_a to device at d_a");

    err = clEnqueueWriteBuffer(commands, d_b, CL_TRUE, 0, sizeof(float) * count, h_b, 0, NULL, NULL);
    checkError(err, "Copying h_b to device at d_b");

    // Set the arguments to our compute kernel
    err  = clSetKernelArg(ko_vadd, 0, sizeof(cl_mem), &d_a);
    err |= clSetKernelArg(ko_vadd, 1, sizeof(cl_mem), &d_b);
    err |= clSetKernelArg(ko_vadd, 2, sizeof(cl_mem), &d_c);
    err |= clSetKernelArg(ko_vadd, 3, sizeof(unsigned int), &count);
    checkError(err, "Setting kernel arguments");

    double rtime = wtime();

    // Execute the kernel over the entire range of our 1d input data set
    // letting the OpenCL runtime choose the work-group size
    global = count;
    err = clEnqueueNDRangeKernel(commands, ko_vadd, 1, NULL, &global, NULL, 0, NULL, NULL);
    checkError(err, "Enqueueing kernel");

    // Wait for the commands to complete before stopping the timer
    err = clFinish(commands);
    checkError(err, "Waiting for kernel to finish");

    rtime = wtime() - rtime;
    printf("\nThe kernel ran in %lf seconds\n",rtime);

    // Read back the results from the compute device
    err = clEnqueueReadBuffer( commands, d_c, CL_TRUE, 0, sizeof(float) * count, h_c, 0, NULL, NULL );  
    if (err != CL_SUCCESS)
    {
        printf("Error: Failed to read output array!\n%s\n", err_code(err));
        exit(1);
    }

    // Test the results
    correct = 0;
    float tmp;

    for(i = 0; i < count; i++)
    {
        tmp = h_a[i] + h_b[i];     // assign element i of a+b to tmp
        tmp -= h_c[i];             // compute deviation of expected and output result
        if(tmp*tmp < TOL*TOL)        // correct if square deviation is less than tolerance squared
            correct++;
        else {
            printf(" tmp %f h_a %f h_b %f h_c %f \n",tmp, h_a[i], h_b[i], h_c[i]);
        }
    }

    // summarise results
    printf("C = A+B:  %d out of %d results were correct.\n", correct, count);

    // cleanup then shutdown
    clReleaseMemObject(d_a);
    clReleaseMemObject(d_b);
    clReleaseMemObject(d_c);
    clReleaseProgram(program);
    clReleaseKernel(ko_vadd);
    clReleaseCommandQueue(commands);
    clReleaseContext(context);

    free(h_a);
    free(h_b);
    free(h_c);

    return 0;
}

```