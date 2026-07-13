# The dmesg Trigger "DQM create queue failed" on rocm-smi by ROCm 1.8.192

- **Issue #:** 506
- **State:** closed
- **Created:** 2018-08-20T13:42:32Z
- **Updated:** 2018-08-21T08:04:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/506

Hi,

These days I found an issue about the consistly executing the rocm-smi by "watch -n 2 /opt/rocm/bin/rocm-smi" , the dmesg will report "DQM create queue failed" as screenshot attached, but the older version ROCm 1.8.1 didn't have this, may someone help to check what problem on ROCm-smi?

![dqm_create_queue_failed](https://user-images.githubusercontent.com/32042214/44343940-e3a9ce80-a4c1-11e8-967c-334ffa76ae0d.png)
