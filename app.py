from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

QUOTES_FILE = "quotes.txt"

def load_quotes():
    """Load quotes from a file, or create one with defaults if missing."""
    try:
        if not os.path.exists(QUOTES_FILE):
            default_quotes = [
                "Believe in yourself and all that you are.",
                "Success is the sum of small efforts repeated daily.",
                "Stay positive, work hard, make it happen.",
                "Push yourself, because no one else is going to do it for you.",
                "Dream big. Start small. Act now."
            ]
            with open(QUOTES_FILE, "w", encoding="utf-8") as f:
                f.write("\n".join(default_quotes))
            print(f"{QUOTES_FILE} created with default quotes.")
            return default_quotes

        with open(QUOTES_FILE, "r", encoding="utf-8") as file:
            quotes = [line.strip() for line in file.readlines() if line.strip()]
            return quotes if quotes else ["No quotes found. Add more to quotes.txt!"]

    except Exception as e:
        print(f"⚠️ Error reading {QUOTES_FILE}: {e}")
        return ["Error loading motivational quotes. Please try again later."]

@app.route('/api/quotes', methods=['GET'])
def get_quote():
    """Return a random motivational quote in JSON format."""
    quotes = load_quotes()
    quote = random.choice(quotes)
    return jsonify({
        "status": "success",
        "quote": quote
    })

@app.route('/', methods=['GET'])
def home():
    """Simple homepage route."""
    return jsonify({
        "message": "Welcome to the Motivational Quotes API",
        "endpoint": "/api/quotes"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)






