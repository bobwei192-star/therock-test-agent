# [Issue]: Unable to fine tune Lamma3

- **Issue #:** 4468
- **State:** closed
- **Created:** 2025-03-08T14:05:09Z
- **Updated:** 2025-03-24T17:36:32Z
- **Labels:** Under Investigation, AMD Radeon Pro W7900, ROCm 6.2.3
- **URL:** https://github.com/ROCm/ROCm/issues/4468

### Problem Description

I was following the AMD doc to fine tune lama 3 https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/QLoRA_Llama-3.1.html
and got this issues by the running the cell 
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, 
    bnb_4bit_quant_type="nf4", 
    bnb_4bit_compute_dtype="float16", 
    bnb_4bit_use_double_quant=True
)

# Load the pre-trained Llama-3.1 model with device mapping for GPU
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    device_map="auto",
    quantization_config=bnb_config,
    trust_remote_code=True
)

# Disable caching to optimize for fine-tuning
base_model.config.use_cache = False
base_model.config.pretraining_tp = 1

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In[24], line 9
      1 bnb_config = BitsAndBytesConfig(
      2     load_in_4bit=True, 
      3     bnb_4bit_quant_type="nf4", 
      4     bnb_4bit_compute_dtype="float16", 
      5     bnb_4bit_use_double_quant=True
      6 )
      8 # Load the pre-trained Llama-3.1 model with device mapping for GPU
----> 9 base_model = AutoModelForCausalLM.from_pretrained(
     10     base_model_name,
     11     device_map="auto",
     12     quantization_config=bnb_config,
     13     trust_remote_code=True
     14 )
     16 # Disable caching to optimize for fine-tuning
     17 base_model.config.use_cache = False

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:564](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py#line=563), in _BaseAutoModelClass.from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs)
    562 elif type(config) in cls._model_mapping.keys():
    563     model_class = _get_model_class(config, cls._model_mapping)
--> 564     return model_class.from_pretrained(
    565         pretrained_model_name_or_path, *model_args, config=config, **hub_kwargs, **kwargs
    566     )
    567 raise ValueError(
    568     f"Unrecognized configuration class {config.__class__} for this kind of AutoModel: {cls.__name__}.\n"
    569     f"Model type should be one of {', '.join(c.__name__ for c in cls._model_mapping.keys())}."
    570 )

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/modeling_utils.py:4264](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/modeling_utils.py#line=4263), in PreTrainedModel.from_pretrained(cls, pretrained_model_name_or_path, config, cache_dir, ignore_mismatched_sizes, force_download, local_files_only, token, revision, use_safetensors, weights_only, *model_args, **kwargs)
   4254         load_contexts.append(tp_device)
   4256     with ContextManagers(load_contexts):
   4257         (
   4258             model,
   4259             missing_keys,
   4260             unexpected_keys,
   4261             mismatched_keys,
   4262             offload_index,
   4263             error_msgs,
-> 4264         ) = cls._load_pretrained_model(
   4265             model,
   4266             state_dict,
   4267             loaded_state_dict_keys,  # XXX: rename?
   4268             resolved_archive_file,
   4269             pretrained_model_name_or_path,
   4270             ignore_mismatched_sizes=ignore_mismatched_sizes,
   4271             sharded_metadata=sharded_metadata,
   4272             _fast_init=_fast_init,
   4273             low_cpu_mem_usage=low_cpu_mem_usage,
   4274             device_map=device_map,
   4275             offload_folder=offload_folder,
   4276             offload_state_dict=offload_state_dict,
   4277             dtype=torch_dtype,
   4278             hf_quantizer=hf_quantizer,
   4279             keep_in_fp32_modules=keep_in_fp32_modules,
   4280             gguf_path=gguf_path,
   4281             weights_only=weights_only,
   4282         )
   4284 # make sure token embedding weights are still tied if needed
   4285 model.tie_weights()

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/modeling_utils.py:4777](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/modeling_utils.py#line=4776), in PreTrainedModel._load_pretrained_model(cls, model, state_dict, loaded_keys, resolved_archive_file, pretrained_model_name_or_path, ignore_mismatched_sizes, sharded_metadata, _fast_init, low_cpu_mem_usage, device_map, offload_folder, offload_state_dict, dtype, hf_quantizer, keep_in_fp32_modules, gguf_path, weights_only)
   4773                 set_module_tensor_to_device(
   4774                     model_to_load, key, "cpu", torch.empty(*param.size(), dtype=dtype)
   4775                 )
   4776     else:
-> 4777         new_error_msgs, offload_index, state_dict_index = _load_state_dict_into_meta_model(
   4778             model_to_load,
   4779             state_dict,
   4780             start_prefix,
   4781             expected_keys,
   4782             device_map=device_map,
   4783             offload_folder=offload_folder,
   4784             offload_index=offload_index,
   4785             state_dict_folder=state_dict_folder,
   4786             state_dict_index=state_dict_index,
   4787             dtype=dtype,
   4788             hf_quantizer=hf_quantizer,
   4789             is_safetensors=is_safetensors,
   4790             keep_in_fp32_modules=keep_in_fp32_modules,
   4791             unexpected_keys=unexpected_keys,
   4792         )
   4793         error_msgs += new_error_msgs
   4794 else:
   4795     # Sharded checkpoint or whole but low_cpu_mem_usage==True

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/modeling_utils.py:944](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/modeling_utils.py#line=943), in _load_state_dict_into_meta_model(model, state_dict, start_prefix, expected_keys, device_map, offload_folder, offload_index, state_dict_folder, state_dict_index, dtype, hf_quantizer, is_safetensors, keep_in_fp32_modules, unexpected_keys, pretrained_model_name_or_path)
    942     set_module_tensor_to_device(model, param_name, param_device, **set_module_kwargs)
    943 else:
--> 944     hf_quantizer.create_quantized_param(model, param, param_name, param_device, state_dict, unexpected_keys)
    945     # For quantized modules with FSDP[/DeepSpeed](http://127.0.0.1:8889/DeepSpeed) Stage 3, we need to quantize the parameter on the GPU
    946     # and then cast it to CPU to avoid excessive memory usage on each GPU
    947     # in comparison to the sharded model across GPUs.
    948     if is_fsdp_enabled() or is_deepspeed_zero3_enabled():

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/quantizers/quantizer_bnb_4bit.py:238](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/transformers/quantizers/quantizer_bnb_4bit.py#line=237), in Bnb4BitHfQuantizer.create_quantized_param(self, model, param_value, param_name, target_device, state_dict, unexpected_keys)
    235         new_value = new_value.T
    237     kwargs = old_value.__dict__
--> 238     new_value = bnb.nn.Params4bit(new_value, requires_grad=False, **kwargs).to(target_device)
    240 module._parameters[tensor_name] = new_value

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/bitsandbytes-0.42.0-py3.10.egg/bitsandbytes/nn/modules.py:212](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/bitsandbytes-0.42.0-py3.10.egg/bitsandbytes/nn/modules.py#line=211), in Params4bit.to(self, *args, **kwargs)
    209 device, dtype, non_blocking, convert_to_format = torch._C._nn._parse_to(*args, **kwargs)
    211 if (device is not None and device.type == "cuda" and not self.bnb_quantized):
--> 212     return self._quantize(device)
    213 else:
    214     if self.quant_state is not None:

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/bitsandbytes-0.42.0-py3.10.egg/bitsandbytes/nn/modules.py:184](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/bitsandbytes-0.42.0-py3.10.egg/bitsandbytes/nn/modules.py#line=183), in Params4bit._quantize(self, device)
    182 def _quantize(self, device):
    183     w = self.data.contiguous().cuda(device)
--> 184     w_4bit, quant_state = bnb.functional.quantize_4bit(w, blocksize=self.blocksize, compress_statistics=self.compress_statistics,
    185                                                        quant_type=self.quant_type, quant_storage=self.quant_storage)
    186     self.data = w_4bit
    187     self.quant_state = quant_state

File [/opt/conda/envs/py_3.10/lib/python3.10/site-packages/bitsandbytes-0.42.0-py3.10.egg/bitsandbytes/functional.py:952](http://127.0.0.1:8889/opt/conda/envs/py_3.10/lib/python3.10/site-packages/bitsandbytes-0.42.0-py3.10.egg/bitsandbytes/functional.py#line=951), in quantize_4bit(A, absmax, out, blocksize, compress_statistics, quant_type, quant_storage)
    950     blocks = n // blocksize
    951     blocks += 1 if n % blocksize > 0 else 0
--> 952     absmax = torch.zeros((blocks,), device=A.device, dtype=torch.float32)
    955 if out is None:
    956     mod = dtype2bytes[quant_storage] * 2

RuntimeError: HIP error: invalid device function
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3.
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.

### Operating System

22.04.4 LTS

### CPU

AMD ryzen 9 p00x

### GPU

AMD Radeon PRO w7900

### ROCm Version

6.2.3-124

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_