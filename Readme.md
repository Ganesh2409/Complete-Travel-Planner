# ✈️ Complete Travel Planner

A smart, AI-powered travel itinerary generator built with Streamlit and Google Gemini AI.

## 🛠️ Features
- ✅ Generates a full travel plan from departure to return
- 🏨 Provides daily itineraries with activity recommendations
- 💰 Budget-conscious suggestions for meals and accommodations
- 🛫 Travel logistics with estimated duration and cost
- 🎯 Personalized recommendations based on interests
- 📅 Supports multi-day trips with structured day-wise plans

## 🖥️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, Google Generative AI (Gemini)
- **APIs:** Google Gemini AI
- **Other Tools:** Docker, Git

## 📁 Directory Structure
```
📦 Complete-Travel-Planner
 ┣ 📜 app.py         # Main Streamlit app
 ┣ 📜 prompts.py     # AI prompt templates
 ┣ 📜 utils.py       # Helper functions
 ┗ 📜 README.md      # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Streamlit
- Google Generative AI API key

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/Complete-Travel-Planner.git
cd Complete-Travel-Planner

# Install dependencies
pip install -r requirements.txt

# Add API key to Streamlit secrets
echo "GEMINI_API_KEY='your_api_key'" > ~/.streamlit/secrets.toml
```

### Running the App
```bash
streamlit run app.py
```

## 📖 Documentation

### How It Works
1. **User Input:** The user provides details like destination, travel dates, budget, and interests.
2. **AI Processing:** The `prompts.py` file structures the input into well-defined queries for the AI model.
3. **Itinerary Generation:** The Google Gemini AI processes the request and generates an optimized travel itinerary.
4. **Display in Streamlit:** The results are formatted and displayed using Streamlit's UI components.
5. **Refinement:** Users can refine their itinerary based on feedback, preferences, and additional inputs.

### Code Breakdown
- `app.py`: Handles the Streamlit UI and integrates AI responses.
- `prompts.py`: Contains structured prompts for refining AI responses.
- `utils.py`: Includes helper functions for formatting and validating user inputs.

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## 📫 Contact
- **GitHub:** [Ganesh2409](https://github.com/Ganesh2409)
- **Email:** pinnamaneniganesh24@gmail.com
 ```
© 2025 Complete-Travel-Planner . Made with ❤️
```

