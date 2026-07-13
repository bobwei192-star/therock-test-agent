# Request for Information: HIP - what's with the prefix?

- **Issue #:** 202
- **State:** closed
- **Created:** 2017-09-08T02:58:23Z
- **Updated:** 2017-09-10T13:16:57Z
- **URL:** https://github.com/ROCm/ROCm/issues/202

Or rather is there not a way to fuse and focus on better nvcc compatability?

What I'm getting at is I respect hip should be by default it's own thing and show that throughout code with the hip prefix.  But I wonder why, when it targets CUDA compatability, it cannot just work for code not relying on intrinsics/inline ptx or fancy features.  I don't know, maybe a sourcecompat flag. The issue is mainly around the runtime/hostside portion of things.

I'd like to gain some reasoning as to why compiling from a very clean and simple "plain-old-CUDA" sourcefile would always require a hipify pass.  It adds burden to the build process to generate sourcefiles and this is definitely a complex detail in any build system I've ever seen (make/cmake in mind specifically).  Should we expect that hipify will always be a required to compile hip-minded CUDA code with the ROCm ecosystem?