# Determine to which NUMA node a GPU belongs from an OpenCL device ID

> **Issue #563**
> **状态**: closed
> **创建时间**: 2018-09-27T20:32:40Z
> **更新时间**: 2018-10-08T19:07:53Z
> **关闭时间**: 2018-10-08T19:07:53Z
> **作者**: Moading
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/563

## 标签

- **Question** (颜色: #cc317c)

## 描述

Hi everybody,

first of all, this a feature request, not a bug report.
Dual socket mainboards contain two or more NUMA nodes. There are systems out there that allow connecting multiple GPUs to each GPU, for example via a PCIe witch. See this machine for example: 
[https://www.supermicro.com/products/system/4U/4028/SYS-4028GR-TR.cfm](url)

When a system with two or more NUMA nodes is used, it is important to bind processes to NUMA nodes and to allocate memory locally, i.e. on the NUMA node that the process was bound to. Otherwise, the performance will decrease due to remote memory access. I have not tested this but I am 100% sure, that the same logic applies to programs using GPUs as well. For example, let's consider a system with 2 NUMA nodes where each node contains a single GPU. If a program runs on NUMA node 0 and uses the GPU that is connected to NUMA node 1, the performance will be less compared to a program running on NUMA node 0 and uses the GPU that is connected to NUMA node 0. When I say performance, I mean host<->device memory transfers in OpenCL.

So here is my question or feature request: When I used clGetDeviceID to get the device IDs for the GPUs, how can I tell to which NUMA node the GPU belongs? Is it possible to extract the PCIe bus ID from the device ID? Are the device IDs returned by clGetDeviceID ordered in some way?

After a short google search it seems that others had similar question years ago but I found no satisfying answer.

This is not super urgent but it is relevant in a HPC context.

Greetings!

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-09-28T20:24:19Z)

Hi @Moading 

This is a good request, and your reasoning is sound. It's so good, in fact, that we anticipated it and hopefully can meet your needs right now. :)

Here is one of my test systems, a two-socket Xeon with six Vega 10 GPUs in it.
```
$ rocminfo | grep "^  Name:"
  Name:                    Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz
  Name:                    Intel(R) Xeon(R) CPU E5-2690 v3 @ 2.60GHz
  Name:                    gfx900
  Name:                    gfx900
  Name:                    gfx900
  Name:                    gfx900
  Name:                    gfx900
  Name:                    gfx900
```

Here is the CPU NUMA layout.
```
$ numactl -H
available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 24 25 26 27 28 29 30 31 32 33 34 35
node 0 size: 128823 MB
node 0 free: 57611 MB
node 1 cpus: 12 13 14 15 16 17 18 19 20 21 22 23 36 37 38 39 40 41 42 43 44 45 46 47
node 1 size: 129018 MB
node 1 free: 67345 MB
node distances:
node   0   1
  0:  10  21
  1:  21  10
```

If your developments are focused on OpenCL, you can get the location of each of these GPUs within the PCIe topology by using the OpenCL extension [cl_amd_device_attribute_query](https://www.khronos.org/registry/OpenCL/extensions/amd/cl_amd_device_attribute_query.txt). The [ROCm OpenCL runtime uses this](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-1.9.x/tools/clinfo/clinfo.cpp#L257) in the `clinfo` application to get PCIe bus and device information about each GPU is displays. 

```
$ /opt/rocm/opencl/bin/x86_64/clinfo | grep "Device Topology"
  Device Topology:                               PCI[ B#6, D#0, F#0 ]
  Device Topology:                               PCI[ B#9, D#0, F#0 ]
  Device Topology:                               PCI[ B#14, D#0, F#0 ]
  Device Topology:                               PCI[ B#17, D#0, F#0 ]
  Device Topology:                               PCI[ B#134, D#0, F#0 ]
  Device Topology:                               PCI[ B#137, D#0, F#0 ]
```

[This blog post](https://anteru.net/blog/2014/08/01/2483/index.html) contains some information about doing this. In addition, this is how [hwloc assigns GPUs to "local" CPUs](https://www.open-mpi.org/projects/hwloc/doc/v1.11.0/a00071_source.php).

Our ROCr runtime (which sits below all of our programming languages) offers an even more direct method to gather what you want, however. We [directly deliver the NUMA distance between HSA device nodes](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-1.9.x/src/inc/hsa_ext_amd.h#L977).

An example of how to use this function can be found in `rocm_bandwith_test` [in the topology testing functions](https://github.com/RadeonOpenCompute/rocm_bandwidth_test/blob/master/rocm_bandwidth_test_topology.cpp#L273).

Here is the output that looks a lot like an advanced `numactl -H`:
```
$ ./rocm_bandwidth_test -t

          Device Index:                             0
            Device Type:                            CPU
              Allocatable Memory Size (KB):         131915160

          Device Index:                             1
            Device Type:                            CPU
              Allocatable Memory Size (KB):         132115024

          Device Index:                             2
            Device Type:                            GPU
              Allocatable Memory Size (KB):         16760832

          Device Index:                             3
            Device Type:                            GPU
              Allocatable Memory Size (KB):         16760832

          Device Index:                             4
            Device Type:                            GPU
              Allocatable Memory Size (KB):         16760832

          Device Index:                             5
            Device Type:                            GPU
              Allocatable Memory Size (KB):         16760832

          Device Index:                             6
            Device Type:                            GPU
              Allocatable Memory Size (KB):         16760832

          Device Index:                             7
            Device Type:                            GPU
              Allocatable Memory Size (KB):         16760832


          Device Access

          D/D       0         1         2         3         4         5         6         7

          0         1         1         1         1         1         1         1         1

          1         1         1         1         1         1         1         1         1

          2         1         1         1         1         1         1         0         0

          3         1         1         1         1         1         1         0         0

          4         1         1         1         1         1         1         0         0

          5         1         1         1         1         1         1         0         0

          6         1         1         0         0         0         0         1         1

          7         1         1         0         0         0         0         1         1


          Device Numa Distance

          D/D       0         1         2         3         4         5         6         7

          0         0         21        20        20        20        20        41        41

          1         21        0         41        41        41        41        20        20

          2         20        41        0         40        40        40        N/A       N/A

          3         20        41        40        0         40        40        N/A       N/A

          4         20        41        40        40        0         40        N/A       N/A

          5         20        41        40        40        40        0         N/A       N/A

          6         41        20        N/A       N/A       N/A       N/A       0         40

          7         41        20        N/A       N/A       N/A       N/A       40        0
```

You'll node some of the info this can give you that you can't get with just the bus information in OpenCL. For instance: there are some N/A entries in the NUMA distance between the first four GPUs (devices 2-5) and the last two GPUs (devices 6-7). This is because they're on different CPU NUMA nodes, and we can only do direct GPU->GPU transfers within a single socket on this Intel platform. (This is not a general constraint, it's only a constraint on this particular host platform). However, if you look across rows 0 and 1, you'll see the NUMA distance from each CPU to each GPU. :) 

---

### 评论 #2 — Moading (2018-09-30T19:20:01Z)

Dear @jlgreathouse,

thank you for this post, it is very helpful and answers my question to perfection. Looking at the source of hwloc_opencl_get_device_cpuset, I realized that the folder /sys/bus/pci/devices/0000:bus:device:funtion contains another file called "numa_node". On my single NUMA node system that file contains "0" when looking in the directories corresponding to the GPUs.

This is what I was looking for. I can simply use that value to identify the GPUs that should be used by a OpenCL programm pinned to a certain NUMA node.

For verification, could you please check on your dual NUMA node system if the file "numa_node" for GPU 6 conatins the value 1? The folder should be  /sys/bus/pci/devices/0000:89:0.0

Thanks!


---

### 评论 #3 — jlgreathouse (2018-10-08T19:07:53Z)

Sorry for the delay. I was out of the office for the last week.

Yes, the `numa_node` for GPUs 5 and 6 are both `1`. The `numa_node` for GPUs 1, 2, 3, and 4 are all `0`.

Hopefully these multiple ways of gathering GPU NUMA information should meet your needs. :)

---
