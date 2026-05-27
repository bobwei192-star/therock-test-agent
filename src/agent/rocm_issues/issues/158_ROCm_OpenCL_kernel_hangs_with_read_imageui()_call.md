# ROCm OpenCL: kernel hangs with read_imageui() call 

> **Issue #158**
> **状态**: closed
> **创建时间**: 2017-07-08T20:14:17Z
> **更新时间**: 2017-10-17T01:04:37Z
> **关闭时间**: 2017-10-17T01:04:36Z
> **作者**: boxerab
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/158

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

So, having some difficulties getting my kernels to run.

My program flow works like this:

1. map an opencl image, and create map completion event `MAP_COMPLETION_EVENT`
1. also unmap the same image, but the unmap call waits on user event `USER_EVENT`, and creates an unmap completion event `UNMAP_COMPLETION_EVENT`
1. when I receive the `MAP_COMPLETION_EVENT` event, copy data to mapped pointer and then set `USER_EVENT`
1. this will trigger the actual unmap, which will then set `UNMAP_COMPLETION_EVENT`
1. the kernel that uses the above image is enqueued but waits for `UNMAP_COMPLETION_EVENT`

I verified that I get as far as step 4 (the image is indeed unmapped and sends the event) but the kernel never actually runs.

What is best way of trouble shooting this ?


Also, I do enqueue a large number of kernels, but they will not run until they get their `UNMAP_COMPLETION_EVENT` events. 



---

## 评论 (51 条)

### 评论 #1 — boxerab (2017-07-08T20:44:49Z)

I realize it is a lot of work, but if someone could port all of the APP SDK examples to ROCm, it would be great. Then I could try some simple kernels with opencl images to isolate the problem. 

---

### 评论 #2 — gstoner (2017-07-08T23:10:18Z)

The old SDK is being Phased out. The Apps team is working on new SDK you can find it here   https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/releases 

Note app like Mixbench already work as well. 

---

### 评论 #3 — boxerab (2017-07-09T02:07:36Z)

Great, can't wait to try this out. Any ballpark ETA for the full release ? 

---

### 评论 #4 — boxerab (2017-07-09T18:42:15Z)

So, I got my kernels to run, but I had to remove one critical line in one kernel:

`read_imageui(......)`

Otherwise, runtime will hang. So, there seems to be a problem with reading OpenCL images.

Also, performance was low : about **4 X slower** than windows version (where I also remove the `read_imageui` call.






---

### 评论 #5 — boxerab (2017-07-10T01:37:28Z)

So, I have a reproducer for the kernel hang.
Who is the best person to email this code to ?

---

### 评论 #6 — nevion (2017-07-10T01:43:24Z)

@boxerab I'd say just attach it to a [gist](https://gist.github.com/) ~if it's a single file~.  Hopefully image calls get fixed soon along with the events - I get mixed results using images over plain old buffers but they definitely help in some cases.  Events though, I use those very heavily but I haven't tested on ROCm yet - are you only have problems with mapping events on images or any buffer type or event type?

---

### 评论 #7 — boxerab (2017-07-10T01:50:35Z)

In my reproducer, I don't use any events at all. Nor do I map. I only enqueue the kernel, then call clFinish. And clFinish never returns.

Since this is some of my production code, prefer to email directly to someone at AMD.

---

### 评论 #8 — boxerab (2017-07-10T01:52:27Z)

I use images quite heavily, and very happy with perf on windows.

---

### 评论 #9 — nevion (2017-07-10T01:52:34Z)

@boxerab I understand... and I'm often in that situation but I take it it's too complicated to boil down to the minimum?  It could speed up efforts on the other side...

---

### 评论 #10 — gstoner (2017-07-10T01:54:15Z)

I am going to have one my of staff contact you.   One thing be careful of out of bounds reference.   We now shutdown applications upon out of bounds. reference.



From Outlook for iOS<https://aka.ms/o0ukef>
____________



---

### 评论 #11 — boxerab (2017-07-10T01:54:37Z)

Yes. I have done a lot of boiling :) so it is pretty simple code. Nothing that earth-shattering, but still would like to send it directly to company.

---

### 评论 #12 — nevion (2017-07-10T01:54:41Z)

I guess what I meant with images vs buffers is I usually cache things to a local tile (I actually forget it's normal not to do this it's so common a technique in my arsonal), and then even blending it's competitive and more flexible with different operations.

---

### 评论 #13 — boxerab (2017-07-10T01:55:51Z)

Thanks, Greg. I do have bounds checking in the kernel. The problem goes away if I don't read from the input image, and I am pretty sure the input location is always in bounds, but I will double check.

---

### 评论 #14 — boxerab (2017-07-10T01:56:44Z)

@nevion can you elaborate ? caching to local tile ?

---

### 评论 #15 — nevion (2017-07-10T01:58:18Z)

@boxerab basically [item 4, step 1 - shared memory here](https://www.evl.uic.edu/sjames/cs525/final.html).  I first came to know of it from nvidia on how to convolve fast, [maybe this was it](http://www.nvidia.com/content/GTC/documents/1412_GTC09.pdf) - they regularly call the tile an apron, although it usually has a surrounding area, which is not always needed.

---

### 评论 #16 — boxerab (2017-07-10T01:58:40Z)

Yes, so even if I always pass in (0,0) as the source location when reading, I still get this problem.

---

### 评论 #17 — boxerab (2017-07-10T02:01:11Z)

OK, got it. In my case, this is a YBR colour transform, so no need for local mem.

---

### 评论 #18 — nevion (2017-07-10T02:04:16Z)

Hm.  Perhaps related - I've done it before for [fast, high quality debayering of images here](https://github.com/nevion/cldemosaic)

---

### 评论 #19 — boxerab (2017-07-10T02:05:59Z)

:) I forked your project a while back. Thanks for sharing this. Would like to play around with it at some point, just too many other things going on.

---

### 评论 #20 — gstoner (2017-07-10T02:31:31Z)

We we be releasing 1.6.1 which will have an OpenCL runtime update.   Note images are still being worked on we have not Shipped our final 1.0 release yet for OpenCL on ROCm


---

### 评论 #21 — boxerab (2017-07-11T20:00:24Z)

Great, looking forward to 1.6.1  Perhaps my problem is already fixed :)

---

### 评论 #22 — boxerab (2017-07-19T18:35:35Z)

Are you guys still interested in a reproducer for this ?

---

### 评论 #23 — gstoner (2017-07-19T19:33:46Z)

Yes.  so we can have unit test to make sure we fix and never show up again.

---

### 评论 #24 — boxerab (2017-07-19T19:46:29Z)

Sounds good - would you mind sending me a contact email @ AMD so I can send it over ? 

---

### 评论 #25 — boxerab (2017-07-22T11:06:35Z)

Great, just say the word and I will make it available :)

---

### 评论 #26 — boxerab (2017-07-22T13:28:09Z)

Sent. Thanks!

---

### 评论 #27 — gstoner (2017-07-23T01:01:17Z)

It has been integrated into our OpenCL Test Framework. 

---

### 评论 #28 — boxerab (2017-07-23T01:27:16Z)

Great. Is this fixed in 1.6.1 ?

---

### 评论 #29 — gstoner (2017-07-25T19:41:08Z)

We found the issue in the compiler, it did not make the ROCm 1.6.1 drop, but we get it into ROCm 1.6.2   -O1 did to work.  

---

### 评论 #30 — boxerab (2017-07-25T20:04:11Z)

Good to hear this, thanks !  Can I test 1.6.2 ?

---

### 评论 #31 — gstoner (2017-07-25T20:10:44Z)

We are working on it now, next Monday or Tuesday is the target.

Greg
On Jul 25, 2017, at 1:04 PM, Aaron Boxer <notifications@github.com<mailto:notifications@github.com>> wrote:


Good to hear this, thanks ! Can I test 1.6.2 ?

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/158#issuecomment-317855761>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuXU3r5jF40fcZzmvsHmEO1v3yjSBks5sRko-gaJpZM4OR2tm>.



---

### 评论 #32 — boxerab (2017-07-25T20:13:04Z)

Fantastic, thanks!

---

### 评论 #33 — boxerab (2017-07-26T18:44:52Z)

I upgraded to 1.6.1, disabled the problem read_imageui call that was causing the hang, and ran my kernels on both Ubuntu 16 with ROCm and Windows 10 with latest Catalyst driver.

Total time on ROCm was slightly slower than Catalyst, but CPU load was significantly lower - 65 % vs. 90.
Of course, the compilers are different, gcc vs msvc, but this looks promising.

Nice work, folks!  



---

### 评论 #34 — boxerab (2017-08-01T00:34:52Z)

So, is 1.6.2 out yet? 

---

### 评论 #35 — boxerab (2017-08-05T01:05:53Z)

Can't wait to try 1.6.2 ...... any ETA on when this will be available? 

---

### 评论 #36 — boxerab (2017-08-10T00:13:02Z)

Thanks. Is this fix available with apt update ? Because I just updated and the issue is still there, unfortunately. I did see the rocm updates.

---

### 评论 #37 — gstoner (2017-08-10T00:29:52Z)

We released 1.6.2 this week.  It might not have made to the cut off, let me check.      I have another release coming in next week. 

---

### 评论 #38 — boxerab (2017-08-10T00:37:32Z)

Thanks. I didn't see an update for opencl, perhaps it wasn't tagged for
release.

On Aug 9, 2017 8:29 PM, "Gregory Stoner" <notifications@github.com> wrote:

We released 1.6.2 this week. It might not have made to the cut off, let me
check. I have another release coming in next week.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub
<https://github.com/RadeonOpenCompute/ROCm/issues/158#issuecomment-321417384>,
or mute the thread
<https://github.com/notifications/unsubscribe-auth/AAF0ocAcWmFDxE8ou72VZIXp0elWtlOdks5sWk8AgaJpZM4OR2tm>
.


---

### 评论 #39 — boxerab (2017-08-11T15:50:38Z)

Any update on this? I am happy to build it myself, but there isn't enough information on the opencl runtime github site to show how to do this.

---

### 评论 #40 — nevion (2017-08-11T20:11:14Z)

@boxerab I share your desire to learn how to build that runtime and where to even change the code.  It's an opensource mystery.

---

### 评论 #41 — gstoner (2017-08-11T23:24:45Z)

We updating the build process to simplify it.   Remember we still in development on opencl on rocm

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Aaron Boxer <notifications@github.com>
Sent: Friday, August 11, 2017 10:50:39 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] ROCm OpenCL: kernel hangs with read_imageui() call (#158)


Any update on this? I am happy to build it myself, but there isn't enough information on the opencl runtime github site to show how to do this.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/158#issuecomment-321849729>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuY_HTxIiAlDtvayDeFzUc1aRihKpks5sXHhPgaJpZM4OR2tm>.


---

### 评论 #42 — boxerab (2017-08-23T03:52:43Z)

Is this fixed in 1.6.3 ?

---

### 评论 #43 — gstoner (2017-08-24T23:52:19Z)

It will come out in 1.6.4 

---

### 评论 #44 — briansp2020 (2017-08-25T00:56:40Z)

When is your target release date for 1.6.4? Do you plant to test it with Ubuntu 16.04.3?

---

### 评论 #45 — boxerab (2017-08-31T18:09:17Z)

Yes, also would like to know ETA for 1.6.4 . 

---

### 评论 #46 — boxerab (2017-09-06T12:49:32Z)

So, it looks like the latest release fixes this issue. Yay!!!!

---

### 评论 #47 — boxerab (2017-09-06T12:50:33Z)

oh, false alarm, still broken .

---

### 评论 #48 — gstoner (2017-09-14T15:51:33Z)

I am working getting OpenCL update out the door.   



---

### 评论 #49 — boxerab (2017-09-14T15:59:21Z)

Thanks! I am hoping I can complete my port to ROCm once this bug is fixed.

---

### 评论 #50 — boxerab (2017-09-24T13:23:06Z)

Looking for ward to this fix. Any ETA on when it will drop ?  Thanks. 

---

### 评论 #51 — boxerab (2017-10-17T01:04:36Z)

Hurray!!! Finally fixed in 1.6.4 release.  Thank you!!!

---
