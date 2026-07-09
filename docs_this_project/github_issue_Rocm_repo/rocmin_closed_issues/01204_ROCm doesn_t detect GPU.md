# ROCm doesn't detect GPU.

- **Issue #:** 1204
- **State:** closed
- **Created:** 2020-08-25T14:05:55Z
- **Updated:** 2021-01-08T05:27:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1204

My laptop: ASUS TUF Gaming FX505DY-BQ024T.
I'm trying to set it up so that I can do mild training and running of TF models for my projects.
There's an internal Vega graphics as well as dedicated RX 560X 4GB.
I can't get the ROCm to detect my GPU using rocminfo or clinfo. Both int gpu and dedicated are detected in rocm-smi. What do I do?
rocminfo shows the resource exhausted problem. clinfo shows the number of devices as 0.
I'm using Ubuntu 20.04.1.
Should I change my ubuntu version or something?