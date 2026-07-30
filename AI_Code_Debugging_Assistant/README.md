# 🐞 AI Code Debugging Assistant

An AI-powered Code Debugging Agent that helps programmers identify, understand, and fix coding errors using Large Language Models (LLM). The assistant analyzes source code and compiler/runtime errors, explains the problem in simple language, and provides possible solutions.

## 🚀 Features

- 🐞 Detects programming errors
- 🔍 Explains error causes in simple language
- ✅ Suggests possible fixes
- 💡 Provides improved code solutions
- 📚 Recommends coding style improvements
- ⚡ Suggests performance optimization tips
- 📥 Allows users to download debugging reports

## 🤖 LLM Used

**Google Gemini Flash LLM**

The Large Language Model is used for:

- Code understanding
- Error analysis
- Bug explanation
- Solution generation
- Code improvement suggestions

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK

## 📂 Project Structure

```
AI_Code_Debugging_Assistant/
│
├── app.py                 # Main Streamlit application
├── export_utils.py        # Export debugging report
├── style.css              # Custom UI styling
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
│
└── .streamlit/
    └── config.toml        # Streamlit configuration
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to project folder:

```bash
cd AI_Code_Debugging_Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 API Configuration

Create Streamlit secrets:

```
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY="your_api_key_here"
```

## ▶️ Run Application

Start the Streamlit app:

```bash
streamlit run app.py
```

## 🖥️ How It Works

1. User selects programming language.
2. User enters source code.
3. User provides compiler/runtime error.
4. Gemini LLM analyzes the issue.
5. AI generates:
   - Error explanation
   - Root cause
   - Solution
   - Improved code
   - Optimization tips
6. User can download the debugging report.

## 📸 Application Images 

(Add your Streamlit app screenshot here)

```
![AI Code Debugging Assistant](images/app_images.png)
```

## 🌐 Deployment

The application is deployed using:

- Streamlit Cloud
- GitHub Repository

## 🔮 Future Enhancements

- Support more programming languages
- Real-time code execution
- Integration with GitHub repositories
- AI code review features
- Voice-based debugging assistant

## App Images 

![AI Code Debugging Assistant](images/20260730_232935.jpg,20260730_234127.jpg)
