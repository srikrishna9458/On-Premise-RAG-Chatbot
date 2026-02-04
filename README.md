# Aura-RAG: On-Premise Chatbot
**Stack:** Python | LangChain | Ollama | ChromaDB | Streamlit

Aura-RAG is a localized Retrieval-Augmented Generation (RAG) system designed to interact with private document sets without external API dependencies. This project prioritizes data sovereignty and privacy.

## Technical Stack
* **Orchestration:** LangChain (LCEL)
* **LLM:** Llama 3.2 (via Ollama)
* **Vector Database:** ChromaDB
* **Embeddings:** mxbai-embed-large
* **Frontend:** Streamlit

## Core Logic
1. **Ingestion:** Processes unstructured CSV data.
2. **Vectorization:** Converts text into high-dimensional embeddings using `mxbai-embed-large`.
3. **Semantic Retrieval:** Employs vector similarity search via ChromaDB.
4. **Grounded Generation:** Augments the LLM prompt with retrieved context for accurate responses.

## Frontend Features
* **Interactive Chat UI:** Responsive dashboard built with Streamlit.
* **Session State:** Maintains conversation history during the active session.
* **Source Attribution:** Collapsible "Source Context" to verify model outputs.

## Setup and Installation
1. **Pull Models:**
   ```bash
   ollama pull llama3.2
   ollama pull mxbai-embed-large
