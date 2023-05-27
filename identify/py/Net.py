from flask import Flask, request
from flask_cors import CORS
import Centre


def mainFunc(put):
    return Centre.middle(put)


app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/', methods=['POST'])
def call_mainFunc():
    url = request.form.get('url')
    res = mainFunc(url)
    return res
app.run(port=55555)

