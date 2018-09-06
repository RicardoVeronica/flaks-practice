import os

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

dbdir = f'sqlite:///{os.path.abspath(os.getcwd())}/db.sqlite'

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
