import streamlit as st
from google import genai
from export_utils import export_to_txt
from pathlib import Path

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Travel Itinerary Planner",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS (if available)
# -----------------------------
css_path = Path(__file__).parent / "style.css"

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# App Title
# -----------------------------
st.title("✈️ AI Travel Itinerary Planner")
st.markdown("Plan your perfect trip with Google Gemini AI.")

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# -----------------------------
# User Inputs
# -----------------------------
destination = st.text_input("Destination")

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=3
)

budget = st.selectbox(
    "Budget",
    ["Low", "Medium", "High"]
)

interests = st.text_area(
    "Interests (e.g. beaches, food, adventure, history)"
)

# -----------------------------
# Generate Itinerary
# -----------------------------
if st.button("Generate Itinerary"):

    if destination and interests:

        prompt = f"""
You are an expert AI Travel Planner.

Create a detailed {days}-day travel itinerary.

Destination: {destination}
Budget: {budget}
Interests: {interests}

Include:

- Day-wise itinerary
- Morning activities
- Afternoon activities
- Evening activities
- Tourist attractions
- Local food recommendations
- Hotel recommendations
- Estimated daily budget
- Transportation suggestions
- Travel tips
"""

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            st.subheader("📍 Your Travel Plan")
            st.write(response.text)

            filename = export_to_txt(response.text)

            with open(filename, "rb") as file:
                st.download_button(
                    label="📥 Download Itinerary",
                    data=file,
                    file_name=filename,
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("⚠️ Please fill all the fields.")
