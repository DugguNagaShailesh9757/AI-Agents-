import streamlit as st
from google import genai

st.title("Available Models")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

try:
    for model in client.models.list():
        st.write(model.name)
except Exception as e:
    st.error(e)
