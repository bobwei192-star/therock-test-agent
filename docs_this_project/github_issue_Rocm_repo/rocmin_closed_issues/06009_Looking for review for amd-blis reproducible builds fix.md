# Looking for review for amd-blis reproducible builds fix

- **Issue #:** 6009
- **State:** closed
- **Created:** 2026-03-02T05:04:12Z
- **Updated:** 2026-03-12T14:50:57Z
- **Labels:** status: fix submitted
- **Assignees:** darren-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6009

Hi,

Can I please get some help getting an amd-blis fix for compliance with the [reproducible builds spec](https://reproducible-builds.org/docs/source-date-epoch/) reviewed & merged?

- https://github.com/amd/blis/pull/44

The PR's been sitting since October. For now, we're [vendoring a patch](https://github.com/NixOS/nixpkgs/blob/master/pkgs/by-name/am/amd-blis/build-date.patch) to work around this to ensure the build is reproducible in NixOS.

Please let me know if this isn't the right place for this. amd-blis isn't under the ROCm org, but is a dependency of ROCm BLAS packages.