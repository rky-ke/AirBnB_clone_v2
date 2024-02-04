#!/usr/bin/python3
"""
This module contains the main Flask application for MyFlaskApp.
"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)