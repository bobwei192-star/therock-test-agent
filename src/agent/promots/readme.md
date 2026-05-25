only for developer reference
模板 适用意图 说明 template_a.md GENERATE/APPEND 创建类 - 完整测试规格模板 template_b.md UPDATE/REFACTOR 修改类 - 带历史代码约束 template_c.md DIAGNOSE/COVERAGE/PROBE 查询诊断类 - 简化模板 template_d.md EXECUTE_EXTERNAL 外部执行类 - 执行规格 template_e.md ENV_BUILD 环境构建类 - Dockerfile 规格

用户输入
   │
   ▼
requirement_parser 节点
   │ 使用 node_requirement_parser.md（节点提示词）
   │ 输出：parsed_intent = "GENERATE"
   ▼
planner 节点
   │ 使用 node_planner.md（节点提示词）
   │ 根据 parsed_intent 选择 create_intent.md（意图提示词）
   ▼
generator 节点
   │ 使用 node_generator.md（节点提示词）
   │ 根据 parsed_intent 选择对应的生成策略
   ▼
sandbox_executor 节点
   │ 使用策略模式执行
   ▼
END


总结 ：节点提示词描述「怎么做」，意图提示词描述「做什么」。两者互补，不需要修改节点提示词文件。 