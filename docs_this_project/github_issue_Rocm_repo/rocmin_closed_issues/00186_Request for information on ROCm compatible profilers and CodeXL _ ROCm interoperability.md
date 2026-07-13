# Request for information on ROCm compatible profilers and CodeXL / ROCm interoperability

- **Issue #:** 186
- **State:** closed
- **Created:** 2017-08-24T04:44:00Z
- **Updated:** 2017-10-17T14:01:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/186

Just wanting to check in on how to optimize for AMD cards these days.

Last time I tried CodeXL out on a system without an AMD card, I couldn't get the main window to appear (IIRC I had this issue in various forms ~ 4 years ago on completely different computers/laptops).  It did work when using on a machine offering firegl drivers + opengl (which is where I think the problem happened...)

Just checked in here:
http://rocm-documentation.readthedocs.io/en/latest/ROCm_GPU_Tunning_Guides/ROCm-GPU-Tunning-Guides.html#vega-tuning-guide
and
http://rocm-documentation.readthedocs.io/en/latest/ROCm_Tools/ROCm-Tools.html

https://github.com/GPUOpen-Tools/GPA/blob/master/GPUPerfAPI/doc/GPUPerfAPI-UserGuide.pdf [dead]
https://github.com/RadeonOpenCompute/ROCm-Profiler/blob/master/README.md (looks like this is a branch of codexl, but hasn't been touched since november 2016)

Which listed but did not inform to the status of tools/apis such as CodeXL, ROCm-Profiler / profiling apis.  Have these been shown to work seamlessly with HIP?

Also, it sounded like no build was available that worked with rocm per that ROCm-Profiler readme - is that still the case with the select distro packages the ROCm project makes available?
