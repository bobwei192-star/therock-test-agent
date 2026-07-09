# [Issue]: TensorFlow nan loss with keras.application based model

- **Issue #:** 6379
- **State:** open
- **Created:** 2026-06-23T21:16:26Z
- **Updated:** 2026-06-24T13:12:43Z
- **Labels:** status: triage
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6379

### Problem Description

Using Tensorflow to train a `tf.keras.applications` based model, I get `nan` loss very quickly after some steps.

Current setup :
* TensorFlow : 2.18.1 (also tried latest 2.19)
* Keras : 3.14.1
* NumPy : 2.0.2
* R9700

I originally get this error with a custom code I will not share here as it work with external data.
Things to know is that this code **originally run fine on another computer** with TensorFlow 2.16.2 and a CUDA/RTX setup.

Here is an example of used model
```python
def build_model(input_shape=(256, 256, 1)):
    inputs = tf.keras.Input(shape=input_shape, name="patch_input")

    x = tf.keras.layers.Conv2D(filters=3, kernel_size=1, padding="same", name="channel_adapter")(inputs)
    
    backbone = tf.keras.applications.EfficientNetV2B0(
        include_top=False,
        weights="imagenet",
        #weights=None,
        input_shape=(input_shape[0], input_shape[1], 3),
        include_preprocessing=False
    )
    x = backbone(x)

    x = tf.keras.layers.BatchNormalization(name="head_bn")(x)
    x = tf.keras.layers.Conv2D(512, 4, strides=4, padding="same")(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation("relu")(x)
    x = tf.keras.layers.Conv2D(256, 4, strides=4, padding="same")(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation("relu")(x)
    x = tf.keras.layers.Dropout(0.2, name="head_drop1")(x)
    outputs = tf.keras.layers.Conv2D(1, 1, padding="same", activation="sigmoid", name="output")(x)
    
    return tf.keras.Model(inputs, outputs)

model = build_model()
```

I've dried a lot of variation, dense encoder instead of the current convolutional end, using non-pretrained weights, and a lot more.

Warning : after a lot of time working on that, my code may be a little confused as I searched a lot of different things.

After a lot of search, I found a crappy solution using `clipnorm` with the optimizers, but it does not seem to fix the error for every case see the reproduction part.

### Operating System

Ubuntu 24.04.4 LTS (Noble Numbat)

### CPU

Intel(R) Core(TM) Ultra 7 265

### GPU

AMD Radeon AI PRO R9700 / amdgcn-amd-amdhsa--gfx1201 / amdgcn-amd-amdhsa--gfx12-generic

### ROCm Version

7.2.4

### ROCm Component

_No response_

### Steps to Reproduce

Except from the model build, the rest of the code as been made with LLM and may contain obvious error due to multiple copy/paste changes.
To note, I cannot reproduce the bug with this code on my other setup mention before.

```python
import numpy as np
import tensorflow as tf

print(f"TF    : {tf.__version__}")
print(f"Keras : {tf.keras.__version__}")
print(f"NumPy : {np.__version__}")
print(f"GPUs  : {tf.config.list_physical_devices('GPU')}")

def build_model(input_shape=(256, 256, 1)):
    inputs = tf.keras.Input(shape=input_shape, name="patch_input")

    x = tf.keras.layers.Conv2D(filters=3, kernel_size=1, padding="same", name="channel_adapter")(inputs)
    
    backbone = tf.keras.applications.EfficientNetV2B0(
        include_top=False,
        weights="imagenet",
        #weights=None,
        input_shape=(input_shape[0], input_shape[1], 3),
        include_preprocessing=False
    )
    x = backbone(x)

    x = tf.keras.layers.BatchNormalization(name="head_bn")(x)
    x = tf.keras.layers.Conv2D(512, 4, strides=4, padding="same")(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation("relu")(x)
    x = tf.keras.layers.Conv2D(256, 4, strides=4, padding="same")(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation("relu")(x)
    x = tf.keras.layers.Dropout(0.2, name="head_drop1")(x)
    outputs = tf.keras.layers.Conv2D(1, 1, padding="same", activation="sigmoid", name="output")(x)
    
    return tf.keras.Model(inputs, outputs)

model = build_model()
```

```python
N = 256
X = np.clip(np.random.normal(loc=0.5, scale=0.5, size=(N, 256, 256, 1)), 0, 1).astype(np.float32)
Y = np.random.randint(0, 2, size=(N, 1, 1, 1)).astype(np.float32)
```

```python
print("--- Testing WITHOUT clipnorm ---")
model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.BinaryCrossentropy(),
)

BATCH = 16
for step in range(10):
    xb = X[step * BATCH:(step + 1) * BATCH]
    yb = Y[step * BATCH:(step + 1) * BATCH]
    loss = model.train_on_batch(xb, yb)
    nan_in_weights = any(tf.reduce_any(tf.math.is_nan(v)).numpy() for v in model.trainable_variables)
    print(f"  step {step+1:2d} | loss={loss:.4f} | nan_in_weights={nan_in_weights}")
    if nan_in_weights:
        print("  ^^^ NaN reproduced ^^^")
        break

print("\n--- Testing WITH clipnorm=1000 ---")
model = build_model()
model.compile(
    optimizer=tf.keras.optimizers.Adam(clipnorm=1000.0),
    loss=tf.keras.losses.BinaryCrossentropy(),
)

for step in range(10):
    xb = X[step * BATCH:(step + 1) * BATCH]
    yb = Y[step * BATCH:(step + 1) * BATCH]
    loss = model.train_on_batch(xb, yb)
    nan_in_weights = any(tf.reduce_any(tf.math.is_nan(v)).numpy() for v in model.trainable_variables)
    print(f"  step {step+1:2d} | loss={loss:.4f} | nan_in_weights={nan_in_weights}")
    if nan_in_weights:
        print("  ^^^ NaN reproduced ^^^")
        break

for step in range(10):
    xb = X[step * BATCH:(step + 1) * BATCH]
    yb = Y[step * BATCH:(step + 1) * BATCH]
    loss = model.train_on_batch(xb, yb)
    nan_in_weights = any(tf.reduce_any(tf.math.is_nan(v)).numpy() for v in model.trainable_variables)
    print(f"  step {step+1:2d} | loss={loss:.4f} | nan_in_weights={nan_in_weights}")

print("\n--- Testing WITH clipnorm=10000 ---")
model = build_model()
model.compile(
    optimizer=tf.keras.optimizers.Adam(clipnorm=10000.0),
    loss=tf.keras.losses.BinaryCrossentropy(),
)

for step in range(10):
    xb = X[step * BATCH:(step + 1) * BATCH]
    yb = Y[step * BATCH:(step + 1) * BATCH]
    loss = model.train_on_batch(xb, yb)
    nan_in_weights = any(tf.reduce_any(tf.math.is_nan(v)).numpy() for v in model.trainable_variables)
    print(f"  step {step+1:2d} | loss={loss:.4f} | nan_in_weights={nan_in_weights}")
    if nan_in_weights:
        print("  ^^^ NaN reproduced ^^^")
        break

for step in range(10):
    xb = X[step * BATCH:(step + 1) * BATCH]
    yb = Y[step * BATCH:(step + 1) * BATCH]
    loss = model.train_on_batch(xb, yb)
    nan_in_weights = any(tf.reduce_any(tf.math.is_nan(v)).numpy() for v in model.trainable_variables)
    print(f"  step {step+1:2d} | loss={loss:.4f} | nan_in_weights={nan_in_weights}")
```
```
--- Testing WITHOUT clipnorm ---
  step  1 | loss=0.8145 | nan_in_weights=False
  step  2 | loss=0.9035 | nan_in_weights=True
  ^^^ NaN reproduced ^^^

--- Testing WITH clipnorm=1000 ---
  step  1 | loss=0.8872 | nan_in_weights=False
  step  2 | loss=1.1851 | nan_in_weights=False
  step  3 | loss=1.0735 | nan_in_weights=False
  step  4 | loss=1.1858 | nan_in_weights=False
  step  5 | loss=1.1858 | nan_in_weights=True
  ^^^ NaN reproduced ^^^
  step  1 | loss=nan | nan_in_weights=True
  step  2 | loss=nan | nan_in_weights=True
  step  3 | loss=nan | nan_in_weights=True
  step  4 | loss=nan | nan_in_weights=True
  step  5 | loss=nan | nan_in_weights=True
  step  6 | loss=nan | nan_in_weights=True
  step  7 | loss=nan | nan_in_weights=True
  step  8 | loss=nan | nan_in_weights=True
  step  9 | loss=nan | nan_in_weights=True
  step 10 | loss=nan | nan_in_weights=True

--- Testing WITH clipnorm=10000 ---
  step  1 | loss=0.6031 | nan_in_weights=False
  step  2 | loss=0.7759 | nan_in_weights=False
  step  3 | loss=0.8342 | nan_in_weights=False
  step  4 | loss=0.9754 | nan_in_weights=False
  step  5 | loss=0.9754 | nan_in_weights=True
  ^^^ NaN reproduced ^^^
  step  1 | loss=nan | nan_in_weights=True
  step  2 | loss=nan | nan_in_weights=True
  step  3 | loss=nan | nan_in_weights=True
  step  4 | loss=nan | nan_in_weights=True
  step  5 | loss=nan | nan_in_weights=True
  step  6 | loss=nan | nan_in_weights=True
  step  7 | loss=nan | nan_in_weights=True
  step  8 | loss=nan | nan_in_weights=True
  step  9 | loss=nan | nan_in_weights=True
  step 10 | loss=nan | nan_in_weights=True

```


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
ROCk module version 6.16.13 is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.18
Runtime Ext Version:     1.15
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Core(TM) Ultra 7 265      
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Core(TM) Ultra 7 265      
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
    L1:                      49152(0xc000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   5300                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            20                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Memory Properties:       
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32297504(0x1ecd220) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32297504(0x1ecd220) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32297504(0x1ecd220) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 4                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32297504(0x1ecd220) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-9596cf8c04e7cb66               
  Marketing Name:          AMD Radeon AI PRO R9700            
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
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30033(0x7551)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2350                               
  BDFID:                   1024                               
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        2147483647(0x7fffffff)             
    y                        65535(0xffff)                      
    z                        65535(0xffff)                      
  Max fbarriers/Workgrp:   32                                 
  Packet Processor uCode:: 128                                
  SDMA engine uCode::      662                                
  IOMMU Support::          None                               
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    31309824(0x1ddc000) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Recommended Granule:2048KB                             
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Recommended Granule:0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx1201         
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
    ISA 2                    
      Name:                    amdgcn-amd-amdhsa--gfx12-generic   
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
        x                        2147483647(0x7fffffff)             
        y                        65535(0xffff)                      
        z                        65535(0xffff)                      
      FBarrier Max Size:       32                                 
*** Done **
```

</details>


### Additional Information

Some code I used to debug on my real data setup :

```python
import gc

optimizers_to_test = {
    "Adam clipnorm=100": tf.keras.optimizers.Adam(clipnorm=100.0),
    "Adam clipnorm=1000": tf.keras.optimizers.Adam(clipnorm=1000.0),
    "Adam clipvalue=100": tf.keras.optimizers.Adam(clipvalue=100.0),
    "SGD momentum": tf.keras.optimizers.SGD(learning_rate=1e-3, momentum=0.9, nesterov=True),
    "AdamW clipnorm=100": tf.keras.optimizers.AdamW(clipnorm=100.0),
    "RMSprop": tf.keras.optimizers.RMSprop(learning_rate=1e-4),
    "Nadam": tf.keras.optimizers.Nadam(learning_rate=1e-4),
}

gen = batch_generator(Xt, Yt, BATCH_SIZE, shuffle=False)
batches = [next(gen) for _ in range(20)]  # pre-fetch so all tests use same data

for opt_name, opt in optimizers_to_test.items():
    model = build_model(2)
    model.compile(optimizer=opt, loss=tf.keras.losses.BinaryCrossentropy())
    
    broke_at = None
    for step, (xb, yb) in enumerate(batches):
        model.train_on_batch(xb, yb)
        if any(tf.reduce_any(tf.math.is_nan(v)).numpy() for v in model.trainable_variables):
            broke_at = step + 1
            break
    
    print(f"{'NaN at step '+str(broke_at) if broke_at else 'OK (20 steps)':<20} | {opt_name}")
    del model
    gc.collect()
```

```
OK (20 steps)        | Adam clipnorm=100
OK (20 steps)        | Adam clipnorm=1000
OK (20 steps)        | Adam clipvalue=100
NaN at step 2        | SGD momentum
OK (20 steps)        | AdamW clipnorm=100
OK (20 steps)        | RMSprop
NaN at step 2        | Nadam
```

Also using no gpu does not fix the problem :
```
import os
os.environ["HIP_VISIBLE_DEVICES"] = ""
```