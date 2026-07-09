# The speed of predict is so slow! 

- **Issue #:** 1564
- **State:** closed
- **Created:** 2021-08-24T09:20:41Z
- **Updated:** 2021-12-13T05:30:24Z
- **URL:** https://github.com/ROCm/ROCm/issues/1564

Hi, everyone. I am meeting a really confusing question!
I use the Super Computing Center in China to accelerate my training process, which deploys the DCU Card and installs the pytorch ROCm whose version is 4.2(beta). 
But I encountered a srange issue:
![image](https://user-images.githubusercontent.com/46133615/130589787-5b55809f-f4d2-481f-a299-e5d57bdd9e58.png)
As the picture above shows, The value in left circle  is time of `out = model(in)` , and the valu in right circle is time of `backward()`.
In NVIDIA's 960, the two value above are both 0.0x. I think this is so weired. The input that was feed to network is an array whose shape is (2500, 12). 
Another, I test on two different Super Compute Center in China. They all have the same problem.
Actually, I know that maybe I have to make some optimization if I want to move from cuda to dcu. But I can't find the solution and I wanna know why.
Thanks vvvvvvery much!!!!!!