🎯 Career Guidance Chatbot
This is a simple web-based Career Guidance Chatbot built using Flask and Pandas. It suggests suitable career paths based on the user's interests by matching input keywords with an Excel dataset containing predefined careers and related keywords.

📁 Project Structure
php
Copy
Edit
career-guidance-bot/
├── app.py                  # Main Flask application
├── career_data.xlsx        # Excel file with career paths and keywords
├── templates/
│   ├── index.html          # Input form template
│   └── result.html         # Result display template
├── static/                 # (Optional) Static files like CSS/images
└── README.md               # Project documentation
⚙️ Features
Match user interests with keyword-based career suggestions.

Fallback mechanism using random suggestions when no matches are found.

Friendly error messages and clean UI (HTML templates required).

Simple and extendable logic using an Excel dataset.

📝 How It Works
Load career data from an Excel file (career_data.xlsx).

The user submits their interests via a form.

Keywords are matched against the dataset.

Top 3 matching careers are displayed. If none match, 3 random careers are shown as fallback.

📦 Requirements
Install the following Python packages:

bash
Copy
Edit
pip install flask pandas openpyxl
🚀 Getting Started
Clone the repository or copy the code.

Make sure you have an Excel file named career_data.xlsx with the following structure:

Career	Keywords
Data Scientist	data, statistics, python
Doctor	medicine, health, biology
Artist	painting, creativity, design

Run the app:

bash
Copy
Edit
python app.py
Open your browser and go to http://localhost:5000.

💡 Customization
Add more careers and keywords in the career_data.xlsx file.

Enhance UI by modifying templates/index.html and result.html.

Connect with a database for dynamic keyword updates (optional).

📌 Notes
The project is for learning/demo purposes and can be extended to include ML/NLP techniques.

Ensure your Excel file has the correct format with columns: Career, Keywords.

