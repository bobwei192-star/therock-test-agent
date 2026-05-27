# Is rocm support rx6650xt?

> **Issue #1972**
> **状态**: closed
> **创建时间**: 2023-03-18T12:06:12Z
> **更新时间**: 2024-05-10T18:24:00Z
> **关闭时间**: 2024-05-10T18:24:00Z
> **作者**: Boom-Hacker
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1972

## 描述

*(无描述)*

---

## 评论 (4 条)

### 评论 #1 — hex76db (2023-03-19T03:43:08Z)

Don't even bother buying AMD card for any serious ML, AI work, I have given up at this point, either buy the only 7 supported cards listed here https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html or just buy a RTX 3060 12GiB it should cost the same and it has way better drivers and support.

---

### 评论 #2 — JustGitting (2023-03-25T00:43:39Z)

I've been watching ROCm for a few years now, living in the hope that they'll support more cards, preferably consumer grade and older cards even better...but AMD have gone backwards. 

I think AMD had created a lot of hope and goodwill from the FOSS ML / data science community and those who wanted an alternative to NVidia's hardware/software stack. However, this project is an example of how NOT to run a FOSS project by a vendor.

AMD are free to run this as they like, but it could have been so much better. There is great potential for some truly cool  and useful projects based on this. Without a stable and clear set of supported hardware (and roadmap) no serious work will be done. AMD have done everything to screw this up, why? Limited scope by AMD, insufficient resources, poor policy to focus on enterprise cards, run by bean counters, high turn over of staff, department politics? Who knows... 

Indeed, AMD is the best friend that NVidia could have hoped for. 

Maybe Intel's ARC is suitable for ML / modeling work with a FOSS stack?

---

### 评论 #3 — MartinDxt (2023-07-23T00:12:00Z)

installing rocm on rx6650xt ubuntu
found this post after looking around and since it's a very similar graphics card to the 6600XT (officialy suppoorted) i gave it a shot with very much success

"""
 @brewfalconenterprises
brewfalconenterprises commented Feb 26, 2023

After much trial-and-error, here's the cocktail that I finally got to work on Ubuntu 22.04 bare metal with Navi23 (6600XT). (Both PyTorch and Tensorflow from the command line)

    ROCm 5.4.2
    Python 3.9 (may need to separately install distutils)
    tensorflow-rocm
    pytorch5.2


pterodactyl-soup, valiangspe, GUUser91, Roman2K, ApoorvRChincholkar, and alfinauzikri reacted with thumbs up emoji
"""
from https://github.com/RadeonOpenCompute/ROCm/issues/1698

and follow these steps but use the versions of the one above

https://askubuntu.com/questions/1429376/how-can-i-install-amd-rocm-5-on-ubuntu-22-04

use rocm5.4.2 where you can and python3.9 for me worked
i did fiddle with the openmp-extras5.1.1 version abit before getting it to work
 
Note: it might get hung up on some steps in the "Edit Package 2/2" file edit section but i worked it through easly(half an hour back and forth) there is like a openmp 5.4.2something that is a dev version and there is to repair some missing files but the datafixer handles that so pay attention to the error messages as it's a life saver :D

i guess i'm too stubborn lol

in pycharm venv
Environment variables:

    PYTHONPATH=/usr/bin/python3.9
    ROCM_PATH=/opt/rocm
    HSA_OVERRIDE_GFX_VERSION=10.3.0

pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/rocm5.4.2
"""
python3
import torch
torch.cuda.is_available()
torch.cuda.get_device_name(torch.cuda.current_device())
"""
Output:
"""
/home/martin_dxt/PycharmProjects/pythonProject1/venv/bin/python /home/martin_dxt/PycharmProjects/pythonProject1/main.py 
True
AMD Radeon RX 6650 XT

Process finished with exit code 0
"""
also run some random 7B parameters models locally that use torch on hugging face so hillarious as the small llm are kinda wanky 

haven't tried tensor flow but in theory should work possibly ???

took me overall 2h (llm excluded slow connection) so if you got time to invest and are a dummy at my lvl or above give it a try
honestly total broke noob was able to get it to run with 4h between research and all 

granted i am studying control engineering but i'm not even close of the lvl of some wizards around here or at my University
so not total random idiot i guess

closing remarks personal opinion:
nvidia got complacent at the low end lately, so far have no trouble with drivers or running high fps in games,
if you are a professional in rendering go for nvidia as those rt cores rock for anything ray tracing, but bang for the buck in non rt tasks i'm confident at the low end amd is competing quite well, with the recent effort to get more cards in the rocm world as stated from Lisa Su it might be less troublesome in the future (also a no brainer on their part). as for now this card i did get it to run as it's under the hood a 6600xt with more cooling and better vram (6600xt is supported forgot to metion that) i think so that might be the real reason this is even possible but again i'm no one to comment on that. lastly especially the higher vram makes the amd cards appealing and big models kida eat up that i see no issues with going amd as long as it's form the supported list you can save a pretty penny if money plays no role for you just rent a server and get all the hp you need why even bother training locally. 

for now enjoy ml on a AMD Radeon RX 6650 XT "non compatible rocm card"  ;P

disclaimer issues may araise not my fault do your own reaserch,try at your own risk! hahahaha

fr though it worked. happy to answer any follow up questions so no worries my full log of cmd is still saved so i can go in full detail as well as the files and ouput logs with all the cringe mistakes sigh

---

### 评论 #4 — ppanchad-amd (2024-05-10T18:24:00Z)

@Boom-Hacker Latest ROCm 6.1.1 does not officially support RX 6650XT. Thanks!

---
