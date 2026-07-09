# MI250X (gfx90a) not available as cuda device on pytorch

- **Issue #:** 1916
- **State:** closed
- **Created:** 2023-03-03T23:00:30Z
- **Updated:** 2024-10-12T00:55:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/1916

I have MI250X system
![image](https://user-images.githubusercontent.com/122632692/222849737-e039480b-3b6f-4e1b-8334-079d205eefab.png)
with rocm5.4 installed
![image](https://user-images.githubusercontent.com/122632692/222849933-d47b49d4-103d-4256-97ed-28c6b1dac4af.png)
I installed pytorch using following command
`pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/rocm**5.4**/`
notice 5.4 at the end. The installation completed successfully.

But when I use torch.cuda.is_available(), it return False
![image](https://user-images.githubusercontent.com/122632692/222850473-76f4c929-e15c-49bc-bd07-f2cfd6a2e5e6.png)

what am I missing?