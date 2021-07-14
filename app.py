from flask import Flask, request, render_template
import numpy as np
import re
import requests

from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__)


def check(typ,output):
    url = "https://api.deepai.org/api/summarization"
    payload = {"text": output}
    print(payload)
    headers = {'api-key': 'a1d0cc1e-7051-48d1-81c2-c566ef074437'}
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    return response.json()["output"]

#home page
@app.route('/')
def home():
    return render_template('home.html')

#summarizer page
@app.route('/summarizer')
def summarizer():
    return render_template('summarizer.html')

#Result screen
@app.route('/summarize',  methods=['POST'])
def summarize():
    typ=request.form['type']
    output = request.form['output']
    if typ=="text":
        output=re.sub("[^a-zA-Z.,]"," ",output)
    print(output)
    essay = check(typ,output)
    return render_template('summary.html',essay=essay)

port=os.getenv('VCAP_APP_PORT','8080')
 
if __name__ == "__main__":
    app.secret_key=os.urandom(12)
    app.run(debug=True,host='0.0.0.0',port=port)
