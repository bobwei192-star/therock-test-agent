# Which devices are even supported? (HIP/ROCm)

- **Issue #:** 1714
- **State:** closed
- **Created:** 2022-03-25T00:51:42Z
- **Updated:** 2024-02-13T19:20:22Z
- **URL:** https://github.com/ROCm/ROCm/issues/1714

I'm a long-time CUDA developer looking to explore ROCm and HIP development, but finding out which hardware even supports these tools is harder than it needs to be. 

Let's see... this repo's readme has a section on "Supported GPUs":

![Screenshot from 2022-03-24 17-23-25](https://user-images.githubusercontent.com/16393433/160030961-ffbcab77-76db-4194-97eb-6360219db7e5.png)

Okay, "extends" implies it supports other GPUs too-- which ones? Maybe the FAQ has more info:

![Screenshot from 2022-03-24 17-26-48](https://user-images.githubusercontent.com/16393433/160031097-ad6ec8d7-7830-4f66-86c3-3f6607bd3a9d.png)

Nope, it'll tell me all of the NVIDIA cards that work, but none of the AMD ones apparently. Okay, I guess I'll look at their HIP Programming Guide pdf. Skimming the table of contents, no indication of "supported GPUs"-- it's a 100 page document, surely they don't expect a user to read all of that to just see if a card works or not? Let's try searching instead:

CTRL+F "supported GPU": zero results
CTRL+F "supported platform": zero results
CTRL+F "supported device": zero results

okay..

CTRL+F "supported": 87 results, great. Going through them one by one, I guess. First 76 results unrelated, 77 is the closest thing I can find:

![Screenshot from 2022-03-24 17-35-47](https://user-images.githubusercontent.com/16393433/160031853-cd0a49a9-eda4-47b0-94f9-9890ee60cb5f.png)

This sounds sort of related to what I'm looking for, although it's deprecated, so the options for `gpu_arch` are probably out of date. I would like to know what HIP _currently_ supports, let's look at the option `--offload-arch=<target>` documentation:

![Screenshot from 2022-03-24 17-39-49](https://user-images.githubusercontent.com/16393433/160032193-0e1ce844-85e5-455d-87da-3206c017bc55.png)

Okay, the documentation doesn't actually explain anything at all, it just links to something. I might have wasted a lot of my time getting here, but finally, a link with an answer to my simple question:

https://clang.llvm.org/docs/ClangOffloadBundlerFileFormat.html#target-id

Ah, of course-- the link is also broken. Maybe try:

https://clang.llvm.org/docs/ClangOffloadBundlerFileFormat.html

No, also broken.

Forgive the sarcastic tone of this issue, but am I an idiot or is this documentation just abysmal?

If I want to know which NVIDIA GPUs support CUDA, and which features, all of that information is readily available in many places, e.g. 

https://developer.nvidia.com/cuda-gpus

I've been looking for an hour and found nothing official about the AMD support for HIP, so I quit. Hopefully creating a github issue will lead to an answer to this trivial question.