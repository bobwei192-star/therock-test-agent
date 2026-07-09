# [Issue]: OOM ERROR on Pytorch Windows preview

- **Issue #:** 5542
- **State:** closed
- **Created:** 2025-10-19T12:38:00Z
- **Updated:** 2025-12-17T19:14:57Z
- **Labels:** status: triage
- **Assignees:** huanrwan-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5542

[###](

<img width="2240" height="1329" alt="Image" src="https://github.com/user-attachments/assets/758c4bcd-e805-4d59-9c82-5c898f49a9be" />

) Problem Description

Frequent OOM errors on using Pytorch for Windows preview. Below are my system specifications:
```
(Get-WmiObject Win32_OperatingSystem).Version: 10.0.26200
(Get-WmiObject win32_Processor).Name: AMD Ryzen 5 7600X 6-Core Processor
(Get-WmiObject win32_VideoController).Name: AMD Radeon RX 7900 XTX
```

```
HIP SDK Libraries: 6.4.0 & 6.2.0
Pytorch Wheels version: 2.8.0a0+gitfc14c65
```

Please let me know if this is to be expected and if there is any other information required from end.

### Operating System

Windows 11

### CPU

AMD Ryzen 5 7600X

### GPU

AMD Radeon 7900XTX

### ROCm Version

6.2

### ROCm Component

HIP

### Steps to Reproduce

Run  the below code:
```python
import torch

class MODEL(torch.nn.Module):
    def __init__(self, in_size=2048, out_size=50000, device="cuda:0"):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=in_size, out_features=out_size, device = device)
        self.layer_norm = torch.nn.LayerNorm(out_size, device = device)
        
    def forward(self, input, mask):
        input += mask
        out = self.linear(input)
        out = self.layer_norm(out)
        print(out.min().item(), out.max().item())
        return out
    
      
        
model = MODEL().half()
for m in model.modules():
    if isinstance(m, (torch.nn.Linear)):
        torch.nn.init.kaiming_normal_(m.weight, nonlinearity='relu')
        if m.bias is not None:
            torch.nn.init.zeros_(m.bias)
            
loss = torch.nn.CrossEntropyLoss(label_smoothing=0.1, ignore_index=3)
optimizer = optimizer = torch.optim.AdamW(model.parameters(), 
                                lr=3e-4,
                                betas=(0.9, 0.999),    # defaults
                                eps=1e-6,              # numerical stability
                                weight_decay=1e-8
                                )
# scaler = torch.amp.GradScaler(device="cuda:0")

for i in range(1,11):
    print(f"Step {i}")
    input = torch.randn(size=(2,8192,2048), device="cuda:0").half()
    target = torch.randint(low = 0, high=50000, size=(2,8192), device="cuda:0", dtype = torch.long)
    mask = (input != 3).to("cuda:0").half()
    # with torch.autocast(device_type="cuda", dtype = torch.float16):
    #     with torch.set_grad_enabled(True):
    out = model.forward(input, mask).to(dtype=torch.float32)
    loss_val = loss(out.view(out.shape[0]*out.shape[1], out.shape[2]), target.view(target.shape[0]*target.shape[1]))
    print(loss_val.item())
    loss_val.backward()
    for name, param in model.named_parameters():
        if param.grad is not None:
            if torch.isnan(param.grad).any() or torch.isinf(param.grad).any():
                print(f"⚠️ NaN/Inf detected in gradient of {name}")
                # Optional: sanitize instead of skipping
                # param.grad = torch.nan_to_num(param.grad, nan=0.0, posinf=1e4, neginf=-1e4)

    optimizer.step()
```
Even a tiny Model like this takes upwards of 17 Gigs of VRAM while training.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_