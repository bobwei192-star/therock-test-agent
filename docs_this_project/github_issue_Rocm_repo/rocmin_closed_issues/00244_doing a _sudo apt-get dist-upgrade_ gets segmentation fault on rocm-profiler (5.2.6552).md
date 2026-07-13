# doing a "sudo apt-get dist-upgrade" gets segmentation fault on rocm-profiler (5.2.6552)

- **Issue #:** 244
- **State:** closed
- **Created:** 2017-11-06T16:42:14Z
- **Updated:** 2018-06-03T15:13:46Z
- **URL:** https://github.com/ROCm/ROCm/issues/244

$ sudo apt-get dist-upgrade
Reading package lists... Done
Building dependency tree
... (deleted a bunch of lines) ...
...
Setting up rocm-profiler (5.2.6552) ...
/var/lib/dpkg/info/rocm-profiler.postinst: line 14: 14658 Segmentation fault      (core dumped) bin/rcprof --list --outputfile ./$COUNTER_FILE_DIR/counters.csl --maxpassperfile 1
Setting up rocm-dev (1.6.180) ...
...
... (deleted a bunch of lines) ...

On Ubuntu 16.04.3 LTS with all updates.

Is this something I need to worry about?
