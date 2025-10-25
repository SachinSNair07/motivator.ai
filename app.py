from flask import Flask, jsonify, render_template
import os, random

app = Flask(__name__)

# File path for storing quotes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUOTES_FILE = os.path.join(BASE_DIR, "quotes.txt")

def load_quotes():
    """Load quotes from file or create default ones if not found."""
    if not os.path.exists(QUOTES_FILE):
        default_quotes = [
            "Believe in yourself and your abilities.",
            "Never give up — every setback is a setup for a comeback.",
            "Discipline beats motivation every single time.",
            "The best way to predict the future is to create it.",
            "Push harder than yesterday if you want a different tomorrow."
        ]
        with open(QUOTES_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(default_quotes))
        return default_quotes
    
    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()]
            return quotes if quotes else ["No quotes found in file."]
    except Exception as e:
        print(f"[ERROR] Couldn't load quotes: {e}")
        return ["Error loading quotes."]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def random_quote():
    quotes = load_quotes()
    return jsonify({"status": "success", "quote": random.choice(quotes)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # works for Render/Replit too
    app.run(host="0.0.0.0", port=port, debug=True)





