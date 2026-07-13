# process hang up when move a tensor's memory access from GPU to CPU, by calling the function .cpu() or to('cpu') in pytorch

- **Issue #:** 1275
- **State:** closed
- **Created:** 2020-11-03T19:45:12Z
- **Updated:** 2020-11-18T07:44:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1275

### Environment
CPU: AMD Ryzen 4500U
GPU: AMD Vega 6
OS: Ubuntu18.04
ROCM: rocm-3.8.0
PyTorch in Docker: rocm/pytorch:rocm3.8_ubuntu18.04_py3.6_pytorch


### Code
def validate(val_loader, model):
    frame=0
    lastFrameTime = time.time()
    for _, (input, _) in enumerate(val_loader):
        frame=frame+1
        input = input.cuda()

        # interval cost
        predStartTime= time.time()
        
        # predict cost
        with torch.no_grad():
            pred = model(input)
        predEndTime = time.time()
        
        # sync cost
        torch.cuda.synchronize()
        afterSyncTime = time.time()

        # transfer cost
        predOnCpu = pred.detach().cpu()
        cpuGetTime = time.time()

        print("frame:", frame, " interval cost: {:.2f} ms,".format((cpuGetTime - lastFrameTime) * 1000),
              " predict cost: {:.2f} ms,".format((predEndTime - predStartTime) * 1000),
              " sync cost: {:.2f} ms,".format((afterSyncTime - predEndTime) * 1000),
              " transfer cost: {:.2f} ms".format((cpuGetTime - afterSyncTime) * 1000))

        lastFrameTime = cpuGetTime


### Issue description
The "transfer cost" in this issue is the time cost of code "pred.detach().cpu()", it moves the predict result( a tensor) from gpu to cpu. It is expected to be finished in a short time, but in fact, it is different when there is window event happens or not. 

In this case, the window event includes: the mouse swiping on the window, typing in the terminal, a pop-up system notification, etc. 

When there is an window event occurs, the program runs well,  the "transfer cost" time in the range of 0.1~100 ms, the log as follows:
frame: 506  interpret cost: 29.65 ms,  predict cost: 4.52 ms,  sync cost: 11.75 ms,  transfer cost: 1.31 ms
frame: 507  interpret cost: 25.40 ms,  predict cost: 4.58 ms,  sync cost: 3.33 ms,  transfer cost: 16.77 ms
frame: 508  interpret cost: 26.54 ms,  predict cost: 4.32 ms,  sync cost: 7.92 ms,  transfer cost: 13.64 ms
frame: 509  interpret cost: 10.53 ms,  predict cost: 4.88 ms,  sync cost: 4.80 ms,  transfer cost: 0.13 ms
frame: 510  interpret cost: 23.40 ms,  predict cost: 5.31 ms,  sync cost: 6.36 ms,  transfer cost: 6.01 ms
frame: 511  interpret cost: 10.36 ms,  predict cost: 7.02 ms,  sync cost: 2.55 ms,  transfer cost: 0.12 ms
frame: 512  interpret cost: 94.45 ms,  predict cost: 4.57 ms,  sync cost: 5.39 ms,  transfer cost: 58.97 ms
frame: 513  interpret cost: 11.41 ms,  predict cost: 4.28 ms,  sync cost: 6.46 ms,  transfer cost: 0.17 ms


But when there is no trigger, the process may hang up at "pred.detach().cpu()", therefore the "transfer cost" time varies over a huge range of 0.1 ms ~ 31 s, the log as follows:
frame: 41  interpret cost: 1655.17 ms,  predict cost: 5.72 ms  sync cost: 4.02 ms,  transfer cost: 1618.75 ms
frame: 42  interpret cost: 26.36 ms,  predict cost: 4.37 ms  sync cost: 6.36 ms,  transfer cost: 14.89 ms
frame: 43  interpret cost: 10.73 ms,  predict cost: 6.44 ms  sync cost: 3.52 ms,  transfer cost: 0.13 ms
frame: 44  interpret cost: 32.59 ms,  predict cost: 3.87 ms  sync cost: 7.42 ms,  transfer cost: 0.14 ms
frame: 45  interpret cost: 338.07 ms,  predict cost: 4.59 ms  sync cost: 6.19 ms,  transfer cost: 302.71 ms
frame: 173  interpret cost: 11496.98 ms,  predict cost: 4.65 ms  sync cost: 27.61 ms,  transfer cost: 11461.40 ms
frame: 185  interpret cost: 31853.51 ms,  predict cost: 4.92 ms  sync cost: 6.10 ms,  transfer cost: **31818.34** ms
frame: 209  interpret cost: 5575.45 ms,  predict cost: 5.05 ms  sync cost: 5.45 ms,  transfer cost: 5540.12 ms
frame: 212  interpret cost: 5943.54 ms,  predict cost: 4.74 ms  sync cost: 32.25 ms,  transfer cost: 5905.95 ms
frame: 236  interpret cost: 15143.76 ms,  predict cost: 5.22 ms  sync cost: 4.32 ms,  transfer cost: 15110.32 ms
frame: 264  interpret cost: 5693.94 ms,  predict cost: 5.03 ms  sync cost: 4.90 ms,  transfer cost: 5658.51 ms


Could somebody please help with this issue, as the serious delay reduced the frame rate significantly and cannot be applied in real time tasks.