from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from flaskps.db import get_db
from flaskps.models.issue import Issue

bp = Blueprint('issue', __name__, url_prefix='/consultas')

@bp.route("/")
def index():
    db = get_db()
    issues = Issue(db).all()

    return render_template('issue/index.html', issues=issues)

@bp.route("/new")
def new():
    return render_template('issue/new.html')


@bp.route("/new", methods=['POST'])
def create():
    db = get_db()
    Issue(db).create(request.form)
    return redirect(url_for('issue.index'))

