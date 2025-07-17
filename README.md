
# medical-rag

This repository is the codebase for a simple MVP of an RAG system interating with medical knowledge-bases. Submitted as an assignment for Wundrsight Health.

---

## 🚀 Core Features

- Natural language prompting using LLMs and context aware generation.
- FAISS-based Vector Search for efficient retrieval of semantically similar document chunks.
- Streamlit UI: A simple and intuitive web interface for querying and viewing model responses.
- Modular codebase for future functionality ingestions.
- Dynamic document uploads for real-time RAG.


---

## 📦 Project Structure

```bash
|── medical-rag/ 
  ├── context/       # FAISS semnantic retrieval 
  ├── data/          # Knowledge-bases and FAISS index cached for faster loading
  ├── model/         # LLM integration and response generation with context
  ├── utils/         # Preprocessing and other helper modules
  ├── main.py/       # Primary script file to be executed
  ├── Readme.md
  ├── Requirements.txt        
```

---

## 🛠️ Tools

| 🔧 Component       |  Why This Choice                                                                                      |
|--------------------|---------------------------------------------------------------------------------------------------------|
| **Embeddings Model** | `"all-MiniLM-L6-v2"` solid trade-off between speed and accuracy; fine-tuned for semantic similarity tasks, ideal for RAG pipelines. |
| **PyPDF2**         | Lightweight and reliable library for extracting text from PDFs - no abstractions or dependency overheads |
| **Streamlit**      | Rapid development yet a offers an interactive real-time UI|
| **LLM**            | `"mistralai/Mistral-7B-Instruct-v0.3"` – Open-weight, instruction-tuned model that offers a good responses |



### Requirements

- Python 3.10+
- `.env` file with:
  - `hf_api_key` #if using hf models with license restrictions.

### Setup

```bash
# Clone the repository
git clone https://github.com/rulezcasa/medical-rag.git
cd medical-rag

# Install dependencies
pip install -r requirements.txt

# Run the script
strealit run main.py

```

---


### Example functionality
<img width="823" height="401" alt="Screenshot 2025-07-17 at 1 33 16 PM" src="https://github.com/user-attachments/assets/36324311-f7d7-48a9-b2b6-24ae6cb031cf" />

---

## Tasks I could take up in due time:

- **Heavy Models Slow Inference:**  
  Using large LLMs led to high latency. A better choice focusing on the trade-off between performance and speed is needed — or some quantization techniques.

- **Ground Truth Data:**  
  I'm not sure if the reponses are relevant and valid, interested to set up an evaluation pipeline for the developed system.

- **Lack of Domain Specialization:**  
  General models work, but medical-specific models like BioBERT, ClinicalBERT, or PubMedBERT should be explored with ablation studies to improve relevance and accuracy.

- **LangChain Integration:**  
  Explore using frameworks like LangChain for structured RAG pipelines, memory handling, tool use, and easier integration with APIs or agents.

- **UI/UX - webapp:**  
  And offcourse, make it more more intutive as a webapp, set up a backend architecture and deploy it as well.


---

## Logical explanations:

Commented explanations inside certain modules are added to explicity clarify the logic.

- **chunking logic:** : ```utils/data_processing.py```
- **prompt logic:** : ```model/generate.py```


---



## AI usage declaration
- To understand and select the most suitable hf model for sentence embedding and generation. 
- To explore FAISS indexing and retrieval mechanisms, against my familiarity with real-time dbs like Qdrant.
- To insert docstrings for functions.
- Some level of core structuring and formatting.




## 🧑‍💻 Authors
- [@rulezcasa](https://gitlab.com/rulezcasa) - Maintainer & Developer

---

## 📈 Project Status

🚧 Actively in development – No stable builds or deployed versions available yet.
---
