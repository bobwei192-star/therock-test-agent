# hcc::__activelaneid_u32() doesn't seem to work in HCC 2.0

- **Issue #:** 688
- **State:** closed
- **Created:** 2019-01-25T04:18:53Z
- **Updated:** 2019-01-29T21:42:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/688

Summary of your hardware: Threadripper 1950x + Vega64

PCIe Information: PCIe 3.0.

Here's my test code.

```
#include<iostream>
#include<stdint.h>

#include <hc.hpp>

int main(){
	const int N = (1 << 30) / sizeof(uint32_t); 
	uint32_t* stuff = new uint32_t[N];
	uint32_t* output = new uint32_t[N];

	for(int i=0; i<N; i++){
		stuff[i] = i;
	}

	hc::array_view<uint32_t, 1> av_in(N, stuff);
	hc::array_view<uint32_t, 1> av_out(N, output);

	hc::parallel_for_each(hc::extent<1>(N), [=](hc::index<1> i) [[hc]] {
		av_out[i[0]] = hc::__activelaneid_u32();
	});

	for(int i=0; i< 100; i++){
		std::cout << i << "    " << av_out[i] << "\n"; 
	}
}
```

When I compile...

```
hcc `hcc-config --cxxflags --ldflags` test.cpp -o test
ld.lld: error: relocation R_AMDGPU_REL32_LO cannot be used against symbol __activelaneid_u32; recompile with -fPIC
>>> defined in /tmp/tmp.hO38AglmSw/kernel-gfx900.hsaco.isabin
>>> referenced by /tmp/tmp.hO38AglmSw/kernel-gfx900.hsaco.isabin:(main::$_0::__cxxamp_trampoline(unsigned int*, int, int, int, int, int, int, int))

ld.lld: error: relocation R_AMDGPU_REL32_HI cannot be used against symbol __activelaneid_u32; recompile with -fPIC
>>> defined in /tmp/tmp.hO38AglmSw/kernel-gfx900.hsaco.isabin
>>> referenced by /tmp/tmp.hO38AglmSw/kernel-gfx900.hsaco.isabin:(main::$_0::__cxxamp_trampoline(unsigned int*, int, int, int, int, int, int, int))
Generating AMD GCN kernel failed in ld.lld for target: gfx900
clang-8: error: linker command failed with exit code 1 (use -v to see invocation)
Makefile:2: recipe for target 'test' failed
make: *** [test] Error 1
```

Version information:

```
hcc --version
HCC clang version 8.0.0 (ssh://gerritgit/compute/ec/hcc-tot/clang 6ec3c61e09fbb60373eaf5a40021eb862363ba2c) (ssh://gerritgit/lightning/ec/llvm ab3b88ffc2ae50f55361a49aec89f6e95d9d0ec4) (based on HCC 1.3.18482-757fb49-6ec3c61-ab3b88f )
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/bin
```