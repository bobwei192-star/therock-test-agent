# Error llvm build cmake in rhel and fedora  ERROR: ambiguous python shebang

- **Issue #:** 3135
- **State:** closed
- **Created:** 2024-05-16T08:10:35Z
- **Updated:** 2024-10-04T14:03:20Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/3135

### Problem Description

OS:
NAME="Red Hat Enterprise Linux"
VERSION="9.4 (Plow)"


```
[3922/3922] Generating ../../bin/llvm-readelf
[2/3] Run CPack packaging tool...
CPack: Create package using RPM
CPack: Install projects
CPack: - Install project: LLVM []
CPack: Create package
CPackRPM: Will use GENERATED spec file: /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/SPECS/llvm.spec
CPackRPM:Debug: You may consult rpmbuild logs in: 
CPackRPM:Debug:    - /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/rpmbuildllvm.err
CPackRPM:Debug: *** + umask 022
+ cd /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/BUILD
+ mv /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/tmpBBroot
+ RPM_EC=0
++ jobs -p
+ exit 0
+ umask 022
+ cd /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/BUILD
+ '[' /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux '!=' / ']'
+ rm -rf /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux
++ dirname /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux
+ mkdir -p /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM
+ mkdir /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux
+ '[' -e /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux ']'
+ rm -rf /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux
+ mv /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/tmpBBroot /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/LLVM-17.0.0git-Linux
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-ldconfig
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/redhat/brp-strip-lto /usr/bin/strip
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/redhat/brp-python-bytecompile '' 1 0
+ /usr/lib/rpm/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-mangle-shebangs
*** ERROR: ambiguous python shebang in /opt/rocm-6.0.2/llvm/share/opt-viewer/optrecord.py: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
*** WARNING: ./opt/rocm-6.0.2/llvm/share/opt-viewer/style.css is executable but has no shebang, removing executable bit
*** ERROR: ambiguous python shebang in /opt/rocm-6.0.2/llvm/share/opt-viewer/opt-diff.py: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
*** ERROR: ambiguous python shebang in /opt/rocm-6.0.2/llvm/share/opt-viewer/opt-stats.py: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
*** ERROR: ambiguous python shebang in /opt/rocm-6.0.2/llvm/share/opt-viewer/opt-viewer.py: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
*** WARNING: ./opt/rocm-6.0.2/llvm/share/opt-viewer/optpmap.py is executable but has no shebang, removing executable bit
*** ERROR: ambiguous python shebang in /opt/rocm-6.0.2/llvm/bin/scan-view: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
error: Bad exit status from /var/tmp/rpm-tmp.H8Vx5N (%install)
    Bad exit status from /var/tmp/rpm-tmp.H8Vx5N (%install)
 ***
CPackRPM:Debug:    - /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM/rpmbuildllvm.out
CPackRPM:Debug: *** Building target platforms: x86_64
Building for target x86_64
setting SOURCE_DATE_EPOCH=1278201600
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.PJ22iy
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.H8Vx5N
mangling shebang in /opt/rocm-6.0.2/llvm/libexec/analyze-c++ from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/libexec/c++-analyzer from /usr/bin/env perl to #!/usr/bin/perl
mangling shebang in /opt/rocm-6.0.2/llvm/libexec/intercept-c++ from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/libexec/ccc-analyzer from /usr/bin/env perl to #!/usr/bin/perl
mangling shebang in /opt/rocm-6.0.2/llvm/libexec/analyze-cc from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/libexec/intercept-cc from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/share/clang/clang-format-diff.py from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/bin/hmaptool from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/bin/git-clang-format from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/bin/scan-build-py from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/bin/analyze-build from /usr/bin/env python3 to #!/usr/bin/python3
mangling shebang in /opt/rocm-6.0.2/llvm/bin/scan-build from /usr/bin/env perl to #!/usr/bin/perl
mangling shebang in /opt/rocm-6.0.2/llvm/bin/intercept-build from /usr/bin/env python3 to #!/usr/bin/python3


RPM build errors:
 ***
CMake Error at /root/workspace/ROCmLol/local/cmake-3.29.3-linux-x86_64/share/cmake-3.29/Modules/Internal/CPack/CPackRPM.cmake:1915 (message):
  RPM package was not generated!
  /root/workspace/ROCmLol/build/llvm/_CPack_Packages/Linux/RPM
Call Stack (most recent call first):
  /root/workspace/ROCmLol/local/cmake-3.29.3-linux-x86_64/share/cmake-3.29/Modules/Internal/CPack/CPackRPM.cmake:1986 (cpack_rpm_generate_package)


CPack Error: Error while execution CPackRPM.cmake
CPack Error: Problem compressing the directory
CPack Error: Error when generating package: LLVM
FAILED: CMakeFiles/package.util 
cd /root/workspace/ROCmLol/build/llvm && /root/workspace/ROCmLol/local/cmake-3.29.3-linux-x86_64/bin/cpack --config ./CPackConfig.cmake
ninja: build stopped: subcommand failed.

```

### Operating System

Red Hat Enterprise Linux" VERSION="9.4 (Plow)"

### CPU

model name	: AMD Ryzen 5 5500

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.0.0

### ROCm Component

llvm-project

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_