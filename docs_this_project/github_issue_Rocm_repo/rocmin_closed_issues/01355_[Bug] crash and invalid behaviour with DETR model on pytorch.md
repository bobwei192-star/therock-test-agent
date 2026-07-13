# [Bug] crash and invalid behaviour with DETR model on pytorch

- **Issue #:** 1355
- **State:** closed
- **Created:** 2021-01-04T09:09:52Z
- **Updated:** 2021-07-29T10:44:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/1355

Running the DETR model from https://github.com/facebookresearch/detr leads to the following issues:
- ROCm spends a lot of time compiling kernels (clang processes spawning all the time and /tmp getting filled with temporary files, presumably the kernels).
- GPU memory usage is abnormally low for the selected batch size.
- Computations seem to be valid (no NaN showing up) althought quite slow.
- Training crashes after a while with:
```
terminate called after throwing an instance of 'miopen::Exception'
  what():  /root/driver/MLOpen/src/hipoc/hipoc_program.cpp:94: Failed creating module hipErrorSharedObjectInitFailed
```

Environment:
- mi50 GPU
- ROCm 3.9
- pytorch from pip package compiled in a centos 8 docker environment
- conda env:
```
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
blas                      1.0                         mkl  
ca-certificates           2020.10.14                    0  
certifi                   2020.6.20          pyhd3eb1b0_3  
cycler                    0.10.0                   pypi_0    pypi
cython                    0.29.21          py38h2531618_0  
intel-openmp              2020.2                      254  
kiwisolver                1.3.1                    pypi_0    pypi
ld_impl_linux-64          2.33.1               h53a641e_7  
libedit                   3.1.20191231         h14c3975_1  
libffi                    3.3                  he6710b0_2  
libgcc-ng                 9.1.0                hdf63c60_0  
libgfortran-ng            7.3.0                hdf63c60_0  
libstdcxx-ng              9.1.0                hdf63c60_0  
matplotlib                3.3.3                    pypi_0    pypi
mkl                       2020.2                      256  
mkl-service               2.3.0            py38he904b0f_0  
mkl_fft                   1.2.0            py38h23d657b_0  
mkl_random                1.1.1            py38h0573a6f_0  
ncurses                   6.2                  he6710b0_1  
numpy                     1.19.2           py38h54aff64_0  
numpy-base                1.19.2           py38hfa32c7d_0  
omegaconf                 2.0.5                    pypi_0    pypi
openssl                   1.1.1h               h7b6447c_0  
pillow                    8.0.1                    pypi_0    pypi
pillow-simd               7.0.0.post3              pypi_0    pypi
pip                       20.2.4           py38h06a4308_0  
pycocotools               2.0.2                    pypi_0    pypi
pyparsing                 2.4.7                    pypi_0    pypi
python                    3.8.5                h7579374_1  
python-dateutil           2.8.1                    pypi_0    pypi
pyyaml                    5.3.1            py38h7b6447c_1  
readline                  8.0                  h7b6447c_0  
scipy                     1.5.2            py38h0b6359f_0  
setuptools                50.3.1           py38h06a4308_1  
six                       1.15.0           py38h06a4308_0  
sqlite                    3.33.0               h62c20be_0  
timm                      0.3.1                    pypi_0    pypi
tk                        8.6.10               hbc83047_0  
torch                     1.8.0a0                  pypi_0    pypi
torchvision               0.9.0a0+74de51d          pypi_0    pypi
typing-extensions         3.7.4.3                  pypi_0    pypi
wheel                     0.35.1             pyhd3eb1b0_0  
xz                        5.2.5                h7b6447c_0  
yaml                      0.2.5                h7b6447c_0  
zlib                      1.2.11               h7b6447c_3  
```

I don't have access to the test server anymore and didn't have admin rights anyways, so a first step would be to have someone else reproduce the problem. I can provide more information on how to do so.