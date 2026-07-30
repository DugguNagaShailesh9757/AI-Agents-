import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="Smart Email Assistant",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Smart Email Assistant")

st.write("Generate professional emails using Google Gemini AI.")

recipient = st.text_input("Recipient")

subject = st.text_input("Subject")

purpose = st.text_area("Purpose")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Formal"]
)

if st.button("Generate Email"):

    prompt = f"""
    You are an expert email writer.

    Write a professional email using the following details.

    Recipient: {recipient}

    Subject: {subject}

    Purpose: {purpose}

    Tone: {tone}
    """

    response = model.generate_content(prompt)

    st.subheader("Generated Email")

    st.write(response.text)
