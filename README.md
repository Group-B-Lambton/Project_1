---
title: PromptPilot (AML-3304)
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.20.0
app_file: app.py
pinned: false
---

# 🤖 PromptPilot – Unified AI Chatbot (AML-3304)

This is an MVP AI chatbot developed for the **AML-3304 assignment**:

**"From Tokens to Transformers: Building AI Systems with Embeddings, Generative Models, and MLOps."**

PromptPilot combines five intelligent chat modes powered by popular Transformer-based models, enabling users to explore code generation, factual Q&A, probabilistic reasoning, and paraphrasing.

---

## 🔄 Chat Modes

| Mode                    | Description                                                 | Model Used                            |
|-------------------------|-------------------------------------------------------------|----------------------------------------|
| 🧑‍💻 Code Generator       | Generate Python code from plain language                    | `Salesforce/codegen-350M-mono`         |
| 📘 General Q&A          | Factual question answering and explanations                 | `google/flan-t5-base`                  |
| 📊 Bayesian Q&A         | Uncertainty-based reasoning using sampling                  | `google/flan-t5-base` + top-k sampling |
| 🌐 Deep Coder           | Technical Q&A and code completion tasks                     | `deepseek-ai/deepseek-coder-6.7b-instruct` |
| 🔁 Transformer Explorer | Paraphrasing and text transformation using sequence models  | `google/flan-t5-base`                  |

---

## 🚀 Live Demo

Try the chatbot here:  
**🔗 [https://huggingface.co/spaces/Group2255/programming-help-chatbot](https://huggingface.co/spaces/Group2255/programming-help-chatbot)**

---

## 🧩 Features

- Multi-mode UI for interactive exploration  
- Efficient model switching using `st.session_state`  
- GPU-compatible on Hugging Face Spaces  
- Supports both deterministic and sampling-based generation  
- Lightweight models for fast response and free-tier compatibility  

---

## 💻 Run Locally

### ✅ Option 1: Python + Streamlit

```bash
git clone https://huggingface.co/spaces/Group2255/programming-help-chatbot
cd programming-help-chatbot
pip install -r requirements.txt
streamlit run app.py
