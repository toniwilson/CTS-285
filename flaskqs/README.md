Flask

Installation
> mkdir myproject
> cd myproject
> py -3 -m venv .venv

Activation
> .venv\Scripts\activate

Install Flask
$ pip install Flask

Quickstart
- minimal application

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"
