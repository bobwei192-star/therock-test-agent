# [Documentation]: Confusing rocm support for gfx1151

- **Issue #:** 5339
- **State:** closed
- **Created:** 2025-09-16T15:33:42Z
- **Updated:** 2026-03-25T18:29:27Z
- **Labels:** Under Investigation, status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5339

### Description of errors

I would love to buy a framework desktop which has a AMD Ryzen™ AI Max 385.
My intended use is to train small to medium size AI models with Rocm for my bachelors degree.
But after checking the documentation for Rocm i am extremely confused.

Some sources claim the gfx1151 has had support since Rocm 6, but on the announcements page of Rocm 7 it said:

```
### Expanding ROCm Ecosystem Across AMD Ryzen™ AI Processor and AMD Radeon™ Graphics

ROCm endpoint AI ecosystem supports Linux and Windows on AMD Radeon products including the latest Radeon RX 9000 series, as well as the class leading Ryzen AI MAX products.
```

Which sounds to me an awful lot like the Ryzen AI max products / gfx1151 are getting support with Rocm 7.

So i initially waited until the updated documentation for Rocm 7 was posted online. Before jumping to conclusions.
Yet when i checked the updated documentation today, it looks like gfx1151 doesn't have Rocm spport at all...

gfx1151 isn't even mentioned on the compatibility matrix page once, nor on the release notes page of Rocm 7.


If someone could please inform me what is going on here and where I'm making a mistake in my reasoning, that would be awesome.

### Attach any links, screenshots, or additional evidence you think will be helpful.

https://www.amd.com/en/products/software/rocm/whats-new.html
https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html
https://rocm.docs.amd.com/en/latest/about/release-notes.htm
https://www.amd.com/en/developer/resources/technical-articles/2025/amd-rocm-7-built-for-developers-ready-for-enterprises.html