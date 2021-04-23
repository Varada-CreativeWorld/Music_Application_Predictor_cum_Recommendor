import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import pickle
import os
import json
import csv


load_model = pickle.load(open('C:/Users/PC/Documents/SGP-III/my_model.pkl', 'rb'))


app = Flask(__name__)


@app.route('/')
def man():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def home():
    results=["blues","classical","country","disco","hiphop","metal","pop","reggae","rock"]
    #filename=request.form['data']
    #data = request.files['data'] 
    #filename = secure_filename(data.file)
    json_dict = request.get_json()
    filename = json_dict['file']
    audio_feature=feature_extraction(filename)
    pred_audio=load_model.predict([audio_feature])
    data=results[int(pred_audio)-1]
    return jsonify(data)


def feature_extraction(file):
    features=[]
    file_path='C:/Users/PC/Music/'+file
    (sampleRate,data) = wav.read(file_path)
    mfcc_feature = mfcc(data,sampleRate,winlen=0.020,appendEnergy = False)
    meanMatrix = mfcc_feature.mean(0)
    for x in meanMatrix:
        features.append(x)
    return features

@app.route('/recommend')
def calculate():
    file=open('C:/Users/PC/Documents/SGP-III/recommendedsongs.json')
    data=json.load(file)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
flask_cors.CORS(app, expose_headers='Authorization')





    


