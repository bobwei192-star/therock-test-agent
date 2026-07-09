# [CMAKE] Variables aren't set correctly in rocBlas 6.3.2

- **Issue #:** 4449
- **State:** open
- **Created:** 2025-02-12T13:08:05Z
- **Updated:** 2025-03-06T09:50:15Z
- **Labels:** Under Investigation
- **Assignees:** TorreZuk
- **URL:** https://github.com/ROCm/ROCm/issues/4449

Heelo,
sometimes it makes me curious how you get your builds done. In this case some CMAKE-variables aren't set in your scripts.
I tried to build rocBlas with the "T_rocblas" make-target on cmd.
Details are in the tarball. 
[rocblas_issue.tar.gz](https://github.com/user-attachments/files/18768247/rocblas_issue.tar.gz)
The variable in question are:
CMAKE_CXX_COMPILER
CMAKE_MAKE_PROGRAM

 