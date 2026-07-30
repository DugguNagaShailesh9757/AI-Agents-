
✈️ AI Travel Itinerary Planner

An AI-powered travel planner built with Streamlit and Google Gemini AI. This application generates personalized travel itineraries based on the user's destination, trip duration, budget, and interests.

🚀 Features

- 🌍 Personalized travel itinerary generation
- 📅 Day-wise travel schedule
- 🍽️ Food recommendations
- 💰 Budget estimation
- 🧳 Travel tips and suggestions
- ⚡ Fast AI-powered responses using Google Gemini

🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK

📂 Project Structure

travel-itinerary-planner/
│── app.py
│── requirements.txt
│── README.md
└── .streamlit/
    └── secrets.toml

⚙️ Installation

1. Clone the repository.
2. Install the dependencies:

pip install -r requirements.txt

3. Create a ".streamlit/secrets.toml" file and add:

GEMINI_API_KEY="YOUR_API_KEY"

4. Run the application:

streamlit run app.py

📸 How to Use

1. Enter your destination.
2. Select the number of travel days.
3. Choose your budget.
4. Enter your interests (adventure, beaches, food, history, etc.).
5. Click Generate Itinerary.
6. Receive a complete AI-generated travel plan.

🎯 Future Improvements

- Hotel recommendations
- Flight suggestions
- Weather integration
- Google Maps integration
- PDF export
- Multi-language support
