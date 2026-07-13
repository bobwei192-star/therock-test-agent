# Rocm performance low issue with HIP-Examples-master/gpu-burn

- **Issue #:** 491
- **State:** closed
- **Created:** 2018-08-06T08:07:51Z
- **Updated:** 2023-12-12T21:50:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/491

Hi, 
    I met with rocm1.8 +ubuntu18.04 LTS + 2 cards Ellesmere [Radeon RX 470/480] performance low issue.
    I ran hip example code to burn gpu to check performance,  the code I run is the HIP examples: HIP-Examples-master/gpu-burn. 
    While gpu burnning, rocm-smi showed that MCLK has only 500M, but SCLK increased to 1130MHz from 300MHz in idle.
     I could use rocm-smi -d 1 --setmclk 2 to change MCLK to 2000M, rocm-smi showed it changed to 2000M but performance not increase at all,  I think GPU not really worked at 2000MHz.

     So my question is:
     1. Why gpu performance is slow under gpu-burn, what can I try to increase performance?
     2. Is it related to 500M MCLK  ?
     3. MCLK changed to 2000M not really work, right?
  
idle:

 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   35c     30.178W  300Mhz   500Mhz   0.0%     manual    0%         0%       
  0   34c     32.244W  300Mhz   500Mhz   0.0%     manual    0%         0%       

While burning:

 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   45c     104.171W 1130Mhz  500Mhz   0.0%     manual    0%         0%       
  0   43c     98.192W  1130Mhz  500Mhz   0.0%     manual    0%         0%       

After rocm-smi -d 1 --setmclk 2

 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  1   38c     32.153W  300Mhz   2000Mhz  0.0%     manual    0%         0%       
  0   36c     34.176W  300Mhz   2000Mhz  0.0%     manual    0%         0%       