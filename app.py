# app.py
# PromptPilot: Unified AI Chatbot with 5 Modes (AML-3304 Assignment)

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import torch

st.set_page_config(page_title="PromptPilot - Unified AI Chatbot", layout="centered")
st.title("🤖 PromptPilot - Unified AI Chatbot")
st.markdown("AML-3304 Assignment: From Tokens to Transformers")

# Initialize session state
if 'mode' not in st.session_state:
    st.session_state.mode = 'Code Generator'

# UI Buttons
cols = st.columns(5)
with cols[0]:
    if st.button("🧑‍💻 Code Generator"):
        st.session_state.mode = 'Code Generator'
with cols[1]:
    if st.button("📘 General Q&A"):
        st.session_state.mode = 'General Q&A'
with cols[2]:
    if st.button("📊 Bayesian Q&A"):
        st.session_state.mode = 'Bayesian Q&A'
with cols[3]:
    if st.button("🌐 Deep Coder"):
        st.session_state.mode = 'Deep Coder'
with cols[4]:
    if st.button("🔁 Transformer Explorer"):
        st.session_state.mode = 'Transformer Explorer'

st.markdown(f"### 🔄 Current Mode: **{st.session_state.mode}**")

# User input
user_input = st.text_area("Enter your prompt/question:")

# Load models
@st.cache_resource
def load_codegen():
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")
    return tokenizer, model

@st.cache_resource
def load_flan():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    return tokenizer, model

# Inference
if user_input and st.session_state.mode:
    with st.spinner("Generating response..."):
        if st.session_state.mode == 'Code Generator':
            tokenizer, model = load_codegen()
            inputs = tokenizer(user_input, return_tensors="pt")
            outputs = model.generate(inputs["input_ids"], max_new_tokens=128, do_sample=True, temperature=0.7, pad_token_id=tokenizer.eos_token_id)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.subheader("💻 Generated Code:")
            st.code(result, language="python")

        elif st.session_state.mode == 'General Q&A':
            tokenizer, model = load_flan()
            inputs = tokenizer(user_input, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=150)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.subheader("📘 Answer:")
            st.write(result)

        elif st.session_state.mode == 'Bayesian Q&A':
            tokenizer, model = load_flan()
            inputs = tokenizer(user_input, return_tensors="pt")
            outputs = model.generate(**inputs, do_sample=True, top_k=40, temperature=0.9, max_new_tokens=100)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.subheader("📊 Bayesian-style Answer:")
            st.write(result)

        elif st.session_state.mode == 'Deep Coder':
            tokenizer, model = load_codegen()
            inputs = tokenizer(user_input, return_tensors="pt")
            outputs = model.generate(inputs["input_ids"], max_new_tokens=128, do_sample=True, temperature=0.8)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.subheader("🌐 Code Output:")
            st.code(result, language="python")

        elif st.session_state.mode == 'Transformer Explorer':
            tokenizer, model = load_flan()
            prompt = f"Paraphrase this: {user_input}"
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=100)
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.subheader("🔁 Paraphrased Text:")
            st.write(result)
