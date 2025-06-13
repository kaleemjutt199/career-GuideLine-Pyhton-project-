from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Load Excel data
df = pd.read_excel('career_data.xlsx', engine='openpyxl')

# Build the career path dictionary
career_paths = {
    row['Career']: [k.strip().lower() for k in row['Keywords'].split(',')]
    for _, row in df.iterrows()
}

# Function to get career recommendations
def get_career_recommendations(user_input):
    user_input = user_input.lower()
    career_scores = {career: 0 for career in career_paths}
    for career, keywords in career_paths.items():
        for keyword in keywords:
            if keyword in user_input:
                career_scores[career] += 1
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    return [career for career, score in sorted_careers if score > 0]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['interests']
        if user_input.strip():
            recommendations = get_career_recommendations(user_input)
            if not recommendations:
                recommendations = random.sample(list(career_paths.keys()), 3)
                return render_template('result.html', recommendations=recommendations, fallback=True)
            return render_template('result.html', recommendations=recommendations[:3], fallback=False)
        else:
            return render_template('index.html', error="⚠️ Please enter something to get recommendations.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
