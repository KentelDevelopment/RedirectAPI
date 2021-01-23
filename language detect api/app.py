from flask import Flask,request,redirect,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    


@app.route('/<language>')
def languageApi(language):
    return {'language':language}

app.run(debug=True)