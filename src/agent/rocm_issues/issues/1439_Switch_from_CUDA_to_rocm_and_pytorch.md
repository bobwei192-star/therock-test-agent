# Switch from CUDA to rocm and pytorch 

> **Issue #1439**
> **状态**: closed
> **创建时间**: 2021-04-05T10:28:40Z
> **更新时间**: 2021-04-16T11:44:16Z
> **关闭时间**: 2021-04-16T11:44:16Z
> **作者**: daniele777
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1439

## 描述

Guys i uninstall CUDA toolkit and Torch because i have AMD video card but now i Discover can i use my and video card ..
Reboot After i install pip3 install Torch -f .../whl/rocm4.0/torch_stable download start ...but failed install.. help

---

## 评论 (8 条)

### 评论 #1 — ROCmSupport (2021-04-06T07:06:19Z)

Hi @daniele777 
Thanks for reaching out.
Can you please share the exact steps to reproduce the problem.
And also request you to share the GPU name, OS, kernel version, ROCm version, outputs of /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo.
Thank you.


---

### 评论 #2 — daniele777 (2021-04-07T05:07:00Z)

https://github.com/LearnedVector/A-Hackers-AI-Voice-Assistant

I setting up ambient and all ok when i train neural network based pytorch  i use this Command :

python3 train.py --sample_rate 8000 --epochs 100 --batch_size 32 --eval_batch_size 32 --lr 0.0001 --model_name ./new_wakeword_v0 --save_checkpoint_path neuralnet/checkpoints --train_data_json data/json/train.json --test_data_json data/json/test.json --num_workers 4 --hidden_size 64

 I have slow process

So i try to switch from CUDA toolkit and standard pytorch uninstalling CUDA and pytorch...

I install ok Torch 1.8.1 +Rocm 4.0.1
But now i have problem in running train Say UnboundLocalError local variabile file_path referrenced  before assignement

Also there is a different Command to train he Ask --gpus ??
BestRegards 


---

### 评论 #3 — ROCmSupport (2021-04-07T12:47:20Z)

Hi @daniele777, sorry for the repeated question.
Can I know the exact steps to reproduce the problem? Do you want me to follow https://github.com/LearnedVector/A-Hackers-AI-Voice-Assistant?
Can I try it on MI50 + ROCm 4.0.1? Please share more details if any.
If the steps are very clear, I can try and update asap.
Thanks for understanding.

---

### 评论 #4 — ROCmSupport (2021-04-09T09:52:16Z)

Hi @daniele777 
Please share an update so that we can work for you and will update with resolution.
Thank you.

---

### 评论 #5 — daniele777 (2021-04-10T12:09:55Z)

First of all i can use ROMc use GPU to train Ai with pytorch ?

I follow read me installation instead a https://github.com/LearnedVector/A-Hackers-AI-Voice-Assistant but i replace Torch with rocm
He train well with pytorch 1.7.1
But thinking of  i install opencl next CUDA use my AMD video card during training .?

---

### 评论 #6 — AGenchev (2021-04-13T07:26:19Z)

@daniele777 if you have: Radeon RX Vega 64, AMD Radeon VII **AND** Ubuntu version 18.04 or 20.04 you can make it work. 
(I assume you **don't have** Radeon Instinct). Read "Supported GPUs" section.
Beware the project you read has mixed tensorflow 2.3 and pytorch 1.7.1 in requirements.txt, so it might fail for other reasons.
Hip does **NOT** work on AMD APU videocards (and AMD does not have anything like Nvidia Jetson though they could) so torch and tensorflow will not accelerate on APU videocards.

---

### 评论 #7 — ROCmSupport (2021-04-16T11:00:25Z)

Hi @daniele777 
Yes, you can use ROCm + Supported GPU to train AI with pytorch.
Request you to close this ticket if you do now have any more issues.
Thank you.

---

### 评论 #8 — daniele777 (2021-04-16T11:44:13Z)

Ok thx 

---
