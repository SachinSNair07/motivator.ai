from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

def load_quotes():
    try:
        if not os.path.exists("quotes.txt"):
            # Create file automatically if not found
            with open("quotes.txt", "w", encoding="utf-8") as f:
                f.write("Believe in yourself.\nKeep going no matter what.\nDream big and stay focused.\n")
            print("quotes.txt file created with default quotes.")

        with open("quotes.txt", "r", encoding="utf-8") as file:
            quotes = [q.strip() for q in file.readlines() if q.strip()]
            return quotes if quotes else ["No quotes found in file."]
    except Exception as e:
        print(f"Error loading quotes: {e}")
        return ["Error reading quotes file. Please try again later."]

@app.route('/get_quote', methods=['GET'])
def get_random_quote():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)













