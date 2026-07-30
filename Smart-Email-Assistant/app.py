import streamlit as st
from google import genai
from export_utils import export_to_txt

st.set_page_config(
    page_title="Smart Email Assistant",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Smart Email Assistant")
st.write("Generate professional emails using Google Gemini AI.")

# Gemini Client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

recipient = st.text_input("Recipient")
subject = st.text_input("Subject")
purpose = st.text_area("Purpose")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Formal"]
)

if st.button("Generate Email"):
    try:
        prompt = f"""
Write a professional email.

Recipient: {recipient}
Subject: {subject}
Purpose: {purpose}
Tone: {tone}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        email = response.text

        st.subheader("Generated Email")
        st.write(email)

        st.download_button(
            label="📥 Download Email",
            data=email,
            file_name="generated_email.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Error: {e}")
