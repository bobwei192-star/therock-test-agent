# Navi 21 GPU hang when passing wrong input to embedding layer

- **Issue #:** 1724
- **State:** closed
- **Created:** 2022-04-12T00:14:37Z
- **Updated:** 2024-02-02T22:46:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1724

Passing an incorrect value to a `torch.nn.Embedding` layer (i.e. a value greater than the number of unique items an embedding layer is initialized to handle) causes a GPU reset/hang on Navi 21 hardware installed in my system. My hardware specs are as follows:

CPU: Ryzen 5900X
GPU: Radeon 6900XT
RAM: 2x 16GB Crucial Ballistix 3600 CL16
SSD: Crucial MX500
Mobo: MSI X570 Tomahawk

Here's the software configuration:

OS: Debian Testing
Kernel: 5.17.1 (custom compiled)
ROCm version: 5.1
Pytorch version: 1.12.0a0+git364055b (built from source)

It also happens when using the official `rocm5.0.1_ubuntu18.04_py3.7_pytorch_staging` docker image.

Here's the code that causes the issue - it causes an error (but no system/GPU hang) on Nvidia hardware:
```
import torch
import torch.nn as nn
import pytorch_lightning as pl

class MovieLensDummyDataset(torch.utils.data.Dataset):
    #dummy version of the dataset with synthetic data
    def __init__(self, n, n_users, n_movies):

        self.users = torch.randint(0,n_users,(n,)).type(torch.int32)
        self.items = torch.randint(0,n_users,(n,)).type(torch.int32)
        self.labels = torch.randint(0,2,(n,)).type(torch.uint8)

    def __getitem__(self, idx):
        return self.users[idx], self.items[idx], self.labels[idx]

    def __len__(self):
        return self.users.shape[0]


class NCF(pl.LightningModule):
    """ Neural Collaborative Filtering (NCF)
    
        Args:
            num_users (int): Number of unique users
            num_items (int): Number of unique items
            ratings (pd.DataFrame): Dataframe containing the movie ratings for training
            all_movieIds (list): List containing all movieIds (train + test)
    """
    
    def __init__(self, num_users, num_items):
        super().__init__()
        self.user_embedding = nn.Embedding(num_embeddings=num_users, embedding_dim=8)
        self.item_embedding = nn.Embedding(num_embeddings=num_items, embedding_dim=8)
        self.fc1 = nn.Linear(in_features=16, out_features=64)
        self.fc1_activation = nn.ReLU()
        self.fc2 = nn.Linear(in_features=64, out_features=32)
        self.fc2_activation = nn.ReLU()
        self.output = nn.Linear(in_features=32, out_features=1)
        self.out_activation = nn.Sigmoid()

        self.loss_func = nn.BCELoss()
        
    def forward(self, user_input, item_input):
        
        # Pass through embedding layers
        user_embedded = self.user_embedding(user_input)
        item_embedded = self.item_embedding(item_input)

        # Concat the two embedding layers
        vector = torch.cat([user_embedded, item_embedded], dim=-1)

        # Pass through dense layer
        vector = self.fc1_activation(self.fc1(vector))
        vector = self.fc2_activation(self.fc2(vector))

        # Output layer
        pred = self.out_activation(self.output(vector))

        return pred
    
    def training_step(self, batch, batch_idx):
        user_input, item_input, labels = batch
        predicted_labels = self(user_input, item_input)
        loss = self.loss_func(predicted_labels, labels.view(-1, 1).float())
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters())

    def train_dataloader(self):
        return self._train_dataloader

    def set_train_dataloader(self, dl):
        self._train_dataloader = dl

    def set_test_dataloader(self, dl):
        self._test_dataloader = dl

num_users=13849
num_items=19103
num_samples=10142520
#the bug is here - the whole thing works if num_users supplied to the dataset is <= num_users supplied to the model - the issue is about the size of the embedding.
#on nvidia hardware, this bug causes an error and the program stops. on amd hardware, this leads to a GPU hang/reset
train_dummy_ds = MovieLensDummyDataset(num_samples, 10*num_users, num_items)
train_dummy_dl = torch.utils.data.DataLoader(train_dummy_ds, batch_size=2048, num_workers=12)
model = NCF(num_users, num_items)

model.set_train_dataloader(train_dummy_dl)

trainer = pl.Trainer(max_epochs=5,
                     gpus=1,
                     progress_bar_refresh_rate=50,
                     logger=False,
                     checkpoint_callback=False,
                     amp_backend='native')

trainer.fit(model)
```

Here's the kernel log when the GPU hang occurs:

```
Apr 12 00:54:42 hostname kernel: [drm:amdgpu_dm_atomic_commit_tail [amdgpu]] *ERROR* Waiting for fences timed out!
Apr 12 00:54:42 hostname kernel: [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring gfx_0.0.0 timeout, signaled seq=159760, emitted seq=159762
Apr 12 00:54:42 hostname kernel: [drm:amdgpu_job_timedout [amdgpu]] *ERROR* Process information: process gnome-shell pid 2594 thread gnome-shel:cs0 pid 2616
Apr 12 00:54:42 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: GPU reset begin!
Apr 12 00:54:42 hostname kernel: amdgpu: Failed to suspend process 0x8007
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring kiq_2.1.0 test failed (-110)
Apr 12 00:54:43 hostname kernel: [drm:gfx_v10_0_hw_fini [amdgpu]] *ERROR* KGQ disable failed
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring kiq_2.1.0 test failed (-110)
Apr 12 00:54:43 hostname kernel: [drm:gfx_v10_0_hw_fini [amdgpu]] *ERROR* KCQ disable failed
Apr 12 00:54:43 hostname kernel: [drm:gfx_v10_0_hw_fini [amdgpu]] *ERROR* failed to halt cp gfx
Apr 12 00:54:43 hostname kernel: [drm] free PSP TMR buffer
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec68053da00 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec68094d200 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec6804f9600 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec680993200 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec680d5c000 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec680de8000 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec6804e9a00 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec6804eb600 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec680994e00 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: AMD-Vi: Event logged [IO_PAGE_FAULT domain=0x001a address=0xec82bbe3900 flags=0x0010]
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: MODE1 reset
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: GPU mode1 reset
Apr 12 00:54:43 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: GPU smu mode1 reset
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: GPU reset succeeded, trying to resume
Apr 12 00:54:44 hostname kernel: [drm] PCIE GART of 512M enabled (table at 0x0000008000300000).
Apr 12 00:54:44 hostname kernel: [drm] VRAM is lost due to GPU reset!
Apr 12 00:54:44 hostname kernel: [drm] PSP is resuming...
Apr 12 00:54:44 hostname kernel: [drm] reserve 0xa00000 from 0x83fe000000 for PSP TMR
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: SECUREDISPLAY: securedisplay ta ucode is not available
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: SMU is resuming...
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: SMU is resumed successfully!
Apr 12 00:54:44 hostname kernel: [drm] DMUB hardware initialized: version=0x02020003
Apr 12 00:54:44 hostname kernel: [drm] kiq ring mec 2 pipe 1 q 0
Apr 12 00:54:44 hostname kernel: [drm] VCN decode and encode initialized successfully(under DPG Mode).
Apr 12 00:54:44 hostname kernel: [drm] JPEG decode initialized successfully.
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring gfx_0.0.0 uses VM inv eng 0 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring sdma0 uses VM inv eng 12 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring sdma1 uses VM inv eng 13 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring sdma2 uses VM inv eng 14 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring sdma3 uses VM inv eng 15 on hub 0
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring vcn_dec_0 uses VM inv eng 0 on hub 1
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring vcn_enc_0.0 uses VM inv eng 1 on hub 1
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring vcn_enc_0.1 uses VM inv eng 4 on hub 1
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring vcn_dec_1 uses VM inv eng 5 on hub 1
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring vcn_enc_1.0 uses VM inv eng 6 on hub 1
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring vcn_enc_1.1 uses VM inv eng 7 on hub 1
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: ring jpeg_dec uses VM inv eng 8 on hub 1
Apr 12 00:54:44 hostname gnome-shell[2594]: amdgpu: amdgpu_cs_query_fence_status failed.
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: recover vram bo from shadow start
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: recover vram bo from shadow done
Apr 12 00:54:44 hostname kernel: [drm] Skip scheduling IBs!
Apr 12 00:54:44 hostname kernel: [drm] Skip scheduling IBs!
Apr 12 00:54:44 hostname kernel: amdgpu 0000:2f:00.0: amdgpu: GPU reset(2) succeeded!
Apr 12 00:54:44 hostname kernel: [drm] Skip scheduling IBs!
Apr 12 00:54:44 hostname kernel: [drm] Skip scheduling IBs!
Apr 12 00:54:44 hostname kernel: [drm] Skip scheduling IBs!
```

[Here's](https://pastebin.com/J017YHZU) what happens with Nvidia hardware instead (A100, Pytorch 1.11 via docker).
