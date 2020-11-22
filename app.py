from flask import Flask, render_template, request
from dictionary import Dictionary, error_message

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

        """
        We are checking whether each type of word is available.
        If it is, then make it the result. 
        e.g..
        If the noun word is available, then the result is the noun word.
        It may be a shitty way of doing things, but it works so I won't touch it anymore
        """

        if dictObject.noun(word=search):
            result = dictObject.noun(search)
        elif dictObject.verb(word=search):
            result = dictObject.verb(word=search)
        elif dictObject.adjective(word=search):
            result = dictObject.adjective(word=search)
        elif dictObject.trans_verb(word=search):
            result = dictObject.trans_verb(search)
        else:
            result = error_message

    return render_template("index.html", meaning=result, word=search.upper(), audio=dictObject.audio(word=search))


if __name__ == '__main__':
    app.run(debug=True)
