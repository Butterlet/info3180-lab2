from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Function to format the joined date
def format_date_joined(date):
    return date.strftime("%B, %Y")

@app.route('/profile')
def profile():
    user = {
        "photo": "Paris.jpg", 
        "full_name": "Paris Wolfe",
        "username": "@withloveparis",
        "location": "Kingston, Jamaica",
        "date_joined": format_date_joined(datetime(2018, 1, 1)),
        "bio": " Hello<3, I'm Paris and I love cats and the color pink. Additionally, I enjoy designing websites and drawing. If you'd like to work together, please contact me!.",
        "posts": 7,
        "followers": 250,
        "following": 100
    }
    return render_template("profile.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)