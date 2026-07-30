import streamlit as st
from google import genai

st.set_page_config(
    page_title="Travel Itinerary Planner",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ AI Travel Itinerary Planner")

# Gemini Client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

destination = st.text_input("Destination")
days = st.number_input("Number of Days", min_value=1, max_value=30, value=3)
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
interests = st.text_area(
    "Interests (e.g. beaches, food, adventure, history)"
)

if st.button("Generate Itinerary"):
    if destination and interests:

        prompt = f"""
Create a detailed {days}-day travel itinerary.

Destination: {destination}
Budget: {budget}
Interests: {interests}

Include:
- Day-wise schedule
- Morning, Afternoon, Evening plans
- Food recommendations
- Estimated daily budget
- Travel tips
"""

        try:
            response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)
            

            st.subheader("Your Travel Plan")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")

    else:
        st.warning("Please fill all fields.")
