正确做法：CLI 应该极简，只做三件事：
接收用户输入（Typer）
调用现有 Graph 并展示过程（Rich + stream）
关键节点暂停等确认（input/HITL）
三、融合极简方案（推荐）
设计原则
2 个文件搞定：cli.py（入口）+ runner.py（执行+渲染+HITL）
零 Graph 修改：现有 4 节点图完全不动
零记忆代码：用 Agent 已有的 MemorySaver
零外部 API：不调用 Langfuse/LangSmith
只保留 run 命令：先能跑起来，chat/status 后续再说
src/agent/cli/          # 或你现有的目录
├── __init__.py
├── cli.py              # Typer 入口：run 命令
└── runner.py           # 封装：stream + rich + HITL
+-------------+     +-----------------------------+     +-----------------+
|   cli.py    |---->|         runner.py           |---->|  你的现有 Graph  |
|  (Typer)    |     |  +---------------------+    |     | (4节点, 零修改) |
|             |     |  | stream 事件消费     |    |     |                 |
| 接收 prompt |     |  | rich 实时树渲染     |    |     |  requirement_   |
| 传 thread_id|     |  | HITL 终端阻塞       |    |     |  parser -> ...  |
|             |     |  | 结果 Panel 输出      |    |     |                 |
+-------------+     |  +---------------------+    |     +-----------------+
                    +-----------------------------+              |
                                                                 |
                    +-----------------------------+               |
                    |   Agent 层 (已有)           |<--------------+
                    |  MemorySaver (Checkpointer)|
                    |  InMemoryStore (长期记忆)  |
                    +-----------------------------+