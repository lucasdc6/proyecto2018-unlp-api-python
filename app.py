from flask import Flask
from flask import render_template
from os import path
from db import init_db

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=path.join('db/db.sqlite'),
)

@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/consultas")
def issues():
    return render_template('issues/index.html')


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print("Vamooooo")


if __name__ == "__main__":
    app.run(debug=True)
