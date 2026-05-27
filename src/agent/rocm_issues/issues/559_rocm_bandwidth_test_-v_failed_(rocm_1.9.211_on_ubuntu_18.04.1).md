# rocm_bandwidth_test -v failed (rocm 1.9.211 on ubuntu 18.04.1)

> **Issue #559**
> **状态**: closed
> **创建时间**: 2018-09-26T17:13:28Z
> **更新时间**: 2018-09-28T20:39:22Z
> **关闭时间**: 2018-09-28T20:39:22Z
> **作者**: y-lu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/559

## 描述

* OS Platform and Distribution (e.g., Linux Ubuntu 16.04):
Ubuntu 18.04.1 (Kernel version: 4.15.0-35-generic #38-Ubuntu SMP)
rocm version : 1.9.211
rocm-opencl: 1.2.0-2018090737

* GPU model and memory:
Vega Frontier Edition (connected via PCIe riser) + onboard VGA
Motherboard: Supermicro X10SRL-F
CPU: Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz

* Problem:
After a clean boot, rocm_bandwidth_test -v reports error:

$ /opt/rocm/bin/rocm_bandwidth_test -v

    RocmBandwidthTest Version: 1.0.0

    Device: 0,  Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
    Device: 1,  Vega 10 XTX [Radeon Vega Frontier Edition]

    Device Access

    D/D       0         1

    0         1         1

    1         1         1


    Data Path Validation

    D/D       0           1

    0         N/A         FAIL

    1         FAIL        PASS

Relevant logs attached.
[vega-10-rocm-logs.txt](https://github.com/RadeonOpenCompute/ROCm/files/2420813/vega-10-rocm-logs.txt)


---

## 评论 (16 条)

### 评论 #1 — y-lu (2018-09-26T17:15:55Z)

The logs were generated from:
lspci -tv; lspci -n; lsmod; dkms status; lsb_release -a; uname -a; dmesg | grep kfd; dmesg | grep amd

---

### 评论 #2 — jlgreathouse (2018-09-26T18:58:24Z)

Hi @y-lu 

Does anything change if you switch our a different GPU into the PCIe slot you're currently using?
Does anything change if you switch your current GPU to a different PCIe slot?
Does anything change if you try plugging directly into a PCIe slot instead of going through a riser?

---

### 评论 #3 — y-lu (2018-09-26T23:47:07Z)

Hi,

It works without the riser (your suggestion # 3).  I tried the same GPU/PCIe with two different risers, but both failed rocm_bandwidth_test.  Is it possible the amdgpu driver stack needs to do something special to support risers?  The same risers work with nNIDIA cards (was able to run both tensorflow and mxnet), so I thought the hardware should be fine.

$ /opt/rocm/bin/rocm_bandwidth_test -v


          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
          Device: 1,  Vega 10 XTX [Radeon Vega Frontier Edition]

          Device Access

          D/D       0         1

          0         1         1

          1         1         1


          Data Path Validation

          D/D       0           1

          0         N/A         PASS

          1         PASS        PASS




---

### 评论 #4 — jlgreathouse (2018-09-27T00:23:58Z)

Hi @y-lu thanks for the added info.

With the riser installed, could you try running the bandwidth test with the environment variable `HSA_ENABLE_SDMA=0`? For instance, `HSA_ENABLE_SDMA=0 /opt/rocm/bin/rocm_bandwidth_test -v`?

With the rister installed, could you also run the following as root?: `cat /sys/class/hwmon/hwmon0/device/current_link_speed`

In addition, is this an active riser/splitter? Or is this a simple passive 90-degree riser so that you can install these cards in a 2U rackmount case? Is there a make/model?

Thanks again.

---

### 评论 #5 — y-lu (2018-09-27T00:51:27Z)

Hi, 

It's an active riser.  I bought it on amazon (https://www.amazon.com/gp/product/B073LZZL9H/)

Here are the output you requested:
$ cat /sys/class/hwmon/hwmon0/device/current_link_speed
8 GT/s

$ HSA_ENABLE_SDMA=0 /opt/rocm/bin/rocm_bandwidth_test -v


          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
          Device: 1,  Vega 10 XTX [Radeon Vega Frontier Edition]

          Device Access

          D/D       0         1

          0         1         1

          1         1         1


          Data Path Validation

          D/D       0           1

          0         N/A         FAIL

          1         FAIL        PASS


---

### 评论 #6 — jlgreathouse (2018-09-27T01:14:01Z)

Last question: What is the output of `/sys/class/hwmon/hwmon0/device/current_link_width`?

I suspect that these PCIe risers are taking your PCIe connection out of spec, and as such your GPUs are not able to accurately transfer data at PCIe gen 3 speeds. My suspicion is that these risers have not passed PCI-SIG conformance testing, and as such I cannot guarantee that they are meeting the analog electrical specifications needed for our GPU to accurate transfer data to the PCIe controller on the other end of the bus.

Some GPUs may be OK operating in this non-conformant situation -- it appears that yours are not. As such, I recommend that if you need risers for your system you buy from a known vendor. For example, SuperMicro sells [PCIe riser boards to so that you can install GPUs in server chases](https://www.supermicro.com/support/resources/Riser.cfm). I am not personally aware of any "PCIe Gen 3 through USB3 cable" extenders that have met PCI-SIG compliance. That doesn't mean they don't exist, only that I haven't seen any.

One possibility: you could try forcibly lowering the PCIe speed (generation) in your BIOS to Gen 2 or Gen 1. I do not know if your motherboard's BIOS has such a setting, but it may be worth looking into. Perhaps your risers can operate at lower speeds. I can't guarantee this, however.

---

### 评论 #7 — y-lu (2018-09-27T01:53:41Z)

Hi,

Here's the output:
$ cat /sys/class/hwmon/hwmon0/device/current_link_width
16

I will try and see if I can lower the speed and report back.  

Also, thanks for your suggestion of risers.  I still have some questions though: looking at the pictures, I'm not sure they would allow enough room to plug in a GPU (I assume they don't use any cables?).  One reason I'm using risers is that my case cannot hold 6 GPUs.  I'd love to hear your advice.

Thanks!

---

### 评论 #8 — jlgreathouse (2018-09-27T01:56:47Z)

That is your output of `current_link_width` with the riser plugged in? Based on the amazon description of your risers, these should actually be x1 links, not x16. Perhaps that is part of the issue.

I'm sorry to say that I'm unable to offer you any advice about which risers would work with your motherboard and case. You should contact your system vendor and perhaps they can recommend something.

---

### 评论 #9 — y-lu (2018-09-27T03:47:56Z)

Yes, that's with the riser plugged in.

The good news is lowering PCIe speed seems to be a workaround. After setting PCIe to gen2, and limiting the payload to 128 bytes, I am now able to run tensorflow benchmarks on a single GPU without problem. 

On the other hand, rocm_bandwidth_test -v still report the same failure as before. Is it because the use of PCIe-USB-PCIe somehow prevents the diagnostic from running properly?



---

### 评论 #10 — jlgreathouse (2018-09-27T04:54:43Z)

If `rocm_bandwidth_test -v` is reporting errors, its because your PCIe link is still producing errors. tensorflow may be somewhat resilient to errors that happen during transfers, but such a setup may crash unexpectedly, produce incorrect results, and generally cause you more difficulties in the future.

---

### 评论 #11 — y-lu (2018-09-27T05:19:41Z)

If PCIe link is producing errors, would it be logged by the kernel? If not, where else can I find details about the errors?  Thanks.

---

### 评论 #12 — jlgreathouse (2018-09-27T16:46:23Z)

Hi @y-lu 

You could modify the source to `rocm_bandwidth_test` to show the data before transmission and after transmission to see what kind of errors it is observing. Depending on the kind of error, your chipset's [EDAC hardware may log errors](https://www.kernel.org/doc/html/v4.14/driver-api/edac.html) that could be seen in `dmesg` logs.
 
That said, I don't know how much time AMD can dedicate to helping you debug non-compliant PCIe risers. I would still caution against trusting any of your results from a GPU-using tensorflow if you can't be sure the data being sent to the GPU is accurate.

---

### 评论 #13 — y-lu (2018-09-28T01:02:03Z)

Thanks for the suggestion.  I'll check out the source code of rocm_bandwidth_test and see if I can get more information.



---

### 评论 #14 — y-lu (2018-09-28T01:39:10Z)

So it turns out again related to the bandwidth.  The validation mode test uses the "peak" bandwidth. If I change to "avg" speed, it works without any problem.
```
diff --git a/rocm_bandwidth_test_report.cpp b/rocm_bandwidth_test_report.cpp
index aab87ee..860735a 100755
--- a/rocm_bandwidth_test_report.cpp
+++ b/rocm_bandwidth_test_report.cpp
@@ -304,7 +304,7 @@ void RocmBandwidthTest::DisplayValidationMatrix() const {
     uint32_t dst_idx = trans.copy.dst_idx_;
     uint32_t src_dev_idx = pool_list_[src_idx].agent_index_;
     uint32_t dst_dev_idx = pool_list_[dst_idx].agent_index_;
-    perf_matrix[(src_dev_idx * agent_index_) + dst_dev_idx] = trans.peak_bandwidth_[0];
+    perf_matrix[(src_dev_idx * agent_index_) + dst_dev_idx] = trans.avg_bandwidth_[0];
   }

   uint32_t format = 10;
```
====
$ ./rocm_bandwidth_test -v


          RocmBandwidthTest Version: 1.0.0

          Device: 0,  Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz
          Device: 1,  Vega 10 XTX [Radeon Vega Frontier Edition]
          Device: 2,  Vega 10 XTX [Radeon Vega Frontier Edition]
          Device: 3,  Vega 10 XTX [Radeon Vega Frontier Edition]
          Device: 4,  Vega 10 XTX [Radeon Vega Frontier Edition]

          Device Access

          D/D       0         1         2         3         4

          0         1         1         1         1         1

          1         1         1         1         1         1

          2         1         1         1         1         1

          3         1         1         1         1         1

          4         1         1         1         1         1


          Data Path Validation

          D/D       0           1           2           3           4

          0         N/A         PASS        PASS        PASS        PASS

          1         PASS        PASS        PASS        PASS        PASS

          2         PASS        PASS        PASS        PASS        PASS

          3         PASS        PASS        PASS        PASS        PASS

          4         PASS        PASS        PASS        PASS        PASS



---

### 评论 #15 — jlgreathouse (2018-09-28T01:52:14Z)

Note that you could also try setting some kernel boot-time parameters to further lower the speed of your PCIe bus. On your Linux kernel command line, you could add `amdgpu.pcie_gen_cap=1` to try to force PCIe gen 1 mode. You could also force fewer lanes by adding `amdgpu.pcie_lane_cap=0x0010000` to turn on x1 mode.

Note that you could set other PCIe widths using the following values from the amdgpu driver:
```
#define CAIL_PCIE_LINK_WIDTH_SUPPORT_X1          0x00010000
#define CAIL_PCIE_LINK_WIDTH_SUPPORT_X2          0x00020000
#define CAIL_PCIE_LINK_WIDTH_SUPPORT_X4          0x00040000
#define CAIL_PCIE_LINK_WIDTH_SUPPORT_X8          0x00080000
#define CAIL_PCIE_LINK_WIDTH_SUPPORT_X12         0x00100000
#define CAIL_PCIE_LINK_WIDTH_SUPPORT_X16         0x00200000
```

PCIe gen 1 x1 will be very, very low bandwidth. However, the fact that you bought a bunch of x1 risers implies that you don't care much about PCIe bandwidth. :)

---

### 评论 #16 — y-lu (2018-09-28T02:13:27Z)

Thanks for the tip; I didn't know of that parameter. 

And yes, while It's nice to have higher PCIe bandwidth, it's likely not the bottleneck of my deep learning system (yet).  

Also, my system seems more stable after manually setting sclk to ~1300Mhz and keeping the GPU temperature below 50C.

---
