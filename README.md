# RxRAG_Agent
# Domain-Aware RAG Agent for Evidence-Based Decision Support

## Overview

This project implements a **production-grade Retrieval-Augmented Generation (RAG) system with agentic workflows** designed to support **evidence-based decision making** in knowledge-intensive domains such as healthcare, legal/compliance, or internal technical documentation.

The system enables users to query large, unstructured document corpora using natural language and receive **grounded, traceable, and auditable answers**, rather than unverified LLM-generated text.

This repository serves as a **capstone project** demonstrating end-to-end AI Engineering capabilities: data ingestion, embeddings, retrieval, LLM integration, agent orchestration, evaluation, deployment, and monitoring.

---

## Problem Statement

Professionals operating in regulated or high-stakes environments face several challenges:

- Knowledge is spread across **long, heterogeneous, unstructured documents** (PDFs, HTML, policies, guidelines).
- Manual search is **slow, error-prone, and not scalable**.
- Traditional keyword-based search systems lack **semantic understanding**.
- Direct use of LLMs is **not acceptable** due to:
  - Hallucinations
  - Lack of traceability
  - No grounding in authoritative sources
  - Regulatory and compliance risks
- There is typically **no operational visibility** into system quality, latency, or failure modes.

---

## Solution

This project delivers a **Domain-Aware RAG Agent** that:

- Retrieves **authoritative evidence** from a curated document corpus.
- Generates answers **strictly grounded in retrieved sources**.
- Exposes **citations, confidence signals, and operational metadata**.
- Supports **agentic multi-step reasoning and tool-calling**.
- Is deployed as a **monitored, testable, and reproducible service**.

The system is designed to **refuse or downgrade answers** when sufficient evidence is not available, prioritizing **safety and reliability over fluency**.

---

## Key Capabilities

### 1. Knowledge Ingestion & Normalization

- Document ingestion from PDFs, HTML, and text sources.
- Semantic chunking with overlap and metadata.
- Versioned and reproducible corpus builds.

### 2. Semantic Retrieval

- Domain-adapted embeddings.
- Vector search using FAISS or managed vector databases.
- Top-k retrieval with relevance scoring and filtering.

### 3. Retrieval-Augmented Generation (RAG)

- Controlled prompt templates enforcing citation requirements.
- Context-constrained generation to reduce hallucinations.
- Source-aware answer synthesis.

### 4. Agentic Workflows

- Multi-step reasoning over retrieval, tools, and external APIs.
- Dynamic decision-making (re-retrieval, fallback, tool usage).
- Example tools: guideline fetchers, calculators, database lookups.

### 5. Evaluation & Governance

- Automated retrieval metrics (e.g. `precision@k`).
- Grounding and citation validation.
- LLM-as-judge evaluation pipelines.
- Human-in-the-loop compatibility.

### 6. Production & MLOps

- REST API built with FastAPI.
- Containerized deployment (Docker).
- Kubernetes-based serving (local or managed).
- CI/CD pipelines for testing and deployment.
- Monitoring with Prometheus and Grafana.

---

## Example Use Case (Healthcare Domain)

**Input query:**

> “What clinically relevant interactions exist between warfarin and macrolide antibiotics?”

**System output:**

- Synthesized answer summarizing known interactions.
- Explicit citations to clinical guidelines and studies.
- Confidence / grounding score.
- Metadata (model version, retrieval scores, latency).

---

## Architecture (High Level)

```text
User Query
   ↓
API (FastAPI)
   ↓
Agent Orchestrator
   ↓
Retriever → Vector DB (FAISS)
   ↓
Evidence Chunks
   ↓
LLM Generator (RAG Prompt)
   ↓
Answer + Citations + Metrics

## Tech Stack

### Modeling & LLMs
- Hugging Face Transformers  
- sentence-transformers  
- PEFT / LoRA  
- PyTorch  

### Retrieval
- FAISS (default)  
- Optional: Pinecone / Weaviate / Milvus  

### Orchestration
- LangChain / AutoGen (agent workflows)

### Serving
- FastAPI, Uvicorn  
- Docker  
- Kubernetes (k3s, GKE, EKS, AKS)

### MLOps & Infra
- GitHub Actions (CI/CD)  
- Terraform + Helm  
- MLflow (optional)  
- Prometheus + Grafana  

---

## Evaluation Metrics

### Quality
- `precision@k` (retrieval relevance)
- Grounding score (% of answers with valid citations)
- LLM-as-judge preference score
- Optional human evaluation

### Performance
- API latency (P95)
- Throughput (requests/sec)
- Error rate

### Operations
- Mean time to detect (MTTD)
- Mean time to recovery (MTTR)
- Deployment success rate

---

## Project Structure (Planned)

```text
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── embeddings/
├── ingestion/
├── retrieval/
├── rag/
├── agents/
├── evaluation/
├── api/
├── infra/
│   ├── docker/
│   ├── helm/
│   └── terraform/
├── notebooks/
├── tests/
└── README.md

