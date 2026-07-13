# HIP out of memory: running Pytorch with ROCm on Windows with over ~16GB of shared graphics memory

- **Issue #:** 5882
- **State:** open
- **Created:** 2026-01-22T16:00:03Z
- **Updated:** 2026-06-17T18:58:27Z
- **Labels:** Windows, application:pytorch, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5882

Dear ROCm developers:

When I'm trying to testing LLM and Z-image models on my ROG FLOW Z13, If I assign a total shared graphics memory of over ~16 GB to 8060s graphics core, The Pytorch would always told me a Out Of Memeoy Error, but at that time Pytorch could still detect the correct number of shared grahics memory, followed information shows "allocate 0 , allocated 0". I've found this fault could be fixed in Linux by upgrading the 6.16 kernel, but now I'm in Windows enviorment, so is there some way to avoid it or any future fix?
This problem appears both in ROCm 7.1.1 with 25.20 adrenalin catalyst and the newly issued ROCm 7.2 with 26.1.1 adrenalin catalyst.

Here are some informations:
windows version: windows 11 home 25H2
adrenalin catalyst version: 26.1.1
ROCm version: 7.2
Pytorch version: 2.9.1
Hardware platform: ROG FLOW Z13, AMD AI MAX+ 395, 128GB memory with 64GB assigned to intergrated graphics (AMD 8060S)

<img width="2560" height="1599" alt="Image" src="https://github.com/user-attachments/assets/536fca07-a5f9-46fc-9362-a5b25972cb0e" />

<img width="2560" height="1600" alt="Image" src="https://github.com/user-attachments/assets/aa066248-43eb-47c2-8238-9988ec648c30" />