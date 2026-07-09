# Segmentation Fault Pytorch  RX 6700xt

- **Issue #:** 1931
- **State:** closed
- **Created:** 2023-03-12T18:32:59Z
- **Updated:** 2024-05-27T18:57:42Z
- **Labels:** application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/1931

Hi,

I am trying to run a test for my RX 6700xt but I  face many problems.
I tried issue#1686 and 1687 but I was not able to fix them.

I get an error of segmentation faul when I am trying to do run a test inside a docker image:

https://www.youtube.com/watch?v=HwGgzaz7ipQ

The other problem is that after having installed rocm and pytorch terminal returns cuda available = false. ( in docker image returns true)

I have used both Ubuntu 22 and 20 but still have the same proble. Is pytorch compatible only with 5.2 rocm?

Also, in the docker image it returns cuda available but does not run the test.

Can anybody help?