from flask import Flask, render_template, request
from dictionary import Dictionary

app = Flask(__name__)
dictObject = Dictionary()


@app.route('/')
def index():
    return render_template("index.html")


# get the form input
@app.route('/getform', methods=['POST', 'GET'])
def getform():
    if request.method == "POST":
        search = request.form['search']
        if dictObject.noun(word=search):
            result = dictObject.noun(search)
        elif dictObject.verb(word=search):
            result = dictObject.verb(word=search)
        elif dictObject.adjective(word=search):
            result = dictObject.adjective(word=search)
        elif dictObject.trans_verb(word=search):
            result = dictObject.trans_verb(search)

    return render_template("index.html", meaning=result, word=search.upper())


if __name__ == '__main__':
    app.run(debug=True)
