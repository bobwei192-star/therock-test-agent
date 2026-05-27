# Radeon Instinct MI series cards

> **Issue #1703**
> **状态**: closed
> **创建时间**: 2022-03-15T18:18:11Z
> **更新时间**: 2024-01-23T21:46:54Z
> **关闭时间**: 2024-01-23T21:46:54Z
> **作者**: Schubox84
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1703

## 描述

I have a few MI25 cards that i just got in. most of them have tested bad. but for the ones that allow me to boot into linux, they arent recognized by Linux. running -sudo -class display shows the intel onboard graphics only. ive installed ROCm but it wont initialize until it finds a card to work with? any ideas would be much appreciated. I have tried these cards on other setups with no luck. Am i just receiving broken cards hoping i wont figure that out? all my PC troubleshooting knowledges leads me to believe that is what is going on. Proficient in Windows, not so much in Linux thats why I am asking. 

---

## 评论 (3 条)

### 评论 #1 — wreckdump (2022-03-16T16:21:38Z)

Can you post the output of the following command, in your linux machine that has the MI25 plugged in?

`lspci | grep Vega`

This may show you whether your machine is recognizing the card or not. And as far as I know, Instinct cards do not work under Windows.

---

### 评论 #2 — ROCmSupport (2022-03-24T06:31:49Z)

Hi @Schubox84 
Thanks for reaching out.
Looks like you have hardware problems, need to be corrected. This is not the right space for this.

When it comes to software side,
MI25 is dropped from ROCm supported list from 4.5.x onwards.
Request to try the previous versions and things work in pretty good way.
Hope this helps.
Thank you.

---

### 评论 #3 — ROCmSupport (2022-05-09T05:04:48Z)

Closing as per previous comment as hoping we shared the necessary information.
Request to file new tickets, if any, for quick resolutions.
Thank you.

---
