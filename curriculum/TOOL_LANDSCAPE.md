# Tool Landscape and Selection Guide
Features and availability vary by plan, region and release; check official docs before teaching.

| Tool | Learning use | Controls to teach |
|---|---|---|
| GitHub Copilot | Inline help, chat, agent-assisted edits, test drafting | Review diffs; protect repository instructions; test generated changes |
| Claude Code | Terminal-oriented repository exploration and edits | Review commands/diffs; constrain permissions; test before commit |
| Claude Cowork | Delegated desktop knowledge work where available | Verify availability, permissions, data handling and human review |
| Azure AI Foundry | Model/agent experimentation, evaluation and deployment | Identity, networking, region, quota, safety and cost |
| Amazon Bedrock | Managed foundation models and agent applications | IAM least privilege, guardrails, region and billing |
| Google Vertex AI | Managed models, grounding, evaluation and AI workflows | IAM, data governance, regional availability and quotas |
| OpenAI API | Model-driven apps, structured outputs and tool use | API keys, usage limits, retention and evaluation |
| LangGraph or similar | Stateful workflows, routing and checkpoints | Avoid unnecessary complexity; design recovery |
| MCP | Tool/context connectivity pattern | Tool identity, scopes, input/output validation |
| Docker | Reproducible environments | Pin images, scan dependencies, avoid privileged containers |
| GitHub Actions | CI, tests and publishing | Least-privilege workflow permissions and protected secrets |
| ROS 2 / Gazebo | Robot middleware and simulation | Simulation assumptions; hardware compatibility and safety |
| OpenCV | Image processing and perception | Consent, privacy, bias and latency |

## Vendor-neutral selection matrix
Score 1–5 with evidence: task quality, data handling, identity, model/region availability, evaluation, latency, reliability, interoperability, portability, cost per successful task, accessibility and operator experience.

## Official docs
- Copilot: https://docs.github.com/en/copilot
- Claude Code: https://docs.anthropic.com/en/docs/claude-code/overview
- Anthropic: https://docs.anthropic.com/
- Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry/
- Amazon Bedrock: https://docs.aws.amazon.com/bedrock/
- Vertex AI: https://cloud.google.com/vertex-ai/docs
- OpenAI API: https://platform.openai.com/docs
- MCP: https://modelcontextprotocol.io/
- ROS 2: https://docs.ros.org/
- Gazebo: https://gazebosim.org/docs/
- GitHub Actions: https://docs.github.com/actions
