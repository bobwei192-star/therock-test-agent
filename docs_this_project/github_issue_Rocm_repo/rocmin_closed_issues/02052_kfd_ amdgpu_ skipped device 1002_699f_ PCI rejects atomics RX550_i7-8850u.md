#  kfd: amdgpu: skipped device 1002:699f, PCI rejects atomics RX550/i7-8850u

- **Issue #:** 2052
- **State:** closed
- **Created:** 2023-04-15T08:06:47Z
- **Updated:** 2024-10-17T14:47:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/2052

Hello. I have Lenovo e580 thinkpad, Latest 1.49 bios installed. 
In Linux distros; In boot messages, I tried LTS kernel (5.15) or 6.1x new version or distributions using the latest software, unfortunately I get these error messages.
(I have tried this on all 10 of the most used linux distributions known. I am getting the same error on all of them.)

It has been going on for years and no fix has been released by either amd or lenovo. It's very sad. 

I also opened the support topic on Lenovo and amd official forum pages. https://forums.lenovo.com/t5/Other-Linux-Discussions/Thinkpad-e580-motherboard-compatibility-bios-issue-with-Radeon-rx-550/m-p/5218384
https://community.amd.com/t5/general-discussions/thinkpad-e580-motherboard-compatibility-bios-issue-with-radeon/td-p/600351

```
[ 9.298192] kfd kfd: amdgpu: skipped device 1002:699f, PCI rejects atomics 730<0

---
ACPI BIOS Error (bug): AE_AML_BUFFER_LIMIT, Field [TBF3] at bit offset/length 262144/32768 exceeds size of target Buffer (262144 bits) (20220331/dsopcode-198)
ACPI Error: Aborting method \_SB.PCI0.GFX0.GETB due to previous error (AE_AML_BUFFER_LIMIT) (20220331/psparse-529)
ACPI Error: Aborting method \_SB.PCI0.GFX0.ATRM due to previous error (AE_AML_BUFFER_LIMIT) (20220331/psparse-529)
failed to evaluate ATRM got AE_AML_BUFFER_LIMIT
```


**My hardware list:**
```
glc@glc-pc:~$ lspci -nnk
00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5914] (rev 08)
Subsystem: Lenovo Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [17aa:5068]
Kernel driver in use: skl_uncore
00:02.0 VGA compatible controller [0300]: Intel Corporation UHD Graphics 620 [8086:5917] (rev 07)
Subsystem: Lenovo UHD Graphics 620 [17aa:5069]
Kernel driver in use: i915
Kernel modules: i915
00:08.0 System peripheral [0880]: Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [8086:1911]
Subsystem: Lenovo Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [17aa:5068]
00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f] (rev 21)
Subsystem: Lenovo Sunrise Point-LP USB 3.0 xHCI Controller [17aa:5068]
Kernel driver in use: xhci_hcd
Kernel modules: xhci_pci
00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31] (rev 21)
Subsystem: Lenovo Sunrise Point-LP Thermal subsystem [17aa:5068]
Kernel driver in use: intel_pch_thermal
Kernel modules: intel_pch_thermal
00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a] (rev 21)
Subsystem: Lenovo Sunrise Point-LP CSME HECI [17aa:5068]
Kernel driver in use: mei_me
Kernel modules: mei_me
00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03] (rev 21)
Subsystem: Lenovo Sunrise Point-LP SATA Controller [AHCI mode] [17aa:5068]
Kernel driver in use: ahci
Kernel modules: ahci
00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 [8086:9d10] (rev f1)
Kernel driver in use: pcieport
00:1c.4 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 [8086:9d14] (rev f1)
Kernel driver in use: pcieport
00:1d.0 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 [8086:9d18] (rev f1)
Kernel driver in use: pcieport
00:1d.2 PCI bridge [0604]: Intel Corporation Sunrise Point-LP PCI Express Root Port #11 [8086:9d1a] (rev f1)
Kernel driver in use: pcieport
00:1d.3 PCI bridge [0604]: Intel Corporation Device [8086:9d1b] (rev f1)
Kernel driver in use: pcieport
00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point LPC Controller/eSPI Controller [8086:9d4e] (rev 21)
Subsystem: Lenovo Sunrise Point LPC Controller/eSPI Controller [17aa:5068]
00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-LP PMC [8086:9d21] (rev 21)
Subsystem: Lenovo Sunrise Point-LP PMC [17aa:5068]
00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-LP HD Audio [8086:9d71] (rev 21)
Subsystem: Lenovo Sunrise Point-LP HD Audio [17aa:5068]
Kernel driver in use: snd_hda_intel
Kernel modules: snd_hda_intel, snd_soc_skl, snd_soc_avs, snd_sof_pci_intel_skl
00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-LP SMBus [8086:9d23] (rev 21)
Subsystem: Lenovo Sunrise Point-LP SMBus [17aa:5068]
Kernel driver in use: i801_smbus
Kernel modules: i2c_i801
02:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X] [1002:699f] (rev c0)
Subsystem: Lenovo Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X] [17aa:5069]
Kernel driver in use: amdgpu
Kernel modules: amdgpu
03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 10)
Subsystem: Lenovo RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [17aa:5068]
Kernel driver in use: r8169
Kernel modules: r8169
04:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961/SM963 [144d:a804]
Subsystem: Samsung Electronics Co Ltd SM963 2.5" NVMe PCIe SSD [144d:a801]
Kernel driver in use: nvme
Kernel modules: nvme
05:00.0 Network controller [0280]: Intel Corporation Dual Band Wireless-AC 3165 Plus Bluetooth [8086:3166] (rev 99)
Subsystem: Intel Corporation Dual Band Wireless-AC 3165 [8086:4210]
Kernel driver in use: iwlwifi
Kernel modules: iwlwifi
06:00.0 SD Host controller [0805]: O2 Micro, Inc. SD/MMC Card Reader Controller [1217:8621] (rev 01)
Subsystem: Lenovo SD/MMC Card Reader Controller [17aa:5068]
Kernel driver in use: sdhci-pci
Kernel modules: sdhci_pci
glc@glc-pc:~$
```

Continue:..    
```
glc@glc-pc:~$ sudo lspci -t
-[0000:00]-+-00.0
+-02.0
+-08.0
+-14.0
+-14.2
+-16.0
+-17.0
+-1c.0-[02]----00.0
+-1c.4-[03]----00.0
+-1d.0-[04]----00.0
+-1d.2-[05]----00.0
+-1d.3-[06]----00.0
+-1f.0
+-1f.2
+-1f.3
\-1f.4

```

Continue:....
```
glc@glc-pc:~$ lspci -tnnv
-[0000:00]-+-00.0 Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers [8086:5914]
+-02.0 Intel Corporation UHD Graphics 620 [8086:5917]
+-08.0 Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model [8086:1911]
+-14.0 Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller [8086:9d2f]
+-14.2 Intel Corporation Sunrise Point-LP Thermal subsystem [8086:9d31]
+-16.0 Intel Corporation Sunrise Point-LP CSME HECI #1 [8086:9d3a]
+-17.0 Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] [8086:9d03]
+-1c.0-[02]----00.0 Advanced Micro Devices, Inc. [AMD/ATI] Lexa PRO [Radeon 540/540X/550/550X / RX 540X/550/550X] [1002:699f]
+-1c.4-[03]----00.0 Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168]
+-1d.0-[04]----00.0 Samsung Electronics Co Ltd NVMe SSD Controller SM961/PM961/SM963 [144d:a804]
+-1d.2-[05]----00.0 Intel Corporation Dual Band Wireless-AC 3165 Plus Bluetooth [8086:3166]
+-1d.3-[06]----00.0 O2 Micro, Inc. SD/MMC Card Reader Controller [1217:8621]
+-1f.0 Intel Corporation Sunrise Point LPC Controller/eSPI Controller [8086:9d4e]
+-1f.2 Intel Corporation Sunrise Point-LP PMC [8086:9d21]
+-1f.3 Intel Corporation Sunrise Point-LP HD Audio [8086:9d71]
\-1f.4 Intel Corporation Sunrise Point-LP SMBus [8086:9d23]
glc@glc-pc:~$
```

Is there a way to completely disable this external / discrete video card in linux distributions? Thank you in advance for your help. have a nice day.
