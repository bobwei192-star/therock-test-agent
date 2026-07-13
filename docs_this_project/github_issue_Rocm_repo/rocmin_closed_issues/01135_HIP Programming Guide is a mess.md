# HIP Programming Guide is a mess

- **Issue #:** 1135
- **State:** closed
- **Created:** 2020-06-06T19:02:17Z
- **Updated:** 2025-01-27T18:08:37Z
- **Labels:** Under Investigation, Documentation
- **Milestone:** 5.7.0
- **Assignees:** Maetveis, MathiasMagnus, Naraenda, saadrahim
- **URL:** https://github.com/ROCm/ROCm/issues/1135

https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html

is unusable.

I have 20 years of programming experience with C, C++, D, and many other languages, and HPC programming, but I can't parse this document at all.

1) It has a number of references to non-HIP stuff, like HCC, and OpenCL. And even Anaconda, where two paragraphs later reader is notified that it actually doesn't work yet.

2) Formatting is all over the place, and many `code` stuff are not formatted or formatted in a broken way.

3) There are no full examples provided or instructions to how to compile and execute simple HIP codes.

4a) It contains stuff that is totally unrelated to Programming Guide purpose. Things like versioning scheme and git tags. It is extremely niche and inconsequential, and shouldn't be there.

4b) The document starts with FAQ of random stuff, instead of providing relevant information first.

4c) There is a link to "HIP Programming Guide" from inside the "HIP programming guide" . I am not sure if this is a joke.

5a) Finding how to even install HIP in this document is hard, there is a link, but it is buried in the middle of the text, plus the link that it leads to shows how to install `hip_hcc` which is supposedly deprecated, or I am confused.

5b) There is a section about HIP-clang, in pre-build binaries, but actually there are no instructions how to install them and verify they work.

6) Document assumes familiarity with CUDA, but why assume that?


Document should be totally reworked, or written from scratch. It should have:

1) Premise (max 3 paragraphs what HIP is).

2) Installation and how to check it is installed. (max 4-5 paragraphs). Don't link to other documents, tell which package to install and how to test it. Assume basic ROCm stuff is already installed. The package dependencies should do the rest anyway.

3) Minimal example (initialization, memory allocation, launching kernel, some minimal synchronization) sample C++ code in a single file (max 25 lines), and exact command line to compile, link and run it. No references to external github directories, Makefiles or other complex build mechanisms. I should just copy paste it, and run.

4) More advanced topics overview (i.e. debugging, compiling for multiple GPUs, link to a reference manual with all hip library constructs).

5) Link to separate article on porting tools and porting methods for CUDA code to HIP.

Please give this task to a good technical writer, because right now I don't know what this document is even trying to achieve. It feels more like a marketing material, than actual something that an engineer or software developer would use.
