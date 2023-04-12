import speech_recognition as sr
from flask import logging, Flask, render_template, request, flash
import requests
import os.path
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://bot.psgroup.xyz"}})

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        r = sr.Recognizer()
        
        audio_ex = sr.AudioFile(file)
        
        with audio_ex as source:
            audio_data = r.record(audio_ex)
        
        text = r.recognize_google(audio_data, language="en-US", show_all = False)
        
        return jsonify(text)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
