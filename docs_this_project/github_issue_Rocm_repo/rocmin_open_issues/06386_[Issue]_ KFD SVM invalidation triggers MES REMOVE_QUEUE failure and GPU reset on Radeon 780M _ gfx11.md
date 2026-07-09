# [Issue]: KFD SVM invalidation triggers MES REMOVE_QUEUE failure and GPU reset on Radeon 780M / gfx1103

- **Issue #:** 6386
- **State:** open
- **Created:** 2026-06-26T16:26:26Z
- **Updated:** 2026-06-26T18:48:06Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6386

### Problem Description

I originally hit this during ROCm/PyTorch training on the same Radeon 780M system. The failure looked random from userspace: training would run for a while and then fail asynchronously with HIP 719, often reported later around synchronization, copy, or device-selection code rather than at the real failing operation.

While investigating, I found that the userspace stack traces were secondary. The kernel log consistently pointed to AMDGPU/KFD/MES queue eviction failures followed by GPU reset. I first suspected that the issue was related to CPU page-table or backing-page changes on memory registered for GPU access, especially on the XNACK-disabled APU path. Based on that assumption, I initially explored whether Linux MM should prevent user THP/mapping policy changes from overriding driver requirements for such mappings.

That turned out to be the wrong direction. Linux MM maintainers clarified that this kind of unmap/remap/invalidation behavior is expected and that MMU notifier users must handle it correctly. AMD maintainers also pointed out that MES queue eviction failures indicate a KFD/MES handling problem rather than an MM policy problem.

I then narrowed the investigation back to the AMDGPU/KFD/MES path. The reduced reproducer keeps HIP compute queues active while invalidating an HSA SVM registered CPU mapping. The GPU kernels do not access that SVM mapping; they only use `hipMalloc()` device memory. This makes the reproducer different from a normal illegal GPU access to a protected mapping.

The consistent failure I now see is that KFD enters queue quiesce/eviction for the SVM invalidation, then MES REMOVE_QUEUE does not complete. Successful queue operations normally complete very quickly, but in the failing case the request remains uncompleted until the driver reports MES failure, KFD eviction fails, the GPU resets, and userspace sees HIP 719.

A minimal HIP/HSA program reliably triggers HIP 719:

```text
hipStreamSynchronize: unspecified launch failure (719)
```

The kernel log shows MES queue removal failure, KFD eviction failure, and GPU reset:

```text
MES failed to respond to msg=REMOVE_QUEUE
failed to remove hardware queue from MES, doorbell=0x1004
MES might be in unrecoverable state, issue a GPU reset
Failed to evict queue 2
Failed to evict process queues
GPU reset begin!. Source: 3
```

### Expected Result

Invalidating a registered HSA SVM CPU mapping while unrelated HIP compute queues are active should not reset the GPU or kill the HIP context.

### Technical Observation

The failing path appears to be:

```text
HSA SVM CPU VMA invalidation
-> KFD SVM invalidation handling
-> active queue quiesce/eviction
-> MES REMOVE_QUEUE
-> KFD eviction failure
-> GPU reset
-> HIP 719
```

### Operating System

Ubuntu 26.04 LTS (Resolute Raccoon)

### CPU

AMD Ryzen 7 8845HS w/ Radeon 780M Graphics

### GPU

AMD Radeon 780M Graphics

### ROCm Version

ROCm 7.13.0

### ROCm Component

ROCK-Kernel-Driver

### Steps to Reproduce

Minimal Reproducer

Attached file:

```text
mes_remove_queue_719_repro.cpp
```

Build:

```bash
hipcc -O2 -std=c++17 mes_remove_queue_719_repro.cpp \
  -lhsa-runtime64 -pthread \
  -o mes_remove_queue_719_repro
```

Run:

```bash
./mes_remove_queue_719_repro
```

The reproducer registers an anonymous CPU mapping as HSA SVM, launches two HIP compute streams that only access `hipMalloc()` device memory, and concurrently toggles CPU permissions on the registered SVM range with `mprotect()`.

The GPU kernels do not read or write the SVM range.

### Result

On the distribution kernel/module listed above, this reproduces 5/5 times:

```text
run_1: hipStreamSynchronize: unspecified launch failure (719)
run_2: hipStreamSynchronize: unspecified launch failure (719)
run_3: hipStreamSynchronize: unspecified launch failure (719)
run_4: hipStreamSynchronize: unspecified launch failure (719)
run_5: hipStreamSynchronize: unspecified launch failure (719)
```

Dmesg summary:

```text
GPU reset begin count: 5
Failed to evict process queues count: 5
MES REMOVE_QUEUE failure count: 13
```

### mes_remove_queue_719_repro.cpp
```cpp
#include <hip/hip_runtime.h>
#include <hsa/hsa.h>
#include <hsa/hsa_ext_amd.h>

#include <atomic>
#include <cstdio>
#include <thread>

#include <sys/mman.h>
#include <unistd.h>

#define HIP(call) do { \
	hipError_t e = (call); \
	if (e != hipSuccess) { \
		fprintf(stderr, "%s: %s (%d)\n", #call, hipGetErrorString(e), e); \
		return 1; \
	} \
} while (0)

#define HSA(call) do { \
	hsa_status_t s = (call); \
	if (s != HSA_STATUS_SUCCESS) { \
		fprintf(stderr, "%s: HSA status %d\n", #call, s); \
		return 1; \
	} \
} while (0)

static constexpr size_t SVM_BYTES = 64ull << 20;
static constexpr size_t DEV_BYTES = 64ull << 20;
static constexpr int STREAMS = 2;

/* Keep the GPU queues active long enough for the CPU-side SVM invalidations
 * below to collide with KFD queue eviction.
 */
__global__ void busy_kernel(float *p, size_t n)
{
	size_t tid = blockIdx.x * blockDim.x + threadIdx.x;
	size_t stride = blockDim.x * gridDim.x;

	for (size_t i = tid; i < n; i += stride) {
		float x = p[i];
		for (int r = 0; r < 256; r++)
			x = x * 1.000001f + (float)((r + tid) & 255) * 0.00001f;
		p[i] = x;
	}
}

static hsa_status_t first_gpu(hsa_agent_t agent, void *data)
{
	hsa_device_type_t type;

	if (hsa_agent_get_info(agent, HSA_AGENT_INFO_DEVICE, &type) == HSA_STATUS_SUCCESS &&
	    type == HSA_DEVICE_TYPE_GPU) {
		*static_cast<hsa_agent_t *>(data) = agent;
		return HSA_STATUS_INFO_BREAK;
	}

	return HSA_STATUS_SUCCESS;
}

int main()
{
	hsa_agent_t gpu = {};
	hipStream_t streams[STREAMS];
	float *dev[STREAMS];
	const size_t page = sysconf(_SC_PAGESIZE);
	const size_t dev_elems = DEV_BYTES / sizeof(float);

	/* Basic HIP setup. */
	HIP(hipSetDevice(0));

	/* Create an anonymous CPU VMA that can later be invalidated with
	 * mprotect(). Touching the pages makes the CPU page tables real before
	 * registering the range with HSA SVM.
	 */
	void *svm = mmap(nullptr, SVM_BYTES, PROT_READ | PROT_WRITE,
			 MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
	if (svm == MAP_FAILED) {
		perror("mmap");
		return 1;
	}

	for (size_t off = 0; off < SVM_BYTES; off += page)
		static_cast<char *>(svm)[off] = 1;

	/* Register the CPU VMA as GPU-accessible SVM. This is what makes later
	 * CPU page-table invalidations enter the KFD SVM invalidation path.
	 */
	HSA(hsa_init());
	hsa_status_t s = hsa_iterate_agents(first_gpu, &gpu);
	if (s != HSA_STATUS_SUCCESS && s != HSA_STATUS_INFO_BREAK) {
		fprintf(stderr, "hsa_iterate_agents: HSA status %d\n", s);
		return 1;
	}
	if (!gpu.handle) {
		fprintf(stderr, "no HSA GPU agent found\n");
		return 1;
	}

	hsa_amd_svm_attribute_pair_t attr = {
		HSA_AMD_SVM_ATTRIB_AGENT_ACCESSIBLE,
		gpu.handle,
	};
	HSA(hsa_amd_svm_attributes_set(svm, SVM_BYTES, &attr, 1));

	/* Create two active HIP compute streams. The kernels below deliberately
	 * use only device memory, not the SVM range, so a HIP 719/MES reset is not
	 * caused by an illegal GPU access to the mprotect()ed CPU mapping.
	 */
	for (int i = 0; i < STREAMS; i++) {
		HIP(hipMalloc(&dev[i], DEV_BYTES));
		HIP(hipMemset(dev[i], 0, DEV_BYTES));
		HIP(hipStreamCreate(&streams[i]));
	}

	/* Core trigger: repeatedly invalidate the registered SVM VMA while the
	 * GPU queues are active. On affected gfx1103/XNACK-disabled systems this
	 * can drive KFD through SVM eviction and MES REMOVE_QUEUE failure.
	 */
	std::atomic<bool> stop{false};
	std::thread invalidator([&] {
		while (!stop.load(std::memory_order_relaxed)) {
			mprotect(svm, SVM_BYTES, PROT_READ);
			usleep(2000);
			mprotect(svm, SVM_BYTES, PROT_READ | PROT_WRITE);
			usleep(5000);
		}
	});

	for (int i = 0; i < STREAMS; i++)
		busy_kernel<<<512, 256, 0, streams[i]>>>(dev[i], dev_elems);
	HIP(hipGetLastError());

	usleep(1000);

	/* Expected failure on affected systems: hipErrorLaunchFailure (719), with
	 * dmesg showing MES REMOVE_QUEUE timeout/failure and a GPU reset.
	 */
	hipError_t err = hipSuccess;
	for (int i = 0; i < STREAMS; i++) {
		err = hipStreamSynchronize(streams[i]);
		if (err != hipSuccess)
			break;
	}

	stop.store(true, std::memory_order_relaxed);
	invalidator.join();

	printf("hipStreamSynchronize: %s (%d)\n", hipGetErrorString(err), err);
	return err == hipSuccess ? 0 : 2;
}
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```text
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.21
Runtime Ext Version:     1.21
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  ENABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   5102
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            16
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    47580332(0x2d604ac) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    47580332(0x2d604ac) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    47580332(0x2d604ac) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    47580332(0x2d604ac) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1103
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon 780M Graphics
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      2048(0x800) KB
  Chip ID:                 6400(0x1900)
  ASIC Revision:           12(0xc)
  Cacheline Size:          128(0x80)
  Max Clock Freq. (MHz):   2700
  BDFID:                   50688
  Internal Node ID:        1
  Compute Unit:            12
  SIMDs per CU:            2
  Shader Engines:          1
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:       APU
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        65535(0xffff)
    z                        65535(0xffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 68
  SDMA engine uCode::      24
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    33554432(0x2000000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    33554432(0x2000000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1103
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        2147483647(0x7fffffff)
        y                        65535(0xffff)
        z                        65535(0xffff)
      FBarrier Max Size:       32
    ISA 2
      Name:                    amdgcn-amd-amdhsa--gfx11-generic
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        2147483647(0x7fffffff)
        y                        65535(0xffff)
        z                        65535(0xffff)
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    aie2
  Uuid:                    AIE-XX
  Marketing Name:          RyzenAI-npu1
  Vendor Name:             AMD
  Feature:                 AGENT_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        1(0x1)
  Queue Min Size:          64(0x40)
  Queue Max Size:          64(0x40)
  Queue Type:              SINGLE
  Node:                    0
  Device Type:             DSP
  Cache Info:
    L2:                      2048(0x800) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          0(0x0)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            0
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:0
  Memory Properties:
  Features:                AGENT_DISPATCH
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: KERNARG, COARSE GRAINED
      Size:                    47580332(0x2d604ac) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    65536(0x10000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    47580332(0x2d604ac) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*** Done ***
```

### Additional Information

_No response_