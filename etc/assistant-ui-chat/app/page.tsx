'use client';

import { AssistantRuntimeProvider } from '@assistant-ui/react';
import { useLangGraphRuntime } from '@assistant-ui/react-langgraph';

export default function Home() {
  const runtime = useLangGraphRuntime({
    apiUrl: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:2024',
    assistantId: process.env.NEXT_PUBLIC_ASSISTANT_ID || 'agent',
  });

  return (
    <AssistantRuntimeProvider runtime={runtime}>
      <main style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
        <h1 style={{ padding: '1rem', textAlign: 'center' }}>TestCaseAgent Chat</h1>
        <div style={{ flex: 1, padding: '1rem' }}>
          <div style={{ border: '1px solid #ccc', borderRadius: '8px', padding: '1rem', height: '100%' }}>
            <p>前端已启动，请确保后端 LangGraph Server 在端口 2024 运行。</p>
            <p>启动后端命令: <code>langgraph dev</code></p>
          </div>
        </div>
      </main>
    </AssistantRuntimeProvider>
  );
}
