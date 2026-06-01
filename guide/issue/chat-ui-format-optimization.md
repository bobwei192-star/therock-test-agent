# Chat UI 前端显示格式优化方案

## 问题分析

### 当前问题表现

用户在前端看到的是：
```
{'messages': [HumanMessage(content="你是 ROCm 测试需求解析专家。首先识别用户意图...
用户需求：[{'type': 'text', 'text': 'hi'}]
## 意图识别（必选其一）
分析用户输入，判断属于以下哪种意图：
- GENERATE: 从零创建新测试用例
...
```

### 问题根因

**后端（主要责任 70%）**：
1. LLM 直接输出包含 prompt 模板、调试信息
2. 没有对输出进行结构化清洗
3. 将内部对象（HumanMessage/AIMessage）暴露给前端

**前端（次要责任 30%）**：
1. 直接渲染原始 content，没有过滤技术性内容
2. 缺少内容预处理和格式化

---

## 优化方案

### 方案 A：后端优化（已完成 ✅）

**文件**：`src/agent/utils/clean_llm_output.py`（新建）

**功能**：
- 移除 HumanMessage/AIMessage 等内部对象
- 移除 prompt 模板重复内容
- 移除调试信息
- 提取结构化内容

**修改**：`src/agent/nodes/node_requirement_parser.py`
- 在返回前端之前调用 `clean_llm_output()`
- 自动提取意图标识

**效果**：
```python
# 清洗前
{'messages': [HumanMessage(content="你是 ROCm 测试需求解析专家...
用户需求：[{'type': 'text', 'text': 'hi'}]
## 意图识别...
意图：GENERATE

# 清洗后
## 测试规格输出

### 1. 测试目标
验证 rocm-smi 命令行工具的存在性及基本功能正确性

### 2. ROCm 组件
rocm-smi (AMD ROCm System Management Interface CLI)
...
```

---

### 方案 B：前端优化（建议实施）

#### B1. 添加内容过滤器

**文件**：`etc/agent-chat-ui/src/components/thread/messages/ai.tsx`

**修改位置**：在 `MarkdownText` 组件之前添加预处理

```typescript
// 在 ai.tsx 中添加清洗函数
function cleanLLMOutput(content: string): string {
  if (!content) return '';
  
  let cleaned = content;
  
  // 移除 HumanMessage/AIMessage 对象
  cleaned = cleaned.replace(
    /(HumanMessage|AIMessage|SystemMessage)\(content=\[?.*?\]?\.?/g,
    ''
  );
  
  // 移除 prompt 模板重复内容
  cleaned = cleaned.replace(
    /你是 ROCm 测试需求解析专家.*?(?=## 意图识别 | 意图：|测试目标：|$)/s,
    ''
  );
  
  // 移除用户需求复述
  cleaned = cleaned.replace(
    /用户需求：\s*\[\{.*?'type':\s*'text'.*?\}\]/gs,
    ''
  );
  
  // 移除调试信息
  cleaned = cleaned.replace(
    /\{[^{}]*"messages":\s*\[.*?\][^{}]*\}/gs,
    '[调试信息已隐藏]'
  );
  
  // 清理多余空行
  cleaned = cleaned.replace(/\n{3,}/g, '\n\n');
  
  return cleaned.trim();
}

// 在渲染时使用
<MarkdownText>{cleanLLMOutput(contentString)}</MarkdownText>
```

#### B2. 添加结构化渲染组件

创建专门的组件来渲染测试规格：

```typescript
// etc/agent-chat-ui/src/components/thread/TestSpecPreview.tsx
interface TestSpecPreviewProps {
  content: string;
}

export function TestSpecPreview({ content }: TestSpecPreviewProps) {
  // 解析 Markdown 格式并结构化展示
  return (
    <div className="test-spec-preview">
      <h3>📋 测试规格</h3>
      {/* 解析并渲染各个章节 */}
    </div>
  );
}
```

#### B3. 添加意图标识徽章

在消息头部显示意图类型：

```typescript
// 在 AssistantMessage 组件中
const intent = extractIntent(content); // 从内容中提取意图

{intent && (
  <Badge className="intent-badge" intent={intent}>
    {intent}
  </Badge>
)}
```

---

## 实施建议

### 第一阶段（立即实施）✅
1. **后端清洗**：已部署
   - `src/agent/utils/clean_llm_output.py`
   - `src/agent/nodes/node_requirement_parser.py`

### 第二阶段（建议实施）
2. **前端基础清洗**：
   - 在 `ai.tsx` 中添加 `cleanLLMOutput()` 函数
   - 在渲染前调用

3. **添加意图标识**：
   - 创建 Badge 组件显示意图类型
   - 提升用户感知

### 第三阶段（可选优化）
4. **结构化渲染**：
   - 创建 TestSpecPreview 组件
   - 解析 Markdown 并美化展示

5. **添加折叠功能**：
   - 技术细节默认折叠
   - 用户可展开查看详情

---

## 测试验证

### 后端测试
```bash
cd /home/zs/TestCaseAgent
source .venv/bin/activate
python -m pytest tests/unit/test_clean_llm_output.py -v
```

### 前端测试
1. 启动 LangGraph Server: `langgraph dev`
2. 启动 Chat UI: `cd etc/agent-chat-ui && pnpm dev`
3. 访问 `http://localhost:3001`
4. 输入 "hi" 或简单问候语
5. 检查输出是否清晰易读

---

## 预期效果

### 优化前 ❌
```
{'messages': [HumanMessage(content="你是 ROCm 测试需求解析专家...
用户需求：[{'type': 'text', 'text': 'hi'}]
## 意图识别（必选其一）
分析用户输入...
意图：GENERATE
...
```

### 优化后 ✅
```
## 测试规格

### 1. 测试目标
验证 rocm-smi 命令行工具的存在性及基本功能正确性

### 2. ROCm 组件
rocm-smi (AMD ROCm System Management Interface CLI)

### 3. 测试点清单
- 命令存在性检查：有效等价类 | Arrange: 检查 PATH...
```

---

## 相关文件

### 后端
- `src/agent/utils/clean_llm_output.py` (新建)
- `src/agent/nodes/node_requirement_parser.py` (修改)
- `src/agent/promots/node_requirement_parser.md` (建议优化)

### 前端
- `etc/agent-chat-ui/src/components/thread/messages/ai.tsx` (建议修改)
- `etc/agent-chat-ui/src/components/thread/markdown-text.tsx` (可扩展)

---

## 总结

**责任分配**：
- 后端：70%（提供干净的输出）
- 前端：30%（美化展示）

**实施优先级**：
1. ✅ 后端清洗（已完成）
2.  前端基础清洗（建议）
3. ⏳ 意图标识（建议）
4. ⏳ 结构化渲染（可选）

通过双管齐下的优化，Chat UI 的显示质量将得到显著提升。
