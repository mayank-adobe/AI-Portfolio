# AI Use Cases Based on My Experience

As I learned about LLMs, RAG, Fine-Tuning, and Agents, I identified several practical AI use cases based on technologies that I have worked with throughout my career, including IBM MQ, IBM IIB/ACE, Azure Data Factory, and Workfront Fusion.

## 1. MQ Knowledge Assistant (RAG + Agent)

During my time working as an IBM MQ Administrator, onboarding new team members often required significant knowledge transfer regarding queue configurations, cluster setup, pub/sub architecture, troubleshooting approaches, and application integrations.

An AI-powered MQ Knowledge Assistant could help address this challenge.

### Proposed Flow

```text
User Question
      ↓
AI Agent
      ↓
RAG Search
      ↓
MQ Documentation / Runbooks / Queue Inventory
      ↓
Grounded Response
