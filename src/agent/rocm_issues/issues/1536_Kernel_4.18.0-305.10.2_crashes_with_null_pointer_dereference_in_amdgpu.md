# Kernel 4.18.0-305.10.2 crashes with null pointer dereference in amdgpu

> **Issue #1536**
> **状态**: closed
> **创建时间**: 2021-07-29T02:28:31Z
> **更新时间**: 2021-07-29T08:07:05Z
> **关闭时间**: 2021-07-29T08:07:05Z
> **作者**: ekeever1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1536

## 描述

We recently updated the kernel on a system running Epyc Milan + MI50 to 4.18.0-305.10.2 due to cve-2021-33909, and we are finding it to be violently incompatible with all of our installed ROCm toolchains (3.8, 4.1 and 4.2).

Basic hello-world level test scripts fail, emitting on the command line
```
    HSA Error:  Incompatible kernel and userspace, Vega 20 disabled.
    Upgrade amdgpu.
```
and provoking in dmesg
`    amdgpu: init_user_pages: Failed to get user pages: -1`

This is our Epyc Milan system, supermicro H12DSG-O-CPU motherboard with latest v.2.1 BIOS installed (as required by Milan). The crash occurs with 100% repeatability after any attempt to access the ROCm API in even the simplest hello-world test codes.

This is the trailing end of one of the vmcore-dmesg.txt generated when the system implodes:
```
[  240.171608] docker0: port 1(veth5fa6990) entered forwarding state [  240.731216] eth0: renamed from vethd63cc46 [  240.742367] IPv6: ADDRCONF(NETDEV_CHANGE): veth5fa6990: link becomes ready
_(these occur when my test_hipcc.sh script attempts to run helloworld
programs)_
[  270.306992] amdgpu: init_user_pages: Failed to get user pages: -1
[  270.307005] amdgpu: init_user_pages: Failed to get user pages: -1
[  270.307011] amdgpu: init_user_pages: Failed to get user pages: -1 
[  270.307016] amdgpu: init_user_pages: Failed to get user pages: -1 
[  313.784173] amdgpu: init_user_pages: Failed to get user pages: -1 
[  313.784185] amdgpu: init_user_pages: Failed to get user pages: -1 
[  313.784192] amdgpu: init_user_pages: Failed to get user pages: -1
[  313.784196] amdgpu: init_user_pages: Failed to get user pages: -1 
[  314.665715] amdgpu: init_user_pages: Failed to get user pages: -1
[  314.665729] amdgpu: init_user_pages: Failed to get user pages: -1
[  314.665736] amdgpu: init_user_pages: Failed to get user pages: -1
[  314.665741] amdgpu: init_user_pages: Failed to get user pages: -1
_(these occur shortly after the script finally exists with failure)_
[  332.619544] BUG: unable to handle kernel NULL pointer dereference at
0000000000000134
[  332.619549] PGD 0 P4D 0
[  332.619552] Oops: 0000 [#1] SMP NOPTI 
[  332.619556] CPU: 90 PID: 2639 Comm: kworker/90:2 Kdump: loaded
Tainted: P           OE    --------- -  - 4.18.0-305.10.2.el8_4.x86_64
#1
[  332.619557] Hardware name: Supermicro AS -4124GS-TNR/H12DSG-O-CPU, BIOS 2.1 05/10/2021 
[  332.619603] Workqueue: kfd_process_wq kfd_process_wq_release [amdgpu] 
[  332.619644] RIP: 0010:kfd_iommu_unbind_process+0x29/0x60 [amdgpu] 
[  332.619646] Code: 00 0f 1f 44 00 00 41 54 55 48 8d af 50 01 00 00 53
48 8b 9f 50 01 00 00 48 39 eb 74 33 49 89 fc eb 08 48 8b 1b 48 39 eb 74
26 <83> bb 34 01 00 00 01 75 ef 48 8b 43 10 41 8b b4 24 48 01 00 00 48 
[  332.619647] RSP: 0018:ffffbbfd75103e58 EFLAGS: 00010203 
[  332.619648] RAX: ffffffffc0cb4420 RBX: 0000000000000000 RCX:
ffff966c0faa97e0
[  332.619649] RDX: 0000000000000001 RSI: ffff966ad5afb828 RDI:
ffff966ad5afb800
[  332.619649] RBP: ffff966ad5afb950 R08: 0000000000000008 R09:
000071775f737365
[  332.619649] R10: 8080808080808080 R11: 0000000000000010 R12:
ffff966ad5afb800
[  332.619650] R13: ffff966ad5afb800 R14: ffff962d10e4d440 R15:
ffff966ad5afb828
[  332.619651] FS:  0000000000000000(0000) GS:ffff966c0fa80000(0000)
knlGS:0000000000000000
[  332.619651] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033 
[  332.619652] CR2: 0000000000000134 CR3: 00000007dba10005 CR4:
0000000000770ee0
[  332.619652] PKRU: 55555554
[  332.619653] Call Trace:
[  332.619693]  kfd_process_wq_release+0xc3/0x160 [amdgpu] 
[  332.619701]  process_one_work+0x1a7/0x360 
[  332.619703]  ? create_worker+0x1a0/0x1a0 
[  332.619704]  worker_thread+0x30/0x390 
[  332.619706]  ? create_worker+0x1a0/0x1a0 
[  332.619707]  kthread+0x116/0x130 
[  332.619709]  ? kthread_flush_work_fn+0x10/0x10 
[  332.619715]  ret_from_fork+0x22/0x40 
[  332.619717] Modules linked in: veth mmfs26(OE) mmfslinux(OE)
tracedev(OE) rpcsec_gss_krb5 auth_rpcgss nfsv4 dns_resolver nfs lockd grace fscache xt_CHECKSUM ipt_REJECT tun xt_conntrack ipt_MASQUERADE nf_conntrack_netlink nft_counter xt_addrtype br_netfilter bridge nf_nat_tftp nf_conntrack_tftp nft_masq nft_objref nf_conntrack_netbios_ns nf_conntrack_broadcast nft_fib_inet
nft_fib_ipv4 nft_fib_ipv6 nft_fib nft_reject_inet nf_reject_ipv4
nf_reject_ipv6 nft_reject nft_ct nf_tables_set nft_chain_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 ip6_tables nft_compat ip_set 8021q garp mrp stp llc overlay nf_tables nfnetlink rdma_ucm(OE)
rdma_cm(OE) iw_cm(OE) ib_ipoib(OE) ib_cm(OE) ib_umad(OE) mlx5_ib(OE)
mlx5_core(OE) mlxdevm(OE) auxiliary(OE) ib_uverbs(OE) ib_core(OE)
mlx_compat(OE) tls psample mlxfw(OE) pci_hyperv_intf sunrpc ext4 mbcache jbd2 intel_rapl_msr nvidia_drm(POE) intel_rapl_common amd64_edac_mod nvidia_modeset(POE) edac_mce_amd amd_energy nvidia(POE) kvm_amd kvm irqbypass 
[  332.619758]  joydev raid0 crct10dif_pclmul crc32_pclmul ghash_clmulni_intel wmi_bmof pcspkr rapl sp5100_tco ipmi_ssif k10temp
i2c_piix4 ccp acpi_ipmi ipmi_si ipmi_devintf ipmi_msghandler acpi_cpufreq knem(OE) binfmt_misc ip_tables xfs sd_mod sg rndis_host cdc_ether usbnet mii amdgpu ast iommu_v2 drm_vram_helper gpu_sched drm_ttm_helper ttm drm_kms_helper ahci libahci syscopyarea sysfillrect sysimgblt bnx2x fb_sys_fops igb libata drm dca mdio i2c_algo_bit libcrc32c crc32c_intel nvme nvme_core t10_pi wmi pinctrl_amd dm_mirror dm_region_hash dm_log dm_mod fuse [last unloaded: tls] 
[  332.619785] CR2: 0000000000000134
```

This system has been extremely unstable since installation of -305.10.2. There are 7 other crash dumps stored on our system just from today, with "only" a majority of them naming the rocm problem above as the cause of the crash.

When the system was rebooted into the previous kernel it was virtually unusable because expected network interfaces were not available (the most beloved feature of the nvidia cuda drivers, now available for your network interface drivers too!). Eventually I copied over a binary to test with... this failed to run
("hipErrorNoBinaryForGpu: Unable to find code object for all current devices!"), but did not provoke a deadly kernel panic. I was also able to run "rocminfo" v.4.2 successfully in kernel 4.18.0-240. 

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-07-29T08:07:05Z)

Hi @ekeever1 
Thanks for reaching out.
I certainly understood the problem.

As per the ROCm documentation: [https://github.com/RadeonOpenCompute/ROCm#supported-operating-systems](url), 
ROCm 4.x supports minimum 5.4.x kernel officially.
We do not validate latest ROCm versions like 4.3, 4.2 with old kernels like 4.18.x.x, 3.x.x.x like that and we do not support these combinations too.
We always try to provide latest kernel support with latest ROCm versions.
So conclusion is that ROCm might/does not work with old kernel versions and so recommend to try with the latest LTS versions of Ubuntu like 20.04.2 + supported kernels with those OSes.
Hope this helps.
Thank you.


---
