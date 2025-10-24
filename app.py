from flask import Flask, render_template
import random

app = Flask(__name__)

def get_random_quote():
    with open("quote.txt", "r", encoding="utf-8") as f:
        quotes = f.readlines()
    return random.choice(quote).strip()

@app.route("/")
def home():
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)


