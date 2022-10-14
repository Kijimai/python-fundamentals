from flask import Flask

app = Flask(__name__)

print(__name__)

# Python decorator - a function that gives additional functionality to an existing function
# It calls the function that is directly below it
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run()
