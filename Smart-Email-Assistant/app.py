import streamlit as st

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
    st.info("Gemini AI integration will be added in the next step.")
