# Abnormal performance with RX 7900XTX+ROCm 6.4.1+PyTorch

- **Issue #:** 5040
- **State:** open
- **Created:** 2025-07-14T13:51:54Z
- **Updated:** 2025-07-22T19:53:08Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5040

Dear all,
I was performing a simple case from [https://discuss.pytorch.org/t/timings-for-intel-arc-graphics-xpu-vs-nvidia-rtx-3000-gpu-on-a-laptop/218200/2](https://discuss.pytorch.org/t/timings-for-intel-arc-graphics-xpu-vs-nvidia-rtx-3000-gpu-on-a-laptop/218200/2) to test the timing of 7900XTX with nightly built of PyTorch (today). However, it produced the performance way below other devices as indicated by pyfan in the link.
7900XTX took around 53 seconds, which seems to be too slow.

/home/jc/PycharmProjects/PythonProject/.venv/bin/python /home/jc/PycharmProjects/PythonProject/t1.py 
2.9.0.dev20250713+rocm6.4
True
version.cuda: None
Radeon RX 7900 XTX
_CudaDeviceProperties(name='Radeon RX 7900 XTX', major=11, minor=0, gcnArchName='gfx1100', total_memory=24560MB, multi_processor_count=48, uuid=35626461-6536-3132-3434-633261393430, pci_bus_id=45, pci_device_id=0, pci_domain_id=0, L2_cache_size=6MB)
device: cuda
lossInit: tensor(0.7298, device='cuda:0', grad_fn=<MseLossBackward0>)
lossFinl: tensor(0.0299, device='cuda:0', grad_fn=<MseLossBackward0>)
device: cuda  time: 53.3579    nBatch: 100000  nEpoch: 1000

Process finished with exit code 0

Best wishes
