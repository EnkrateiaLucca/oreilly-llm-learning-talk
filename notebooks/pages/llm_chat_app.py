import streamlit as st
from langchain.llms import OpenAI


openai_api_key = "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"

st.title("LLM Question App")

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)