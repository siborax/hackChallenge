from flask import Flask
import nlpcloud
import difflib
import requests
import json
from flask import send_file
app = Flask(__name__)
#textSum =  TextSummarization()

@app.route("/")
def index():
    return "Welcome to the page!</p>"

@app.route("/GetSummarization/")
def getVoiceData():
    return "SummarizedData!"

@app.route("/GetText/<string:text>")
def getTextData(text):
    return text
