from flask import Flask, jsonify, render_template
import random
import os

app = Flask(__name__)

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
                "Push harder than yesterday if you want a different tomorrow."
            ]
            with open(QUOTES_PATH, "w", encoding="utf-8") as f:
                f.write("\n".join(default_quotes))
            return default_quotes

        with open(QUOTES_PATH, "r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()]
            return quotes if quotes else ["No quotes found. Add some to quotes.txt."]
    except Exception as e:
        # Log error so you can see it in console / render logs
        print(f"[ERROR] Failed to load quotes: {e}")
        return ["Error loading quotes."]

@app.route("/")
def homepage():
    # Renders templates/index.html
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    quotes = load_quotes()
    return jsonify({"status": "success", "quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)








