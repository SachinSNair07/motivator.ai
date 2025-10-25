from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Function to load or create quotes
def load_quotes():
    if not os.path.exists("quotes.txt"):
        default_quotes = [
            "Believe in yourself.",
            "Never give up on your dreams.",
            "Discipline beats motivation.",
            "Every expert was once a beginner.",
            "Push harder than yesterday if you want a different tomorrow.",
        ]
        with open("quotes.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(default_quotes))
        return default_quotes
    else:
        with open("quotes.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to your Motivational AI!",
        "endpoints": {
            "/quote": "Get a random motivational quote"
        }
    })

# Random quote route
@app.route("/quote")
def get_quote():
    quotes = load_quotes()
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)






