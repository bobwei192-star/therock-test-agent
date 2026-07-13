# [Question] Typical power sensor update intervals and accuracy

- **Issue #:** 1649
- **State:** closed
- **Created:** 2021-12-28T14:09:40Z
- **Updated:** 2023-03-31T10:16:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/1649

For a thesis, I am currently evaluating on-board power monitoring facilities of different CPUs and GPUs in the field of scientific computing.
In the documentation of the SMI, I found out that many power and energy metrics as well  as information on the respective accuracy and update interval are exposed through the sysfs interface and can be updated by the GPU during runtime (c.f. https://rocmdocs.amd.com/en/latest/ROCm_System_Managment/ROCm-System-Managment.html). Unfortunately, I do not have a supported GPU available to investigate this.
Are there any further information on details of the power sensors available? Specifically, I am interested in typical values for update_interval, power[1-*]_average_interval, and power[1-*]_accuracy for an exemplary device. Thanks in advance!