# hipconfig seems missing some package dependency

> **Issue #1518**
> **状态**: closed
> **创建时间**: 2021-07-12T02:44:59Z
> **更新时间**: 2021-07-12T08:54:21Z
> **关闭时间**: 2021-07-12T08:54:20Z
> **作者**: terU3760
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1518

## 描述

When manually installed HIP according to here: [HIP-Installation](https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP-Installation.html). And run the following command:

`/opt/hip/bin/hipconfig --full`

shows:

```
HIP version  : 4.2.21155-37cb3a34

== hipconfig
HIP_PATH     : /opt/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I"/opt/hip/include" -I"/opt/rocm/llvm/bin/../lib/clang/12.0.0" -I/opt/rocm/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
clang version 12.0.0 (https://github.com/RadeonOpenCompute/llvm-project.git b204d7f0cae65b6cd4446eec50fc1fb675d582af)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 12.0.0git
  Optimized build with assertions.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver1

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/hip/bin/hipcc line 592.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/hip/bin/hipcc line 593.
Use of uninitialized value $targetsStr in split at /opt/hip/bin/hipcc line 599.
 -std=c++11 -isystem "/opt/rocm/llvm/lib/clang/12.0.0/include/.." -isystem /opt/rocm/hsa/include -isystem "/opt/hip/include" -O3
hip-clang-ldflags  : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/hip/bin/hipcc line 592.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/hip/bin/hipcc line 593.
Use of uninitialized value $targetsStr in split at /opt/hip/bin/hipcc line 599.
--driver-mode=g++ -L"/opt/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/home/yimin/anaconda3/bin:/home/yimin/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

== Linux Kernel
Hostname     : yimin-System-Product-LatexWorkstation
Linux yimin-System-Product-LatexWorkstation 5.4.0-050400-lowlatency #201911242031 SMP PREEMPT Mon Nov 25 01:44:43 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.5 LTS
Release:	18.04
Codename:	bionic

```

it says: Can't exec "/opt/rocm/bin/rocm_agent_enumerator" ...... , how to fix it?


---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-07-12T05:20:43Z)

Thanks @terU3760 for reaching out.
I will definitely help you, let me take a look.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-07-12T05:23:29Z)

Hi @terU3760 
Looking at the error message, found that HIP installation did not go well.
/opt/hip/bin/hipcc is a wrong path from the error message you pasted. 
**Make sure that once HIP installed successfully under /opt/rocm/hip**

hip-clang-cxxflags : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at **/opt/hip/bin/hipcc** line 592.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/hip/bin/hipcc line 593.
Use of uninitialized value $targetsStr in split at /opt/hip/bin/hipcc line 599.
 -std=c++11 -isystem "/opt/rocm/llvm/lib/clang/12.0.0/include/.." -isystem /opt/rocm/hsa/include -isystem "/opt/hip/include" -O3
hip-clang-ldflags  : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/hip/bin/hipcc line 592.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/hip/bin/hipcc line 593.
Use of uninitialized value $targetsStr in split at /opt/hip/bin/hipcc line 599.
--driver-mode=g++ -L"/opt/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt


Request you to check the same: [https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP-Installation.html#default-paths-and-environment-variables](url)

Hope this helps.
Thank you.

---

### 评论 #3 — terU3760 (2021-07-12T06:26:33Z)

Hi, @ROCmSupport 
Fatually I looked at the code of /opt/hip/bin/hipcc .
It is:

```
......

if($HIP_PLATFORM eq "amd"){
    # No AMDGPU target specified at commandline. So look for HCC_AMDGPU_TARGET
    if($default_amdgpu_target eq 1) {
        if (defined $ENV{HCC_AMDGPU_TARGET}) {
            $targetsStr = $ENV{HCC_AMDGPU_TARGET};
        } elsif (not $isWindows) {
            # Else try using rocm_agent_enumerator
            $ROCM_AGENT_ENUM = "${ROCM_PATH}/bin/rocm_agent_enumerator";
            $targetsStr = `${ROCM_AGENT_ENUM} -t GPU`;                         <------------------ line 592
            $targetsStr =~ s/\n/,/g;
        }
        $default_amdgpu_target = 0;
    }

......
```

But I found factually rocm_agent_enumerator was installed under:
`/usr/bin/rocm_agent_enumerator`
Which I installed ROCclr via runnning:
`sudo make install`
What should I do to make it run correctly?
But it seems /usr/bin/rocm_agent_enumerator is an empty file. I did installed rocm, when I run the command:
`sudo apt install rocm-dkms`
I got the following output:
```
Reading package lists... Done
Building dependency tree       
Reading state information... Done
rocm-dkms is already the newest version (4.2.0.40200-21).
The following packages were automatically installed and are no longer required:
  cmake-data librhash0 libsubunit-perl libuv1 python-cairo python-extras
  python-fixtures python-gobject-2 python-gtk2 python-junitxml
  python-linecache2 python-mimeparse python-pbr python-pkg-resources
  python-six python-subunit python-testtools python-traceback2
  python-unittest2 python3-extras python3-fixtures python3-linecache2
  python3-mimeparse python3-pbr python3-subunit python3-testtools
  python3-traceback2 python3-unittest2
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 10 not upgraded.

```
What should I do?

---

### 评论 #4 — ROCmSupport (2021-07-12T08:54:20Z)

Hi @terU3760 
Looks like everything got messed up.
To try/install/build anything, you need to have rocm installed on your machine first.
So I request you to do the below things.

1. clean your machine from rocm and all other things
sudo apt autoremove rocm-dkms and check if everything is removed. Check this by "sudo dpkg -l | grep rocm".
Next replace rocm to rock, hsa,hip,llvm, comgr and remove one by one if you have any package in the system.
2. Once cleaned, reboot the machine.
3. Now install rocm freshly as per instructions @ [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu](url)
4. Reboot now and check your installation by "/opt/rocm/bin/rocminfo" and "/opt/rocm/opencl/bin/clinfo" commands.
5. /opt/hip/bin/hipconfig --full --> shows data without any errors.

Hope this helps.
Thank you.


---
