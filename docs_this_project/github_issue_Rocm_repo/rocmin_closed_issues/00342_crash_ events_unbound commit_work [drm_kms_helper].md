# crash: events_unbound commit_work [drm_kms_helper]

- **Issue #:** 342
- **State:** closed
- **Created:** 2018-02-21T03:22:05Z
- **Updated:** 2018-06-03T14:43:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/342

Ubuntu 17.10, ROCm 1.7, Vega64.
While running the OpenCL app GpuOwl, I get a complete GPU freeze. I see this in dmesg:

```
[707581.262503] INFO: task kworker/u34:0:13629 blocked for more than 120 seconds.
[707581.262508]       Tainted: G           OE   4.13.0-32-generic #35-Ubuntu
[707581.262509] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[707581.262511] kworker/u34:0   D    0 13629      2 0x00000000
[707581.262533] Workqueue: events_unbound commit_work [drm_kms_helper]
[707581.262534] Call Trace:
[707581.262541]  __schedule+0x28b/0x880
[707581.262543]  schedule+0x36/0x80
[707581.262544]  schedule_timeout+0x1f1/0x350
[707581.262631]  ? amdgpu_cgs_read_register+0x14/0x20 [amdgpu]
[707581.262672]  ? dce120_timing_generator_get_crtc_position+0x5d/0xb0 [amdgpu]
[707581.262709]  ? dce120_timing_generator_get_crtc_scanoutpos+0x76/0xd0 [amdgpu]
[707581.262714]  kcl_fence_default_wait+0x1c2/0x250 [amdkcl]
[707581.262715]  ? kcl_fence_default_wait+0x1c2/0x250 [amdkcl]
[707581.262720]  ? dma_fence_free+0x20/0x20
[707581.262723]  dma_fence_wait_timeout+0x38/0xf0
[707581.262724]  reservation_object_wait_timeout_rcu+0x14f/0x2d0
[707581.262763]  amdgpu_dm_do_flip+0x112/0x360 [amdgpu]
[707581.262766]  ? __slab_free+0x14c/0x2d0
[707581.262803]  amdgpu_dm_atomic_commit_tail+0x854/0xa40 [amdgpu]
[707581.262807]  ? pick_next_task_fair+0x48e/0x560
[707581.262809]  ? __switch_to+0xad/0x540
[707581.262817]  commit_tail+0x3f/0x60 [drm_kms_helper]
[707581.262821]  commit_work+0x12/0x20 [drm_kms_helper]
[707581.262825]  process_one_work+0x1e7/0x410
[707581.262827]  worker_thread+0x4b/0x420
[707581.262829]  kthread+0x125/0x140
[707581.262830]  ? process_one_work+0x410/0x410
[707581.262832]  ? kthread_create_on_node+0x70/0x70
[707581.262833]  ? kthread_create_on_node+0x70/0x70
[707581.262836]  ret_from_fork+0x1f/0x30
```