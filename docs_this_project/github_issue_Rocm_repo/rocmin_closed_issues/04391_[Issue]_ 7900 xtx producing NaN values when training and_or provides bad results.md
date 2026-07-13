# [Issue]: 7900 xtx producing NaN values when training and/or provides bad results.

- **Issue #:** 4391
- **State:** closed
- **Created:** 2025-02-18T21:57:49Z
- **Updated:** 2025-03-18T14:41:10Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/4391

### Problem Description

I had two issues when training, NaN values and poor accuracy, tested on two models. Both models is pulled from HF. Full training passes has been successful using nvidia GPU's, and partial training (reduced dataset) has been successful using apple ARM chips - neither of which suceeded on 7900 XTX.

Issues:
1. NaN values start appearing after a few thousand steps when fine tuning bert from google, specifically "google/bert-base-multilingual-uncased".
2. Accuracy is very, very poor when training succeeds on fine tuning facebooks model roberta-base, specifically "roberta-base".  When fine-tuning on apple/nvidia, we reach ~98% accuracy. on amd we reach ~35% accuracy, clearly denoting an issue.

Furthermore, both bert and roberta produces NaN values when enabling mixed precision. Bert produces NaN values regardless of precision.

The original script which is provided below uses HF wrappers. Script has been rewritten using only torch and transformers in an attempt to improve results, but to no avail.

### Operating System

24.04.01 LTS

### CPU

ryzen 9700x

### GPU

7900 xtx

### ROCm Version

ROCm 6.3.2

### ROCm Component

_No response_

### Steps to Reproduce

1. Download radeon driver and ROCm from [amds official site](https://www.amd.com/en/support/download/linux-drivers.html)
2. Instantiate venv using python 3.11.9
3. Install dependencies: 
`sentence-transformers = "^3.3.1"
sentencepiece = "^0.2.0"`
4. pip install torch. Will uninstall torch from sentence-transformers and install correct version - "pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2.4"
5. Add some data. My dataset is propeitary and written in danish. Thus special chars "åæø" is prevelant. Token size for all entries is <100 with ~2 million entries.  

```
from sentence_transformers import CrossEncoder, InputExample
from torch.utils.data import DataLoader
from sentence_transformers.cross_encoder.evaluation import CEBinaryClassificationEvaluator
import math
import os
import torch
from sklearn.model_selection import train_test_split

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # To ensure onboard graphics is not chosen.

def some_cross_encoder(X_train, y_train, X_val, y_val, epochs=5, batch_size=32, learning_rate=2e-5, model_folder_name="version"):
    model = CrossEncoder('google/bert-base-multilingual-uncased', num_labels=1)

    # model.model.to(torch.float32)
    device = "cuda" if torch.cuda.is_available() else "cpu" 
    model.model.to(device)

    train_examples = [InputExample(texts=[sent1, sent2], label=label) for (sent1, sent2), label in zip(X_train, y_train)]
    val_examples = [InputExample(texts=[sent1, sent2], label=label) for (sent1, sent2), label in zip(X_val, y_val)]
    
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=batch_size)
    evaluator = CEBinaryClassificationEvaluator.from_input_examples(val_examples, name="Evaluate dataset")

    warmup_steps = math.ceil(len(train_dataloader) * epochs * 0.1) 
    model.fit(
        train_dataloader=train_dataloader,
        evaluator=evaluator,
        epochs=epochs,
        warmup_steps=warmup_steps,
        optimizer_params={'lr': learning_rate},
        save_best_model=True,
        output_path=(model_folder_name + '_best'),
    )

    model.save(model_folder_name)

    return model

# X: [(str, str)], y: [float]
X_t, X_v, y_t, y_v = train_test_split(X, y, test_size=0.1, random_state=42)
some_cross_encoder(X_t, X_v, y_t, y_v)
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_