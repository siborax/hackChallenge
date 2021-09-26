from flask import Flask
import nlpcloud
import difflib
import requests
from  TextSummarization import TextSummarization
import json
from flask import send_file
app = Flask(__name__)
textSum =  TextSummarization()

@app.route("/")
def index():
    return "Welcome to the page!</p>"

@app.route("/GetSummarization/")
def getVoiceData():
    return textSum.GetSummarization()

@app.route("/GetText/<string:text>")
def getTextData(text):
    return text

""" @app.route('/path')
def view_method():

    buf = StringIO()

    # generate_wav_file should take a file as parameter and write a wav in it
    #generate_wav_file(buf) 

    #response = make_response(buf.getvalue())
    #buf.close()
   
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=speech.wav'
    
    return response

@app.route('/path')
def view_method():
     path_to_file = "/speech.wav"
     with open('/apiCred.json') as f:
        credentials = json.load(f)
     x = requests.post(credentials, data = myobj)
     with open('/speech.wav', 'rb') as fobj:
         requests.post(credentials, files={'fieldname': fobj})
     return send_file(
         path_to_file, 
         mimetype="audio/wav", 
         as_attachment=True, 
         attachment_filename="speech.wav") """
