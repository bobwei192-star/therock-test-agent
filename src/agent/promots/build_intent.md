## 意图识别
意图: ENV_BUILD

## 构建规格输出
1. 构建目标: <一句话，如"编译 ROCm 6.0 + PyTorch 2.3 + LLVM 17 的测试基础镜像">
2. 基础镜像: <如 rocm/dev-ubuntu-22.04:6.0>
3. ROCm 组件清单:
   - <组件1>: <版本/分支> | <安装方式: apt/源码编译/官方wheel>
4. 第三方依赖:
   - <PyTorch>: <版本> | <构建方式>
   - <LLVM>: <版本> | <构建方式>
5. 构建阶段设计:
   - Stage 1 (系统层): <apt update/install 基础工具>
   - Stage 2 (ROCm层): <安装/验证 ROCm 核心库>
   - Stage 3 (Python层): <pip install / 编译 PyTorch>
   - Stage 4 (验证层): <rocm-smi 探测、CUDA 可用性检查>
6. 缓存与体积优化:
   - 层缓存策略: <哪些指令合并以减少层数>
   - 清理动作: <apt clean / pip cache purge>
7. 运行时约束:
   - 设备挂载: </dev/kfd,/dev/dri>
   - 环境变量: <HSA_OVERRIDE_GFX_VERSION / PYTORCH_ROCM_ARCH>
8. 验证脚本:
   - 自检命令: <rocm-smi、python -c "import torch; print(torch.cuda.is_available())">
9. 输出物:
   - Dockerfile 片段或完整文件
   - build.sh（含 docker buildx 命令、标签策略）