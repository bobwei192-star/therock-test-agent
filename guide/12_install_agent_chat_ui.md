Skip to content
langchain-ai
agent-chat-ui
Repository navigation
Code
Issues
51
 (51)
Pull requests
34
 (34)
Actions
Projects
Security and quality
Insights
Owner avatar
agent-chat-ui
Public
langchain-ai/agent-chat-ui
Go to file
t
T
Name		
dependabot[bot]
dependabot[bot]
Bump next from 15.5.15 to 15.5.18 (#286)
91da3c5
 · 
3 weeks ago
.github
Bump pnpm/action-setup from 5 to 6 (#272)
last month
src
Bump the minor-and-patch group across 1 directory with 35 updates (#279)
last month
.codespellignore
feat: Add going to production docs
last year
.dockerignore
Add dockerignore
last year
.env.example
feat: Support for Agent Builder agents (#253)
3 months ago
.gitignore
cr
last year
.prettierignore
chore: update prettier config
last year
LICENSE
Update LICENSE year
last year
README.md
Bump the minor-and-patch group across 1 directory with 35 updates (#279)
last month
components.json
improved agent
last year
eslint.config.js
cr
last year
next.config.mjs
lint and format
last year
package.json
Bump next from 15.5.15 to 15.5.18 (#286)
3 weeks ago
pnpm-lock.yaml
Bump next from 15.5.15 to 15.5.18 (#286)
3 weeks ago
postcss.config.mjs
refactor: Use next.js instead of vite
last year
prettier.config.js
chore: update prettier config
last year
tailwind.config.js
cr
last year
tsconfig.json
refactor: Use next.js instead of vite
last year
Repository files navigation
README
Code of conduct
Contributing
MIT license
Security
Agent Chat UI
Agent Chat UI is a Next.js application which enables chatting with any LangGraph server with a messages key through a chat interface.

Note

🎥 Watch the video setup guide here.

Setup
Tip

Don't want to run the app locally? Use the deployed site here: agentchat.vercel.app!

First, clone the repository, or run the npx command:

npx create-agent-chat-app
or

git clone https://github.com/langchain-ai/agent-chat-ui.git

cd agent-chat-ui
Install dependencies:

pnpm install
Run the app:

pnpm dev
The app will be available at http://localhost:3000.

Usage
Once the app is running (or if using the deployed site), you'll be prompted to enter:

Deployment URL: The URL of the LangGraph server you want to chat with. This can be a production or development URL.
Assistant/Graph ID: The name of the graph, or ID of the assistant to use when fetching, and submitting runs via the chat interface.
LangSmith API Key: (only required for connecting to deployed LangGraph servers) Your LangSmith API key to use when authenticating requests sent to LangGraph servers.
Built with Agent Builder: Toggle this on for Agent Builder deployments. This automatically sets the auth scheme to langsmith-api-key.
After entering these values, click Continue. You'll then be redirected to a chat interface where you can start chatting with your LangGraph server.

Environment Variables
You can bypass the initial setup form by setting the following environment variables:

NEXT_PUBLIC_API_URL=http://localhost:2024
NEXT_PUBLIC_ASSISTANT_ID=agent
NEXT_PUBLIC_AUTH_SCHEME=
Note

If you are connecting to a LangSmith Agent Builder deployment, set NEXT_PUBLIC_AUTH_SCHEME=langsmith-api-key.

Tip

If you want to connect to a production LangGraph server, read the Going to Production section.

To use these variables:

Copy the .env.example file to a new file named .env
Fill in the values in the .env file
Restart the application
When these environment variables are set, the application will use them instead of showing the setup form.

Hiding Messages in the Chat
You can control the visibility of messages within the Agent Chat UI in two main ways:

1. Prevent Live Streaming:

To stop messages from being displayed as they stream from an LLM call, add the langsmith:nostream tag to the chat model's configuration. The UI normally uses on_chat_model_stream events to render streaming messages; this tag prevents those events from being emitted for the tagged model.

Python Example:

from langchain_anthropic import ChatAnthropic

# Add tags via the .with_config method
model = ChatAnthropic().with_config(
    config={"tags": ["langsmith:nostream"]}
)
TypeScript Example:

import { ChatAnthropic } from "@langchain/anthropic";

const model = new ChatAnthropic()
  // Add tags via the .withConfig method
  .withConfig({ tags: ["langsmith:nostream"] });
Note: Even if streaming is hidden this way, the message will still appear after the LLM call completes if it's saved to the graph's state without further modification.

2. Hide Messages Permanently:

To ensure a message is never displayed in the chat UI (neither during streaming nor after being saved to state), prefix its id field with do-not-render- before adding it to the graph's state, along with adding the langsmith:do-not-render tag to the chat model's configuration. The UI explicitly filters out any message whose id starts with this prefix.

Python Example:

result = model.invoke([messages])
# Prefix the ID before saving to state
result.id = f"do-not-render-{result.id}"
return {"messages": [result]}
TypeScript Example:

const result = await model.invoke([messages]);
// Prefix the ID before saving to state
result.id = `do-not-render-${result.id}`;
return { messages: [result] };
This approach guarantees the message remains completely hidden from the user interface.

Rendering Artifacts
The Agent Chat UI supports rendering artifacts in the chat. Artifacts are rendered in a side panel to the right of the chat. To render an artifact, you can obtain the artifact context from the thread.meta.artifact field. Here's a sample utility hook for obtaining the artifact context:

export function useArtifact<TContext = Record<string, unknown>>() {
  type Component = (props: {
    children: React.ReactNode;
    title?: React.ReactNode;
  }) => React.ReactNode;

  type Context = TContext | undefined;

  type Bag = {
    open: boolean;
    setOpen: (value: boolean | ((prev: boolean) => boolean)) => void;

    context: Context;
    setContext: (value: Context | ((prev: Context) => Context)) => void;
  };

  const thread = useStreamContext<
    { messages: Message[]; ui: UIMessage[] },
    { MetaType: { artifact: [Component, Bag] } }
  >();

  return thread.meta?.artifact;
}
After which you can render additional content using the Artifact component from the useArtifact hook:

import { useArtifact } from "../utils/use-artifact";
import { LoaderIcon } from "lucide-react";

export function Writer(props: {
  title?: string;
  content?: string;
  description?: string;
}) {
  const [Artifact, { open, setOpen }] = useArtifact();

  return (
    <>
      <div
        onClick={() => setOpen(!open)}
        className="cursor-pointer rounded-lg border p-4"
      >
        <p className="font-medium">{props.title}</p>
        <p className="text-sm text-gray-500">{props.description}</p>
      </div>

      <Artifact title={props.title}>
        <p className="whitespace-pre-wrap p-4">{props.content}</p>
      </Artifact>
    </>
  );
}
Going to Production
Once you're ready to go to production, you'll need to update how you connect, and authenticate requests to your deployment. By default, the Agent Chat UI is setup for local development, and connects to your LangGraph server directly from the client. This is not possible if you want to go to production, because it requires every user to have their own LangSmith API key, and set the LangGraph configuration themselves.

Production Setup
To productionize the Agent Chat UI, you'll need to pick one of two ways to authenticate requests to your LangGraph server. Below, I'll outline the two options:

Quickstart - API Passthrough
The quickest way to productionize the Agent Chat UI is to use the API Passthrough package (NPM link here). This package provides a simple way to proxy requests to your LangGraph server, and handle authentication for you.

This repository already contains all of the code you need to start using this method. The only configuration you need to do is set the proper environment variables.

NEXT_PUBLIC_ASSISTANT_ID="agent"
# This should be the deployment URL of your LangGraph server
LANGGRAPH_API_URL="https://my-agent.default.us.langgraph.app"
# This should be the URL of your website + "/api". This is how you connect to the API proxy
NEXT_PUBLIC_API_URL="https://my-website.com/api"
# Your LangSmith API key which is injected into requests inside the API proxy
LANGSMITH_API_KEY="lsv2_..."
Let's cover what each of these environment variables does:

NEXT_PUBLIC_ASSISTANT_ID: The ID of the assistant you want to use when fetching, and submitting runs via the chat interface. This still needs the NEXT_PUBLIC_ prefix, since it's not a secret, and we use it on the client when submitting requests.
LANGGRAPH_API_URL: The URL of your LangGraph server. This should be the production deployment URL.
NEXT_PUBLIC_API_URL: The URL of your website + /api. This is how you connect to the API proxy. For the Agent Chat demo, this would be set as https://agentchat.vercel.app/api. You should set this to whatever your production URL is.
LANGSMITH_API_KEY: Your LangSmith API key to use when authenticating requests sent to LangGraph servers. Once again, do not prefix this with NEXT_PUBLIC_ since it's a secret, and is only used on the server when the API proxy injects it into the request to your deployed LangGraph server.
For in depth documentation, consult the LangGraph Next.js API Passthrough docs.

Advanced Setup - Custom Authentication
Custom authentication in your LangGraph deployment is an advanced, and more robust way of authenticating requests to your LangGraph server. Using custom authentication, you can allow requests to be made from the client, without the need for a LangSmith API key. Additionally, you can specify custom access controls on requests.

To set this up in your LangGraph deployment, please read the LangGraph custom authentication docs for Python, and TypeScript here.

Once you've set it up on your deployment, you should make the following changes to the Agent Chat UI:

Configure any additional API requests to fetch the authentication token from your LangGraph deployment which will be used to authenticate requests from the client.
Set the NEXT_PUBLIC_API_URL environment variable to your production LangGraph deployment URL.
Set the NEXT_PUBLIC_ASSISTANT_ID environment variable to the ID of the assistant you want to use when fetching, and submitting runs via the chat interface.
Modify the useTypedStream (extension of useStream) hook to pass your authentication token through headers to the LangGraph server:
const streamValue = useTypedStream({
  apiUrl: process.env.NEXT_PUBLIC_API_URL,
  assistantId: process.env.NEXT_PUBLIC_ASSISTANT_ID,
  // ... other fields
  defaultHeaders: {
    Authentication: `Bearer ${addYourTokenHere}`, // this is where you would pass your authentication token
  },
});
About
🦜💬 Web app for interacting with any LangGraph agent (PY & TS) via a chat interface.

agentchat.vercel.app
Topics
chat agent llm langgraph
Resources
 Readme
License
 MIT license
Code of conduct
 Code of conduct
Contributing
 Contributing
Security policy
 Security policy
 Activity
 Custom properties
Stars
 2.9k stars
Watchers
 20 watching
Forks
 631 forks
Report repository
Releases
No releases published
Deployments
433
 Preview 3 weeks ago
 Production 3 weeks ago
+ 431 deployments
Packages
No packages published
Contributors
17
@bracesproul
@dqbd
@starmorph
@dependabot[bot]
@jkennedyvz
@claude
@Neulhan
@cgoinglove
@lien-dkseo
@DavoCoder
@samecrowder
@linganmin
@sanjeed5
@VMinB12
+ 3 contributors
Languages
TypeScript
95.4%
 
CSS
2.8%
 
JavaScript
1.8%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
