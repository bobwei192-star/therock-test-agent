# Performance Issue on AMD MI300x

- **Issue #:** 4384
- **State:** closed
- **Created:** 2025-02-17T06:36:24Z
- **Updated:** 2025-05-26T19:39:18Z
- **Labels:** Under Investigation, AMD Instinct MI300X
- **URL:** https://github.com/ROCm/ROCm/issues/4384

We are running Pytorch Profiler with 

Model - **Llama 3.3 -70B**
Tensor - **TP4** 
Prompt - **The quick brown fox jumps over the lazy**

and our observation is that accelerator performance is marginal difference but CPU overhead is not able to achieve optimise performance.


![Image](https://github.com/user-attachments/assets/b6faec48-002d-4d81-8825-86ec1b76a316)

![Image](https://github.com/user-attachments/assets/6dbe4eed-a0bf-4dfa-97c9-11b877c5dbc6)

If any further information is required please let me know.