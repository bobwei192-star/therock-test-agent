# Clarify text wrt closed-source: "These components are only available through the ROCm repositories"

- **Issue #:** 267
- **State:** closed
- **Created:** 2017-12-05T11:43:35Z
- **Updated:** 2018-09-17T21:10:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/267

The README states:

```
These components are only available through the ROCm repositories, 
and will either be deprecated or become open source components in 
the future. These components are made available in the following packages:
      hsa-ext-rocr-dev
```

could you please clarify?  If closed-source components are available through repos, are we talking about binaries in the github repositories, or are we talking about deb repositories? 

Also, is this required?

The reason for asking is that I'd like to generally know how to build ROCm on NixOS.  We can build from source, or we can unpack the debian archives.  Also, specifically knowing how this relates to the 4.15rc2 kernel (which is the latest as of today) would be good.

A general update wrt the 4.15 kernel would be good.