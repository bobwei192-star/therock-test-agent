# hipcc linker issue

- **Issue #:** 918
- **State:** closed
- **Created:** 2019-10-22T13:33:49Z
- **Updated:** 2023-12-18T17:14:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/918

I am having one hip project in which i came across following scenario:

I have two cuda files(hipyfied) with same name in following file structure:
1) /root/tmp/file.cu
2) /root/tmp/in/file.cu
[sample.zip](https://github.com/RadeonOpenCompute/ROCm/files/3755949/sample.zip)

which have different implementation they are not identical.
While compiling i did not get any error but after linking in my .so it is
linking second file twice which i have verified using nm command.
I have created sample code for above scenario which is also failing with same reason.

How to reproduce:
hipcc -c f1.cpp f2.cpp
hipcc -c test/f1.cpp
hipcc f1.o f2.o test/f1.o -o -shared libf.so

please find sample code attached 