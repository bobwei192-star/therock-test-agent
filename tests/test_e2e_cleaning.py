"""前后端联调测试用例 - 验证 LLM 输出清洗功能

测试场景：
1. 验证后端 clean_llm_output 函数能正确清洗各种格式的 LLM 输出
2. 验证意图识别功能正常工作
3. 验证前端清洗函数与后端行为一致
4. 验证特殊输入（如 "hi"、空输入）的处理
"""

import pytest

from src.agent.utils.clean_llm_output import clean_llm_output, extract_intent_from_llm_response


class TestLLMOutputCleaning:
    """测试 LLM 输出清洗功能"""

    def test_clean_llm_output_with_prompt_template(self):
        """测试清洗包含完整 prompt 模板的输出"""
        raw_output = """你是 ROCm 测试需求解析专家。首先识别用户意图，然后输出结构化的测试规格。

用户需求: [{'type': 'text', 'text': '写一个测试用例'}]

## 意图识别（必选其一）
分析用户输入，判断属于以下哪种意图：
- GENERATE: 从零创建新测试用例
- APPEND: 在现有测试文件上追加新测试函数
- UPDATE: 修复已有测试的错误
- REFACTOR: 优化代码结构
- EXECUTE_EXTERNAL: 下载/编译/运行第三方测试套件
- DIAGNOSE: 分析测试失败日志
- COVERAGE: 分析现有测试集的覆盖度
- PROBE: 探测当前 ROCm 环境能力

意图：GENERATE

## 测试规格输出
1. 测试目标: 验证 rocm-smi 命令的基本功能
2. ROCm 组件: rocm-smi
3. 测试点清单:
- 测试点1: 有效等价类 | Arrange:检查命令存在→Act:执行rocm-smi→Assert:返回码为0→Cleanup:无
"""
        cleaned = clean_llm_output(raw_output)
        
        # 清洗后应该不包含 prompt 模板内容
        assert "你是 ROCm 测试需求解析专家" not in cleaned
        assert "## 意图识别（必选其一）" not in cleaned
        assert "分析用户输入，判断属于以下哪种意图" not in cleaned
        assert "用户需求:" not in cleaned
        
        # 但应该保留意图和测试规格
        assert "意图：GENERATE" in cleaned
        assert "测试目标:" in cleaned
        assert "rocm-smi" in cleaned

    def test_clean_llm_output_with_message_objects(self):
        """测试清洗包含 HumanMessage/AIMessage 对象的输出"""
        raw_output = """HumanMessage(content="你是测试专家")AIMessage(content="好的，我来分析")意图：GENERATE

测试目标: 测试命令存在性"""
        
        cleaned = clean_llm_output(raw_output)
        
        assert "HumanMessage" not in cleaned
        assert "AIMessage" not in cleaned
        assert "意图：GENERATE" in cleaned
        assert "测试目标:" in cleaned

    def test_clean_llm_output_with_debug_json(self):
        """测试清洗包含调试 JSON 对象的输出"""
        raw_output = """{"messages": [{"role": "user", "content": "hi"}], "context": {}}意图：CHAT

你好！有什么我可以帮助你的吗？"""
        
        cleaned = clean_llm_output(raw_output)
        
        assert "[调试信息已隐藏]" in cleaned or "{\"messages\"" not in cleaned
        assert "意图：CHAT" in cleaned
        assert "你好！" in cleaned

    def test_clean_empty_input(self):
        """测试清洗空输入"""
        assert clean_llm_output("") == ""
        assert clean_llm_output("   \n\n  ") == ""
        assert clean_llm_output(None) == ""

    def test_clean_chat_intent(self):
        """测试清洗闲聊意图的输出"""
        raw_output = """你是 ROCm 测试需求解析专家。首先识别用户意图...

用户需求: [{'type': 'text', 'text': 'hi'}]

## 意图识别（必选其一）
...
意图：CHAT

你好！有什么我可以帮助你的吗？"""
        
        cleaned = clean_llm_output(raw_output)
        
        assert "意图：CHAT" in cleaned
        assert "你好！" in cleaned
        assert "你是 ROCm 测试需求解析专家" not in cleaned


class TestIntentExtraction:
    """测试意图提取功能"""

    def test_extract_generate_intent(self):
        """测试提取 GENERATE 意图"""
        content = "意图：GENERATE\n测试目标: 测试命令"
        assert extract_intent_from_llm_response(content) == "GENERATE"

    def test_extract_chat_intent(self):
        """测试提取 CHAT 意图"""
        content = "意图：CHAT\n你好！"
        assert extract_intent_from_llm_response(content) == "CHAT"

    def test_extract_append_intent(self):
        """测试提取 APPEND 意图"""
        content = "意图：APPEND\n追加测试用例"
        assert extract_intent_from_llm_response(content) == "APPEND"

    def test_extract_intent_with_colon_variations(self):
        """测试不同冒号格式的意图提取（中文冒号、英文冒号）"""
        assert extract_intent_from_llm_response("意图: GENERATE") == "GENERATE"
        assert extract_intent_from_llm_response("意图：GENERATE") == "GENERATE"
        assert extract_intent_from_llm_response("意图： GENERATE") == "GENERATE"

    def test_extract_unknown_intent(self):
        """测试无法识别意图时返回 None"""
        assert extract_intent_from_llm_response("这是一段普通文本") is None
        assert extract_intent_from_llm_response("") is None
        assert extract_intent_from_llm_response(None) is None


class TestEndToEndFlow:
    """测试前后端联调流程"""

    def test_cleaning_preserves_intent(self):
        """测试清洗后保留意图信息"""
        raw_output = """HumanMessage(content="prompt模板内容")
用户需求: [{'type': 'text', 'text': 'hi'}]
## 意图识别（必选其一）
分析用户输入...
- GENERATE: 从零创建
- CHAT: 闲聊
意图：CHAT

你好！欢迎使用 Test Case Agent。"""
        
        cleaned = clean_llm_output(raw_output)
        intent = extract_intent_from_llm_response(cleaned)
        
        assert intent == "CHAT"
        assert "你好！" in cleaned

    def test_cleaning_with_real_world_input(self):
        """测试真实场景的清洗效果"""
        raw_output = """你是 ROCm 测试需求解析专家。首先识别用户意图，然后输出结构化的测试规格（Test Spec），供下游节点做执行编排和代码生成。不要输出执行步骤、时间安排或工程部署细节。

用户需求: [{'type': 'text', 'text': '写一个pytest测试用例，测试rocm-smi指令的存在性和正确性'}]

## 意图识别（必选其一）
分析用户输入，判断属于以下哪种意图：
- GENERATE: 从零创建新测试用例
- APPEND: 在现有测试文件上追加新测试函数/场景
- UPDATE: 修复已有测试的错误或适配新版本
- REFACTOR: 优化代码结构，不改测试逻辑与断言目标
- EXECUTE_EXTERNAL: 下载/编译/运行第三方测试套件（如 igt-gpu-tools）
- DIAGNOSE: 分析测试失败日志，定位根因
- COVERAGE: 分析现有测试集的等价类/边界值覆盖度
- PROBE: 探测当前 ROCm 环境能力，输出报告

意图：GENERATE

## 测试规格输出
1. 测试目标: 验证 rocm-smi 指令的存在性和基本功能正确性
2. ROCm 组件: rocm-smi
3. 测试点清单:
- 测试点1: 有效等价类 | Arrange:检查rocm-smi命令是否在PATH中→Act:执行rocm-smi --help→Assert:返回码为0且输出包含帮助信息→Cleanup:无
- 测试点2: 无效等价类 | Arrange:无需准备→Act:执行不存在的命令→Assert:返回非零码→Cleanup:无
4. 等价类划分:
- 有效等价类: rocm-smi命令存在且可执行
- 无效等价类: rocm-smi命令不存在
5. AAAC 四阶段设计原则:
- Arrange: 检查rocm-smi命令存在性
- Act: 执行rocm-smi --help
- Assert: 返回码为0，输出包含帮助关键词
- Cleanup: 无
"""
        
        cleaned = clean_llm_output(raw_output)
        
        # 验证关键信息保留
        assert "意图：GENERATE" in cleaned
        assert "测试目标:" in cleaned
        assert "rocm-smi" in cleaned
        assert "测试点1:" in cleaned
        assert "测试点2:" in cleaned
        
        # 验证模板内容被移除
        assert "你是 ROCm 测试需求解析专家" not in cleaned
        assert "## 意图识别（必选其一）" not in cleaned
        assert "分析用户输入，判断属于以下哪种意图" not in cleaned
        assert "用户需求:" not in cleaned

    def test_cleaning_preserves_yaml_block(self):
        """测试清洗后保留 YAML 执行计划块"""
        raw_output = """HumanMessage(content="prompt内容")意图：GENERATE

测试计划...

```yaml
execution_plan:
  environment:
    type: "docker"
  steps:
    - name: "执行测试"
      action: "run"
```"""
        
        cleaned = clean_llm_output(raw_output)
        
        assert "意图：GENERATE" in cleaned
        assert "```yaml" in cleaned
        assert "execution_plan:" in cleaned
        assert "HumanMessage" not in cleaned


if __name__ == "__main__":
    pytest.main([__file__, "-v"])