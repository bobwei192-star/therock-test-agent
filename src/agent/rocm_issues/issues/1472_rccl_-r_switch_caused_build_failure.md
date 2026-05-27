# rccl -r switch caused build failure

> **Issue #1472**
> **状态**: closed
> **创建时间**: 2021-05-16T09:55:26Z
> **更新时间**: 2021-08-04T11:03:24Z
> **关闭时间**: 2021-06-04T21:49:54Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1472

## 描述

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




---

## 评论 (5 条)

### 评论 #1 — gggh000 (2021-05-19T03:55:06Z)

4.2 failed as well 
```
./install.sh -r

..
[ 76%] Building CXX object test/CMakeFiles/UnitTestsMultiProcess.dir/test_CombinedCallsMultiProcess.cpp.o
[ 77%] Building CXX object test/CMakeFiles/UnitTestsMultiProcess.dir/test_ReduceScatterMultiProcess.cpp.o
[ 78%] Building CXX object test/CMakeFiles/UnitTestsMultiProcess.dir/test_ScatterMultiProcess.cpp.o
[ 80%] Building CXX object test/CMakeFiles/UnitTestsMultiProcess.dir/test_ReduceMultiProcess.cpp.o
[ 81%] Building CXX object test/CMakeFiles/UnitTests.dir/test_AllGather.cpp.o
[ 82%] Building CXX object test/CMakeFiles/UnitTests.dir/test_ReduceScatter.cpp.o
[ 84%] Building CXX object test/CMakeFiles/UnitTests.dir/test_GroupCalls.cpp.o
[ 85%] Building CXX object test/CMakeFiles/UnitTests.dir/test_AllReduce.cpp.o
[ 86%] Building CXX object test/CMakeFiles/UnitTests.dir/test_Reduce.cpp.o
[ 88%] Building CXX object test/CMakeFiles/UnitTests.dir/test_Broadcast.cpp.o
In file included from /root/ROCm-4.2/rccl/test/test_CombinedCallsMultiProcess.cpp:6:
In file included from /root/ROCm-4.2/rccl/test/test_CombinedCallsMultiProcess.hpp:10:
/root/ROCm-4.2/rccl/test/CorrectnessTest.hpp:465:15: error: use of undeclared identifier 'GTEST_SKIP'
              GTEST_SKIP();
              ^
/root/ROCm-4.2/rccl/test/CorrectnessTest.hpp:506:17: error: use of undeclared identifier 'IsSkipped'
            if (IsSkipped()) return;
                ^
In file included from /root/ROCm-4.2/rccl/test/test_ReduceScatter.cpp:7:
In file included from /root/ROCm-4.2/rccl/test/test_ReduceScatter.hpp:9:
/root/ROCm-4.2/rccl/test/CorrectnessTest.hpp:465:15: error: use of undeclared identifier 'GTEST_SKIP'
              GTEST_SKIP();
              ^
In file included from /root/ROCm-4.2/rccl/test/test_GroupCallsMultiProcess.cpp:6:
In file included from /root/ROCm-4.2/rccl/test/test_GroupCallsMultiProcess.hpp:10:
/root/ROCm-4.2/rccl/test/CorrectnessTest.hpp:465:15: error: use of undeclared identifier 'GTEST_SKIP'
              GTEST_SKIP();
..
```


---

### 评论 #2 — ROCmSupport (2021-05-31T10:53:21Z)

Thanks @gggh000 
I am able to reproduce this problem and assigned to developer.
Thank you.

---

### 评论 #3 — stanleytsang-amd (2021-06-03T20:20:49Z)

Hi @gggh000,

I'm one of the developers for RCCL.

Taking a quick look at this issue, I think I know what's wrong with the install script.  Passing just the "-r" option should not trigger a rebuild of the tests, but it does.  This can be fixed.

In the meantime, you can completely avoid this issue by installing dependencies (-d), building unit tests (-t) and running the unit tests (-r) in one step: ./install -dtr

Or, if the unit tests are already built and you want to rerun them without triggering a rebuild, you can run the install script as follows: ./install -r --no_clean

---

### 评论 #4 — gggh000 (2021-06-04T19:02:47Z)

ok, I will retry. 

---

### 评论 #5 — ROCmSupport (2021-08-04T11:03:24Z)

Hi @gggh000 
Got some update on this.
Verifed with ROCm 4.3, issue is fixed and no more observed.
Thank you.

---
