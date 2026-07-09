# Help CLBlast (The tuned OpenCL BLAS library) by tuning for more AMD chips

- **Issue #:** 2161
- **State:** closed
- **Created:** 2023-05-22T23:22:39Z
- **Updated:** 2024-08-01T15:14:45Z
- **URL:** https://github.com/ROCm/ROCm/issues/2161

CLBlast ( https://github.com/CNugteren/CLBlast ) is a lightweight, performant, and tunable OpenCL BLAS library.

It is used in, among many other projects, [whisper.cpp](https://github.com/ggerganov/whisper.cpp) , a very popular high-performance inference of [OpenAI's Whisper](https://github.com/openai/whisper).

Unfortunately CLBlast's [the list of already tuned-for devices](https://github.com/CNugteren/CLBlast/blob/master/doc/tuning.md#already-tuned-for-devices) is lacking and there are actually more Nvidia GPUs (which have a better alternative in cuBLAS) than AMD's.

It would be nice to drastically improve the situation. I did my part by sending the tuning results of my AMD card. But that's where my power ends. This current post is the only other avenue I could come up with to help with the efforts.

I kindly implore:
1. If there are people with non-tuned GPUs reading my message, I hope that you decide to make a personal contribution and help the project by tuning it to your GPU.
2. I hope that people from the ROCM project understand the importance of CLBlast and how much AMD/ROCM/AI can be helped by expanding the list of tuned AMD GPUs. You have access to all the GPUs and it would be a trivial small side-project to tune all of them at the same time. If this issue is not up to ROCM people's valley of responsibilities, I hope you will forward my request to other AMD people who can make it happen (be it the marketing or engineering side).

Tuning and submitting the results is very easy:
1. Download https://github.com/CNugteren/CLBlast
2. Tune the entire library for your device by running the following commands (starting from the root of the CLBlast folder):
```
mkdir build
cd build
cmake -DTUNERS=ON ..
make
make alltuners
python ../scripts/database/database.py . ..
make
```
The process will take a couple of hours.
3. Collect all the created `.json` files in the `build` directory, pack them into the .zip file, and send your [tuning results into this post](https://github.com/CNugteren/CLBlast/issues/1).