# HCC RUNTIME ERROR in hipCaffe

- **Issue #:** 354
- **State:** closed
- **Created:** 2018-03-07T09:11:46Z
- **Updated:** 2018-03-08T01:50:08Z
- **URL:** https://github.com/ROCm/ROCm/issues/354

Issue summary

./build/test/test_all.testbin

Backtrace:
0x00007f04870cd32e:	Kalmar::CLAMP::DetermineAndGetProgram(Kalmar::KalmarQueue*, unsigned long*, void**) + 0x59e
0x00007f04870cd690:	Kalmar::KalmarBootstrap::KalmarBootstrap() + 0x120
0x00007f04870cd549:	__hcc_shared_library_init + 0x29
0x00007f048a2766ba:	_dl_rtld_di_serinfo + 0x706a
0x00007f048a2767cb:	_dl_rtld_di_serinfo + 0x717b
0x00007f048a266c6a:	+ 0x717b

HCC RUNTIME ERROR: Fail to find compatible kernel at file:mcwamp.cpp line:346


Operating system: Ubuntu 16.04
