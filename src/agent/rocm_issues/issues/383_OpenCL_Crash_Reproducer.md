# OpenCL Crash Reproducer

> **Issue #383**
> **状态**: closed
> **创建时间**: 2018-04-10T00:37:47Z
> **更新时间**: 2018-04-17T20:04:32Z
> **关闭时间**: 2018-04-17T20:04:32Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/383

## 描述

I get the following error when I run a relatively simple OpenCL kernel on the latest ROCM 1.7, with RX 470:

    Memory access fault by GPU node-1 on address 0x901b09000. Reason: Page not present or supervisor privilege.

I am quite sure that there are no out-of-bounds memory accesses.
I've attached a complete reproducer to this issue: see if you can prove me wrong !

[opencl_crash.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/1892395/opencl_crash.tar.gz)




---

## 评论 (30 条)

### 评论 #1 — briansp2020 (2018-04-10T00:58:28Z)

Sounds similar to https://github.com/ROCmSoftwarePlatform/tensorflow/issues/21


---

### 评论 #2 — briansp2020 (2018-04-10T00:59:40Z)

Oh. Did not realize that you were already on that thread... Doh...

---

### 评论 #3 — boxerab (2018-04-10T01:14:32Z)

That's a different issue. Fix is coming shortly.
This seems to be a compiler bug.

---

### 评论 #4 — todxx (2018-04-10T10:14:23Z)

This line
`			FLAG_CACHE(SIGN_N_CACHE_ID) = SCRATCH_FLAG_N(scratchFlags, SIGN_FLAG_ID, S_GRID_ID);`
is invoking this macro
`#define SCRATCH_FLAG_N(flagPtr,id, loc)	select((STRIPELET_T)0, (STRIPELET_T)(flagPtr)[((loc)+NORTH(sGridDimX))*SCRATCH_STRIDE+(id)*SCRATCH_LINE],		(STRIPELET_T)( sGridY != 0) )`

Looking at the expression `(STRIPELET_T)(flagPtr)[((loc)+NORTH(sGridDimX))*SCRATCH_STRIDE+(id)*SCRATCH_LINE]`

For the first iteration of your inner loop, I believe this expression results in:`(STRIPELET_T)(flagPtr)[((0)+-4)*1024+(0)*1024]` or `(STRIPELET_T)(flagPtr)[-4096]`

The flagPtr here is your `scratchFlags` kernel argument, which is a uint pointer to the beginning of a 32kB global memory buffer.  Evaluating the above expression results in an invalid memory access since the code is trying to access memory before this buffer.

You can double check this by commenting out the line invoking the macro, and add a print out of just the index expression:
```
            int index = ((S_GRID_ID)+NORTH(sGridDimX))*SCRATCH_STRIDE+(SIGN_FLAG_ID)*SCRATCH_LINE;
            printf("scratchFlags index is %d\n", index); 
//          FLAG_CACHE(SIGN_N_CACHE_ID) = SCRATCH_FLAG_N(scratchFlags, SIGN_FLAG_ID, S_GRID_ID); 

```

Hope this helps.

---

### 评论 #5 — boxerab (2018-04-10T12:19:20Z)

@todxx thanks for looking at this! For the first iteration, the third parameter in the `select` call is false,
so I assumed that in this case, the second parameter would not be evaluated.  

If it is evaluated, then yes, there is an out of bounds access.

So, on ROCm OpenCL, I guess the question is: are both first and second parameters evaluated in a 
`select` call ?




---

### 评论 #6 — todxx (2018-04-10T12:27:27Z)

I'm not entirely sure, but I believe the builtin functions are treated the
same way as normal functions when it comes evaluating arguments.  I.e. if
you wrote your own select function, you would expect argument expressions
to be evaluated before the function is invoked.

On Tue, Apr 10, 2018, 05:19 Aaron Boxer <notifications@github.com> wrote:

> @todxx <https://github.com/todxx> thanks for looking at this! For the
> first iteration, the third parameter in the select call is false,
> so I assumed that in this case, the second parameter would not be
> evaluated.
>
> If it is evaluated, then yes, there is an out of bounds access.
>
> So, on ROCm OpenCL, I guess the question is: are both first and second
> parameters evaluated in a
> select call ?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/383#issuecomment-380078288>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AiZxN_AOnHz0v3N1pyasQA31iAqWrkkcks5tnKNPgaJpZM4TNbey>
> .
>


---

### 评论 #7 — boxerab (2018-04-10T12:33:16Z)

Thanks. I've fixed this out of bounds issue, by offsetting the global memory pointer.
But, I still get an error. I've attached the updated files.

[opencl_crash_2.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/1894554/opencl_crash_2.tar.gz)


---

### 评论 #8 — boxerab (2018-04-10T12:34:15Z)

@todxx do you also see this memory error ?

---

### 评论 #9 — todxx (2018-04-10T12:40:15Z)

I can't test your new version at the moment, but I'll give it a try
tomorrow.

On Tue, Apr 10, 2018, 05:34 Aaron Boxer <notifications@github.com> wrote:

> @todxx <https://github.com/todxx> do you also see this memory error ?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/383#issuecomment-380082160>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AiZxN2Lu2Hd0lFWGjLbL0TyUMHBTcP3Gks5tnKbcgaJpZM4TNbey>
> .
>


---

### 评论 #10 — boxerab (2018-04-10T12:50:51Z)

Cool, thanks.

---

### 评论 #11 — todxx (2018-04-11T10:45:49Z)

I gave your new version a shot, and I can reproduce the problem.

Looking at your code, I think this line might be causing some problems:
```    scratchFlags += 32*4*1024 + globalBlockNumber;```
This line will increase the scratchFlags pointer by (32 * 4 * 1024 + globalBlockNumber) uints, I.e. at least 512k bytes, which is larger than your buffer of 256k bytes.  I think you might have over looked the 4x multiplier for the pointer arithmetic due to the base type of uint. 

However, this does not seem to fix the problem, as the kernel still crashes.  I hope this at least helps a little.  I'll check back later when I have more time.

---

### 评论 #12 — boxerab (2018-04-11T11:34:58Z)

Thanks, I've fixed this issue and made the global memory buffer over size, so no more buffer out of bounds.
And yet, I still see this error.  Here is the final version of this reproducer.

@gstoner Can you guys please take a look at this ?

[opencl_crasher_3.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/1898580/opencl_crasher_3.tar.gz)


---

### 评论 #13 — boxerab (2018-04-16T11:48:11Z)

Can I please get some feedback on this from AMD team? This bug is a show stopper for me - no workaround and my decoder will not run on ROCm. Works fine on windows.

---

### 评论 #14 — gstoner (2018-04-16T11:54:48Z)

The bug you reported was an error in your kernel an out of bounds memory. reference, not the OpenCL stack or ROCm driver.    Have you run clArmour on it yet.  https://github.com/ROCm-Developer-Tools/clARMOR.   I am having the team look at this but it in the queue,  Since we right now trying to get ROCm 1.8 ready for beta and also bring up of the follow-on to Vega10.

---

### 评论 #15 — boxerab (2018-04-16T12:03:11Z)

@gstoner Thanks.  Yes, first two kernels had out of bounds memory ref. But third did not, and still caused error.
I will try clArmour just to make sure.

---

### 评论 #16 — boxerab (2018-04-16T12:33:20Z)

So, clArmor just gives the same error message. But, I made the global memory buffer extra large, so it is no possible for there to be an out of bounds access.

---

### 评论 #17 — boxerab (2018-04-16T12:33:41Z)

And core is getting dumped with clArmor.

---

### 评论 #18 — gstoner (2018-04-16T12:53:47Z)

clAMOUR does not caught all out of bound memory access 

---

### 评论 #19 — boxerab (2018-04-16T12:57:28Z)

Thanks. So, as I made the global memory very large in `opencl_crasher_3` , it isn't possible to have a buffer out of bounds, so it appears that there is a bug in the opencl library.

---

### 评论 #20 — todxx (2018-04-16T13:22:38Z)

I can confirm that a compiler bug is involved here.

Adding `#pragma unroll` to the loops results in the kernel running successfully, with no memory access faults.

---

### 评论 #21 — boxerab (2018-04-16T15:19:32Z)

@todxx thanks for testing that. I will add that pragma as a workaround for now until this gets fixed.

---

### 评论 #22 — boxerab (2018-04-16T15:33:19Z)

@todxx is there a down-side to unrolling the loop ? For performance ?

---

### 评论 #23 — boxerab (2018-04-16T20:31:08Z)

Yes, can confirm @todxx 's finding: adding pragma before first loop fixes the error.

---

### 评论 #24 — gstoner (2018-04-16T22:34:21Z)


Just an update. . About the bug, seems line:170 of HelloWorld.cl causes the problem.
Line 170 is:
FLAG_CACHE(SIGN_N_CACHE_ID) = SCRATCH_FLAG_N(scratchFlags, SIGN_FLAG_ID, S_GRID_ID);
 
Note this output on new debugger we are working on. 

Memory access fault by GPU agent: AMD gfx900
Node: 1
Address: 0x1502F3Cxxx (page not present;)
 
16 wavefront(s) found in XNACK error state @PC: 0x0000001101F0B1A4
printing the first one:
 
   EXEC: 0xFFFFFFFFFFFFFFFF
STATUS: 0x00412461
TRAPSTS: 0x30000000
     M0: 0x0000100C
 
     s0: 0x00000400    s1: 0x11111111    s2: 0xFFFFF000    s3: 0x00000000
     s4: 0xEEEEEEEE    s5: 0x00000080    s6: 0x00000000    s7: 0x00000000
     s8: 0xFFFFC000    s9: 0x00000003   s10: 0x00000000   s11: 0x00000000
    s12: 0xFFFFFFFF   s13: 0xFFFFFFFF   s14: 0x00000000   s15: 0x00000000
 
Lane 0x0
     v0: 0x02F40000    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C000
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014000    v7: 0x00000000
Lane 0x1
     v0: 0x02F40004    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C004
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014028    v7: 0x00000000
Lane 0x2
     v0: 0x02F40008    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C008
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014050    v7: 0x00000000
Lane 0x3
     v0: 0x02F4000C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C00C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014078    v7: 0x00000000
Lane 0x4
    v0: 0x02F40010    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C010
     v4: 0x00000015    v5: 0x00000011    v6: 0x000140A0    v7: 0x00000000
Lane 0x5
     v0: 0x02F40014    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C014
     v4: 0x00000015    v5: 0x00000011    v6: 0x000140C8    v7: 0x00000000
Lane 0x6
     v0: 0x02F40018    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C018
     v4: 0x00000015    v5: 0x00000011    v6: 0x000140F0    v7: 0x00000000
Lane 0x7
     v0: 0x02F4001C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C01C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014118    v7: 0x00000000
Lane 0x8
     v0: 0x02F40020    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C020
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014140    v7: 0x00000000
Lane 0x9
     v0: 0x02F40024    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C024
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014168    v7: 0x00000000
Lane 0xA
     v0: 0x02F40028    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C028
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014190    v7: 0x00000000
Lane 0xB
     v0: 0x02F4002C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C02C
     v4: 0x00000015    v5: 0x00000011    v6: 0x000141B8    v7: 0x00000000
Lane 0xC
     v0: 0x02F40030    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C030
     v4: 0x00000015    v5: 0x00000011    v6: 0x000141E0    v7: 0x00000000
Lane 0xD
     v0: 0x02F40034    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C034
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014208    v7: 0x00000000
Lane 0xE
     v0: 0x02F40038    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C038
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014230    v7: 0x00000000
Lane 0xF
     v0: 0x02F4003C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C03C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014258    v7: 0x00000000
Lane 0x10
     v0: 0x02F40040    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C040
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014280    v7: 0x00000000
Lane 0x11
     v0: 0x02F40044    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C044
     v4: 0x00000015    v5: 0x00000011    v6: 0x000142A8    v7: 0x00000000
Lane 0x12
     v0: 0x02F40048    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C048
     v4: 0x00000015    v5: 0x00000011    v6: 0x000142D0    v7: 0x00000000
Lane 0x13
     v0: 0x02F4004C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C04C
     v4: 0x00000015    v5: 0x00000011    v6: 0x000142F8    v7: 0x00000000
Lane 0x14
     v0: 0x02F40050    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C050
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014320    v7: 0x00000000
Lane 0x15
     v0: 0x02F40054    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C054
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014348    v7: 0x00000000
Lane 0x16
     v0: 0x02F40058    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C058
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014370    v7: 0x00000000
Lane 0x17
     v0: 0x02F4005C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C05C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014398    v7: 0x00000000
Lane 0x18
     v0: 0x02F40060    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C060
     v4: 0x00000015    v5: 0x00000011    v6: 0x000143C0    v7: 0x00000000
Lane 0x19
     v0: 0x02F40064    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C064
     v4: 0x00000015    v5: 0x00000011    v6: 0x000143E8    v7: 0x00000000
Lane 0x1A
     v0: 0x02F40068    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C068
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014410    v7: 0x00000000
Lane 0x1B
     v0: 0x02F4006C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C06C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014438    v7: 0x00000000
Lane 0x1C
     v0: 0x02F40070    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C070
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014460    v7: 0x00000000
Lane 0x1D
     v0: 0x02F40074    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C074
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014488    v7: 0x00000000
Lane 0x1E
     v0: 0x02F40078    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C078
     v4: 0x00000015    v5: 0x00000011    v6: 0x000144B0    v7: 0x00000000
Lane 0x1F
     v0: 0x02F4007C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C07C
     v4: 0x00000015    v5: 0x00000011    v6: 0x000144D8    v7: 0x00000000
Lane 0x20
     v0: 0x02F40080    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C080
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014500    v7: 0x00000000
Lane 0x21
     v0: 0x02F40084    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C084
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014528    v7: 0x00000000
Lane 0x22
     v0: 0x02F40088    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C088
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014550    v7: 0x00000000
Lane 0x23
     v0: 0x02F4008C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C08C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014578    v7: 0x00000000
Lane 0x24
     v0: 0x02F40090    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C090
     v4: 0x00000015    v5: 0x00000011    v6: 0x000145A0    v7: 0x00000000
Lane 0x25
     v0: 0x02F40094    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C094
     v4: 0x00000015    v5: 0x00000011    v6: 0x000145C8    v7: 0x00000000
Lane 0x26
     v0: 0x02F40098    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C098
     v4: 0x00000015    v5: 0x00000011    v6: 0x000145F0    v7: 0x00000000
Lane 0x27
     v0: 0x02F4009C    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C09C
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014618    v7: 0x00000000
Lane 0x28
     v0: 0x02F400A0    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0A0
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014640    v7: 0x00000000
Lane 0x29
     v0: 0x02F400A4    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0A4
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014668    v7: 0x00000000
Lane 0x2A
     v0: 0x02F400A8    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0A8
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014690    v7: 0x00000000
Lane 0x2B
     v0: 0x02F400AC    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0AC
     v4: 0x00000015    v5: 0x00000011    v6: 0x000146B8    v7: 0x00000000
Lane 0x2C
     v0: 0x02F400B0    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0B0
     v4: 0x00000015    v5: 0x00000011    v6: 0x000146E0    v7: 0x00000000
Lane 0x2D
     v0: 0x02F400B4    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0B4
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014708    v7: 0x00000000
Lane 0x2E
     v0: 0x02F400B8    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0B8
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014730    v7: 0x00000000
Lane 0x2F
     v0: 0x02F400BC    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0BC
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014758    v7: 0x00000000
Lane 0x30
     v0: 0x02F400C0    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0C0
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014780    v7: 0x00000000
Lane 0x31
     v0: 0x02F400C4    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0C4
     v4: 0x00000015    v5: 0x00000011    v6: 0x000147A8    v7: 0x00000000
Lane 0x32
     v0: 0x02F400C8    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0C8
     v4: 0x00000015    v5: 0x00000011    v6: 0x000147D0    v7: 0x00000000
Lane 0x33
     v0: 0x02F400CC    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0CC
     v4: 0x00000015    v5: 0x00000011    v6: 0x000147F8    v7: 0x00000000
Lane 0x34
     v0: 0x02F400D0    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0D0
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014820    v7: 0x00000000
Lane 0x35
     v0: 0x02F400D4    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0D4
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014848    v7: 0x00000000
Lane 0x36
     v0: 0x02F400D8    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0D8
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014870    v7: 0x00000000
Lane 0x37
     v0: 0x02F400DC    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0DC
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014898    v7: 0x00000000
Lane 0x38
     v0: 0x02F400E0    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0E0
     v4: 0x00000015    v5: 0x00000011    v6: 0x000148C0    v7: 0x00000000
Lane 0x39
     v0: 0x02F400E4    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0E4
     v4: 0x00000015    v5: 0x00000011    v6: 0x000148E8    v7: 0x00000000
Lane 0x3A
     v0: 0x02F400E8    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0E8
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014910    v7: 0x00000000
Lane 0x3B
     v0: 0x02F400EC    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0EC
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014938    v7: 0x00000000
Lane 0x3C
     v0: 0x02F400F0    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0F0
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014960    v7: 0x00000000
Lane 0x3D
     v0: 0x02F400F4    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0F4
     v4: 0x00000015    v5: 0x00000011    v6: 0x00014988    v7: 0x00000000
Lane 0x3E
     v0: 0x02F400F8    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0F8
     v4: 0x00000015    v5: 0x00000011    v6: 0x000149B0    v7: 0x00000000
Lane 0x3F
     v0: 0x02F400FC    v1: 0x00000011    v2: 0x00000011    v3: 0x02F3C0FC
     v4: 0x00000015    v5: 0x00000011    v6: 0x000149D8    v7: 0x00000000
 
Faulty Code Object:
 
/tmp/ROCm_Tmp_PID_5500/ROCm_Code_Object_1:      file format ELF64-amdgpu-hsacobj
 
Disassembly of section .text:
BB0_1:
 
BB0_2:
; /tmp/AMD_5500_19/t_5500_21.cl:170
        s_lshl_b32 s2, s6, 8                                       // 000000001184: 8E028806
; /tmp/AMD_5500_19/t_5500_21.cl:170
        s_ashr_i32 s7, s2, 6                                       // 000000001188: 90078602
; /tmp/AMD_5500_19/t_5500_21.cl:170
        s_add_i32 s2, s7, -4                                       // 00000000118C: 8102C407
; /tmp/AMD_5500_19/t_5500_21.cl:170
        s_mul_i32 s2, s2, s0                                       // 000000001190: 92020002
; /tmp/AMD_5500_19/t_5500_21.cl:170
        s_lshl_b64 s[8:9], s[2:3], 2                               // 000000001194: 8E888202
; /tmp/AMD_5500_19/t_5500_21.cl:170
        v_mov_b32_e32 v4, s9                                       // 000000001198: 7E080209
; /tmp/AMD_5500_19/t_5500_21.cl:170
        v_add_i32_e32 v3, vcc, s8, v0                              // 00000000119C: 32060008
; /tmp/AMD_5500_19/t_5500_21.cl:170
        v_addc_u32_e32 v4, vcc, v1, v4, vcc                        // 0000000011A0: 38080901
; /tmp/AMD_5500_19/t_5500_21.cl:170
        global_load_dword v3, v[3:4], off                          // 0000000011A4: DC508000 037F0003
; /tmp/AMD_5500_19/t_5500_21.cl:170
        v_cmp_eq_u32_e64 s[8:9], s6, 0                             // 0000000011AC: D0CA0008 00010006
; /tmp/AMD_5500_19/t_5500_21.cl:170
        s_mov_b32 s2, 0                                            // 0000000011B4: BE820080
        s_waitcnt vmcnt(0)                                         // 0000000011B8: BF8C0F70
        v_lshrrev_b32_e32 v3, 3, v3                                // 0000000011BC: 20060683
        v_and_b32_e32 v3, s1, v3                                   // 0000000011C0: 26060601
 
Faulty PC offset: 11A4
 
Aborted (core dumped)


---

### 评论 #25 — boxerab (2018-04-16T22:53:25Z)

Great, thanks for testing this. 

---

### 评论 #26 — b-sumner (2018-04-17T14:08:27Z)

After preprocessing the file I added a print:

            uchar sGridId = sGridX + sGridY * sGridDimX;
            uchar stripeletDimX = (1 << 3);
            uchar stripeletDimY = (1 << 2);
            // (flagCache[(0)]) = select((uint) 0,
            //           (uint) (scratchFlags)[((mad24(sGridY, sGridDimX, sGridX)) +
            //                                   NORTH(sGridDimX)) * (numCodeBlocks * 1) + (0) * numCodeBlocks],
            //           (uint) (sGridY != 0));
            uint i = ((mad24(sGridY, sGridDimX, sGridX)) + NORTH(sGridDimX)) * (numCodeBlocks * 1) + (0) * numCodeBlocks;
            if (sGridX == 0 && sGridY == 0 && globalBlockNumber == 0)
                printf("i = %u\n", i);
            flagCache[0] = select((uint)0, scratchFlags[i & 0xff], (uint)(sGridY != 0));

The output was:
i = 4294963200

When sGridX and sGridY are 0, then the index is (0 + NORTH(4)) * numCodeBlocks.  NORTH(4) = -4, so that index is -4096, which as an unsigned int is 4294963200.

Clearly that is outside of the scratchFlags buffer.

---

### 评论 #27 — boxerab (2018-04-17T14:22:20Z)

@b-sumner thanks. What is strange is that pragma unroll "fixes" the issue.
I guess unroll uses a signed type. 

My apologies then, this is my bad!  

---

### 评论 #28 — boxerab (2018-04-17T14:59:22Z)

@b-sumner actually, no, this is not an issue. The `select` call will make sure that index is never negative.  Assuming that `select` doesn't evaluate both first and second arguments.

---

### 评论 #29 — b-sumner (2018-04-17T15:15:53Z)

That's an invalid assumption.   A call to select(,,) is an ordinary function call without special shortcut semantics like ?: has.

---

### 评论 #30 — boxerab (2018-04-17T20:04:30Z)

@b-sumner yes, you're correct. Thank you! So, it looks like this was the issue. If I store index as `int` and then
access memory, there is no error. Gonna close this.

---
