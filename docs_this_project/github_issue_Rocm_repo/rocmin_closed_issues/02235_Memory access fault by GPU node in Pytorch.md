# Memory access fault by GPU node in Pytorch

- **Issue #:** 2235
- **State:** closed
- **Created:** 2023-06-10T14:12:42Z
- **Updated:** 2023-12-05T20:57:51Z
- **Labels:** hardware:Radeon, application:pytorch
- **URL:** https://github.com/ROCm/ROCm/issues/2235

Hi, 
I am running rocm + pytorch. I am using rocm 5.4.2 + Pytorch2.0.0 docker.
I have two types of cards, RX6300, and Radeon VII. RX 6300 worked fine, but when I using Radeon VII, I encountered a memory fault. Codes are shown below:
```
 torch.cuda.set_device(2)
print(f"running with device: {torch.cuda.get_device_name(torch.cuda.current_device())}")
\\ return running with device: AMD Radeon VII
a = torch.rand((1,1)).float()
a.to(torch.device('cuda'))
\\ error messeage: Memory access fault by GPU node-10 (Agent handle: 0x7538750) on address (nil). Reason: Page not present or 
\\ supervisor privilege.
\\ Aborted (core dumped)

\\ sometimes, it return: Segmentation fault (core dumped) 
```

Can anyone help me? Thanks in advance!
