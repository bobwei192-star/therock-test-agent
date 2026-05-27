# Dell R7525 with 3xMI100 clinfo kills machine with multiGPU PCIe

> **Issue #1493**
> **状态**: closed
> **创建时间**: 2021-06-15T07:15:46Z
> **更新时间**: 2022-04-20T07:11:13Z
> **关闭时间**: 2021-06-16T09:55:41Z
> **作者**: sjjamsa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1493

## 描述

Hi!

I have a Dell R7525 with 3xMI100 installed. No Infinity fabric, only PCIe connection. I have had the below issues from the very first install of the machine. They happen with Centos7.9 and latest Ubuntu LTS server HWE. They also occur with ROCm 4.1.1 and 4.2. The problem goes away if I disable any two of the three MI100 cards.

After following [the installation instructions](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html), I tried the two suggested commands:
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
The first runs fine, the **clinfo crashes the machine** on Ubuntu while Centos doesn't quite die, and I was able to capture the attached [dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/6653439/dmesg.txt).

I tried various tests from [the validation suite](https://rocmdocs.amd.com/en/latest/Other_Solutions/rocm-validation-suite.html).
The following modules run fine: `gpup`, `peqt`, `pebb`. However, **the pqt module crashed the machine** (got NMIs):

```
- name: action_4
  device: 55570
  module: pqt
  log_interval: 800
  duration: 5000
  peers: 51147
  test_bandwidth: true
  bidirectional: true
  block_size: 1000000 2000000 10000000
```

Later, if I **disable any two of the three MI100 cards** in BIOS, `clinfo` runs fine. 

My colleagues have used the system for some development. This is of course not satisfactory; all three cards must be stably usable. If the peer2peer performance must be low, we can live with that, but the system must remain stable.

Any help would be appreciated.

Best regards,
 - Simppa -

---

## 评论 (16 条)

### 评论 #1 — ROCmSupport (2021-06-15T08:53:17Z)

Hi @sjjamsa 
Thanks for reaching out.
Let me check this for you and get back asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-06-15T08:56:22Z)

Got that with single MI100 card, things are working well.
But with 3 MI100 cards, clinfo is broken.

When I see the dmesg, found that a few MI100 cards are not working well, which is hardware issue.
dmesg clearly shows the same.
I recommend to do the things in below way.
1. Keep only one MI100 card and run clinfo
2. Add one card to the system and run clinfo again
3. Add the third card now and run clinfo

My expectation is that one or two of your 3 cards are not working good, having hardware problem.

_**[  340.596150] {1}[Hardware Error]: Hardware error from APEI Generic Hardware Error Source: 8
[  340.605427] {1}[Hardware Error]: event severity: fatal
[  340.611515] {1}[Hardware Error]:  Error 0, type: fatal
[  340.617592] {1}[Hardware Error]:   section_type: PCIe error
[  340.624112] {1}[Hardware Error]:   port_type: 1, legacy PCI end point
[  340.631519] {1}[Hardware Error]:   version: 3.0
[  340.637000] {1}[Hardware Error]:   command: 0x0547, status: 0x5810
[  340.644125] {1}[Hardware Error]:   device_id: 0000:83:00.0
[  340.650549] {1}[Hardware Error]:   slot: 0
[  340.655567] {1}[Hardware Error]:   secondary_bus: 0x00
[  340.661619] {1}[Hardware Error]:   vendor_id: 0x1002, device_id: 0x738c
[  340.669146] {1}[Hardware Error]:   class_code: 000000
[  340.675093] {1}[Hardware Error]:   aer_uncor_status: 0x00008000, aer_uncor_mask: 0x00010000
[  340.684362] {1}[Hardware Error]:   aer_uncor_severity: 0x004ef030
[  340.691360] {1}[Hardware Error]:   TLP Header: 40009001 8000000f 9927f000 00000000
[  340.699901] amdgpu 0000:83:00.0: aer_status: 0x00008000, aer_mask: 0x00010000
[  340.707957] Completer Abort
[  340.711668] amdgpu 0000:83:00.0: aer_layer=Transaction Layer, aer_agent=Completer ID
[  340.720354] amdgpu 0000:83:00.0: aer_uncor_severity: 0x004ef030
[  340.727210] amdgpu 0000:83:00.0:   TLP Header: 40009001 8000000f 9927f000 00000000
[  340.735721] amdgpu 0000:83:00.0: broadcast error_detected message
[  340.735726] [drm] PCI error: detected callback, state(2)!!
[  348.627473] amdgpu: qcm fence wait loop timeout expired
[  348.633860] amdgpu: The cp might be in an unrecoverable state due to an unsuccessful queues preemption**_

---

### 评论 #3 — sjjamsa (2021-06-15T10:44:01Z)

Thank you for looking into this!

My first guess also was a broken card.

Thus, I already tried all the 7 non-empty combinations of cards:
* c0 
* c1
* c2
* c0 & c1
* c0 & c2
* c1 & c2
* c0 & c1 & c2

But only the first three (single card) worked; in all other cases clinfo crashes the machine.

Best regards,
 - Simppa -


---

### 评论 #4 — ROCmSupport (2021-06-15T10:52:07Z)

Thanks @sjjamsa 
Then I guess its the PCI slot problem. _[drm] PCI error: detected callback, state(2)!!_
As first slot is working, any card in that slot works.
So I feel the problem is with second slot.

As you said, for example: C0 & C1 --> clinfo crashed, remove C0 from the placeholder and try to run clinfo after reboot.
clinfo might not work. Please give a try.

Thank you.

---

### 评论 #5 — sjjamsa (2021-06-15T11:29:17Z)

Thank you for the advice!

Let me see if I understand you correctly:
You propose that one or more of the PCI slots is broken. You specifically suggest that is the slot for card c0. And this somehow causes problems regardless of which card is enabled in BIOS. How would this happen?

I don't quite understand what you propose me to test. Should I disable C2 and physically remove C1? This combination might work, but it would not give any new information over disabling C1 and C2 in BIOS. Please elaborate.

Best regards,
 - Simppa -

---

### 评论 #6 — sjjamsa (2021-06-15T11:37:28Z)

Just to make everything clear, each card is in a separate PCIe slot; in a separate riser. 

You can have a look at the [Technical Guide](https://i.dell.com/sites/csdocuments/Product_Docs/en/dell-emc-poweredge-r7525-technical-guide.pdf) pages 12-13 and pages 21-22.

Best regards,
 - Simppa -

---

### 评论 #7 — ROCmSupport (2021-06-15T11:54:42Z)

I mean c0 slot is good, c1 slot is bad.
So I recommend to keep a card in c1 and remove all other cards. Try to check whether clinfo crashes or not. 
Thank you.

---

### 评论 #8 — sjjamsa (2021-06-15T12:06:49Z)

To be precise, the three cards are in PCIe slots 2, 5, and 7. 

`dmidecode -t slot:`
- Designation: PCIe Slot 2 ; Bus Address: 0000:21:00.0
- Designation: PCIe Slot 3 ; Bus Address: 0000:41:00.0
- Designation: PCIe Slot 5 ; Bus Address: 0000:81:00.0
- Designation: PCIe Slot 6 ; Bus Address: 0000:a1:00.0
- Designation: PCIe Slot 7 ; Bus Address: 0000:e2:00.0

`lspci  -tvb `
```
-+-[0000:e0]-+-00.0  Advanced Micro Devices, Inc. [AMD] Starship/Matisse Root Complex
 |           +-03.1-[e2-e4]----00.0-[e3-e4]----00.0-[e4]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 738c
 +-[0000:80]-+-00.0  Advanced Micro Devices, Inc. [AMD] Starship/Matisse Root Complex
 |           +-01.1-[81-83]----00.0-[82-83]----00.0-[83]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 738c
 +-[0000:20]-+-00.0  Advanced Micro Devices, Inc. [AMD] Starship/Matisse Root Complex
 |           +-03.1-[21-23]----00.0-[22-23]----00.0-[23]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 738c
```

I now interpret your proposal to be to try the 7 combinations of cards, this time with physically plugging and unplugging the cards. That will take a while, but is doable.

Did you spot something in the dmesg that would indicate which slot (2,5,7) is the culprit, please?

Best regards,
 - Simppa -

---

### 评论 #9 — ROCmSupport (2021-06-15T12:31:52Z)

Its pointing to the below card/slot.

[  340.644125] {1}[Hardware Error]:   **device_id: 0000:83:00.0** --> Slot
[  340.650549] {1}[Hardware Error]:   slot: 0
[  340.655567] {1}[Hardware Error]:   secondary_bus: 0x00
[  340.661619] {1}[Hardware Error]:   **vendor_id: 0x1002, device_id: 0x738c** --> MI100 card

---

### 评论 #10 — sanjtrip (2021-06-15T15:21:59Z)

Disable IOMMU and test - it is currently enabled.

---

### 评论 #11 — ROCmSupport (2021-06-16T04:45:21Z)

Yes, Its also good suggestion.
Hi @sjjamsa 
Can you please **disable IOMMU** and check, things might work.
Thank you.

---

### 评论 #12 — reed259 (2021-06-16T05:47:21Z)

When IOMMU is enabled in Dell Sesto BIOS, please add the "iommu=pt" kernel parameter:

sudo bash -c 'echo GRUB_CMDLINE_LINUX=\"amd_iommu=on iommu=pt\" >> /etc/default/grub'
sudo grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg
sudo reboot

Alternatively, you can disable IOMMU completely via OS and also will not hit this issue.

sudo bash -c 'echo GRUB_CMDLINE_LINUX=\"amd_iommu=off\" >> /etc/default/grub'
sudo grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg
sudo reboot

---

### 评论 #13 — sjjamsa (2021-06-16T06:28:43Z)

The kernel parameters:

`GRUB_CMDLINE_LINUX="amd_iommu=on iommu=pt"`

Did the trick!  At least `/opt/rocm/opencl/bin/clinfo` finishes nicely! :-)

Thank you very much!

Btw, was this documented somewhere? Which document should I have read, please?

Best regards,
 - Simppa -

---

### 评论 #14 — ROCmSupport (2021-06-16T09:55:41Z)

Thanks @sjjamsa for confirmation.
So issue is resolved after disabling IOMMU. I am closing this now.
Let me work with documentation team on the information part.
Thank you.

---

### 评论 #15 — sanjtrip (2021-06-18T00:43:46Z)

Use of rocm-techsupport script (available at https://github.com/amddcgpuce/rocmtechsupport) helps to identify these issues quicker. Use it, as appropriate.

---

### 评论 #16 — lanwatch (2022-04-06T13:11:04Z)

I have a similar issue with the latest version (5.1, but 5.0.2 also was failing). In this case it's a single Radeon PRO W6800. We also have a Mi100 on a twin machine which works just fine. Output of [rocmtechsupport](https://github.com/amddcgpuce/rocmtechsupport) here: [rocm_techsupport.txt](https://github.com/RadeonOpenCompute/ROCm/files/8427118/rocm_techsupport.txt).
 
This is a clean RHEL 8.5 in both cases.

This is what I believe to be the relevant bits of dmesg:

```
[    2.385540] [drm] GART: num cpu pages 131072, num gpu pages 131072
[    2.389720] Uhhuh. NMI received for unknown reason 2d on CPU 55.
[    2.389721] Do you have a strange power saving mode enabled?
[    2.389722] Dazed and confused, but trying to continue
[    2.389725] Uhhuh. NMI received for unknown reason 2d on CPU 35.
[    2.389726] Do you have a strange power saving mode enabled?
[    2.389726] Dazed and confused, but trying to continue 

[...]

[    2.389949] Dazed and confused, but trying to continue
[    2.390305] amdgpu 0000:83:00.0: STB initialized to 2048 entries
[    2.390313] {1}[Hardware Error]: event severity: recoverable
[    2.390318] {1}[Hardware Error]:  Error 0, type: fatal
[    2.390465] [drm] Loading DMUB firmware via PSP: version=0x0202000C
[    2.390776] {1}[Hardware Error]:   section_type: PCIe error
[    2.393295] [drm] use_doorbell being set to: [true]
[    2.393684] {1}[Hardware Error]:   port_type: 1, legacy PCI end point
[    2.394688] [drm] use_doorbell being set to: [true]
[    2.395275] {1}[Hardware Error]:   version: 3.0
[    2.395276] {1}[Hardware Error]:   command: 0x0143, status: 0x4010
[    2.395276] {1}[Hardware Error]:   device_id: 0000:83:00.0
[    2.395277] {1}[Hardware Error]:   slot: 0
[    2.395277] {1}[Hardware Error]:   secondary_bus: 0x00
[    2.395277] {1}[Hardware Error]:   vendor_id: 0x1002, device_id: 0x73a3
[    2.395278] {1}[Hardware Error]:   class_code: 000000
[    2.395278] {1}[Hardware Error]:   aer_uncor_status: 0x00100000, aer_uncor_mask: 0x00010000
[    2.395278] {1}[Hardware Error]:   aer_uncor_severity: 0x004ef030
[    2.395279] {1}[Hardware Error]:   TLP Header: 40009001 8000000f 9927f000 00000000 

[...]

[    2.799605] [drm:amdgpu_ras_eeprom_init [amdgpu]] *ERROR* Failed to read EEPROM table header, res:-5 
```
we have also tested a Radeon Pro W5700 in the same machine (both hw & sw) which works just fine.

I am suspecting the hardware may be faulty?




---
