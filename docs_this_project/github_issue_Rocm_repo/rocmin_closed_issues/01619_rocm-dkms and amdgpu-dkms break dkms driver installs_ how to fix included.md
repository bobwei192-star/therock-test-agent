# rocm-dkms and amdgpu-dkms break dkms driver installs, how to fix included

- **Issue #:** 1619
- **State:** closed
- **Created:** 2021-11-16T18:26:46Z
- **Updated:** 2024-01-25T17:59:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/1619

When ROCm 4.5.0 was released, I tried installing it a few days later
on our  GPU system, so that we could give AMD immediate feedback.

Unfortunately,  I was unable to install and operate the newer ROCm-4.5.0
release.  In addition I was _unable_ to revert our platform back to using the previous
version of rocm.  We could not use our GPU, nor install the AMD software
for the GPU.

This is on centos-8 using the RPM packages provided by AMD's repository

        I tracked down the problem, was about to further investigate,
        and then found that the researchers and staff at Rice had
        the same problem earlier this year and tracked down the
        cause and made a solution.

After examining their results, I was able to easily remedy the
problem on our ROCm platform.

I'm forwarding this information to you so that a fix can be made
to the ROCm software in the future, and also the current and future
release notes can be updated so that users affected by this problem
can resume normal operation.


The fix to this problem is that the rock-dkms and amdgpu-dkms
packages have an error.  They change the "driving signing state"
for dkms drivers to require a signed driver.   They do this _after_
the driver is installed (with an RPM scriptlet).

        So, the first time you install those drivers... they install
        correctly.  After that, well it can NOT be re-installed or
        modified or updated.  In addition, the DKMS configuration is
        broken for most any other DKMS driver.


The error with that change is that....

What is happening, is that the RPM scriptlet is incorrectly configuring
a site-chosen decision, a policy change which does not belong in an
installed package.

        DKMS Driver signing is a _site_ decision, not a _package_ (rpm)
        decision.   In our cases, the {rocm,amdgpu}-dkms packages doing
        this, causes a failure to install (even after removal) of any
        different or newer {rocm,amdgpu}-dkms  package on the system.

It is a _site_ decision, as a site needs to invest in the
infrastructure to support dkms driver signing -- and that is not a
common configuration.


From my point of view, The solution to this is two fold:

        1) The rocm-dkms and amdgpu-dkms packages should
        be fixed so that they no longer try to change the
        driver signing configuration, and leave it to the
        site's choice.

        2) A note about this needs to be added to the ROCm release notes.

                The note should say that the /etc/dkms/framework.conf
                may need to be edited to remove the driving signing
                installed by the rocm-dkms or amdgpu-dkms packages
                for sites that do not use driver signing.

                That is the "sign_tool=" directive in that file.

I say "may be" .. because it won't break a site with driver
signing enabled, just those who do not use it.  So, if a site uses
driver signing, they won't see this flaw.

With this change,  I was able to upgrade to amdgpu-dkms from the old
rocm-dkms, and successfully install and test rocm-4.5.0 on our GPU platform

I advise fixing the RPMs and adding a note about this to the installer instructions,
so that installations which have this problem can easily fix their installs.
