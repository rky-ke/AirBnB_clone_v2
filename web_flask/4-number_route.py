#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/<text>: display “Python ”, followed by the value of the 
    text variable
"""


from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces in the text variable
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    # Replace underscores with spaces in the text variable
    text = escape(text).replace('_', ' ')
    return 'Python {}'.format(text)

@app.route("/number/<int:number>", strict_slashes=False)
def number(number):
        return '{} is a number'.format(number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
