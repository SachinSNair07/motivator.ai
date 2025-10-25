from flask import Flask, render_template
import random

app = Flask(__name__)

def load_quotes():
   def load_quotes():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["No quotes found. Please add a quotes.txt file."]


@app.route("/")
def home():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)














