# Support Assistant Agent 🤖

## Overview
Automated customer support assistant that answers FAQs using RAG and escalates complex queries.

## Features
- FAQ answering using knowledge base
- Escalation to human support when confidence is low
- Ticket logging system

## Tech Stack
| Component | Technology |
|-----------|-----------|
| UI | Streamlit |
| AI Model | OpenAI GPT |
| Retrieval | Chroma / embeddings |
| DB | CSV / Sheets |

## Run Locally

git clone <repo>
cd support-assistant-agent
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py