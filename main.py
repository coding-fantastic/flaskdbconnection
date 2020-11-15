from flask import Flask

from flask_sqlalchemy import sqlalchemy


app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')
def index():
   return "<h1>am here </h2>"


if __name__ = "__main__":
    app.run()