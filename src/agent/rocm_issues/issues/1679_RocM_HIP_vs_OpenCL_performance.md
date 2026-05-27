# RocM HIP vs OpenCL performance

> **Issue #1679**
> **状态**: closed
> **创建时间**: 2022-02-16T10:40:03Z
> **更新时间**: 2024-05-07T21:12:01Z
> **关闭时间**: 2024-05-07T21:12:01Z
> **作者**: incardon
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1679

## 描述

Dear ROCM developers.

First I wanted to thanks for creating the HIP interface.

I was trying to asses the performance of HIP vs OpenCL

I tried to use the miniBUDE benchmark. Is a benchmark that came out of ISC 2021 as best paper award.

https://github.com/UoB-HPC/miniBUDE

I tried to run that benchmark on my Vega 64. With ROCM 4.5.

Than I also tried to take the CUDA version. converted manually to hip (just have to change some cuda function into hip). Activate shared memory (because the OpenCL version use shared memory). (-ffast-math to emulate the OpenCL options)


I am not sure why is happening. looking at the .s with --save-temps

main-hip-amdgcn-amdhsa-gfx900:xnack-.s. It seems that OpenCL has the tendency to create a kernel that use much more register (with less occupancy) than the one with HIP.



I attach the CUDA version converted to HIP because is condensated everything in one file can be compiled easily with

hipcc -O3 -march=native -std=c++14 -ffast-math -mcpu=gfx900:xnack- -DUSE_SHARED bude.cpp -o bude

and run with

./bude -n 131072 -w 128

The original OpenCL miniBUDE

is in the original repo 

https://github.com/UoB-HPC/miniBUDE/tree/master/opencl

I run as well with

./bude -n 131072 -w 128

P.S. I make sure that shared is used on both cases and NUM_TD_PER_THREAD=4 


Thanks gmarkomanolis. I missed that option.








---

## 评论 (27 条)

### 评论 #1 — gmarkomanolis (2022-02-17T07:37:54Z)

Hi,

I have used the miniBUDE with AMD MI100 and achieved a bit more than 22 TFLOPs (SP) with HIP. I assume you used their approach to hipify, no need to do something, they have integrated in their Makefile to hipify on the fly. However, for MI100 I had to increase the workload as the default input files were not that big to stress the GPU. I used 983040 poses, the default 65536 was not a big workload for me, but this is for MI100 which is quite more strong and has more memory than Vega 64. I have not tried OpenCL, however, HIP achieved more than 95% of the peak.
I have some data and the script here: https://github.com/cschpc/epmhpcgpu/blob/v1.4.1/miniBUDE/minibude_hip_mi100.sh as also the input data in the main miniBUDE directory but I am sure you need a different problem size for your GPU.



---

### 评论 #2 — incardon (2022-02-17T09:28:33Z)

Thanks gmarkomanolis. I missed that option.

I will rerun with your big5 deck and post the results





---

### 评论 #3 — gmarkomanolis (2022-02-17T11:01:13Z)

Also, it was better performance for NUM_TD_PER_THREAD=1, the 4 is good for NVIDIA GPU.
https://github.com/cschpc/epmhpcgpu/blob/v1.4.1/miniBUDE/patch_hip_mi100.patch 

---

### 评论 #4 — incardon (2022-02-17T18:53:00Z)

Thanks. You are using the counter indicated by miniBUDE application ?.

I see also you are using A100. Do you also remember the result for the A100 ?

---

### 评论 #5 — incardon (2022-02-17T18:57:42Z)

Oh I see you actually have it in the result section.

---

### 评论 #6 — gmarkomanolis (2022-02-17T19:18:15Z)

Yes, the provided counter, everything is here: https://github.com/cschpc/epmhpcgpu/tree/v1.4.1/miniBUDE all these files are part of a dataset from a paper that we are presenting next month ( https://zenodo.org/record/5497028#.Yg6fTd-xW-Y ) 

---

### 评论 #7 — incardon (2022-02-17T21:14:02Z)

Oh I see, you are collaborating with Bussmann and Rosendorf. Greetings from my side.

---

### 评论 #8 — incardon (2022-02-18T10:28:43Z)

Thanks unfortunately, it did not workout. An increase of number of poses does not improve performance. While using a deck as big as big5 or bm2 does not seems to work on Vega 64. (maybe too big ?)

---

### 评论 #9 — gmarkomanolis (2022-02-18T12:28:35Z)

Sure, I was expecting memory issues with so big problem. Download the files that were provided to me by the miniBUDE developers from here: https://www.dropbox.com/sh/ttbnvl0w8zaibfy/AADBm55BmxvoqNg_s679lbcJa?dl=0 

The bm3.zip is another case. The raw.zip are the files to create a new dataset.
In order to create a new one (use files from raw.zip), execute (I hope I am not wrong):

    ./makedeck -f heavy_by-atom_2016-v1.bhff -p bude_1gcz_proA.mol2 -l bude_1gcz_proA.mol2 -o output -n <N> --force

where N is the number of the poses and -o output I think would be a folder with all the data.

Run minibude with the updated pose count (default is 65536):

    ./bude --deck ../data/bm3 --numposes 131072

---

### 评论 #10 — incardon (2022-02-20T16:53:17Z)

Thanks. It works. But the result are the same to the original bm1. (Actually bm3 is a little slower than bm1)

2.6 Teraflops for HIP and 4.5 Teraflops OpenCL


---

### 评论 #11 — gmarkomanolis (2022-02-22T09:30:41Z)

Could you try in bude.c to declare   _cuda.posesPerWI  = 8;  // line 121

I had to try it again to run it and this helped. However, increasing the problem helps most of the time but you do not have enough memory probably.

---

### 评论 #12 — incardon (2022-02-22T09:58:50Z)

Thanks, I think I did it and was not producing any speed-up. But maybe I confuse Nvidia with AMD. I will try again.

P.S. It is a bit of time, so maybe I remember incorrectly but to increase _cuda.posesPerWI = 8 I think you have to increase NUM_TD_PER_THREADS as well otherwise you get a crash.

I will try this evening, because the machine is at home

---

### 评论 #13 — ROCmSupport (2022-02-22T13:42:48Z)

Hi @incardon 
Thanks for reaching out.
Looks like some good discussion is happening. Please let me know if you need any support.
Thank you.

---

### 评论 #14 — incardon (2022-02-24T07:54:19Z)

Thanks. Sorry for the delay gmarkomanolis

I tried to change only

 _cuda.posesPerWI = 8

and poses 131072

And went to 4.4 Teraflops. The program is a bit evil because it say success (mostly no difference) but it is actually broken. Unfortunately it only check the 65536 poses and does not detect the error. If I now run with 65536 we see that is broken and it did half of the job.
(P.S. I think you can change the number of poses checked, from REF_NPOSES, but never explicitly tried)

bringing NUM_TD_PER_THREADS=8 the program start to work again and renormalize to 2.5 Terflops


---

### 评论 #15 — incardon (2022-02-24T08:24:47Z)

I will have an MI50 soon, so I will check also there.

P.S.

I see in your patch, you change NUM_TH_PER_THREADS without changing _cuda.posesPerWI. That in theory could inflate the results for MI100. Is it ?

---

### 评论 #16 — gmarkomanolis (2022-02-24T11:41:47Z)

I have to remember but I had activated to test all the data and not only the 65536 to be sure that there is no issue, I had seen the crash you describe with wrong values etc. that's why I always declare to check all the points and not only for 65536. I think the patch does not include all the changes, as I was trying to make a clean patch because I had added many other things for control, I need to check it. 

Edit: indeed no need to modify cuda.posesPerWI.  The NUM_TD_PER_THREAD was also proposed by the developers when compared NVIDIA and AMD GPUs

---

### 评论 #17 — incardon (2022-02-24T17:17:12Z)

So you change NUM_TD_PER_THREAD, but you leave cuda.posesPerWI the same. You do not change it neither by command line ?

---

### 评论 #18 — gmarkomanolis (2022-02-24T17:53:45Z)

yes, nothing else, I tried a bit the wgsize, it helped a bit only as 256 is better for the MI100 and I assume not only. Not huge improvement though, just a bit. 

---

### 评论 #19 — incardon (2022-02-26T20:35:29Z)

> yes, nothing else

Thanks, for me does not work, changing only NUM_TD_PER_THREAD and having it different from _cuda.posesPerWI. if NUM_TD_PER_THREAD is smaller than _cuda.posesPerWI it runs, but the GFlops are inflated, and the results are wrong. if NUM_TD_PER_THREAD is bigger it crash

---

### 评论 #20 — gmarkomanolis (2022-02-27T14:01:20Z)

So the message "Largest difference was 0.000%" is not 0, right? I am not sure about this. If I remember correctly with high NUM_TD_PER_THREAD it was almost not finishing, lasting forever. Have you checked the clpeak benchmark to test the GPU card?  

---

### 评论 #21 — incardon (2022-02-27T14:07:55Z)

For me it say "inf" in bm1 if I do not keep it consistent.  I did not check clpeak

---

### 评论 #22 — gmarkomanolis (2022-02-27T14:12:00Z)

ok, I had never seen something like that. clpeak gives close to the peak performance. 

---

### 评论 #23 — incardon (2022-02-27T14:21:54Z)

>  clpeak gives close to the peak performance.

Can be ... miniBUDE is not clpeak. At least from my testing changing NUM_TD_PER_THREAD and not _cuda.posesPerWI is incorrect. If you want I can test exactly your parameters. poses 131072 _cuda.posesPerWI = 4, NUM_TD_PER_THREAD = 1 deck bm3 ?

---

### 评论 #24 — gmarkomanolis (2022-02-27T15:02:00Z)

For sure it is not clpeak, I have seen various performances with miniBUDE which are not close at all to the peak. Also some results depend on the software in some cases. Yes, with 131072 I could not get a lot of performance on MI100 as the workload was not enough but you could try. 

---

### 评论 #25 — incardon (2022-02-27T19:10:21Z)

I see, probably I was not clear. For correct result I do not refer to the performance, but I refer to the correctness of the result. Up to now I tried any deck, any GPU, either 65536 either 131072, and I did not see one case where using NUM_TD_PER_THREAD different from _cuda.posesPerWI produces "Largest difference was " near to zero. I do not put in doubt that the author of miniBUDE could have said that NUM_TD_PER_THREAD is the only parameter you have to tune, but in addition to the wrong results, I was also cheking the code. Maybe I missed something, but also the logic of the code does not add-up to me. In the sense that clearly NUM_TD_PER_THREAD indicate the factor of work each thread take in the kernel. Because of this I am expecting an equivalent reduction in the in the number of blocks or total threads in the kernel launching. Printing the number of blocks used to launch the kernel the only parameter able to do this is _cuda.posesPerWI parameter. NUM_TD_PER_THREAD does not influence the number of blocks/threads launched

It surprises me that having NUM_TD_PER_THREAD and _cuda.posesPerWI produce correct result, because I am not able to reproduce it



---

### 评论 #26 — gmarkomanolis (2022-02-27T19:26:14Z)

I am not sure, but I was trying to have as possible as good performance with always largest difference equal to 0 for all the poses, not just 65k. Sure, the code maybe is not perfect and I am not fully aware of all of it. Yes,  NUM_TD_PER_THREAD does not change the blocks/threads. 

---

### 评论 #27 — ROCmSupport (2022-05-09T05:02:04Z)

Hi All,
Did we get some conclusion on this.
Can we close this if we find some reasonable information on this topic. Please let me know.
Thank you.

---
