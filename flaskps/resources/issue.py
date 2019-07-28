from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from flaskps.db import get_db
from flaskps.models.issue import Issue

bp = Blueprint('issue', __name__, url_prefix='/consultas')

@bp.route("/")
def index():
    Issue.db = get_db()
    issues = Issue.all()

    return render_template('issue/index.html', issues=issues)

@bp.route("/new")
def new():
    return render_template('issue/new.html')


@bp.route("/", methods=['POST'])
def create():
    Issue.db = get_db()
    Issue.create(request.form)

    return redirect(url_for('issue.index'))

