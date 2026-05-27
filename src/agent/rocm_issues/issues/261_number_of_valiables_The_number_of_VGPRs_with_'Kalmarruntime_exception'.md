# number of valiables  "The number of VGPRs " with 'Kalmar::runtime_exception'

> **Issue #261**
> **状态**: closed
> **创建时间**: 2017-11-24T18:25:50Z
> **更新时间**: 2018-06-03T15:12:28Z
> **关闭时间**: 2018-06-03T15:12:28Z
> **作者**: smithakihide
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/261

## 描述

hello. thank you for reading.

I got the below error during executing the kernel having many local variables.
here is my environment .
Ubuntu 16.04.3
RX 580
32GB RAM
Core i5 4670
ROCm version 1.6, HCC version 1.2

```
terminate called after throwing an instance of 'Kalmar::runtime_exception'
  what():  The number of VGPRs (153) needed by this launch (int, int, int, int, SGInfo*, int, int, int, int
, int, int, int, double*, int, int, int, int, int, int, int, int, int, int, int, int, int, double*, int, int, int, int,
int, int, int, int, int, int, int, int, int, double*, int, int, int, int, int, int, int, int, int, int, int, int, int, d
ouble*, int, int, int, int, int, int, int, int, int, int, int, int, int, double, double, double, double, double, double,
 double*, int, int, int, int, int, int, int, int, int, int, int, int, int, double*, int, int, int, int, int, int, int, i
nt, int, int, int, int, int, double, double, double, double*, int, int, int, int, int, int, int, int, int, int, int, int
, int)) exceeds HW limit due to big work group size (672) workitems!
Aborted (core dumped)
```

I can run the same code on Windows + VS2017 + RX480 with no error.

I suppose the cause of this error is because of too many local variables in the kernel as described in the error massage.
but it's strange that this error occurred despite of the same hardware on both Windows and Linux. 
could you give me any information?

p.s. this number of index variables should be needed to run numerical simulations at least.

---

## 评论 (3 条)

### 评论 #1 — smithakihide (2017-11-28T00:23:20Z)

here are the specification of GFX7 (Hawaii i.e. W8100) and GFX8.

this is for GFX7.
[http://developer.amd.com/wordpress/media/2013/07/AMD_Sea_Islands_Instruction_Set_Architecture.pdf](http://developer.amd.com/wordpress/media/2013/07/AMD_Sea_Islands_Instruction_Set_Architecture.pdf)
and this is for GFX8.
[http://amd-dev.wpengine.netdna-cdn.com/wordpress/media/2013/12/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf](http://amd-dev.wpengine.netdna-cdn.com/wordpress/media/2013/12/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf)

these documents say both architecture have more than 256 VGPR units available.
but my code failed when it used 153 VGPR units.  so this behavior is strange.

please help me.

---

### 评论 #2 — acmeman925 (2017-11-30T19:20:39Z)

Hi @smithakihide  Could you please share the test you are trying to run.  I might be missing something but I do not see the test case.

---

### 评论 #3 — szellmann (2018-01-02T10:31:41Z)

I'm having similar problems:

```
terminate called after throwing an instance of 'Kalmar::runtime_exception'
  what():  The number of VGPRs (93) needed by this launch (visionaray::detail::hcc_sched_impl_frame<visionaray::basic_ray<float>, visionaray::pathtracing::kernel<visionaray::kernel_params<visionaray::normals_per_face_binding, visionaray::index_bvh_ref_t<visionaray::basic_triangle<3ul, float, unsigned int> >*, visionaray::vector<3ul, float>*, visionaray::plastic<float>*, visionaray::point_light<float>*, visionaray::vector<4ul, float> > >, visionaray::sched_params<visionaray::sched_params_base<visionaray::rectangle<visionaray::xywh_layout, int> >, visionaray::pinhole_camera, visionaray::gpu_buffer_rt<) exceeds HW limit due to big work group size (625) workitems!
Aborted (core dumped)
```
I'm on a Ryzen 7 1800X system with an RX 580. I have a testcase [here](https://github.com/szellmann/visionaray/tree/hcc-tmp). I can provide instructions on how to reproduce the error if interested.

---
