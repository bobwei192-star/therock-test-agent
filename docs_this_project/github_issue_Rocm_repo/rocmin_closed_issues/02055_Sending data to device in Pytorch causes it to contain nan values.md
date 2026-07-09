# Sending data to device in Pytorch causes it to contain nan values

- **Issue #:** 2055
- **State:** closed
- **Created:** 2023-04-16T17:53:42Z
- **Updated:** 2024-05-10T19:02:38Z
- **URL:** https://github.com/ROCm/ROCm/issues/2055

Pytorch Version 2.0 ROCm version 5.4.2 on Linux Mint 20.3 (Ubuntu 20.04)

Initiating checking for cuda device results in the following warning.
`/home/sm/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")` 

`torch.cuda.is_available()` comes out as `True`

`print(torch.cuda.get_device_name(device=device))` shows simply AMD Radeon Graphics instead of AMD 6950XT.

Onto to the problem, my loss and model outputs were showing nan, puzzled I went back and checked the data for nan, which also showed it to be True. This was odd as I had previously run the code on Kaggle notebooks, which didn't show it to be a problem. I then decided to test it with random data and the data was still showing it containing nan. I then checked it before sending it `.to(device)` and after, and as expected initial data did not contain nan values but after `.to(device)` it did. Following is the code for testing.

    device = torch.device("cuda" if (torch.cuda.is_available()) else "cpu")
    model = ENet(3,2)
    model.to(device)
    criterion = nn.BCELoss()
    opt = torch.optim.Adam(model.parameters(), lr = 1e-4)

    for i in range(10):

      data = torch.rand(3,3,512,512).float()
      print('Initial Data nan', torch.any(torch.isnan(data)))
      labels =torch.randint(low = 0, high = 2, size = (3,2)).float()
      data = data.to(device)
      print('Device Data nan',torch.any(torch.isnan(data)))
      labels = labels.to(device)

      output = model(data)
      loss = criterion(output, labels)
      loss.backward()
      opt.step()
      opt.zero_grad()

The output for the first loop is 

    Initial Data nan tensor(False)

    Device Data nan tensor(True, device='cuda:0')


The problem is agnostic to the model or data (even doing to randomly generated data), but the following is a basic model for anyone wanting to replicate and troubleshoot. Uses the package timm for efficientnet. I have tried it on a Resnet model (not from timm but locally coded) with the same error.

    class ENet(nn.Module):
        def __init__(self, in_channels, num_classes):
            super(ENet, self).__init__()
            
            self.first_conv = nn.Conv2d(in_channels = in_channels, out_channels = 3, kernel_size = 1)
            self.backbone = timm.create_model('efficientnet_b0', pretrained = False)
            self.relu = nn.ReLU()
            self.classifier = nn.Linear(1000,num_classes)
            self.softmax = nn.Softmax(dim = -1)
            
        def forward(self, x):
            out = self.first_conv(x)
            out = self.relu(out)
            out = self.backbone(out)
            out = self.relu(out)
            out = self.classifier(out)
            out = self.softmax(out)
            return out

below is an excerpt from `rocminfo` My card is 6950 XT but agent 2 shows as gfx1030, not sure if that's relevant, along with the initial warning of NVML.

    ROCk module is loaded
    =====================    
    HSA System Attributes    
    =====================    
    Runtime Version:         1.1
    System Timestamp Freq.:  1000.000000MHz
    Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
    Machine Model:           LARGE                              
    System Endianness:       LITTLE                             
    
    ==========               
    HSA Agents               
    ==========               
    *******                  
    Agent 1                  
    *******                  
      Name:                    AMD Ryzen 7 3700X 8-Core Processor 
      Uuid:                    CPU-XX                             
      Marketing Name:          AMD Ryzen 7 3700X 8-Core Processor 
      Vendor Name:             CPU                                
      Feature:                 None specified                     
      Profile:                 FULL_PROFILE                       
      Float Round Mode:        NEAR                               
      Max Queue Number:        0(0x0)                             
      Queue Min Size:          0(0x0)                             
      Queue Max Size:          0(0x0)                             
      Queue Type:              MULTI                              
      Node:                    0                                  
      Device Type:             CPU                                
    
    *******                  
    Agent 2                  
    *******                  
      Name:                    gfx1030                            
      Uuid:                    GPU-618b03fa3848708f               
      Marketing Name:                                             
      Vendor Name:             AMD                                
      Feature:                 KERNEL_DISPATCH                    
      Profile:                 BASE_PROFILE                       
      Float Round Mode:        NEAR                               
      Max Queue Number:        128(0x80)                          
      Queue Min Size:          64(0x40)                           
      Queue Max Size:          131072(0x20000)                    
      Queue Type:              MULTI                              
      Node:                    1                                  
      Device Type:             GPU                                
      ASIC Revision:           1(0x1)                             
      Cacheline Size:          64(0x40)                           
      Max Clock Freq. (MHz):   2720                                                          
      ISA Info:                
        ISA 1                    
          Name:                    amdgcn-amd-amdhsa--gfx1030         
          Machine Models:          HSA_MACHINE_MODEL_LARGE            
          Profiles:                HSA_PROFILE_BASE                   
          Default Rounding Mode:   NEAR                               
          Default Rounding Mode:   NEAR                               
          Fast f16:                TRUE                               
          Workgroup Max Size:      1024(0x400)                        
          Workgroup Max Size per Dimension:
            x                        1024(0x400)                        
            y                        1024(0x400)                        
            z                        1024(0x400)                        
          Grid Max Size:           4294967295(0xffffffff)             
          Grid Max Size per Dimension:
            x                        4294967295(0xffffffff)             
            y                        4294967295(0xffffffff)             
            z                        4294967295(0xffffffff)             
          FBarrier Max Size:       32                                 
    *** Done ***         

Any help would be appreciated, thanks.