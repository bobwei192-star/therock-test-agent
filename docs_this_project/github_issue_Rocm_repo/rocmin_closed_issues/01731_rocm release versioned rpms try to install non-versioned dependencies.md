# rocm release versioned rpms try to install non-versioned dependencies

- **Issue #:** 1731
- **State:** closed
- **Created:** 2022-04-25T20:21:40Z
- **Updated:** 2024-02-17T15:41:37Z
- **URL:** https://github.com/ROCm/ROCm/issues/1731

When I say "release versioned" I mean rpms such as rocm-core4.5.0 vs the non-versioned rocm-core-4.5.0.

Switching our system over from 4.5.0 to a split 4.5.0 + 5.0.0 set of packages, as a test case, I found that
trying to add random rocm packages in would try to "drag in" non-versioned packages instead of the matching
versioned packages.    

I worked around this by installing dependencies by hand, or trying a group install (a package which
brings in many other packages) ... and checking the list to make sure all the dependencies were
versioned dependencies.   Needless to say this was quite time consuming to track down something
which allowed a proper install due to this issue.

I've added details about the last thing our researcher needed, and used it as an example here, after
everything else was installed.

I don't have the time to track this down, but it was definitely quite repeatable.  You might try a centos-8
container to repeat it in.   I removed all the non-versioned rocm software before migrating to the
versioned software.     I may try to repeat this in a container, as time permits, but it is low on my
priority list.

If you try to install the "versioned" rocm-gdb, you will find out that it tries to install non-versioned dependencies,
such as comgr, rocm-core, and rocm-dbgapi.    Those dependencies are incorrect, and it should be calling
for versioned dependency, such as comgr4.5.0, rocm-core4.5.0, and rocm-dbgapi4.5.0.

However, if I install versioned dependency, rocm-dbgapi4.5.0, for example, then it looks like
it has a side-effect of remedying this issue with rocm-gdb.    

rocm-gdb is not the only package that has this issue; I've had to install most of the rocm stack by hand
(aka package by package by hand to find ones that have complete versioned dependencies, instead
of some versioned and then reverting to un-versioned  due to this same issue with almost any versioned package.  

This occurred on centos-8 with rocm versions 4.5.0 and 5.0.0.

Once I validate our dual-version install, I'll add in the latest rocm version, to see if the behavior
persists with it.   I am using the rpm / yum based install.