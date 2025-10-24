import random
import pyttsx3

def get_random_quote():
    with open("quotes.txt", "r", encoding="utf-8") as f:
        quotes = f.readlines()
    return random.choice(quotes).strip()

def speak_quote(quote):
    engine = pyttsx3.init()
    engine.say(quote)
    engine.runAndWait()

def main():
    print("💬 Welcome to Motivator AI 💬")
    print("-----------------------------")

    while True:
        quote = get_random_quote()
        print(f"\n🌟 {quote}")
        speak_quote(quote)

        next_quote = input("\nWant another quote? (y/n): ").lower()
        if next_quote != "y":
            print("\n💖 Stay strong! Keep pushing forward!")
            break

if __name__ == "__main__":
    main()
