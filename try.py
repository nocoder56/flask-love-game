from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_word = random.choice(['love', 'wifeyy', 'naughty', 'peace', 'happiness'])
attempts = 5

def give_compliment():
    compliments = [
        "You're the best thing that ever happened to me! 💖",
        "I love you more than anything Anu. 🌟",
       "I’m lucky to have you by my side chellakutty. ❤️"
    ]
    return random.choice(compliments)

@app.route('/', methods=['GET', 'POST'])
def index():
    global attempts
    message = ""
    if request.method == 'POST':
        guess = request.form.get('guess')
        if guess:
            guess = guess.lower()
            if guess == secret_word:
                message = f"Yay! You guessed it right! The word was '{secret_word}'. {give_compliment()}"
                attempts = 5  # reset
            else:
                attempts -= 1
                message = f"Oops! That’s not it. {attempts} attempts left."
                if attempts == 0:
                    message = f"You’re out of attempts. The word was '{secret_word}'. Still you are amazing chellakutty i love you soo much Anu! 😘"
                    attempts = 5
        else:
            message = "Please enter a guess!"
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
