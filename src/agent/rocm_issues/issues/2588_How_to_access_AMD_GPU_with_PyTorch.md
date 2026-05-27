# How to access AMD GPU with PyTorch

> **Issue #2588**
> **状态**: closed
> **创建时间**: 2023-10-20T05:20:32Z
> **更新时间**: 2023-10-23T08:17:34Z
> **关闭时间**: 2023-10-23T08:14:23Z
> **作者**: Aditya-Scalers
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2588

## 描述

Using PyTorch we are able to access AMD GPU by specifying device as 'cuda'.
Is this the recommended way to access AMD GPU through PyTorch ROCM?
What about 'hip' as a parameter for device?

```
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2', device_map="auto")
model = GPT2LMHeadModel.from_pretrained('gpt2', device_map="auto")
prompt = "What is Quantum Computing?"

encoded_input = tokenizer(prompt, return_tensors='pt')
encoded_input = encoded_input.to('cuda')

output = model.generate(**encoded_input, max_length=100)
print(tokenizer.decode(output[0], skip_special_tokens = True))
```


