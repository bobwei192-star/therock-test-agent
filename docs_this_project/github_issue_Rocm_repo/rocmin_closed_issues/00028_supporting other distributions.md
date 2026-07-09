# supporting other distributions

- **Issue #:** 28
- **State:** closed
- **Created:** 2016-08-31T17:49:55Z
- **Updated:** 2017-10-23T09:28:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/28

Hi - I wanted to inquire on the availability of packages for other distributions - from RHEL/SLES to desktops such as OpenSUSE.

I understand this project on the whole is FOSS, but it is a big /complex toolchain and seemingly the FOSS path is unused (take #27 as a kernel of truth towards this ).  Ubuntu is a good start but there needs to be some builds available for other distributions.  It would probably operate best if using the upstream build systems, such as Novell/SuSE's Open Build System (OBS), whether you still host a local repository (like for Ubuntu) or use build.opensuse.org for hosting.  Fedora has something similar as does really many distros - however I know several projects/corporation have used OBS, such as Intel Tizen... it also supports building against many other distros, if that's of interest.   My main point is though that support should be increased in a manner similar to ZFSonLinux.

Surely you have more resources than a LLNL project porting an existing software? :-)
