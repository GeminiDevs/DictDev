from flask import Flask, render_template, request
import dictionary
from dictionary import dictionary

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


# get the form input
@app.route('/getform', methods=['POST', 'GET'])
def getform():
    if request.method == "POST":
        search = request.form['search']

    return render_template("index.html", meaning=dictionary(search), word=search.upper())


if __name__ == '__main__':
    app.run(debug=True)
