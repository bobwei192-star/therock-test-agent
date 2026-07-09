# hipStreamEndCapture SIGSEGVs on second call after a capture is invalidated (gfx1151/WSL2, ROCm 7.13 + 7.2.4)

- **Issue #:** 6372
- **State:** open
- **Created:** 2026-06-22T03:29:05Z
- **Updated:** 2026-06-22T16:53:15Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/6372

## Problem

After a HIP stream capture is invalidated mid-flight (e.g. by an illegal operation such as a synchronous `hipMemcpy` DeviceToHost during capture), `hipStreamEndCapture` correctly returns `hipErrorStreamCaptureInvalidated`, but it leaves the stream's capture status as `hipStreamCaptureStatusInvalidated` (2) instead of clearing it to `hipStreamCaptureStatusNone` (0). A **second** `hipStreamEndCapture` call on that stream then **SIGSEGVs** inside `libamdhip64` instead of returning an error.

This bites any framework whose capture teardown defensively calls `hipStreamEndCapture` to discard a partial/failed capture (guarded by `hipStreamIsCapturing != None`): because the status stays `Invalidated`, the guard passes and the second call crashes the whole process instead of allowing a graceful fall back to eager execution.

## Environment

- ROCm 7.13.0 (technology preview); also reproduces on ROCm 7.2.4
- WSL2 (Ubuntu 24.04), librocdxg 1.2.0, AMD Software: Adrenalin Edition 26.5.2
- GPU: AMD Radeon 8060S / Ryzen AI MAX+ 395 (gfx1151)

## Reproducer

```cpp
#include <hip/hip_runtime.h>
#include <cstdio>
__global__ void addone(float* x){ int i=threadIdx.x; x[i]+=1.0f; }
int main(){
  hipSetDevice(0);
  float* d=nullptr; hipMalloc(&d,256*sizeof(float));
  hipStream_t s; hipStreamCreate(&s);
  hipLaunchKernelGGL(addone,dim3(1),dim3(256),0,s,d); hipStreamSynchronize(s);

  hipStreamBeginCapture(s, hipStreamCaptureModeRelaxed);
  hipLaunchKernelGGL(addone,dim3(1),dim3(256),0,s,d);
  float h[256];
  hipMemcpy(h,d,256*sizeof(float),hipMemcpyDeviceToHost);   // invalidates the capture

  hipStreamCaptureStatus st;
  hipStreamIsCapturing(s,&st); printf("isCapturing(post-invalidate)=%d\n",(int)st); // 2

  hipGraph_t g1=nullptr;
  printf("endCapture#1 -> %s\n", hipGetErrorString(hipStreamEndCapture(s,&g1)));     // Invalidated (ok)

  hipStreamIsCapturing(s,&st); printf("isCapturing(post-end1)=%d\n",(int)st);         // 2  <-- should be 0

  hipGraph_t g2=nullptr;
  printf("endCapture#2 -> %s\n", hipGetErrorString(hipStreamEndCapture(s,&g2)));      // SIGSEGV
  printf("no crash\n");
  return 0;
}
```

Build/run: `hipcc --offload-arch=gfx1151 repro.cpp -o repro && ./repro`

Output:
```
isCapturing(post-invalidate)=2
endCapture#1 -> operation failed due to a previous error during capture
isCapturing(post-end1)=2
Segmentation fault (core dumped)
```

## Expected

Either (a) `hipStreamEndCapture` clears the capture status to `None` once it has terminated an invalidated capture, or (b) a redundant `hipStreamEndCapture` on a stream that is no longer actively capturing returns an error (e.g. `hipErrorIllegalState`) rather than dereferencing freed/null capture state and crashing.

## Notes

A clean single-token graph capture/instantiate/launch works correctly on this stack, so HIP graphs are functional on WSL/gfx1151; this is specifically the teardown path after an invalidated capture.
