import streamlit as st
from google import genai
from export_utils import export_to_txt
from pathlib import Path

st.set_page_config(
    page_title="AI Code Debugging Assistant",
    page_icon="🐞",
    layout="centered"
)

# Load CSS
css_path = Path(__file__).parent / "style.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🐞 AI Code Debugging Assistant")
st.markdown("Fix coding errors with Google Gemini AI.")

# Gemini Client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

language = st.selectbox(
    "Programming Language",
    ["Python", "Java", "C", "C++", "JavaScript", "HTML", "CSS", "Other"]
)

code = st.text_area("Paste your source code", height=250)

error = st.text_area(
    "Paste compiler/runtime error",
    height=120
)

if st.button("Debug Code"):

    if code and error:

        prompt = f"""
You are an expert software engineer.

Programming Language:
{language}

Source Code:
{code}

Compiler/Runtime Error:
{error}

Please provide:

1. Error Explanation (Simple Language)
2. Root Cause
3. Correct Solution
4. Improved Code
5. Code Quality Suggestions
6. Performance Tips

Use headings and bullet points.
"""

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            st.subheader("🐞 Debug Report")
            st.write(response.text)

            filename = export_to_txt(response.text)

            with open(filename, "rb") as file:
                st.download_button(
                    "📥 Download Report",
                    data=file,
                    file_name=filename,
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter both source code and the error message.")
