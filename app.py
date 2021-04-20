from flask import Flask
from email_class import *
from flask_cors import CORS
import csv23
import os

app = Flask(__name__)
CORS(app)
cors=CORS(app,resources={
	'r"/*"':{
	"origins":"*"
	}
	})

@app.route('/')
def predict():
    return "Demo page"

@app.route('/<string:message>')
def func2(message):
    type = message_classifier(message)

    string =  type
    return string
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)


# string = "http://127.0.0.1:4000/" + message
