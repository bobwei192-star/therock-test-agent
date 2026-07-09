# Errors installing rocm-dkms:  dracut:Failed to install module amdkfd

- **Issue #:** 774
- **State:** closed
- **Created:** 2019-04-18T15:52:43Z
- **Updated:** 2019-04-18T16:30:53Z
- **URL:** https://github.com/ROCm/ROCm/issues/774

Hello,

I'm running CentOS7.6 with the `5.0.8` mainline kernel from ELrepo to include a lot of the fixes for known issues like `amdgpu: [powerplay] failed to send message 261
ret is 0` that's addressed [in this patch here.](https://patchwork.freedesktop.org/patch/259364/)

I've not had much luck trying to setup the proprietary amdgpu drivers with the newer kernel so thought I'd try ROCm.

When installing via RPM / repo I get the following error for the dkms part:

```Message from syslogd@tomatan at Apr 18 11:10:12 ...
 dracut:Failed to install module amdkfd
Loading new amdgpu-2.3-14.el7 DKMS files...
Building for 5.0.8-1.el7.elrepo.x86_64
Building initial module for 5.0.8-1.el7.elrepo.x86_64
Done.
Forcing installation of amdgpu

amdgpu.ko:
Running module version sanity check.
 - Original module
   - Found /lib/modules/5.0.8-1.el7.elrepo.x86_64/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko
   - Storing in /var/lib/dkms/amdgpu/original_module/5.0.8-1.el7.elrepo.x86_64/x86_64/
   - Archiving for uninstallation purposes
 - Installation
   - Installing to /lib/modules/5.0.8-1.el7.elrepo.x86_64/extra/

amdttm.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/5.0.8-1.el7.elrepo.x86_64/extra/

amdkcl.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/5.0.8-1.el7.elrepo.x86_64/extra/

amd-sched.ko:
Running module version sanity check.
 - Original module
 - Installation
   - Installing to /lib/modules/5.0.8-1.el7.elrepo.x86_64/extra/
Adding any weak-modules
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol trace_raw_output_prep
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol bpf_trace_run2
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol prepare_to_wait_event
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol event_triggers_call
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol trace_event_buffer_commit
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol trace_event_ignore_this_pid
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol init_wait_entry
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol __list_add_valid
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol perf_trace_buf_alloc
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol trace_event_reg
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol __cpu_online_mask
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol __list_del_entry_valid
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol bpf_trace_run1
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol pv_ops
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol ex_handler_refcount
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol call_rcu
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol trace_event_buffer_reserve
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amd-sched.ko needs unknown symbol trace_handle_return
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol trace_raw_output_prep
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol event_triggers_call
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol trace_event_buffer_commit
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol trace_event_ignore_this_pid
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol perf_trace_buf_alloc
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol trace_event_reg
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol __cpu_online_mask
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol bpf_trace_run1
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol ex_handler_refcount
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol trace_event_buffer_reserve
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdkcl.ko needs unknown symbol trace_handle_return
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol devmap_managed_key
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol __put_page
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol ww_mutex_lock_interruptible
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol vmf_insert_pfn
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol memcpy_fromio
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol prepare_to_wait_event
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol memcpy_toio
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol clear_page_rep
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol dma_direct_unmap_page
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol init_wait_entry
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol __list_add_valid
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol dma_alloc_attrs
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol dma_direct_map_page
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol clear_page_orig
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol ww_mutex_lock
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol clear_page_erms
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol __list_del_entry_valid
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol __default_kernel_pte_mask
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol pv_ops
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol ex_handler_refcount
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol dma_free_attrs
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol vmf_insert_mixed
depmod: WARNING: /lib/modules/3.10.0-957.10.1.el7.x86_64/weak-updates/amdttm.ko needs unknown symbol memset_io
Possible missing firmware "amdgpu/raven_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "radeon/hawaii_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "radeon/bonaire_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_sos.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_sos.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec2_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_me_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_pfp_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_ce_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec2_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_me_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_pfp_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_ce_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec2_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_me_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_pfp_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_ce_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_vcn.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_acg_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_smc_sk.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_smc_sk.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_gpu_info.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/si58_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tahiti_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tahiti_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tahiti_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tahiti_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tahiti_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/banks_k_2_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hainan_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/oland_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/verde_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/pitcairn_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tahiti_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_k_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_k_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_k_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_mc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_sos.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_sos.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_ta.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_asd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_sos.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec2_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_me_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_pfp_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_ce_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec2_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_me_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_pfp_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_ce_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec2_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_me_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_pfp_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_ce_2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_rlc_am4.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_rlc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_mec2.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_mec.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_me.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_pfp.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_ce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_sdma1.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_sdma.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_uvd.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/stoney_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/carrizo_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/mullins_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kaveri_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/kabini_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_vce.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven2_vcn.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/picasso_vcn.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_vcn.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega12_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_acg_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega10_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vegam_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris12_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_k2_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_smc_sk.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris11_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_k2_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_smc_sk.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/polaris10_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/fiji_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/tonga_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/topaz_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/hawaii_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_k_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/bonaire_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/vega20_smc.bin" for kernel module "amdgpu.ko"
Possible missing firmware "amdgpu/raven_dmcu.bin" for kernel module "amdgpu.ko"
Failed to install module amdkfd

depmod...

Backing up initramfs-5.0.8-1.el7.elrepo.x86_64.img to /boot/initramfs-5.0.8-1.el7.elrepo.x86_64.img.old-dkms
Making new initramfs-5.0.8-1.el7.elrepo.x86_64.img
(If next boot fails, revert to initramfs-5.0.8-1.el7.elrepo.x86_64.img.old-dkms image)
dracut............

DKMS: install completed.
```

Just trying the opencl installation I get the following:

```
Running transaction
  Installing : hsakmt-roct-1.0.9_135_g34da614-1.x86_64                                                                     1/5 
  Installing : hsa-rocr-dev-1.1.9_64_g619177ee-1.x86_64                                                                    2/5 
  Installing : rocm-opencl-1.2.0-2019040803.x86_64                                                                         3/5 
  Installing : rocm-opencl-devel-1.2.0-2019040803.x86_64                                                                   4/5 
  Installing : rock-dkms-2.3-14.el7.noarch                                                                                 5/5 

Broadcast message from systemd-journald@tomatan.firi.dev (Thu 2019-04-18 11:28:53 EDT):

dracut[32077]: Failed to install module amdkfd


Message from syslogd@tomatan at Apr 18 11:28:53 ...
 dracut:Failed to install module amdkfd
```

Any idea what I might be missing?