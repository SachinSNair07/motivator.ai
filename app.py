from flask import Flask, render_template
import random

app = Flask(__name__)

# Function to load motivational quotes from the text file
def load_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = [line.strip() for line in file if line.strip()]
    return quotes

@app.route("/")
def home():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    # Use 0.0.0.0 for Render or Replit hosting compatibility
    app.run(host="0.0.0.0", port=5000)




