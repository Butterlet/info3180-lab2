from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Function to format the joined date
def format_date_joined(date):
    return date.strftime("%B, %Y")

@app.route('/profile')
def profile():
    user = {
        "photo": "profile.jpg",  # Image should be in 'static/images/'
        "full_name": "Mary Jane",
        "username": "@mjane",
        "location": "Kingston, Jamaica",
        "date_joined": format_date_joined(datetime(2018, 1, 1)),
        "bio": "I am a smart and talented young woman who loves website design and development. Contact me if you'd like to work together on a new project.",
        "posts": 7,
        "followers": 250,
        "following": 100
    }
    return render_template("profile.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)