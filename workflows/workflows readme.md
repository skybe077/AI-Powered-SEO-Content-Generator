# SEO Content Generator Agent

## Overview
The **SEO Content Generator Agent** is a modular, multi-agent automation workflow that transforms a **seed concept** into **SEO-optimized content** ready for publication.

It automates and connects four key stages:
1. **Topic Expansion**
2. **Keyword Research**
3. **Content Planning**
4. **Content Generation**

This system is designed for **scalability**, **feedback loops**, and **flexible integration** (e.g., via Appsmith UI, API calls, or manual inputs).

---

## Workflow Structure

| Stage                | Agent Name              | Purpose                                                                                  |
|----------------------|--------------------------|------------------------------------------------------------------------------------------|
| 1. Topic Expansion    | Topic Expansion Agent    | Expands a seed concept into SEO-friendly topics with localized and delocalized versions  |
| 2. Keyword Research   | SEO Agent                | Identifies keywords for each topic (main, cluster, long-tail) and assesses topic strength|
| 3. Content Planning   | Content Planner Agent    | Organizes topics and keywords into pillar-cluster content plans                          |
| 4. Content Generation | Content Generator Agent  | Creates human-like SEO-optimized articles based on the plan                              |

Each agent is modular and can be improved or replaced independently.

---

## Inputs

- **Seed Concept** (string):  
  E.g., `"small business marketing strategies"`
- **Minimum Keyword Volume** (integer, optional):  
  Filters topics based on minimum SEO volume.
- **Excluded Topics** (list, optional):  
  Topics to omit during expansion.

---

## Outputs

- **Expanded Topics** (with localized/delocalized versions)
- **Keyword Lists** (categorized as primary, cluster, long-tail)
- **Content Plans** (pillar page + cluster topics)
- **SEO-Optimized Articles** (HTML or Markdown)

All outputs are saved to a database (e.g., Xata) and optionally pushed to the front-end (e.g., Appsmith).

---

## Workflow Diagram

```plaintext
Seed Concept 
    ↓
Topic Expansion Agent
    ↓
SEO Agent (Keyword Research)
    ↓
Content Planner Agent
    ↓
Content Generator Agent
    ↓
Database Save + (Optional) Display in UI
