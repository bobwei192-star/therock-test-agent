import os
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

# 1. 初始化模型（deepagents 对模型无依赖，任意支持 tool-calling 的即可）
model = init_chat_model("openai:gpt-4o")  
# 如果成本敏感，可换 gpt-4o-mini 或本地模型：
# model = init_chat_model("openai:gpt-4o-mini")

# 2. 定义 Agent 角色：只生成 pytest，不写其他内容
SYSTEM_PROMPT = """\
你是一个 AMD ROCm 测试用例生成助手。你的唯一任务是：把用户的自然语言需求转换成可执行的 pytest Python 代码。

规则：
1. 生成的代码必须是标准 pytest 格式，函数名以 test_ 开头。
2. 每个生成的用例文件必须包含：测试目标注释、预期结果注释、必要的 import。
3. 代码生成后，你必须使用 write_file 工具将代码保存到 ./generated_tests/ 目录下，文件名格式为 test_<主题>.py。
4. 不要返回 Markdown 代码块给用户，直接写入文件并告知文件路径。
5. 如果需求涉及 ROCm 底层算子（rocBLAS/MIOpen/rocSOLVER），优先使用 hip-python 或 pytorch 的 ROCm 接口风格。
6. 如果需求涉及 vLLM 推理，生成基于 requests 或 openai 客户端的测试代码。
"""

# 3. 创建 Agent（deepagents 已内置 read/write/edit/ls/grep 等文件工具 + plan 能力）
agent = create_deep_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    # 这里不传入额外 tools，先利用 deepagents 自带的文件系统工具完成落盘
)

# 4. 简单的 CLI 循环
def main():
    os.makedirs("./generated_tests", exist_ok=True)
    print("🧪 ROCm Test Case Agent (极简版)")
    print("输入你的测试需求，例如：为 vLLM 上的 Llama-3.1-8B 生成推理吞吐量测试")
    print("输入 'exit' 退出\n")

    while True:
        user_input = input("需求> ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        if not user_input:
            continue

        # 调用 agent：deepagents 会自动处理 plan → generate → write_file 的流程
        result = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
        
        # 输出最后一条 assistant 消息
        final_msg = result["messages"][-1].content
        print(f"\n🤖 Agent: {final_msg}\n")

if __name__ == "__main__":
    main()