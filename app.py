from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['POST'])
def whisper(request):
    f = request.files['file']
    f.save(f.filename)
    console.log('a')
