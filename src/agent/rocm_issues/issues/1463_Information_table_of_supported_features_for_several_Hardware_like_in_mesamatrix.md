# Information table of supported features for several Hardware like in mesamatrix or better

> **Issue #1463**
> **状态**: closed
> **创建时间**: 2021-04-28T17:10:00Z
> **更新时间**: 2024-01-10T18:43:00Z
> **关闭时间**: 2024-01-10T18:42:59Z
> **作者**: stefano2734
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1463

## 描述

Information table of supported OpenCL features for several Hardware like in mesamatrix or better

See OpenCL tables at the end of website

https://mesamatrix.net/

---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-04-29T05:15:39Z)

Hi @stefano2734 
Thanks for reaching out.
I did not understand your point well. Are you sharing information or are you looking for some information?
Please clarify.
Thank you.

---

### 评论 #2 — stefano2734 (2021-04-29T09:03:32Z)

I want see same or better information tables in rocM also.
Mesamatrix with his tables shows not perfect but good the status of their development.
This tables can help users and developers.
Most functions are not used in software by asymmetrical information.
Internal  status of a software is complex.
Quality of code, performance, bugs, Features, todo list and much more.
And this all under permanent time pressure.
So sometimes a project Team must go in a helicopter ahead and see the world of their project.
And one helicopter tool is a table of supported functions also in relation to other implementation and teams.
Normally a standard is a wonderful milestone.
OpenCL 3.0 is a „broken“ standard. OpenCL 2.x is only optional. And many other functions are also optional not in the Standard. Not all hardware can do all of this. So there is a Matrix of possible.
A developer for many platforms must now, what he can use by base for his software. 
At the moment only OpenCL 1.2 is secure for actual and older hardware. Only very old is compatible only to OpenCL 1.1.
So 50% of your work less or more is actual not used.
Some functions are optional but available in most OpenCL-teams.
With public clear information more functions are used with progress in software.

Internal you should have status tables of your project with comparisons to the other teams of Nvidia, Intel and Mesa and others.


---

### 评论 #3 — stefano2734 (2021-04-30T11:12:41Z)

And see slides: FAST development and their problems with OpenCL features and OpenCL support in drivers
https://www.iwocl.org/wp-content/uploads/17-iwocl-syclcon-2021-smistad-slides.pdf
Gromacs goes to SYCL 
https://www.iwocl.org/wp-content/uploads/22-iwocl-syclcon-2021-alekseenko-slides.pdf


---

### 评论 #4 — ROCmSupport (2021-08-09T05:17:54Z)

Thanks @stefano2734 
I will let developer to comment on this. Thank you.

---

### 评论 #5 — ROCmSupport (2022-02-09T13:07:31Z)

Hi @stefano2734 
I got update from developer and pasting here.

**For extensions OpenCL supports, run clinfo, all will be listed for the GPU, as well as the platform extensions.**

Hope this helps.
Thank you.

---

### 评论 #6 — ROCmSupport (2022-05-13T13:16:54Z)

I am closing this considering as requested information is shared.
Feel free to open a new issue, for any, for quick resolutions.
Thank you.

---

### 评论 #7 — nartmada (2024-01-10T18:42:59Z)

Closing the ticket as requested info has been shared by ROCmSupport on May 13, 2022.  

---
