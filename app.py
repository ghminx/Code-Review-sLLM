import streamlit as st
from code_review_llm import code_review, translate_deepl
import os
import time

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

def stream_data(text):
    for line in text.split("\n"):
        yield line
        time.sleep(0.1)
        
        
st.title('Code Review')

code_input = st.text_area("enter the code:", height=300)

model_name = st.selectbox("Model", ["yi-coder:1.5b", "qwen2.5-coder","deepseek-coder:6.7b-instruct"])

if st.button("Run"):
    if code_input.strip():
        with st.spinner("Running Code Review..."):
            
            result = code_review(model_name, code_input)
            translated_text = translate_deepl(result, DEEPL_API_KEY)
        
            st.markdown("### Code Review Result")
            output_area = st.empty()  

            full_text = "" 

            for chunk in stream_data(translated_text):
                full_text += chunk + "\n"  
                output_area.markdown(full_text)  

        
    else:
        st.warning("please enter the code")
