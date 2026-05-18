#!/usr/bin/env python3
import deepagents
import inspect

print("=== deepagents 模块内容 ===")
items = [x for x in dir(deepagents) if not x.startswith('_')]
for item in items:
    obj = getattr(deepagents, item)
    if inspect.isfunction(obj) or inspect.isclass(obj):
        print(f"  {item}: {type(obj).__name__}")

# 尝试找 agent 相关的
print("\n=== 可能的 Agent 入口 ===")
for item in items:
    if 'agent' in item.lower():
        print(f"  - {item}")