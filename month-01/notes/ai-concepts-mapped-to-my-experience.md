# AI Concepts Mapped To My Experience

## Introduction

While learning about LLMs, RAG, Fine-Tuning, and Agents, I identified several AI use cases that can be applied to technologies I have worked on throughout my career, including IBM MQ, Azure Data Factory, and Workfront Fusion.

---

## MQ Knowledge Assistant (RAG + Agent)

During my time working as an IBM MQ Administrator, onboarding new team members required significant knowledge transfer regarding queue configurations, cluster setup, pub/sub architecture, troubleshooting approaches, and application integrations.

An AI-powered MQ Knowledge Assistant could help address this challenge.

### Proposed Flow

User Question
↓
AI Agent
↓
RAG Search
↓
MQ Documentation / Runbooks / Queue Inventory
↓
Grounded Response

### Example Use Cases

- What is the purpose of Queue_X?
- Which applications use Queue_X?
- What troubleshooting steps should I follow for a queue issue?
- What pub/sub topics are configured?

The agent would retrieve information from project documentation and operational runbooks to provide accurate and consistent answers while reducing onboarding effort.

---

## Azure Data Factory Pipeline Assistant (Agent + RAG)

While working on Azure Data Factory projects, creating new file transfer pipelines often required gathering details about source systems, target systems, schedules, connection details, file formats, and transformation requirements.

An AI-powered ADF Assistant could simplify this process.

### Proposed Flow

User Requirement
↓
AI Agent
↓
Collect Required Information
↓
Generate Pipeline Design
↓
Generate Configuration Recommendation
↓
Trigger Deployment Workflow

### Example Questions Asked By The Agent

- What is the source system?
- What is the target system?
- What file format is being transferred?
- What is the expected file size?
- How frequently should the pipeline execute?

The agent could recommend pipeline configurations based on existing patterns and organizational standards. Fine-tuning could later be used to ensure generated outputs follow company naming conventions and development standards.

---

## Workfront Project Intake Agent (Agent + RAG)

My current experience with Workfront Fusion and Workfront Core provides an opportunity to directly apply AI to project intake and planning processes.

### Proposed Flow

Meeting Recording / Request
↓
Transcript
↓
AI Agent
↓
Requirement Analysis
↓
Generate Summary
↓
Generate Tasks
↓
Identify Risks
↓
Suggest Priority
↓
Create Workfront Project
↓
Create Custom Forms
↓
Update Planning Records

### Potential Benefits

- Automatic meeting summaries
- Faster requirement gathering
- Better communication between business and development teams
- Reduced manual project setup effort
- Automated task generation
- Improved planning record quality

The agent could act as a bridge between business stakeholders and development teams by converting meeting discussions into structured project requirements and Workfront artifacts.

---

## Conclusion

My experience in MQ, Azure Data Factory, and Workfront Fusion demonstrates that many enterprise processes already follow workflow and automation patterns.

AI extends these workflows by introducing:

- Knowledge retrieval through RAG
- Content generation through LLMs
- Decision-making through Agents
- Automation through integrations and workflows

The strongest opportunity I currently see is in Workfront, where AI Agents can assist with project intake, requirement analysis, task generation, planning record creation, and workflow automation while still keeping humans involved for review and approval.
