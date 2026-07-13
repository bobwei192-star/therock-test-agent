# Does the Rocm now work fine with ubuntu 20.04

- **Issue #:** 1107
- **State:** closed
- **Created:** 2020-05-10T04:45:00Z
- **Updated:** 2021-07-29T06:07:29Z
- **URL:** https://github.com/ROCm/ROCm/issues/1107

The tensorflow-rocm worked fine on 19.10.
When I updated to ubuntu 20.04 and used the tensorflow-rocm then I got this
2020-05-10 12:24:20.926812: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libhip_hcc.so
2020-05-10 12:24:20.982479: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:03:00.0 name: Vega 10 XL/XT [Radeon RX Vega 56/64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.59GHz coreCount: 56 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-05-10 12:24:21.020605: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-10 12:24:21.021757: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-10 12:24:21.024344: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-10 12:24:21.024556: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-10 12:24:21.024624: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-10 12:24:21.024894: I tensorflow/core/platform/cpu_feature_guard.cc:143] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE3 SSE4.1 SSE4.2 AVX
2020-05-10 12:24:21.031167: I tensorflow/core/platform/profile_utils/cpu_utils.cc:102] CPU Frequency: 3411120000 Hz
2020-05-10 12:24:21.031533: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x86a0570 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-10 12:24:21.031555: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-05-10 12:24:21.032908: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x8708d60 initialized for platform ROCM (this does not guarantee that XLA will be used). Devices:
2020-05-10 12:24:21.032932: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Vega 10 XL/XT [Radeon RX Vega 56/64], AMDGPU ISA version: gfx900
2020-05-10 12:24:21.033075: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1579] Found device 0 with properties: 
pciBusID: 0000:03:00.0 name: Vega 10 XL/XT [Radeon RX Vega 56/64]     ROCm AMD GPU ISA: gfx900
coreClock: 1.59GHz coreCount: 56 deviceMemorySize: 7.98GiB deviceMemoryBandwidth: -1B/s
2020-05-10 12:24:21.033109: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocblas.so
2020-05-10 12:24:21.033125: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libMIOpen.so
2020-05-10 12:24:21.033140: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocfft.so
2020-05-10 12:24:21.033153: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library librocrand.so
2020-05-10 12:24:21.033188: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1703] Adding visible gpu devices: 0
2020-05-10 12:24:21.033206: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1102] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-05-10 12:24:21.033214: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1108]      0 
2020-05-10 12:24:21.033220: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1121] 0:   N 
2020-05-10 12:24:21.033282: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1247] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 7444 MB memory) -> physical GPU (device: 0, name: Vega 10 XL/XT [Radeon RX Vega 56/64], pci bus id: 0000:03:00.0)
2020-05-10 12:24:27.770244: E tensorflow/stream_executor/rocm/rocm_event.cc:28] Error polling for event status: failed to query event: hipError_t(600)
2020-05-10 12:24:27.770282: F tensorflow/core/common_runtime/gpu/gpu_event_mgr.cc:273] Unexpected Event status: 1

Both rocminfo and clinfo work fine now so I have no idea what happened
I tried to reinstall all rocm-dkms and tensorflow-rocm but it didn't work.