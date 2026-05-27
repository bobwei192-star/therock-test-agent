# Query for New Ubuntu 18.04 setup: Radeon R5 230 for Display and Radeon VII for Computation

> **Issue #747**
> **状态**: closed
> **创建时间**: 2019-03-20T04:27:59Z
> **更新时间**: 2019-08-07T16:49:35Z
> **关闭时间**: 2019-08-07T16:49:35Z
> **作者**: avimanyu786
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/747

## 描述

Hello,

I'm awaiting the Radeon VII for my new home-lab PC that was assembled a few days ago. I attempted installing ROCm without the Radeon VII while I have the R5 230 right now. The 1080p display lost its original 1920x1080 resolution and dropped to a low resolution right after reboot . The rocminfo and clinfo commands would also show up errors. I later found that the ROCm installation had also removed the monitor.xml file located at $HOME/.config. As I still don't have the Radeon VII yet and that ROCm might not support the low-end card, I did not try any more troubleshooting attempts and reinstalled Ubuntu.

My query is regarding the installation procedure after I later connect the Radeon VII. As I would still be using the R5 230 for display, is it possible that this resolution issue will occur again? Is it not possible to keep the R5 230 graphics unaffected from the ROCm installation once the Radeon VII is there? Should I connect the Radeon VII to the display when installing ROCm? What about when I connect the display back again to the R5 230 after the ROCm installation?

My lab configuration:

ASUS Strix B450F Motherboard
AMD Ryzen 2700X CPU
Sapphire AMD Radeon R5 230 2GB DDR3 Graphics Card (For Display)
Sapphire AMD Radeon VII 16 GB HBM2 (Not connected yet)
Corsair 2x16 GB 3200 Mhz DDR4 RAM
WD Blue 500 GB M2 SSD
WD NAS Red 4 TB HDD
Corsair TX Gold 850M PSU
Corsair Spec 1 Case
ASUS 22" VZ229H Monitor

Thank you.



---

## 评论 (12 条)

### 评论 #1 — jlgreathouse (2019-03-20T15:20:10Z)

The Radeon R5 230 uses the `radeon` driver, while ROCm requires the `amdgpu` driver. As part of the ROCm installation process, we blacklist the `radeon` driver so that `amdgpu` will work propersly. As such, Is suspect that your R5 230 will only work in software VGA mode if you install ROCm.

---

### 评论 #2 — avimanyu786 (2019-03-20T18:10:49Z)

Thanks a lot for the clarification. Please keep this issue open until I connect the Radeon VII. It would take a week at most.

---

### 评论 #3 — avimanyu786 (2019-03-20T18:16:26Z)

Also, could you please recommend a replacement low-end card in place of the R5 230 that uses the 'amdgpu' driver.

---

### 评论 #4 — kentrussell (2019-03-20T19:30:05Z)

Radeon RX550 or RX550X (Lexa), Radeon RX560 (Baffin), R7 260 (Bonaire), R7 265 (Pitcairn), are all options <$150 at launch. Can potentially get them cheaper now that Bonaire and Pitcairn are a bit older. Hawaii/Tonga/Polaris10/Vega10/Vega20 are all supported, but are pricier. 

---

### 评论 #5 — jlgreathouse (2019-03-20T19:38:58Z)

Note that Baffin, Bonaire, and Pitcairn are not supported as ROCm compute devices. Lexa should be, however.

---

### 评论 #6 — kentrussell (2019-03-20T19:52:00Z)

Thanks Joe. I was just going through GPUIDs in the amdgpu_drv.c file :)

---

### 评论 #7 — avimanyu786 (2019-03-20T20:43:03Z)

Thanks so much @kentrussell @jlgreathouse !

---

### 评论 #8 — avimanyu786 (2019-03-21T06:20:51Z)

I just recalculated my remaining expenses for the new Radeon VII. In India, it is costing me > $900 due to revised taxation rules. So purchasing another $100-150 card is really very difficult for me. 

I'd be very grateful if you could please suggest a workaround to be able to get the R5 230 to keep working with the 1080p display. It was purchased only for the display as the 2700X does not include integrated graphics. Since the RVII would only be used for computation purpose with ROCm, I do not plan to use it for the display but only when running graphical simulations. In the future, if going for a second larger monitor (preferably 32"), I would be connecting the RVII to the same. During running computations I would plan to disable the secondary display. 

I recently looked up online for a workaround and found some references:

https://launchpad.net/~oibaf/+archive/ubuntu/graphics-drivers

https://wiki.archlinux.org/index.php/AMDGPU#Enable_Southern_Islands_(SI)_and_Sea_Islands_(CIK)_support

https://varunpriolkar.com/2016/12/how-to-use-amdgpu-driver-for-southern-islands-and-sea-islands-card-on-ubuntu-linux/

Perhaps it could work for Ubuntu 18.04? Should I downgrade to 16.04?

Thanks again for the support so far!

---

### 评论 #9 — avimanyu786 (2019-03-29T17:49:00Z)

Recently got the Radeon VII. Tried every possible way to get both the cards working. But Ubuntu 18.04 refuses to even boot when the legacy card is attached on the second PCIe. When using `nomodeset ` it would give an UMS error for the Radeon module. The RVII works only when I remove the R5 230. Installed ROCm based on the official documentation and everything went perfectly fine.

---

### 评论 #10 — briansp2020 (2019-03-29T18:08:28Z)

I have NVidia 1080 in the second PCIe slot and Radeon VII in the first PCIe slot and they work ok with Ryzen 1800X and GigaByte AB350M-D3H (rev. 1.0)

Initially, when I had 1080 and Vega FE, I had problem setting them up properly. After updating BIOS to the latest and selecting the second PCIe slot as the initial video output device in BIOS, things started working.

So, if you haven't, try updating to the latest BIOS and setting the initial video output device to PCIe slot 2 .

---

### 评论 #11 — avimanyu786 (2019-03-29T18:47:42Z)

Thanks @briansp2020. On the current BIOS, I couldn't find any such option.

---

### 评论 #12 — avimanyu786 (2019-08-07T16:49:35Z)

Long cherished dream finally fulfilled in my little lab. Got the RX 550 and it worked straight out of the box. Cheers to ROCm! Thank you @jlgreathouse @kentrussell @briansp2020 !!!

---
