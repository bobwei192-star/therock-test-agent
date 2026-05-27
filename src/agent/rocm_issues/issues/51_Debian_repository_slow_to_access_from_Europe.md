# Debian repository slow to access from Europe

> **Issue #51**
> **状态**: closed
> **创建时间**: 2016-11-27T15:33:06Z
> **更新时间**: 2017-07-02T17:15:23Z
> **关闭时间**: 2017-07-02T17:15:23Z
> **作者**: almson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/51

## 描述

Download speeds in Europe are 100 KB/s. I've mentioned this to Greg already. The issue is most like a mis-configuration of TCP stack parameters. Basically, the servers are allowing too few packets in flight and don't work well with high-latency networks. There's no need to add additional European servers or set up a CDN.

---

## 评论 (3 条)

### 评论 #1 — gstoner (2016-11-27T15:35:01Z)

We moving of this server, since we can not get control of these setting.  We get this addressed when we move over to our new system.

Greg
On Nov 27, 2016, at 9:33 AM, almson <notifications@github.com<mailto:notifications@github.com>> wrote:


Download speeds in Europe are 100 KB/s. I've mentioned this to Greg already. The issue is most like a mis-configuration of TCP stack parameters. Basically, the servers are allowing too few packets in flight and don't work well with high-latency networks. There's no need to add additional European servers or set up a CDN.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/51>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duc5ydKNFjCFKNgOUz5X6j61Zfmpzks5rCaKzgaJpZM4K9LKZ>.



---

### 评论 #2 — keithdunnett (2016-12-12T03:38:53Z)

Glad to see improvements are apparently in the works, just to add that the issue is still happening a fortnight later and it really does stand out as the longest I've waited for anything in a while. I'm getting a _very_ stable 118-119kB/sec with bursts to ~125kB (150Mbit cable, middle of the night).

14 hops, ~120ms away, no signs of packet loss or jitter.  This bears little or no resemblance to a TCP congestion control issue, and whilst I'm across the pond from Atlanta, the link is no worse than plenty of UK/US links I use. Nope. This is exactly in line with what happens when you set a 1Mbit/sec per client bandwidth restriction and it's been stable within 5% of that for half an hour. 

Of course I can't know from outside, but I strongly suspect a misconfiguration at your server, most likely rate limiting with QoS rather than at web server level. Your ISP is unlikely to be the cause, as a cheap $10 VPS is restricted to far more than that. 

My guess is qdisc in some form; unlike a straight bandwidth limit it quickly confuses people, not helped by the fact that mosr implementations take their input in _bits_ per second. Which is an awfully big number even for a cable connection, probably not something you want on a hosted GigE server. Sure, it's an educated guess, but it's unlikely to be the ISP.

If this is Greek to you (let's face it, so is homogeneous computing to systems & networks guys...) try running "tc -d qdisc show"; that should get you to what's on the network interface irrespective of what you may use to manage it. A qdisc of type 'pfifo_fast' is the default on many systems and nothing to worry about; my suspicion is of a misplaced token bucket filter. Now, back to seeing what I just installed...



 

---

### 评论 #3 — gstoner (2017-07-02T17:15:23Z)

Repo has been upgraded to a new server foundation 

---
