# Performance drop between 5.3 and 5.4 with the RX6700s on resnet50

- **Issue #:** 1877
- **State:** closed
- **Created:** 2022-12-14T16:39:07Z
- **Updated:** 2024-02-25T04:33:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1877

After installing rocm 5.4 on a fresh install of Ubuntu 22.10 I get a performance drop compared to rocm 5.3 on the same OS/hardware


Steps to reproduce:
```
pip3 install tensorflow-rocm
git clone https://github.com/tensorflow/benchmarks.git
cd benchmarks/scripts/tf_cnn_benchmarks
export HSA_OVERRIDE_GFX_VERSION=10.3.0
python3 tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50
```
Results:

- with 5.3 : **total images/sec: 97.40**
- with 5.4 : **total images/sec: 80.03**

Specs:

- Ubuntu 22.10 - Kernel 5.19.X
- Asus g14 2022 laptop
- RX 6700s  8GB
- R7 6800HS 16GB DDR5