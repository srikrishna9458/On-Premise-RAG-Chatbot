# On-Premise RAG Chatbot
**Stack:** Python | LangChain | Ollama | ChromaDB | Llama 3.2

Aura-RAG is a localized Retrieval-Augmented Generation (RAG) system designed to interact with private document sets without external API dependencies. This project demonstrates the implementation of a secure, local-first AI architecture that prioritizes data sovereignty and privacy.


## Overview
Standard LLM implementations often require transmitting sensitive data to third-party cloud providers. Aura-RAG solves this by utilizing a local inference engine (Ollama) and a local vector database (ChromaDB), ensuring that all data processing remains on the host machine.

## Technical Stack
* Orchestration: LangChain (LCEL)
* LLM: Llama 3.2 (via Ollama)
* Vector Database: ChromaDB
* Embeddings: nomic-embed-text
* Development Environment: Python 3.13

## Core Logic
1. Ingestion: Processes unstructured data from local directories (PDF, CSV).
2. Document Chunking: Implements recursive character splitting to maintain semantic context within model window limits.
3. Vectorization: Converts text chunks into high-dimensional embeddings using the nomic-embed-text model.
4. Semantic Retrieval: Employs vector similarity search to identify relevant context for user queries.
5. Grounded Generation: Augments the LLM prompt with retrieved context to ensure deterministic and factually accurate responses.

## Setup and Installation
1. Install Ollama and pull the required model:
   ```bash
   ollama pull llama3.2