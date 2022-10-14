from flask import Flask
from random import randint
app = Flask(__name__)

random_number = randint(0, 10)


@app.route('/')
def index():
    return "<h1>Guess a number between 0 and 9!<h2> \
          <p>Type on the address bar your guess.</p>"


@app.route('/<int:number>')
def guess_page(number):
    print(random_number)
    if number < random_number:
        return "<h1 style='color: red'>Too low! Try again</h1>"
    elif number > random_number:
        return "<h1 style='color: red'>Too High! Try again</h1>"
    else:
        return f"<h1 style='color: green'>You guessed correctly! The number was {random_number}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
