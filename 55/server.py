from flask import Flask
from random import randint
app = Flask(__name__)

random_number = randint(1, 11)


def make_bold(func):
  def wrapper():
    return f"<b>{func()}</b>"
  return wrapper


def make_underline(func):
  def wrapper():
      return f"<u>{func()}</u>"
  return wrapper

def make_italic(func):
  def wrapper():
      return f"<em>{func()}</em>"
  return wrapper

@app.route("/")
@make_bold
@make_italic
@make_underline
def index():
    return "Guess a number between 1 and 10!"


@app.route("/<int:number>")
def guess(number):
    print(random_number)
    if number == random_number:
        return f'<div> \
                    <h1>You guessed it right! it was {number}</h1> \
                    <img alt="kitten" src="https://media2.giphy.com/media/cODtmm19jmTv2/giphy.gif?cid=ecf05e47rdpauoch2ot6hapx8ohinx5y69ko5qdjgh5s5sh0&rid=giphy.gif&ct=g"/> \
                  </div>'
    else:
        return "Incorrect Guess!"


@app.route("/<path:username>")
def new_path(username):
    return f"Hello {username}!"


if __name__ == "__main__":
    app.run(debug=True)
