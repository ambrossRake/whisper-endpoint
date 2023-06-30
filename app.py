from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/whisper', methods=['POST']):
def whisper(request):
    f = request.files['file']
    f.save(f.filename)
    console.log('a')