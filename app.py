from flask import Flask
from flask import render_template
from flask import request
from os import path
from db import init_db, get_db

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
    db = get_db()
    data = db.execute('SELECT * FROM issues').fetchall()
    return render_template('issues/index.html', issues=data)


@app.route("/consultas/new", methods=['POST'])
def create_issue():
    db = get_db()
    db.execute('INSERT INTO issues (email, description, category_id, status_id) VALUES (:email, :description, :category_id, :status_id)', request.form)
    db.commit()
    return 'POST'

@app.route("/consultas/new")
def new_issue():
    return render_template('issues/new.html')

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print("Vamooooo")


if __name__ == "__main__":
    app.run(debug=True)
