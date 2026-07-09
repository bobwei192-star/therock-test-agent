# Will rocm repo accept a pull request for adding Navi support for HCC & HIP?

- **Issue #:** 1003
- **State:** closed
- **Created:** 2020-01-22T02:59:09Z
- **Updated:** 2021-04-19T12:58:24Z
- **Assignees:** b-sumner
- **URL:** https://github.com/ROCm/ROCm/issues/1003

HI dear official rocm team:
There are long time since Navi launched and ROCm still missing Navi support yet.  There are lots of improvement in rocm 3.0 codebase for Navi to functional well.  Meanwhile, MyROCm porting to navi for hcc and hip component, seems stable now. So I would like contribute this patch to rocm git, but I am not sure if AMD have the any decision on Navi support from rocm yet.   
Would AMD treat Navi as a consumer grade card excluding from ROCm or it will soon add the support ?
Would the contribution for Navi to Rocm welcome or it will against some AMD's policy ?

Can't wait for a clear guidance from AMD and the plan for Navi with ROCm.

Good new:
linux kernel 5.4+'s golden register patch improve Navi performance by 20%+ after myrocm's benchmark. that's really amazing patch. 

If any interest to review myrocm navi build , you can find binary download url here:
https://github.com/smartbitcoin/MyROCm/releases/download/3.0_navi10/myrocm.3.0.tar.bz2