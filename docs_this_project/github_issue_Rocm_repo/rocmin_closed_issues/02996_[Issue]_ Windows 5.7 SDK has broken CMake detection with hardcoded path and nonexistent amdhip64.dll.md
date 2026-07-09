# [Issue]: Windows 5.7 SDK has broken CMake detection with hardcoded path and nonexistent amdhip64.dll

- **Issue #:** 2996
- **State:** closed
- **Created:** 2024-04-04T12:32:27Z
- **Updated:** 2024-08-21T14:35:11Z
- **Labels:** Under Investigation, AMD Radeon VII, ROCm 5.7.0
- **URL:** https://github.com/ROCm/ROCm/issues/2996

### Problem Description

The HIP 5.7 SDK for Windows cannot be used with CMake because it hardcodes some HIP import prefix as `C:/constructicon/builds/gfx/two/23.30/drivers/compute/install/native/Release/x64/hip` and tries to find a non-existent `amdhip64.dll` file in the SDK.

### Operating System

Windows 11, will update exact version later, on linux right now

### CPU

AMD Ryzen 7 5800H with Radeon Graphics

### GPU

AMD Radeon VII

### ROCm Version

ROCm 5.7.0

### ROCm Component

_No response_

### Steps to Reproduce

  Install the ROCm 5.7 SDK for Windows with default settings: https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html. This example uses the "Windows 10 & 11" version, but the "Windows Server" version has the same problem. All commands are run in Powershell.
  
  1. Write a simple CMake file. This examples uses the native CMake support, but using the legacy `target_link_libraries(MyLib PRIVATE hip::device)` gives the same result.
  ```cmake
  cmake_minimum_required(VERSION 3.21) # HIP language support requires 3.21
  cmake_policy(VERSION 3.21.3...3.27)
  project(MyProj LANGUAGES HIP)
  add_executable(vectoradd_hip vectoradd_hip.cpp)
  set_source_files_properties(vectoradd_hip.cpp PROPERTIES LANGUAGE HIP)
  ```
  2. Create a file at `vectoradd_hip.cpp`. I just used https://github.com/ROCm/HIP-Examples/blob/master/vectorAdd/vectoradd_hip.cpp.
  3. Run `cmake -GNinja -B build -S . -DCMAKE_PREFIX_PATH="C:/Program Files/AMD/ROCm/5.7`. If CMake claims that it can't find a valid HIP compiler, run `$env:Path = "C:\Program Files\AMD\ROCm\5.7;$env:Path"` prior to executing CMake.
  4. Now you should see an error message, claiming that the file `C:/constructicon/builds/gfx/two/23.30/drivers/compute/install/native/Release/x64/hip/lib/amdhip64.lib` is not found. This shouldn't happen.

<details>
<summary> error message </summary>

```
CMake Error at C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-targets.cmake:82 (message):
  The imported target "hip-lang::amdhip64" references the file

     "C:/constructicon/builds/gfx/two/23.30/drivers/compute/install/native/Release/x64/hip/lib/amdhip64.lib"

  but this file does not exist.  Possible reasons include:

  * The file was deleted, renamed, or moved to another location.

  * An install or uninstall procedure did not complete successfully.

  * The installation package was faulty and contained

     "C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-targets.cmake"

  but not all the files it references.

Call Stack (most recent call first):
  C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-config.cmake:87 (include)
  C:/Program Files/CMake/share/cmake-3.29/Modules/CMakeHIPInformation.cmake:159 (find_package)
  CMakeLists.txt:3 (project)


CMake Debug Log at C:/Program Files/CMake/share/cmake-3.29/Modules/CMakeHIPInformation.cmake:159 (find_package):
    C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-langConfig.cmake
    C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-config.cmake

Call Stack (most recent call first):
  CMakeLists.txt:3 (project)


-- Configuring incomplete, errors occurred!
```

</details>  


  5. Now, (might need admin privileges), go edit `C:\Program Files\AMD\ROCm\5.7\lib\cmake\hip-lang\hip-lang-targets.cmake`. You'll see that line 45 has `set(_IMPORT_PREFIX "C:/constructicon/builds/gfx/two/23.30/drivers/compute/install/native/Release/x64/hip")`. Replace that with `set(_IMPORT_PREFIX "C:/Program Files/AMD/ROCm/5.7")`, and run the CMake command in step 3 again.
  6. Now you should get a different error, claiming that CMake fails to find `amdhip64.dll`, but that file is not present anywhere in `C:/Program Files/AMD/ROCm/5.7`:
  <details>
  
  <summary> error message </summary>
  
  ```
  CMake Error at C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-targets.cmake:83 (message):
    The imported target "hip-lang::amdhip64" references the file
  
       "C:/Program Files/AMD/ROCm/5.7/bin/amdhip64.dll"
  
    but this file does not exist.  Possible reasons include:
  
    * The file was deleted, renamed, or moved to another location.
  
    * An install or uninstall procedure did not complete successfully.
  
    * The installation package was faulty and contained
  
       "C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-targets.cmake"
  
    but not all the files it references.
  
  Call Stack (most recent call first):
    C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-config.cmake:87 (include)
    C:/Program Files/CMake/share/cmake-3.29/Modules/CMakeHIPInformation.cmake:159 (find_package)
    CMakeLists.txt:3 (project)
  
  
  CMake Debug Log at C:/Program Files/CMake/share/cmake-3.29/Modules/CMakeHIPInformation.cmake:159 (find_package):
      C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-langConfig.cmake
      C:/Program Files/AMD/ROCm/5.7/lib/cmake/hip-lang/hip-lang-config.cmake
  
  Call Stack (most recent call first):
    CMakeLists.txt:3 (project)
  
  
  -- Configuring incomplete, errors occurred!
  ```
  
  </details>


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_