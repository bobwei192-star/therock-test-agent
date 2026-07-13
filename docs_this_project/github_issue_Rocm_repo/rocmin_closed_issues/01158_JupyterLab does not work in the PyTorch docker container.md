# JupyterLab does not work in the PyTorch docker container 

- **Issue #:** 1158
- **State:** closed
- **Created:** 2020-06-22T14:57:11Z
- **Updated:** 2020-06-22T18:41:33Z
- **URL:** https://github.com/ROCm/ROCm/issues/1158

Hello all, 
After running `python3.6 -m pip install jupyterlab && jupyter lab --allow-root` in the official docker container, JupyterLab seems to start, but the web GUI freezes at: 
![image](https://user-images.githubusercontent.com/18728114/85302096-55f8ea80-b46e-11ea-8f1b-f0a463c97370.png)

This issue only exists when `torch` is present in the environment. A new conda environment with python3.6 installed runs `jupyter lab` just fine, but when `torch` is added via symlink, Jupyter Lab freezes on the above screen. 
