# Missing dependency perl-URI-Encode not in CentOS PowerTools

- **Issue #:** 1448
- **State:** closed
- **Created:** 2021-04-09T15:02:40Z
- **Updated:** 2021-07-07T03:52:44Z
- **URL:** https://github.com/ROCm/ROCm/issues/1448

The ROCm 4.1.1 release notes mention new the the "hip-base package has a dependency on Perl modules that some operating systems may not have in their default package repositories."
According to the release notes it should be enough to enable the Power Tools repository for CentOS. (CoreReady Builder for RHEL). However the Power Tools repository does **not** contain the (all?) newly added dependencies.

In particular hip-base now requires `perl-URI-Encode`. This package is not part of Power Tools or any other official CentOS (or RHEL repository). It seems to be part of EPEL, but I hesitate to enable EPEL on all machines just for this dependency.

I hence ask you to please remove this depency again or contact Red Hat and ask them to include it in a future RHEL minor/major release. Of course you'd have to provide sufficient arguments why this particular package is required.