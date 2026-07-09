# rccl -r switch caused build failure

- **Issue #:** 1472
- **State:** closed
- **Created:** 2021-05-16T09:55:26Z
- **Updated:** 2021-08-04T11:03:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1472

```
the install -idt (install, dependency, build test is ok).
however -r (run quick test) has failed as below starting around 88%...
Tested on rocm4.1, 4.2 on Ubuntu1804 + MI25 all similar result. 

[ 79%] Building CXX object test/CMakeFiles/UnitTestsMultiProcess.dir/test_GroupCallsMultiProcess.cpp.o
[ 81%] Building CXX object test/CMakeFiles/UnitTestsMultiProcess.dir/test_ScatterMultiProcess.cpp.o
[ 82%] Building CXX object test/CMakeFiles/UnitTests.dir/test_AllReduce.cpp.o
[ 84%] Building CXX object test/CMakeFiles/UnitTests.dir/test_Reduce.cpp.o
[ 84%] Building CXX object test/CMakeFiles/UnitTests.dir/test_AllGather.cpp.o
[ 86%] Building CXX object test/CMakeFiles/UnitTests.dir/test_ReduceScatter.cpp.o
[ 87%] Building CXX object test/CMakeFiles/UnitTests.dir/test_Broadcast.cpp.o
[ 88%] Building CXX object test/CMakeFiles/UnitTests.dir/test_GroupCalls.cpp.o
/root/ROCm-4.1/rccl/test/test_ReduceScatterMultiProcess.cpp:72:30: error: unknown type name 'ReduceScatterMultiProcessCorrectnessSweep'; did you mean 'ReduceScatterMultiProcessCorrectnessTest'?
    INSTANTIATE_TEST_SUITE_P(ReduceScatterMultiProcessCorrectnessSweep,
                             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                             ReduceScatterMultiProcessCorrectnessTest
/root/ROCm-4.1/rccl/test/test_ReduceScatterMultiProcess.hpp:13:11: note: 'ReduceScatterMultiProcessCorrectnessTest' declared here
    class ReduceScatterMultiProcessCorrectnessTest : public MultiProcessCorrectnessTest
          ^
/root/ROCm-4.1/rccl/test/test_ReduceScatterMultiProcess.cpp:72:71: error: parameter type 'CorrectnessTests::ReduceScatterMultiProcessCorrectnessTest' is an abstract class
    INSTANTIATE_TEST_SUITE_P(ReduceScatterMultiProcessCorrectnessSweep,
                                                                      ^
/usr/local/include/gtest/gtest.h:484:16: note: unimplemented pure virtual method 'TestBody' in 'ReduceScatterMultiProcessCorrectnessTest'
  virtual void TestBody() = 0;
```


