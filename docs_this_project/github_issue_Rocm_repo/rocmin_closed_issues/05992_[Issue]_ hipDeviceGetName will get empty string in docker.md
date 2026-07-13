# [Issue]: hipDeviceGetName will get empty string in docker

- **Issue #:** 5992
- **State:** closed
- **Created:** 2026-02-24T06:36:07Z
- **Updated:** 2026-02-26T19:51:46Z
- **Labels:** status: triage
- **Assignees:** amd-nicknick
- **URL:** https://github.com/ROCm/ROCm/issues/5992

### Problem Description

```
#include <hip/hip_runtime.h>
#include <iostream>
#include <string>

int main() {
    // 1. Get the number of available AMD devices
    int deviceCount = 0;
    hipError_t err = hipGetDeviceCount(&deviceCount);
    
    if (err != hipSuccess || deviceCount == 0) {
        std::cerr << "Error: No AMD devices detected, error code: " << hipGetErrorString(err) << std::endl;
        return 1;
    }

    std::cout << "Detected " << deviceCount << " AMD device(s):" << std::endl;

    // 2. Iterate through all devices to get device names
    for (int i = 0; i < deviceCount; ++i) {
        // Set the current device to query
        hipSetDevice(i);

        // Buffer to store device name (HIP specifies max length of device name is 256)
        char deviceName[256];
        err = hipDeviceGetName(deviceName, sizeof(deviceName), i);

        if (err == hipSuccess) {
            std::cout << "Device " << i << " name: " << deviceName << std::endl;
            
            // Filter for MI300X devices
            std::string nameStr = deviceName;
            if (nameStr.find("MI300X") != std::string::npos) {
                std::cout << "  ✅ Found AMD Instinct MI300X device!" << std::endl;
            }
        } else {
            std::cerr << "Failed to query Device " << i << ": " << hipGetErrorString(err) << std::endl;
        }
    }

    return 0;
}
```
compile with `hipcc -o get_amd_device_name get_amd_device_name.cu`

start a docker with command:
```
docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --net=host --shm-size 128G  --name roywang-sglang docker.io/lmsysorg/sglang:v0.5.8-rocm700-mi35x
```

out the docker container:
```
Detected 8 AMD device(s):
Device 0 name: AMD Instinct MI350X
Device 1 name: AMD Instinct MI350X
Device 2 name: AMD Instinct MI350X
Device 3 name: AMD Instinct MI350X
Device 4 name: AMD Instinct MI350X
Device 5 name: AMD Instinct MI350X
Device 6 name: AMD Instinct MI350X
Device 7 name: AMD Instinct MI350X
```

inside the docker container
```
Detected 8 AMD device(s):
Device 0 name: 
Device 1 name: 
Device 2 name: 
Device 3 name: 
Device 4 name: 
Device 5 name: 
Device 6 name: 
Device 7 name: 
```

### Operating System

NAME="Ubuntu" VERSION="22.04.4 LTS (Jammy Jellyfish)"

### CPU

model name      : AMD EPYC 9655 96-Core Processor

### GPU

  Name:                    gfx950                                Marketing Name:          AMD Instinct MI350X                       Name:                    amdgcn-amd-amdhsa--gfx950:sramecc+:xnack-       Name:                    amdgcn-amd-amdhsa--gfx9-4-generic:sramecc+:xnack-

### ROCm Version

7.0.2

### ROCm Component

_No response_

### Steps to Reproduce

```
#include <hip/hip_runtime.h>
#include <iostream>
#include <string>

int main() {
    // 1. Get the number of available AMD devices
    int deviceCount = 0;
    hipError_t err = hipGetDeviceCount(&deviceCount);
    
    if (err != hipSuccess || deviceCount == 0) {
        std::cerr << "Error: No AMD devices detected, error code: " << hipGetErrorString(err) << std::endl;
        return 1;
    }

    std::cout << "Detected " << deviceCount << " AMD device(s):" << std::endl;

    // 2. Iterate through all devices to get device names
    for (int i = 0; i < deviceCount; ++i) {
        // Set the current device to query
        hipSetDevice(i);

        // Buffer to store device name (HIP specifies max length of device name is 256)
        char deviceName[256];
        err = hipDeviceGetName(deviceName, sizeof(deviceName), i);

        if (err == hipSuccess) {
            std::cout << "Device " << i << " name: " << deviceName << std::endl;
            
            // Filter for MI300X devices
            std::string nameStr = deviceName;
            if (nameStr.find("MI300X") != std::string::npos) {
                std::cout << "  ✅ Found AMD Instinct MI300X device!" << std::endl;
            }
        } else {
            std::cerr << "Failed to query Device " << i << ": " << hipGetErrorString(err) << std::endl;
        }
    }

    return 0;
}
```
compile with `hipcc -o get_amd_device_name get_amd_device_name.cu`

start a docker with command:
```
docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --net=host --shm-size 128G  --name roywang-sglang docker.io/lmsysorg/sglang:v0.5.8-rocm700-mi35x
```

out the docker container:
```
Detected 8 AMD device(s):
Device 0 name: AMD Instinct MI350X
Device 1 name: AMD Instinct MI350X
Device 2 name: AMD Instinct MI350X
Device 3 name: AMD Instinct MI350X
Device 4 name: AMD Instinct MI350X
Device 5 name: AMD Instinct MI350X
Device 6 name: AMD Instinct MI350X
Device 7 name: AMD Instinct MI350X
```

inside the docker container
```
Detected 8 AMD device(s):
Device 0 name: 
Device 1 name: 
Device 2 name: 
Device 3 name: 
Device 4 name: 
Device 5 name: 
Device 6 name: 
Device 7 name: 
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_