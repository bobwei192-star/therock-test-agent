# RuntimeError: miopenStatusUnknownError

- **Issue #:** 1661
- **State:** closed
- **Created:** 2022-01-27T01:37:36Z
- **Updated:** 2022-02-09T12:17:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/1661

 `$ rocminfo
ROCk module is loaded
acgwurvyi7 is member of video group
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
  Name:                    Hygon C86 7185 32-core Processor   
  Marketing Name:          Hygon C86 7185 32-core Processor   
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
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2000                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            8                                  
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32602660(0x1f17a24) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32602660(0x1f17a24) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Acessible by all:        TRUE                               
  ISA Info: `

This show   Device Type:             CPU , but torch.has_cuda return Ture.

When I run my pytorch program,some errors happened ,someone can give me some suggestions?

  `  output = model(tensor_img)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/module.py", line 889, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/public/home/acgwurvyi7/code/myh_code/ml_decoder/src_files/models/tresnet/tresnet_noabn.py", line 231, in forward
    x = self.body(x)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/module.py", line 889, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/container.py", line 119, in forward
    input = module(input)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/module.py", line 889, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/container.py", line 119, in forward
    input = module(input)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/module.py", line 889, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/conv.py", line 399, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/public/home/acgwurvyi7/anaconda3/envs/ML_Decoder/lib/python3.6/site-packages/torch/nn/modules/conv.py", line 396, in _conv_forward
    self.padding, self.dilation, self.groups)
RuntimeError: miopenStatusUnknownError`