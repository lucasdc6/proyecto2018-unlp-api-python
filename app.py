from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('layout.html')


@app.route("/consultas")
def issues():
    return render_template('issues/index.html')


if __name__ == "__main__":
  app.run(debug=True)
