# ROCm in 6900xt not recognized

- **Issue #:** 1631
- **State:** closed
- **Created:** 2021-11-29T18:31:47Z
- **Updated:** 2022-02-02T12:34:01Z
- **URL:** https://github.com/ROCm/ROCm/issues/1631

Hello. I am trying to run my pytorch model with the ROCm with my 6900xt. I installed the ROCm 4.5 correctly, it works perfectly with tensorflow. So I moved on and downloaded with docker pull rocm/pytorch:latest, but it wont recognize my GPU. The command I am using is `sudo docker run -it -v $HOME:/data --privileged --rm --device=/dev/kfd --device=/dev/dri --group-add video rocm/pytorch:latest` it gives me the following error:
![image](https://user-images.githubusercontent.com/55565758/143923202-05496d18-7a5a-48cb-9bfe-34946c0bd3fb.png)
