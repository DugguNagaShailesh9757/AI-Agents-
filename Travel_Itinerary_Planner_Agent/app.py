import streamlit as st
from google import genai
from export_utils import export_to_txt

st.set_page_config(
    page_title="Travel Itinerary Planner",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="expanded"
    with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
)

st.title("✈️ AI Travel Itinerary Planner")
st.markdown("Plan your perfect trip with Google Gemini AI.")

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
                model="gemini-flash-latest",
                contents=prompt
            )

            st.subheader("Your Travel Plan")
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
            st.error(f"Error: {str(e)}")

    else:
        st.warning("Please fill all fields.")
