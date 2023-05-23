from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello')
def hello():
    return 'Hello, World'
