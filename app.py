from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Always use full path for safety
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUOTES_PATH = os.path.join(BASE_DIR, "quotes.txt")

def load_quotes():
    try:
        if not os.path.exists(QUOTES_PATH):
            default_quotes = [
                "Believe in yourself.",
                "Never give up on your dreams.",
                "Discipline beats motivation.",
                "Every expert was once a beginner.",
                "Push harder than yesterday if you want a different tomorrow.",
            ]
            with open(QUOTES_PATH, "w", encoding="utf-8") as f:
                f.write("\n".join(default_quotes))
            return default_quotes
        else:
            with open(QUOTES_PATH, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[ERROR] Failed to load quotes: {e}")
        return ["Error loading quotes. Please try again later."]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to your Motivational AI 🚀",
        "endpoints": {
            "/quote": "Get a random motivational quote"
        }
    })

@app.route("/quote")
def get_quote():
    quotes = load_quotes()
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)







