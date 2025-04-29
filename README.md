# 🧠 AI-Powered SEO Content Generator (n8n + Appsmith + GPT-4o)

This project is a full-stack AI agent system that automates the creation of SEO-optimized content — from a single seed concept to a publish-ready article — using **n8n**, **Appsmith**, and **GPT-4o**.

Built over 30 days (Mar–Apr 2025) as a proof-of-concept for intelligent, modular content workflows.

---

## 🚀 What It Does


✅ Accepts a seed phrase (e.g. `erp for smes`)

✅ Expands it into SEO-aligned topics using LLMs

✅ Performs real-time keyword research and clustering

✅ Categorizes keywords by intent and commercial value

✅ Plans content (pillar + supporting)

✅ Generates full-length, markdown-formatted articles

✅ Displays results through a user-facing Appsmith frontend

---

## 🧱 System Architecture

![AI-Powered SEO Content Generator System Architecture](../main/images/sys_architecture.png)


---

### 🔗 Agents

| Agent | Role |
| --- | --- |
| `Topic_Expansion_Agent` | Expands seed into 10–20 SEO-useful topics |
| `SEO_Agent` | Enriches each topic with keyword volume, CPC, and search intent |
| `Keyword_Categorizer` | Classifies keywords as `priority`, `cluster`, `long-tail`, or `ignore` |
| `Content_Planner` | Groups keywords into pillar + clusters |
| `Content_Generator` | Writes full article using outline + keywords |
| `SEO_Review_Results` | Summarizes cluster performance and keyword gaps |

---

## 📸 UI (Built with Appsmith)

- Seed Concept Submission
- Topic & Keyword Table Viewer
- Content Preview Pane (with regenerate option)
- Keyword Stats & Validation Display

> Includes error handling, usefulness explanation, and manual control where needed.
> 

---

## 🧠 Key Features

- 🔁 LLM batching (10x reduction in OpenAI calls)
- ⚖️ CPC + volume + competition filtering
- 🧼 Pre-filters to drop low-value or vague topics
- 🧠 Natural-language topic normalization
- 🧪 Outline + content QA loop (planned in v1.1)
- 📊 Structured Xata/Postgres backend

---

## Project Structure 

AI-Powered-SEO-Content-Generator/

│

├── README.md

├── /workflows/

│   ├── topic-expander.json

│   ├── seo-agent.json

│   ├── content-writer.json

│   └── ...

├── /appsmith/

│   └── content-generator-app.json

├── /examples/

│   ├── input-output-seed-to-article.md

│   └── keyword-categorization-sample.json

├── /docs/
│   ├── architecture-diagram.png
│   └── prompts.md

└── LICENSE


