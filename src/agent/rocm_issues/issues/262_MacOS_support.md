# MacOS support

> **Issue #262**
> **状态**: closed
> **创建时间**: 2017-11-25T04:33:24Z
> **更新时间**: 2021-12-25T22:45:04Z
> **关闭时间**: 2020-12-16T12:20:07Z
> **作者**: dmayle
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/262

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Is there a timeline for RocM on MacOS?

---

## 评论 (87 条)

### 评论 #1 — smithakihide (2017-11-27T14:10:05Z)

I think there is no.
ROCm is based on customized linux kernel. so there is no compatibility with Unix kernel.

---

### 评论 #2 — gstoner (2017-11-27T14:17:14Z)

Right now we need a way to port the ROCm tools to the Mac, which means exposed driver API and also LLVM IR interface,  AIR could be the path to get our compiler to work, but better would be the support of our standardized loader interface so we could also support Assembly.  This would be dependent on Apple tools team for the latter. 

---

### 评论 #3 — oscarbg (2017-11-30T12:12:18Z)

+1

Would be nice to expose ROCM i.e. improved compute on Macos right now OpenCL 1.2 for too many years while Nvidia supports CUDA..
seems Nvidia supports CUDA (even lastests features like "unified mem").. it just keeps releasing new CUDA releases and seems it works without Apple involvement.. couldn't AMD do the same with some ROCM.kext kernel driver extension similar to CUDA.kext?
just asking, no pressure..

---

### 评论 #4 — hery (2018-10-12T15:28:40Z)

Hola! Just double-checking things here. Is it possible at all to get ROCm working for a Docker container running on macOS? Or can the ROC kernel not work that way?

---

### 评论 #5 — lambdaupb (2018-10-26T18:17:49Z)

@hery Docker on macOS is run in a virtual machine. Since the radeon GPUs used in macs are used by the main OS and Hypervisor.framework does not support PCIe passthrough, Docker probably does not change the situation.

---

### 评论 #6 — leedrake5 (2019-01-04T01:40:37Z)

Just wanted to leave a vote here for a Mac version. Thanks for your efforts to make AMD GPUs work for deep learning. 

---

### 评论 #7 — OAKOAITE (2019-01-04T03:22:47Z)

I vote for this too! Mac devices should have more GPU support like Windows does.

---

### 评论 #8 — MatthewWaller (2019-01-05T18:58:51Z)

Hello! I would like to throw in my request for a Mac version as well!

---

### 评论 #9 — leedrake5 (2019-01-05T19:36:52Z)

If you've come to this page looking for a Mac version, just keep commenting and leaving a vote. Don't know if it will change anything, but at least the developers will have a sense that demand is real. Though I also think Apple needs to step up and dedicate resources if they are going to stick with AMD. 

---

### 评论 #10 — gentlesystems (2019-01-05T23:39:38Z)

I've been watching this issue for a while.  Now I'm wondering if there's anything we can do to help make this happen.  The kernel code is more extensive than I would have expected.

---

### 评论 #11 — allenfrostline (2019-01-07T07:14:14Z)

Still no progress? I thought it'd be an urgent issue and solved at least months ago...

---

### 评论 #12 — yash-s20 (2019-01-07T07:29:18Z)

Leaving a vote, it's a surprise it hasn't happened yet, considering we don't have a choice on the GPU on the Mac

---

### 评论 #13 — hery (2019-01-07T10:17:54Z)

I ended up getting an Nvidia GPU. I feel like even if AMD makes decent GPU, the software stack is just so far behind.

---

### 评论 #14 — nehbit (2019-01-18T09:33:16Z)

Yet another request for Mac OS. It doesn't have to be native, if you guys can get it to work in such a way that I can run it in a VirtualBox Linux VM, that would be just fine, too. 

---

### 评论 #15 — ai-smith (2019-01-24T21:15:08Z)

It is simply a sin not to make support on mac os.

---

### 评论 #16 — Arthur77Wang (2019-02-11T02:03:29Z)

Please do something for mac os support. Don't think it's such a complex staff to cover UNIX as LINUX support finished.

---

### 评论 #17 — mgbvox (2019-02-13T19:57:35Z)

One more request for Mac OS Support. Please. How is this not a chief commercial concern?

---

### 评论 #18 — farleylai (2019-02-13T20:29:30Z)

Apple is embracing AMD GPUs. The lack of support for macOS would be a pity. Two years are long enough for PyTorch to grow mature towards production. Though compilation from source is required for PyTorch to support nvidia GPUs on macOS, it's definitely working. So what's actually going on with ROCm? At least in the aspect of driver release, it should be easier for AMD GPUs compared with [nvidia's](https://www.forbes.com/sites/marcochiappetta/2018/12/11/apple-turns-its-back-on-customers-and-nvidia-with-macos-mojave/#e0c429037e9f).



---

### 评论 #19 — aleh-null (2019-02-16T11:06:35Z)

Really surprised that it is like this. Plz do something, support Mac. 

---

### 评论 #20 — bkozik (2019-02-23T01:58:26Z)

+1 to macOS support, especially because Nvidia can't even work with Mojave.

---

### 评论 #21 — marcjones-io (2019-03-02T14:13:41Z)

Hi 👋🏽 +1 over here on the MacOs support. Would be dreamy to accomplish all the tasks on one machine. 

---

### 评论 #22 — plattenschieber (2019-03-03T16:38:29Z)

Same here 👋 

---

### 评论 #23 — iseanstevens (2019-03-07T02:45:33Z)

Same here - I upgraded to a new MacBook pro with a vega56 as an eGPU and it's great but I'd love to be able to proudly exclaim how awesome it is by making some kick ass art-robots which currently are going to use an nVidia box. 

---

### 评论 #24 — Degerz (2019-03-12T00:33:46Z)

Why is this issue still even open ? It's in Apple's full responsibility to maintain their compute stack so the people in this issue need to contact Apple instead to get a meaningful response from them ... 

For any of you guys that are interested in machine learning, why not ask for a single source C++ compute API like CUDA, HCC, SYCL from Apple because their Metal API is total junk ?

---

### 评论 #25 — gentlesystems (2019-03-19T16:24:21Z)

The recent response from Degerz is unhelpful, and, in fact, highlights the disparity between the support from Nvidia and AMD.  Nvidia’s Cuda has taken over the industry and driven much of this kind of work away from AMD products, even where good hardware and APIs are available from AMD and competitors.  Nvidia continues to supply drivers for their video cards on Mac, as well as Cuda and OpenCL stacks, despite a lack of support and cooperation from Apple.  Meanwhile, Apples supplies AMD drivers and puts AMD cards in all of their products, but drivers and support from AMD themselves is starkly missing.

I realize that this Issue is unlikely to be resolved with anything other than a "won't fix" because ROCm so depends so much on its custom linux kernel, and Mac support would require a new effort to integrate with Mac.  However, Nvidia has already done this type of work and more.  Nvidia products are the biggest reason this project will fail or succeed, as they continually drive the parallel compute industry.  Apple is just a platform.  Negativity toward them or their APIs isn't very productive.

---

### 评论 #26 — Degerz (2019-03-21T20:06:37Z)

> The recent response from Degerz is unhelpful, and, in fact, highlights the disparity between the support from Nvidia and AMD.

> Nvidia products are the biggest reason this project will fail or succeed, as they continually drive the parallel compute industry. Apple is just a platform. Negativity toward them or their APIs isn't very productive.

No, what's unhelpful are posts like yours in being complacent on accepting mediocrity from Apple and you can kiss goodbye to CUDA support on macOS starting from macOS Mojave so it's high time that you along with the others start holding Apple responsible for their subpar compute stack! 

It's exactly as you said, Apple are the ones who provide the drivers so they better damn well provide drivers adequate for machine learning or other high-end compute applications ... 

Demanding that AMD support a platform that they have no control whatsoever is not at all productive in any form and all the work that Nvidia has tried to bypass the macOS kernel has already been dropped. The fundamental issue with Apple's Metal API is that it's **_NOT_ single source** like CUDA or HIP but despite that design flaw AMD will gladly use Metal for some of their projects, however it'll never become a viable option for machine learning. It's amazing that you're quick to point out AMD's failings but will ignore Apple making the very same mistake twice already once with OpenCL and another with Metal both of which are designed as separate source ... 

How do you expect the community to cope with a useless tool ? 

---

### 评论 #27 — hmmmph (2019-04-09T10:00:54Z)

 Contrary to the complete rubbish the previous commenter spewed, `Apple` nor the Metal API is to blame (in case you didn't know, [OS X is opensource](https://opensource.apple.com)). 

There are many other projects that were once exclusive to `CUDA` that support `OpenCL`/`AMD` GPU's on macOS now (eg. hashcat). The lack of a macOS compatible tensorflow-rocm is more likely simply not where the developer's priorities are atm. `AMD` has a [portal](https://amd-osx.com) and [community](https://forum.amd-osx.com) exclusively dedicated to `OS X`, maybe put in a request over there perhaps — that's why it exists.

---

### 评论 #28 — Degerz (2019-04-09T18:42:17Z)

> AMD has a portal and community exclusively dedicated to OS X, maybe put in a request over there perhaps — that's why it exists.

"**AMD OS X is in no way affiliated with © Advanced Micro Devices Inc**, © Apple Inc or any of their subsidiaries. **All opinions and reviews are our own.**"

This is why no one takes the Apple community seriously ... 

> Apple nor the Metal API is to blame (in case you didn't know, OS X is opensource).

Too bad they didn't open source where it actually mattered which was their graphics/compute stack and Metal API is indeed to blame since it's not single source ... 

> There are many other projects that were once exclusive to CUDA that support OpenCL/AMD GPU's on macOS now (eg. hashcat). 

And their still exclusive to CUDA to this very day! Consider OpenCL as effectively deprecated with no future. There's no future in compute either on Windows or macOS ...

> The lack of a macOS compatible tensorflow-rocm is more likely simply not where the developer's priorities are atm.

You must be very naive behind the reasons as to why ROCm exists in the first place ...

---

### 评论 #29 — gbrow004 (2019-04-17T18:06:22Z)

Another +1 for MacOS support, even if we have to compile from source (I'm looking at you PyTorch with GPU support for MacOS!).

---

### 评论 #30 — maddyscientist (2019-06-07T20:26:13Z)

With the recent announcement of the new Mac Pros with up to 4x Vega 7s in them, which would be a dream ROCm workstation, have there been any plans made yet to address ROCm on Mac yet?

---

### 评论 #31 — Degerz (2019-06-08T04:52:00Z)

@maddyscientist Don't ask AMD ? Go ask Apple instead and ask them when they're going to support a single-source programming model ? 

If your interest like everyone else in here is in machine learning frameworks such as Tensorflow, PyTorch, etc then ROCm only works because it's APIs support template kernels/shaders ... 

No matter how many people ask AMD or plead for them to bring over ROCm to MacOS, it'll never happen because Apple only wants to support inferior programming models ... 

---

### 评论 #32 — maddyscientist (2019-06-08T05:58:33Z)

@Degerz so how come CUDA works on Mac but not ROCm?

---

### 评论 #33 — Degerz (2019-06-08T06:40:25Z)

@maddyscientist Not anymore it doesn't starting from macOS version 10.14. There's going to be no more CUDA support starting on Mojave and subsequently no CUDA as well on Catalina ... 

Again, no single-source programming model means no advanced machine learning frameworks like Tensorflow or PyTorch ... 

You can tell there's an echochamber in here from people not willing to admit that what Apple are doing with their Metal API is total rubbish. They should give Metal the ability to do templated kernels/shaders or they can get get lost ... 

Metal = pile of hot junk :wink:

---

### 评论 #34 — ThoreauHenry (2019-06-24T12:35:48Z)

On the practical/linux side of things, it's either integrated into the newest kernel or inserted as a dkms module into the kernel at runtime.  If Apple's Mach kernel disallows that, it will be impossible to run.  OS X is not open source.  The freebsd kernel they swiped is closed source.  You need Apple's keys and/or permission to access it.

If Apple wanted ROCm implemented, it could be done in a month with the code here that is freely available.  But they don't want to.  From their recent announcements they are going to reinvent the wheel with metal.  

And I understand why, because it must integrate with their kernel, which is in fact a vertical/closed package.  So they literally have to do it themselves unless NDA's/permission are granted to an outside vendor, as was done with Nvidia(for a short time).  I'm sure Apple will be releasing some kind of compute layer shortly with metal.  I just doubt it'll be called ROCm.  And yes, that new Navi gpu is an amazing piece of hardware.  I would be shocked if they didn't support compute on that crazy overpowered card.  

If they are charging $1000 for a monitor stand, the least they can do is let you use your own gpu for compute tasks.

---

### 评论 #35 — Degerz (2019-06-26T15:36:17Z)

They won't because Apple only intends for Metal to be a gfx API and even then it's missing tons of features. Literally, every time some developer uses it beyond games it fails pretty hard and miserably at that ... 

From [years](https://forums.developer.apple.com/thread/8359) on since it's release, a former AMD employee has made the [same](https://github.com/ROCm-Developer-Tools/HIP/issues/150#issuecomment-321272082) complaint. There are currently ZERO and EXACTLY ZERO ways to be able to do CUDA-style templates on Apple systems currently since Metal is a dumpster fire of a compute API. If Metal actually had the ability to execute CUDA-style templates then having CUDA or ROCm on their platforms would become redundant and any serious professionals with Apple cash wouldn't care but this is not the case so here we are where we have people who guilty of putting up with an inferior programming model from Apple ... 

Metal is just another abomination to ML framework specialists and unless somebody [demands](https://forums.developer.apple.com/thread/118774) that Apple support a single-source programming model like CUDA then nothing will change ... 

---

### 评论 #36 — gy2256 (2019-06-27T10:17:32Z)

Currently, one solution to do deep learning on a Mac with external AMD GPU is to use PlaidML, which supports Keras. I have successfully tested it with an external RX580 GPU. 

It might also be possible to add support to TensorFlow 2.0, as shown in the comment: [Plaidml_issue_281](https://github.com/plaidml/plaidml/issues/281#issuecomment-478260583). 

The PlaidML supports Metal or OpenCL as backend. That being said, it will be exciting if ROCm can support Mac OS as well, so there will be more options. Especially after the release of Apple cheese grater.  


 

---

### 评论 #37 — lericson (2019-07-01T12:15:51Z)

+1 for AMD GPGPU support, I don't really care if it's ROCm or HIP. Just let me write GPU-accelerated programs like CUDA does. This is a problem with lack of vision from both Apple with its shader file approach in the Metal API, and a from AMD with having ROCm be tied to Linux.

---

### 评论 #38 — lericson (2019-07-01T12:19:18Z)

@paradox56 The acceleration in PlaidML works by reverting to graphics-based approaches from yesteryear. It is really rather a sad testament that it is easier to regress to previous techniques than to get AMD/Apple on the same page in this.

---

### 评论 #39 — boozook (2019-07-24T19:34:54Z)

I just found 

> A MTLComputePipelineState object represents a compute processing pipeline. Unlike a graphics rendering pipeline, you can create a MTLComputePipelineState object with a single kernel function, without using a pipeline descriptor.

https://developer.apple.com/documentation/metal/hello_compute

---

### 评论 #40 — lericson (2019-07-24T20:10:38Z)

It is not single-source, and the API is ridiculously complex to call a single function, sadly. 

- Ludvig

> On 24 Jul 2019, at 21:35, Alexander Koz. <notifications@github.com> wrote:
> 
> I just found
> 
> A MTLComputePipelineState object represents a compute processing pipeline. Unlike a graphics rendering pipeline, you can create a MTLComputePipelineState object with a single kernel function, without using a pipeline descriptor.
> 
> https://developer.apple.com/documentation/metal/hello_compute
> 
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub, or mute the thread.


---

### 评论 #41 — leedrake5 (2019-07-24T20:12:25Z)

> @paradox56 The acceleration in PlaidML works by reverting to graphics-based approaches from yesteryear. It is really rather a sad testament that it is easier to regress to previous techniques than to get AMD/Apple on the same page in this.

This is true, but having worked with CUDA on a Linux system, the plaidml framework has been much more stable and easier to use. It regulates itself far better with available RAM, as one example. It is frustrating to think of the lost potential here.

---

### 评论 #42 — Aeroxander (2019-08-22T04:34:05Z)

The TVM deep learning compiler stack should also have Metal support, PlaidML doesn't have support for every type of operator yet (or at least not for my more advanced model, normal ones should work)

---

### 评论 #43 — kenthinson (2019-08-30T04:19:23Z)

Everyone should ask Apple to implement the drivers changes to make ROCm possible on osx. Send them feedback. I will be doing so also.

https://www.apple.com/feedback/macos.html

---

### 评论 #44 — songololo (2019-10-01T10:38:01Z)

@kenthinson that or find a journalist to investigate and publish whether Apple develops their ML using non-apple workflows...!

---

### 评论 #45 — Degerz (2019-11-25T00:41:00Z)

It's finally [official](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#title-new-features), Nvidia will drop CUDA support for macOS (not that it mattered since Mojave) after release 10.2 and no amount of shouting or screaming at AMD will reverse this decision since they were never at fault to begin with like some people here seem to have implied ... :sunglasses:

Their trash Metal API will have to meet these 3 demands to be even considered again or else ... 

1. Single-source programming model 
2. Support for templated kernels and other common C++ features found in CUDA/HIP
3. Support for an offline compilation model

Until these demands are met by Apple their Metal API will be straight garbage. Even Intel with their oneAPI compute stack and their DPC++ API is a better idea than Metal which shows just how pathetic Apple's support has been thus far for this community ...

---

### 评论 #46 — leedrake5 (2019-11-25T03:08:20Z)

Looks like [PlaidML](https://github.com/plaidml/plaidml) is the only viable option moving forward

---

### 评论 #47 — mirh (2019-11-25T08:28:23Z)

Plaid is a "program". You'll mean opencl as the equivalent api to rocm, for eventually talking with the gpu.
But that's already been deprecated last year (in addition to being too old to support everything the hardware has), bets are taken on when it will be removed too. 

---

### 评论 #48 — leedrake5 (2019-11-25T11:54:21Z)

PlaidML works with metal too. So I don’t anticipate any problems. Because it is a program, it is a little more robust to Apple’s baffling decisions. I don’t know how well it will Leah with Keras now that it is integrated within tensorflow in v2.

---

### 评论 #49 — bofeizhu (2019-11-25T17:32:30Z)

@Degerz Will MLIR make any difference in the future?

---

### 评论 #50 — Degerz (2019-11-26T03:33:41Z)

@bofeizhu Unfortunately, I don't think MLIR is going to help with the situation on macOS all that much. It looks to be an even higher level IR than SPIR-V! SPIR-V compute shaders in Vulkan as it is have too many limitations for targeting advanced machine learning frameworks like Tensorflow or PyTorch so MLIR targeting SPIR-V won't end well IMO ... 

My main motivation behind demanding an offline compilation model for Metal (or any other API really) is because nobody wants to deal with the weaknesses of high-level abstractions such as SPIR-V or MSL (Metal Shading Language). An offline compilation model would offer us more powerful programming features to enable more complex frameworks like machine learning and more powerful  lower level optimizations ... 

Currently today, shading languages/bytecode aren't very powerful abstractions of the hardware we use. CUDA proves that having a less portable standard is a more powerful tool and the industry is slowly starting to acknowledge this in the current ecosystem ... 

CUDA kernel language -> PTX ISA -> SASS (Nvidia)
DPC++ kernel language -> GEN ISA (Intel)
HIP kernel language -> GCN ISA (AMD) 

Apple like with the above standards should embrace CUDA's programming/compilation model rather than Direct3D or Vulkan's programming/compilation model with the Metal API if they want to have any chance of success with complex machine learning frameworks. MSL is unacceptable as it is but if Apple doesn't want an offline compilation model for portability reasons then they should at least give us something lower level like a virtual ISA such as PTX because things can't keep going on like this ... 

---

### 评论 #51 — bofeizhu (2019-11-26T03:43:07Z)

@Degerz Correct me if I’m wrong, but I think MLIR is supposed to be working with Swift for Tensorflow. And we can use Swift to write every layer of the deep learning stack and compile them directly to hardware.

---

### 评论 #52 — Degerz (2019-11-26T06:53:26Z)

@bofeizhu Think of it like this ... 

MLIR uses a source language as an input (such as Swift as you mentioned) as the **front-end** for the intermediate representation and then compiles it into the target back-end intermediate representation or native ISA (like PTX or GCN ISA) ... (following example)

Swift source language -> (source-to-IR compiler) -> MLIR -> (IR-to-IR/ISA compiler) -> PTX ISA
Input source language -> (front-end compiler) -> MLIR -> (back-end compiler) -> hardware IR/ISA

MLIR is just simply another layer in the compilation process. IMO the biggest hurdle to Tensorflow support on macOS/Metal isn't going to be the source language or the higher level IR but it's going to be the back-end IR/ISA ... 

Right now we can't just simply use the Metal Shading Language to support the full featured Tensorflow framework because it doesn't have enough features. At best it's only good enough for Tensorflow Lite and it's the same story with SPIR-V ... 

We need a lower level target from Apple to be able to have Tensorflow use the Metal API. If we had access to some sort of virtual ISA like PTX or even a native ISA like GCN bytecode in Metal API then we could just start porting existing CUDA/HIP kernels by writing custom hand optimized Metal shaders with assembly code instead of only using the high level MSL source which is not nearly as powerful or featured compared to the assembly language ... 

The biggest gripe with the Metal API is that it's not nearly low level enough compared to CUDA in which you can write kernels using Nvidia's assembly language for their GPUs known as PTX or with HIP in AMD's case you can write HIP kernels using GCN assembly! Where is Metal's equivalent to PTX or GCN ISA in Apple's case ?  

---

### 评论 #53 — ayushnvijay (2019-12-05T07:27:19Z)

Has anyone tried using Parallels desktop with Ubuntu to make this work? Or nGraph + PlaidML to use tensorflow on AMD Gpu?

---

### 评论 #54 — mk2016a (2020-01-08T06:00:11Z)

It is not a problem with apple.
Apple now has its Creative ML which is easy for app developer to use.
Even the cuda support old Mac system.
How could AMD be so much worse ?
I think Apple should not use AMD graphics card at all.
Price of a Mac is far more enough for them to Nvidia's best graphics cards.
Because of the lower cost of its product, now we can only use stupid AMD's graphic card with almost no support at all.

Apple should not use amd.
As long as apple using amd's graphics card, we will never buy any apple computer again.
Things like this, really stupid and Apple is no longer the old Apple any more.

---

### 评论 #55 — Nevensky (2020-03-03T18:31:23Z)

vote up for adding mac support

---

### 评论 #56 — zhiyuanzhai (2020-03-21T09:22:12Z)

+1. We want Radeon Open Compute for Mac!
Now I have to install an Arch Linux system on my MacBook Pro, which means a huge amount of extra work to do.

---

### 评论 #57 — jjbeto (2020-05-14T22:27:30Z)

vote up for adding mac support

---

### 评论 #58 — ugahugo (2020-05-15T13:18:17Z)

It will never happen. The original team didn't introduce nor HAL, nor other critical components in order to introduce new OS support at any point in the future.

---

### 评论 #59 — MirrMurr (2020-05-26T22:16:38Z)

Still holding up and staying in the line for Mac support!

I'm also interested in whether it has more chance of this Mac support happening, or rather buy an Nvidia eGPU. What is your advice? Any comment is welcome!

(I'm a computer scientist student studying Deep Learning, using MBP 15", yet no use of the Radeon Pro inside.....)

---

### 评论 #60 — ugahugo (2020-05-26T23:17:08Z)

> Still holding up and staying in the line for Mac support!
> 
> I'm also interested in whether it has more chance of this Mac support happening, or rather buy an Nvidia eGPU. What is your advice? Any comment is welcome!
> 
> (I'm a computer scientist student studying Deep Learning, using MBP 15", yet no use of the Radeon Pro inside.....)

Nvidia drivers support was canceled for past major MAC OS updates, so no Nvidia eGPU support for you, unless you roll back your Apple product to the older OS versions (which is a big pain in the ass considering other apps support for old MAC OS versions). 

Welcome to hell.

---

### 评论 #61 — MirrMurr (2020-05-27T07:34:15Z)

> > Still holding up and staying in the line for Mac support!
> > I'm also interested in whether it has more chance of this Mac support happening, or rather buy an Nvidia eGPU. What is your advice? Any comment is welcome!
> > (I'm a computer scientist student studying Deep Learning, using MBP 15", yet no use of the Radeon Pro inside.....)
> 
> Nvidia drivers support was canceled for past major MAC OS updates, so no Nvidia eGPU support for you, unless you roll back your Apple product to the older OS versions (which is a big pain in the ass considering other apps support for old MAC OS versions).
> 
> Welcome to hell.

Thank you for replying! 

Wow, this is really an eye opening inconvenience.. I guess stick to Google Colab and pray for PlaidML or Apple or some god. Until then, maybe spin up an Ubuntu machine.

---

### 评论 #62 — ChristianLagares (2020-06-16T18:56:01Z)

Yet another vote for a MacOS port. This would enable not only ML workloads to be accelerated, but also many other HPC-related workloads to _at least_ compile natively on MacOS. Apple has recently shown its commit for Radeon with the introduction of the 5600M with HBM2. I do understand a significant amount of work would be required, but the payoff of enabling a large amount of workloads seems to outweigh the initial effort. 

---

### 评论 #63 — Gerzer (2020-06-16T23:46:22Z)

Please do port ROCm to Metal on macOS! There's a huge demand for that.

---

### 评论 #64 — mk2016a (2020-06-17T01:03:48Z)

Forget it. No company would like to corperate with ATI. That is why they went bankrupt.

---

### 评论 #65 — Nevensky (2020-07-13T12:06:07Z)

I wish to throw my ball in this game as well, please port the Rocm to MacOS / Metal.

---

### 评论 #66 — xyzus (2020-07-14T04:49:00Z)

please do port RocM on MacOS

---

### 评论 #67 — anmolresourceone (2020-07-20T16:44:41Z)

much needed

---

### 评论 #68 — greenstick (2020-09-18T01:53:07Z)

Still dreaming about this by night and living the nightmare of no MacOS support by day. 

---

### 评论 #69 — Filco306 (2020-09-27T17:15:49Z)

Would a reasonable workaround be to partition one's disk and install Ubuntu? Would that enable the use of one's graphic's card? 

---

### 评论 #70 — gbrow004 (2020-09-27T17:21:56Z)

> Would a reasonable workaround be to partition one's disk and install Ubuntu? Would that enable the use of one's graphic's card?

Yes, but installing Ubuntu on Macs that have the T2 security chip (2018 and later) can be troublesome. You can try my guide to start out:
https://gist.github.com/gbrow004/096f845c8fe8d03ef9009fbb87b781a4

---

### 评论 #71 — Filco306 (2020-09-27T18:40:16Z)

Thank you @gbrow004 , I will check it out! 

---

### 评论 #72 — sbetko (2020-11-10T22:50:32Z)

Leaving my vote. With AMD being the sole third party dedicated GPU option on MacOS, ROCm support seems like a no-brainer. Please make this happen!

---

### 评论 #73 — ugahugo (2020-11-10T23:04:29Z)

@gstoner, 

Do you see this? Hundreds of people voted for make damn Windows / Mac OS X support, not for useless Linux. This is what should be done from the very beginning!

This is late 2020 and NOTHING happened. The Radeon team just releases the code for themselves, no one is interested in shitty Linux because no one uses it!  

---

### 评论 #74 — egorgam (2020-11-18T00:02:23Z)

How I understand a situation, it must be some kernel patches for use RoCM on linux (what is unreal wit proprietary Darwin kernel) but MacOS docker (and hypervisors) implementation can't passtrough PCI devices (as discrete GPU). So where is any possible way for AMD developers to resolve a problem?

---

### 评论 #75 — ChristianLagares (2020-11-19T22:12:00Z)

And you are right, @egorgam . However, many other API's have successfully been ported to run atop Metal. For instance, MoltenGL provides OpenGL ES 2.0 over Metal. Metal already provides a low-latency, API that could be targeted. I'm fairly confident that a large portion of the ROCm Core could be ported to run over Metal which would provide a Native platform. Not to mention, AMD would incentivize developer investment. 

I have to disagree with @ugahugo. AMD did the right move by bringing Linux into the play. For ROCm to succeed, they needed to appeal the HPC market, but their greatest mistake was to relinquish ROCm to being a niche development platform more or less exclusive to Linux. For instance, CUDA's greatest success comes from targeting every Nvidia GPU. AMD has a massive consumer and prosumer marker that they are not aggressively targeting by not porting ROCm. I do believe that even the development effort required for ROCm over Metal would render their codebase much more robust and mature enough to target newer platforms. They already have HIP. Why not add Metal as a backend? I have a Radeon Pro 5600M that I can only target through Metal (which is painful to target from C++ or Python) or OpenCL (relegated to 1.0). Apple recently published TensorFlow running on ML Compute. Why would AMD lose a marketing opportunity to bring ROCm over Metal which could potentially pave the way to ROCm over DirectCompute. This would enable fully portable AMD GPU compute shaders. 

---

### 评论 #76 — egorgam (2020-11-20T04:38:25Z)

@ChristianLagares wow! https://github.com/apple/tensorflow_macos/issues/7#issuecomment-730073221 look like it works with radeon pro)

---

### 评论 #77 — ugahugo (2020-11-22T18:34:36Z)

> I have to disagree with @ugahugo. AMD did the right move by bringing Linux into the play. For ROCm to succeed, they needed to appeal the HPC market, but their greatest mistake was to relinquish ROCm to being a niche development platform more or less exclusive to Linux.

>I have to disagree

>but their greatest mistake was to relinquish ROCm to being a niche development platform more or less exclusive to Linux

nuff said... //from authors of "the negative growth", masters of confusing speech and word manipulations

btw, @ChristianLagares, how many real products (that customers use) did you roll-out? Is it your bias among the Linux OS speaking or is it a real request? If yes, please refer to the products you work on, not the research you will share with how many? 10-50-100 other researchers...? Because we do a real product and we put this request YEARS AGO and argued everything a hundred times at least!

Since then, nothing happened for the №1 (Windows) and №2 (Mac OS X) popular operating systems, just f. NOTHING! 

Now, with new Apple hardware product releases, with its own silicons embedded, what AMD Radeon software development unit wants to target? Its own employee office PCs? Linux-based, I believe

Vergüenza as is

---

### 评论 #78 — zhiyuanzhai (2020-11-23T11:04:46Z)

@ugahugo It's clear that ROCm is aimed at High Performance Computing, which is mostly applied on clusters, servers, supercomputers or workstations, rather than a desktop or laptop PC. In those systems, Linux is undoubtedly the most popular OS, thus Linux has to be focused on. Actually the most recommended OS for CUDA from NVidia is also Ubuntu Linux. It makes sense if AMD would like to apply ROCm to Linux first.

Now we are just waiting to see if AMD has the plan to bring ROCm to other OSs like macOS or Windows after ROCm is mature enough on Linux.

---

### 评论 #79 — ugahugo (2020-11-23T13:16:30Z)

@zhiyuanzhai, Do you know that with modern GPU there is no such thing as a supercomputer market? That modern laptops, gaming laptops are far more advanced than you had in your mind by calling as "workstations"? I mean, the addressable market is huge, far bigger than the traditional supercomputer market you mentioned. 

Watching the Radeon unit fan zone explaining why the Radeon unit shot themselves into the leg by targeting a tiny market looks really bad! 

Why Nvidia did everything perfectly? Once and everything, and for everyone? What's the purpose of limiting something? What's the purpose of avoiding the C++ support in Windows and Mac OS X in 2020? I see the only reason is bad management and lack of skills in code development, and I am not sorry for that because it's not my problem but AMD's... 

I really don't understand two things in this topic (and others in ROCm githubs): 

1. Why people are trying to protect AMD's when they obviously failed alone (I didn't help them to fail, nor did any of you)

2. And why AMD continuously closing all the issues related to other OS support, providing 0 amount of information on plans and progress while the community just literally demanded this by hundreds of votes?! I just can't stand that behavior!

I see the behavior for such a huge corporation as AMD / Radeon just unacceptable. They chose to mute these problems, ignore the elephants in the room, they chose to avoid the problem. 

Do they think this problem will be gone if they just ignore it? I don't have anything to say to them, Vergüenza as is

---

### 评论 #80 — mirh (2020-11-23T22:21:59Z)

> What's the purpose of limiting something?

Idk, if you really cared about arbitrary limitations you shouldn't be using apple products I guess. 
Anyway, just for the records, with the release of ROCclr I believe HIP/rocm should be very near (if it isn't already?) to running on Windows. 

---

### 评论 #81 — ROCmSupport (2020-12-16T12:20:07Z)

Currently we are not supporting MacOS with ROCm.
We will share an update once we have plans to support in future.
Thank you.

---

### 评论 #82 — leedrake5 (2021-01-01T20:43:36Z)

Hi all,

Good news, Apple has released a version of tensorflow that can use AMD GPUs. See it [here](https://github.com/apple/tensorflow_macos).

---

### 评论 #83 — ugahugo (2021-01-01T21:14:34Z)

> Hi all,
> 
> Good news, Apple has released a version of tensorflow that can use AMD GPUs. See it [here](https://github.com/apple/tensorflow_macos).

What is the point to post this here? It's not related to the ROCm. More of that, having the TensorFlow library compiled for Mac OS X isn't the big deal. Also, the GPU acceleration for the case of M1 will be just really low comparing with PC 

---

### 评论 #84 — martinezhermes (2021-01-01T21:30:15Z)

> > Hi all,
> > Good news, Apple has released a version of tensorflow that can use AMD GPUs. See it [here](https://github.com/apple/tensorflow_macos).
> 
> What is the point to post this here? It's not related to the ROCm. More of that, having the TensorFlow library compiled for Mac OS X isn't the big deal. Also, the GPU acceleration for the case of M1 will be just really low comparing with PC

I believe people that follow this issue here are looking for ways for using their AMD GPU for machine learning, what @leedrake5  has replied comes as the _only_ solution so far for this issue! yes, tensorflow_macos is not related to ROCm at all but it is in fact related to AMD GPU cards in Mac computers. I’ve been testing it for the past 3 weeks and the performance is getting there, it is almost as fast as my ROCm setup using linux (with the same Mac) for both training and inference. 

I also believe ROCm on macOS is never gonna happen. I suggest people to follow the tensorflow development and post issues over there, hopefully pytorch and other libs will follow through, otherwise using Xcode Swift and PythonKit is also an option for machine learning projects with Mac computers that have AMD dedicated GPUs.

---

### 评论 #85 — greenstick (2021-01-04T19:35:16Z)

> > > Hi all,
> > > Good news, Apple has released a version of tensorflow that can use AMD GPUs. See it [here](https://github.com/apple/tensorflow_macos).
> > 
> > 
> > What is the point to post this here? It's not related to the ROCm. More of that, having the TensorFlow library compiled for Mac OS X isn't the big deal. Also, the GPU acceleration for the case of M1 will be just really low comparing with PC
> 
> I believe people that follow this issue here are looking for ways for using their AMD GPU for machine learning, what @leedrake5 has replied comes as the _only_ solution so far for this issue! yes, tensorflow_macos is not related to ROCm at all but it is in fact related to AMD GPU cards in Mac computers. I’ve been testing it for the past 3 weeks and the performance is getting there, it is almost as fast as my ROCm setup using linux (with the same Mac) for both training and inference.
> 
> I also believe ROCm on macOS is never gonna happen. I suggest people to follow the tensorflow development and post issues over there, hopefully pytorch and other libs will follow through, otherwise using Xcode Swift and PythonKit is also an option for machine learning projects with Mac computers that have AMD dedicated GPUs.

Sure, a lot (maybe even most) people are hoping for ROCm support on Mac so that they can use ML libraries, and in that respect the info provided by @leedrake5  is helpful. Let's be real, though –  tensorflow is _one library_ among _one use case_. Full ROCm support would allow developers to create their own libraries/applications that leverage their AMD GPU on their Mac – that's what I was after. I agree with you, ROCm for Mac will probably never happen, especially now that Apple's push towards SoCs with integrated GPUs on their laptop and desktop offerings (M1) is finally being rolled out in production, but your belief that people are following this issue because they're "looking for ways for using their AMD GPU for machine learning" is reductive. And even if that were the case, the idea that we should be satisfied now that tensorflow supports it (e.g. what about pytorch?) is wrongheaded. This is (...was *sigh*) bigger than a single library or use case; this was about supporting a platform. 

---

### 评论 #86 — zhiyuanzhai (2021-01-11T16:13:40Z)

In my perspective, Apple is unlikely to accept ROCm on Mac, for the same reason why Apple refused to support CUDA at the very beginning. It's not Apple's manner to rely on other manufacturers on such an important field as GPGPU.

It's becoming more and more clear that Apple is trying to push forward their own platform on GPU rendering and parallel computing, i.e., the Metal API.

---

### 评论 #87 — Crear12 (2021-12-25T22:45:04Z)

> 

With the promotion of Silicon platform, I think that this wish can never be realized.

---
