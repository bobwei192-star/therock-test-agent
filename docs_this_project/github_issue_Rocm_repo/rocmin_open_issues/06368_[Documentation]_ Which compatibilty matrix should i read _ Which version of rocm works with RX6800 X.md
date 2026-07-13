# [Documentation]: Which compatibilty matrix should i read ? Which version of rocm works with RX6800 XT ?

- **Issue #:** 6368
- **State:** open
- **Created:** 2026-06-18T12:15:35Z
- **Updated:** 2026-06-22T18:37:05Z
- **Labels:** status: triage
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6368

### Description of errors

It is impossible to know which version of Rocm i should use with my RX600XT GPU

There are tons of "compatibility matrix", some saying i can use it with 6, or 7 or not !
This is absolutely confisusing.


So far the different ansnswer i got are :

- https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html 7.2.4 which says 7.2.4 + RX6800XT + ubuntu 24.04 **ok**

- https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html , written on  2026-04-17 which **says the opposite, for 7.2.4 too** !

Which page is right  ?

Is it possible to have a _single_ table for Linux listing GPU | minRocm + kernel version | max rocm + kernel version  , so one could easyly know that for R6800XT , one need rocm_X to rocm_Y on linux ?


### Attach any links, screenshots, or additional evidence you think will be helpful.

- https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html 7.2.4 which says 7.2.4 + RX6800XT + ubuntu 24.04 **ok**

- https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html , written on  2026-04-17 which **says the opposite, for 7.2.4 too** !
