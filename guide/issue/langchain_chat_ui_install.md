一、问题根因（3 个核心点）
pnpm 11 安全策略变更：onlyBuiltDependencies 不再支持写在 package.json 的 pnpm 字段里，pnpm 11 会直接忽略。导致 esbuild 等需要编译原生二进制的包被拦截，Docker 构建和本地安装都报 [ERR_PNPM_IGNORED_BUILDS]。
Monorepo workspace 安装范围错误：这个项目根目录和 frontend/ 是 pnpm workspace 结构。根目录只有 18 个 setup 脚本依赖（@clack/prompts 等），真正的 Next.js + React 依赖全在 frontend/package.json 里。在根目录执行 pnpm install 时，只装了根目录的包，frontend 的 600+ 个依赖被跳过。
pnpm store 缓存误导：虽然删了 node_modules，但 pnpm 全局 store 里有缓存，所以一直报 "Already up to date"，实际上 frontend/node_modules/.bin/next 根本不存在。
二、问题现象
pnpm launch 配置向导能跑完，但启动的 dev server 退出后，3001 端口无服务
根目录 pnpm install 只装 18 个包，frontend 的 next 命令找不到
pnpm dev --port 3001 报错：sh: 1: next: not found
Docker 构建卡在 esbuild@0.27.2 脚本被忽略
浏览器访问 3001 显示 Langfuse（实际 3001 无 Chat UI 服务，是缓存/重定向）
三、最终解决步骤（已成功验证）
bash
复制
# 1. 确保 LangGraph 后端在跑（另开终端，不要关）
cd ~/TestCaseAgent
source .venv/bin/activate
langgraph dev

# 2. 在前端目录独立安装（绕过 workspace，避免根目录的 pnpm 11 缓存干扰）
cd ~/TestCaseAgent/etc/langgraph-chat-ui/frontend
rm -rf node_modules
pnpm install --ignore-workspace

# 3. 启动前端开发服务器
pnpm dev --port 3001

# 4. 浏览器访问（手动输入，不要点历史记录）
http://localhost:3001
四、换台电脑/新环境怎么做？
推荐直接用这个简化流程，不要走 pnpm launch 的自动向导（它容易触发 workspace 安装问题）：
bash
复制
# 克隆项目
git clone https://github.com/teddynote-lab/langgraph-chat-ui.git
cd langgraph-chat-ui/frontend

# 复制环境配置模板（根据你的后端地址修改）
cp .env.example .env
# 编辑 .env，确保 LANGGRAPH_API_URL=http://localhost:2024，ASSISTANT_ID=你的graph_id

# 独立安装前端依赖（绕过 monorepo workspace）
pnpm install --ignore-workspace

# 启动
pnpm dev --port 3001
如果那台电脑也是 pnpm 11，且 --ignore-workspace 还是报 esbuild 错误，就先执行：
bash
复制
echo "esbuild" | pnpm approve-builds
pnpm install --ignore-workspace
五、遗留问题 & 注意事项
表格
问题	影响	处理建议
1. 构建脚本被忽略警告	日志里 Ignored build scripts: @swc/core, esbuild, sharp, prisma...	目前 dev 模式能跑，因为 pnpm 10 实际执行了安装。但生产构建 pnpm build 时，如果 sharp 或 prisma 没编译可能报错。需要时再 pnpm approve-builds 全部授权。
2. Next.js workspace root 警告	Detected multiple lockfiles	无害警告。因为 --ignore-workspace 把 frontend 当独立项目装，生成了独立的 pnpm-lock.yaml。要消除警告，可以删除根目录的 pnpm-lock.yaml，或配置 outputFileTracingRoot。
3. /api/auth/session 404	Standalone 无认证模式下，Next.js middleware 仍尝试请求 auth 接口	不影响使用，只是控制台 404 日志，聊天功能正常。
4. 前端连接的是 localhost:2024	如果 LangGraph 后端换端口或改 IP，前端 .env 里的 LANGGRAPH_API_URL 必须同步改	记住：改后端地址 → 改 frontend/.env → 重启 pnpm dev
5. Docker 仍未修复	之前 docker-compose up -d --build 因为同样的 esbuild 问题构建失败	如果要部署到 Docker，需要修改 Dockerfile，在 RUN pnpm install 之前加 RUN pnpm approve-builds esbuild 或改用 npm install。
一句话总结
根因是 pnpm 11 的 workspace + 安全策略双重变化导致 frontend 依赖没装进去。最终解法是：在 frontend 目录里用 pnpm install --ignore-workspace 独立安装，再 pnpm dev 启动。