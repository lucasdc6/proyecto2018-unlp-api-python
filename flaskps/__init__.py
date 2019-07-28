from os import path
from flask import Flask, render_template, g
from flaskps.db import init_db
from flaskps.resources import issue
from flaskps.resources import user
from flaskps.resources import auth

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=path.join("../db/db.sqlite"),
)

# Example using Blueprint
app.register_blueprint(issue.bp)

# Example using methods
app.add_url_rule("/usuarios", 'user_index', user.index)
app.add_url_rule("/usuarios", 'user_create', user.create, methods=['POST'])
app.add_url_rule("/usuarios/new", 'user_new', user.new)

app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)

# Example on single file
@app.route("/")
def hello():
    return render_template('home.html')


@app.cli.command('initdb')
def initdb_command():
    print("Init db start!")
    init_db()
    print("Init db done!")


