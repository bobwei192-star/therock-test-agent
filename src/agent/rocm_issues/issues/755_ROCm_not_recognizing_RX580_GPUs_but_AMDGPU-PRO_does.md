# ROCm not recognizing RX580 GPUs but AMDGPU-PRO does

> **Issue #755**
> **状态**: closed
> **创建时间**: 2019-04-05T01:20:01Z
> **更新时间**: 2019-04-05T18:48:51Z
> **关闭时间**: 2019-04-05T18:48:51Z
> **作者**: pgaffney
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/755

## 描述

did a completely clean install of ROCm on Ubuntu 18.04 and 7 of my 8 GPUs get "PCI rejects atomics"; another clean rebuild with AMDGPU-PRO 18.50 on same Ubuntu recognizes and lights up all 8 GPUs; what am I missing in my ROCm install?

---

## 评论 (12 条)

### 评论 #1 — jlgreathouse (2019-04-05T01:43:03Z)

You're missing PCIe atomics, which amdgpu-pro does not require. :)

---

### 评论 #2 — pgaffney (2019-04-05T01:58:56Z)

what component is missing the PCIe atomics? CPU is a Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz and the RX580's are listed as supported GPUs; sorry for what is probably a silly question but I've searched high and low and can't understand what component is not providing PCIe atomics

---

### 评论 #3 — jlgreathouse (2019-04-05T02:42:49Z)

I would guess that you are using a PCIe bridge, switch, or extender that does not support the forwarding of atomics.  [Your CPU](https://ark.intel.com/content/www/us/en/ark/products/88195/intel-core-i7-6700k-processor-8m-cache-up-to-4-20-ghz.html) only has can only be configured to have up to 3 PCIe connections directly to the CPU. The Ark listing says that the 16 PCIe lanes can be configured as "1x16, 2x8, [or] 1x8+2x4". As such, I suspect that you're hooking some or most of your GPUs through a PCIe switch. Or, depending on your motherboard, that your remaining 7 PCIe slots are connected through the chipset, and that your motherboard chipset does not support PCIe atomics.

See also these two answers for similar situations: [1](https://github.com/RadeonOpenCompute/ROCm/issues/622#issuecomment-441941594) [2](https://github.com/RadeonOpenCompute/ROCm/issues/589#issuecomment-433636380)

---

### 评论 #4 — pgaffney (2019-04-05T11:07:32Z)

thanks for helping on this; condensed from my `lspci -vvv` output:
for each of the 8 GPUs: 
```
Capabilities: [58] Express (v2) Legacy Endpoint, MSI 00
...
DevCap2: ... AtomicOpsCap: 32bit+ 64bit+ 128bitCAS-
```
Is the 128bit the problem or is there something else?

---

### 评论 #5 — jlgreathouse (2019-04-05T13:22:11Z)

It's not about each of the 8 GPUs. It's about all of the connections between the GPUs and the CPU's root complex. While all 8 of your GPUs support PCIe atomics, something in between your CPU and the 7 non-working GPUs does not support forwarding of PCIe atomics.

---

### 评论 #6 — pgaffney (2019-04-05T13:40:24Z)

I get that in concept I'm just a little lost on how to find the link that is not working. The MOB is an ASUS  B250 with the latest firmware and the RX580s are each on PCI risers. The MOB has 19 PCIe slots and I'm using the first 8. What are the requirements of the MOB PCI slots and the risers? How do I interrogate those?

---

### 评论 #7 — valeriob01 (2019-04-05T13:46:47Z)

PCI risers do not work with ROCm.


---

### 评论 #8 — jlgreathouse (2019-04-05T14:40:19Z)

Indeed, none of the 1x slots on your motherboard support PCIe atomics. Your CPU only has 16 lanes that support PCIe atomics, and looking at that motherboard -- that would be the single 16x slot. All of the other slots likely go through the motherboard's chipset.  The B250 chipset does not support atomics. See [my response in this issue](https://github.com/RadeonOpenCompute/ROCm/issues/439#issuecomment-452380308).

We can continue down the path of exploring your motherboard with lspci (you can see what devices your GPUs are connected through, visually, with `lspci -t`, then see if any upstream active devices between the CPU's root complex and your non-working GPUs support the atomic routing capability). However, I can assure you that the reason your GPUs are not working with ROCm is because your CPU cannot talk to your GPU using PCIe atomics.

---

### 评论 #9 — valeriob01 (2019-04-05T15:05:08Z)

That's a good label, but on the single 16x slot of B250 it supports atomics, and works with ROCm.
So it is just an unsupported configuration after all.


---

### 评论 #10 — pgaffney (2019-04-05T15:09:37Z)

> Indeed, none of the 1x slots on your motherboard support PCIe atomics. Your CPU only has 16 lanes that support PCIe atomics, and looking at that motherboard -- that would be the single 16x slot. All of the other slots likely go through the motherboard's chipset. The B250 chipset does not support atomics. See [my response in this issue](https://github.com/RadeonOpenCompute/ROCm/issues/439#issuecomment-452380308).
> 
> We can continue down the path of exploring your motherboard with lspci (you can see what devices your GPUs are connected through, visually, with `lspci -t`, then see if any upstream active devices between the CPU's root complex and your non-working GPUs support the atomic routing capability). However, I can assure you that the reason your GPUs are not working with ROCm is because your CPU cannot talk to your GPU using PCIe atomics.

Thanks for the thorough answer - that makes sense. TL;DR is this is a motherboard issue - can any motherboard support PCIe atomics on 1x slots?

---

### 评论 #11 — jlgreathouse (2019-04-05T16:39:30Z)

Some may be able to, but I do not have an encyclopedic knowledge of all motherboards, so I can't give you a list.

If you want a motherboard that does this, it would need an active PCIe switch that supports forwarding PCIe atomics. And that switch would have to be connected directly to the CPU. Your CPU only has 16 PCIe 3.0 lanes coming out of it, and the CPU only supports splitting these lanes into the following configurations:
- 1x16 (your current motherboard uses this)
- 2x8
- 1x8+2x4

If you wanted to pull this into multiple x1 lanes, a manufacturer would need to take one of these configurations, run it to an active PCIe switch, and then have that switch routed to multiple x1 connectors. That switch would also need to support forwarding PCIe atomics.

I do not know if any manufacturers have designed such a system. I suspect not, as most of "cram as many GPUs into a single box as possible with no regard for PCIe bandwidth" designs are build for the crypto mining market. That market is very cost conscious, and an active switch is more expensive than just connecting to the chipset (as your board does).

---

### 评论 #12 — pgaffney (2019-04-05T18:48:51Z)

thanks for the education (and I'm happy to have a new version of lpsci)

---
