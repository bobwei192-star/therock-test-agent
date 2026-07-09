# [MI300A] Understanding hipmemcpy() within the framework of unified memory 

- **Issue #:** 3652
- **State:** closed
- **Created:** 2024-08-28T07:49:47Z
- **Updated:** 2024-09-23T00:09:44Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3652

Hi, 

According to MI300A official optimization guide: 
https://hipcub.readthedocs.io/en/rocm-6.2.0/how-to/system-optimization/mi300a.html 

The cpu-gpu bandwidth measured with `rocm_bandwidth` is ~ 58 GB/s for a 4-way MI300A node. 

![image](https://github.com/user-attachments/assets/a27c53ec-7db6-4762-9d49-8c6c5a8eedfb)

The above result is somewhat counter-intuitive.
If the data is located in APU's HBM3 and then loaded into the infinity cache, there should be no memory copy required. 
- How is memory copy defined in this case, i.e. the physical path through which data travels between CPU and GPU ? 
- Is it correct to assume that 0,1,2,3 correspond to the Zen4 CPUs ? 
    - Why is bandwidth between 0-1 pair, which corresponds to zen4-to-zen4 bandwidth, undefined ? 
- What is origin of lack of locality between MI300A ?  
    - 0-4 pair: CPU-GPU within same MI300A 
    - 0-5 pair: CPU-GPU across MI300A   
    - Yet, the bandwidth is uniformly ~ 58 GB/s  
- Conversely, what is the origin of discrepancy between HBMs across MI300A ? 
   - 0-5 pair: CPU-GPU across socket 
   - 4-5 pair : GPU-GPU across socket 
   - From an unified memory point of view, both are just a HBM-to-HBM bandwidth.  
     Yet, the  former is 58 GB/s, and the latter is 116 GB/s 

I appreciate if AMD engineer can help clarify these points. 
These number is underwhelmed in comparison to the theoretical 5.3 TB/s bandwidth of HBM3. 

Thanks. 