# ROCclr cmake failed 4.1.0

> **Issue #1437**
> **状态**: closed
> **创建时间**: 2021-04-02T02:44:39Z
> **更新时间**: 2021-05-07T12:10:03Z
> **关闭时间**: 2021-05-07T12:10:03Z
> **作者**: SomnusMistletoe
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1437

## 描述

I have built rocm-dkms，HIP-Clang and ROCm device library successfully, howerver, when I build ROCclr as follows：

git clone https://github.com/ROCm-Developer-Tools/ROCclr.git
git clone -b master-next https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime.git
export ROCclr_DIR="$(readlink -f ROCclr)"
export OPENCL_DIR="$(readlink -f ROCm-OpenCL-Runtime)"
cd "$ROCclr_DIR"
mkdir -p build; cd build
cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..
make -j$(nproc)

When I cmake rocclr, I encountered the following error：

# cmake -DOPENCL_DIR="$OPENCL_DIR" -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocclr ..

-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:46 (find_package):
  Could not find a package configuration file provided by "amd_comgr" with
  any of the following names:

    amd_comgrConfig.cmake
    amd_comgr-config.cmake

  Add the installation prefix of "amd_comgr" to CMAKE_PREFIX_PATH or set
  "amd_comgr_DIR" to a directory containing one of the above files.  If
  "amd_comgr" provides a separate development package or SDK, be sure it has
  been installed.


-- Configuring incomplete, errors occurred!
See also "/usr/local/ROCclr/build/CMakeFiles/CMakeOutput.log".

May I ask why？Thank you.


---

## 评论 (9 条)

### 评论 #1 — xuhuisheng (2021-04-02T02:58:42Z)

Need install https://github.com/RadeonOpenCompute/ROCm-CompilerSupport

---

### 评论 #2 — SomnusMistletoe (2021-04-02T05:25:37Z)

I have git clone ROCm-CompilerSupport, and try to build it in lib/comgr, I have cmake successfully, when I make, it prompt:

```
Scanning dependencies of target opencl2.0-c.pch_target
Scanning dependencies of target opencl1.2-c.pch_target
Scanning dependencies of target shared23-v2
Scanning dependencies of target source4-v3
Scanning dependencies of target shared14-v2
Scanning dependencies of target bc2h
Scanning dependencies of target shared12-v2
Scanning dependencies of target reloc-asm
Scanning dependencies of target source3-v3
Scanning dependencies of target source1-v3
Scanning dependencies of target source4-v2
Scanning dependencies of target source2-v3
[  0%] Generating opencl1.2-c.pch
[  1%] Generating source4-v2.o
[  2%] Generating source3-v2.o
[  2%] Generating opencl2.0-c.pch
[  3%] Generating source4-v3.o
[  3%] Generating source3-v3.o
[  3%] Building C object CMakeFiles/bc2h.dir/bc2h.c.o
[  3%] Generating source1-v3.o
[  3%] Generating reloc-asm.o
[  4%] Generating source2-v2.o
[  6%] Generating source2-v3.o
[  6%] Generating source4-v2.o
[  6%] Built target source1-v3
[  6%] Built target source4-v3
[  6%] Generating source2-v2.o
[  7%] Generating source1-v2.o
[  7%] Built target reloc-asm
[  7%] Built target source4-v2
[  8%] Built target source3-v3
[  8%] Generating source1-v2.o
Scanning dependencies of target reloc2
Scanning dependencies of target source3-v2
Scanning dependencies of target source2-v2
Scanning dependencies of target shared23-v3
[  8%] Built target source2-v3
Scanning dependencies of target reloc1
[  9%] Built target source3-v2
[ 10%] Generating reloc2.o
[ 11%] Generating shared23-v3.so
[ 12%] Built target source2-v2
[ 13%] Generating reloc1.o
Scanning dependencies of target shared
Scanning dependencies of target source1-v2
Scanning dependencies of target shared-v3
[ 13%] Generating shared.so
[ 14%] Generating shared-v3.so
[ 15%] Built target source1-v2
[ 16%] Generating shared23-v2.so
Scanning dependencies of target shared12-v3
[ 16%] Generating shared12-v2.so
[ 17%] Generating shared14-v2.so
[ 17%] Generating shared12-v3.so
[ 18%] Linking C executable bc2h
[ 18%] Built target reloc2
[ 19%] Built target shared23-v3
[ 19%] Built target reloc1
Scanning dependencies of target shared14-v3
[ 20%] Generating shared14-v3.so
[ 20%] Built target shared23-v2
[ 20%] Built target shared14-v2
[ 20%] Built target shared12-v2
[ 22%] Built target shared12-v3
[ 22%] Built target bc2h
[ 22%] Built target shared
Scanning dependencies of target oclc_daz_opt_on_header
Scanning dependencies of target oclc_isa_version_805_header
Scanning dependencies of target oclc_isa_version_701_header
Scanning dependencies of target oclc_isa_version_1033_header
Scanning dependencies of target oclc_isa_version_705_header
Scanning dependencies of target hip_header
Scanning dependencies of target oclc_isa_version_908_header
Scanning dependencies of target oclc_isa_version_801_header
[ 22%] Built target shared-v3
[ 23%] Built target shared14-v3
Scanning dependencies of target oclc_isa_version_700_header
Scanning dependencies of target oclc_isa_version_802_header
[ 24%] Generating oclc_daz_opt_on.inc
[ 25%] Generating oclc_isa_version_1033.inc
[ 25%] Generating oclc_isa_version_700.inc
[ 25%] Generating oclc_isa_version_802.inc
[ 26%] Generating oclc_isa_version_801.inc
[ 27%] Generating oclc_isa_version_701.inc
[ 28%] Generating hip.inc
[ 29%] Generating oclc_isa_version_705.inc
[ 30%] Generating oclc_isa_version_908.inc
[ 31%] Generating oclc_isa_version_805.inc
[ 31%] Built target oclc_isa_version_1033_header
[ 31%] Built target oclc_isa_version_801_header
[ 31%] Built target oclc_isa_version_701_header
[ 31%] Built target oclc_isa_version_705_header
[ 31%] Built target oclc_isa_version_700_header
Scanning dependencies of target oclc_isa_version_600_header
Scanning dependencies of target oclc_isa_version_803_header
Scanning dependencies of target oclc_isa_version_1032_header
Scanning dependencies of target oclc_isa_version_601_header
Scanning dependencies of target oclc_isa_version_1031_header
[ 31%] Generating oclc_isa_version_600.inc
[ 31%] Built target oclc_isa_version_802_header
[ 31%] Built target oclc_daz_opt_on_header
[ 32%] Generating oclc_isa_version_1032.inc
[ 33%] Generating oclc_isa_version_803.inc
[ 34%] Generating oclc_isa_version_601.inc
[ 34%] Built target oclc_isa_version_805_header
[ 35%] Generating oclc_isa_version_1031.inc
[ 35%] Built target hip_header
[ 35%] Built target oclc_isa_version_908_header
[ 35%] Built target oclc_isa_version_600_header
[ 35%] Built target oclc_isa_version_803_header
Scanning dependencies of target ocml_header
Scanning dependencies of target oclc_isa_version_1012_header
[ 35%] Built target oclc_isa_version_1032_header
[ 35%] Built target oclc_isa_version_601_header
Scanning dependencies of target opencl2.0-c.inc_target
Scanning dependencies of target oclc_isa_version_810_header
Scanning dependencies of target oclc_isa_version_602_header
[ 35%] Built target oclc_isa_version_1031_header
[ 36%] Generating ocml.inc
Scanning dependencies of target oclc_isa_version_703_header
Scanning dependencies of target oclc_unsafe_math_off_header
[ 37%] Generating oclc_isa_version_1012.inc
Scanning dependencies of target oclc_wavefrontsize64_off_header
[ 38%] Generating oclc_isa_version_810.inc
[ 39%] Generating opencl2.0-c.pch
Scanning dependencies of target oclc_isa_version_1010_header
Scanning dependencies of target oclc_isa_version_904_header
[ 40%] Generating oclc_isa_version_602.inc
[ 40%] Generating oclc_unsafe_math_off.inc
[ 40%] Built target oclc_isa_version_1012_header
[ 41%] Generating oclc_wavefrontsize64_off.inc
[ 42%] Generating oclc_isa_version_703.inc
[ 42%] Generating oclc_isa_version_1010.inc
[ 43%] Generating oclc_isa_version_904.inc
Scanning dependencies of target oclc_finite_only_off_header
[ 43%] Built target oclc_isa_version_810_header
[ 44%] Built target oclc_unsafe_math_off_header
[ 44%] Generating oclc_finite_only_off.inc
[ 44%] Built target oclc_isa_version_602_header
[ 44%] Built target oclc_wavefrontsize64_off_header
[ 44%] Built target oclc_isa_version_703_header
[ 44%] Built target oclc_isa_version_904_header
[ 44%] Built target oclc_isa_version_1010_header
Scanning dependencies of target oclc_isa_version_704_header
Scanning dependencies of target hc_header
Scanning dependencies of target opencl1.2-c.inc_target
Scanning dependencies of target oclc_correctly_rounded_sqrt_on_header
[ 44%] Built target oclc_finite_only_off_header
Scanning dependencies of target oclc_isa_version_900_header
Scanning dependencies of target oclc_finite_only_on_header
Scanning dependencies of target oclc_isa_version_902_header
[ 44%] Generating oclc_isa_version_704.inc
Scanning dependencies of target oclc_isa_version_906_header
[ 45%] Generating hc.inc
[ 46%] Generating oclc_correctly_rounded_sqrt_on.inc
[ 47%] Generating opencl1.2-c.pch
[ 48%] Generating oclc_finite_only_on.inc
[ 48%] Generating oclc_isa_version_900.inc
[ 49%] Generating oclc_isa_version_902.inc
[ 49%] Built target oclc_isa_version_704_header
[ 49%] Generating oclc_isa_version_906.inc
[ 49%] Built target oclc_correctly_rounded_sqrt_on_header
Scanning dependencies of target oclc_isa_version_90c_header
Scanning dependencies of target oclc_unsafe_math_on_header
[ 50%] Generating oclc_isa_version_90c.inc
[ 50%] Built target ocml_header
[ 51%] Generating oclc_unsafe_math_on.inc
Scanning dependencies of target oclc_daz_opt_off_header
[ 51%] Generating oclc_daz_opt_off.inc
[ 51%] Built target oclc_daz_opt_off_header
[ 51%] Built target oclc_unsafe_math_on_header
[ 51%] Built target oclc_isa_version_90c_header
[ 51%] Built target oclc_isa_version_902_header
[ 51%] Built target oclc_finite_only_on_header
[ 51%] Built target oclc_isa_version_906_header
[ 51%] Built target oclc_isa_version_900_header
Scanning dependencies of target opencl_header
Scanning dependencies of target ockl_header
Scanning dependencies of target oclc_isa_version_1030_header
Scanning dependencies of target oclc_isa_version_1011_header
Scanning dependencies of target oclc_wavefrontsize64_on_header
[ 52%] Generating opencl.inc
Scanning dependencies of target oclc_correctly_rounded_sqrt_off_header
[ 52%] Generating ockl.inc
Scanning dependencies of target oclc_isa_version_702_header
[ 52%] Generating oclc_isa_version_1030.inc
[ 53%] Generating oclc_isa_version_1011.inc
[ 54%] Generating oclc_correctly_rounded_sqrt_off.inc
[ 55%] Generating oclc_isa_version_702.inc
[ 55%] Built target oclc_isa_version_1030_header
[ 55%] Generating oclc_wavefrontsize64_on.inc
[ 55%] Built target hc_header
[ 55%] Built target oclc_isa_version_1011_header
[ 55%] Built target oclc_correctly_rounded_sqrt_off_header
[ 55%] Built target oclc_wavefrontsize64_on_header
Scanning dependencies of target oclc_isa_version_909_header
[ 56%] Generating oclc_isa_version_909.inc
[ 56%] Built target oclc_isa_version_909_header
[ 56%] Built target oclc_isa_version_702_header
[ 56%] Built target ockl_header
[ 56%] Built target opencl2.0-c.pch_target
[ 56%] Built target opencl1.2-c.pch_target
[ 56%] Built target opencl_header
[ 57%] Generating opencl1.2-c.inc
[ 58%] Generating opencl2.0-c.inc
[ 58%] Built target opencl1.2-c.inc_target
[ 58%] Built target opencl2.0-c.inc_target
Scanning dependencies of target amd_comgr
[ 58%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-compiler.cpp.o
[ 58%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-disassembly.cpp.o
[ 59%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr.cpp.o
[ 60%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-env.cpp.o
[ 61%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-objdump.cpp.o
[ 61%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-symbol.cpp.o
[ 62%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-metadata.cpp.o
[ 64%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-signal.cpp.o
[ 64%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-device-libs.cpp.o
[ 65%] Building CXX object CMakeFiles/amd_comgr.dir/src/comgr-elfdump.cpp.o
[ 65%] Building CXX object CMakeFiles/amd_comgr.dir/src/time-stat/time-stat.cpp.o
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-objdump.cpp:64:10: fatal error: llvm/Object/FaultMapParser.h: No such file or directory
 #include "llvm/Object/FaultMapParser.h"
          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
CMakeFiles/amd_comgr.dir/build.make:153: recipe for target 'CMakeFiles/amd_comgr.dir/src/comgr-objdump.cpp.o' failed
make[2]: *** [CMakeFiles/amd_comgr.dir/src/comgr-objdump.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp: In member function ‘void llvm::DisassemHelper::printELFFileHeader(const llvm::object::ObjectFile*)’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:118:51: error: no matching function for call to ‘printProgramHeaders(const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, false> >*, llvm::raw_ostream&)’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note: candidate: template<class ELFT> void printProgramHeaders(const llvm::object::ELFFile<ELFT>&, llvm::raw_ostream&)
 void printProgramHeaders(const ELFFile<ELFT> &ELF, raw_ostream &OS) {
      ^~~~~~~~~~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note:   template argument deduction/substitution failed:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:118:51: note:   mismatched types ‘const llvm::object::ELFFile<ELFT>’ and ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, false> >*’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:123:51: error: no matching function for call to ‘printProgramHeaders(const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, false> >*, llvm::raw_ostream&)’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note: candidate: template<class ELFT> void printProgramHeaders(const llvm::object::ELFFile<ELFT>&, llvm::raw_ostream&)
 void printProgramHeaders(const ELFFile<ELFT> &ELF, raw_ostream &OS) {
      ^~~~~~~~~~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note:   template argument deduction/substitution failed:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:123:51: note:   mismatched types ‘const llvm::object::ELFFile<ELFT>’ and ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, false> >*’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:128:51: error: no matching function for call to ‘printProgramHeaders(const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, true> >*, llvm::raw_ostream&)’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note: candidate: template<class ELFT> void printProgramHeaders(const llvm::object::ELFFile<ELFT>&, llvm::raw_ostream&)
 void printProgramHeaders(const ELFFile<ELFT> &ELF, raw_ostream &OS) {
      ^~~~~~~~~~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note:   template argument deduction/substitution failed:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:128:51: note:   mismatched types ‘const llvm::object::ELFFile<ELFT>’ and ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, true> >*’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:133:51: error: no matching function for call to ‘printProgramHeaders(const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >*, llvm::raw_ostream&)’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note: candidate: template<class ELFT> void printProgramHeaders(const llvm::object::ELFFile<ELFT>&, llvm::raw_ostream&)
 void printProgramHeaders(const ELFFile<ELFT> &ELF, raw_ostream &OS) {
      ^~~~~~~~~~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note:   template argument deduction/substitution failed:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:133:51: note:   mismatched types ‘const llvm::object::ELFFile<ELFT>’ and ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >*’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note: candidate: template<class ELFT> void printProgramHeaders(const llvm::object::ELFFile<ELFT>&, llvm::raw_ostream&)
 void printProgramHeaders(const ELFFile<ELFT> &ELF, raw_ostream &OS) {
      ^~~~~~~~~~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:50:6: note:   template argument deduction/substitution failed:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-elfdump.cpp:133:51: note:   mismatched types ‘const llvm::object::ELFFile<ELFT>’ and ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >*’
     printProgramHeaders(ELFObj->getELFFile(), OutS);
                                                   ^
CMakeFiles/amd_comgr.dir/build.make:114: recipe for target 'CMakeFiles/amd_comgr.dir/src/comgr-elfdump.cpp.o' failed
make[2]: *** [CMakeFiles/amd_comgr.dir/src/comgr-elfdump.cpp.o] Error 1
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-isa-metadata.def:70:60: error: ‘EF_AMDGPU_MACH_AMDGCN_GFX90A’ is not a member of ‘llvm::ELF’
 HANDLE_ISA("amdgcn-amd-amdhsa-", "gfx90a",    true,  true, EF_AMDGPU_MACH_AMDGCN_GFX90A,  true, 65536,  32,  4,   40, 1024,   16, 800, 102,    4, 256, 256)
                                                            ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:380:9: note: in definition of macro ‘HANDLE_ISA’
    ELF::ELF_MACHINE,                                                           \
         ^~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-isa-metadata.def:70:60: note: suggested alternative: ‘EF_AMDGPU_MACH_AMDGCN_GFX90C’
 HANDLE_ISA("amdgcn-amd-amdhsa-", "gfx90a",    true,  true, EF_AMDGPU_MACH_AMDGCN_GFX90A,  true, 65536,  32,  4,   40, 1024,   16, 800, 102,    4, 256, 256)
                                                            ^
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:380:9: note: in definition of macro ‘HANDLE_ISA’
    ELF::ELF_MACHINE,                                                           \
         ^~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfMetadataRoot(const llvm::object::ELFObjectFile<ELFT>*, COMGR::DataMeta*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, false>; amd_comgr_status_t = amd_comgr_status_s]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:339:45:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:272:24: error: invalid initialization of reference of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, false> >&’ from expression of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, false> >*’
   const ELFFile<ELFT> &ELFFile = Obj->getELFFile();
                        ^~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfMetadataRoot(const llvm::object::ELFObjectFile<ELFT>*, COMGR::DataMeta*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, true>; amd_comgr_status_t = amd_comgr_status_s]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:342:45:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:272:24: error: invalid initialization of reference of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, true> >&’ from expression of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, true> >*’
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfMetadataRoot(const llvm::object::ELFObjectFile<ELFT>*, COMGR::DataMeta*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, false>; amd_comgr_status_t = amd_comgr_status_s]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:345:45:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:272:24: error: invalid initialization of reference of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, false> >&’ from expression of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, false> >*’
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfMetadataRoot(const llvm::object::ELFObjectFile<ELFT>*, COMGR::DataMeta*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, true>; amd_comgr_status_t = amd_comgr_status_s]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:348:43:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:272:24: error: invalid initialization of reference of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >&’ from expression of type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >*’
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameImpl(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, false>; amd_comgr_status_t = amd_comgr_status_s; size_t = long unsigned int]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:795:52:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:776:38: error: request for member ‘getHeader’ in ‘Obj->llvm::object::ELFObjectFile<llvm::object::ELFType<(llvm::support::endianness)1, false> >::getELFFile()’, which is of pointer type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, false> >*’ (maybe you meant to use ‘->’ ?)
   auto ElfHeader = Obj->getELFFile().getHeader();
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameImpl(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, true>; amd_comgr_status_t = amd_comgr_status_s; size_t = long unsigned int]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:798:52:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:776:38: error: request for member ‘getHeader’ in ‘Obj->llvm::object::ELFObjectFile<llvm::object::ELFType<(llvm::support::endianness)1, true> >::getELFFile()’, which is of pointer type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)1, true> >*’ (maybe you meant to use ‘->’ ?)
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameImpl(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, false>; amd_comgr_status_t = amd_comgr_status_s; size_t = long unsigned int]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:801:52:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:776:38: error: request for member ‘getHeader’ in ‘Obj->llvm::object::ELFObjectFile<llvm::object::ELFType<(llvm::support::endianness)0, false> >::getELFFile()’, which is of pointer type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, false> >*’ (maybe you meant to use ‘->’ ?)
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp: In instantiation of ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameImpl(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, true>; amd_comgr_status_t = amd_comgr_status_s; size_t = long unsigned int]’:
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:804:50:   required from here
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:776:38: error: request for member ‘getHeader’ in ‘Obj->llvm::object::ELFObjectFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >::getELFFile()’, which is of pointer type ‘const llvm::object::ELFFile<llvm::object::ELFType<(llvm::support::endianness)0, true> >*’ (maybe you meant to use ‘->’ ?)
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:668:1: warning: ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameFromElfHeader(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, true>]’ used but never defined
 getElfIsaNameFromElfHeader(const ELFObjectFile<ELFT> *Obj, size_t *Size,
 ^~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:668:1: warning: ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameFromElfHeader(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, false>]’ used but never defined
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:668:1: warning: ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameFromElfHeader(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, true>]’ used but never defined
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:668:1: warning: ‘amd_comgr_status_t COMGR::metadata::getElfIsaNameFromElfHeader(const llvm::object::ELFObjectFile<ELFT>*, size_t*, char*) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, false>]’ used but never defined
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:223:13: warning: ‘bool COMGR::metadata::processNote(COMGR::metadata::Elf_Note<ELFT>&, COMGR::DataMeta*, llvm::msgpack::DocNode&) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, true>]’ used but never defined
 static bool processNote(const Elf_Note<ELFT> &Note, DataMeta *MetaP,
             ^~~~~~~~~~~
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:223:13: warning: ‘bool COMGR::metadata::processNote(COMGR::metadata::Elf_Note<ELFT>&, COMGR::DataMeta*, llvm::msgpack::DocNode&) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)0, false>]’ used but never defined
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:223:13: warning: ‘bool COMGR::metadata::processNote(COMGR::metadata::Elf_Note<ELFT>&, COMGR::DataMeta*, llvm::msgpack::DocNode&) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, true>]’ used but never defined
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:223:13: warning: ‘bool COMGR::metadata::processNote(COMGR::metadata::Elf_Note<ELFT>&, COMGR::DataMeta*, llvm::msgpack::DocNode&) [with ELFT = llvm::object::ELFType<(llvm::support::endianness)1, false>]’ used but never defined
/usr/local/ROCm-CompilerSupport/lib/comgr/src/comgr-metadata.cpp:441:20: warning: ‘std::__cxx11::string COMGR::metadata::convertOldTargetNameToNew(const string&, bool, uint32_t)’ defined but not used [-Wunused-function]
 static std::string convertOldTargetNameToNew(const std::string &OldName,
                    ^~~~~~~~~~~~~~~~~~~~~~~~~
CMakeFiles/amd_comgr.dir/build.make:140: recipe for target 'CMakeFiles/amd_comgr.dir/src/comgr-metadata.cpp.o' failed
make[2]: *** [CMakeFiles/amd_comgr.dir/src/comgr-metadata.cpp.o] Error 1
CMakeFiles/Makefile2:1402: recipe for target 'CMakeFiles/amd_comgr.dir/all' failed
make[1]: *** [CMakeFiles/amd_comgr.dir/all] Error 2
Makefile:162: recipe for target 'all' failed
make: *** [all] Error 2
root@vegacloud:/usr/local/ROCm-CompilerSupport/lib/comgr/build# Makefile:162: recipe for target 'all' failed
make: *** [all] Error 2
```




---

### 评论 #3 — xuhuisheng (2021-04-02T05:27:24Z)

I suggest you following my build scripts order. 11 to 19
https://github.com/xuhuisheng/rocm-build


---

### 评论 #4 — ROCmSupport (2021-04-05T08:01:09Z)

Thanks @SomnusMistletoe for reaching out.
Can you please try installing comgr via "sudo apt install comgr" and give a try.
And also we are enhancing build steps for ROCm, it will take some time. Meanwhile you can try building rocm from above comment also.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-04-09T09:50:03Z)

Hi @SomnusMistletoe 
Please share an update so that we will work and provide resolution asap.
Thank you.

---

### 评论 #6 — SomnusMistletoe (2021-04-09T10:02:14Z)

Hi @ROCmSupport 
I have a question：in this document   https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP-Installation.html
In order to build rocclr, we need to execute
`git clone -b rocm-4.1.x https://github.com/ROCm-Developer-Tools/ROCclr.git`

howerver，the latest release version of ROCclr is 4.0.0 in https://github.com/ROCm-Developer-Tools/ROCclr.
So which version should I git clone?



---

### 评论 #7 — ROCmSupport (2021-04-09T10:08:33Z)

Hi @SomnusMistletoe 
4.1 branch is there and so request you to use: [https://github.com/ROCm-Developer-Tools/ROCclr/tree/rocm-4.1.x](url)
Thank you.

---

### 评论 #8 — xuhuisheng (2021-04-09T11:14:17Z)

@SomnusMistletoe 
Github only display release on the homepage of repo.
Actually there is a rocm-4.1.0 tag after rocm-4.0.0 release. 
https://github.com/ROCm-Developer-Tools/ROCclr/releases/tag/rocm-4.1.0

---

### 评论 #9 — ROCmSupport (2021-05-07T12:10:03Z)

Hi @SomnusMistletoe 
Hope you tried 4.1.0 now. As its open for more than 14 days, I am closing this right now.
I tried the same and as I said no issue is observed, compilation of rocclr is perfect.
Feel free to open a new issue, if any.
Thank you.


---
