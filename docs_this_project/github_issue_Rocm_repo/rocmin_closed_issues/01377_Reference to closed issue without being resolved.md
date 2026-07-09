# Reference to closed issue without being resolved

- **Issue #:** 1377
- **State:** closed
- **Created:** 2021-02-11T02:25:35Z
- **Updated:** 2021-04-08T11:38:34Z
- **URL:** https://github.com/ROCm/ROCm/issues/1377

I revisited this issue which was closed without resolving.
ROCclr build issue, make failed. #1358

It was closed because it is waited too long. Waiting too long does not resolve the issue, why you (rocm-support) think doing so will resolve the issue itself?
This will cause test escape and problem to escape and only to regress later. 

I have revisited the problem and found the problem for you at no cost when rocm-support did not root cause but instead chose to close.
The export statement in the README is wrong and does not set path correct. Please revisit the closed one and found yourself. 

It should be rocm-support's responsibility to root cause not me and test their solution on their end not me as submitter. 
I was able to build but I am not going to post the solution as it should have been your responsibility. 
You should not close this one either until instruction is corrected in the README that led to a successfull build no longer how long the issue stays dormant. Because otherwise you dont root cause, yet you close the issue when the problem exist, that is bad practice for rocm-support. 


